# I102 — LogMate Home static shell→runtime authority transfer

Date: 2026-09-20
Purpose: **TRANSFER VALIDATION / CONTRADICTION PREVENTION**

## RELATED DOMAIN CHECK
T083/T084, C114/C115, L105, W114, CD120 and latest Home draft reviewed. UX remains cross-cutting; no new ownership path is created.

## Problem
The latest Home draft intentionally contains a Search shell, direct actions, period selectors and ledger rows without inventing SEARCH-001, save/sync or other runtime semantics. Coding can accidentally convert visual affordances into unsupported behavior.

## Authority map
Before implementation, each visible affordance must be assigned one of:
- navigation destination;
- query draft/input only;
- committed selector/filter state;
- record opener;
- mutation trigger;
- informational display.

A static shell is not permission to infer hidden authority. `Search logbook` cannot imply search submission/result behavior until SEARCH-001 is implemented. Period selection must distinguish preview/draft from committed filter state if those differ. Recent-flight row activation must preserve stable record identity and route/history behavior.

## End-to-end fixture
Home → View Logbook → record → Back; Home → Recent Flight → record → Back; Home period selector → changed projection → restore; Search shell → eventual SEARCH-001 only when implemented. For every path capture focus origin, requested action, route/query state, authoritative result, restored focus/scroll/projection and recovery.

## Falsifiers
FAIL if static appearance silently invents:
- search-on-type, result ordering or empty/error behavior;
- save/sync status;
- a dominant primary action not supported by product semantics;
- row click behavior without stable record identity;
- period state that visually changes without a defined authority/projection contract;
- route return that loses prior context.

## UX boundary
Non-human review can verify semantic consistency, focus/order contracts and state-machine completeness. Discoverability, perceived clarity, workload, trust and pilot preference remain OPEN until representative human validation.

## HANDOFFS
Layout receives focus/return/projection relationships; Content receives only implemented state truth; Web must capture route/history/query provenance; Color must inject runtime states rather than infer them from the static render.

## OPEN
Actual coded interactions, NAV/SEARCH runtime closure, AT, physical device/PWA, representative-pilot evidence.