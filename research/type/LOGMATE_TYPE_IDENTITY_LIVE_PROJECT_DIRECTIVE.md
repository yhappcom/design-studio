# LogMate Type Identity — Live Project Research Redirect

Status: **INCOMING LIVE-PROJECT PRIORITY / TYPE SPECIALIST ACTION REQUIRED**  
Date: 2026-09-16  
Target project: `yhappcom/logmate` / `design/design-studio-proposal`

## Why this directive exists

LogMate Type research began because the product should not remain visually dependent on an undifferentiated default Flutter/UI-font treatment. The objective is not merely to make text render safely. The Type system must help LogMate become recognizably its own professional aviation-logbook product while preserving or improving operational legibility, scan rhythm, density and alignment.

Recent LogMate transfer work narrowed the question too aggressively toward conservative implementation safety:

- T017 treated proportional identifiers + semantic geometry as the default direction;
- T018 compared mature UI sans families and kept Roboto as the conservative control;
- T020 hardened the shipped Roboto 400/500/700 package and rejected synthetic weights;
- the pre-existing LogMate implementation had already used generic monospace for airport/ledger code data.

Those studies remain useful evidence, but they are **not the final product-identity answer**. Returning to generic monospace as the final answer would preserve an old implementation tactic rather than demonstrate that the Type program improved the product.

## Live-project objective

Reframe the LogMate Type question as:

> Can Design Studio produce a LogMate typography system that is more distinctive and coherent than the current Roboto/default-control state, while matching or exceeding the old monospace solution for operational alignment, scanability and identifier legibility?

This is a project-transfer priority and may pre-empt nonessential curriculum expansion under `AGENTS.md`.

## Controls, not conclusions

Treat the following as **controls**:

### Control A — existing LogMate generic monospace

Strengths already observed:
- three-character airport codes occupy stable equal advances;
- repeated DEP/ARR scan rhythm is visually stable;
- ledger columns are easy to compare.

Weaknesses / open questions:
- generic `monospace` is runtime/platform dependent;
- it may weaken product identity;
- it may over-technicalize the interface;
- it has not been shown to be optimal for identifier ambiguity, density or visual integration with the rest of LogMate.

### Control B — current Roboto proportional system

Strengths:
- mature UI behavior;
- exact product assets and weights are now controlled;
- general UI reading rhythm is familiar and stable.

Weaknesses:
- proportional airport-code width variance remains visibly distracting in repeated route rows;
- the visual identity remains generic;
- T018 proved that simply swapping among Roboto / Inter / Noto Sans does not solve airport-code width variance.

Neither control is automatically the final answer.

## Research direction

Use the ongoing Stage 2 Type Design work — especially the T021 chain of glyph construction, advance widths, sidebearings, pair-gap diagnostics and target-size raster proof — to investigate a LogMate-specific operational/identity treatment.

Do **not** assume in advance that the solution must be:
- full monospace;
- fully proportional;
- a second technical font;
- a custom full family;
- an OpenType feature;
- fixed-width layout boxes.

Instead compare materially different hypotheses.

Potential hypotheses may include, where evidence supports them:

1. **Refined proportional primary family** — improved LogMate identity but airport-code alignment solved elsewhere without visual penalty.
2. **Family-related operational uppercase treatment** — airport/operational capitals share LogMate family DNA while using controlled advance discipline.
3. **Semi-mono / duplex / width-disciplined operational subset** — fixed or tightly constrained advances only for roles that benefit from it.
4. **Dedicated alternate/style/feature path** — only if technically credible and useful; do not invent OpenType complexity without evidence.
5. **A mature mono companion** — retained as a valid candidate/control if it beats custom alternatives on product criteria.

The research is allowed to conclude that the old mono strategy remains best, but only after comparative evidence shows that newer alternatives do not improve the product.

## Product corpus

At minimum, test actual LogMate strings.

### Airport codes
`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`

### Flight / aircraft / registration identifiers
`KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`

### Numeric operational values
`00:45 02:18 09:55 12:40 1,284:35 9,999:59 1 11 111 8 88 888`

### Ambiguity controls
`0/O`, `1/I/l`, `5/S`, `8/B`

## Required comparison criteria

Compare the candidate directions against both controls using explicit criteria:

- product identity / distinctiveness without aviation cosplay;
- airport-code advance consistency;
- identifier recognition geometry;
- `0/O`, `1/I/l`, `5/S`, `8/B` distinction;
- compactness and information density;
- baseline and repeated-row rhythm;
- figure behavior and `tnum` integration;
- punctuation and hyphen behavior in aircraft/registration strings;
- small-size raster quality at actual LogMate target sizes;
- mobile/tablet ledger scan behavior;
- Flutter implementation feasibility;
- font package/fallback/runtime determinism;
- multilingual free-text separation: Crew/Remark remain Unicode/fallback-safe and must not inherit operational fixed-width rules by accident.

## Opening + View Logbook transfer requirement

The result must work as one system across at least:

- Opening route samples;
- Home recent-flight rows;
- View Logbook DEP / ARR;
- View Logbook flight identifiers;
- dense operational numeric columns.

Do not optimize only for the Opening screenshot.

## UI team's temporary implementation

The live UI will continue while this research proceeds.

Temporary product rule:
- airport-code text may use an explicitly controlled monospaced role to remove visible width drift;
- general UI remains proportional;
- time/duration remains tabular-numeric where appropriate;
- this temporary mono treatment is a **control / interim implementation**, not the final Type contract.

When the Type specialist produces stronger evidence, the UI team must be able to replace the interim treatment.

## Required output from Type specialist

Produce a project-facing comparison that answers:

1. What should LogMate's primary UI family/identity direction become?
2. What should airport codes use, and why is that better than both generic mono and current proportional Roboto?
3. Which other operational identifiers should share that treatment, and which should not?
4. Does the proposal improve product identity without sacrificing scan rhythm or compactness?
5. What exact glyph/metric evidence supports the choice?
6. What remains OPEN until Flutter/device/human validation?
7. What does the UI team change now, later, or never?

End with one of:

- `READY FOR LOGMATE TYPE IDENTITY TRANSFER`
- `NOT READY — KEEP INTERIM CONTROL`

If not ready, identify the narrow blocking evidence rather than falling back to a permanent generic-mono conclusion.

## Relationship to T021–T024

This directive does not discard the curriculum. It reorients it toward the live product:

- T021 family/drawing/spacing work should use LogMate operational strings as a meaningful transfer substrate where appropriate;
- T022 figure/kerning work should include LogMate numeric and identifier consequences;
- T023 weight/coherence work should test the roles LogMate actually needs;
- T024 multi-role typography work should become the natural place to integrate product identity if the family evidence is mature enough.

The exact study numbering remains owned by the Type specialist. The live-product problem, however, takes priority over unrelated expansion.

## Success criterion

The research succeeds when the Type system no longer answers only:

> "How do we make Roboto/default Flutter typography safe?"

and can instead answer:

> "Why does this typography belong to LogMate, and how is it measurably better for the operational data LogMate must present?"
