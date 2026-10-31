# Claude Code contract: awesome-mcp-servers

Read [AGENTS.md](AGENTS.md) first. OpenViking memory project id: `awesome-mcp-servers`.

## Anti-Hallucination Canonical Loop

1. **Canon First:** AGENTS.md + `npm run session:context` (when defined) + one bounded OpenViking recall (<=700 tok, limit=3, project=`awesome-mcp-servers`).
2. **Execute and baseline verify:** PLAN -> BUILD -> DIFF -> QA -> APPROVAL -> APPLY -> DOCS; run tests and review session errors.
3. **Periodic audit:** Repeated failures or high token use trigger canonical rule and skill updates.
4. **Subagent delegation:** Read-only multi-file work to `.claude/agents/fast-researcher.md` (haiku); pre-APPLY review to `.claude/agents/code-reviewer.md` (sonnet); delegate summaries <=90 lines.
5. **Closeout:** `npm --prefix ~/@github/ai run session:closeout -- "<topic>" "<verdict>" --project awesome-mcp-servers`.

Operator chat: Lithuanian. Code, comments, and commits: English. No emoji.
