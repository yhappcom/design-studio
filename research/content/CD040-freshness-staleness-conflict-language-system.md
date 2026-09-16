# CD040 — Freshness / staleness / conflict language system

Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / LOCALIZATION TOOLCHAIN OPEN**

## RELATED DOMAIN CHECK
I021 owns whether freshness is known and which actions are safe; L025 owns spatial priority; W034 owns browser restoration/authority provenance; C034 verifies semantic survival without authored hue; T021 owns identifier rendering.

## Content gap
CD039 covers resumption and retrieval, but a restored surface may show last-known data without current authority. Content needs a semantic distinction that does not turn “screen restored” into “data current.”

## Semantic IDs
Maintain distinct IDs even when concise localized wording later converges:
- `restored.authorityChecking`
- `restored.lastKnown`
- `restored.currentConfirmed`
- `restored.authorityUnavailable`
- `restored.conflict`
- `restored.historyUnavailable`

## Required information
Where relevant, bind typed variables for object identifier, local revision/time, authoritative revision/time, last successful check, operation reference and safe action. Dates/times must state the event they describe; a timestamp beside a record must not ambiguously imply “last synced,” “last edited,” or “confirmed current.”

## Language invariants
- Do not use “Up to date” until the product contract establishes current authority.
- Do not convert “last known” into “current” for brevity.
- Do not use “Sync failed” when the authoritative outcome is unknown.
- Do not hide conflict behind generic “Updated.”
- Do not imply a retry is safe unless Interaction exposes it as safe.
- Localization may reorder clauses and choose idiomatic tense/aspect but may not strengthen certainty or erase the distinction between observation time and authoritative state time.

## Complete-system integration
Forms/onboarding should explain only durable concepts users need; recovery screens carry immediate certainty/consequence; retrieval/history surfaces preserve object/revision semantics; tone becomes concise under operational pressure without becoming falsely reassuring. Search/retrieval results that may be stale must expose freshness semantics before an action whose safety depends on current state.

## Closure evidence
Stage-3 Content still requires actual ARB/ICU or equivalent execution, pseudo-expansion, plural/select/date/time/duration cases, missing-resource/fallback behavior, runtime semantic-ID binding, linguistic review and later human comprehension/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies truth/action availability. Web supplies restoration/check provenance. Layout protects freshness/conflict priority. Color verifies non-color survival. Type validates identifier/revision rendering after T021.