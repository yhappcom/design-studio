# I041 — Coherent owner-review gate vs internal iteration

Evidence purpose: **TRANSFER VALIDATION / PROCESS CRITIQUE**

## RELATED DOMAIN CHECK
L045 product hierarchy; T022 string stress; C054 semantic outcome cues; W053 runtime evidence; CD059 state language.

## Finding
Real-product transfer exposed a process failure mode: requesting owner/human review after every small component mutation creates review fatigue and produces weak evidence because the evaluator sees fragments without the surrounding workflow.

## STUDIO JUDGMENT
Separate two loops:
1. internal deterministic loop — specialist critique, implementation, automated/state/responsive/accessibility stress, cross-domain reconciliation;
2. coherent human gate — present a sufficiently complete workflow/system so the reviewer can judge hierarchy, continuity and product-level trade-offs.

Human review at the second gate is still owner/expert evidence, not representative-user usability evidence. It must not be promoted to population-level comprehension/task-performance claims.

## Failure conditions
Do not defer human review so long that irreversible architecture is locked in; do not ask humans to validate claims that deterministic tooling can cheaply falsify first; do not aggregate contradictory states into a polished demo.

## OPEN
Representative user research, task timing, workload and discoverability remain open.

## HANDOFFS
All specialists should package cross-domain evidence before owner review; Web/native implementation should provide stable build identity and scenario corpus.