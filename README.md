# Docket2Me MCP Skill

A portable agent skill for setting up the [Docket2Me MCP server](https://docket2me.ai/) in Codex, Claude Desktop, Claude Code, Cowork, and other MCP clients.

Live install page: <https://docket2me-mcp-skill.samcarlton.workers.dev/>

## Install

Use the open skills CLI for Codex:

```bash
npx skills add ThatGuySam/docket2me-mcp-skill@docket2me-mcp -g -a codex -y
```

Or for Claude Code:

```bash
npx skills add ThatGuySam/docket2me-mcp-skill@docket2me-mcp -g -a claude-code -y
```

Or paste this into Codex or another agent:

```text
Install the Docket2Me MCP skill from https://github.com/ThatGuySam/docket2me-mcp-skill.
Review docket2me-mcp/SKILL.md and referenced scripts first.
Install the docket2me-mcp folder into my user-level skills folder, preferably ~/.agents/skills/docket2me-mcp for cross-agent discovery, or the tool-specific folder for my agent.
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

## Troubleshooting

If a global all-agent install prints this warning:

```text
docket2me-mcp -> PromptScript: PromptScript does not support global skill installation
```

the skill usually still installed for the supported agents. To avoid the warning, target the agent explicitly:

```bash
npx skills add ThatGuySam/docket2me-mcp-skill@docket2me-mcp -g -a codex -y
npx skills add ThatGuySam/docket2me-mcp-skill@docket2me-mcp -g -a claude-code -y
```

## Verify Locally

```bash
python3 docket2me-mcp/scripts/ensure_codex_mcp.py --config /tmp/codex-config.toml --dry-run
python3 -m http.server 8080 --directory docs
```

Then open `http://localhost:8080`.

The skills CLI installs this skill into the selected agent's user-level skill directory.

## Deploy to Cloudflare

```bash
wrangler deploy --config wrangler.jsonc --old-asset-ttl 0
```
