# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / LOGMATE TYPE IDENTITY PRIORITY / T021 R2 EXACT RASTER DRAWING GATE FAIL**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Next new-study ID: `T022` only after T021 family/drawing/spacing/operational evidence is sufficiently stable

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority: T019 for Stage 1; T020 for Stage 2 entry.

## T021 evidence state

Canonical CI review: `research/type/T021-r2-canonical-ci-and-gate-review.md`.  
Exact raster critique: `research/type/T021-r2-exact-raster-critique.md`.

The prior exact-source M metrics/construction blocker is **RESOLVED**. Exact repository R2 builds on GitHub-hosted CI with bounded required non-space corpus coverage **36/36**, no missing characters, kerning OFF, and 14/17/24px measurements.

Workflow run `35041942223` on commit `eeb618682ba56b8bb762669f1fb401806e3eecef` additionally executed a deterministic raster-proof step and uploaded the exact R2 TTF, JSON and 14/17/24px specimen PNGs. Artifact `10425870809` has digest `sha256:43304420f417126c883309248f04bd63b66af9b1e1920d2788ebe2e94658c765`.

The exact 17px and 24px specimens were directly inspected. The drawing gate is **FAIL**, not merely OPEN. Dominant defects are rectangular/debug-like round and bowl vocabulary, immature seven-segment-like figures, weak family coherence between capitals/lowercase, and construction extremity in ambiguity controls. These are DRAWING defects and must not be compensated with spacing/kerning.

Existing adversarial source audit remains canonical and complementary:
- `research/type/T021-r2-structural-collision-review.md`;
- `research/type/T021-r2-structural-collision-audit.py`;
- `research/type/T021-r2-structural-collision-audit-results.json`.

It found `5/S` normalized construction collapse and broad `D/O/0` rectangular-ring weakness, while `1/I/l` and `8/B` retain materially different source signatures. The fresh raster evidence independently confirms that the current ambiguity/figure system is not optically mature.

## Evidence chain

`declared repertoire → complete metric map → explicit glyph construction → executable build → cmap coverage → deterministic intended-size raster → drawing validity → general spacing → pair residual → kerning`

The chain now has direct evidence through intended-size raster production and stops at **drawing validity FAIL**.

## Current LogMate control boundary

Fresh audit of current `yhappcom/logmate` `main` found font assets `NotoSansKR-wght.ttf`, `Roboto-Regular.ttf`, and `Roboto-Medium.ttf`. Current `pubspec.yaml` declares only `LogMateNotoSansKR` and `LogMateRoboto`; no `LogMateRobotoMono` asset/family is present on current main.

Therefore proportional Roboto is the current-main product control. Any historical Roboto Mono experiment must remain historical unless a specific branch/artifact is deliberately restored. Generic mono must not be mislabeled as a current product control.

## Stage 2 matrix

| Requirement | Current state |
| --- | --- |
| coherent glyph family | **PRACTICE / FAIL at R2 drawing gate; exact raster + source collision evidence agree** |
| spacing/control strings | **PRACTICE; exact advances/raster exist, optical/base-spacing judgment blocked by redraw** |
| kerning classes/exceptions | **OPEN / BLOCKED** |
| figure styles | **PRACTICE; equal-advance geometry measured but current figure drawings FAIL; proportional-vs-tabular decision deferred** |
| diacritics/punctuation coherence | **PRACTICE; encoded/executable evidence exists, optical quality OPEN** |
| weight/width relationships | **PARTIAL / STRONG BRIDGE** |
| interpolation fundamentals | **SUPPORTED FOR ENTRY** |
| screen rendering/small-size compensation | **PRACTICE — deterministic 14/17/24 R2 artifact EXECUTED; drawing quality FAIL** |
| typography across product roles | **PARTIAL / STRONG BRIDGE; current-main proportional Roboto control verified** |
| multiple solutions + defended selection | **PRACTICE; B/R2 rejected as product identity candidate, retained as falsification/control evidence** |

## Active next queue — large block only

Do not report after one micro-step. Next Type block should proceed through as many linked gates as executable:

1. produce **R3** within the same bounded repertoire; do not add breadth;
2. replace rectangular round/bowl grammar with credible curved/optically corrected O/0/C/G/D/B/R/U forms;
3. separate `5/S` at construction and raster levels;
4. redesign figures, especially `1`, `8`, and seven-segment-like forms, while preserving useful operational alignment where justified;
5. improve lowercase n/o relationship to the capital system;
6. keep kerning OFF;
7. emit deterministic 14/17/24 specimens and execute exact CI;
8. inspect exact artifacts and revise again in the same block if repairable;
9. only after drawing validity, revise sidebearings/general spacing from repeated-context evidence;
10. enumerate only true pair-specific residuals as T022 kerning candidates;
11. close T021 only if its contract is satisfied; then open T022 immediately.

## Evidence boundary

No R2 drawing PASS is claimed. No human/native/browser recognition evidence is simulated. Static construction differentiation and designer inspection are necessary evidence but not human recognition/error-rate evidence.

## HANDOFFS

- Layout/Interaction: keep product column geometry reversible; do not compensate for R2 glyph defects by globally loosening layouts.
- Web: exact artifact reproducibility is established; browser transfer waits for a stable drawing candidate.
- Content: preserve literal operational identifiers and ambiguity corpus.
- Color: glyph identity must not depend on color.

## Latest checkpoint

- Stage 1: **PASS**.
- T020: **COMPLETE as Stage 2 entry**.
- T021 exact canonical source reproducibility: **PASS on CI**.
- T021 bounded encoded coverage: **36/36 PASS**.
- deterministic intended-size specimen: **14/17/24 EXECUTED and retained as CI artifact**.
- T021 R2 drawing gate: **FAIL — exact raster + 5/S source collision + 0/O weakness**.
- current LogMate main control: **proportional Roboto + Noto Sans KR fallback; no bundled Roboto Mono**.
- general spacing: **BLOCKED by drawing gate**.
- T022: **BLOCKED**.
- Stage 2: **NOT PASSED**.
