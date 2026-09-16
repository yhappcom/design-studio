# T021 — Construction-Complete Architecture Reset / Exact CI Raster Review

Status: **EXACT CI PASS / 36-CHAR COVERAGE PASS / A+B DRAWING FAIL / ARCHITECTURE TOKEN OPERATIONALITY REWORK**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Scope

The first A/B architecture reset was invalid as a complete comparison because figures 2/3/4/6/7/9 delegated to the R4D constructor. `T021-family-architecture-reset-complete-harness.py` removes that figure delegation and gives all ten figures an architecture-reset construction path before accepting new A/B evidence.

A dedicated clean GitHub Actions proof executed commit `c6a43969863aa5716dcb21047ad536ecfbc2e04a` on Ubuntu 24.04 / Python 3.13.15 / FontTools 4.65.0 / Pillow 12.3.0. Job `104634521908`, run `35045568141`, completed successfully and uploaded artifact `10427275894` containing both TTFs, both 14/17/24 specimen sets and the JSON result.

## SOURCE → EXECUTION

Machine result:
- same bounded operational corpus: yes;
- required distinct non-space characters: 36;
- A coverage: 36/36, missing `[]`;
- B coverage: 36/36, missing `[]`;
- kerning: OFF;
- intended sizes: 14/17/24px;
- digit provenance assertion: 0–9 all `architecture-reset-complete`;
- construction-class completeness flag for the previously detected figure-delegation defect: true.

Representative 17px widths:

| Control | A proportional | B semi-mono |
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

The A/B width hypotheses are therefore materially observable in the executable fonts. B regularizes many operational widths more strongly; A retains more proportional variation. This is geometry evidence only.

## Exact artifact inspection

The uploaded exact-CI 17px A and B PNGs were downloaded and visually inspected. This is designer raster critique, not human-recognition testing.

### KEEP — architecture comparison as a method

A and B are now genuinely different executable width/weight/zero hypotheses over the same corpus. This is more informative than serially patching one candidate because a rejected direction has an explicit alternative.

### FAIL — neither A nor B is drawing-valid

Both 17px specimens still read as a coarse constructed display/technical alphabet rather than a controlled text family suitable for promotion. Problems remain systemic rather than pair-specific:

- `S/5` remain too close in overall silhouette/rhythm despite different source recipes;
- `8/B` remain weakly separated at target size;
- round/bowl glyphs show compressed, mechanical counter rhythm;
- lowercase `n/o` do not yet form a mature lowercase texture with the capitals;
- several figures retain visibly schematic transitions and terminals;
- repeated operational strings expose uneven black/white rhythm that cannot responsibly be diagnosed as kerning yet.

B's slash gives `0/O` a stronger explicit distinction, but that single ambiguity mechanism does not make B a coherent-family winner. A's plain zero avoids the slash but leaves 0/O more dependent on proportion/context. Neither direction passes the drawing gate.

## New adversarial source finding — architecture metadata is not fully operational

The reset declares architecture tokens `corner`, `join`, `diag_comp`, and `terminal`, but the current glyph constructors do not materially consume those tokens. The A/B implementation therefore satisfies **figure provenance completeness** but does **not** yet satisfy the stronger requirement that the declared architecture contract actually drives every claimed construction dimension.

This is an important correction to the gate model:

`no predecessor glyph delegation` is necessary but not sufficient for `architecture-complete`.

The stronger gate is:

`architecture token declared → token consumed by relevant construction class → measurable/raster consequence → family-level critique`.

Tokens that exist only as metadata must not be cited as evidence that the corresponding corner/join/diagonal/terminal policy was tested.

## Decision

- A architecture: **REWORK**, not selected.
- B architecture: **REWORK**, not selected.
- A/B comparison method: **KEEP**.
- figure predecessor delegation defect: **CLOSED**.
- architecture-token operationality: **FAIL / REWORK**.
- coherent drawing: **FAIL**.
- general spacing: **BLOCKED**.
- T022: **BLOCKED**.

## Method revision

The next implementation should stop adding named architecture parameters that do not alter outlines. It should reduce the architecture contract to a small set of **operational parameters with explicit consumers**, for example:

1. stem/round-stem → straight/round classes;
2. aperture → C/G and open-form classes;
3. overshoot → O/o/0 and related round classes;
4. diagonal compensation → A/V/X/K/N diagonal stroke construction;
5. terminal policy → C/G/S/5 and selected figures;
6. bowl asymmetry/join policy → D/B/P/R/8;
7. shoulder tension → n;
8. figure-width mode + zero treatment → all 0–9.

Each parameter must have a source assertion proving which glyph classes consume it. A/B should then be regenerated and rastered again. If the two architectures still fail as families after the architecture is truly operational, the bespoke-font route itself should be questioned against the current proportional Roboto product control rather than indefinitely extending local redraws.

## RELATED DOMAIN CHECK

- Layout/Interaction: B's more regular widths are measurable, but layout must not be changed to rescue failed drawing.
- Web: no browser transfer; neither candidate is stable enough.
- Content: literal operational corpus remains unchanged.
- Color: ambiguity remains monochrome; no identity depends on hue.

## Verdict

**The construction-complete CI pass closes the inherited-figure defect but does not close T021. Exact raster evidence rejects both current A and B drawings. More importantly, the audit reveals that several declared architecture tokens are metadata-only. The next gate is operational architecture, not another cosmetic glyph patch.**
