# W088 — IME composition + contextual Undo served-runtime closure

## Purpose
Move W087 from abstract simultaneous histories into a browser/runtime case that matters for Korean localization: active IME composition while display-configuration recovery exists.

## RELATED DOMAIN CHECK
Checked T057, C088, I075, L079 and CD094. Web owns served-browser integration evidence, not the underlying product Undo semantics.

## SOURCE
W3C Input Events Level 2 Working Draft (2026-05-01) defines `historyUndo`/`historyRedo` input types and composition-specific event behavior; composition-process `beforeinput` is generally non-cancellable. UI Events defines composition event sequencing. Flutter exposes composing ranges in `TextEditingValue`; current `EditableText` implementation treats composing text specially in undo-stack coalescing.

These sources establish observable concepts, not cross-browser parity. Input Events Level 2 remains a Working Draft and its implementation reports are still work in progress.

## SERVED-RUNTIME MANIFEST
For each scenario record:
`build/commit, engine/version, OS, locale/IME, viewport, zoom, theme/forced-colors, focused semantic ID, Flutter composing range, editor value/selection, browser composition/input event trace where observable, Flutter intent/action resolution, resolved scope, configuration branch/inverse eligibility, projection hash, visible/a11y status, focus/recovery rectangles, scroll/obscuration, runtime exceptions`.

## REQUIRED SCENARIOS
Run twice in the same production build:
1. active Korean composition + configuration inverse eligible + Cmd/Ctrl+Z;
2. composition committed + editor Undo eligible + configuration inverse eligible;
3. explicit configuration Undo control while editor history exists;
4. focus transfer between editor and recovery control;
5. composition + 200% text/reflow;
6. stale configuration recovery after new branch;
7. navigation/Back interruption while composition is active.

## CLOSURE LADDER
`actual widget/runtime → production Web build → served primary engine → independent engine → 200% → forced-colors`.
A Chromium-only synthetic specimen cannot close this study. Safari/Firefox transfer is particularly valuable because composition/input-event implementation can differ from Chromium.

## CRITIQUE / FAIL
FAIL if one invocation mutates both editor and configuration history, if composition is lost through app-level interception without intended editor/platform behavior, if status is emitted from the chord instead of resolved result, or if visual geometry contradicts the owning scope.

## PERFORMANCE EVIDENCE BOUNDARY
No performance claim is introduced here. Lighthouse/DevTools/CI remain LAB/synthetic. Only provenance-bearing field aggregate/RUM may support FIELD LCP/INP/CLS.

## WCAG 2.2
Use WCAG 2.2 as the current W3C accessibility baseline. Keyboard operability, focus visibility/obscuration, reflow and status semantics remain relevant where applicable. WCAG does not define IME-vs-configuration Undo precedence.

## OPEN
No served W088 execution yet; independent engine, Korean IME on physical devices, forced colors, screen reader, field Core Web Vitals and representative-human evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives routing contradictions; Content receives actual resolved payloads; Layout receives viewport/reflow evidence; Color receives forced-colors evidence; Type receives real fallback/composition rendering only after T021 permits transfer.