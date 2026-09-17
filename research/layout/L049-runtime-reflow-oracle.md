# L049 — Runtime reflow oracle

Status: PRACTICE / TRANSFER VALIDATION PREPARATION

## PURPOSE
Turn L048 protected semantic groups into observable runtime pass/fail conditions under narrow width, large text/zoom and localization stress.

## RELATED DOMAIN CHECK
T027 distinguishes type pressure from spatial failure; C058 preserves state redundancy; I045 owns behavioral continuity; W057 owns runtime identity; CD063 supplies immutable semantic requirements.

## ORACLE
Protected groups:
- label → value → qualifier;
- field → error → correction;
- state → action → recovery.

Geometry may change rows to columns, wrap, reorder nonessential decoration, or increase page length. It fails when required information/controls overlap, clip, disappear, detach from their semantic partner, require avoidable two-dimensional scrolling for ordinary content, or when focused content is obscured by authored UI.

Record viewport, scale/zoom, locale, group bounding relationships, clipping/overflow, scroll axes, focus visibility and screenshot reference.

## CRITIQUE RULE
Do not solve reflow failure by shrinking below established readable hierarchy, global text-scale clamping, semantic truncation, or moving a required qualifier into undiscoverable disclosure.

## EVIDENCE BOUNDARY
No runtime, physical-device or human task evidence is claimed here.

## HANDOFFS
T027 receives genuine glyph/metric failures; I045 receives focus/recovery failures; W057 records artifacts; CD063 controls semantic deletion decisions.