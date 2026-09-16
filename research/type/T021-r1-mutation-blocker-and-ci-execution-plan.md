# T021 R1 Mutation Blocker and CI Execution Plan

## PURPOSE

`EXECUTION PLANNING` after the R1 readiness review. This note prevents another specification-only loop and defines the exact evidence needed from the already-authorized mutation/build path.

## CURRENT GATE

Stage 2 remains PRACTICE. Drawing repair precedes general spacing; general spacing precedes kerning. T022 stays closed.

## EXECUTION FINDING

The canonical executable source is `T021-normalized-architecture-harness.py`; the repository workflow `type-t021-normalized-proof.yml` installs FontTools/Pillow, runs semantic sensitivity, runs the normalized proof, and uploads `/tmp/t021-normalized-*` artifacts. Therefore the next useful Type evidence is not another design rubric. It is a bounded source mutation followed by CI raster evidence.

The present automation environment can read and write repository text but does not expose a local editable checkout/browser-like raster inspection surface. A blind source rewrite would weaken provenance because the full executable file, generated artifacts, and before/after visual critique cannot be atomically inspected here. Mutation is therefore OPEN rather than simulated.

## REQUIRED R1 EXECUTION

1. mutate only `I`, `l`, `1`, and candidate-B `0` slash construction;
2. keep kerning OFF and advance widths/sidebearings frozen;
3. run the existing normalized workflow;
4. preserve commit SHA, source blob SHA, font hashes and raster hashes;
5. inspect `Il1 I1l lI1 111 lll III`, `O0 00 OO 00:45 B737-900`, bounded airport/identifier/numeric/temporal rows at 14/17/24 px;
6. reject local ambiguity gains that regress operational strings;
7. only after a defensible drawing verdict open general-spacing critique.

## RELATED DOMAIN CHECK

- Color: semantic cues cannot compensate for glyph ambiguity.
- Layout/Interaction: concurrent/audit identifiers require stable discrimination but must not freeze provisional metrics.
- Web: product transfer remains on mature fallback until drawing/spacing gates are defensible.
- Content: exact operational and temporal strings remain regression inputs.
- UX: deterministic raster critique is not human recognition evidence.

## HANDOFFS TO OTHER SPECIALISTS

Do not design around provisional custom metrics. Preserve exact stress strings and keep human recognition/error-rate claims OPEN.

## EVIDENCE BOUNDARY

This closes the planning ambiguity about where/how R1 must execute. It does not close the repaired-raster blocker, drawing gate, spacing gate, T022 entry, browser/native transfer, or human validation.