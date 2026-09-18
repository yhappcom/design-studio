# CD087 — Reset Result & Focus-Neutral Status Contract

## Purpose
Extend CD086 baseline semantics into post-Reset feedback without inventing persistence truth or using focus movement as a substitute for status communication.

## RELATED DOMAIN CHECK
Type T021/T049; Color C080; Layout L071/L072; Interaction I067/I068; Web W080 checked. This is semantic TRANSFER VALIDATION.

## Semantic model
`baseline_identity + mutation_result(changed|no-op|failed) + recovery_scope + persistence_truth -> message_contract -> locale realization`.

Protected distinctions:
- changed Reset ≠ no-op Reset;
- Reset ≠ Undo ≠ erase;
- applied locally ≠ saved ≠ synced;
- hidden ≠ deleted;
- focus location ≠ status meaning.

## PRACTICE
Define payloads, not final universal strings:
1. changed Reset: object + restored baseline + recovery availability;
2. no-op: already at declared baseline; no fake success transaction;
3. failed: what did not change + available recovery/retry;
4. undoable Reset: exact recovery scope and lifetime.

Visible concise feedback may differ from richer accessibility payload while preserving the same truth. Do not force focus onto status solely so it is announced.

## CRITIQUE
Reject `Saved`, `Synced`, `Reset complete` or `Restored` when they conceal unsupported persistence, baseline identity, no-op, failure or recovery scope. Do not use color references as semantic wording.

## Validation
Bind payloads to I068 scenario IDs; run actual localization/runtime before production claims. Evaluate wrapping at 200%, layout direction, accessibility-tree/status behavior and interruption. Human comprehension/AT quality require human/AT evidence.

## OPEN
Actual multilingual runtime, linguistic review, screen-reader behavior, representative-pilot comprehension/workload.

## HANDOFFS TO OTHER SPECIALISTS
Type receives protected strings; Layout receives non-shortenable consequence requirements; Color receives non-color semantic requirements; Interaction receives status/focus separation; Web validates actual browser accessibility/runtime.