# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 R2 DRAWING GATE FAIL**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/drawing/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 evidence state

Canonical CI review: `research/type/T021-r2-canonical-ci-and-gate-review.md`.

The prior exact-source M metrics/construction blocker is **RESOLVED**. Commit `340705130357eed2d715439bec1577ed94d40561` repaired repertoire/metrics/construction consistency and the exact repository generator executed successfully on GitHub-hosted CI.

Current engineering evidence:
- exact repository generator: **PASS on clean CI**;
- bounded required non-space corpus coverage: **36/36 PASS**;
- intended-size advance measurement: **EXECUTED at 14/17/24px**;
- kerning: **OFF**;
- exact-source build/repertoire blocker: **CLOSED**.

Latest adversarial drawing audit:
- `research/type/T021-r2-structural-collision-review.md`;
- `research/type/T021-r2-structural-collision-audit.py`;
- `research/type/T021-r2-structural-collision-audit-results.json`.

The R2 source audit found:
- `5` and `S` use the **same normalized five-element construction recipe** and differ primarily by width;
- `D`, `O`, and `0` share the same broad rectangular-ring topology at this construction abstraction, leaving `0/O` structurally weak for an explicit ambiguity control;
- `1/I/l` retain materially different source construction signatures;
- `8/B` retain materially different source construction signatures.

This is static source/topology evidence, not human-recognition evidence. Nevertheless the literal `5S` ambiguity control makes the `5/S` construction collapse sufficient to keep the current drawing gate at **FAIL** rather than merely OPEN.

## Evidence chain

`declared repertoire → complete metric map → explicit glyph construction → executable build → cmap coverage → drawing validity → intended-size raster → general spacing → pair residual → kerning`

The chain now passes through encoded coverage but stops at drawing validity.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE / FAIL at current R2 drawing gate; 5/S structural collapse found** |
| spacing/control strings | **PRACTICE; measured advances exist, optical/base-spacing judgment blocked by redraw** |
| kerning classes/exceptions | **OPEN / BLOCKED** |
| figure styles | **PRACTICE; equal-advance R2 figures measured, proportional-vs-tabular decision deferred** |
| diacritics/punctuation coherence | **PRACTICE; encoded/executable evidence exists, optical quality OPEN** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE; deterministic R2/R3 specimen artifact still required** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE; B direction remains provisional, final identity selection OPEN** |

## Active next queue — large block only

Do not report after one micro-step. The next Type block should proceed through as many linked gates as executable:

1. produce **R3** with construction-level separation of `5/S`;
2. strengthen `0/O` distinction without relying on color/context;
3. preserve or improve `1/I/l` and `8/B` distinction;
4. keep kerning OFF;
5. emit deterministic 14/17/24px specimen images covering ambiguity controls + airports + identifiers + numeric/time + spacing strings;
6. execute the exact repository generator/CI path and retain TTF + JSON + specimen evidence;
7. critique drawing at all intended sizes and revise again in the same block if technically possible;
8. only after drawing validity, audit general spacing;
9. enumerate only residual pair-specific problems as future kerning candidates;
10. compare accepted candidate against proportional Roboto and exact `LogMateRobotoMono` only when that exact artifact is available;
11. close T021 only if its contract is actually satisfied; then open T022.

## Evidence boundary

No R2 drawing/raster PASS is claimed. No human/native/browser recognition evidence is simulated. Exact LogMate mono comparison remains OPEN. Static construction differentiation is necessary but not sufficient for human recognition.

## HANDOFFS

- Layout/Interaction: retain literal ambiguity controls; do not compensate for glyph defects by globally loosening dense operational layouts.
- Web: custom-font loading success is not drawing validity; browser transfer waits for a structurally stable candidate.
- Content: do not rewrite necessary identifiers to hide glyph ambiguity.
- Color: glyph identity must not depend on color.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as Stage 2 entry**.
- T021 exact canonical source reproducibility: **PASS on CI**.
- T021 bounded encoded coverage: **36/36 PASS**.
- T021 R2 drawing gate: **FAIL — 5/S normalized construction collision; 0/O structural weakness**.
- deterministic R2/R3 intended-size specimen artifact: **OPEN**.
- general spacing: **BLOCKED by drawing gate**.
- T022: **BLOCKED**.
- Stage 2: **NOT PASSED**.
