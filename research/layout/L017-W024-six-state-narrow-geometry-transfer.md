# L017 — W024 six-state narrow-geometry transfer

Classification: **TRANSFER VALIDATION + SYSTEMS PRACTICE**

## Purpose
Test whether the complete certainty/recovery vocabulary survives spatial recomposition rather than validating only one long unknown-state fixture.

## RELATED DOMAIN CHECK
Type T022 remains metric-flexible; Color C026 owns state-pair contrast; Interaction I012 owns action semantics; Web W024 supplies rendered geometry; Content CD031 owns wording; UX human workload remains open.

## Runtime evidence
W024 executed six semantic states at 1280, 390 and strict 320 CSS px. Across all 18 cases, neither body nor status container developed horizontal overflow. The combined forced-colors/reduced-motion phone run kept the focused sticky Edit control fully within the viewport.

## Spatial verdict
PASS, bounded:
- state title/body/action blocks reflow at 320 CSS px;
- long conflict/offline/unknown recovery text does not require semantic truncation;
- action availability changes do not force horizontal clipping;
- operational literals remain structurally separate from state copy.

OPEN:
- actual 200% browser zoom equivalence;
- overlays/keyboards/safe-area insets;
- native Flutter text scaling;
- tablet product IA beyond the bounded specimen;
- localization expansion beyond current English fixtures;
- human scan/load evidence.

## Handoff
Web may use the six-state matrix as a bounded spatial regression surface. Content need not shorten recovery semantics to preserve 320px geometry. Color still needs exact adjacency if overlays/sticky layers change. Type product metrics remain unresolved for dense numeric columns.

## Verdict
**L017 bounded six-state narrow-geometry transfer PASS; Layout Stage 3 remains PRACTICE.**