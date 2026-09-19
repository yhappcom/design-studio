# L088 — Route/history focus and viewport geometry

## Goal
Transfer I084 into measurable responsive geometry without confusing browser scroll restoration with semantic focus restoration.

## Practice matrix
At baseline and 200%, run commit/cancel/Undo/Reset followed by route leave→Back/Forward, plus restored document vs new-document return where observable. Capture before/after rectangles for focused control, semantic source row, sticky header/footer, recovery action and viewport; capture scroll offset and layout displacement.

## Acceptance
- Current semantic focus is not fully obscured by author-created content (WCAG 2.2 SC 2.4.11 AA).
- Restored scroll position never substitutes for focus restoration.
- Focus does not attach to a recycled ordinal slot after projection change.
- History traversal does not expose stale drag proxy/candidate geometry.
- At 200%, restored/recovered controls remain operable without clipping or sticky obstruction.

## Critique
Classify displacement as browser history restoration, application scroll correction, responsive reflow, focus-induced scrolling or mutation-driven geometry. Unknown provenance stays OPEN.

## RELATED DOMAIN CHECK
I084 supplies authority; C097 visual semantics; CD103 result language; T066 string stress; W097 served provenance.

## Evidence boundary
No runtime geometry, human spatial-orientation or AT PASS is claimed.

## Sources
- https://www.w3.org/WAI/WCAG22/Understanding/focus-not-obscured-minimum.html
- https://developer.mozilla.org/en-US/docs/Web/API/History/scrollRestoration
