# CD038 — Localization Semantic-Invariant Test Vectors

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / LOCALIZATION TEST CONTRACT / TOOLCHAIN EXECUTION OPEN**

## RELATED DOMAIN CHECK
- **Interaction:** I018/I019 owns certainty, enabled actions and resumption truth.
- **Layout:** L023 owns association/reflow when strings expand.
- **Color:** C032 requires semantic identity independent of hue/string matching.
- **Web:** W032 supplies locale/runtime provenance.
- **Type:** T021 consumes bounded operational strings but cannot force semantic shortening.

## Purpose
CD037 defines the complete content system. CD038 supplies test vectors that detect semantic drift during localization, pseudo-localization, resumption and recovery rather than checking string length alone.

## Canonical semantic vectors
Each locale realization must preserve the semantic ID and the propositions below even when surface wording differs.

| semantic ID | must assert | must not assert | primary action contract |
| --- | --- | --- | --- |
| operation.pending | operation is still awaiting authoritative result | success, failure | wait/check only if available |
| operation.outcomeUnknown | result is not known | failed, safe-to-retry | check outcome |
| operation.confirmed | authoritative commit confirmed | uncertainty | view/continue |
| operation.rejected | authoritative rejection known | transport ambiguity | correct/review |
| operation.reconciledNotFound | authoritative lookup found no committed operation under the fixture contract | universally safe retry | retry only if Interaction/backend permits |
| record.conflict | competing versions/values require resolution | automatic winner | compare/resolve |
| resumption.contextRestored | object/state context restored from durable evidence | new operation dispatched | continue/check as governed |
| resumption.contextIncomplete | required correlation/context unavailable | certainty about prior operation | return/check source |

## Typed-variable rules
Operation IDs, record IDs, dates, times, durations, counts and names remain typed variables; translators must not concatenate fragments that alter grammar or certainty. Date/time/duration formatting belongs to locale-aware tooling. Plural/select logic must be executed, not approximated by English suffix rules.

## Pseudo/expansion vectors
For every consequential message execute:
1. +30–50% expansion condition;
2. long record/object name;
3. long date/time representation;
4. zero/one/many where plural semantics exist;
5. reordered variable condition where grammar permits;
6. missing-resource/fallback condition;
7. resumption after route/reload with the same semantic ID.

## Discrepancy classes
- **S1 truth drift:** certainty/action/consequence changed — blocker.
- **S2 variable contract:** type/order/format assumption invalid — blocker.
- **S3 retrieval continuity:** later surface uses a different term for the same object/state — revise/govern.
- **S4 spatial stress:** semantics intact but fit/association fails — hand to Layout/Web; do not shorten blindly.
- **S5 tone:** semantics intact but register inconsistent — Content revision, lower severity than S1/S2.

## Closure boundary
Static vectors are not a real ARB/ICU/TMS round trip. Stage 3 remains OPEN until resources pass actual tooling/runtime binding and discrepancies are logged. Linguistic quality and human comprehension require appropriate reviewers/users and remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** bind semantic ID + content revision + locale to W032 run IDs.
- **Layout:** consume S4 expansion cases without changing truth.
- **Color:** attach state tokens by semantic ID, never localized string.
- **Type:** use the unchanged operational corpus as rendering stress.
