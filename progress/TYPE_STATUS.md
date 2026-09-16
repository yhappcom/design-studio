# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 EXACT-SOURCE REPRODUCIBILITY DEFECT FOUND**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 evidence state

Prior bounded equivalent execution remains valid as a bounded experiment: 36/36 encoded cmap coverage, 14/17/24px render/measurement, Roboto width comparison, and a drawing-quality FAIL. Canonical critique: `research/type/T021-operational-expansion-executed-raster-critique.md`.

New canonical audit: `research/type/T021-redraw-build-blocker-audit.md`.

A subsequent redraw/reproducibility attempt exposed a stricter source defect before a second-pass raster could be accepted. The exact canonical harness declares `UPPER='ABCDEFGHIJKLMNOPRSTUVX'`, including `M`, but its `widths` dictionary omits `M` while the loop indexes `widths[c]`. Exact execution therefore reaches `KeyError: 'M'`. In addition, `boxglyph` has no explicit M branch, so merely adding a metric would route M to the generic filled-box fallback and still fail drawing validity.

This corrects the earlier wording that the canonical harness itself was already a complete reproducible bounded-family generator. The earlier 36/36 result came from an equivalent local execution and remains useful as a falsification/raster experiment, but it is not proof that the exact repository source currently reproduces that result.

## Method correction

Evidence chain is now:
`declared repertoire → complete metric map → explicit glyph construction → executable build → cmap coverage → raster drawing validity → general spacing → pair residual → kerning`.

Build exceptions and generic placeholder fallbacks are both failures before spacing/kerning analysis.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE — first bounded raster exposed drawing defects; exact-source redraw path additionally blocked by M metrics/construction defect** |
| spacing/control strings | **PRACTICE — prior measurements exist; redraw spacing remains blocked until drawings/build stabilize** |
| kerning classes/exceptions | **OPEN / BLOCKED** |
| figure styles | **PRACTICE — first figures rendered but structural quality insufficient; redraw OPEN** |
| diacritics/punctuation coherence | **PRACTICE — executable evidence exists; optical/component quality OPEN** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — prior 14/17/24 evidence exists; exact-source redraw rerun required** |
| typography across product roles | **PARTIAL / STRONG BRIDGE** |
| multiple solutions + defended selection | **PRACTICE — B metric direction provisional; final identity selection OPEN** |

## Active next queue — large block only

1. Repair repertoire/metrics/construction consistency, including a real M construction rather than a generic fallback.
2. Replace invalid C/G additive-mask forms and redraw S, R, B/D, lowercase n and deficient figures.
3. Execute the **exact repository generator** and retain measured JSON/raster evidence at 14/17/24px with kerning OFF.
4. Inspect every operational string and classify drawing vs general-spacing vs pair-specific residual.
5. Repair drawing/base-spacing failures and rerun before reporting completion.
6. Compare accepted candidate against proportional Roboto and exact `LogMateRobotoMono` only when that exact artifact is available.
7. Close T021 only if its contract is actually satisfied; then and only then open T022.

## Evidence boundary

No second-pass redraw raster PASS is claimed. The latest attempt failed before build completion. No human/native/browser recognition evidence is simulated. Exact LogMate mono comparison remains OPEN.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as Stage 2 entry**.
- T021 first bounded equivalent build/raster: **EXECUTED; 36/36 cmap but drawing gate FAIL**.
- T021 exact canonical source reproducibility: **FAIL — M metric/construction inconsistency found**.
- structural redraw: **IN PROGRESS / no PASS claimed**.
- T022: **BLOCKED**.
- Stage 2: **NOT PASSED**.
