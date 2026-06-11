# Docket2Me Current Setup Snapshot

Source checked: https://docket2me.ai/ on June 10, 2026.

## Product Scope

Docket2Me exposes Oklahoma court research through an MCP server so AI assistants can pull cases, inspect dockets, watch case activity, and search court documents. Access is limited to Docket2Me members and closed beta firms.

Sign-in is passwordless. Users sign in with their membership email — Docket2Me emails them a code.

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

A browser tab opens — sign in with your membership email. We'll email you a code.

The Codex IDE extension uses the same config.

If Codex says "user cancelled MCP tool call", Codex blocked the call on your machine. Approve the tool prompt when it appears, or allow docket2me in your Codex approval settings.

## Claude — Desktop, Web & Cowork

Fastest path: the one-click install link. Open it in a browser; the connector form is pre-filled. Click Add, then sign in with your membership email — we'll email you a code.

```text
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Docket2Me&connectorUrl=https%3A%2F%2Fdocket2me.ai%2Fmcp
```

Connectors are account-level. Adding once covers claude.ai web, Claude Desktop, Cowork, and mobile.

Manual fallback: use Claude settings, then Connectors, then Add custom connector. Set:

```text
Name: docket2me
URL: https://docket2me.ai/mcp
```

Save, then sign in with your membership email — we'll email you a code.

## Claude Code CLI

Run:

```bash
claude mcp add --transport http docket2me https://docket2me.ai/mcp
```

Then run `/mcp` in a Claude Code session, choose `docket2me`, and sign in with your membership email — we'll email you a code.

## Cowork

A connector added through the one-click link above appears in Cowork automatically. Nothing more to configure.

Fallback — add it locally through the Cowork UI. Use Settings, Tools, MCP servers, then Add server. Select Remote HTTP and set:

```text
Name: docket2me
URL: https://docket2me.ai/mcp
Auth: OAuth
```

Save, then sign in with your membership email — we'll email you a code.

## Stdio Bridge

For clients without remote MCP support:

```bash
npx -y mcp-remote https://docket2me.ai/mcp
```

## Support

Use help@docket2me.com for access or setup issues.
