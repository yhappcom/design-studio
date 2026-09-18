# I080 — Scroll/drag gesture arbitration and UA pan boundary

Status: PRACTICE / TRANSFER SPEC — runtime evidence OPEN
Date: 2026-09-19

## Question
When LogMate Customize reorder lives inside a scrollable surface, how do we preserve native/user-agent panning while preventing an ambiguous touch stream from being interpreted as both scrolling and reorder intent?

## SOURCE
- WCAG 2.2 SC 2.5.7 requires a single-pointer non-drag alternative for authored dragging functionality. Native/user-agent scrolling is outside that requirement, but authored suppression/reimplementation of scrolling returns responsibility to the content author.
- Pointer Events defines `touch-action` as the declaration that determines which direct-manipulation pan/zoom behaviors the user agent may consume. Once pan/zoom wins, the UA can suppress the pointer stream and issue `pointercancel`; changing `touch-action` after the gesture begins does not retroactively change that decision.
- Flutter gesture recognizers compete in a gesture arena; drag and scroll recognition therefore require explicit runtime evidence rather than assuming that a pointer stream belongs to reorder because it began on a reorder affordance.

## Contract
Separate these identities:
`pointer stream != gesture-arena winner != UA pan owner != reorder preview owner != reorder transaction owner`.

A reorder transaction may commit only after the product recognizer has won the intended reorder gesture and a valid semantic destination is resolved. Scroll ownership, `pointercancel`, arena loss, or UA stream suppression must terminate preview without mutating order or creating Undo history.

Do not solve the conflict by globally disabling native panning. Any `touch-action` restriction must be the minimum needed for the affordance and verified against page/region scrolling and zoom expectations. The non-drag single-pointer alternative remains independently required by I077.

## Scenario families
1. Touch begins on row body and moves vertically: native/Flutter scroll wins; projection unchanged.
2. Touch begins on reorder affordance then resolves to scroll/arena loss: preview clears; no transaction.
3. Valid reorder gesture wins: one semantic move commits; one recovery entry becomes eligible.
4. UA pan begins and emits `pointercancel`: no stale drag owner, candidate or recovery.
5. 200% reflow makes the row taller while touch is active: layout motion does not change gesture authority.
6. Boundary/no-op destination: no success state and no false Undo entry.
7. Non-drag Move control performs the same semantic move without drag and without suppressing scroll.

Each executable family requires two runs before REPLICATION is claimed.

## Evidence manifest
Record: scenario ID, build SHA, browser/OS, pointer type/id, coordinates, scroll offset before/after, `touch-action`/effective direct-manipulation policy where observable, browser pointer event order, Flutter recognizer/arena outcome where instrumented, semantic object/destination IDs, transaction ID, projection hash, recovery eligibility, focus owner, visible/a11y status, target/focus rectangles, 200% state, forced-colors state.

## Acceptance
PASS requires mutually exclusive semantic outcomes: scroll-only, cancelled/no-op, or one committed reorder. A stream that both scrolls and commits reorder without an explicitly designed combined interaction is FAIL. Suppressing native scroll merely to make reorder easier is not accepted without a product-level necessity and an accessible equivalent path.

## Evidence boundary
This is SOURCE→PRACTICE→CRITIQUE→TRANSFER specification, not product runtime proof. Physical touch/pen, representative-pilot usability, motor-error rate, AT comprehension, independent-engine and forced-colors results remain OPEN.

## Related-domain handoff
- Layout: measure scroll displacement, affordance geometry and 200% reflow without redefining semantic ownership.
- Content: never describe arena/capture mechanics as user outcomes; announce only resolved semantic results.
- Color: preview, scroll ownership, commit and recovery must not collapse into one accent state.
- Type: long Move/Cancel/Undo/localized labels may wrap; do not compensate immature drawing with spacing/kerning.
- Web: served runtime must capture browser + Flutter arbitration provenance; synthetic performance remains LAB.