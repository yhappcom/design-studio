# I099 — LogMate Search/Retrieval Authority

Date: 2026-09-20  
Purpose: convert SEARCH-001 from a named blocker into an executable end-to-end UX contract without inventing a new UX owner.

## RELATED DOMAIN CHECK
T081, C112, L103, W112 and CD118 are the companion transfer artifacts. I098 navigation/history remains authoritative for route restoration; I099 owns search/query/result/selection transition semantics only.

## SOURCE
WCAG 2.2 remains the accessibility baseline. WAI APG distinguishes editable combobox input, popup suggestions and listbox option semantics. WCAG SC 4.1.3 distinguishes result/status messages such as `Searching…`, result counts and `No results` from the result content itself; status can be exposed without moving focus. SC 2.4.3 requires sequential focus order to preserve meaning and operability.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/ARIA/apg/patterns/combobox/
- https://www.w3.org/WAI/ARIA/apg/patterns/listbox/
- https://www.w3.org/WAI/WCAG22/Understanding/status-messages
- https://www.w3.org/WAI/WCAG22/Understanding/focus-order

## Authority chain
`query draft ≠ submitted query ≠ retrieval request ≠ returned result set ≠ highlighted/active option ≠ selected result ≠ opened record ≠ browser-history state ≠ restored query/result state`.

Search is not a single text field. Preserve separately:
- query text and normalization policy;
- request identity/version and cancellation/supersession;
- result-set identity/order and result record IDs;
- active/highlighted option versus committed selection;
- transition to record/detail and return restoration;
- empty, no-match, loading, degraded/offline and error states;
- filters/sort when present, without silently folding them into query text.

## Scenario family
1. empty → type → submit → results → open record → Back;
2. edit query after results and ensure stale results/status cannot masquerade as current;
3. zero results versus retrieval error versus offline/degraded;
4. repeated/superseded request where an older response arrives after a newer one;
5. result selection → record edit/cancel/commit → route return;
6. reload/deep-link behavior under actual product addressability;
7. narrow/reflow/enlarged/text-spacing and keyboard-only traversal;
8. clear query/filter and verify state ownership/recovery.

## Interaction rules
- Do not move focus merely to announce routine search progress/count/no-results; use programmatic status semantics where applicable.
- If a combobox/listbox pattern is actually chosen, implement its keyboard/focus contract completely; do not borrow ARIA roles only for styling.
- Result rows that contain multiple independent actions are not automatically valid listbox options; listbox semantics flatten option names and do not support interactive descendants as ordinary result cards.
- Opening a record changes task context; restoring search must reconstruct the correct query/result/filter/scroll contract or explicitly re-run under a documented policy.
- Human discoverability, preferred search model, query vocabulary and pilot task efficiency remain OPEN.

## Failure conditions
Stale response replacing newer results; active option treated as committed selection; `No results` used for network failure; focus theft on routine status; Back returns to wrong query/result context; result identity lost after sort/filter; inaccessible custom popup semantics; hidden query mutation; search and global navigation state conflated.

## STUDIO JUDGMENT
SEARCH-001 is now analyzable and implementable but remains OPEN. No actual LogMate search runtime, AT or representative-human evidence exists.

## HANDOFFS
L103 owns geometry/focus/scroll relationships; C112 owns semantic salience; T081 owns rendering stress; CD118 owns wording/content semantics; W112 owns browser/runtime provenance.