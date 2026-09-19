# I092 — LogMate Signature-Code Workflow Transfer Audit

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION PLAN — no gate promotion**

## PURPOSE
Test whether the completed signature candidates remain functional across end-to-end professional workflows rather than only across static surfaces.

## RELATED DOMAIN CHECK
T074/T073, C105/C104, L095, W104, CD110 and the coordinator Operational Geometry/Signature Code contracts were checked. No separate UX specialist exists; UX remains cross-cutting.

## WORKFLOW TRANSFER MODEL
A signature is not transferred merely because two screens look related. Transfer requires preservation of semantic identity, action consequence, feedback, recovery and input equivalence across a task.

### Workflow A — Add Flight
open → enter required operational data → validation → optional details → review/save intent → result/recovery.

### Workflow B — Ledger retrieval/edit
find record → inspect comparison axes → open/edit → validate → commit/cancel → return with focus/context restoration.

### Workflow C — Customize/reorder
identify object → move via drag or required non-drag single-pointer path → candidate destination → commit/cancel → Undo/Reset.

### Workflow D — Import
acquire file → source/mapping → normalize/validate → duplicate resolution → preview → commit → Undo.

## SIGNATURE AUDIT
- SC-A must aid comparison without changing object identity when rows move, reflow or restore.
- SC-B must distinguish authored UI from operational data without changing interaction semantics.
- SC-C must stay quiet at rest but become explicit at the exact state/action owner.
- SC-D must preserve truthful inverse/recovery and must not use motion as sole feedback.

## HARD FAILURE CONDITIONS
- drag remains the only single-pointer reorder mechanism where WCAG 2.2 SC 2.5.7 applies;
- browser restoration is presented as product Save/Sync truth;
- focus restoration targets ordinal position rather than stable semantic object;
- quiet boundary treatment hides action ownership or recovery;
- visual continuity masks a failed/ambiguous transaction;
- Home bottom dock is promoted into app-wide navigation semantics before NAV-001 closes.

## UX INTEGRATION
Non-human review can establish structural consistency, state-machine integrity, target/focus geometry and semantic equivalence. It cannot establish discoverability, cognitive load, trust, comprehension or representative-pilot task performance. Those remain OPEN.

## NEXT EXECUTABLE VALIDATION
When concept/runtime exists, execute each applicable workflow twice at baseline and enlarged text, then independent engine and physical touch device where relevant. Record stable semantic IDs, focus, state transition, inverse availability and recovery result.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: couple workflow state ownership to local geometry, not fixed screen coordinates.
- Web: preserve event/provenance logs across route/network/browser lifecycle.
- Content: visible/a11y messages must derive from actual transaction state.
- Color: state salience must survive authored-color loss.