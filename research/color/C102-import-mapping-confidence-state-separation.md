# C102 — Import mapping confidence/state separation

Status: **STAGE 3 PRACTICE / rendered transfer OPEN**

## RELATED DOMAIN CHECK
I089 defines mapping semantics; L093 owns spatial relationships; CD108 owns wording; W102 owns runtime provenance; T021/T070 constrain text rendering. Purpose: **TRANSFER VALIDATION** of C101 from duplicate classification to schema mapping.

## Semantic axes
Do not collapse:
- mapping provenance: documented exact / source-rule alias / ambiguous / unknown / excluded;
- validation: unvalidated / valid / invalid;
- interaction: idle / hover / focus / selected / edited;
- transaction: proposed / committed / reverted;
- persistence: local / Saved / Synced only when implemented.

`ambiguous` is not automatically `error`; `documented exact` is not `successfully imported`; `excluded` is not `disabled`.

## PRACTICE
Construct token/state matrices for I089 fixture under light, night/dark and forced-colors targets. Require redundant text/icon/structure where state meaning matters; color is reinforcement only.

## CRITIQUE / FAIL
- green exact-mapping paint is read as imported/validated success;
- red ambiguity makes reviewable uncertainty indistinguishable from invalid data;
- focus and mapping status share the same only cue;
- remapping leaves stale previous-status paint;
- forced colors erases the only distinction;
- selected/excluded and valid/invalid collide.

## Reproducible validation
When runtime exists, capture computed/used colors plus screenshots in primary and independent engines, baseline/200%, forced colors, twice per scenario. Pair every color assertion with semantic state and visible/a11y label. Contrast checks alone do not establish semantic discrimination or human comprehension.

## HANDOFFS TO OTHER SPECIALISTS
L093 receives required simultaneous-state cases; CD108 must not reference color alone; W102 captures rendered state/provenance; Type keeps mature fallback until T021 permits custom-font transfer.

## Evidence boundary
No C102 rendered, forced-colors, independent-engine/device, observer or representative-human PASS is claimed.