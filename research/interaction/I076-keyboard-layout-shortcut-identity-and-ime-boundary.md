# I076 — Keyboard-layout shortcut identity and IME boundary

Date: 2026-09-19
Stage: 3 PRACTICE
Purpose: TRANSFER VALIDATION of I074–I075 from focus/IME ownership to keyboard-layout identity.

## RELATED DOMAIN CHECK

- Type T057: Korean/Latin mixed-script and composition remain rendering transfer, not shortcut semantics.
- Color C088: focus/composition/recovery paint cannot define command ownership.
- Layout L079: geometry is evaluated only after semantic owner resolution.
- Web W088: browser/runtime must prove actual event/action routing; framework concepts are not browser parity.
- Content CD094: feedback is generated from resolved scope/result, not the chord.

## SOURCE

Flutter `HardwareKeyboard` exposes physical key, logical key and produced character as distinct event information. Flutter also states that `KeyEvent.character` does not account for IME edits; composing text belongs in text-editing widgets. Flutter Shortcuts supports activators based on key identity or produced character. WCAG 2.2 SC 2.1.4 applies when a shortcut uses only printable character keys; it requires an off/remap/focus-only mechanism. Modifier chords such as Ctrl/Cmd+Z are therefore a different class from single-character accelerators.

## PRACTICE — identity ledger

For every shortcut scenario record: `platform`, `keyboard_layout`, `input_method`, `composition_active`, `physical_key`, `logical_key`, `character`, modifiers, focused semantic owner, matched activator, resolved Intent/Action, scope, eligibility, result, and whether the event was consumed.

Test families:
1. US-layout Ctrl/Cmd+Z with editor/configuration histories.
2. Korean layout with IME inactive and active.
3. Layout switch while focus remains in the same editor.
4. Dead/combining-key sequence adjacent to application shortcuts.
5. Printable-character accelerator, if introduced, under alternate layout and speech-input risk.
6. Explicit Undo button versus keyboard shortcut equivalence.

## CRITIQUE / failure conditions

FAIL when physical position is treated as semantic command identity without product rationale; when a produced printable character accidentally activates a command during text entry/composition; when layout switch silently changes command ownership; when a shortcut is reported successful before resolved Action/result; or when a character-only shortcut lacks the SC 2.1.4 safeguard.

`physical key ≠ logical key ≠ produced character ≠ IME composition ≠ resolved command`.

## REPRODUCIBLE VALIDATION

Run each available family twice with the same scenario ID. Compare state projection, editor value/selection/composing range, configuration branch/inverse, focus owner and feedback. A runtime PASS requires identical intended product consequence across supported layouts, or an explicitly documented platform/layout exception.

## TRANSFER / OPEN

Actual Korean hardware/IME, alternate physical layouts, independent browser engines, screen readers, speech input and representative-pilot expectations remain OPEN. This study does not claim WCAG conformance or product shortcut correctness before runtime evidence.

## HANDOFFS TO OTHER SPECIALISTS

Content: never infer command wording from key glyph alone. Web: capture all identity layers and actual browser/framework routing. Layout/Color: render shortcut hints without implying unavailable ownership. Type: later stress shortcut legends and Korean/Latin fallback only after T021 permits transfer.