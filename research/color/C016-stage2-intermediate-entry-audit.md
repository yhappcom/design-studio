# C016 — Stage 2 Intermediate Professional Practice Entry Audit

Status: **ENTRY AUDIT / Stage 2 NOT PASSED — strong bridge evidence exists; remaining gaps are integrated palette-system practice and transfer validation**

Owner: Color Specialist

## Question

After Color Stage 1 Foundation PASS, which Master Curriculum Stage 2 Color requirements are already supported by existing evidence, and which still require new intermediate-practice work?

This audit prevents two errors: repeating advanced color science merely because it is available, and promoting Stage 2 because sophisticated numerical/browser studies exist without a complete authored product-color-system exercise.

## RELATED DOMAIN CHECK

### Typography / Type
Evidence checked: current `progress/TYPE_STATUS.md` and Color C009. Type is already in Stage 2 practice with actual outline/raster work. Reusable constraint: text-color decisions depend on real role, weight, fallback and raster conditions; Color should not infer typography production PASS from nominal contrast.

### Color
Evidence checked: Study 017, C002, C006, C010, C011, C015 and current Color status. Existing evidence is unusually strong in semantic architecture, two-context transfer, contrast, gamut/CMM reasoning and forced-colors resilience. The missing evidence is not another color-space survey.

### Layout / Interaction
Evidence checked: current `progress/LAYOUT_STATUS.md` plus latest `L008-stage2-intermediate-entry-audit.md`. Reusable constraint: Interaction owns state meaning; Color encodes it. L008 also independently identifies integrated product practice, rather than more isolated mechanism proofs, as the next useful Stage 2 direction.

### Web Design
Evidence checked: current `progress/WEB_STATUS.md` through W013. Web now has executed Chromium runtime transfer and is no longer merely a future dependency. C011 already supplies Color-owned Chromium forced-colors evidence; future palette work can hand concrete light/dark/gamut/token specimens to Web for independent browser transfer.

### Master Curriculum
Stage 2 Color requires:
- palette/ramp construction with explicit authoring models;
- semantic color-role systems;
- state/focus color coupled to interaction semantics;
- gamut-aware production values and fallback behavior;
- viewing-condition and device-aware validation.

The shared Stage 2 gate additionally requires multiple solutions to the same problem and a defended selected direction using explicit criteria and correctly borrowed adjacent-specialist evidence.

### Overlap decision
**ENTRY AUDIT + EVIDENCE MAPPING + CAPSTONE PLANNING.** No prior Color Stage 2 audit exists in the current main tree.

---

## Stage 2 requirement matrix

| Requirement | Existing evidence | Audit verdict |
| --- | --- | --- |
| Palette/ramp construction with explicit authoring model | Study 017 compares HSL, CIELCh and OkLCh and establishes explicit gamut/contrast boundaries | **STRONG BRIDGE / PRACTICE INCOMPLETE** — model selection exists, but no complete product palette is authored as competing alternatives and selected after integrated critique |
| Semantic color-role systems | C002 architecture; C006 two materially different product contexts and collision→revision | **STRONG / SATISFIED FOR ENTRY** — implementation/system transfer still open |
| State/focus color coupled to interaction semantics | C002 state/domain separation; C006 state roles; C011 forced-colors state/focus proof; I003 peer semantics | **STRONG / SATISFIED FOR ENTRY** |
| Gamut-aware production values and fallback | Study 016 + C010 high-precision Display-P3→sRGB/CMM work | **STRONG TECHNICAL BRIDGE / PRODUCT CONTRACT OPEN** — no selected palette has a complete P3/sRGB shipping/fallback token contract |
| Viewing-condition/device-aware validation | C015 low-light/high-glare bounded design/math stress; C009 DPR/raster transfer; C010 device/profile limitations | **PARTIAL** — no physical display/environment/device measurement; Stage 2 can progress without pretending those later physical gaps are closed |
| Multiple viable solutions + explicit selection | C006 collision-heavy vs role-separated mappings; C007/C008 failure→revision; C015 swatch-context critique | **METHOD EVIDENCE STRONG / INTEGRATED COLOR-SYSTEM GATE OPEN** — no single Stage 2 palette problem yet has 3 materially viable authored directions with explicit selection criteria |
| Comparative studies / hypothesis / critique | C004–C015 repeatedly compare methods/conditions and preserve failures | **STRONG** |
| KEEP / REWORK / REJECT | failure→revision is common, but not consistently framed at whole palette-system scale | **PARTIAL / CAPSTONE NEEDED** |
| Cross-specialist dependency / handoff | C006/C009/C011/C015 and current peer scans | **STRONG** |

---

## Audit conclusion

**Color Stage 2 is NOT PASSED.**

The current imbalance is not lack of color science. Color already has evidence beyond a normal intermediate baseline in ICC/CMM, gamut, spectral provenance, forced colors and rendered transfer. The missing work is authorship and integration:

1. construct a bounded product palette from an explicit authoring model rather than only describing one;
2. produce multiple materially viable palette/system directions for the same semantic requirements;
3. bind primitives to semantic roles, pair contracts, state/focus roles and light/dark context resolution;
4. define sRGB shipping values and, only where useful, Display-P3 values/fallback policy;
5. measure contrast, lightness ordering, chroma/hue behavior, gamut membership/mapping and semantic collisions;
6. critique the alternatives with explicit KEEP / REWORK / REJECT decisions;
7. select a direction without presenting preference as evidence;
8. preserve physical-device/environment and human-observer claims as OPEN until those methods are actually available.

## Highest-value next study

### C017 — Controlled Semantic Palette Derivation & Token Contract

Use one bounded product problem, preferably an operational/data product archetype rather than a decorative marketing palette.

Create three materially different but viable directions, for example:
- **A — restrained neutral + single action accent**;
- **B — brand-forward accent with separated semantic status hues**;
- **C — low-chroma operational system prioritizing luminance/state separation**.

All three must solve the same semantic job inventory and geometry so Color, not Layout, is the manipulated variable.

Required evidence:
- explicit OkLCh/other justified authoring coordinates;
- target sRGB gamut and mapping rule;
- optional P3 enhancement only when it changes a useful role;
- light and dark context resolution for the same semantic roles;
- primary/secondary content, surface, boundary, action, focus, selected, success/caution/critical and disabled/unavailable distinctions where the product actually needs them;
- foreground/background and boundary pair matrices;
- hue-removal/redundant-cue review for critical meaning;
- gamut membership/mapping diagnostics;
- semantic-collision audit;
- comparison criteria and KEEP/REWORK/REJECT critique;
- one defended provisional selection;
- explicit OPEN list for browser/device/physical/human transfer.

### Selection criteria
Do not collapse these into one generic score. Compare at least:
- semantic clarity;
- hierarchy without decorative chroma dependence;
- contrast margin;
- state/focus separability;
- light/dark role continuity;
- gamut/fallback stability;
- brand flexibility;
- token-system complexity;
- compatibility with Type and Layout/Interaction constraints;
- implementation and future-change risk.

## What is deliberately not a Stage 2 blocker

The following remain valuable later evidence but must not be used to keep Stage 2 permanently open:
- instrumented physical-display matching;
- measured glare/ambient illumination studies;
- real CVD/human observer studies;
- second CMM and print/soft-proof production validation;
- full Firefox/Safari/OS/device matrix;
- enterprise multi-product token governance.

They belong to later production/advanced/research gates unless a live project makes one immediately material.

## HANDOFFS TO OTHER SPECIALISTS

### Type
C017 should use realistic text-role constraints and preserve C009's warning that nominal pair contrast is not a substitute for exact raster/font validation.

### Layout / Interaction
Hold geometry and state meaning fixed while comparing Color alternatives. Reuse I003/L008 semantics; do not let hue redefine selected, focused, pending or critical states.

### Web Design
Once C017 produces a provisional token contract, Web can independently transfer-test CSS light/dark resolution, forced colors, P3/sRGB fallback and real page integration. Browser execution should confirm or limit Color conclusions rather than silently redefine them.

## Entry verdict

**Stage 2 — Intermediate Professional Practice: NOT PASSED / READY FOR CONTROLLED INTEGRATED PALETTE CAPSTONE.**

Color's next useful move is not broader theory. It is a complete, reproducible, multi-solution palette-system exercise with explicit selection criteria and bounded implementation contracts.