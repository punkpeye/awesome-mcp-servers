# Job Tracker MCP Server

[![M8ven Score](https://m8ven.ai/badge/mcp/ravi-d-mad-job-tracker-mcp-1q7tlo)](https://m8ven.ai/mcp/ravi-d-mad-job-tracker-mcp-1q7tlo?s=readme)

An [MCP (Model Context Protocol)](https://modelcontextprotocol.io) server built with **Java 17, Spring Boot and Spring AI** that lets an AI client such as Claude Desktop manage job applications in plain English.

> "Log an application to Infosys for Senior Java Developer"
> "Move TCS to SCREENING"
> "Which applications need a follow-up?"

The model never touches the database. It only sees the tool contract (names, descriptions, JSON schemas), and the server's Java code decides what actually happens.

<!-- Add a screenshot or GIF of Claude Desktop calling the tools here -->
<!-- ![Demo](docs/demo.gif) -->

## Tools

| Tool | Description | Parameters |
|------|-------------|------------|
| `addApplication` | Log a new job application (status `APPLIED`, follow-up set 7 days out) | `company`, `role`, `jobUrl` (optional) |
| `listApplications` | List applications, optionally filtered by status | `status` (optional) |
| `updateStatus` | Change the status of an application | `id`, `status` |
| `followUpsDue` | Applications whose follow-up date is today or earlier | none |

Statuses: `APPLIED`, `SCREENING`, `INTERVIEW`, `OFFER`, `REJECTED`.

## How it works

```
User prompt in Claude Desktop
  -> MCP client discovers tools via tools/list (names, descriptions, JSON schemas)
  -> Model picks a tool and the client sends tools/call over stdio (JSON-RPC)
  -> Spring AI routes the call to the matching @Tool method
  -> JobTools -> Spring Data JPA -> H2 database
  -> Result is serialized to JSON and returned to the model
```

## Tech stack

- Java 17
- Spring Boot 3
- Spring AI MCP Server (stdio transport)
- Spring Data JPA, H2 (file database)
- Gradle

## Getting started

### Prerequisites

- JDK 17
- Node.js (only for the MCP Inspector)
- Claude Desktop (optional, for the full demo)

### Build

```bash
./gradlew clean bootJar -x test
```

The runnable jar is created in `build/libs/`.

### Configuration

The database location is configurable through the `JOB_TRACKER_DB` environment variable and defaults to `./data/jobs`:

```properties
spring.datasource.url=jdbc:h2:file:${JOB_TRACKER_DB:./data/jobs};AUTO_SERVER=TRUE
```

Use an **absolute path** when more than one client launches the server (see "Lessons learned").

### Try it with the MCP Inspector

```bash
npx @modelcontextprotocol/inspector java -jar build/libs/job-tracker-mcp-0.0.1-SNAPSHOT.jar
```

Connect, open the **Tools** tab and run `addApplication`, then `listApplications`.

### Connect to Claude Desktop

Open Settings, Developer, **Edit Config** and add the server to the single top-level JSON object:

```json
{
  "mcpServers": {
    "job-tracker": {
      "command": "java",
      "args": ["-jar", "/absolute/path/to/build/libs/job-tracker-mcp-0.0.1-SNAPSHOT.jar"],
      "env": { "JOB_TRACKER_DB": "/absolute/path/to/job-tracker-data/jobs" }
    }
  }
}
```

Fully quit and reopen Claude Desktop. The server should show as **running** under Settings, Developer.

## Lessons learned

- **stdout belongs to the protocol.** With stdio transport, any banner or log line on stdout corrupts the JSON-RPC stream. The banner is disabled and logs go to stderr (`logback-spring.xml`).
- **Tool descriptions are part of the prompt.** The model decides when to call a tool from its description and parameter schema, so they need to be clear and specific.
- **Serialization needs getters.** Without getters on the entity, Jackson returns empty `{}` results.
- **Relative paths are fragile.** A relative database path depends on the folder that launches the process, so two clients ended up with two separate databases. A single absolute path plus H2's `AUTO_SERVER=TRUE` lets several processes share one file.

## Limitations

This is a personal, single-user tool: H2 database, no authentication, entities returned directly, and limited automated tests.

## Roadmap

- [ ] `addNote` tool and an MCP prompt template for interview prep
- [ ] MCP resource exposing a pipeline summary
- [ ] DTOs, validation and pagination for list results
- [ ] Unit and repository tests (`@DataJpaTest`)
- [ ] PostgreSQL with Flyway migrations
- [ ] Streamable HTTP transport with authentication
- [ ] Docker packaging

## License

MIT
