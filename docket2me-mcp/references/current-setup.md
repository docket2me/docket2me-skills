# Docket2Me Current Setup Snapshot

Source checked: https://docket2me.ai/ on June 5, 2026.

## Product Scope

Docket2Me exposes Oklahoma court research through an MCP server so AI assistants can pull cases, inspect dockets, watch case activity, and search court documents. Access is limited to Docket2Me members and closed beta firms.

## Endpoint

```text
Server URL: https://docket2me.ai/mcp
Transport: Streamable HTTP
Auth: OAuth 2.1 authorization code with PKCE S256
OAuth discovery: https://docket2me.ai/.well-known/oauth-authorization-server
Dynamic client registration: https://docket2me.ai/register
```

## Codex

Add this to `~/.codex/config.toml`:

```toml
[mcp_servers.docket2me]
url = "https://docket2me.ai/mcp"
```

Then run:

```bash
codex mcp login docket2me
```

The Codex IDE extension uses the same config.

## Claude Desktop

Use Claude settings, then Connectors, then Add custom connector. Set:

```text
Name: docket2me
URL: https://docket2me.ai/mcp
```

Save and complete browser sign-in.

## Claude Code CLI

Run:

```bash
claude mcp add --transport http docket2me https://docket2me.ai/mcp
```

Then run `/mcp` in a Claude Code session, choose `docket2me`, and complete browser sign-in.

## Cowork

Use Settings, Tools, MCP servers, then Add server. Select Remote HTTP and set:

```text
Name: docket2me
URL: https://docket2me.ai/mcp
Auth: OAuth
```

Save and sign in.

## Stdio Bridge

For clients without remote MCP support:

```bash
npx -y mcp-remote https://docket2me.ai/mcp
```

## Support

Use help@docket2me.com for access or setup issues.
