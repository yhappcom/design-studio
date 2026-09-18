# C078 — Recovery Status & State-Layer Integrity

Status: **STAGE 3 PRACTICE / OPEN RENDERED TRANSFER**  
Purpose: **EXTENSION** of C076/C077 into reversible mutation states.

## RELATED DOMAIN CHECK
I065 defines transaction truth; L069 defines recovery surfaces; CD084 defines non-color semantic meaning; T046 protects text rendering; W077/W078 own browser evidence.

## State axes
Recovery introduces a new orthogonal axis rather than a new all-purpose accent:
- visibility: SHOWN / HIDDEN;
- interaction: idle / hover / focus / pressed / selected;
- move boundary: can-move / cannot-move;
- mutation: unchanged / moved / undone / reset;
- recovery: unavailable / available / activated / expired;
- persistence: not-applicable / pending / confirmed / failed / ambiguous, only when implemented.

## Acceptance chain
`semantic token → paint owner → visible surface → non-color cue → accessible meaning`.

Test contradictions such as:
- focused moved row + Undo available;
- selected row + boundary-disabled earlier action;
- HIDDEN field + recovery available;
- persistence failure + move visually applied;
- forced-colors where authored recovery accent disappears.

Color must not make `Undo available` indistinguishable from focus/selection, nor encode persistence success merely because the local move is visible.

## Practice matrix
When runtime exists, capture light/night/forced-colors for before move, after move, after Undo and Reset. Compare focus indicator, disabled treatment, status surface boundary and non-color labels/icons. Re-run in an independent browser engine before cross-browser claims.

## CRITIQUE
A success-colored snackbar after every move can falsely imply persistence and compete with focus/selection salience. Mutations that are locally successful but not persisted require separate semantic/state treatment; Color follows that truth rather than inventing it.

## OPEN
No rendered C078 PASS, forced-colors/independent-engine, calibrated display, observer or human evidence.

## HANDOFFS TO OTHER SPECIALISTS
Content: never name color as the sole recovery cue. Layout: preserve focus/status surface separation. Interaction: expose distinct recovery/persistence states. Web: capture computed/used rendering and screenshots in same scenario. Type: no type changes implied.