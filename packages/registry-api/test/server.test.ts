import { once } from "node:events";
import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import type { AddressInfo } from "node:net";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { afterEach, describe, expect, it } from "vitest";
import type { CatalogEntry } from "../../catalog-builder/src/types.js";
import { createRegistryApiServer, loadBuildInfo, type BuildInfo } from "../src/server.js";

const catalog: CatalogEntry[] = [
  {
    id: "postgres-mcp",
    name: "Postgres MCP",
    description: "Query PostgreSQL databases from agents.",
    category: "Databases",
    source: {
      readmePath: null,
      docsPath: "docs/databases.md",
      featuredInReadme: false,
    },
    links: {
      primary: "https://github.com/example/postgres-mcp",
      repo: "https://github.com/example/postgres-mcp",
      homepage: null,
      docs: null,
      endpoint: null,
    },
    install: {
      commands: ["npx postgres-mcp"],
      env: ["DATABASE_URL"],
      confidence: "high",
    },
    transport: ["stdio"],
    auth: {
      type: "api-key",
      notes: [],
    },
    clients: [],
    tools: {
      count: null,
      names: [],
      source: "unknown",
    },
    license: "unknown",
    installReady: true,
    verifiedAt: null,
    health: {
      repoPublic: null,
      packageFound: null,
      endpointReachable: null,
      lastCheckedAt: null,
    },
    verification: {
      status: "unknown",
      notes: [],
    },
    community: {
      maintainedBy: [],
      verifiedBy: [],
      claimed: false,
    },
  },
];

type CatalogEntryOverrides = Partial<Omit<CatalogEntry, "source" | "links">> & {
  source?: Partial<CatalogEntry["source"]>;
  links?: Partial<CatalogEntry["links"]>;
};

const catalogEntry = (overrides: CatalogEntryOverrides): CatalogEntry => ({
  ...catalog[0],
  ...overrides,
  source: {
    ...catalog[0].source,
    ...overrides.source,
  },
  links: {
    ...catalog[0].links,
    ...overrides.links,
  },
});

const servers: Array<ReturnType<typeof createRegistryApiServer>> = [];

afterEach(async () => {
  await Promise.all(servers.splice(0).map((server) => new Promise<void>((resolve, reject) => {
    server.closeAllConnections();
    server.close((error) => {
      if (error) {
        reject(error);
        return;
      }

      resolve();
    });
  })));
});

describe("registry API server", () => {
  it("serves Codex TOML for a direct-copy request while default JSON stays available", async () => {
    const baseUrl = await startServer();
    const url = `${baseUrl}/v1/servers/postgres-mcp/install-config?client=codex`;
    const jsonResponse = await fetch(url);
    const body = await jsonResponse.json() as { config: unknown; nativeConfig: { content: string } };
    expect(jsonResponse.status).toBe(200);
    expect(body.config).toEqual({ mcpServers: { "postgres-mcp": {
      command: "npx", args: ["postgres-mcp"], env: { DATABASE_URL: "<DATABASE_URL>" },
    } } });
    const textResponse = await fetch(`${url}&format=toml`);
    expect(textResponse.status).toBe(200);
    expect(textResponse.headers.get("content-type")).toContain("text/plain");
    expect(textResponse.headers.get("access-control-allow-origin")).toBe("*");
    expect(textResponse.headers.get("cache-control")).toBe("public, max-age=60");
    expect(await textResponse.text()).toBe(body.nativeConfig.content);
  });

  it.each(["client=cursor&format=toml", "client=codex&format=yaml"])(
    "rejects unsupported install output %s", async (query) => {
      const baseUrl = await startServer();
      const response = await fetch(`${baseUrl}/v1/servers/postgres-mcp/install-config?${query}`);
      expect(response.status).toBe(400);
      expect(response.headers.get("content-type")).toContain("application/json");
    });

  it("returns API discovery from the root path", async () => {
    const baseUrl = await startServer();
    const response = await fetch(baseUrl);
    const body = await response.json() as {
      name: string;
      catalogEntries: number;
      endpoints: Record<string, string>;
    };

    expect(response.status).toBe(200);
    expect(body.name).toBe("TensorBlock MCP Index API");
    expect(body.catalogEntries).toBe(1);
    expect(body.endpoints.searchServers).toBe("/v1/servers?query=postgres&limit=5");
    expect(body.endpoints.recentServers).toBe("/v1/servers/recent?limit=12");
    expect(body.endpoints.updatedServers).toBe("/v1/servers/updated?limit=12");
    expect(body.endpoints.serverProfile).toBe("https://tensorblock.co/mcp/servers/{id}");
    expect(body.endpoints.apiHtmlProfile).toBe("/servers/{id}");
    expect(body.endpoints.badge).toBe("/v1/servers/{id}/badge.svg");
  });

  it("keeps the version discovery path available", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/v1`);
    const body = await response.json() as { version: string };

    expect(response.status).toBe(200);
    expect(body.version).toBe("v1");
  });

  it("returns build fingerprint metadata from the health endpoint", async () => {
    const build = {
      commitSha: "abc123def456",
      builtAt: "2026-07-08T00:00:00.000Z",
    };
    const baseUrl = await startServer(catalog, build);
    const response = await fetch(`${baseUrl}/health`);
    const body = await response.json() as {
      status: string;
      catalogEntries: number;
      loadedAt: string;
      build: BuildInfo;
    };

    expect(response.status).toBe(200);
    expect(body.status).toBe("ok");
    expect(body.catalogEntries).toBe(1);
    expect(body.loadedAt).toBe("2026-06-06T00:00:00.000Z");
    expect(body.build).toEqual(build);
  });

  it("loads build fingerprint metadata from JSON", () => {
    const directory = mkdtempSync(join(tmpdir(), "registry-api-build-"));
    const buildInfoPath = join(directory, "build-info.json");
    const build = {
      commitSha: "abc123def456",
      builtAt: "2026-07-08T00:00:00.000Z",
    };

    try {
      writeFileSync(buildInfoPath, `${JSON.stringify(build)}\n`, "utf8");

      expect(loadBuildInfo(buildInfoPath)).toEqual(build);
    } finally {
      rmSync(directory, { recursive: true, force: true });
    }
  });

  it("uses null build fingerprint metadata when the JSON file is missing", () => {
    const missingPath = join(tmpdir(), "missing-registry-api-build-info.json");

    expect(loadBuildInfo(missingPath)).toEqual({
      commitSha: null,
      builtAt: null,
    });
  });

  it("serves a shareable HTML profile page for a server", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/servers/postgres-mcp`);
    const body = await response.text();

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("text/html");
    expect(body).toContain("<h1>Postgres MCP</h1>");
    expect(body).toContain("Query PostgreSQL databases from agents.");
    expect(body).toContain("npx postgres-mcp");
    expect(body).toContain("https://tensorblock.co/mcp/servers/postgres-mcp");
    expect(body).toContain("/v1/servers/postgres-mcp");
    expect(body).toContain("claude-desktop");
  });

  it("serves a branded SVG badge for a server", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/v1/servers/postgres-mcp/badge.svg`);
    const body = await response.text();

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("image/svg+xml");
    expect(body).toContain("<svg");
    expect(body).toContain("TensorBlock");
    expect(body).toContain("MCP Indexed");
    expect(body).toContain("Postgres MCP is indexed on TensorBlock MCP Index");
  });

  it("serves a branded SVG badge through a unique repo slug alias", async () => {
    const baseUrl = await startServer([
      catalogEntry({
        id: "github-crystaldba-postgres-mcp-22e80ea8",
        name: "crystaldba/postgres-mcp",
        links: {
          primary: "https://github.com/crystaldba/postgres-mcp",
          repo: "https://github.com/crystaldba/postgres-mcp",
        },
      }),
    ]);
    const response = await fetch(`${baseUrl}/v1/servers/postgres-mcp/badge.svg`);
    const body = await response.text();

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("image/svg+xml");
    expect(body).toContain("crystaldba/postgres-mcp is indexed on TensorBlock MCP Index");
  });

  it("serves a fallback SVG badge for an unresolved server id", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/v1/servers/missing-server/badge.svg`);
    const body = await response.text();

    expect(response.status).toBe(200);
    expect(response.headers.get("content-type")).toContain("image/svg+xml");
    expect(body).toContain("<svg");
    expect(body).toContain("TensorBlock");
    expect(body).toContain("MCP Profile");
    expect(body).toContain("missing-server was not resolved in TensorBlock MCP Index");
  });

  it("keeps unresolved install config requests as JSON 404 errors", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/v1/servers/missing-server/install-config`);
    const body = await response.json() as { error: { message: string; statusCode: number } };

    expect(response.status).toBe(404);
    expect(response.headers.get("content-type")).toContain("application/json");
    expect(body.error).toEqual({
      message: "Server not found: missing-server",
      statusCode: 404,
    });
  });

  it("returns recently added server summaries", async () => {
    const baseUrl = await startServer([
      catalogEntry({
        id: "older-pr",
        name: "Older PR",
        source: {
          pullRequest: 10,
          lastUpdatedAt: "2026-06-18T10:00:00.000Z",
        },
      }),
      catalogEntry({
        id: "newer-pr",
        name: "Newer PR",
        source: {
          pullRequest: 42,
          lastUpdatedAt: "2026-06-01T10:00:00.000Z",
        },
      }),
      catalogEntry({
        id: "timestamp-only",
        name: "Timestamp Only",
        source: {
          lastUpdatedAt: "2026-06-20T10:00:00.000Z",
        },
      }),
    ]);
    const response = await fetch(`${baseUrl}/v1/servers/recent?limit=2`);
    const body = await response.json() as {
      count: number;
      limit: number;
      servers: Array<{ id: string; sourcePullRequest: number | null; lastUpdatedAt: string | null }>;
    };

    expect(response.status).toBe(200);
    expect(body.count).toBe(2);
    expect(body.limit).toBe(2);
    expect(body.servers.map((server) => server.id)).toEqual(["timestamp-only", "older-pr"]);
    expect(body.servers[0]).toMatchObject({
      sourcePullRequest: null,
      lastUpdatedAt: "2026-06-20T10:00:00.000Z",
    });
  });

  it("returns recently updated server summaries", async () => {
    const baseUrl = await startServer([
      catalogEntry({
        id: "older",
        name: "Older",
        source: {
          lastUpdatedAt: "2026-06-01T10:00:00.000Z",
        },
      }),
      catalogEntry({
        id: "newer",
        name: "Newer",
        source: {
          lastUpdatedAt: "2026-06-20T10:00:00.000Z",
        },
      }),
    ]);
    const response = await fetch(`${baseUrl}/v1/servers/updated?limit=1`);
    const body = await response.json() as {
      count: number;
      limit: number;
      servers: Array<{ id: string; lastUpdatedAt: string | null }>;
    };

    expect(response.status).toBe(200);
    expect(body.count).toBe(1);
    expect(body.limit).toBe(1);
    expect(body.servers).toEqual([
      expect.objectContaining({
        id: "newer",
        lastUpdatedAt: "2026-06-20T10:00:00.000Z",
      }),
    ]);
  });

  it("returns JSON errors for missing profile pages", async () => {
    const baseUrl = await startServer();
    const response = await fetch(`${baseUrl}/servers/missing`);
    const body = await response.json() as { error: { message: string; statusCode: number } };

    expect(response.status).toBe(404);
    expect(body.error.statusCode).toBe(404);
    expect(body.error.message).toBe("Server not found: missing");
  });
});

const startServer = async (
  entries = catalog,
  build: BuildInfo = {
    commitSha: null,
    builtAt: null,
  }
): Promise<string> => {
  const server = createRegistryApiServer({
    catalog: entries,
    loadedAt: "2026-06-06T00:00:00.000Z",
    build,
  });
  servers.push(server);
  server.listen(0, "127.0.0.1");
  await once(server, "listening");

  const address = server.address() as AddressInfo;
  return `http://127.0.0.1:${address.port}`;
};
