# W021 — Cross-domain UX integration review

Classification: **UX INTEGRATION + SYSTEMS CRITIQUE**

UX remains cross-cutting under current governance; this review does not create a new specialist or ownership path.

## End-to-end professional workflow
`find/select record → inspect identity/state → edit → commit → pending → resolve confirmed/known-failure/outcome-unknown → continue/recover`.

## Integration findings
### Information architecture / discoverability
Record identity, current certainty and available safe action form the minimum decision context. Desktop may show more regions simultaneously, but phone disclosure cannot hide the current commit/recovery truth behind unrelated navigation.

### State / feedback / recovery
I008 is authoritative. CD021 names the truth, C021 reinforces it, L013 keeps it spatially connected, and W021 must expose it in DOM/runtime behavior. This prevents a common cross-domain failure: visually polished feedback that asserts more certainty than the system has.

### Cognitive load
Density adaptation is permitted; semantic multiplication is not. A state should have one stable concept/message ID even when surfaces vary. Outcome-unknown deserves interruption priority because it changes the safe action, not because yellow is visually salient.

### Accessibility
WCAG 2.2 conformance is a floor, not evidence of complete usability. Focus visibility/obscuration, non-color state identity, meaningful DOM order, expansion/reflow, reduced-motion equivalence and input-neutral action access are integrated constraints. AT and human evidence remain OPEN.

### Responsive/adaptive consistency
Surface changes may alter simultaneous visibility, persistence and disclosure, but not object identity, certainty, safe action, consequence or recovery. This is the principal invariant connecting L013/I008/CD021/C021/W021.

### Type dependency
T021 custom typography remains outside the integrated acceptance path until drawing validity. W021 should use current product/fallback typography so an immature custom family cannot contaminate layout/content conclusions.

## Cross-domain acceptance contract
A three-surface specimen is invalid if any of these occurs:
1. viewport change alters safe action/state truth;
2. color loss removes state identity;
3. string expansion deletes certainty/recovery;
4. focus is hidden by persistent UI;
5. visual reorder breaks meaningful DOM/task order;
6. operational identifiers are corrupted by localization/bidi handling;
7. local performance diagnostics are reported as field LCP/INP/CLS;
8. deterministic/runtime evidence is described as human usability evidence.

## Result
The studio now has one shared falsifiable Stage-3 integration target across Color, Layout/Interaction, Web and Content while Type remains correctly gated. No human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Each peer should treat the eight failure conditions above as transfer-return triggers. Contradictions discovered in W021 browser execution return to the canonical owning specialist rather than being silently patched in Web.