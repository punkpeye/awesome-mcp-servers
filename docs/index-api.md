# TensorBlock MCP Index API

The TensorBlock MCP Index API exposes the generated catalog as HTTP JSON. It is intended for agents, clients, and lightweight integrations that need to search MCP servers or generate install configs without parsing markdown.

Hosted API:

```text
https://mcp-index.tensorblock.co
```

## Endpoints

```text
GET /
GET /health
GET /v1
GET /v1/categories
GET /v1/servers?query=&category=&transport=&auth=&limit=
GET /v1/servers/recent?limit=
GET /v1/servers/updated?limit=
GET /v1/servers/{id}
GET /v1/servers/{id}/badge.svg
GET /v1/servers/{id}/install-config?client=claude-desktop|cursor|codex|vscode
GET /v1/servers/{id}/install-config?client=codex&format=toml
```

## Examples

Discover available endpoints:

```bash
curl "$MCP_INDEX_API_URL/"
```

Check API health and deployment fingerprint:

```bash
curl "$MCP_INDEX_API_URL/health"
```

```json
{
  "status": "ok",
  "catalogEntries": 7729,
  "loadedAt": "2026-07-08T00:00:00.000Z",
  "build": {
    "commitSha": "694bc1a8c555e6d6df6dfe2ee1b04b7ae866eee5",
    "builtAt": "2026-07-08T00:11:55.000Z"
  },
  "uptimeSeconds": 60
}
```

Search for Postgres servers:

```bash
curl "$MCP_INDEX_API_URL/v1/servers?query=postgres&limit=5"
```

Filter by category and transport:

```bash
curl "$MCP_INDEX_API_URL/v1/servers?category=Databases&transport=stdio"
```

Fetch recently added servers:

```bash
curl "$MCP_INDEX_API_URL/v1/servers/recent?limit=12"
```

Fetch recently updated catalog entries:

```bash
curl "$MCP_INDEX_API_URL/v1/servers/updated?limit=12"
```

Server summaries include `sourcePullRequest` when known and `lastUpdatedAt` when the catalog builder can derive it from git history. The `recent` and `updated` collections sort by `lastUpdatedAt`, using source pull request numbers as an additional ordering signal when timestamps tie.

Fetch a full server profile:

```bash
curl "$MCP_INDEX_API_URL/v1/servers/github-crystaldba-postgres-mcp-22e80ea8"
```

Open a shareable website profile page:

```text
https://tensorblock.co/mcp/servers/github-crystaldba-postgres-mcp-22e80ea8
```

The API also keeps `GET /servers/{id}` as a lightweight HTML fallback, but the canonical community profile is hosted on the TensorBlock website.

Embed an MCP Index badge in a project README:

```markdown
[![Indexed on TensorBlock MCP Index](https://mcp-index.tensorblock.co/v1/servers/github-crystaldba-postgres-mcp-22e80ea8/badge.svg)](https://tensorblock.co/mcp/servers/github-crystaldba-postgres-mcp-22e80ea8)
```

Generate an install config:

```bash
curl "$MCP_INDEX_API_URL/v1/servers/github-crystaldba-postgres-mcp-22e80ea8/install-config?client=claude-desktop"
```

## Railway Deployment

The API is designed to run as a Railway service from this repository.

Build command:

```bash
npm run catalog:build && npm run profiles:build && npm run build
```

Start command:

```bash
npm run start
```

The service reads `data/catalog.json` on startup and keeps it in memory. Every deploy includes the latest generated catalog from the repository. No database is required for the MVP.

## Automatic Refresh

The deployment workflow runs on every push to `main` that touches the catalog, docs, API package, schema, or Railway config. It rebuilds `data/catalog.json` and `data/profiles/*.json`, writes `data/build-info.json`, and verifies the live `/health` deployment fingerprint before finishing, so newly merged server entries are reflected by the live API after the Railway deployment succeeds.

The workflow requires a GitHub repository secret named `RAILWAY_TOKEN` with deploy access to the Railway project.


### Codex config.toml output

`client=codex` keeps the existing JSON `config.mcpServers` object for API consumers
and additionally returns `nativeConfig` with `filename`, `format`, and `content`.
The content is a TOML MCP section for Codex's `config.toml`, not a whole configuration
file. Merge the section into the existing file; do not replace other settings.
See the [official Codex MCP configuration documentation](https://learn.chatgpt.com/docs/extend/mcp).

For directly copyable text, request:

```sh
curl "$MCP_INDEX_API_URL/v1/servers/github-crystaldba-postgres-mcp-22e80ea8/install-config?client=codex&format=toml"
```

This opt-in response is `text/plain; charset=utf-8`. Other client targets retain
JSON output. Unsupported format/client combinations return a JSON 400 error.
Environment values remain placeholders from the catalog; the generator does not
read local credentials, contact MCP servers, or change install-confidence scores.
