# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 EXACT R1 PATCH SPECIFIED — MUTATION + RASTER EXECUTION OPEN**
Governance sync: 2026-09-17
Primary path: `research/type/`
Active authority: `T021` direct critique + bounded R1 repair

## Current level
Stage 1 **PASS**; Stage 2 **PRACTICE / NOT PASSED**.

## Latest evidence
`T021-r1-exact-geometry-patch-specification.md` re-inspects the normalized harness and converts the accepted repair direction into exact source-level invariants for `I/l/1` and candidate-B `0`. Kerning remains OFF; widths, sidebearings, semantic strings and unrelated glyphs are frozen. Candidate-B zero slash geometry is explicitly isolated from the zero ring.

This advances execution readiness but is not a repaired raster. The connector cannot safely replace the complete source and execute source→font→14/17/24px artifacts atomically, so blind mutation was rejected. General spacing and T022 kerning remain closed.

## Active queue
1. Apply the bounded R1 geometry patch in an inspectable complete-source environment.
2. Run normalized CI with kerning OFF and frozen metrics; capture source/build/font/raster hashes.
3. Critique ambiguity + operational + destructive/retention corpora at 14/17/24px.
4. Only after drawing is defensible, execute general spacing and fallback/notdef recheck.
5. Open kerning only for residual pair-specific defects after general spacing.
6. Keep browser/native and human recognition/task evidence OPEN.

## Cross-domain state
W048 and peers must continue mature fallback; CD054 strings must not be shortened to protect provisional geometry; C048 cannot repair glyph ambiguity; L039 must not freeze provisional metrics.

## Evidence boundary
No R1 mutation, repaired raster, drawing PASS, T021 closure, kerning entry, custom-font production recommendation, native/browser transfer or human recognition PASS is claimed.