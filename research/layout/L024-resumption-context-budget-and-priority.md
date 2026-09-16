# L024 — Resumption context budget and priority

Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / OPEN**

## RELATED DOMAIN CHECK
I020 defines required resumption information; C033 tests cue degradation; CD038 provides semantic invariants; W032 executes responsive/browser transfer; T021 blocks custom metric freezing.

## Spatial priority
On interruption/resumption surfaces, preserve this semantic order before secondary chrome: object identity → current certainty/state → consequence/recovery explanation → safe primary action → history/detail path → secondary actions. Responsive recomposition may change columns/regions but not this relationship.

## Budget test
At baseline, 320 CSS px reflow, actual 200% zoom, text enlargement and keyboard-reduced viewport where executable, record whether required context remains present, associated and reachable without two-dimensional scrolling except where WCAG permits it. Sticky/fixed layers must be tested separately for focus obscuration.

## Failure classes
- **association:** action visually detaches from the state/object it affects;
- **priority:** secondary chrome precedes recovery-critical context;
- **reachability:** safe action/history path exists but is inaccessible in the active viewport/input mode;
- **occlusion:** authored layer hides focused/recovery-critical content;
- **density:** truncation/removal deletes required semantic fields.

These are geometry/structure failures, not human workload claims.

## HANDOFFS TO OTHER SPECIALISTS
Web captures real viewport/visualViewport/rect evidence. Content identifies fields that may not be dropped. Interaction determines safe action availability. Color verifies state survives mode changes. Type provides final metrics only after T021.
