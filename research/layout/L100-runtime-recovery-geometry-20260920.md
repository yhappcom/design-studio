# L100 — Runtime recovery geometry

Date: 2026-09-20
Status: Stage 3 PRACTICE / H5 RUNTIME TRANSFER

## Purpose
Ensure offline/retry/update/recovery states remain spatially attributable and operable without destroying SC-A local semantic calibration.

## RELATED DOMAIN CHECK
Checked T078, C109, I096, W108 and CD114. This transfers runtime authority into spatial contracts.

## Spatial contract
Status/recovery UI must remain attributable to the affected object or batch. Sticky/offline banners may summarize global capability but must not obscure focused controls or detach row/form errors from their owner. Reflow may change coordinates, not object→state→action→recovery relationships.

## Practice scenarios
Measure Home/ledger/Add Flight/import under: online baseline, offline banner, pending retry, row/form error, stale-data notice, reload/update recovery, enlarged text and text spacing. Capture focus rectangle, status rectangle, recovery target, sticky regions, scroll displacement and target geometry.

## Critique
FAIL if global banners cover focus; recovery action separates from its consequence; enlarged status text pushes the active object offscreen without recoverable context; local and global failures become visually indistinguishable; or target geometry is sacrificed for density.

## WCAG 2.2 anchors
Focus must not be entirely obscured by author-created content (2.4.11). Pointer targets require the 2.5.8 minimum-size/spacing logic where applicable. Dragging alternatives remain a separate 2.5.7 blocker.

## OPEN
No rendered runtime, independent-engine/device, AT or human workload PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture these rectangles with route/network provenance; Color must preserve state distinction; Content must keep status/recovery semantics intact under reflow; Type fallback metrics are an input to this geometry.