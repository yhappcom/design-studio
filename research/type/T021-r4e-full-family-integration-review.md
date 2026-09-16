# T021 — R4E full-family integration review

Date: 2026-09-16  
Classification: **TRANSFER VALIDATION + CONTRADICTION REVIEW**  
Status: **R4E EXECUTED / BUILD-COVERAGE PASS / DRAWING FAIL / INCREMENTAL R4 LOOP REJECTED**

## Question

Can the R4D candidate be repaired into a coherent bounded LogMate family by imposing a small shared terminal/join/aperture grammar on C/G/S/P/R, while holding kerning off and comparing slash-zero against an otherwise identical plain-zero control?

## RELATED DOMAIN CHECK

- **Type:** R4D exact full-family critique is the direct predecessor. R4B/R4C showed that bounded grammar invariants can improve a small cluster but do not prove family coherence.
- **Color:** no color cue is allowed to rescue character identity.
- **Layout/Interaction:** operational strings and geometry remain literal; layout widening is not a Type repair.
- **Web:** W018 confirms long strings may reflow rather than be semantically shortened. Browser font transfer remains downstream of a drawing-valid candidate.
- **Content:** CD016 reinforces preservation of professional identifiers and typed literal data. Type must support those strings rather than alter them.

## R4E construction intervention

The R4E harness imports the exact R4D build/corpus plumbing and changes only the drawing layer needed for the hypothesis.

Shared parameters:

- terminal thickness: 82 units;
- optical inset: 24 units;
- bowl/stem join inset: 18 units;
- C/G aperture: 150 units;
- kerning: OFF.

C/G receive one open-curve terminal rule; G adds a controlled bar. S is rebuilt as opposing bowls joined by a controlled spine. P/R share one bowl/join construction and R adds the leg. A slash-zero primary and plain-zero control are generated from otherwise identical non-zero geometry.

## Exact execution

GitHub Actions run `35044716022` executed the repository harness successfully under Python 3.13.15 with fontTools 4.65.0 and Pillow 12.3.0.

Retained artifact `10425858762` contains:

- slash-zero R4E TTF;
- plain-zero R4E TTF;
- 14/17/24 px slash-zero specimens;
- 14/17/24 px plain-zero specimens;
- result JSON;
- intermediate R4D TTF produced by the imported harness.

Result contract:

- required unique non-space operational characters: **36**;
- covered: **36/36**;
- missing: **[]**;
- kerning: **OFF**;
- two zero variants generated under a controlled geometry comparison.

The temporary workflow used to obtain this exact run was removed after execution because `.github/` is outside the Type specialist's ordinary writing boundary. The run remains valid historical execution evidence; future specialist work must stay inside `research/type/` and `progress/TYPE_STATUS.md` unless coordinator authorization changes that boundary.

## Raster critique

The retained 17 px slash-zero and plain-zero specimens were inspected directly after downloading the exact CI artifact. The intervention does **not** clear the drawing gate.

### What improved

- C/G no longer use the exact R4D aperture construction.
- P/R now share an explicit join rule instead of independent ad-hoc joins.
- S is no longer the R4D pinched construction.
- slash-zero and plain-zero are now a legitimate controlled comparison rather than two unrelated candidates.

### What still fails

1. **The family remains visibly construction-led rather than optically integrated.** The new C/G/S/P/R rules coexist with inherited straight/diagonal R3/R4D forms whose skeleton, terminal behavior and proportions were never redesigned under the same grammar.
2. **S remains awkward at operational raster size.** Changing the contour topology removed one defect but did not produce a settled skeleton/weight distribution.
3. **C/G remain mechanical.** A numeric aperture token does not itself solve terminal placement, curvature tension or optical opening.
4. **P/R remain schematic.** A shared join parameter makes the source more systematic, but source regularity is not equivalent to optical coherence.
5. **Ambiguity-critical forms remain uneven as a family.** The zero alternatives are technically controlled, but choosing slash vs plain zero before the surrounding alphabet/figure grammar stabilizes would be premature.
6. **Inherited forms dominate the remaining identity problem.** The exact full specimen shows that repairing a handful of visibly weak glyphs cannot establish a coherent family when the base skeleton vocabulary itself was assembled incrementally.

These are designer/raster observations, not human-recognition or task-performance claims.

## Contradiction result

R4B established that internal grammar constraints could be made deterministic. R4C showed a bounded cluster could be promotable. R4D then showed bounded success did not survive full-family context. R4E now tests the natural repair hypothesis—add shared parameters to the worst full-family forms—and falsifies it as a sufficient method.

**A small set of shared numeric drawing tokens is not sufficient to integrate an incrementally assembled alphabet.**

This changes the next action. Continuing R4F/R4G as isolated contour repair would repeat the same method after its transfer failure.

## Decision

- exact build/reproducibility: **PASS**;
- bounded operational cmap: **PASS 36/36**;
- deterministic 14/17/24 raster: **PASS**;
- controlled slash/plain-zero experiment: **PASS as method, NO product selection**;
- coherent-family drawing: **FAIL**;
- general spacing: **BLOCKED**;
- kerning: **BLOCKED**;
- T021 closure: **NO**;
- T022 opening: **NO**.

### Method decision

**REJECT further incremental R4 glyph patching as the primary path.**

The next Type block should be a **family-architecture reset**, not R4F contour repair. It should define complete skeleton/proportion/terminal/join/curve/figure rules across construction classes before drawing another full candidate. At least two materially different family architectures should be generated from that common operational corpus and compared at 14/17/24 px. This is more aligned with the Stage 2 requirement for multiple solutions and defended selection than serially polishing one inherited construction.

A sensible architecture comparison is:

- **Architecture A — restrained humanist/technical proportional:** conventional skeletons, modest apertures, differentiated figures, low novelty;
- **Architecture B — engineered operational semi-mono:** tighter width band and stronger identifier rhythm, but optical width exceptions preserved.

These are hypotheses, not selections. Proportional Roboto remains the current product control. No custom candidate becomes a product recommendation until drawing, spacing and later transfer evidence support it.

## Evidence boundary

No human readability, recognition, preference or task-performance claim. No Flutter/native/browser transfer. No physical-device evidence. No production font recommendation. R4E is exact CI/raster + designer critique only.

## HANDOFFS TO OTHER SPECIALISTS

- **Layout/Interaction:** preserve literal operational strings and current geometry; custom Type remains unstable.
- **Web:** do not spend browser-transfer effort on R4E as though it were a candidate release; proportional Roboto remains the current product control.
- **Content:** continue preserving identifiers/numerics exactly; the failed custom family does not justify wording changes.
- **Color:** keep ambiguity controls independent of hue.
