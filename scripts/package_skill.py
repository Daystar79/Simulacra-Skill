#!/usr/bin/env python3
"""Build portable, offline Simulacra .skill and .zip packages."""
from pathlib import Path
import argparse
import json
import subprocess
import sys
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = [
    "SKILL.md",
    "LICENSE.md",
    "UPSTREAM.md",
]
EXCLUDED_DIRS = {".git", ".github", "__pycache__", "dist", "tests", ".venv"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo"}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, default=ROOT / "dist")
    args = parser.parse_args()
    subprocess.run([sys.executable, str(ROOT / "scripts" / "validate_skill.py")], check=True)
    files = []
    for rel in SKILL_FILES:
        files.append(ROOT / rel)
    for subdir in ("references", "scripts"):
        for p in sorted((ROOT / subdir).rglob("*")):
            if p.is_file() and not any(part in EXCLUDED_DIRS for part in p.relative_to(ROOT).parts) and p.suffix not in EXCLUDED_SUFFIXES:
                files.append(p)
    files = sorted(set(files))
    if not files:
        raise SystemExit("No skill files found")
    args.output.mkdir(parents=True, exist_ok=True)
    for ext in ("skill", "zip"):
        dest = args.output / f"simulacra.{ext}"
        with zipfile.ZipFile(dest, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
            for path in files:
                archive_path = Path("simulacra") / path.relative_to(ROOT)
                zf.write(path, str(archive_path))
        with zipfile.ZipFile(dest) as zf:
            assert zf.testzip() is None
            assert "simulacra/SKILL.md" in zf.namelist()
            assert "simulacra/references/CognitivePipeline.md" in zf.namelist()
        print(f"Built {dest} ({dest.stat().st_size:,} bytes, {len(files)} files)")

if __name__ == "__main__":
    main()
