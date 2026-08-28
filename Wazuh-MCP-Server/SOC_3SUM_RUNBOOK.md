# 3-Sum APT Correlation - SOC Runbook

Operational guide for `three_sum_correlation`. Covers enabling MITRE-driven classification, reading the new engine metrics, and interpreting escalation severity.

---

## 1. Enabling MITRE-driven classification

`use_mitre` is **enabled by default** (`True`) - no action required to get `MITRE ATT&CK`-driven classification. The flag is a tool parameter, not a server-level setting.

```json
{
  "time_window_minutes": 10080,
  "threshold_score": 35,
  "z_score_threshold": 2.5,
  "use_mitre": true,
  "response_format": "json"
}
```

When `use_mitre=True`, alerts classify in priority order:

| Priority | Source | How |
|----------|--------|-----|
| 1 (primary) | `rule.mitre.tactic` | mapped to category A/B/C via `MITRE_TACTIC_TO_CATEGORY` |
| 2 (secondary) | `rule.mitre.id` | technique → tactic resolved through the MITRE ATT&CK STIX bundle (`kill_chain_phases`) |
| 3 (fallback) | `rule.groups` | only for alerts with **no** MITRE data |

**Prerequisites for reliable results**

- Wazuh rules must populate `rule.mitre.tactic` / `rule.mitre.id` on production alerts. If these fields are empty, detection silently degrades to `rule.groups` string matching (the legacy path).
- The `STIX` bundle is loaded from `MITRE_ATTACK_STIX` (default: the public `enterprise-attack.json`) and cached to `BLUETEAM_STIX_CACHE` (default `/var/log/blue-team-mcp/mitre_enterprise_attack.json`). New `ATT&CK` techniques classify automatically with no code change once the cache refreshes.

Category → tactic mapping:

| Category | Tactics | Signal |
|----------|---------|--------|
| A (**recon**) | Reconnaissance, Resource Development, Discovery | weakest (*scanner noise*) |
| B (**access**) | Initial Access, Execution, Privilege Escalation, Defense Evasion, Credential Access, Lateral Movement | mid |
| C (**C2/exfil**) | Persistence, Collection, Command and Control, Exfiltration, Impact | strongest |

---

## 2. Reading the metrics

Engine A emits two counts in its `stats` block. They measure different things:

| Metric | Meaning | Role |
|--------|---------|------|
| `multi_category_count` | srcips present in **≥2** categories (A+B, B+C, A+C, or all 3) | **this gates triggering** - the chained-attack rule |
| `intersection_count` | srcips present in **all 3** categories (A∩B∩C) | high-confidence signal, informational |

Key facts:

- `multi_category_count >= intersection_count` **always** (a 3-way hit is also a ≥2-way hit).
- An IP only becomes a trigger if it is in `multi_category_count` **and** its weighted score ≥ 35.
- A full `intersection_count` hit (all 3 categories) is the strongest possible single-IP signal treat it as a confirmed chained attack candidate even at moderate score.
- `triggers_count` is the number of IPs that actually passed the gate (the actionable set).

Example:

```json
{
  "engine_a": {
    "stats": {
      "total_unique_a": 412,
      "total_unique_b": 87,
      "total_unique_c": 23,
      "intersection_count": 2,
      "multi_category_count": 9,
      "triggers_count": 4
    }
  }
}
```

Read: 9 IPs touched ≥2 categories; 2 touched all 3; 4 of the 9 crossed the 35 threshold and became triggers. The 2 full-intersection IPs are your highest-priority leads.

---

## 3. When it escalates to HIGH / CRITICAL

There are two distinct layers.

### Layer 1 per-IP trigger (the 35 threshold)

An individual srcip triggers Engine A only when **both** hold:

1. It appears in **≥2 categories** (chained-attack gate), and
2. Its weighted score **≥ 35**.

Score = `Σ (rule.level × MITRE_TACTIC_WEIGHTS[tactic])` across that IP alerts.

Reference points (35):

| Situation | Typical score | Outcome |
|-----------|--------------|---------|
| Single C2 alert, level 12 (×2.5) | ~30 | **no trigger** (single-category, below 35) |
| Single C2 alert, level 14 (×2.5) | ~35 | borderline — still needs ≥2 categories |
| Recon (2.5) + access (13) + C2 (25) | ~40 | **trigger** (cross-category chain) |
| Two high-severity C2 alerts | ~50+ | **trigger** (multiple high-severity) |

A lone high-severity C2/Exfil alert never fires Engine A on its own the gate requires activity across at least two kill-chain categories.

### Layer 2 — unified severity (aggregate)

The final `HIGH`/`CRITICAL` verdict comes from `unified_scoring`, which counts **volume**, not the 35 score magnitude:

```
unified_score = min(engine_a_triggers + engine_b_anomalies + overlap_bonus, 10)
```

| `unified_score` | `severity` |
|----------------|------------|
| 0 | NONE |
| 1–2 | LOW |
| 3–5 | MEDIUM |
| 6–8 | **HIGH** |
| 9–10 | **CRITICAL** |

- `engine_a_triggers` - number of IPs that passed Layer 1.
- `engine_b_anomalies` - number of time-buckets where **all three** sources spiked (Z ≥ 2.5).
- `overlap_bonus` - +1 when **both** engines fired in the same window (*strongest corroboration*).

**Escalation guidance**

- `LOW` (1–2 hits): single suspicious IP or a lone Z-spike - log and watch, no immediate action.
- `MEDIUM` (3–5 hits): several IPs crossing the gate, or Engine A + Engine B both firing - start investigation (`blueteam_investigate_ip`, `blueteam_threat_card`).
- `HIGH` (6–8 hits): coordinated multi-IP or multi-source activity - active incident response.
- `CRITICAL` (9–10 hits): broad campaign, both engines corroborating - full incident declaration.
- **Regardless of severity**, an `intersection_count` hit (a true A∩B∩C IP) should be triaged immediately - it is the rarest and highest-confidence indicator the engine produces.

> Note: if the Indexer is unreachable, the result carries `"_degraded": true` and
> `severity=NONE` must be read as *unknown*, not *clean*.
