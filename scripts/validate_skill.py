#!/usr/bin/env python3
"""Validate the standalone Simulacra skill package without third-party dependencies."""
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md", "UPSTREAM.md", "LICENSE.md",
    "references/CognitivePipeline.md", "references/Rules_Index.md",
    "references/Modules.md", "references/Main.md",
    "references/Design_QA_Protocol.md", "references/realm_data.yaml",
    "references/psychosomatic_state.json", "references/_template.md",
    "references/_log_template.yaml",
]
def main():
    missing = [path for path in REQUIRED if not (ROOT / path).is_file()]
    if missing:
        raise SystemExit("Missing required files: " + ", ".join(missing))
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    if not re.match(r"^---\nname: simulacra\n", skill):
        raise SystemExit("Invalid skill frontmatter")
    schema = json.loads((ROOT / "references/psychosomatic_state.json").read_text(encoding="utf-8"))
    assert schema.get("type") == "object"
    assert "autonomic_state" in schema.get("required", [])
    assert "priority_arbitration" in schema.get("required", [])
    print("Simulacra Skill package validated.")
if __name__ == "__main__":
    main()
