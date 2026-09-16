# L037 — Destructive-Concurrency Spatial Continuity Contract

## PURPOSE
Transfer L036 concurrent-branch geometry to deletion/update conflicts, where one branch may disappear from the primary live surface.

## INFORMATION SPINE
Preserve a recoverable relationship among: `object identity → current existence/consequence → conflicting branch evidence → delete/restore certainty → safe action → durable history/recheck`.

When an authoritative deletion removes the normal live row/card, the history/recovery path must not disappear with it. Conversely, keeping a ghost row for provenance must not make the object appear live or actionable.

## RESPONSIVE / STATIC STRESS
Test narrow width, 200% text, long localized labels, keyboard focus, list→detail transitions, empty collection after deletion, print/export, and branch/history views. Reflow may change physical order but must not fabricate authority priority. Focus must move to a meaningful surviving target after confirmed removal; it must not fall into an unrelated destructive action.

## FAILURE CONDITIONS
- row disappearance erases access to unresolved outcome/history;
- ghost/tombstone presentation looks like a live actionable record;
- empty state says “no records” while unresolved deletion provenance is the only safe recovery path;
- branch comparison is separated from the action it governs after reflow;
- restore action is spatially presented as trivial undo despite I033 requiring a new mutation;
- page break/export separates deletion certainty from the object/event identity.

## RELATED DOMAIN CHECK
C046 defines visual precedence, I033 authority/action truth, W046 runtime provenance, CD052 semantic labels, and Type remains on mature fallback pending T021. UX human scanning/discoverability evidence remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture geometry/focus before and after removal. Content should preserve enough wording to distinguish ghost/history from live state. Color must not make a historical deleted row look like current destructive action state.

## EVIDENCE BOUNDARY
Spatial contract ready; no executed browser/native/print geometry, AT, or human scanning/task PASS.