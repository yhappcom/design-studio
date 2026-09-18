# CD088 — Semantic Object / Recovery Message Binding

## Purpose
Advance CD087: after list mutation, feedback must describe the semantic object and transaction that actually changed, not the row index that happens to occupy a visual position after recomposition.

## RELATED DOMAIN CHECK
I069 defines semantic focus/action identity; L073 handles locus geometry; C082 handles rendered focus ownership; Type T050 protects strings; W081 handles runtime status evidence. This study owns only the linguistic/semantic binding.

## Semantic contract
Source truth: `transaction_id + semantic_object_id + action + result + resulting_position/group/visibility + recovery_scope + persistence_truth`.

Protected distinctions: visual index ≠ object identity; focus location ≠ changed object; moved ≠ saved; hidden ≠ deleted; Reset ≠ Undo; no-op ≠ failure; locally applied ≠ persisted/synced.

## PRACTICE / CRITIQUE
Stress messages where A moves and B takes A's old index; A becomes hidden; a system group moves as one unit while projecting multiple ledger leaves; Reset changes many items; Undo restores the previous transaction. Reject copy generated from stale index or displayed English label when a stable semantic ID exists.

Visible feedback may be concise, but accessibility/status payload must remain derivable from the same semantic contract. Do not force focus to a status surface merely to announce it. Do not encode product logic in English strings.

## Localization transfer
Keep semantic IDs, professional identifiers and typed variables separate from localized grammar. Test longer locale realizations, bidirectional/layout-direction conditions and compact/full aviation labels without changing state selection.

## Reproducible validation
For every executable mutation compare event truth against visible string and accessibility payload. Classify `SEMANTIC-MATCH`, `STALE-IDENTITY`, `STATE-COLLAPSE`, `LOCALIZATION-BLOCKED`, `NOT-EXECUTED`.

## OPEN
Actual multilingual runtime, linguistic review, AT comprehension and representative-pilot task evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Interaction must expose stable semantic IDs and transaction truth. Web must prove payload/runtime binding. Layout must accommodate necessary wording. Color cannot substitute for object/result language. Type must not compress semantics to fit provisional geometry.