# L102 — LogMate Navigation Orientation and Responsive Geometry

Date: 2026-09-20  
Purpose: `TRANSFER VALIDATION` of I098 into spatial systems practice.

## RELATED DOMAIN CHECK
Type T079/T021, Color C110, Interaction I098, Web W108–W110, Content CD114–CD116 checked. Reuse semantic/state boundaries; this note owns spatial relationships only.

## SOURCE
W3C WCAG 2.2 SC 3.2.3 requires repeated navigation to retain relative order unless user-initiated. WAI menu guidance states that responsive menus may collapse/hide items, but items that remain should preserve order, wording and destination. Current-page indication must remain programmatically available, not just spatial/color styling.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-navigation.html
- https://www.w3.org/WAI/tutorials/menus/structure/

## SYNTHESIS
Protected geometry is `destination identity → relative order → current-location cue → target → content relationship`, not a fixed bottom-dock rectangle or global x-coordinate.

## PRACTICE
Stress one canonical destination set across:
- wide rail/top-region candidate;
- narrow bottom-dock or compact-primary candidate where product evidence supports it;
- enlarged text and WCAG text-spacing;
- long but semantically valid labels;
- current destination + focus on another destination;
- transient status/banner and virtual keyboard overlap.

Measure target rectangles, label wrap/truncation, current-state boundary, focus visibility, safe-area/sticky overlap, content occlusion, reading order and route-content start position.

## CRITIQUE
Reject a candidate when responsive adaptation changes destination order/meaning, hides a required primary destination without an equivalent discoverable path, uses current-location styling as the only orientation cue, clips required wording, or allows fixed/sticky navigation to obscure focused/task-critical content.

Do not solve label fit with Type compression. Do not solve geometry with Color salience. Do not infer human discoverability from a clean screenshot.

## Reproducible validation
Same route fixture and sequence as I098; capture geometry at baseline, narrow/reflow, enlarged text, text-spacing, light/night/forced-colors, actual fallback font. Compare semantic order before/after recomposition. Runtime proof belongs with Web.

## HANDOFFS TO OTHER SPECIALISTS
Type gets real label-width/wrap stress; Color gets boundary/focus/current-state overlap cases; Web gets exact geometry captures; Content gets label-fit failures that require recomposition rather than semantic shortening.

## OPEN
Actual production navigation model, safe-area/device measurements, browser chrome/PWA standalone effects, human scan/wayfinding performance.