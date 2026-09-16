# L013 — Three-surface recomposition assertions

Classification: **SYSTEMS PRACTICE + TRANSFER PREPARATION**

## RELATED DOMAIN CHECK
Type T021 metrics remain unfrozen; C020/C021 supplies semantic state roles; I007 supplies state truth; W020 requires browser transfer; CD020 supplies stable message IDs and expansion requirements.

## Fixed professional-record model
One record task is expressed across phone, tablet/EFB and desktop/web. The surfaces may recompose, but they may not change task truth.

### Invariants
- record identity precedes editable detail;
- save/commit state remains adjacent enough to the affected object to preserve causality;
- outcome-unknown remains more prominent than secondary metadata and blocks blind retry;
- recovery action follows the state explanation in reading/task order;
- keyboard/focus order follows meaningful task order rather than CSS visual placement;
- expanded/localized strings may increase height but may not delete certainty, consequence or recovery content;
- no critical action is hidden solely because viewport width changes.

### Adaptive composition
**Phone:** one primary column; detail regions disclose progressively; persistent bottom action may exist only if it does not obscure focused content/status.

**Tablet/EFB:** record list/selection and detail may coexist; selection state must remain explicit and interruption-safe; transient overlays may not erase recovery context.

**Desktop/web:** navigation/list/detail may coexist; denser simultaneous regions are permitted, but DOM/task order must remain coherent when CSS rearranges columns.

## Stress assertions
1. **Type/fallback:** +20% line-box or width change must reflow, not clip identifiers or recovery text.
2. **Localization:** pseudo-expanded labels/messages may wrap; action identity and certainty cannot be abbreviated away to restore one-line geometry.
3. **200% text/zoom:** content must recompose rather than require two-dimensional scrolling for ordinary record editing; exceptions require content-specific justification.
4. **Color loss:** consequential state survives with text/icon/structure.
5. **Focus:** sticky header/footer/overlay cannot fully hide the focused target; remediation may use scroll padding, repositioning or layout change.
6. **Reduced motion:** transition meaning survives without animation.
7. **Offline/stale:** status remains attached to the affected scope, not only a global banner if object certainty differs.

## Deterministic model
For each surface, state transition is evaluated as:
`selected object + edit state + commit state + connectivity/certainty + viewport class → regions + order + visible actions + recovery affordance`.

A recomposition is invalid if the same semantic input changes the safe action merely because viewport class changed.

## Gate result
**STATIC/DETERMINISTIC SYSTEM CONTRACT PASS; RENDERED TRANSFER OPEN.**
No claim is made for native/web rendering, actual 200% zoom, AT, physical device or human task performance.

## HANDOFFS TO OTHER SPECIALISTS
- Interaction I008 should use the same state tuple and assert action/retry invariants.
- Web W021 can implement these exact three surface contracts.
- Content CD021 should provide expanded strings without semantic deletion.
- Color C021 state carriers plug into these regions; color alone never establishes state.