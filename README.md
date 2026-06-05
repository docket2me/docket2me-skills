# Docket2Me MCP Skill

A portable agent skill for setting up the [Docket2Me MCP server](https://docket2me.ai/) in Codex, Claude Desktop, Claude Code, Cowork, and other MCP clients.

## Install

Use the open skills CLI:

```bash
npx skills add ThatGuySam/docket2me-mcp-skill@docket2me-mcp -g -y
```

Or paste this into Codex or another agent:

```text
Install the Docket2Me MCP skill from https://github.com/ThatGuySam/docket2me-mcp-skill.
Review docket2me-mcp/SKILL.md and referenced scripts first.
Install the docket2me-mcp folder into my user-level skills folder, such as ~/.codex/skills/docket2me-mcp for Codex or ~/.claude/skills/docket2me-mcp for Claude.
Do not inspect or print secrets.
After installing, use $docket2me-mcp to configure Docket2Me and leave OAuth sign-in to the normal browser flow.
```

## What It Does

The skill gives an agent the current Docket2Me setup workflow:

- Add the remote MCP endpoint: `https://docket2me.ai/mcp`
- Configure Codex, Claude Desktop, Claude Code, Cowork, or generic MCP clients
- Use OAuth sign-in without handling passwords or stored tokens
- Verify the client connection with a low-risk Docket2Me query
- Use `mcp-remote` only when a client lacks remote MCP support

## Repo Layout

```text
docket2me-mcp/
  SKILL.md
  agents/openai.yaml
  references/current-setup.md
  scripts/ensure_codex_mcp.py
docs/
  index.html
  styles.css
  script.js
```

## Access

Docket2Me access is member or beta gated. This skill does not bypass access controls. It only helps configure clients that already support remote MCP and OAuth.

## Verify Locally

```bash
python3 docket2me-mcp/scripts/ensure_codex_mcp.py --config /tmp/codex-config.toml --dry-run
python3 -m http.server 8080 --directory docs
```

Then open `http://localhost:8080`.
