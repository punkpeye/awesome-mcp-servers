# Awesome MCP Servers ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

[![Website](https://img.shields.io/badge/Website-tensorblock.co-blue?logo=google-chrome&logoColor=white)](https://tensorblock.co)
[![Twitter](https://img.shields.io/twitter/follow/tensorblock_aoi?style=social)](https://twitter.com/tensorblock_aoi)
[![Discord](https://img.shields.io/badge/Discord-Join%20Us-5865F2?logo=discord&logoColor=white)](https://discord.gg/yefvtqDd2w)
[![🤗 Hugging Face](https://img.shields.io/badge/HuggingFace-TensorBlock-yellow?logo=huggingface&logoColor=white)](https://huggingface.co/tensorblock)
[![Telegram](https://img.shields.io/badge/Telegram-Group-blue?logo=telegram)](https://t.me/TensorBlock)

## ☁️ LagrangeCloud — Run your MCP-powered agent in the cloud

[![LagrangeCloud: Deploy your agent](https://img.shields.io/badge/LagrangeCloud-Deploy_your_agent-FF6B35?style=for-the-badge)](https://lgr.tensorblock.co/)
[![MCP50: $5 signup credit](https://img.shields.io/badge/MCP50-%245_signup_credit-2EA043?style=for-the-badge)](https://lgr.tensorblock.co/console/?coupon=MCP50)

**[LagrangeCloud](https://lgr.tensorblock.co/) · Built by TensorBlock**

Found the MCP tools for your agent? Deploy the agent you built
in Codex or Claude Code and make it available beyond your terminal.

- Bring your agent instructions, skills, scripts, and supported MCP connections.
- Call your agent through an API, embed it on your site, or run it on a schedule.
- Inspect execution traces to see what happened in each run.

> [!TIP]
> **$5 in credit for this community.** Sign up with code **MCP50** to try LagrangeCloud.

**[Sign up & get $5 credit →](https://lgr.tensorblock.co/console/?coupon=MCP50)**
· [Plugin & setup guide](https://github.com/TensorBlock/lagrange-plugins)

---

<div style="text-align: left; margin: 20px 0;">
    <a href="https://discord.com/invite/Ej5NmeHFf2" style="display: inline-block; padding: 10px 20px; background-color: #5865F2; color: white; text-decoration: none; border-radius: 5px; font-weight: bold;">
        Join the TensorBlock Discord
    </a>
</div>
TensorBlock MCP Index turns this community-curated MCP server directory into a hosted, searchable registry for agents and applications. Contributors add servers in markdown; TensorBlock normalizes the entries, generates structured profiles and install-config previews, and serves the index through a free public API.

**MCP Index website:** [https://www.tensorblock.co/mcp](https://www.tensorblock.co/mcp)

**Hosted API:** [https://mcp-index.tensorblock.co](https://mcp-index.tensorblock.co)

**Community cleanup queue:** [Help verify and improve indexed MCP servers](docs/community-cleanup-queue.md)

## MCP Maintainer Quick Start

If you maintain an MCP server, the index can give your project a public profile, install-config previews, API metadata, and a README badge.

1. Add your server in the best `docs/*.md` category, or use the [Add MCP server issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=add-mcp-server.yml).
2. Include install, transport, auth, supported clients, docs, license, endpoint, and tool details when you have them.
3. After merge, the follow-up comment gives you the public profile URL, API profile URL, install-config links, and badge markdown.
4. Add the TensorBlock MCP Index badge to your project README so users can jump back to the indexed profile.
5. Claim your profile or send metadata fixes through the [claim profile](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=claim-profile.yml) and [metadata improvement](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=improve-metadata.yml) forms. Valid profile claims and structured metadata updates generate draft metadata PRs; once reviewed, merged, and deployed, the public profile shows maintainer claim status plus install, auth, docs, license, tool, and verification metadata when available. Claim status is separate from TensorBlock verification.

## Coverage

This repo currently indexes **7,747 unique MCP server links** from the category docs. The README stays lightweight while the full directory lives in `docs/*.md`, `data/catalog.json`, and the registry MCP server.

## Community Cleanup Queue

Want to contribute without adding a new server? Start with the [MCP Index Community Cleanup Queue](docs/community-cleanup-queue.md). It links to live GitHub issue queues for good first metadata fixes, broken entries, catalog-health reports, new server submissions, client config requests, and profile claims.

Cleanup work improves the value of the hosted index: fewer duplicates, fresher source links, better install metadata, clearer categories, and more trustworthy profiles.

## How to Participate

This repo is a community directory plus a hosted index. Every useful contribution makes the MCP Index easier for people and agents to search, compare, install, and verify.

Choose the path that matches what you want to do.

**If you maintain an MCP server:**

- Share your public MCP profile from [https://www.tensorblock.co/mcp](https://www.tensorblock.co/mcp) so users can inspect metadata, install configs, source links, and badges without reading the raw markdown.
- Add your server to the best category under [Browse by Category](#browse-by-category), or use the [Add MCP server issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=add-mcp-server.yml).
- Improve your existing entry with install command, transport, auth requirements, supported clients, docs URL, license, endpoint, and tool details. Use the [metadata issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=improve-metadata.yml) if you do not want to open a PR directly; when the profile id and structured values are clear, automation drafts a metadata sidecar PR for maintainer review.
- Claim your TensorBlock MCP profile with the [claim profile issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=claim-profile.yml). Claims show community maintainer ownership metadata and do not imply TensorBlock verification.
- Add the TensorBlock MCP Index badge to your project README so users can jump from your repo to the indexed profile.

**If you build MCP clients, agents, or developer tools:**

- Use the hosted API at [https://mcp-index.tensorblock.co](https://mcp-index.tensorblock.co) to search servers, fetch normalized profiles, list categories, or generate install-config previews.
- Request another install target with the [client config issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=request-client-config.yml). Include the client name, expected config shape, example config, and official docs. Clear requests generate a draft client-config spec PR so maintainers can review the target before implementation.
- Help improve the config generator for Claude Desktop, Cursor, Codex, VS Code, and future clients.

**If you want to improve the index itself:**

- Fix duplicate, stale, broken, or poorly categorized entries. Use the [broken entry issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=report-broken-entry.yml) when you want maintainers to triage it. Clear dead-link reports can generate direct cleanup PRs, while duplicate, stale, category, safety, or unclear reports generate draft investigation PRs so cleanup work can be reviewed and tracked.
- Add missing metadata that makes search and install generation more accurate.
- Pick a scoped cleanup task from the [community cleanup queue](docs/community-cleanup-queue.md).
- Propose verification signals, ranking improvements, or better category rules. The catalog health checker also runs on a schedule to flag duplicate primary links, missing GitHub repos, archived repos, and disabled repos as broken-entry reports.
- Join the [TensorBlock Discord](https://discord.com/invite/Ej5NmeHFf2) to discuss roadmap work before opening a larger PR.

Issue forms are routed automatically. When you submit a server, metadata update, profile claim, client config request, or broken-entry report, the repo adds the right triage labels and posts the next steps so contributors and maintainers can keep the workflow moving. Server submissions with a clear category can generate draft docs PRs, structured metadata updates or profile claims can generate draft metadata PRs, clear client-config requests can generate draft spec PRs, and clear broken-entry reports can generate either direct cleanup PRs or draft investigation PRs depending on the report type.

New server submissions also get intake status labels so the queue is easier to review at scale:

- `needs-metadata` means required fields, a valid project URL, or category routing still need contributor/maintainer input.
- `duplicate` means the submitted project URL already appears in the catalog.
- `ready-for-pr` means automation created or updated a draft docs PR for maintainer review.
- `automation-blocked` means automation generated a branch but GitHub permissions blocked PR creation.

Maintainers can run **MCP Add Server Intake Refresh** from GitHub Actions to backfill or repair these labels across open server submissions. Run it with `dry_run=true` first to preview changes, then rerun with `dry_run=false` to apply them.

New server entries can be simple, but high-quality metadata makes the profile much more useful. The best entries answer:

- What can an agent do with this server?
- How does a user install or connect to it?
- Does it use `stdio`, `sse`, or `streamable-http`?
- Does it require an API key, OAuth, bearer token, or no auth?
- Which MCP clients does it support?
- Where are the setup docs, source repo, license, and public endpoint?

After a PR lands on `main`, the deploy workflow rebuilds the catalog and profiles. The hosted API and public profile pages refresh after the Railway deployment succeeds.

The scheduled catalog health check uses the generated catalog to open `catalog-health` issues for duplicate links and stale or unreachable GitHub repositories. Those issues feed back into the same broken-entry report workflow, so verified dead links can become direct cleanup PRs and ambiguous cleanup work can become reviewable investigation PRs instead of staying as loose maintainer notes.

## TensorBlock MCP Index

This repo is both a community directory and an agent-ready index. Humans add MCP servers in markdown category pages; the indexer turns those entries into structured data that agents can search, inspect, and use to draft install configs.

### Hosted MCP Index API

TensorBlock provides the MCP Index API as free community infrastructure. We contribute the compute, hosting, data normalization, and ongoing maintenance needed to make this directory usable by agents and applications without requiring every user to clone the repo or parse markdown.

Public website:

```text
https://www.tensorblock.co/mcp
```

Base URL:

```text
https://mcp-index.tensorblock.co
```

Useful endpoints:

- `GET /` - discover available endpoints and current catalog size.
- `GET /v1/categories` - list categories with entry counts and source docs.
- `GET /v1/servers?query=postgres&limit=5` - search servers by name, description, category, or URL.
- `GET /v1/servers?category=Databases&transport=stdio` - filter by category, transport, auth type, and result limit.
- `GET /v1/servers/recent?limit=12` - list recently added servers using git-derived catalog timestamps.
- `GET /v1/servers/updated?limit=12` - list recently updated entries using git-derived catalog timestamps.
- `GET /v1/servers/{id}` - fetch the normalized profile for one MCP server.
- `GET /v1/servers/{id}/badge.svg` - render a TensorBlock MCP Index badge for project READMEs.
- `GET /v1/servers/{id}/install-config?client=claude-desktop` - generate an MCP client config for Claude Desktop, Cursor, Codex, or VS Code.
- `https://tensorblock.co/mcp/servers/{id}` - share a public website profile for an indexed server.

What the API supports today:

- Search MCP servers by keyword.
- Filter by category, transport, auth type, and result limit.
- Browse recently added and recently updated servers.
- Browse all categories with entry counts.
- Fetch a normalized server profile by stable server id.
- Generate install-config previews for Claude Desktop, Cursor, Codex, and VS Code.

We want this registry to support more MCP clients and installation formats over time. If you want another client, package manager, transport, auth flow, or metadata field supported, please open an issue or PR with the expected config shape and examples.

We plan to keep investing in this hosted registry: improving metadata quality, expanding install-config coverage, adding verification signals, and keeping the service available for the MCP community. Contributors are welcome to help build the registry by adding servers, improving metadata, reporting bad entries, and proposing better search or verification workflows. When changes land on `main`, the deploy workflow rebuilds the catalog and profiles before publishing, so newly merged server entries become searchable after the Railway deployment succeeds.

How entries become index data:

1. The source of truth is the category markdown under `docs/*.md`.
2. Optional `data/server-metadata/*.json` sidecars preserve structured install, transport, auth, client, and license metadata without making the markdown entry long.
3. Each server entry is parsed from a markdown bullet with a link and description.
4. `npm run catalog:build` merges markdown entries with sidecar metadata and generates `data/catalog.json`.
5. `npm run profiles:build` generates `data/profiles/*.json` for stable per-server profiles.
6. The deploy workflow publishes the refreshed catalog to the hosted API after changes land on `main`.

For local development:

- `npm run registry:mcp` starts a local registry MCP server with `search_servers`, `get_server_profile`, and `get_install_config` tools.
- `npm run registry:api:dev` starts a local HTTP API for search, category browsing, profiles, and install configs. See [TensorBlock MCP Index API](docs/index-api.md).

Contributors still submit normal awesome-list entries, but better metadata makes each entry more useful to agents. See the [MCP Index Metadata Contribution Guide](docs/index-alpha/contribution-guide.md) for examples.

## Add or Improve an Entry

To add a new MCP server:

1. Pick the best category from [Browse by Category](#browse-by-category).
2. Open that category page under `docs/`.
3. Add one markdown bullet using this format:
   ```
   - [Server Name](https://github.com/owner/repo): Brief description of what the MCP server lets an agent do. Install: `npx your-package`.
   ```
4. Search the repo for your URL or project name to avoid duplicates.
5. Open a pull request.

If you are not sure where the server belongs, use the [Add MCP server issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=add-mcp-server.yml) and we can help route it. When the form has enough information, automation can draft a PR with both the markdown entry and a metadata sidecar.

To improve an existing server, edit the same markdown bullet where the server is listed, or use the [metadata issue form](https://github.com/TensorBlock/awesome-mcp-servers/issues/new?template=improve-metadata.yml) with the TensorBlock profile id and structured values such as `Install:`, `Transport:`, `Auth:`, `Docs URL:`, `License:`, and `Tools:`. Clear metadata issues can generate a draft sidecar PR automatically.

`data/server-metadata/*.json` files are source metadata used by the indexer. Generated files such as `data/catalog.json` and `data/profiles/*.json` are maintained by the indexer. If you only add a simple server entry, editing the relevant `docs/*.md` category page is enough for the PR.

For metadata and indexer examples, see the [MCP Index Metadata Contribution Guide](docs/index-alpha/contribution-guide.md).

For maintainers validating a metadata/indexer change:

```
npm run catalog:build
npm run profiles:build
npm test
npm run typecheck
npm run build
```

## Browse by Category

The README is now a lightweight entry point. Browse the full directory in the category pages below, or use `data/catalog.json` and the registry MCP server for agent-native search.

| Category | Listed entries | Full list |
| --- | ---: | --- |
| AI & LLM Integration | 1,632 | [Browse](docs/ai--llm-integration.md) |
| Art, Culture & Media | 82 | [Browse](docs/art-culture--media.md) |
| Browser Automation & Web Scraping | 281 | [Browse](docs/browser-automation--web-scraping.md) |
| Build & Deployment Tools | 88 | [Browse](docs/build--deployment-tools.md) |
| Cloud Platforms & Services | 373 | [Browse](docs/cloud-platforms--services.md) |
| Code Analysis & Quality | 118 | [Browse](docs/code-analysis--quality.md) |
| Code Execution | 164 | [Browse](docs/code-execution.md) |
| Communication & Messaging | 334 | [Browse](docs/communication--messaging.md) |
| Content Management Systems | 60 | [Browse](docs/content-management-systems-cms.md) |
| Data Analysis & Business Intelligence | 244 | [Browse](docs/data-analysis--business-intelligence.md) |
| Databases | 299 | [Browse](docs/databases.md) |
| Developer Productivity & Utilities | 414 | [Browse](docs/developer-productivity--utilities.md) |
| Filesystems | 56 | [Browse](docs/filesystems.md) |
| Finance & Crypto | 445 | [Browse](docs/finance--crypto.md) |
| Frameworks | 245 | [Browse](docs/frameworks.md) |
| Gaming | 108 | [Browse](docs/gaming.md) |
| Hardware & IoT | 67 | [Browse](docs/hardware--iot.md) |
| Healthcare & Life Sciences | 59 | [Browse](docs/healthcare--life-sciences.md) |
| Infrastructure | 162 | [Browse](docs/infrastructure.md) |
| Knowledge Management & Memory | 572 | [Browse](docs/knowledge-management--memory.md) |
| Location & Maps | 92 | [Browse](docs/location--maps.md) |
| Marketing, Sales & CRM | 189 | [Browse](docs/marketing-sales--crm.md) |
| Monitoring & Observability | 88 | [Browse](docs/monitoring--observability.md) |
| Multimedia Processing | 212 | [Browse](docs/multimedia-processing.md) |
| Operating System & Command Line | 107 | [Browse](docs/operating-system--command-line.md) |
| Project & Task Management | 222 | [Browse](docs/project--task-management.md) |
| Real Estate & Home Services | 3 | [Browse](docs/real-estate--home-services.md) |
| Science & Research | 118 | [Browse](docs/science--research.md) |
| Search | 172 | [Browse](docs/search.md) |
| Security | 140 | [Browse](docs/security.md) |
| Social Media & Content Platforms | 112 | [Browse](docs/social-media--content-platforms.md) |
| Sports | 3 | [Browse](docs/sport.md) |
| Travel & Transportation | 51 | [Browse](docs/travel--transportation.md) |
| Utilities & Helpers | 357 | [Browse](docs/utilities--helpers.md) |
| Version Control | 78 | [Browse](docs/version-control.md) |
