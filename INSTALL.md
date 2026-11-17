# Install Simulacra without Git

Download the archives from a tagged GitHub Release or a successful GitHub Actions build artifact.

## ChatGPT plugin upload

Use **simulacra-chatgpt.zip**, not the generic `simulacra.zip`.

ChatGPT's plugin upload error specifies an accepted skill entrypoint under `skills/*/SKILL.md`. This archive uses `skills/simulacra/SKILL.md` and bundles all referenced files under that directory. In ChatGPT's New Plugin dialog, upload this archive and select Add plugin when enabled. This packaging matches the reported path requirement; actual ChatGPT acceptance should be confirmed in the UI.

## Gemini CLI

```bash
gemini skills install /path/to/simulacra.skill --scope user
```

Inside Gemini CLI, run `/skills reload` and `/skills list`. Alternatively extract `simulacra.zip` into `~/.gemini/skills/`.

## Claude Code / Codex / other filesystem agents

Extract `simulacra.zip` under your agent's user or workspace skills directory.

## Build locally

```bash
python scripts/package_skill.py
```

Outputs `dist/simulacra.skill`, `dist/simulacra.zip`, and `dist/simulacra-chatgpt.zip`. No third-party packages required.

## Contents and privacy

The archives include public upstream references, schema, realm data, and empty character templates. They exclude named author-local cards, filled logs, and relationship maps.
