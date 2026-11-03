import type { CatalogEntry } from "../../catalog-builder/src/types.js";
import { badgeMarkdown } from "./badge.js";
import { webProfileUrl } from "./webProfile.js";

const CLIENTS = ["claude-desktop", "cursor", "codex", "vscode"] as const;
const DISCORD_URL = "https://discord.com/invite/Ej5NmeHFf2";
const ISSUE_FORM_BASE_URL = "https://github.com/TensorBlock/awesome-mcp-servers/issues/new";

export const renderServerProfilePage = (entry: CatalogEntry): string => {
  const title = `${entry.name} - TensorBlock MCP Index`;
  const profileUrl = webProfileUrl(entry.id);
  const readmeBadge = badgeMarkdown(entry, profileUrl);
  const maintainerActions = renderMaintainerActions(entry);
  const maintainerIntro = entry.community.claimed
    ? "This profile has been claimed by a community maintainer. Claim status is separate from TensorBlock verification; keep metadata current when install, auth, docs, license, or tool details change."
    : "Use this profile as the public install and metadata page for your MCP server. Claim the profile, add the badge to your README, and send metadata fixes when install or auth details change.";
  const installCommands = entry.install.commands.length > 0
    ? entry.install.commands.map((command) => `<code>${escapeHtml(command)}</code>`).join("")
    : "<p>No install command has been indexed yet.</p>";
  const envVars = entry.install.env.length > 0
    ? entry.install.env.map((name) => `<code>${escapeHtml(name)}</code>`).join(" ")
    : "<span>None indexed</span>";
  const tools = entry.tools.count === null
    ? "Unknown"
    : `${entry.tools.count}`;
  const sourceLink = entry.source.docsPath
    ? `<a href="${githubSourceUrl(entry.source.docsPath)}">${escapeHtml(entry.source.docsPath)}</a>`
    : "Not indexed";

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${escapeHtml(title)}</title>
  <meta name="description" content="${escapeAttribute(entry.description)}">
  <style>
    :root {
      color-scheme: light;
      --bg: #f7f8fb;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #5d6978;
      --line: #dde3ea;
      --accent: #2457d6;
      --accent-soft: #eef3ff;
      --code: #111827;
    }
    * { box-sizing: border-box; }
    body {
      margin: 0;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: var(--bg);
      color: var(--text);
      line-height: 1.55;
    }
    main {
      width: min(960px, calc(100% - 32px));
      margin: 0 auto;
      padding: 40px 0 56px;
    }
    header {
      margin-bottom: 24px;
    }
    .eyebrow {
      color: var(--accent);
      font-size: 13px;
      font-weight: 700;
      letter-spacing: 0;
      margin: 0 0 10px;
      text-transform: uppercase;
    }
    h1 {
      font-size: clamp(30px, 5vw, 48px);
      line-height: 1.05;
      letter-spacing: 0;
      margin: 0 0 14px;
    }
    p {
      margin: 0 0 14px;
    }
    a {
      color: var(--accent);
      text-decoration: none;
    }
    a:hover {
      text-decoration: underline;
    }
    .summary {
      color: var(--muted);
      font-size: 18px;
      max-width: 760px;
    }
    .badges {
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin-top: 18px;
    }
    .badge {
      background: var(--accent-soft);
      border: 1px solid #dbe6ff;
      border-radius: 999px;
      color: #173f9f;
      display: inline-flex;
      font-size: 13px;
      font-weight: 650;
      padding: 5px 10px;
      white-space: nowrap;
    }
    .badge.claimed {
      background: #eaf8ef;
      border-color: #c9ecd4;
      color: #17663a;
    }
    section {
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      margin-top: 16px;
      padding: 20px;
    }
    h2 {
      font-size: 18px;
      margin: 0 0 14px;
      letter-spacing: 0;
    }
    dl {
      display: grid;
      gap: 14px;
      grid-template-columns: minmax(140px, 220px) 1fr;
      margin: 0;
    }
    dt {
      color: var(--muted);
      font-weight: 650;
    }
    dd {
      margin: 0;
      min-width: 0;
      overflow-wrap: anywhere;
    }
    code {
      background: #f3f5f8;
      border: 1px solid #e1e6ee;
      border-radius: 6px;
      color: var(--code);
      display: inline-block;
      font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", monospace;
      font-size: 13px;
      margin: 0 6px 6px 0;
      padding: 3px 6px;
      white-space: pre-wrap;
      word-break: break-word;
    }
    .links {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      margin-top: 6px;
    }
    .button {
      align-items: center;
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 7px;
      color: var(--accent);
      cursor: pointer;
      display: inline-flex;
      font: inherit;
      font-weight: 650;
      min-height: 38px;
      padding: 7px 11px;
    }
    .button.primary {
      background: var(--accent);
      border-color: var(--accent);
      color: #ffffff;
    }
    .helper {
      color: var(--muted);
      max-width: 760px;
    }
    h3 {
      font-size: 15px;
      margin: 18px 0 8px;
      letter-spacing: 0;
    }
    pre {
      background: #f3f5f8;
      border: 1px solid #e1e6ee;
      border-radius: 8px;
      margin: 0;
      overflow-x: auto;
      padding: 12px;
    }
    pre code {
      background: transparent;
      border: 0;
      display: block;
      margin: 0;
      padding: 0;
      white-space: pre-wrap;
    }
    .footer {
      color: var(--muted);
      font-size: 14px;
      margin-top: 24px;
    }
    @media (max-width: 640px) {
      main {
        width: min(100% - 24px, 960px);
        padding-top: 28px;
      }
      dl {
        grid-template-columns: 1fr;
        gap: 4px;
      }
      dd {
        margin-bottom: 12px;
      }
    }
  </style>
</head>
<body>
  <main>
    <header>
      <p class="eyebrow">TensorBlock MCP Index</p>
      <h1>${escapeHtml(entry.name)}</h1>
      <p class="summary">${escapeHtml(entry.description)}</p>
      <div class="badges">
        <span class="badge">${escapeHtml(entry.category)}</span>
        <span class="badge">Install confidence: ${escapeHtml(entry.install.confidence)}</span>
        <span class="badge">Auth: ${escapeHtml(entry.auth.type)}</span>
        <span class="badge">Transport: ${escapeHtml(entry.transport.join(", "))}</span>
        ${entry.community.claimed ? '<span class="badge claimed">Claimed profile</span>' : ""}
      </div>
    </header>

    <section>
      <h2>Links</h2>
      <div class="links">
        <a class="button" href="${escapeAttribute(safeHref(entry.links.primary))}">Primary link</a>
        ${optionalLink("Repository", entry.links.repo)}
        ${optionalLink("Docs", entry.links.docs)}
        ${optionalLink("Homepage", entry.links.homepage)}
        ${optionalLink("Remote endpoint", entry.links.endpoint)}
        <a class="button" href="${escapeAttribute(profileUrl)}">Website profile</a>
        <a class="button" href="/v1/servers/${encodeURIComponent(entry.id)}">JSON profile</a>
      </div>
    </section>

    <section class="maintainer-actions">
      <h2>For Maintainers</h2>
      <p class="helper">${escapeHtml(maintainerIntro)}</p>
      <div class="links">
        ${maintainerActions}
      </div>
      <h3>README badge</h3>
      <pre><code id="readme-badge">${escapeHtml(readmeBadge)}</code></pre>
      <div class="links">
        <button class="button" type="button" data-copy-target="readme-badge">Copy badge</button>
      </div>
    </section>

    <section>
      <h2>Install Metadata</h2>
      <dl>
        <dt>Commands</dt>
        <dd>${installCommands}</dd>
        <dt>Environment</dt>
        <dd>${envVars}</dd>
        <dt>Generated configs</dt>
        <dd>${CLIENTS.map((client) => `<a href="/v1/servers/${encodeURIComponent(entry.id)}/install-config?client=${client}${client === "codex" ? "&amp;format=toml" : ""}">${client === "codex" ? "Codex (config.toml)" : client}</a>`).join(" · ")}</dd>
      </dl>
    </section>

    <section>
      <h2>Indexed Metadata</h2>
      <dl>
        <dt>Server ID</dt>
        <dd><code>${escapeHtml(entry.id)}</code></dd>
        <dt>Category</dt>
        <dd>${escapeHtml(entry.category)}</dd>
        <dt>Transport</dt>
        <dd>${escapeHtml(entry.transport.join(", "))}</dd>
        <dt>Auth</dt>
        <dd>${escapeHtml(entry.auth.type)}</dd>
        <dt>Tools</dt>
        <dd>${escapeHtml(tools)}</dd>
        <dt>License</dt>
        <dd>${escapeHtml(entry.license)}</dd>
        <dt>Verification</dt>
        <dd>${escapeHtml(entry.verification.status)}</dd>
        <dt>Verification notes</dt>
        <dd>${renderInlineValues(entry.verification.notes, "None indexed")}</dd>
        <dt>Claimed</dt>
        <dd>${entry.community.claimed ? "Yes" : "No"}</dd>
        <dt>Maintainers</dt>
        <dd>${renderInlineValues(entry.community.maintainedBy, "None indexed")}</dd>
        <dt>Verified by</dt>
        <dd>${renderInlineValues(entry.community.verifiedBy, "None indexed")}</dd>
        <dt>Source</dt>
        <dd>${sourceLink}</dd>
      </dl>
    </section>

    <p class="footer">This profile is generated from the community-maintained <a href="https://github.com/TensorBlock/awesome-mcp-servers">TensorBlock MCP Index</a>.</p>
  </main>
  <script>
    document.querySelectorAll("[data-copy-target]").forEach((button) => {
      const originalText = button.textContent;

      button.addEventListener("click", async () => {
        const target = document.getElementById(button.getAttribute("data-copy-target"));
        if (!target) return;

        try {
          await navigator.clipboard.writeText(target.textContent || "");
          button.textContent = "Copied";
        } catch {
          button.textContent = "Copy failed";
        }

        window.setTimeout(() => {
          button.textContent = originalText;
        }, 1800);
      });
    });
  </script>
</body>
</html>`;
};

const optionalLink = (label: string, href: string | null | undefined): string =>
  href
    ? `<a class="button" href="${escapeAttribute(safeHref(href))}">${escapeHtml(label)}</a>`
    : "";

const githubSourceUrl = (path: string): string =>
  `https://github.com/TensorBlock/awesome-mcp-servers/blob/main/${encodeURIComponent(path).replace(/%2F/g, "/")}`;

const renderMaintainerActions = (entry: CatalogEntry): string => {
  const claimButton = entry.community.claimed
    ? ""
    : `<a class="button primary" href="${escapeAttribute(issueFormUrl("claim-profile.yml", `Claim MCP profile: ${entry.name}`))}">Claim profile</a>`;
  const improveClass = entry.community.claimed ? "button primary" : "button";

  return [
    claimButton,
    `<a class="${improveClass}" href="${escapeAttribute(issueFormUrl("improve-metadata.yml", `Improve metadata: ${entry.name}`))}">Improve metadata</a>`,
    `<a class="button" href="${escapeAttribute(issueFormUrl("report-broken-entry.yml", `Report broken MCP entry: ${entry.name}`))}">Report issue</a>`,
    `<a class="button" href="${escapeAttribute(issueFormUrl("request-client-config.yml", `Request client config support: ${entry.name}`))}">Request client config</a>`,
    `<a class="button" href="${escapeAttribute(DISCORD_URL)}">Join Discord</a>`,
  ].filter(Boolean).join("\n        ");
};

const renderInlineValues = (values: string[], fallback: string): string =>
  values.length > 0
    ? values.map((value) => `<code>${escapeHtml(value)}</code>`).join("")
    : `<span>${escapeHtml(fallback)}</span>`;

const issueFormUrl = (template: string, title: string): string => {
  const params = new URLSearchParams({
    template,
    title,
  });

  return `${ISSUE_FORM_BASE_URL}?${params.toString()}`;
};

const escapeAttribute = (value: string): string =>
  escapeHtml(value).replace(/"/g, "&quot;");

const escapeHtml = (value: string): string =>
  value
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;");

const safeHref = (href: string): string => {
  if (href.startsWith("/") && !href.startsWith("//")) {
    return href;
  }

  try {
    const url = new URL(href);
    return url.protocol === "https:" || url.protocol === "http:"
      ? href
      : "#";
  } catch {
    return "#";
  }
};
