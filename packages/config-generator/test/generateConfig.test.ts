import { describe, expect, it } from "vitest";
import { generateClientConfig } from "../src/generateConfig.js";
import type { CatalogEntry } from "../../catalog-builder/src/types.js";
import { readFileSync } from "node:fs";
import { buildCatalogFromMarkdown } from "../../catalog-builder/src/buildCatalog.js";
import { readMetadataSidecars } from "../../catalog-builder/src/metadata.js";

const createEntry = (overrides: Partial<CatalogEntry> = {}): CatalogEntry => ({
  id: "github-owner-demo",
  name: "owner/demo",
  description: "Demo MCP server.",
  category: "Demo",
  source: {
    readmePath: "README.md",
    docsPath: null,
    featuredInReadme: true,
  },
  links: {
    primary: "https://github.com/owner/demo",
    repo: "https://github.com/owner/demo",
    homepage: null,
    docs: null,
    endpoint: null,
  },
  install: {
    commands: [],
    env: [],
    confidence: "medium",
  },
  transport: ["stdio"],
  auth: {
    type: "none",
    notes: [],
  },
  clients: [],
  tools: {
    count: null,
    names: [],
    source: "unknown",
  },
  license: "unknown",
  installReady: false,
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
  ...overrides,
});

describe("generateClientConfig", () => {
  it.each(["localcloud", "lc", "/opt/homebrew/bin/localcloud", "/home/linuxbrew/.linuxbrew/bin/localcloud"])("recognizes %s mcp as a stdio launch command", (command) => {
    const entry = createEntry({ install: { commands: [`${command} mcp`], env: [], confidence: "high" } });
    expect(generateClientConfig(entry, "cursor").config.mcpServers[entry.id]).toEqual({command, args: ["mcp"]});
  });

  it("does not launch the Cursor configuration installer as an MCP server", () => {
    const entry = createEntry({ install: { commands: ["lc mcp install --client cursor"], env: [], confidence: "low" } });
    expect(generateClientConfig(entry, "cursor").config.mcpServers[entry.id]).toEqual({command: "<command>", args: ["<args>"]});
  });

  it("generates runnable LocalCloud stdio JSON from the actual catalog entry and metadata", () => {
    const path = "docs/cloud-platforms--services.md";
    const result = buildCatalogFromMarkdown("", new Map([[path, readFileSync(path, "utf8")]]), readMetadataSidecars());
    const entry = result.entries.find(entry => entry.id === "github-localgcloud-localcloud-cli-46793d77")!;
    expect(entry.links.endpoint).toBeNull();
    expect(entry.links.docs).toBe("https://github.com/LocalGCloud/localcloud-cli#ai-agents--mcp");
    for (const client of ["claude", "cursor", "codex", "vscode"] as const) {
      const generated = generateClientConfig(entry, client);
      expect(JSON.parse(JSON.stringify(generated.config)).mcpServers[entry.id]).toEqual({command: "localcloud", args: ["mcp"]});
      expect(generated.confidence).toBe("high");
    }
  });

  it("generates Claude Desktop stdio config from install command and env", () => {
    const entry = createEntry({
      install: {
        commands: ["npx -y @owner/demo-mcp"],
        env: ["DEMO_API_KEY"],
        confidence: "medium",
      },
    });

    expect(generateClientConfig(entry, "claude")).toMatchObject({
      serverId: "github-owner-demo",
      client: "claude",
      confidence: "medium",
      config: {
        mcpServers: {
          "github-owner-demo": {
            command: "npx",
            args: ["-y", "@owner/demo-mcp"],
            env: {
              DEMO_API_KEY: "<DEMO_API_KEY>",
            },
          },
        },
      },
    });
  });

  it("generates Cursor-like remote HTTP config from endpoint when no install command exists", () => {
    const entry = createEntry({
      links: {
        primary: "https://github.com/owner/demo",
        repo: "https://github.com/owner/demo",
        homepage: null,
        docs: null,
        endpoint: "https://example.com/mcp",
      },
      install: {
        commands: [],
        env: [],
        confidence: "medium",
      },
      transport: ["streamable-http"],
    });

    expect(generateClientConfig(entry, "cursor")).toMatchObject({
      serverId: "github-owner-demo",
      client: "cursor",
      confidence: "medium",
      config: {
        mcpServers: {
          "github-owner-demo": {
            url: "https://example.com/mcp",
          },
        },
      },
    });
  });

  it("falls back when install commands are setup steps instead of launch commands", () => {
    const entry = createEntry({
      install: {
        commands: [
          "git clone https://github.com/owner/demo.git && cd demo && npm install && npm run build",
        ],
        env: [],
        confidence: "low",
      },
    });

    const config = generateClientConfig(entry, "claude");

    expect(config.config).toEqual({
      mcpServers: {
        "github-owner-demo": {
          command: "<command>",
          args: ["<args>"],
        },
      },
    });
    expect(config.notes).toContain(
      "Install commands look like setup steps; provide the server launch command before use."
    );
  });
});


describe("Codex native configuration", () => {
  it("adds a copyable MCP TOML section without replacing the legacy JSON object", () => {
    const entry = createEntry({
      links: { primary: "https://example.invalid", repo: null, homepage: null, docs: null,
        endpoint: "https://example.invalid/mcp?first=1&second=2" },
      transport: ["streamable-http"],
    });
    const generated = generateClientConfig(entry, "codex");
    expect(generated.config).toEqual({ mcpServers: {
      [entry.id]: { url: "https://example.invalid/mcp?first=1&second=2" },
    } });
    expect(generated).toHaveProperty("nativeConfig", {
      filename: "config.toml", format: "toml",
      content: '[mcp_servers."github-owner-demo"]\nurl = "https://example.invalid/mcp?first=1&second=2"\n',
    });
    expect(generateClientConfig(entry, "cursor")).not.toHaveProperty("nativeConfig");
    expect(generated.notes).toContain("Merge this MCP section into config.toml; do not replace the whole file.");
  });

  it("preserves stdio argument boundaries and keeps environment values in the env table", () => {
    const entry = createEntry({
      id: "owner.demo",
      install: { commands: ['node "path with spaces/server.js" --name "two words"'],
        env: ["DEMO.API_KEY"], confidence: "medium" },
    });
    expect(generateClientConfig(entry, "codex")).toHaveProperty("nativeConfig.content",
      '[mcp_servers."owner.demo"]\ncommand = "node"\nargs = ["path with spaces/server.js", "--name", "two words"]\n\n[mcp_servers."owner.demo".env]\n"DEMO.API_KEY" = "<DEMO.API_KEY>"\n');
  });

  it("escapes quotes, newlines and DEL without allowing a second TOML table", () => {
    const entry = createEntry({ id: 'demo"\n[other]',
      links: { primary: "https://example.invalid", repo: null, homepage: null, docs: null,
        endpoint: 'https://example.invalid/"\n\u007f' }, transport: ["streamable-http"] });
    expect(generateClientConfig(entry, "codex")).toHaveProperty("nativeConfig.content",
      '[mcp_servers."demo\\"\\n[other]"]\nurl = "https://example.invalid/\\"\\n\\u007f"\n');
  });

  it("rejects non-scalar Unicode instead of emitting invalid TOML", () => {
    const entry = createEntry({ id: "bad\ud800" });
    expect(() => generateClientConfig(entry, "codex")).toThrow("TOML strings must contain valid Unicode scalar values");
    expect(() => generateClientConfig(entry, "cursor")).not.toThrow();
  });
});
