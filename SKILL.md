---
name: simulacra
description: Character cognition, embodied decision-making, stateful roleplay, and long-form fiction drafting using the Simulacra cognitive pipeline. Use for character simulation, character-driven scene design, drafting, continuity checks, and state commits.
---
# Simulacra

This skill is a downstream adapter of [Daystar79/Simulacra](https://github.com/Daystar79/Simulacra), not a replacement psychology engine.

## Activation
1. Identify mode: `simulate`, `design`, `draft`, `audit`, or `commit`. Ask only when the request cannot determine it.
2. Read `references/CognitivePipeline.md`, `references/Rules_Index.md`, `references/Modules.md`, `references/psychosomatic_state.json`, and `references/realm_data.yaml`. The upstream source wins over summaries here.
3. Load the requested character card, durable log, and event/scene context from the user's project. Never invent missing card facts or claim a file was loaded when it was not.
4. For drafting read `references/Main.md`; for design read `references/Design_QA_Protocol.md` and follow its mandatory project-context load manifest.
5. Execute the cognitive pipeline **before** rendering prose or dialogue. Apply only enabled and verified module hooks.
6. Keep the framework's internal state and terminology off-page in creative output. Show only the requested output; offer diagnostics separately when asked.
7. Do not write persistent changes without explicit approval. On approval commit only durable-mapped fields to character logs; do not modify immutable character cards.

## Cognitive contract
- First resolve nervous system and somatic pressure, then raw affect.
- Choose deliberative versus reactive circuit according to the source spec. Reactive processing bypasses rational arbitration.
- In deliberative processing apply wound/gift prism, masking and weighted drive arbitration.
- Produce the four channels `Feels`, `Thinks`, `Says`, `Does` and a live snapshot matching the bundled JSON schema.
- Card defines identity; durable log overlays evolved defaults; live state is transient. Memory and competence must respect their recorded gates.
- Characters retain agency, individual voice, competing motives, and the ability to refuse.
- Respect host system policies and user instructions above the skill; upstream invariants govern simulation only within that hierarchy.

## Mode routing
- **simulate**: use the cognitive contract and user-provided event; render in-character output, not diagnostic dumps.
- **design**: follow the design Q&A protocol, verify required context, ask one question at a time, record locks and produce a movement brief.
- **draft**: use an approved movement brief and `Main.md` drafting rules; keep prose clean and preserve style lock.
- **audit**: compare existing text against loaded cards, logs, timeline, voices, rules and schemas; report concrete findings without silently rewriting.
- **commit**: show proposed durable deltas, obtain approval, then update logs atomically when file tools are available.

## Missing inputs
If the source files or character state cannot be loaded, identify the missing inputs. Do not pretend a simulation was run at full fidelity.

## Distribution
The bundled references are upstream-derived and retain CC BY-SA 4.0 terms. Scripts are MIT. Do not distribute named author-local character cards or filled logs. See `LICENSE.md` and `UPSTREAM.md`.
