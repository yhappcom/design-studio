# L012 — Three-surface Spatial System

Classification: **SYSTEMS PRACTICE + UX SYNTHESIS**

## RELATED DOMAIN CHECK
- Type T021 remains unstable; compositions must tolerate proportional control and future metric changes.
- Color C020 supplies state/non-color carrier and semantic-token invariants.
- Interaction I007 owns temporal state/navigation/recovery behavior paired with this spatial work.
- Web W019 supplies responsive/runtime evidence but not yet the complete Stage 3 system.
- Content CD019 supplies long/localized consequential strings and semantic state distinctions.

## Fixed task substrate
`lookup → inspect → compare → correct → confirm/recover`

The same task model is composed for three form factors without treating responsive scaling as system coherence.

## Spatial invariants
Across all surfaces:
1. record identity precedes mutable details;
2. current truth state is adjacent to the record/task context it qualifies;
3. consequence/recovery content precedes optional explanation;
4. primary action remains distinguishable from destructive/recovery actions without color alone;
5. reading/task order is stable even when panes collapse;
6. selected record and transient overlay are separate spatial/state layers;
7. focusable controls are not intentionally hidden behind persistent chrome;
8. long content reflows rather than being semantically deleted.

## Adaptive compositions
### Phone
Single primary column. Record list → record identity/header → state → core details → correction/action → recovery detail. Comparison becomes sequential disclosure; transient navigation cannot erase selected-record context.

### Tablet / EFB
Two-region composition when space permits: record/list or summary rail + active detail/work area. Comparison may become adjacent. Touch geometry and interruption recovery take priority over maximum density.

### Desktop / web
Persistent navigation may coexist with list/detail or table/detail. Dense comparison is permitted, but DOM/reading order must still correspond to meaningful task order. Sticky regions must not obscure keyboard focus.

## Stress matrix
- Type metric change: containers use intrinsic/min-max behavior; no fixed widths tied to T021 candidates.
- Content expansion: consequence/recovery regions can grow vertically; truncation cannot remove state certainty.
- Color adverse mode: grouping and hierarchy remain visible through spacing, boundaries, text and native/system affordances.
- 200% text enlargement/zoom: simultaneous columns may collapse; task order remains invariant.
- reduced motion: spatial state change cannot require animation to explain origin/destination.

## Spatial failure tests
FAIL if any surface: changes the semantic task order; moves recovery outside recoverable context; hides state behind a transient layer; requires color to distinguish state; clips consequential text; freezes widths around an unapproved custom font; or makes density more important than target/focus access.

## Gate result
**L012 STATIC SYSTEM CONTRACT: PASS / Stage 3 remains PRACTICE.**

The three compositions are now derived from one invariant model. Rendered three-form-factor geometry, real native/web router behavior, actual zoom/focus, physical EFB and human workload/findability remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- Interaction: I007 binds temporal state/navigation/recovery to these regions.
- Web: W020 should transfer the invariant reading/focus order and adaptive compositions.
- Color: C020 role graph fits without changing meaning by surface.
- Content: long strings remain first-class stress inputs.
- Type: no geometry freeze around T021.