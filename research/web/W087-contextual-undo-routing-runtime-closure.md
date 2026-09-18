# W087 — Contextual Undo routing served-runtime closure

## PURPOSE
Move Web closure from branch eligibility alone to contextual command routing across native/editor and configuration histories.

## RELATED DOMAIN CHECK
I074 defines scope routing; L078 spatial ownership; C087 visual state separation; CD093 semantic payload; T056 keeps current product evidence on mature fallback.

## SOURCE
Flutter Actions/Shortcuts resolves intents through widget/focus context and allows Actions to determine enabledness. APG documents platform Undo conventions. This makes actual focus/action-tree evidence necessary; a synthetic configuration-state test alone is insufficient.

## RUNTIME MANIFEST
For each scenario record:
- product commit/build, served URL/route, engine/version, OS and keyboard layout;
- invocation path: visible control or shortcut;
- physical/logical chord;
- browser active element / Flutter semantic focus identity where observable;
- resolved intent/action and `isEnabled` equivalent;
- `scope_id`, branch head, eligible inverse transaction;
- text-editor value and selection before/after;
- configuration projection hash before/after;
- visible/accessibility status;
- focus/recovery rectangles, scroll/obscuration;
- console/runtime exceptions.

## SCENARIOS
A. focused text editor + eligible configuration recovery + Cmd/Ctrl+Z;
B. focused Customize control + eligible configuration recovery + Cmd/Ctrl+Z;
C. move focus between scopes before invocation;
D. stale/superseded configuration recovery;
E. visible Undo button versus shortcut for same inverse;
F. 200% recomposition while both histories exist.

Execute twice per available path. PASS requires exactly one intended scope mutation and stable non-owning scope.

## TRANSFER LADDER
actual product/widget → production Web build → served primary engine → independent engine → 200% → forced-colors. Browser/OS/AT shortcut conflicts must be logged rather than normalized away.

## PERFORMANCE EVIDENCE
No change: Lighthouse/DevTools/CI synthetic measurements are LAB. Only provenance-bearing aggregate/RUM can support FIELD LCP/INP/CLS claims.

## OPEN
Executable LogMate Actions/Shortcuts tree, branching Undo, independent browser, forced-colors, screen reader, physical device, representative-pilot use.

## HANDOFFS
Interaction receives routing contradictions; Content receives actual resolved-scope payload; Layout/Color receive runtime geometry/state; Type receives only post-T021 product-transfer findings.
