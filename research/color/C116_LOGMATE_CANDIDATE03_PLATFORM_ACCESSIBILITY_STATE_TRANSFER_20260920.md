# C116 — LogMate Candidate 03 Platform Accessibility-State Transfer — 2026-09-20

Status: **TRANSFER VALIDATION PLAN / STAGE 3 NOT PASSED**

## Purpose
Candidate 03's scarce accent passed static owner-review gating. This study defines the next Color evidence: whether semantic rank survives actual Flutter platform accessibility modes and injected consequence-bearing states.

## SOURCE
Flutter exposes platform accessibility features through MediaQuery/AccessibilityFeatures, including high contrast and related settings, and recommends contrast, grayscale/color-vision and large-scale testing. Flutter's Accessibility Guideline API can test text contrast, target size and labels.

Sources:
- https://docs.flutter.dev/ui/accessibility
- https://docs.flutter.dev/ui/accessibility/ui-design-and-styling
- https://docs.flutter.dev/ui/accessibility/accessibility-testing

## PRACTICE — state matrix
On the coded Candidate 03 fixture, preserve independent axes for:
1. brand/accent;
2. focus;
3. current/selected state;
4. invalid/error;
5. pending;
6. offline/degraded;
7. recovery/Undo;
8. evidenced success only after authoritative success.

Test light/night plus platform high-contrast where supported. Flutter Web forced-colors remains a separate Web transfer condition; native high-contrast must not be mislabeled as CSS forced-colors.

## CRITIQUE / failure conditions
FAIL if:
- mint accent becomes the sole cue for current/focus/action identity;
- pending/offline/error collapse into one generic red state;
- success color appears before authoritative persistence evidence;
- high-contrast transformation removes the non-color boundary between interactive/state roles;
- text scaling/reflow causes state indicators to detach from the object they describe.

## Reproducible validation
Use stable semantic/state IDs and capture each injected state under the same fixture, scale, theme and platform setting. Record contrast calculations as LAB evidence; preserve screenshots/runtime captures separately. Human salience/readability is not inferred from ratios.

## RELATED DOMAIN CHECK
- Type: T085 may grow rows/labels; Color state ownership must follow the object.
- Layout/Interaction: I102/L106 define object/state geometry.
- Web: W115 records platform/browser provenance and keeps native high-contrast distinct from web forced-colors.
- Content: CD121 prohibits invented state wording; injected states use canonical test labels only.

## HANDOFFS TO OTHER SPECIALISTS
Web should label accessibility-mode provenance precisely. Interaction should provide authoritative injected state fixtures. Layout should flag any state indicator detached by reflow. Content should keep verbal state truth available when color is transformed.

## OPEN
No production palette, native high-contrast, web forced-colors, calibrated-display, glare/night, observer or human PASS is claimed.