#!/usr/bin/env python3
"""
© NAuliajati - TangerangKota-CSIRT
3-Sum APT detection - pure computation module (stdlib only)
This module MUST remain pure-computation - ``math``, ``typing``, ``ipaddress`` only. Never import ``httpx``, ``pydantic``, ``mcp``,
or ``logging``. All API/orchestration logic lives in ``engine.py`` and ``investigation.py``.
"""
from __future__ import annotations
import ipaddress
from typing import Any
from mcp_server.core.constants import MITRE_TACTIC_TO_CATEGORY, MITRE_TACTIC_WEIGHTS

# Default thresholds (Aul Tunning;P)
# threshold_score=35: with dynamic scoring (rule.level x MITRE tactic weight),
# a single high-severity C2 alert lands ~25-32 (level 12-13 x 2.5). 35 therefore
# requires either a cross-category chain or multiple high-severity alerts before
# Engine A triggers - suppresses single-alert false positives.
DEFAULT_THRESHOLD_SCORE: int = 35
DEFAULT_Z_THRESHOLD: float = 2.5
DEFAULT_WINDOW_MINUTES: int = 10080  # 7 days
DEFAULT_SPARSE_FLOOR: int = 10  # suppress single-event spikes in quiet categories
DEFAULT_SHOULDER_RATIO: float = 0.6  # adjacent-bucket Z threshold fraction

# Multi-resolution tiers for M12 slow-burn APT detection.
# Tighter thresholds on short windows (high signal-to-noise),
# looser on long windows (catch slow periodic patterns).
# Re-scaled for dynamic rule.level × tactic-weight scoring (MCP-TAXONOMY-V2):
# all tiers stay above the ~32 single-alert C2 ceiling.
_MULTI_RES_TIERS: list[dict[str, Any]] = [
    {"label": "1h",  "window_minutes": 60,    "threshold_score": 50, "z_score_threshold": 3.0},
    {"label": "24h", "window_minutes": 1440,  "threshold_score": 40, "z_score_threshold": 2.5},
    {"label": "7d",  "window_minutes": 10080, "threshold_score": 35, "z_score_threshold": 2.0},
]
_EXCLUDE_IP_FALLBACKS: set[str] = {"0.0.0.0", "unknown", ""}

# Active Response wrapper rule IDs - these duplicate the underlying alert
_DEDUP_WRAPPER_RULES: set[str] = {"606029", "651"}


# MITRE ATT&CK -> 3-Sum dynamic classification (MCP-TAXONOMY-V2) (Aul Tunning;P)
# MITRE_TACTIC_TO_CATEGORY is the PRIMARY classification engine; rule.groups
# string tokens are only a fallback for alerts lacking rule.mitre.* data.
def normalize_tactic(tactic: str) -> str:
    """Lowercase + hyphen-to-space normalization (case/format-insensitive lookup)."""
    return (tactic or "").strip().replace("-", " ").lower()


_MITRE_CATEGORY: dict[str, str] = {normalize_tactic(k): v for k, v in MITRE_TACTIC_TO_CATEGORY.items()}
_MITRE_WEIGHTS: dict[str, float] = {normalize_tactic(k): v for k, v in MITRE_TACTIC_WEIGHTS.items()}


def classify_mitre_tactic(tactic: str) -> str | None:
    """Map an ATT&CK tactic name -> 3-Sum category ('A'/'B'/'C'). None if unknown."""
    if not tactic:
        return None
    return _MITRE_CATEGORY.get(normalize_tactic(tactic))


def tactics_for_category(category: str) -> list[str]:
    """Title-case ATT&CK tactic names belonging to a 3-Sum category (for query filters)."""
    return [t for t, c in MITRE_TACTIC_TO_CATEGORY.items() if c == category]


def compute_mitre_risk(rule_level: float, tactic: str | None) -> float:
    """Dynamic risk score = rule.level x MITRE tactic weight. Unknown tactic -> weight 1.0."""
    w = _MITRE_WEIGHTS.get(normalize_tactic(tactic), 1.0) if tactic else 1.0
    return rule_level * w


def category_default_weight(category: str) -> float:
    """Mean MITRE tactic weight for a category (fallback for alerts lacking a tactic)."""
    tactics = tactics_for_category(category)
    if not tactics:
        return 1.0
    return sum(MITRE_TACTIC_WEIGHTS.get(t, 1.0) for t in tactics) / len(tactics)


def build_category_techniques(technique_tactics: dict[str, list[str]]) -> dict[str, list[str]]:
    """Derive {category: [technique IDs]} dynamically from STIX technique->tactics.
    Uses the MITRE ATT&CK STIX bundle's kill_chain_phases to resolve each technique
    to its tactics, then MITRE_TACTIC_TO_CATEGORY to bucket into A/B/C. A technique
    spanning multiple categories appears in each of its categories.
    """
    result: dict[str, list[str]] = {"A": [], "B": [], "C": []}
    for tid, tactics in technique_tactics.items():
        for t in tactics:
            cat = classify_mitre_tactic(t)
            if cat and tid not in result[cat]:
                result[cat].append(tid)
    return result


def compute_technique_risk(rule_level: float, technique_id: str,
                           technique_tactics: dict[str, list[str]],
                           category: str) -> float:
    """Risk for a technique-only alert: rule.level x max tactic weight among the
    technique's tactics that resolve to `category`. Falls back to the category mean
    weight when the technique is unknown or maps to no tactic in that category."""
    w = 0.0
    for t in technique_tactics.get((technique_id or "").strip().upper(), []):
        if classify_mitre_tactic(t) == category:
            w = max(w, compute_mitre_risk(1.0, t))
    if w <= 0.0:
        w = category_default_weight(category)
    return rule_level * w


def normalize_srcip_to_cidr(ip: str, prefix: int = 24) -> str:
    """Normalize an IP to its /24 CIDR network (opt-in grouping).
    Args:
        ip: IPv4 or IPv6 address string.
        prefix: CIDR prefix length (default 24 for IPv4).

    Returns:
        CIDR network string (e.g. ``"10.0.0.0/24"``) or the original IP string
        if it cannot be parsed.
    """
    try:
        net = ipaddress.ip_network(f"{ip}/{prefix}", strict=False)
        return str(net)
    except ValueError:
        return ip


def evaluate_engine_a(
    srcips_a: list[tuple[str, int]],
    srcips_b: list[tuple[str, int]],
    srcips_c: list[tuple[str, int]],
    threshold_score: int = DEFAULT_THRESHOLD_SCORE,
    exclude_srcips: list[str] | None = None,
    cidr_normalize: bool = False,
    cluster_map: dict[str, set[str]] | None = None,
    ppr_scores: dict[str, float] | None = None,
    ppr_boost_factor: float = 0.0,
    confirmed_ips: set[str] | None = None,
    confirmed_bonus: float = 0.0,
    cat_a_weight: float = 1.0,
    cat_b_weight: float = 1.5,
    cat_c_weight: float = 2.0,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Engine A - Multi-IoC Risk Thresholding (graph-integrated).

    Finds source IPs appearing in at least 2 alert categories (chained-attack
    gate), sums their per-category risk scores (weighted), and returns those
    exceeding ``threshold_score``. An IP concentrated in a single category never
    triggers, regardless of score (suppresses single-category false positives).

    Per-category weights default to A=1.0, B=1.5, C=2.0 - C2/Exfil (C) carries
    the most weight because it is the strongest APT signal; Recon (A) the least
    because it is common scanner noise.

    Graph integration (all optional, pure data - see ``investigation.py`` for the
    orchestrator that builds them from ``core/attack_graph.py``):
      - ``cluster_map``: {ip: {cluster member IPs}}. When given, an IP's category
        coverage is the MAX over itself and its cluster members - a campaign
        cluster spanning all 3 categories triggers even when no single IP does.
      - ``ppr_scores`` / ``ppr_boost_factor``: adds ``ppr * factor`` to the total
        for IPs ranked by suspicion propagation (0.0 disables).
      - ``confirmed_ips`` / ``confirmed_bonus``: adds a flat bonus for
        registry-confirmed attacker IOCs (0.0 disables).
    """
    exclude_set: set[str] = set(exclude_srcips or []) | _EXCLUDE_IP_FALLBACKS

    def _normalize(ip: str) -> str:
        if cidr_normalize:
            return normalize_srcip_to_cidr(ip)
        return ip

    # Build per-category dicts: {normalized_ip: max_score}
    def _build_map(entries: list[tuple[str, int]]) -> dict[str, int]:
        result: dict[str, int] = {}
        for ip, score in entries:
            if ip in exclude_set:
                continue
            norm = _normalize(ip)
            result[norm] = max(result.get(norm, 0), score)
        return result

    map_a = _build_map(srcips_a)
    map_b = _build_map(srcips_b)
    map_c = _build_map(srcips_c)

    def _coverage(cat_map: dict[str, int], ip: str) -> int:
        """Category score for ip: max over itself + cluster members."""
        score = cat_map.get(ip, 0)
        if cluster_map:
            for member in cluster_map.get(ip, ()):
                score = max(score, cat_map.get(member, 0))
        return score

    # Candidates: IPs directly observed in any category this window
    candidates = set(map_a) | set(map_b) | set(map_c)
    confirmed = confirmed_ips or set()

    triggers: list[dict[str, Any]] = []
    spanning = 0        # IPs present in all 3 categories (classic 3-Sum intersection)
    multi_category = 0  # IPs present in >= 2 categories (chained-attack gate)
    for ip in sorted(candidates):
        score_a = _coverage(map_a, ip)
        score_b = _coverage(map_b, ip)
        score_c = _coverage(map_c, ip)
        present = sum(1 for s in (score_a, score_b, score_c) if s > 0)
        if present == 3:
            spanning += 1
        if present >= 2:
            multi_category += 1
        total = score_a * cat_a_weight + score_b * cat_b_weight + score_c * cat_c_weight
        if ppr_scores and ppr_boost_factor:
            total += ppr_scores.get(ip, 0.0) * ppr_boost_factor
        if confirmed_bonus and ip in confirmed:
            total += confirmed_bonus
        # Chained-attack gate: require >= 2 distinct categories before the score
        # may trigger. A single-category burst stays silent even if score >= threshold.
        if present >= 2 and total >= threshold_score:
            triggers.append({
                "ip": ip,
                "score_a": score_a,
                "score_b": score_b,
                "score_c": score_c,
                "total": round(total, 2),
            })

    stats = {
        "total_unique_a": len(map_a),
        "total_unique_b": len(map_b),
        "total_unique_c": len(map_c),
        "intersection_count": spanning,
        "multi_category_count": multi_category,
        "triggers_count": len(triggers),
        "cluster_aware": bool(cluster_map),
    }
    return triggers, stats


def _median(values: list[float]) -> float:
    """Median of a non-empty list (stdlib-only, no numpy)."""
    s = sorted(values)
    n = len(s)
    if n % 2 == 1:
        return s[n // 2]
    return (s[n // 2 - 1] + s[n // 2]) / 2.0


def _mad(values: list[int], median: float) -> float:
    """Median Absolute Deviation (consistency factor 1.4826 for normality)."""
    abs_devs = [abs(v - median) for v in values]
    return _median(abs_devs) * 1.4826


def evaluate_engine_b(
    buckets_a: list[dict[str, Any]],
    buckets_b: list[dict[str, Any]],
    buckets_c: list[dict[str, Any]],
    z_score_threshold: float = DEFAULT_Z_THRESHOLD,
    sparse_floor: int = DEFAULT_SPARSE_FLOOR,
    use_mad: bool = False,
    shoulder_ratio: float = DEFAULT_SHOULDER_RATIO,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Engine B - 3-Source Volumetric Z-Score (sparse-guard + robust-stats aware).
    Computes rolling μ/σ (or median/MAD when ``use_mad=True``) across three
    time-bucketed alert sources and flags buckets where all three simultaneously
    exceed the Z-threshold.

    ``sparse_floor``: per-source total-event floor (default 10). A source whose
    window total is below the floor contributes Z = 0 for every bucket (its signal
    is too sparse to be statistically meaningful - prevents single-event spikes in
    quiet categories from driving detections). 0 disables the guard.

    ``use_mad``: when True, compute Z-scores using median/MAD instead of mean/stddev.
    MAD is more robust to bursty alert volumes (maintenance windows, patch cycles)
    and reduces outlier-driven false positives. Off by default.

    ``shoulder_ratio``: adjacent-bucket confirmation threshold (default 0.6).
    A Z-score spike must have at least one adjacent bucket with Z ≥ threshold ×
    shoulder_ratio. Filters single-bucket noise from log rotation / Indexer flush
    artifacts. 0 disables the shoulder check.

    Args:
        buckets_a: Category A (recon) time buckets with ``doc_count``.
        buckets_b: Category B (access anomaly) time buckets.
        buckets_c: Category C (c2/exfil) time buckets.
        z_score_threshold: Z threshold (default 2.5).
        use_mad: Use median/MAD instead of mean/stddev (default False).
        shoulder_ratio: Adjacent-bucket confirmation ratio (default 0.6).

    Returns:
        ``(anomalies, stats)`` where *anomalies* is a list of dicts with
        ``timestamp``, ``z_a``, ``z_b``, ``z_c`` and *stats* has per-source
        μ/σ/bucket counts.
    """
    def _compute(values: list[int]) -> dict[str, Any]:
        n = len(values)
        if n < 2:
            return {"mean": values[0] if values else 0.0, "stddev": 0.0,
                    "median": values[0] if values else 0.0, "mad": 0.0, "buckets": n}
        mean = sum(values) / n
        variance = sum((v - mean) ** 2 for v in values) / n
        stddev = variance ** 0.5
        med = _median([float(v) for v in values])
        mad = _mad(values, med)
        return {"mean": mean, "stddev": stddev, "median": med, "mad": mad, "buckets": n}

    def _z_scores(values: list[int], stats: dict[str, Any], use_mad_local: bool) -> list[float]:
        if use_mad_local:
            center = stats["median"]
            scale = stats["mad"]
        else:
            center = stats["mean"]
            scale = stats["stddev"]
        if scale <= 0.0001:
            return [0.0] * len(values)
        return [(v - center) / scale for v in values]

    counts_a = [b.get("doc_count", 0) for b in buckets_a]
    counts_b = [b.get("doc_count", 0) for b in buckets_b]
    counts_c = [b.get("doc_count", 0) for b in buckets_c]

    stats_a = _compute(counts_a)
    stats_b = _compute(counts_b)
    stats_c = _compute(counts_c)

    z_a = _z_scores(counts_a, stats_a, use_mad)
    z_b = _z_scores(counts_b, stats_b, use_mad)
    z_c = _z_scores(counts_c, stats_c, use_mad)

    # Sparse-category guard: sources below the total-event floor contribute Z=0
    if sparse_floor > 0:
        if sum(counts_a) < sparse_floor:
            z_a = [0.0] * len(z_a)
        if sum(counts_b) < sparse_floor:
            z_b = [0.0] * len(z_b)
        if sum(counts_c) < sparse_floor:
            z_c = [0.0] * len(z_c)

    # Find buckets where ALL THREE Z-scores exceed threshold simultaneously.
    # When shoulder_ratio > 0, additionally require at least one adjacent bucket
    # (i-1 or i+1) to have all three Z-scores at >= threshold * shoulder_ratio.
    min_len = min(len(z_a), len(z_b), len(z_c))
    timestamps = [b.get("key_as_string", b.get("key", f"b{i}"))
                  for i, b in enumerate(buckets_a[:min_len])]
    shoulder_z = z_score_threshold * shoulder_ratio if shoulder_ratio > 0 else 0.0

    anomalies: list[dict[str, Any]] = []
    for i in range(min_len):
        if z_a[i] >= z_score_threshold and z_b[i] >= z_score_threshold and z_c[i] >= z_score_threshold:
            # Shoulder confirmation: if enabled, at least one adjacent bucket must
            # also have all three Z-scores elevated (at the lower shoulder threshold)
            if shoulder_z > 0:
                left_ok = (i > 0 and z_a[i-1] >= shoulder_z
                           and z_b[i-1] >= shoulder_z and z_c[i-1] >= shoulder_z)
                right_ok = (i + 1 < min_len and z_a[i+1] >= shoulder_z
                            and z_b[i+1] >= shoulder_z and z_c[i+1] >= shoulder_z)
                if not (left_ok or right_ok):
                    continue  # isolated spike - skip
            anomalies.append({
                "timestamp": timestamps[i] if i < len(timestamps) else f"b{i}",
                "z_a": round(z_a[i], 2),
                "z_b": round(z_b[i], 2),
                "z_c": round(z_c[i], 2),
                "count_a": counts_a[i] if i < len(counts_a) else 0,
                "count_b": counts_b[i] if i < len(counts_b) else 0,
                "count_c": counts_c[i] if i < len(counts_c) else 0,
            })

    stats = {
        "source_a": {"label": "recon", "mean": round(stats_a["mean"], 2),
                      "stddev": round(stats_a["stddev"], 2),
                      "median": round(stats_a["median"], 2),
                      "mad": round(stats_a["mad"], 2),
                      "buckets": stats_a["buckets"]},
        "source_b": {"label": "access_anomaly", "mean": round(stats_b["mean"], 2),
                      "stddev": round(stats_b["stddev"], 2),
                      "median": round(stats_b["median"], 2),
                      "mad": round(stats_b["mad"], 2),
                      "buckets": stats_b["buckets"]},
        "source_c": {"label": "c2_exfil", "mean": round(stats_c["mean"], 2),
                      "stddev": round(stats_c["stddev"], 2),
                      "median": round(stats_c["median"], 2),
                      "mad": round(stats_c["mad"], 2),
                      "buckets": stats_c["buckets"]},
        "z_method": "mad" if use_mad else "zscore",
        "shoulder_ratio": shoulder_ratio,
        "anomaly_count": len(anomalies),
    }
    return anomalies, stats


def format_evaluation_dict(
    since_iso: str,
    until_iso: str,
    engine_a_results: tuple[list[dict[str, Any]], dict[str, Any]] | None = None,
    engine_b_results: tuple[list[dict[str, Any]], dict[str, Any]] | None = None,
    evaluation_time_ms: float = 0.0,
) -> dict[str, Any]:
    """Format combined Engine A + B results into a unified output dict.

    Args:
        since_iso: ISO 8601 window start.
        until_iso: ISO 8601 window end.
        engine_a_results: ``(triggers, stats)`` from :func:`evaluate_engine_a`.
        engine_b_results: ``(anomalies, stats)`` from :func:`evaluate_engine_b`.
        evaluation_time_ms: Wall-clock evaluation time in milliseconds.

    Returns:
        Structured dict with ``window``, ``engine_a``, ``engine_b``,
        ``unified_scoring``, and ``meta`` keys. Safe to serialize via ``json.dumps``.
    """
    result: dict[str, Any] = {
        "window": {"since": since_iso, "until": until_iso},
        "meta": {"evaluation_time_ms": round(evaluation_time_ms, 1)},
    }

    # Engine A
    if engine_a_results is not None:
        triggers, stats = engine_a_results
        result["engine_a"] = {"triggers": triggers, "stats": stats}
    else:
        result["engine_a"] = {"triggers": [], "stats": {}, "status": "disabled"}

    # Engine B
    if engine_b_results is not None:
        anomalies, stats = engine_b_results
        result["engine_b"] = {"anomalies": anomalies, "stats": stats}
    else:
        result["engine_b"] = {"anomalies": [], "stats": {}, "status": "disabled"}

    # Unified scoring: compute overlap and severity
    e_a_triggers = len(result["engine_a"].get("triggers", []))
    e_b_anomalies = len(result["engine_b"].get("anomalies", []))
    overlap_bonus = 1 if (e_a_triggers > 0 and e_b_anomalies > 0) else 0
    unified_score = min(e_a_triggers + e_b_anomalies + overlap_bonus, 10)

    if unified_score == 0:
        severity = "NONE"
    elif unified_score <= 2:
        severity = "LOW"
    elif unified_score <= 5:
        severity = "MEDIUM"
    elif unified_score <= 8:
        severity = "HIGH"
    else:
        severity = "CRITICAL"

    result["unified_scoring"] = {
        "engine_a_triggers": e_a_triggers,
        "engine_b_anomalies": e_b_anomalies,
        "overlap_bonus": overlap_bonus,
        "unified_score": unified_score,
        "severity": severity,
    }

    return result


def evaluate_multi_resolution(
    tier_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """Cross-tier APT persistence analysis (M12).

    Accepts 3 result dicts from :func:`format_evaluation_dict` at different
    time windows (1h / 24h / 7d) and detects attack patterns that persist
    across scales vs. transient noise at a single tier.

    Slow-burn APT: activity invisible at 1h/24h but detected at 7d.
    Burst: activity detected at 1h but absent at 24h/7d (likely noise).
    Persistent: activity detected at all 3 tiers (high confidence).

    Args:
        tier_results: List of 3 result dicts from ``format_evaluation_dict``,
                      ordered by increasing window size.

    Returns:
        Dict with ``tiers`` (per-tier summary), ``cross_tier`` (overlap analysis),
        ``slow_burn`` (7d-only triggers), and ``persistent_iocs`` (IPs flagged
        at all tiers with a srcip).
    """
    tiers: list[dict[str, Any]] = []
    all_tier_ips: list[set[str]] = []

    for r in tier_results:
        window = (r.get("window") or {})
        ea = (r.get("engine_a") or {})
        eb = (r.get("engine_b") or {})
        us = (r.get("unified_scoring") or {})
        tier_ips = {t.get("ip") for t in ea.get("triggers", []) if t.get("ip")}
        all_tier_ips.append(tier_ips)
        tiers.append({
            "window": f"{window.get('since', '?')} → {window.get('until', '?')}",
            "engine_a_triggers": ea.get("stats", {}).get("triggers_count", 0),
            "engine_b_anomalies": eb.get("stats", {}).get("anomaly_count", 0),
            "severity": us.get("severity", "NONE"),
            "unified_score": us.get("unified_score", 0),
            "trigger_ips": sorted(tier_ips)[:20],
            "_degraded": r.get("_degraded", False),
        })

    # Cross-tier IP overlap
    persistent = all_tier_ips[0] & all_tier_ips[1] & all_tier_ips[2] if len(all_tier_ips) >= 3 else set()
    slow_burn = (all_tier_ips[2] - all_tier_ips[0] - all_tier_ips[1]) if len(all_tier_ips) >= 3 else set()
    burst_only = (all_tier_ips[0] - all_tier_ips[1] - all_tier_ips[2]) if len(all_tier_ips) >= 3 else set()

    return {
        "tiers": tiers,
        "cross_tier": {
            "persistent_count": len(persistent),
            "slow_burn_count": len(slow_burn),
            "burst_only_count": len(burst_only),
        },
        "slow_burn_iocs": sorted(slow_burn)[:30],
        "persistent_iocs": sorted(persistent)[:30],
        "interpretation": (
            "persistent ({}) = detected at all 3 tiers (high confidence). "
            "slow_burn ({}) = 7d only (possible slow beacon / monthly C2). "
            "burst ({}) = 1h only (likely noise or short-lived scan)."
        ).format(len(persistent), len(slow_burn), len(burst_only)),
    }


def evaluate_baseline_drift(
    baseline_counts: list[int],
    current_counts: list[int],
    z_score_threshold: float = DEFAULT_Z_THRESHOLD,
) -> tuple[list[dict[str, Any]], dict[str, Any]]:
    """Baseline-drift anomaly detection - current buckets vs a historical baseline.

    Computes \u03bc/\u03c3 over the baseline series, Z-scores each current bucket against
    it, and flags buckets where Z >= threshold. Pure computation (stdlib only).

    Args:
        baseline_counts: Per-bucket alert counts from the historical window.
        current_counts: Per-bucket alert counts from the current window.
        z_score_threshold: Z threshold (conservative default 2.5 per Hard Rule 10).

    Returns:
        ``(anomalies, stats)`` where *anomalies* is a list of dicts with ``bucket``,
        ``count``, ``z_score`` and *stats* carries baseline \u03bc/\u03c3, totals and
        ``anomaly_count``. Zero-variance baselines yield Z = 0 (\u03c3 = 0 guard).
    """
    n = len(current_counts)
    if n < 2 or not baseline_counts:
        return [], {"status": "insufficient_data", "buckets": n}
    mean = sum(baseline_counts) / len(baseline_counts)
    variance = sum((v - mean) ** 2 for v in baseline_counts) / len(baseline_counts)
    stddev = variance ** 0.5
    if stddev <= 0.0001:
        z_scores = [0.0] * n  # \u03c3 = 0 guard - no variance, no anomaly
    else:
        z_scores = [(c - mean) / stddev for c in current_counts]
    anomalies = [
        {"bucket": i, "count": c, "z_score": round(z_scores[i], 2)}
        for i, c in enumerate(current_counts) if z_scores[i] >= z_score_threshold
    ]
    stats = {
        "baseline_mean": round(mean, 2),
        "baseline_stddev": round(stddev, 2),
        "z_score_threshold": z_score_threshold,
        "baseline_total": sum(baseline_counts),
        "current_total": sum(current_counts),
        "buckets": n,
        "anomaly_count": len(anomalies),
    }
    return anomalies, stats


def compute_time_decay_weight(
    first_seen_iso: str,
    last_seen_iso: str,
    half_life_hours: float = 168.0,
) -> float:
    """Compute a time-decay weight for an IOC based on recency.

    Uses exponential decay: weight = 2 ^ (-age / half_life).
    Recent IOCs weight closer to 1.0; IOCs older than several half-lives
    approach 0.0. Default half-life is 168 hours (7 days).

    Args:
        first_seen_iso: ISO 8601 timestamp of first observation.
        last_seen_iso: ISO 8601 timestamp of last observation (or None).
        half_life_hours: Hours after which weight halves (default 168).

    Returns:
        Float weight in [0.0, 1.0]. Returns 1.0 if timestamps cannot be parsed.
    """
    from datetime import datetime, timezone
    try:
        ts_str = last_seen_iso or first_seen_iso
        if not ts_str:
            return 1.0
        ts = datetime.fromisoformat(ts_str.replace("Z", "+00:00").rstrip("Z"))
        now = datetime.now(timezone.utc)
        age_hours = (now - ts).total_seconds() / 3600.0
        if age_hours <= 0:
            return 1.0
        return 2.0 ** (-age_hours / half_life_hours)
    except (ValueError, TypeError):
        return 1.0
