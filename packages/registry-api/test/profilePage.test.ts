import { describe, expect, it } from "vitest";
import type { CatalogEntry } from "../../catalog-builder/src/types.js";
import { renderServerProfilePage } from "../src/profilePage.js";

const entry: CatalogEntry = {
  id: "unsafe-demo",
  name: "Unsafe <Demo>",
  description: "Server with \"quoted\" metadata and <script>alert(1)</script>.",
  category: "Utilities & Helpers",
  source: {
    readmePath: null,
    docsPath: "docs/utilities--helpers.md",
    featuredInReadme: false,
  },
  links: {
    primary: "https://github.com/example/unsafe-demo",
    repo: "javascript:alert(1)",
    homepage: null,
    docs: null,
    endpoint: null,
  },
  install: {
    commands: ["npx unsafe-demo"],
    env: ["API_KEY"],
    confidence: "medium",
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
};

describe("renderServerProfilePage", () => {
  it("labels the Codex destination and links to copyable TOML", () => {
    const html = renderServerProfilePage(entry);
    expect(html).toContain('install-config?client=codex&amp;format=toml">Codex (config.toml)</a>');
    expect(html).toContain('install-config?client=cursor">cursor</a>');
  });

  it("escapes text and blocks unsafe links", () => {
    const html = renderServerProfilePage(entry);

    expect(html).toContain("Unsafe &lt;Demo&gt;");
    expect(html).toContain("&quot;quoted&quot;");
    expect(html).toContain("&lt;script&gt;alert(1)&lt;/script&gt;");
    expect(html).not.toContain("<script>alert(1)</script>");
    expect(html).not.toContain("javascript:alert");
    expect(html).toContain('href="#"');
  });

  it("renders maintainer action links and README badge markdown", () => {
    const html = renderServerProfilePage(entry);

    expect(html).toContain("For Maintainers");
    expect(html).toContain("template=claim-profile.yml");
    expect(html).toContain("template=improve-metadata.yml");
    expect(html).toContain("template=report-broken-entry.yml");
    expect(html).toContain("template=request-client-config.yml");
    expect(html).toContain("discord.com/invite/Ej5NmeHFf2");
    expect(html).toContain("README badge");
    expect(html).toContain("Copy badge");
    expect(html).toContain("https://mcp-index.tensorblock.co/v1/servers/unsafe-demo/badge.svg");
    expect(html).toContain("https://tensorblock.co/mcp/servers/unsafe-demo");
  });

  it("renders claimed profile community metadata", () => {
    const html = renderServerProfilePage({
      ...entry,
      verification: {
        status: "verified",
        notes: ["Maintainer relationship verified in #761."],
      },
      community: {
        maintainedBy: ["@owner"],
        verifiedBy: ["TensorBlock"],
        claimed: true,
      },
    });

    expect(html).toContain("Claimed profile");
    expect(html).toContain("community maintainer");
    expect(html).toContain("Claim status is separate from TensorBlock verification");
    expect(html).toContain("<dd>Yes</dd>");
    expect(html).toContain("<code>@owner</code>");
    expect(html).toContain("<code>TensorBlock</code>");
    expect(html).toContain("<code>Maintainer relationship verified in #761.</code>");
    expect(html).not.toContain(">Claim profile</a>");
    expect(html).toContain("button primary");
    expect(html).toContain(">Improve metadata</a>");
  });
});
