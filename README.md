# Docket2Me MCP Skill

A portable agent skill for setting up the [Docket2Me MCP server](https://docket2me.ai/) in Codex, Claude Desktop, Claude Code, Cowork, and other MCP clients.

## Install

Use the open skills CLI for Codex:

```bash
npx skills add docket2me/docket2me-skills@docket2me-install-mcp -g -a codex -y
```

Or for Claude Code:

```bash
npx skills add docket2me/docket2me-skills@docket2me-install-mcp -g -a claude-code -y
```

Or paste this into Codex or another agent:

```text
Install the Docket2Me MCP skill from https://github.com/docket2me/docket2me-skills.
Review docket2me-install-mcp/SKILL.md and referenced scripts first.
Install the docket2me-install-mcp folder into my user-level skills folder, preferably ~/.agents/skills/docket2me-install-mcp for cross-agent discovery, or the tool-specific folder for my agent.
Do not inspect or print secrets.
After installing, use $docket2me-install-mcp to configure Docket2Me and leave OAuth sign-in to the normal browser flow.
```

## What It Does

The skill gives an agent the current Docket2Me setup workflow:

- Add the remote MCP endpoint: `https://docket2me.ai/mcp`
- Configure Codex, Claude Desktop, Claude Code, Cowork, or generic MCP clients
- Use OAuth sign-in without handling passwords or stored tokens
- Verify the client connection with a low-risk Docket2Me query
- Use `mcp-remote` only when a client lacks remote MCP support

## Access

Docket2Me access is member or beta gated. This skill does not bypass access controls. It only helps configure clients that already support remote MCP and OAuth.

## Troubleshooting

If a global all-agent install prints this warning:

```text
docket2me-install-mcp -> PromptScript: PromptScript does not support global skill installation
```

the skill usually still installed for the supported agents. To avoid the warning, target the agent explicitly:

```bash
npx skills add docket2me/docket2me-skills@docket2me-install-mcp -g -a codex -y
npx skills add docket2me/docket2me-skills@docket2me-install-mcp -g -a claude-code -y
```

The skills CLI installs this skill into the selected agent's user-level skill directory.

Maintainer docs: [MAINTAINERS.md](MAINTAINERS.md)
