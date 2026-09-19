# C109 — Runtime state salience under degradation

Date: 2026-09-20
Status: Stage 3 PRACTICE / H5 RUNTIME TRANSFER

## Purpose
Test whether C108 semantic salience survives offline, retry, stale-data, update/reload and font-fallback conditions without turning infrastructure state into decorative noise.

## RELATED DOMAIN CHECK
Checked T077/T078, I095/L099, W108 and CD114. Reuses their object/state/recovery and runtime provenance contracts. TRANSFER VALIDATION.

## State separation
Keep distinct: offline capability, pending/retrying, stale/possibly stale, local commit, persistence failure, Saved, Synced, validation error, ambiguity, selection/focus and recovery availability. Brand accent remains subordinate.

## Critique
FAIL if offline is painted as generic error when work remains available; if stale and failed are merged; if success color appears before persistence truth; if a retry clears error color while the underlying state is unresolved; or if fallback/reflow causes focus/validation boundary loss.

## Reproducible validation
Capture semantic state ID plus rendered boundary/focus/status treatment in light/night/forced-colors for first load, offline launch, reconnect/retry, stale refresh, commit failure/recovery and reload. Repeat stale-state cleanup after each transition.

## OPEN
No production palette, rendered C109, calibrated-display/glare/night, independent-engine/device or representative-human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction/Content must provide actual state truth; Web must capture runtime provenance; Layout must preserve state ownership after reflow; Type fallback must not be encoded as semantic status.