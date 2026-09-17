# I040 — Dependency Graph Integrity Authority Contract

Evidence purpose: **STAGE 3 PRACTICE / SYSTEMS VALIDATION**. Extends I039 from execution over a valid explicit dependency graph to validation and safe behavior when the graph itself is malformed, incomplete or policy-ambiguous.

## RELATED DOMAIN CHECK
- **Type:** mature fallback until T021 repair/spacing gates close.
- **Color:** C053 encodes graph/member truth but does not define it.
- **Layout:** L044 preserves graph-level and member-level hierarchy.
- **Web:** W053 owns executable runtime/reconstruction evidence.
- **Content:** CD059 names graph-integrity states.
- **UX:** deterministic safety does not prove discoverability/comprehension.

## Authority model
Consequential execution requires both member-level eligibility and a graph that is authoritative enough for the applicable production policy. Batch order, row order, timestamps or client reconstruction do not repair missing dependency evidence.

Minimum graph states:
`valid | validationPending | policyUnknown | missingReference | cycleDetected | invalidKnown`.

## Safe execution rules
1. Unknown/malformed dependency policy → safe-block affected consequential members and request/reconcile authoritative policy.
2. Missing prerequisite reference → do not infer success, deletion or independence from absence.
3. Cycle → do not break the cycle by row order, timestamp, lexical ID or client heuristics.
4. Known independent members may proceed only when production policy proves their independence from the invalid subgraph.
5. Cancellation/removal of one queued member must trigger graph revalidation; local removal does not silently rewrite authoritative dependencies.
6. Reload/deep-link/history reconstruction must preserve graph revision and validation result.

## Deterministic scenarios
- q1→q2→q3 valid chain;
- q1↔q2 cycle;
- q2 references missing q0;
- graph policy revision unavailable;
- one invalid subgraph plus one explicitly independent member;
- prerequisite locally cancelled while dependent persists;
- graph changes between enqueue and dispatch;
- response loss during graph revalidation.

## HANDOFFS TO OTHER SPECIALISTS
L044 should expose graph-level cause before member recovery actions. W053 should persist graph/policy revision and validation evidence. C053/CD059 must distinguish graph invalidity from member failure/denial.

## Evidence boundary
No production dependency semantics, native/browser execution, AT, human causal comprehension, workload or task-performance PASS is claimed.