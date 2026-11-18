import type {
  CatalogBuildError,
  CatalogEntry,
  CatalogMetadataOverride,
  CatalogSourceMetadata,
  ParsedMarkdownEntry,
} from "./types.js";
import { CATEGORY_TO_DOCS_PATH } from "./category-map.js";
import { parseMarkdownEntries, slugFromUrl } from "./parseMarkdown.js";

export interface CatalogBuildResult {
  entries: CatalogEntry[];
  errors: CatalogBuildError[];
}

interface NormalizedParsedEntry {
  entry: ParsedMarkdownEntry;
  normalizedUrl: string;
}

interface ParsedDocsEntries {
  entriesByPath: Map<string, NormalizedParsedEntry[]>;
  entries: NormalizedParsedEntry[];
  errors: CatalogBuildError[];
}

export function buildCatalogFromMarkdown(
  readmeMarkdown: string,
  docsByPath: Map<string, string>,
  metadataById: Map<string, CatalogMetadataOverride> = new Map(),
  sourceMetadataByLocation: Map<string, CatalogSourceMetadata> = new Map(),
): CatalogBuildResult {
  const readmeEntries = parseMarkdownEntries(readmeMarkdown, "README.md");
  const docsEntries = parseDocsEntries(docsByPath);
  const errors: CatalogBuildError[] = [...docsEntries.errors];
  const readmeEntriesByUrl = normalizeReadmeEntries(readmeEntries, errors);
  const seenUrls = new Map<string, NormalizedParsedEntry>();
  const entries: CatalogEntry[] = [];

  for (const docsEntry of docsEntries.entries) {
    const id = slugFromUrl(docsEntry.entry.url);
    const previous = seenUrls.get(docsEntry.normalizedUrl);
    if (previous) {
      errors.push({
        code: "duplicate_url",
        message: `Duplicate URL also appears at ${previous.entry.sourcePath}:${previous.entry.line}`,
        entryId: id,
        sourcePath: docsEntry.entry.sourcePath,
        line: docsEntry.entry.line,
      });
      continue;
    }

    seenUrls.set(docsEntry.normalizedUrl, docsEntry);
    entries.push(toCatalogEntry(
      docsEntry.entry,
      id,
      docsEntry.entry.sourcePath,
      readmeEntriesByUrl.has(docsEntry.normalizedUrl),
      metadataById.get(id),
      sourceMetadataByLocation.get(locationKey(docsEntry.entry)),
    ));
  }

  for (const [normalizedUrl, readmeEntry] of readmeEntriesByUrl.entries()) {
    const id = slugFromUrl(readmeEntry.url);
    const docsPath = CATEGORY_TO_DOCS_PATH[readmeEntry.category] ?? null;
    const previous = seenUrls.get(normalizedUrl);
    if (previous) {
      continue;
    }

    if (docsPath && !isMirroredInDocs(normalizedUrl, docsEntries.entriesByPath.get(docsPath) ?? [])) {
      errors.push({
        code: "missing_docs_mirror",
        message: `Entry is present in README.md but missing from ${docsPath}`,
        entryId: id,
        sourcePath: readmeEntry.sourcePath,
        line: readmeEntry.line,
      });
    }

    const normalizedEntry = { entry: readmeEntry, normalizedUrl };
    seenUrls.set(normalizedUrl, normalizedEntry);
    entries.push(toCatalogEntry(
      readmeEntry,
      id,
      null,
      true,
      metadataById.get(id),
      sourceMetadataByLocation.get(locationKey(readmeEntry)),
    ));
  }

  return { entries, errors };
}

function normalizeReadmeEntries(
  readmeEntries: ParsedMarkdownEntry[],
  errors: CatalogBuildError[],
): Map<string, ParsedMarkdownEntry> {
  const entriesByUrl = new Map<string, ParsedMarkdownEntry>();

  for (const entry of readmeEntries) {
    try {
      const normalizedUrl = normalizeUrl(entry.url);
      const previous = entriesByUrl.get(normalizedUrl);
      const id = slugFromUrl(entry.url);

      if (previous) {
        errors.push({
          code: "duplicate_url",
          message: `Duplicate URL also appears at ${previous.sourcePath}:${previous.line}`,
          entryId: id,
          sourcePath: entry.sourcePath,
          line: entry.line,
        });
      } else {
        entriesByUrl.set(normalizedUrl, entry);
      }
    } catch (error) {
      errors.push({
        code: "parse_error",
        message: error instanceof Error ? error.message : "Unable to parse README entry URL",
        sourcePath: entry.sourcePath,
        line: entry.line,
      });
    }
  }

  return entriesByUrl;
}

function parseDocsEntries(docsByPath: Map<string, string>): ParsedDocsEntries {
  const entriesByPath = new Map<string, NormalizedParsedEntry[]>();
  const errors: CatalogBuildError[] = [];

  for (const [path, markdown] of docsByPath.entries()) {
    const entries = parseMarkdownEntries(markdown, path);
    const normalizedEntries: NormalizedParsedEntry[] = [];

    for (const entry of entries) {
      try {
        const normalizedEntry = {
          entry,
          normalizedUrl: normalizeUrl(entry.url),
        };
        normalizedEntries.push(normalizedEntry);
      } catch (error) {
        errors.push({
          code: "parse_error",
          message: error instanceof Error ? error.message : "Unable to parse docs entry URL",
          sourcePath: entry.sourcePath,
          line: entry.line,
        });
      }
    }

    entriesByPath.set(path, normalizedEntries);
  }

  return { entriesByPath, entries: Array.from(entriesByPath.values()).flat(), errors };
}

function isMirroredInDocs(normalizedUrl: string, docsEntries: NormalizedParsedEntry[]): boolean {
  return docsEntries.some((docsEntry) => docsEntry.normalizedUrl === normalizedUrl);
}

function toCatalogEntry(
  entry: ParsedMarkdownEntry,
  id: string,
  docsPath: string | null,
  featuredInReadme: boolean,
  metadata: CatalogMetadataOverride | undefined,
  sourceMetadata: CatalogSourceMetadata | undefined,
): CatalogEntry {
  const repo = isGithubUrl(entry.url) ? entry.url : null;
  const installCommands = extractInstallCommands(entry.description);
  const toolCount = extractToolCount(entry.description);

  const catalogEntry: CatalogEntry = {
    id,
    name: entry.name,
    description: entry.description,
    category: entry.category,
    source: {
      readmePath: featuredInReadme ? "README.md" : null,
      docsPath,
      featuredInReadme,
      ...(sourceMetadata?.pullRequest ? { pullRequest: sourceMetadata.pullRequest } : {}),
      ...(sourceMetadata?.lastUpdatedAt ? { lastUpdatedAt: sourceMetadata.lastUpdatedAt } : {}),
    },
    links: {
      primary: entry.url,
      repo,
      homepage: repo ? null : entry.url,
      docs: null,
      endpoint: extractEndpoint(entry.description),
    },
    install: {
      commands: installCommands,
      env: extractEnvVars(entry.description),
      confidence: installCommands.length > 0 ? "medium" : "low",
    },
    transport: inferTransport(entry.description),
    auth: inferAuth(entry.description),
    clients: inferClients(entry.description),
    tools: {
      count: toolCount,
      names: [],
      source: toolCount === null ? "unknown" : "self_reported",
    },
    license: inferLicense(entry.description),
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

  return withDerivedSignals(applyMetadataOverride(catalogEntry, metadata));
}

function locationKey(entry: ParsedMarkdownEntry): string {
  return `${entry.sourcePath}:${entry.line}`;
}

function applyMetadataOverride(
  entry: CatalogEntry,
  metadata: CatalogMetadataOverride | undefined,
): CatalogEntry {
  if (!metadata) {
    return entry;
  }

  return {
    ...entry,
    description: nonEmptyString(metadata.description) ?? entry.description,
    category: nonEmptyString(metadata.category) ?? entry.category,
    links: {
      ...entry.links,
      ...(metadata.links?.repo ? { repo: metadata.links.repo } : {}),
      ...(metadata.links?.docs ? { docs: metadata.links.docs } : {}),
      ...(metadata.links?.homepage ? { homepage: metadata.links.homepage } : {}),
      ...(metadata.links?.endpoint ? { endpoint: metadata.links.endpoint } : {}),
    },
    install: {
      commands: nonEmptyArray(metadata.install?.commands) ?? entry.install.commands,
      env: metadata.install?.env ?? entry.install.env,
      confidence: metadata.install?.confidence ?? entry.install.confidence,
    },
    transport: nonEmptyArray(metadata.transport) ?? entry.transport,
    auth: metadata.auth
      ? {
          type: metadata.auth.type ?? entry.auth.type,
          notes: metadata.auth.notes ?? entry.auth.notes,
        }
      : entry.auth,
    clients: nonEmptyArray(metadata.clients) ?? entry.clients,
    tools: metadata.tools
      ? {
          count: metadata.tools.count ?? entry.tools.count,
          names: nonEmptyArray(metadata.tools.names) ?? entry.tools.names,
          source: metadata.tools.source ?? entry.tools.source,
        }
      : entry.tools,
    license: nonEmptyString(metadata.license) ?? entry.license,
    verification: metadata.verification
      ? {
          status: metadata.verification.status ?? entry.verification.status,
          notes: nonEmptyArray(metadata.verification.notes) ?? entry.verification.notes,
        }
      : entry.verification,
    community: metadata.community
      ? {
          maintainedBy: nonEmptyArray(metadata.community.maintainedBy) ?? entry.community.maintainedBy,
          verifiedBy: nonEmptyArray(metadata.community.verifiedBy) ?? entry.community.verifiedBy,
          claimed: metadata.community.claimed ?? entry.community.claimed,
        }
      : entry.community,
  };
}

function withDerivedSignals(entry: CatalogEntry): CatalogEntry {
  return {
    ...entry,
    installReady: isInstallReady(entry),
    verifiedAt: verifiedAt(entry),
  };
}

function isInstallReady(entry: CatalogEntry): boolean {
  const hasInstallTarget = entry.install.commands.length > 0 || Boolean(entry.links.endpoint);
  const hasKnownTransport = entry.transport.some((transport) => transport !== "unknown");

  return hasInstallTarget && hasKnownTransport && entry.install.confidence !== "low";
}

function verifiedAt(entry: CatalogEntry): string | null {
  if (entry.verification.status !== "verified") {
    return null;
  }

  return entry.health.lastCheckedAt ?? entry.source.lastUpdatedAt ?? null;
}

function nonEmptyArray<T extends string>(value: T[] | undefined): T[] | null {
  return value && value.length > 0 ? Array.from(new Set(value)) : null;
}

function nonEmptyString(value: string | undefined): string | null {
  const trimmed = value?.trim();
  return trimmed ? trimmed : null;
}

function normalizeUrl(url: string): string {
  const parsed = new URL(url);
  parsed.hash = "";
  parsed.protocol = parsed.protocol.toLowerCase();
  parsed.hostname = parsed.hostname.toLowerCase().replace(/^www\./, "");

  if ((parsed.protocol === "https:" && parsed.port === "443") || (parsed.protocol === "http:" && parsed.port === "80")) {
    parsed.port = "";
  }

  return parsed.toString().replace(/\/+$/, "");
}

function isGithubUrl(url: string): boolean {
  return new URL(url).hostname.toLowerCase().replace(/^www\./, "") === "github.com";
}

function extractInstallCommands(text: string): string[] {
  const commands = text.match(/`([^`]*(?:npx|uvx|pip|docker|npm)[^`]*)`/gi) ?? [];
  return unique(commands.map((command) => command.slice(1, -1).trim()).filter(Boolean));
}

function extractEnvVars(text: string): string[] {
  const matches = text.match(/\b[A-Z][A-Z0-9_]{2,}\b/g) ?? [];
  return unique(matches.filter((match) => /^.+(?:KEY|TOKEN|SECRET|PASSWORD|ENDPOINT|URL)$/.test(match)));
}

function extractEndpoint(text: string): string | null {
  const matches = text.match(/https?:\/\/[^\s`,)\]]+/gi) ?? [];
  const endpoint = matches
    .map(stripUrlPunctuation)
    .find((url) => looksLikeRemoteEndpoint(url));

  return endpoint ?? null;
}

function inferTransport(text: string): CatalogEntry["transport"] {
  const lower = text.toLowerCase();
  const transports: CatalogEntry["transport"] = [];

  if (lower.includes("stdio")) transports.push("stdio");
  if (lower.includes("streamable") || /\bhttp\b/.test(lower)) transports.push("streamable-http");
  if (/\bsse\b/.test(lower)) transports.push("sse");

  return transports.length > 0 ? transports : ["unknown"];
}

function inferAuth(text: string): CatalogEntry["auth"] {
  const lower = text.toLowerCase();

  if (lower.includes("no api key") || lower.includes("no auth")) return { type: "none", notes: [] };
  if (lower.includes("oauth")) return { type: "oauth", notes: [] };
  if (lower.includes("bearer")) return { type: "bearer", notes: [] };
  if (lower.includes("api key") || lower.includes("api-key") || /\b[A-Z][A-Z0-9_]*API_KEY\b/.test(text)) {
    return { type: "api-key", notes: [] };
  }

  return { type: "unknown", notes: [] };
}

function inferClients(text: string): string[] {
  const clientPatterns: Array<[string, RegExp]> = [
    ["Claude", /\bclaude\b/i],
    ["Cursor", /\bcursor\b/i],
    ["Codex", /\bcodex\b/i],
    ["VS Code", /\bvs\s*code\b|\bvscode\b/i],
  ];

  return clientPatterns.filter(([, pattern]) => pattern.test(text)).map(([client]) => client);
}

function extractToolCount(text: string): number | null {
  const match = text.match(/\b(\d+)\s+(?:mcp\s+)?tools?\b/i);
  return match ? Number(match[1]) : null;
}

function inferLicense(text: string): string {
  const match = text.match(/\b(MIT|Apache-2\.0|AGPL-3\.0|GPL-3\.0|BSD-3-Clause|BSD-2-Clause|ISC)\b/i);
  return match?.[1] ?? "unknown";
}

function unique(values: string[]): string[] {
  return Array.from(new Set(values));
}

function stripUrlPunctuation(url: string): string {
  return url.replace(/[.;:!?]+$/, "");
}

function looksLikeRemoteEndpoint(url: string): boolean {
  try {
    const parsed = new URL(url);
    const hostname = parsed.hostname.toLowerCase().replace(/^www\./, "");
    const pathname = parsed.pathname.toLowerCase().replace(/\/+$/, "");

    return (
      hostname.startsWith("mcp.") ||
      hostname.startsWith("sse.") ||
      pathname === "/mcp" ||
      pathname.endsWith("/mcp") ||
      pathname.startsWith("/mcp/") ||
      pathname === "/sse" ||
      pathname.endsWith("/sse") ||
      pathname.startsWith("/sse/") ||
      pathname.includes("/api/mcp")
    );
  } catch {
    return false;
  }
}
