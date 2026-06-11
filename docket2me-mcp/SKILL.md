---
name: docket2me-mcp
description: Set up, verify, or troubleshoot the Docket2Me remote MCP server for Codex, Claude Desktop, Claude Code, Cowork, or other MCP clients. Use when the user asks to connect docket2me.ai, configure the Docket2Me MCP endpoint, add Oklahoma court research tools to an AI assistant, run Codex MCP login, add a Claude or Cowork MCP server, or bridge Docket2Me through mcp-remote.
---

# Docket2Me MCP

Configure the Docket2Me remote MCP server for AI assistants that support Streamable HTTP and OAuth. The endpoint is `https://docket2me.ai/mcp`, but refresh from the public setup page when the exact client instructions matter.

## Workflow

1. Identify the target client from the request or active environment:
   - Codex or Codex IDE extension
   - Claude (Desktop, claude.ai web, or mobile)
   - Claude Code CLI
   - Cowork
   - another MCP client

2. When network access is available, check the live setup instructions at <https://docket2me.ai/>. If the live page differs from this skill, follow the live page and mention the drift.

3. Respect access requirements. Docket2Me access is membership/beta gated. Sign-in is passwordless: the user signs in with their membership email and receives a code by email. Do not try to bypass OAuth, scrape private endpoints, inspect stored tokens, or ask the user for a password. Let the client launch the normal browser sign-in flow.

4. Apply the client-specific setup below, then run the narrowest available verification.

## Codex

Prefer the bundled helper for `~/.codex/config.toml` because it updates only the `docket2me` MCP block. Resolve `scripts/ensure_codex_mcp.py` relative to this installed skill folder:

```bash
for candidate in "$HOME/.agents/skills/docket2me-mcp" "${CODEX_HOME:-$HOME/.codex}/skills/docket2me-mcp" "$HOME/.claude/skills/docket2me-mcp"; do
  if [ -f "$candidate/scripts/ensure_codex_mcp.py" ]; then SKILL_DIR="$candidate"; break; fi
done
: "${SKILL_DIR:?Could not find installed docket2me-mcp skill folder}"
python3 "$SKILL_DIR/scripts/ensure_codex_mcp.py"
codex mcp login docket2me
```

For a dry run:

```bash
for candidate in "$HOME/.agents/skills/docket2me-mcp" "${CODEX_HOME:-$HOME/.codex}/skills/docket2me-mcp" "$HOME/.claude/skills/docket2me-mcp"; do
  if [ -f "$candidate/scripts/ensure_codex_mcp.py" ]; then SKILL_DIR="$candidate"; break; fi
done
: "${SKILL_DIR:?Could not find installed docket2me-mcp skill folder}"
python3 "$SKILL_DIR/scripts/ensure_codex_mcp.py" --dry-run
```

The intended config block is:

```toml
[mcp_servers.docket2me]
url = "https://docket2me.ai/mcp"
```

If `codex mcp login docket2me` fails, verify that the user has Docket2Me access and that the client supports remote MCP with OAuth.

### Troubleshooting: "user cancelled MCP tool call"

Symptom: Codex is configured and signed in, but every Docket2Me tool call fails with "user cancelled MCP tool call".

Cause: Codex's own approval/sandbox layer blocked the call on the user's machine. The request never reaches the server. This is not a server problem and not a sign-in problem. Updating Codex does not fix it.

Fix:

- Interactive Codex: approve the tool prompt when it appears, or allow docket2me in Codex approval settings.
- Headless `codex exec`: the default read-only sandbox cancels every MCP call. Run with a permissive sandbox flag, for example `codex exec --sandbox danger-full-access`, only if the user accepts what that flag allows.

Reference: OpenAI codex issue #24135.

## Claude — Desktop, Web & Cowork

Fastest path: the one-click install link. Have the user open it in a browser and click **Add** on the pre-filled form:

```text
https://claude.ai/customize/connectors?modal=add-custom-connector&connectorName=Docket2Me&connectorUrl=https%3A%2F%2Fdocket2me.ai%2Fmcp
```

Connectors are account-level. Adding once covers claude.ai web, Claude Desktop, Cowork, and mobile.

Manual fallback — use the UI path rather than editing hidden app config by hand:

1. Open Claude settings.
2. Go to Connectors.
3. Add a custom connector named `docket2me`.
4. Set the URL to `https://docket2me.ai/mcp`.
5. Save, then sign in with your membership email — Docket2Me emails a code.

## Claude Code CLI

Run:

```bash
claude mcp add --transport http docket2me https://docket2me.ai/mcp
```

Then open `/mcp` inside a Claude Code session, choose `docket2me`, and sign in with your membership email — Docket2Me emails a code.

## Cowork

A connector added through the one-click link above appears in Cowork automatically. Check there first.

Fallback — add it locally through the Cowork UI:

1. Open Settings.
2. Go to Tools, then MCP servers.
3. Add a Remote HTTP server named `docket2me`.
4. Set URL to `https://docket2me.ai/mcp`.
5. Set auth to OAuth, save, then sign in with your membership email — Docket2Me emails a code.

## Other MCP Clients

Use these connection values:

```text
Name: docket2me
URL: https://docket2me.ai/mcp
Transport: Streamable HTTP
Auth: OAuth 2.1 authorization code with PKCE S256
```

If the client only supports stdio, bridge through `mcp-remote`:

```bash
npx -y mcp-remote https://docket2me.ai/mcp
```

Do not add `mcp-remote` as a project dependency just to test one client unless the user explicitly asks.

## Verification

Use whichever check fits the configured client:

- Codex: confirm the config block exists, then run `codex mcp login docket2me`.
- Claude Code: run `claude mcp list` if available, or use `/mcp` in-session.
- UI clients: confirm the server appears in the MCP/connectors list and the OAuth sign-in completes.
- Any client: ask a low-risk query that should require court-data access, then confirm the assistant uses `docket2me` and returns source links.

Report the client configured, whether OAuth sign-in completed, which command or UI path was used, and any remaining access or client-support blocker.

## Resources

- <https://docket2me.ai/>: live public setup instructions.
- `scripts/ensure_codex_mcp.py`: safe Codex config helper for the `docket2me` MCP block.
