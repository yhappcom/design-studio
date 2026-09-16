# CD039 — Resumption / retrieval content closure matrix

Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / TOOLCHAIN OPEN**

## RELATED DOMAIN CHECK
I020 owns certainty/action safety; L024 owns information priority/reachability; C033 tests semantic survival without authored hue; W033 owns runtime routes/captures; T021 owns glyph/rendering validity.

## Purpose
CD037–CD038 established complete workflow semantics and localization invariants. CD039 closes a remaining content-system gap: what the user-facing interface must say when a task is resumed or retrieved after interruption.

## Matrix
For each semantic state (`pending`, `outcomeUnknown`, `confirmed`, `rejected`, `reconciledNotFound`, `conflict`, `historyUnavailable`) define separately:
- object identifier label/value;
- last-operation reference when available;
- state heading;
- consequence/recovery explanation;
- safe primary action label;
- history/detail action;
- unavailable-data explanation;
- localization variables and formatting type;
- revision/semantic ID.

## Content rules
Do not imply recency from screen arrival alone. Do not say “failed” for outcome-unknown. Do not say “not sent/not saved” merely because reconciliation returned not-found unless the product contract makes that conclusion authoritative. Do not hide a conflict behind generic “updated” language. Do not shorten object identity or consequence text merely to fit a preferred layout.

Tone may become concise under recovery pressure, but certainty, consequence and action safety are invariant. Localization may reorder clauses but may not strengthen certainty or invent an available action.

## Closure evidence
Static matrix completeness is not Content Stage-3 closure. Required future evidence remains actual ARB/ICU or equivalent localization-tool execution, pseudo-expansion, plural/select/date/time/duration cases, runtime binding to W033 semantic IDs, linguistic review and later human comprehension/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction validates available actions and certainty. Layout protects information priority. Web binds route/runtime state. Color verifies non-color survival. Type validates identifier/string rendering.
