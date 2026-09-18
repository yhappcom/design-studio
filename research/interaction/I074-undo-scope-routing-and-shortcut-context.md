# I074 — Undo scope routing and shortcut context

## PURPOSE
Stage 3 systems practice. Extend I073 branch eligibility to a larger product problem: when multiple editable subsystems coexist, which history owns an Undo invocation?

## RELATED DOMAIN CHECK
- Type: T055 protects recovery strings without changing T021 drawing/spacing/kerning gates.
- Color: C086 separates eligible/stale recovery from focus and restoration.
- Layout: L077 makes recovery-surface geometry subordinate to Interaction truth.
- Web: W086 requires branch/inverse/focus provenance in served runtime.
- Content: CD092 verbalizes current eligible inverse without fabricating persistence.
- UX: no separate canonical UX specialist exists; end-to-end workflow analysis remains cross-cutting.

## SOURCE
Flutter's current Actions/Shortcuts documentation separates key bindings (`Shortcuts`) from contextual intent fulfillment (`Actions`). The same shortcut may map to different actions depending on focused context; Actions can also report whether an intent is enabled. Flutter explicitly notes that action dispatchers can support concerns such as logging and undo/redo. WAI-ARIA APG lists Ctrl+Z / Command+Z as conventional Undo assignments and advises platform-appropriate assignments to reduce browser/system conflicts. WCAG 2.2 SC 2.1.4 constrains single-character shortcuts; modifier-based conventional Undo is not a single-character shortcut case.

## SYNTHESIS
A global-looking Undo chord does not imply one global product history. Invocation routing must resolve an **undo scope** before resolving an eligible inverse inside that scope.

Required provenance:
`invocation_id → input_path → focused_context → scope_id → branch_id → eligible_inverse_tx_id → action_enabled → result`.

Candidate scopes for LogMate-style products:
- text-edit scope (native/editor history);
- display-configuration scope (reorder/hide/group/reset);
- record-edit scope (flight-entry values), if/when implemented;
- page/navigation history is not configuration Undo.

## PRACTICE / ADVERSARIAL SCENARIOS
1. Focus a text field, edit text, then invoke Cmd/Ctrl+Z: configuration history must not steal the command merely because a configuration inverse exists.
2. Focus a Customize reorder control, mutate display configuration, invoke Undo: the current display scope may own the inverse if its contract says so.
3. Move focus from Customize to an unrelated editable field while a display Undo remains eligible: test whether the visible Undo control remains explicit while the keyboard chord routes to the focused editor.
4. Stale/superseded configuration inverse: its Action must not remain enabled merely because the chord is recognized.
5. Button invocation versus shortcut invocation: both may reach the same inverse, but provenance must retain invocation path and focus context.
6. Browser/system-reserved conflicts: do not override a higher-level browser/OS/AT function without explicit, validated rationale.

## CRITIQUE
Failure patterns:
- one app-global Ctrl/Cmd+Z always mutates Customize regardless of focus;
- text editor consumes configuration Undo unexpectedly;
- disabled/stale recovery is still announced as available;
- UI says “Undo” without enough scope/context when multiple histories are simultaneously plausible;
- configuration Undo stack is confused with Flutter FocusScope history or browser navigation history.

## REPRODUCIBLE VALIDATION CONTRACT
For each scenario, capture twice:
- build/commit, platform, engine, keyboard layout;
- invocation path and physical/logical chord;
- focused semantic object/action before/after;
- resolved `scope_id`, `branch_id`, `eligible_inverse_tx_id`;
- `Action.isEnabled`/equivalent before invocation;
- configuration projection hash and editor value before/after;
- visible/accessibility status payload;
- runtime exceptions.

PASS requires exactly the intended scope to mutate; non-owning scopes remain byte/semantic-equivalent. A recognized chord with ambiguous or wrong scope is FAIL even if some state was successfully undone.

## UX INTEGRATION
Information architecture must expose recovery near enough to its owning workflow to reduce scope ambiguity. Discoverability of shortcuts, user expectation of global versus local Undo, cognitive workload and screen-reader comprehension require human evidence and remain OPEN.

## OPEN
Actual LogMate shortcut/action tree, native text-edit integration, macOS/Windows/browser conflicts, independent-engine behavior, AT and representative-pilot evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Content: name recovery from resolved scope, not chord alone.
- Layout: preserve spatial ownership between recovery control and edited subsystem.
- Color: encode eligibility only after scope resolution.
- Web: log contextual Actions/Shortcuts routing and native-editor interception.
- Type: later stress any necessary scope-qualified labels; do not alter T021 gate.
