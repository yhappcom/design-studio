# C111 — LogMate Navigation Current/Focus/Status Separation

Date: 2026-09-20  
Purpose: `TRANSFER VALIDATION` of I098/L102 into semantic Color systems.

## RELATED DOMAIN CHECK
T080, I098/L102, W110 direction and CD116 checked. Interaction owns destination/focus/state truth; Color only reinforces it.

## SYNTHESIS
Navigation has independent axes: `current destination`, `keyboard/pointer focus`, `pressed`, `disabled/unavailable`, `notification/status`, and page-local selection. Current destination is persistent orientation; focus is transient input location. They must not collapse into one accent treatment.

## PRACTICE
For each implemented navigation surface, capture light/night/forced-colors conditions with: current+unfocused, noncurrent+focused, current+focused, status badge on current/noncurrent, unavailable action where applicable, and route transition/pending states.

## CRITIQUE
FAIL when:
- current destination is distinguishable only by hue;
- focus and current destination become visually indistinguishable;
- a badge/error color changes the perceived current destination;
- route transition leaves stale current-state paint;
- forced-colors removes the only surviving state boundary;
- decorative brand accent outranks functional orientation/focus.

WCAG contrast requirements remain necessary but are not a proof that semantic state separation is understandable.

## Reproducible validation
Use the I098 route fixture and L102 geometry. Capture semantic state IDs plus rendered boundary/foreground/background under baseline, focus traversal, route transition, Back/Forward and reload. Repeat light/night/forced-colors in served primary and independent engines when available.

## HANDOFFS TO OTHER SPECIALISTS
Layout gets state-boundary geometry constraints; Web captures computed/used runtime behavior; Content must not refer to color as the sole locator; Type supplies actual weight/fallback conditions.

## OPEN
Production palette, rendered navigation implementation, forced-colors cross-engine/device transfer, calibrated-display/glare/night physical evidence, observer/human orientation evidence.