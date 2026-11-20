export type Transport = "stdio" | "streamable-http" | "sse" | "unknown";
export type AuthType = "none" | "api-key" | "oauth" | "bearer" | "unknown";
export type Confidence = "high" | "medium" | "low";
export type VerificationStatus = "unknown" | "self_reported" | "partial" | "verified" | "failing";

export interface CatalogSourceMetadata {
  lastUpdatedAt?: string | null;
  pullRequest?: number | null;
}

export interface CatalogEntry {
  id: string;
  name: string;
  description: string;
  category: string;
  source: {
    readmePath: string | null;
    docsPath: string | null;
    featuredInReadme: boolean;
    pullRequest?: number | null;
    lastUpdatedAt?: string | null;
  };
  links: {
    primary: string;
    repo?: string | null;
    homepage?: string | null;
    docs?: string | null;
    endpoint?: string | null;
  };
  install: {
    commands: string[];
    env: string[];
    confidence: Confidence;
  };
  transport: Transport[];
  auth: {
    type: AuthType;
    notes: string[];
  };
  clients: string[];
  tools: {
    count: number | null;
    names: string[];
    source: "self_reported" | "verified" | "unknown";
  };
  license: string;
  installReady: boolean;
  verifiedAt: string | null;
  health: {
    repoPublic: boolean | null;
    packageFound: boolean | null;
    endpointReachable: boolean | null;
    lastCheckedAt: string | null;
  };
  verification: {
    status: VerificationStatus;
    notes: string[];
  };
  community: {
    maintainedBy: string[];
    verifiedBy: string[];
    claimed: boolean;
  };
}

export interface CatalogMetadataOverride {
  id?: string;
  source?: {
    issue?: number;
    projectUrl?: string;
  };
  description?: string;
  category?: string;
  links?: Partial<Pick<CatalogEntry["links"], "repo" | "docs" | "homepage" | "endpoint">>;
  install?: Partial<CatalogEntry["install"]>;
  transport?: Transport[];
  auth?: Partial<CatalogEntry["auth"]>;
  clients?: string[];
  tools?: Partial<CatalogEntry["tools"]>;
  license?: string;
  verification?: Partial<CatalogEntry["verification"]>;
  community?: Partial<CatalogEntry["community"]>;
}

export interface ParsedMarkdownEntry {
  category: string;
  name: string;
  url: string;
  description: string;
  sourcePath: string;
  line: number;
}

export interface CatalogBuildError {
  code: "missing_docs_mirror" | "duplicate_url" | "parse_error";
  message: string;
  entryId?: string;
  sourcePath?: string;
  line?: number;
}
