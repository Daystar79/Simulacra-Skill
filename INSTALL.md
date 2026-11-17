# Install Simulacra without Git

Download `simulacra.skill` or `simulacra.zip` from a tagged GitHub Release. The same archives are generated as workflow artifacts on every main-branch push.

## Gemini CLI

```bash
gemini skills install /path/to/simulacra.skill --scope user
```

Inside Gemini CLI, run `/skills reload` and `/skills list`.

If the local installer is unavailable, extract `simulacra.zip` into `~/.gemini/skills/`, producing `~/.gemini/skills/simulacra/SKILL.md`.

## Claude Code / Codex / other filesystem agents

Extract `simulacra.zip` under your agent's user or workspace skills directory. The archive includes a top-level `simulacra/` folder and its `SKILL.md`.

## Gemini web and other upload-based chat apps

Where the product supports uploading a custom skill archive, upload `simulacra.zip`. Where it only supports file attachments, extract the archive and attach the relevant files; attachment alone does not necessarily activate an Agent Skill.

## Build locally

```bash
python scripts/package_skill.py
```

Outputs `dist/simulacra.skill` and `dist/simulacra.zip`. No third-party Python packages required.

## Contents and privacy

Both archives contain the same public skill files, including all bundled upstream reference documents, JSON schema, realm data, and empty character templates. They do not contain named author-local characters, filled logs, or relationship maps.
