# CD094 — IME composition and Undo language contract

## Purpose
Extend CD093 contextual command language into Korean/IME editing so user-facing feedback never confuses provisional composition, committed text history and display-configuration recovery.

## RELATED DOMAIN CHECK
Checked T056/T057, C087/C088, I074/I075, L078/L079 and W087. Interaction remains owner of actual command scope; Content only names the resolved truth.

## SOURCE / SYNTHESIS
Flutter defines composing text as provisional IME-controlled text. W3C Input Events distinguishes composition input from `historyUndo`/`historyRedo`. Therefore strings must be generated after runtime scope/result resolution, not from `Cmd/Ctrl+Z` itself.

## CONTENT MODEL
Minimum payload:
`invocation_path, focused_object, composition_active, resolved_scope, inverse_id, changed_object, result, recovery_availability, persistence_truth`.

Protected invariants:
- composing ≠ committed;
- text Undo ≠ display-configuration Undo ≠ browser Back;
- shortcut recognized ≠ action applied;
- current focus ≠ recovery owner;
- restored ≠ focused;
- applied locally ≠ Saved ≠ Synced;
- unavailable ≠ failed ≠ superseded.

## PRACTICE
Develop EN/KO runtime variants only after scope truth exists for:
1. editor Undo while composition/text history owns the command;
2. configuration Undo invoked from its explicit control;
3. configuration recovery unavailable because a newer branch superseded it;
4. no-op invocation;
5. composition commit followed by editor Undo.

Prefer concise visible feedback when context is unambiguous; permit richer accessibility payload when scope/result needs qualification. Do not use wording such as `Saved`, `Synced`, `Returned to …`, or `Undid display change` unless those exact facts are proven.

## CRITIQUE
FAIL if Korean localization converts a provisional composition event into a persistence claim, if one generic `Undo complete` masks which history changed, or if wording instructs users by color alone.

## VALIDATION
Use I075/W088 runtime payloads. Verify actual EN/KO string fit at baseline/200%, accessibility status semantics, and linguistic review before production PASS. Model/static critique is not human comprehension evidence.

## OPEN
Actual Korean wording, professional linguistic review, screen-reader comprehension and representative-pilot task evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Type receives final EN/KO corpus only after wording validation; Layout receives unavoidable string expansion; Color must not replace scope wording with hue; Web must prove runtime scope before emitting status.