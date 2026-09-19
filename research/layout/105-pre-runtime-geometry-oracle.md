# L105 — Pre-runtime protected-geometry oracle

Date: 2026-09-20
Purpose: PRACTICE / TRANSFER VALIDATION planning after L104.

## RELATED DOMAIN CHECK
T082/T083, C113/C114, I100/I101, W113 and CD119 checked. Reuse the same five end-to-end scenarios.

## Protected relationships
Geometry is acceptable when representation may change but these relationships survive: object↔identity; field↔value; item↔reorder action; query↔status/results; current destination↔page; invalid field↔error/recovery; transaction↔status/retry/Undo; comparison values↔local comparison axis.

## Falsification matrix
At baseline, narrow/reflow, enlarged text and WCAG text-spacing, reject implementations where required content is unrecoverably clipped; sticky/fixed UI obscures focus or recovery; target geometry separates an action from its object; reading/action order contradicts task order; horizontal scrolling expands beyond the bounded comparison region without necessity; responsive recomposition changes semantic ownership; route return restores content but not meaningful focus/scroll context.

Identical coordinates are not required. Stable semantic relationships are.

## HANDOFFS TO OTHER SPECIALISTS
Type provides actual resolved metrics; Interaction provides state/action ownership; Color provides state boundaries; Content provides indivisible semantic jobs; Web records rectangles, scroll/sticky regions, viewport and focus provenance.

## Evidence boundary
No Stage 3, runtime, independent-engine, physical-device, AT or human performance PASS is claimed.