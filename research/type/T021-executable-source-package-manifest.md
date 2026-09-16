# T021 — Executable Source Package Manifest

Date: 2026-09-16
Evidence class: **PRACTICE / EXECUTION READINESS / BLOCKER REDUCTION**

## RELATED DOMAIN CHECK
- Color C034 cannot repair glyph ambiguity and must not influence drawing closure.
- Layout L025 must not freeze widths from an incomplete candidate.
- Interaction I021 supplies operational state strings but does not redefine Type gates.
- Web W034 continues with mature system/product fonts until this manifest is satisfied.
- Content CD040 supplies unchanged freshness/conflict strings for later proofing.

## Purpose
T021 is now blocked by absence of a verified editable candidate source/build package, not by lack of another spacing theory note. This manifest defines the minimum package required before drawing work can produce canonical evidence.

## Required package
1. editable source file(s) with repository path or immutable artifact identity;
2. source SHA-256 or Git blob/commit identity;
3. units-per-em, ascender, descender, line-gap and glyph-order metadata;
4. deterministic build command and tool/version record;
5. explicit kerning-OFF proof mode;
6. output binary hash;
7. proof command for 14/17/24px H/O/n/o/l/I/1/0 controls;
8. fallback/notdef detection command or reproducible inspection method;
9. before/after proof artifact naming convention;
10. defect ledger classifying drawing → general spacing → raster → fallback → pair-specific residual.

## Decision rule
- Package recovered and identities verified: continue the same T021 candidate.
- Only raster/PDF/SVG proofs recovered without editable continuity: use them as reference evidence, but any reconstructed editable font becomes a **new candidate lineage**.
- Build is nondeterministic or kerning cannot be disabled: execution evidence is invalid until corrected.

## Gate
No kerning work, width-token freeze, production recommendation or product identity integration may bypass this package gate.

## HANDOFFS TO OTHER SPECIALISTS
Web/Layout continue mature-font metrics. Content retains truthful strings without shortening to fit the unfinished candidate. Color/Interaction may provide stress states but cannot close Type evidence.
