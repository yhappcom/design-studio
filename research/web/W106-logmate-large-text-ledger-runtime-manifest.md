# W106 — LogMate Large-Text Ledger Runtime Manifest

Status: **STAGE 3 PRACTICE / PRODUCTION TRANSFER PLAN — no runtime PASS**

## PURPOSE
Turn H2 large-text ledger adaptation into observable browser evidence instead of a static responsive claim.

## RELATED DOMAIN CHECK
Type T075, Color C106, Interaction I093, Layout L097 and Content CD112 checked. W105 promotion ladder retained. Current official W3C WCAG 2.2 guidance checked for Reflow 1.4.10, Text Spacing 1.4.12, Focus Not Obscured 2.4.11 and Target Size 2.5.8.

## SOURCE BOUNDARIES
- Reflow allows a scoped exception for two-dimensional data tables/grids where that layout is necessary for meaning/function; it does not excuse unrelated page content or automatically excuse individual cell content.
- Text Spacing requires no content/function loss under the specified spacing overrides.
- Focus Not Obscured (Minimum) requires the focused component not be entirely hidden by author-created content.
- Target Size (Minimum) establishes 24×24 CSS px or qualifying exceptions/spacing for pointer targets.
These are separate checks.

## RUNTIME MATRIX
Execute each chosen L097 mode through:
- production Web build, not isolated specimen only;
- served primary engine;
- independent engine;
- baseline viewport;
- 200% text enlargement/zoom condition;
- 320 CSS-px-equivalent reflow condition where applicable;
- WCAG text-spacing override;
- light/night;
- forced-colors;
- reduced-motion where transitions occur;
- actual production font load and forced fallback;
- real route return after opening a record/detail.

Replicate executable scenario families twice.

## REQUIRED PROVENANCE
Capture per scenario:
- build/commit and route;
- engine/version and viewport/zoom;
- actual loaded font/fallback;
- semantic record/field IDs;
- selected/focused object IDs;
- visible + accessibility payload;
- L097 geometry/scroll/sticky rectangles;
- clipping/overflow/ellipsis/reveal state;
- target rectangles;
- validation/transaction/recovery state;
- screenshot or trace references.

## PASS / FAIL BOUNDARY
A static concept or isolated Chromium screenshot can falsify a design but cannot promote H2. Promotion requires the production path and at least one independent engine. Physical mobile/iPad evidence remains required where native browser chrome, touch, virtual keyboard or platform behavior materially affects the result.

## PERFORMANCE BOUNDARY
Lighthouse, DevTools and CI traces remain **LAB** evidence. Layout changes may alter synthetic LCP/INP/CLS, but these metrics become FIELD evidence only from provenance-bearing representative RUM/aggregate data. Do not label synthetic deltas as field performance.

## SYNTHESIS
The correct large-text ledger question is not “does the table fit?” It is “does the chosen representation preserve record truth, comparison, focus/action/recovery and complete content under real browser adaptation?” W106 makes that claim observable.

## OPEN
No W106 runtime has been executed. No independent-browser, physical-device, screen-reader, field Core Web Vitals or human usability PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
- Type: actual loaded-font evidence decides whether metric assumptions transferred.
- Color: forced-colors/light/night screenshots must preserve state hierarchy.
- Layout/Interaction: runtime geometry/focus/scroll traces adjudicate adaptation modes.
- Content: accessibility payload and reveal behavior adjudicate semantic preservation.
