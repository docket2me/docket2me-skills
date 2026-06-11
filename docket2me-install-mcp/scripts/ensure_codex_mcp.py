#!/usr/bin/env python3
"""Ensure Codex has the Docket2Me remote MCP server configured."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

SERVER_NAME = "docket2me"
SERVER_URL = "https://docket2me.ai/mcp"
SECTION_HEADER = f"[mcp_servers.{SERVER_NAME}]"
URL_LINE = f'url = "{SERVER_URL}"'
SECTION_RE = re.compile(r"^\s*\[[^\]]+\]\s*$")
TARGET_SECTION_RE = re.compile(r"^\s*\[mcp_servers\.docket2me\]\s*$")
URL_RE = re.compile(r"^\s*url\s*=")


def update_config_text(original: str) -> tuple[str, str]:
    lines = original.splitlines()
    section_start = None

    for index, line in enumerate(lines):
        if TARGET_SECTION_RE.match(line):
            section_start = index
            break

    if section_start is None:
        prefix = "\n" if lines and lines[-1].strip() else ""
        suffix = f"{SECTION_HEADER}\n{URL_LINE}\n"
        return original.rstrip("\n") + prefix + suffix, "added"

    section_end = len(lines)
    for index in range(section_start + 1, len(lines)):
        if SECTION_RE.match(lines[index]):
            section_end = index
            break

    for index in range(section_start + 1, section_end):
        if URL_RE.match(lines[index]):
            if lines[index].strip() == URL_LINE:
                return original if original.endswith("\n") else original + "\n", "unchanged"
            lines[index] = URL_LINE
            return "\n".join(lines) + "\n", "updated"

    lines.insert(section_start + 1, URL_LINE)
    return "\n".join(lines) + "\n", "updated"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Add or update the Docket2Me MCP server in Codex config.",
    )
    parser.add_argument(
        "--config",
        default=str(Path.home() / ".codex" / "config.toml"),
        help="Path to Codex config.toml.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would change without writing the file.",
    )
    args = parser.parse_args()

    config_path = Path(args.config).expanduser()
    original = config_path.read_text() if config_path.exists() else ""
    updated, status = update_config_text(original)

    if args.dry_run:
        print(f"{status}: {config_path}")
        print(SECTION_HEADER)
        print(URL_LINE)
        print(f"Next login command: codex mcp login {SERVER_NAME}")
        return 0

    if status != "unchanged":
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config_path.write_text(updated)

    print(f"{status}: {config_path}")
    print(f"Next login command: codex mcp login {SERVER_NAME}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
