# CD086 — Reset Baseline & Consequence Language Contract

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION + CONTRADICTION REVIEW** of CD084–CD085 using I067 baseline provenance.

## RELATED DOMAIN CHECK
I067 owns Reset target/transaction truth; L071 owns surface geometry; C080 owns state encoding; T049 owns rendering; W080 owns runtime semantics. No separate UX owner exists.

## Semantic invariants
- `Reset ≠ Undo`.
- `Reset display ≠ erase flight data`.
- `product default ≠ session-entry state ≠ last saved ≠ last synced`.
- `Applied locally ≠ Saved ≠ Synced`.
- `Already at baseline ≠ Reset succeeded after a change`.
- English wording never selects the underlying baseline state.

## Content model
Each Reset payload derives from structured truth: `baseline_kind`, `baseline_name/version if exposed`, `affected_scope`, `change_count if reliable`, `recovery_available`, `commit_state`, `navigation_effect`.

Candidate patterns must be tested, not assumed:
- action-only when consequence is low-risk and obvious;
- concise inline consequence + Undo;
- preview/confirmation when consequence breadth or irreversibility justifies interruption.

Avoid generic claims such as `Reset everything`, `Restore`, or `Saved` unless system truth supports the object, target and persistence consequence.

## Localization stress
Test long German-like expansion, Korean/Japanese compact forms, RTL ordering, numerals/position tokens, and aviation abbreviations without translating canonical aviation identifiers incorrectly. Semantic IDs, not English strings, select state.

## Acceptance
Visible and accessible language identifies the object and target baseline sufficiently for the chosen architecture; no wording implies data deletion, persistence or sync that did not occur; no-op Reset does not announce a false successful change.

## OPEN
No production wording, multilingual runtime, linguistic review, AT comprehension or pilot comprehension PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Type receives protected strings after baseline truth is fixed; Layout receives expansion pressure; Color must not substitute color for baseline/consequence language; Web validates visible/accessibility output; Interaction remains source of truth.