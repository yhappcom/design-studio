# T021 — R1 Exact Geometry Patch Specification

Evidence purpose: **PRACTICE / EXECUTION SPECIFICATION**. This converts the accepted drawing-repair direction into an exact source-level patch target without claiming a rendered result.

## RELATED DOMAIN CHECK
- **Color:** C047 and successor state-color work cannot compensate for `I/l/1/0` ambiguity.
- **Layout/Interaction:** operational IDs and recovery evidence must remain readable without changing provisional metrics.
- **Web:** browser closure continues on mature fallback until T021 drawing and spacing gates pass.
- **Content:** semantic strings remain unchanged; Type must adapt the drawing, not shorten authoritative wording.
- **UX:** human recognition/error-rate evidence remains OPEN.

## Canonical source inspected
`T021-normalized-architecture-harness.py` remains the normalized executable source. The current constructions were re-read directly. The R1 patch remains bounded to four geometry loci and does not alter widths, sidebearings, corpus semantics or kerning.

## Exact patch intent

### Capital I
Current construction uses full-width top and bottom bars plus a centered stem. R1 may change terminal depth/shape **inside the existing advance width and LSB/RSB envelope only**. It must preserve a bilateral-capital silhouette at 14/17/24 px and must not converge toward `1`.

### Lowercase l
Current construction is a vertical stem plus a base-only foot. R1 must introduce a second primary silhouette cue above the baseline while preserving `(aw,l)` metrics. A mere longer foot is rejected because the direct critique already found base-only distinction insufficient.

### Digit 1
Current construction combines centered stem, baseline bar and top-entry polygon. R1 must preserve numeral entry/base identity but move its dominant silhouette away from repaired `l`; no sidebearing or advance-width change is allowed.

### Candidate-B zero
Current slash polygon is `[(l+112,72),(l+164+dc,72),(r-112,CAP-72),(r-164-dc,CAP-72)]`. R1 may reduce slash width/dominance and increase inset, but must not change the zero ring, figure width or sidebearings. Candidate A plain zero remains the control.

## Patch invariants
1. Kerning OFF.
2. `WIDTH_A`, `WIDTH_B`, lower-case `(aw,l)` and digit `figure_width_mode` unchanged.
3. No unrelated glyph edits.
4. No content-string edits to make the repair look better.
5. Source SHA, built-font hash and every 14/17/24px raster hash must be captured.
6. Original ambiguity, operational, destructive-state and retention-expiry corpora must all rerender from the same source commit.

## Acceptance / rejection
A patch is accepted for **drawing critique**, not PASS, only if `I/l/1` gain independent silhouette identity and candidate-B `0` retains O/0 discrimination without slash dominance. Any material regression in airport, identifier, revision, time or interval strings rejects the patch. General spacing remains closed until this rerender is directly critiqued; kerning remains closed until general spacing.

## EXECUTION BLOCKER
This connector can inspect and write repository text but cannot execute the font/raster toolchain or safely replace the complete 12k+ line-return-truncated harness as an atomic source→artifact operation. Blind partial replacement would violate reproducibility. The next browser/CI-capable Type run should apply this bounded patch to the complete source, run the existing normalized workflow, and return artifacts/hashes.

## HANDOFFS TO OTHER SPECIALISTS
All peers should continue mature fallback for product evidence. Do not freeze geometry around provisional custom metrics. When R1 artifacts exist, Web/Layout should transfer-test them only after Type direct critique and general-spacing gates.