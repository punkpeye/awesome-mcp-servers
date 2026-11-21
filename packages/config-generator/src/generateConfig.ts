import type { CatalogEntry, Confidence } from "../../catalog-builder/src/types.js";

export type ClientName = "claude" | "cursor" | "codex" | "vscode";

export interface GeneratedConfig {
  serverId: string;
  client: ClientName;
  confidence: Confidence;
  config: {
    mcpServers: Record<string, ServerConfig>;
  };
  nativeConfig?: {
    filename: "config.toml";
    format: "toml";
    content: string;
  };
  notes: string[];
}

type ServerConfig =
  | {
      command: string;
      args: string[];
      env?: Record<string, string>;
    }
  | {
      url: string;
    };

const PLACEHOLDER_CONFIG: ServerConfig = {
  command: "<command>",
  args: ["<args>"],
};

export const generateClientConfig = (
  entry: CatalogEntry,
  client: ClientName
): GeneratedConfig => {
  const serverConfig = buildServerConfig(entry);

  return {
    serverId: entry.id,
    client,
    confidence: entry.install.confidence,
    config: {
      mcpServers: {
        [entry.id]: serverConfig,
      },
    },
    ...(client === "codex" ? {
      nativeConfig: {
        filename: "config.toml" as const,
        format: "toml" as const,
        content: renderCodexConfig(entry.id, serverConfig),
      },
    } : {}),
    notes: [
      ...buildNotes(entry),
      ...(client === "codex" ? ["Merge this MCP section into config.toml; do not replace the whole file."] : []),
    ],
  };
};

const tomlString = (value: string): string => {
  if (/[\uD800-\uDFFF]/u.test(value)) {
    throw new Error("TOML strings must contain valid Unicode scalar values");
  }
  return JSON.stringify(value).replace(/\u007f/g, "\\u007f");
};

const renderCodexConfig = (serverId: string, config: ServerConfig): string => {
  const table = `mcp_servers.${tomlString(serverId)}`;
  const lines = [`[${table}]`];

  if ("url" in config) {
    lines.push(`url = ${tomlString(config.url)}`);
  } else {
    lines.push(`command = ${tomlString(config.command)}`);
    lines.push(`args = [${config.args.map(tomlString).join(", ")}]`);
    if (config.env && Object.keys(config.env).length > 0) {
      lines.push("", `[${table}.env]`);
      for (const [key, value] of Object.entries(config.env)) {
        lines.push(`${tomlString(key)} = ${tomlString(value)}`);
      }
    }
  }

  return `${lines.join("\n")}\n`;
};

const buildServerConfig = (entry: CatalogEntry): ServerConfig => {
  const commandParts = findLaunchCommand(entry.install.commands);

  if (commandParts) {
    const [command, ...args] = commandParts;
    const config: ServerConfig = {
      command,
      args,
    };

    if (entry.install.env.length > 0) {
      config.env = Object.fromEntries(
        entry.install.env.map((name) => [name, `<${name}>`])
      );
    }

    return config;
  }

  if (entry.links.endpoint) {
    return {
      url: entry.links.endpoint,
    };
  }

  return PLACEHOLDER_CONFIG;
};

const buildNotes = (entry: CatalogEntry): string[] => {
  const notes: string[] = [];

  if (entry.install.confidence === "low") {
    notes.push("Install confidence is low; verify this config before use.");
  }

  if (entry.auth.type === "unknown") {
    notes.push("Authentication requirements are unknown.");
  } else if (entry.auth.type !== "none") {
    notes.push(`Authentication type: ${entry.auth.type}.`);
  }

  if (entry.install.commands.length > 0 && !findLaunchCommand(entry.install.commands)) {
    notes.push("Install commands look like setup steps; provide the server launch command before use.");
  }

  return notes;
};

const findLaunchCommand = (commands: string[]): string[] | null => {
  for (const command of commands) {
    const parts = splitCommand(command);

    if (isLaunchCommand(command, parts)) {
      return parts;
    }
  }

  return null;
};

const isLaunchCommand = (command: string, parts: string[]): boolean => {
  if (parts.length === 0 || /(?:&&|\|\||[;|<>])/.test(command)) {
    return false;
  }

  const [binary, firstArg = ""] = parts;
  const normalizedBinary = binary.toLowerCase();

  const binaryName = normalizedBinary.split("/").pop();
  if (binaryName === "localcloud" || binaryName === "lc") {
    return firstArg === "mcp" && parts[2] !== "install";
  }

  if (normalizedBinary === "npx" || normalizedBinary === "uvx") {
    return true;
  }

  if (normalizedBinary === "docker") {
    return firstArg === "run";
  }

  if (normalizedBinary === "node" || normalizedBinary === "python" || normalizedBinary === "python3") {
    return true;
  }

  if (normalizedBinary === "npm") {
    return firstArg === "exec" || firstArg === "start";
  }

  return normalizedBinary.includes("mcp");
};

const splitCommand = (command: string): string[] => {
  const parts: string[] = [];
  let current = "";
  let quote: "'" | "\"" | null = null;
  let escaping = false;

  for (const char of command.trim()) {
    if (escaping) {
      current += char;
      escaping = false;
      continue;
    }

    if (char === "\\") {
      escaping = true;
      continue;
    }

    if (quote) {
      if (char === quote) {
        quote = null;
      } else {
        current += char;
      }
      continue;
    }

    if (char === "'" || char === "\"") {
      quote = char;
      continue;
    }

    if (/\s/.test(char)) {
      if (current.length > 0) {
        parts.push(current);
        current = "";
      }
      continue;
    }

    current += char;
  }

  if (escaping) {
    current += "\\";
  }

  if (current.length > 0) {
    parts.push(current);
  }

  return parts;
};
