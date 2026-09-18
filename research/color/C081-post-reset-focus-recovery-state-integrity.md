# C081 — Post-Reset Focus & Recovery State Integrity

## Purpose
Extend C080 from baseline-aware state tokens into the post-Reset temporal state where focus, baseline, visibility and recovery coexist.

## RELATED DOMAIN CHECK
Type T021/T049, Layout L071/L072, Interaction I067/I068, Web W080, Content CD086/CD087 checked. TRANSFER VALIDATION.

## State matrix
Keep independent axes: `at-baseline|dirty`, `focus owner`, `Reset enabled|no-op`, `recovery available|unavailable`, `visible|hidden`, `success|failure|superseded`, theme/forced-colors.

Examples that must remain distinguishable without color alone:
- at-baseline + focused + Reset no-op;
- restored + focused + Undo available;
- restored + focus moved by explicit rule + Undo available;
- failure + focus retained;
- hidden field + recovery available.

## CRITIQUE
FAIL if focus is conflated with selection/insertion color, no-op with failure/hidden via opacity, or recovery availability is conveyed only by hue. Contrast/token inspection alone is insufficient: acceptance remains semantic state → token → paint owner → rendered surface → non-color cue → accessible meaning.

## Validation
When runtime exists, execute light/night/forced-colors with I068/L072 scenario IDs, then independent engine. Record rendered state and focus visibility. WCAG 2.2 remains the accessibility baseline; forced-colors/browser emulation is not human perception evidence.

## OPEN
No rendered C081 PASS, independent-engine/device, calibrated-display, observer or human evidence.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web must expose actual paint/focus surfaces; Content must preserve non-color meaning; Interaction supplies state truth; Type strings must not be compressed to preserve color-state geometry.