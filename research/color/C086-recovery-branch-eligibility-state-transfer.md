# C086 — Recovery branch eligibility state transfer

## Question
Can the visual system distinguish a currently eligible recovery action from consumed, superseded, no-op and failed states after I073 branching history?

## RELATED DOMAIN CHECK
Type T054/T021, Layout L077, Interaction I073, Web W085 and Content CD091 checked. `TRANSFER VALIDATION` of causal eligibility into semantic color/state architecture.

## State axes
Keep independent: current focus owner; selected object; restored object; current recovery eligibility; consumed/superseded recovery; failure; no-op; enabled/disabled; SHOWN/HIDDEN. Do not encode several axes with one generic accent.

## Required visual semantics
- `eligible` may receive actionable treatment but cannot rely on hue alone.
- `consumed/superseded` must not retain success or active-action paint that implies current reversibility.
- `failed` is not a synonym for unavailable/superseded.
- `restored` is not `focused` or `selected`.
- focus indicator ownership follows current semantic focus, not branch history.

Validation chain: `semantic state → token → paint owner → rendered surface → non-color cue → accessible meaning`.

## Accessibility boundary
WCAG 2.2 remains baseline. Focus Visible and Focus Not Obscured are relevant lower-level requirements; Focus Appearance is AAA. Forced-colors transfer must verify that state distinctions survive system-color substitution or are carried by non-color structure/text.

## Runtime matrix
For A→B→Undo B→C, capture light/night/forced-colors screenshots and computed/used state where possible for: current focus, C recovery control, superseded B recovery representation if present, status message, selection. Repeat in primary and independent engine when available.

## Failure conditions
FAIL if stale recovery looks actionable; failure paint is reused for superseded/no-op without semantic cue; restoration highlight masquerades as focus; forced colors erases the only state distinction; or Color implies persistence/Sync not present in product truth.

## OPEN
No rendered C086, forced-colors/independent-engine, calibrated-display, observer or representative-human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies eligibility truth; Content supplies state names; Layout owns locus; Web proves actual browser paint/state; Type must not be compressed to preserve color-led geometry.
