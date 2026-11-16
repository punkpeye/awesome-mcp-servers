import { readFileSync } from "node:fs";
import { createRequire } from "node:module";
import { describe, expect, it } from "vitest";
import type { FormatsPlugin } from "ajv-formats";
import { Ajv2020 as Ajv } from "ajv/dist/2020.js";
import { buildCatalogFromMarkdown } from "../src/buildCatalog.js";
import { slugFromUrl } from "../src/parseMarkdown.js";

const require = createRequire(import.meta.url);
const addFormats = require("ajv-formats") as FormatsPlugin;

describe("buildCatalogFromMarkdown", () => {
  it("builds README entries and flags missing docs mirrors", () => {
    const readme = [
      "## 🔎 Search",
      "- [owner/search-mcp](https://github.com/owner/search-mcp): Search tool.",
      "- [Only README](https://github.com/owner/only-readme): Missing mirror.",
    ].join("\n");

    const docs = new Map([
      [
        "docs/search.md",
        [
          "## 🔎 Search",
          "- [owner/search-mcp](https://github.com/owner/search-mcp): Search tool.",
        ].join("\n"),
      ],
    ]);

    const result = buildCatalogFromMarkdown(readme, docs);

    expect(result.entries).toHaveLength(2);
    expect(result.entries[0]?.id).toMatch(/^github-owner-search-mcp-[a-f0-9]{8}$/);
    expect(result.entries[0]?.source.docsPath).toBe("docs/search.md");
    expect(result.entries[0]?.source).toMatchObject({
      readmePath: "README.md",
      featuredInReadme: true,
    });
    expect(result.errors).toEqual([
      {
        code: "missing_docs_mirror",
        message: "Entry is present in README.md but missing from docs/search.md",
        entryId: expect.stringMatching(/^github-owner-only-readme-[a-f0-9]{8}$/),
        sourcePath: "README.md",
        line: 3,
      },
    ]);
  });

  it("uses docs as the primary catalog source and keeps README-only entries as featured supplements", () => {
    const readme = [
      "## 🔎 Search",
      "- [Featured](https://github.com/owner/featured): Featured in README.",
      "- [README Only](https://github.com/owner/readme-only): Missing mirror.",
    ].join("\n");
    const docs = new Map([
      [
        "docs/search.md",
        [
          "## 🔎 Search",
          "- [Featured](https://github.com/owner/featured): Full docs entry.",
          "- [Docs Only](https://github.com/owner/docs-only): Archived docs entry.",
        ].join("\n"),
      ],
    ]);

    const result = buildCatalogFromMarkdown(readme, docs);

    expect(result.entries.map((entry) => entry.name)).toEqual([
      "Featured",
      "Docs Only",
      "README Only",
    ]);
    expect(result.entries.map((entry) => entry.source)).toEqual([
      {
        readmePath: "README.md",
        docsPath: "docs/search.md",
        featuredInReadme: true,
      },
      {
        readmePath: null,
        docsPath: "docs/search.md",
        featuredInReadme: false,
      },
      {
        readmePath: "README.md",
        docsPath: null,
        featuredInReadme: true,
      },
    ]);
    expect(result.errors).toEqual([
      {
        code: "missing_docs_mirror",
        message: "Entry is present in README.md but missing from docs/search.md",
        entryId: expect.stringMatching(/^github-owner-readme-only-[a-f0-9]{8}$/),
        sourcePath: "README.md",
        line: 3,
      },
    ]);
  });

  it("flags duplicate URLs", () => {
    const readme = [
      "## 🔎 Search",
      "- [First](https://example.com/mcp): First entry.",
      "- [Second](https://example.com/mcp): Second entry.",
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map());

    expect(result.errors.some((error) => error.code === "duplicate_url")).toBe(true);
  });

  it("sets source.docsPath to null when a category has no docs mapping", () => {
    const readme = [
      "## Experimental",
      "- [Experimental MCP](https://example.com/experimental-mcp): Experimental server.",
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map());

    expect(result.entries).toHaveLength(1);
    expect(result.entries[0]?.source.docsPath).toBeNull();
    expect(result.errors).toEqual([]);
  });

  it("uses homepage instead of repo for non-GitHub entries", () => {
    const readme = [
      "## Experimental",
      "- [Hosted MCP](https://example.com/hosted-mcp): Hosted server.",
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map());

    expect(result.entries[0]?.links).toMatchObject({
      primary: "https://example.com/hosted-mcp",
      repo: null,
      homepage: "https://example.com/hosted-mcp",
    });
  });

  it("adds a hosted server's repository without changing its primary URL or profile id", () => {
    const projectUrl = "https://example.com/hosted-mcp";
    const id = slugFromUrl(projectUrl);
    const readme = [
      "## Experimental",
      `- [Hosted MCP](${projectUrl}): Hosted service with a separate integration repository.`,
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map(), new Map([
      [id, {
        links: {
          repo: "https://github.com/owner/integration-toolkit",
          docs: "https://example.com/docs/mcp",
          endpoint: "https://app.example.com/mcp",
        },
      }],
    ]));

    expect(result.entries).toHaveLength(1);
    expect(result.entries[0]?.id).toBe(id);
    expect(result.entries[0]?.links).toEqual({
      primary: projectUrl,
      repo: "https://github.com/owner/integration-toolkit",
      homepage: projectUrl,
      docs: "https://example.com/docs/mcp",
      endpoint: "https://app.example.com/mcp",
    });
    expect(result.errors).toEqual([]);
  });

  it("extracts only URLs that look like remote MCP endpoints", () => {
    const readme = [
      "## Experimental",
      [
        "- [Awesome MCP](https://github.com/owner/awesome):",
        "See [catalog](https://awesome-mcp.tools),",
        "Endpoint: `https://awesome-mcp.tools/mcp`.",
      ].join(" "),
      [
        "- [Post For Me](https://github.com/owner/postforme):",
        "Get started at [postforme.dev](https://www.postforme.dev),",
        "then access our [hosted server](https://mcp.postforme.dev).",
      ].join(" "),
      "- [Docs Only](https://github.com/owner/docs-only): Read docs at https://docs.example.com/setup.",
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map());

    expect(result.entries.map((entry) => entry.links.endpoint)).toEqual([
      "https://awesome-mcp.tools/mcp",
      "https://mcp.postforme.dev",
      null,
    ]);
  });

  it("reports malformed docs mirror URLs without crashing the build", () => {
    const readme = [
      "## 🔎 Search",
      "- [Valid](https://example.com/mcp): Valid server.",
    ].join("\n");
    const docs = new Map([
      [
        "docs/search.md",
        [
          "## 🔎 Search",
          "- [Bad](notaurl): Bad mirror entry.",
          "- [Valid](https://example.com/mcp): Valid server.",
        ].join("\n"),
      ],
    ]);

    const result = buildCatalogFromMarkdown(readme, docs);

    expect(result.entries).toHaveLength(1);
    expect(result.errors).toEqual([
      {
        code: "parse_error",
        message: "Invalid URL",
        sourcePath: "docs/search.md",
        line: 2,
      },
    ]);
  });

  it("infers install, auth, client, tool, and license metadata from descriptions", () => {
    const readme = [
      "## Experimental",
      [
        "- [Metadata MCP](https://example.com/metadata-mcp):",
        "Run `npx metadata-mcp` with API_KEY against any URL for OAuth-enabled Claude usage.",
        "Includes 13 tools for managing assets under MIT license.",
      ].join(" "),
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map());
    const entry = result.entries[0];

    expect(entry?.install.commands).toEqual(["npx metadata-mcp"]);
    expect(entry?.install.env).toEqual(["API_KEY"]);
    expect(entry?.install.confidence).toBe("medium");
    expect(entry?.transport).toEqual(["unknown"]);
    expect(entry?.auth.type).toBe("oauth");
    expect(entry?.clients).toEqual(["Claude"]);
    expect(entry?.tools).toEqual({
      count: 13,
      names: [],
      source: "self_reported",
    });
    expect(entry?.license).toBe("MIT");
  });

  it("applies sidecar metadata over markdown inference", () => {
    const projectUrl = "https://github.com/owner/plain-mcp";
    const id = slugFromUrl(projectUrl);
    const readme = [
      "## Experimental",
      `- [Plain MCP](${projectUrl}): Plain server entry without install metadata.`,
    ].join("\n");

    const result = buildCatalogFromMarkdown(readme, new Map(), new Map([
      [
        id,
        {
          description: "Structured sidecar description.",
          category: "Monitoring & Observability",
          links: {
            docs: "https://docs.example.com/plain-mcp",
          },
          install: {
            commands: ["npx -y plain-mcp"],
            env: ["PLAIN_API_KEY"],
            confidence: "medium",
          },
          transport: ["stdio"],
          auth: {
            type: "api-key",
            notes: ["Submitted through the add-server issue form."],
          },
          clients: ["Claude Desktop", "Cursor"],
          tools: {
            count: 2,
            names: ["inspect_project", "summarize_incidents"],
            source: "self_reported",
          },
          license: "MIT",
          verification: {
            status: "verified",
            notes: ["Maintainer relationship verified in #42."],
          },
          community: {
            maintainedBy: ["@owner"],
            verifiedBy: ["TensorBlock"],
            claimed: true,
          },
        },
      ],
    ]));
    const entry = result.entries[0];

    expect(entry?.description).toBe("Structured sidecar description.");
    expect(entry?.category).toBe("Monitoring & Observability");
    expect(entry?.links.docs).toBe("https://docs.example.com/plain-mcp");
    expect(entry?.install).toEqual({
      commands: ["npx -y plain-mcp"],
      env: ["PLAIN_API_KEY"],
      confidence: "medium",
    });
    expect(entry?.transport).toEqual(["stdio"]);
    expect(entry?.auth).toEqual({
      type: "api-key",
      notes: ["Submitted through the add-server issue form."],
    });
    expect(entry?.clients).toEqual(["Claude Desktop", "Cursor"]);
    expect(entry?.tools).toEqual({
      count: 2,
      names: ["inspect_project", "summarize_incidents"],
      source: "self_reported",
    });
    expect(entry?.license).toBe("MIT");
    expect(entry?.installReady).toBe(true);
    expect(entry?.verifiedAt).toBeNull();
    expect(entry?.verification).toEqual({
      status: "verified",
      notes: ["Maintainer relationship verified in #42."],
    });
    expect(entry?.community).toEqual({
      maintainedBy: ["@owner"],
      verifiedBy: ["TensorBlock"],
      claimed: true,
    });
  });

  it("attaches source update metadata from the entry location", () => {
    const projectUrl = "https://github.com/owner/tracked-mcp";
    const id = slugFromUrl(projectUrl);
    const readme = [
      "## 🔎 Search",
      `- [Tracked MCP](${projectUrl}): Search tool.`,
    ].join("\n");
    const docs = new Map([
      [
        "docs/search.md",
        [
          "## 🔎 Search",
          `- [Tracked MCP](${projectUrl}): Search tool.`,
        ].join("\n"),
      ],
    ]);

    const result = buildCatalogFromMarkdown(readme, docs, new Map([
      [
        id,
        {
          verification: {
            status: "verified",
          },
        },
      ],
    ]), new Map([
      [
        "docs/search.md:2",
        {
          lastUpdatedAt: "2026-06-18T12:34:56.000Z",
        },
      ],
    ]));

    expect(result.entries[0]?.source.lastUpdatedAt).toBe("2026-06-18T12:34:56.000Z");
    expect(result.entries[0]?.verifiedAt).toBe("2026-06-18T12:34:56.000Z");
  });

  it("builds entries that validate against the catalog schema", () => {
    const readme = [
      "## Experimental",
      "- [Schema MCP](https://example.com/schema-mcp): Schema-valid server.",
    ].join("\n");
    const schema = JSON.parse(readFileSync("schemas/server.schema.json", "utf8"));
    const ajv = new Ajv({ strict: false });
    addFormats(ajv);
    const validate = ajv.compile(schema);

    const result = buildCatalogFromMarkdown(readme, new Map());

    expect(validate(result.entries[0])).toBe(true);
    expect(validate.errors).toBeNull();
  });
});
