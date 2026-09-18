# L077 — Recovery branch replacement locus geometry

## Purpose
Spatial transfer of I073. When Undo is consumed and a new mutation creates the current branch, recovery UI may disappear, change target, or be replaced. Geometry must follow semantic eligibility rather than preserve a stale control merely to avoid layout movement.

## RELATED DOMAIN CHECK
Type T054/T021, Color C085, Interaction I073, Web W085 and Content CD091 were checked. This is `TRANSFER VALIDATION`: I073 owns branch truth; L077 owns spatial continuity after that truth changes.

## Spatial scenarios
Measure at baseline and 200% text/zoom, twice per executable path:
1. recovery control remains but target/label updates to current eligible transaction;
2. consumed recovery control disappears;
3. stale control becomes unavailable without implying failure;
4. new mutation creates a new recovery control;
5. recovery/status surface wraps from one to multiple lines;
6. sticky/bottom recovery surface intersects focused content.

Capture `recovery_surface_rect`, `focus_rect`, `target_rect`, `scroll_offset_before/after`, viewport, safe-area/sticky rectangles, wrapping/line count, obscuration, and semantic owner IDs.

## Acceptance
- Interaction first declares current branch and eligible recovery target.
- Layout may not preserve stale semantics merely to avoid reflow.
- Replacing/removing recovery UI must not cause unexplained large scroll displacement.
- Current focus must remain at least partially visible under WCAG 2.2 Focus Not Obscured (Minimum); Studio critique additionally records displacement and context loss.
- At 200%, wrapping may increase height but must not cover or eject the current semantic locus without an explicit reveal strategy.
- Geometry PASS requires the correct semantic control; a perfectly aligned stale Undo control is a semantic FAIL.

## Critique alternatives
A fixed-height snackbar minimizes movement but risks clipping/localization pressure. A growing inline status preserves content truth but can displace the work locus. A sticky recovery rail preserves availability but can obscure content. No pattern is selected without runtime geometry and product truth.

## OPEN
Actual LogMate recovery UI, non-drag reorder, 200% browser measurements, forced-colors/independent engine, keyboard/safe-area device behavior and human workload remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web should record branch change and geometry in one scenario manifest; Content should supply realistic EN/KO lengths; Color must keep focus and recovery eligibility visually distinct; Type must use mature fallback until T021 gates close.
