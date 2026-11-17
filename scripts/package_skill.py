#!/usr/bin/env python3
"""Build offline Simulacra Agent Skill and ChatGPT plugin archives."""
from pathlib import Path
import argparse
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = ["SKILL.md", "LICENSE.md", "UPSTREAM.md"]
EXCLUDED_DIRS = {".git", ".github", "__pycache__", "dist", "tests", ".venv"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py")], check=True)
    files = [ROOT / rel for rel in SKILL_FILES]
    for subdir in ("references", "scripts"):
        for path in sorted((ROOT / subdir).rglob("*")):
            if path.is_file() and not any(p in EXCLUDED_DIRS for p in path.relative_to(ROOT).parts) and path.suffix not in EXCLUDED_SUFFIXES:
                files.append(path)
    files = sorted(set(files))
    args.output.mkdir(parents=True, exist_ok=True)
    formats = [
        ("simulacra.skill", "simulacra/"),
        ("simulacra.zip", "simulacra/"),
        ("simulacra-chatgpt.zip", "skills/simulacra/"),
    ]
    for filename, prefix in formats:
        dest = args.output / filename
        with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in files:
                zf.write(path, prefix + path.relative_to(ROOT).as_posix())
        with zipfile.ZipFile(dest) as zf:
            assert zf.testzip() is None
            assert prefix + "SKILL.md" in zf.namelist()
            assert prefix + "references/CognitivePipeline.md" in zf.namelist()
        print(f"Built {dest} ({dest.stat().st_size:,} bytes, {len(files)} files)")
if __name__ == "__main__":
    main()
