# I075 — IME composition, text history and configuration Undo ownership

## Purpose
Extend I074 contextual Undo routing into the highest-risk localization case: an editable field has an active IME composition while display-configuration recovery also exists. This is `TRANSFER VALIDATION`, not a new global Undo architecture.

## RELATED DOMAIN CHECK
- **Type:** T056 keeps scope-qualified strings subordinate to T021 drawing; Korean/CJK composition adds rendering/fallback stress but cannot justify early spacing/kerning repair.
- **Color:** C087 requires focus, recovery ownership and state paint to remain independent; composition adds a provisional-text state that must not be mistaken for configuration recovery.
- **Layout/Interaction:** I074 resolves focused context before configuration branch eligibility. L078 treats recovery placement as an ownership cue, not the behavior source.
- **Web:** W087 requires served-runtime proof of focused context, Action/Intent scope and editor/configuration state together.
- **Content:** CD093 distinguishes configuration Undo, text Undo and browser Back; Korean IME makes the text-history boundary operational rather than theoretical.

## SOURCE
Flutter `TextEditingValue.composing` defines the composing range as provisional text controlled primarily by the IME/user; an empty range means no active composition. Flutter `EditableTextState` also treats composing text specially in undo-stack coalescing. W3C Input Events Level 2 (Working Draft, 2026-05-01) defines composition-specific input events and `historyUndo`/`historyRedo`; it explicitly notes that composition-process `beforeinput` events are not generally cancellable. UI Events likewise treats composition as a distinct event sequence.

## SYNTHESIS
A global-looking `Cmd/Ctrl+Z` cannot be routed from the chord alone. During active composition there are at least four distinct state owners: IME provisional text, committed editor history, display-configuration history, and browser/navigation history. Configuration recovery must not intercept or mutate composition merely because a configuration inverse is eligible.

## PRACTICE — causal matrix
Record for each invocation:

`scenario_id, platform, engine, focused_semantic_id, composing_range_before/after, committed_text_before/after, selection_before/after, shortcut/intention, resolved_scope, configuration_branch_id, eligible_inverse, configuration_projection_before/after, status_payload, runtime_exception`.

Required families, twice per executable path:
1. active Korean IME composition + eligible configuration Undo + `Cmd/Ctrl+Z`;
2. composition committed, editor history eligible + configuration Undo eligible;
3. composition cancelled by IME/user, then Undo;
4. focus leaves editor for Customize recovery control, then Undo;
5. configuration Undo button invoked while an editor elsewhere retains committed history;
6. browser Back/navigation while composition is active;
7. stale configuration recovery after a new configuration branch.

## CRITIQUE / failure conditions
FAIL if any of the following occurs:
- configuration state changes while the active text/IME context owns the command;
- provisional composing text is reported as saved/committed configuration state;
- composition is destroyed merely by a global shortcut handler with no platform/editor contract;
- editor Undo and configuration Undo both fire from one invocation;
- visible recovery ownership contradicts the resolved runtime scope;
- browser Back is described or executed as configuration Undo.

## REPRODUCIBLE VALIDATION
Start with a known configuration projection and one eligible configuration inverse. Focus a real editable control, enter Korean text until `composing` is non-empty, capture state, invoke the platform shortcut, and capture state again. Repeat after composition commit and after focus moves to the configuration recovery control. A PASS requires exactly one intended history owner to mutate per invocation and all non-owning state to remain unchanged.

## WCAG 2.2 boundary
SC 2.1.1 Keyboard remains relevant to keyboard operability. SC 2.1.4 Character Key Shortcuts concerns printable-character-only shortcuts and does not itself define Ctrl/Cmd+Z routing. WCAG does not specify the product's IME/configuration Undo precedence; that precedence is a product/runtime contract to validate.

## OPEN
- Actual Flutter Web behavior with Korean IMEs on macOS/Windows.
- Safari/Firefox/Chromium differences in composition and history event exposure.
- Screen-reader + IME interaction.
- Human predictability/workload for pilots using Korean/English mixed entry.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** execute this matrix in production served builds; do not infer browser behavior from Flutter widget tests.
- **Content:** generate status only from resolved scope/result; composition is not configuration persistence.
- **Layout/Color:** preserve editor/composition locus and configuration-recovery distinction under 200%/forced colors.
- **Type:** treat Korean composition/fallback as later transfer corpus, not a reason to bypass T021.