# CD118 — LogMate Search/Retrieval Content System

Date: 2026-09-20

## RELATED DOMAIN CHECK
I099/L103/T081/C112/W112 checked. CD118 owns product-authored wording/semantic distinctions, not search algorithm or IA.

## Complete content contract
Keep distinct:
`search scope/label ≠ query text ≠ filter/sort ≠ progress ≠ result count ≠ zero-match ≠ retrieval failure ≠ offline/degraded ≠ result identity ≠ selection/open action ≠ return/restoration state`.

Product-authored LogMate UI remains English-only. Source/user Unicode and operational identifiers remain literal stress inputs rather than being translated into product terminology.

## Candidate semantic jobs
- input identifies what can be searched, not merely `Search` when scope would be ambiguous;
- progress says work is occurring without claiming completion;
- count states actual current-result truth;
- zero-match explains absence without implying system failure;
- error/offline wording reflects the actual cause/capability known to runtime;
- Retry means a safe repeat under I099/W112 authority, not blind duplicate work;
- result labels preserve differentiating flight/record identity;
- Clear search/filter actions state their actual scope.

WCAG 2.2 SC 4.1.3 is relevant when progress/count/no-results is presented as a status message without focus movement. SC 3.2.4 supports consistent identification of repeated search functions.

Sources:
- https://www.w3.org/WAI/WCAG22/Understanding/status-messages
- https://www.w3.org/WAI/WCAG22/Understanding/consistent-identification

## FAILURE CONDITIONS
`No results` used for network error; `Search`/`Find` inconsistently names the same repeated function; stale count remains after query changes; source identifiers are normalized into misleading product language; geometry-dependent instructions; content claims restored state when runtime actually re-ran and changed results.

## HUMAN BOUNDARY
Preferred pilot vocabulary, query strategy, discoverability, comprehension, workload and task efficiency remain OPEN; they are not simulated.