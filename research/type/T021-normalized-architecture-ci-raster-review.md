# T021 — Normalized Architecture CI + Raster Review

Classification: **EXECUTED VALIDATION / METHOD GATE / ROUTE DECISION**

## SOURCE / execution
GitHub Actions `Type T021 Normalized Proof` run `35048673549`, job `104644072791`, checked out exact commit `21f9bc8470403716cbf2b45ab3f8338db18c3323` on Ubuntu 24.04 with Python 3.13.15, FontTools 4.65.0 and Pillow 12.3.0. Semantic sensitivity, normalized A/B build and artifact upload all completed successfully. Artifact ID: `10428146590`.

## Semantic architecture gate
The reconciled semantic contract passed **11/11** normalized token groups:
`stem, round_stem, cap_overshoot, x_overshoot, aperture, diag_comp, terminal_policy, bowl_join, shoulder_tension, figure_width_mode, zero_treatment`.

Every mandatory consumer changed under the corresponding perturbation and protected consumers remained invariant. Conditional consumers were reported without being forced. In particular:
- `aperture` changed C/G while S/5 remained independent;
- `zero_treatment` changed 0 while O remained invariant;
- `shoulder_tension` changed n while o remained invariant;
- `figure_width_mode` changed all 0–9 while O remained invariant;
- `bowl_join` changed B/D/P/R/8 and also affected conditional 6/9;
- `diag_comp` changed A/V/X/K/R/2/4/7.

**SYNTHESIS:** the previous metadata-only architecture defect is closed. The normalized architecture is executable rather than declarative.

## Build / corpus gate
Both A and B built with kerning OFF and rendered the same bounded operational corpus with **36/36 coverage, missing=[]**. Deterministic specimens were emitted at 14/17/24px.

Representative 17px widths:

| string | A | B |
| --- | ---: | ---: |
| ICN | 27.3906 | 27.7188 |
| NRT | 30.3594 | 30.2656 |
| JFK | 27.7812 | 29.9219 |
| B737-900 | 72.7344 | 74.9531 |
| 1,284:35 | 65.7500 | 68.0000 |
| 0O | 19.7500 | 19.8906 |
| 1Il | 24.8125 | 26.5156 |
| 5S | 19.0781 | 19.8906 |
| 8B | 19.5469 | 19.8906 |
| AVAVA | 51.0156 | 51.0156 |

A/B therefore remain materially different metric hypotheses, but metric difference is not a drawing-quality verdict.

## Exact raster inspection
The exact CI artifact was downloaded and the A/B 17px and 24px specimens were inspected directly.

### Improvements that survive inspection
- B's slashed zero creates a real 0/O distinction without contaminating O.
- A/B terminal and diagonal policies are visibly different rather than metadata labels.
- n responds to the new shoulder system and no longer depends on an inert token.
- the repertoire renders consistently enough to inspect as a family rather than as missing-glyph engineering output.

### Remaining drawing failures
Both candidates still fail the professional drawing gate.

1. **5/S** — their silhouettes are distinguishable but the stroke logic and terminals still read as constructed research glyphs rather than a resolved family pair. The 5 remains mechanically segmented while S uses a different continuous grammar.
2. **8/B** — distinction exists, but bowl/counter relationships are not optically balanced across sizes. B's bowl joins and 8's stacked counters do not yet share a mature curve system.
3. **1/I/l** — the ambiguity set is structurally separated, but lowercase l and figure 1 remain weak/skeletal at target sizes; this is not a convincing operational identifier system.
4. **round/bowl family** — O/0, B/D/P/R/8 still show uneven curve tension and counter treatment. Parameter operationality did not automatically create optical coherence.
5. **figures** — 2/3/4/6/7/9 remain visibly constructed from research primitives; several transitions are abrupt at 17px and remain conspicuous at 24px.
6. **overall texture** — both A and B produce an uneven word texture: some glyphs are conventional enough while others have display/technical eccentricities. This prevents a coherent text family judgment.

## KEEP / REWORK / REJECT
**KEEP:** semantic architecture method, exact CI, bounded corpus, 14/17/24 raster gate, protected-consumer tests, B zero treatment as an available operational feature hypothesis.

**REWORK:** no further serial glyph patch cycle is authorized inside T021 before route comparison.

**REJECT as current product family:** both normalized A and B. Neither earns drawing PASS.

## Method conclusion
The study has now tested more than a local drawing iteration. It has produced a semantically operational architecture, full bounded coverage and exact intended-size raster, yet both custom directions still fail drawing coherence.

This satisfies the previously defined stop condition: **do not begin another R5/R6-style bespoke patch cycle.** The next T021 method is a route comparison against the current product control (proportional Roboto), asking whether bespoke authorship is justified at all for LogMate's current product needs.

This is not a claim that bespoke type is inherently inferior. It is a scope/evidence decision: current bespoke candidates have not demonstrated sufficient benefit to justify continued authorship cost before comparison with a mature product control.

## Spacing / T022 boundary
General spacing remains blocked for the bespoke candidates because drawing is still invalid. Pair-specific residuals and kerning remain blocked. T022 does not open.

## RELATED DOMAIN CHECK
- Layout/Interaction: continue flexible geometry; do not freeze cells to A/B widths.
- Web: retain current mature product typography control until a custom family earns a drawing/product advantage.
- Content: exact operational tokens remain proof inputs; no wording was altered to improve specimens.
- Color: no ambiguity repair via color.

## HANDOFFS TO OTHER SPECIALISTS
The normalized custom metrics are not stable product inputs. Web/Layout should continue with current product typography and stress-test metric flexibility. If a later custom route is revived, it must first demonstrate a concrete advantage over mature controls under the same operational corpus.

## Verdict
**Semantic architecture: PASS. 36/36 build: PASS. Exact 14/17/24 raster: EXECUTED. Drawing: FAIL for A and B. Bespoke serial repair: STOP. Next gate: bespoke-route vs current proportional Roboto comparison.**
