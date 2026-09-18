# C075 — LogMate Customize State-Visibility Transfer

Date: 2026-09-18
Mode: **TRANSFER VALIDATION**
Stage: 3 PRACTICE / NOT PASSED

## Question
Can Customize expose visible/hidden, focus, selection, drag/reorder and disabled states without semantic dependence on color?

## SOURCE
LogMate's current configuration contract divides one catalog into visible/ON and hidden/OFF items, supports immediate toggles and reorder, Reset, system Field Groups, and a disabled `+ Custom Field` entry point. Widget evidence covers drag lift, placeholder/insertion behavior and visibility changes, but independent-engine/forced-colors/device evidence is absent.

WCAG 2.2 remains the normative accessibility baseline. Color state is therefore supporting evidence, not the sole semantic channel; focus and pointer targets must also survive actual browser/platform rendering.

## PRACTICE MATRIX
Validate these intersections rather than isolated tokens:
- SHOWN + idle/focus/pressed;
- HIDDEN + idle/focus/pressed;
- selected/reorder source + drag lift;
- insertion destination + focus;
- disabled Custom Field + hover/focus where applicable;
- Reset + focus/pressed;
- light/night/forced-colors;
- semantic aviation content with dense ledger background adjacent to Customize chrome.

For each capture: semantic token, actual paint owner, visible surface, foreground/background pair, non-color cue, accessibility name/state, and screenshot/raster where useful.

## CRITIQUE
A green/red or saturated/desaturated distinction for SHOWN/HIDDEN would be semantically fragile. The switch state, section placement and text/state semantics already provide stronger redundant channels. Color should reinforce those channels, not replace them.

Drag lift and insertion feedback need enough visual salience to guide direct manipulation, but motion/color-only feedback is insufficient. Forced-colors may replace authored colors; structural indicators and native/system-compatible focus remain necessary.

## REPRODUCIBLE VALIDATION
Run the same semantic scenario IDs in light, night and forced-colors/browser override conditions after Web exposes the surface. Record TOKEN_PASS separately from RENDER_PASS. Any `TOKEN_PASS / RENDER_FAIL` remains a Color failure.

## RELATED DOMAIN CHECK
- **Type:** compact labels and state text determine real foreground raster.
- **Layout/Interaction:** state meaning and insertion geometry are not Color-owned.
- **Web:** browser forced-colors and focus rendering are decisive transfer contexts.
- **Content:** SHOWN/HIDDEN/Reset semantics must survive without color references.

## HANDOFFS TO OTHER SPECIALISTS
Web should add forced-colors and independent-engine coverage. Interaction should provide state IDs. Content should avoid color-only instructions. Layout should preserve insertion/focus geometry under dense lists.

## OPEN
Forced-colors runtime, independent browser, native platform, calibrated display, observer/representative-human evidence.

## Conclusion
C075 extends Color from auth-state evidence to configuration-state systems. It does not justify Stage 3 PASS until actual override/browser/device transfer is executed.