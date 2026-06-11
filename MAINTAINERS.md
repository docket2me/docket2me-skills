# Maintainer Notes

Internal docs for working on this repo. Customers only need the README.

## Repo Layout

```text
docket2me-install-mcp/
  SKILL.md
  agents/openai.yaml
  scripts/ensure_codex_mcp.py
docs/
  index.html
  styles.css
  script.js
```

## Verify Locally

```bash
python3 docket2me-install-mcp/scripts/ensure_codex_mcp.py --config /tmp/codex-config.toml --dry-run
python3 -m http.server 8080 --directory docs
```

Then open `http://localhost:8080`.

## Deploy to Cloudflare

Publishes the `docs/` install page.

```bash
wrangler deploy --config wrangler.jsonc --old-asset-ttl 0
```
