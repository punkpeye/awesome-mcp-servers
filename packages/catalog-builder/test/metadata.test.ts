import { mkdtempSync, readFileSync, rmSync, writeFileSync } from "node:fs";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { describe, expect, it } from "vitest";
import { createRequire } from "node:module";
import type { FormatsPlugin } from "ajv-formats";
import { Ajv2020 as Ajv } from "ajv/dist/2020.js";
import { readMetadataSidecars } from "../src/metadata.js";

const require = createRequire(import.meta.url);
const addFormats = require("ajv-formats") as FormatsPlugin;

describe("readMetadataSidecars", () => {
  it("returns an empty map when the metadata directory does not exist", () => {
    expect(readMetadataSidecars(join(tmpdir(), "missing-mcp-metadata-dir")).size).toBe(0);
  });

  it("loads sidecar metadata by explicit id", () => {
    const metadataDir = mkdtempSync(join(tmpdir(), "mcp-metadata-"));

    try {
      writeFileSync(
        join(metadataDir, "ignored-file-name.json"),
        JSON.stringify({
          id: "github-owner-demo-12345678",
          install: {
            commands: ["npx -y demo"],
            confidence: "medium",
          },
        }),
      );

      const metadata = readMetadataSidecars(metadataDir);

      expect(metadata.get("github-owner-demo-12345678")?.install?.commands).toEqual(["npx -y demo"]);
    } finally {
      rmSync(metadataDir, { recursive: true, force: true });
    }
  });
});

describe("server-metadata.schema.json", () => {
  it("accepts sidecars with description, category, docs, install, and tools metadata", () => {
    const schema = JSON.parse(readFileSync("schemas/server-metadata.schema.json", "utf8"));
    const ajv = new Ajv({ strict: false });
    addFormats(ajv);
    const validate = ajv.compile(schema);

    expect(validate({
      id: "github-owner-demo-mcp-12345678",
      source: {
        issue: 812,
        projectUrl: "https://github.com/owner/demo-mcp",
      },
      description: "Structured sidecar description.",
      category: "Monitoring & Observability",
      links: {
        repo: "https://github.com/owner/demo-mcp",
        docs: "https://docs.example.com/demo-mcp",
        homepage: "https://example.com/demo-mcp",
      },
      install: {
        commands: ["npx -y @owner/demo-mcp"],
        env: ["DEMO_API_KEY"],
        confidence: "medium",
      },
      tools: {
        count: 2,
        names: ["inspect_project", "summarize_incidents"],
        source: "self_reported",
      },
    })).toBe(true);
    expect(validate.errors).toBeNull();
  });
});
