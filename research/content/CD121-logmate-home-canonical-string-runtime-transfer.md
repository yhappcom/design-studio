# CD121 — LogMate Home canonical-string→runtime transfer

Date: 2026-09-20
Purpose: **TRANSFER VALIDATION / COMPLETE CONTENT SYSTEM**

## RELATED DOMAIN CHECK
T084, C115, I102/L106, W114 and CD120 reviewed. Latest Home draft deliberately forbids invented greeting, pilot identity, slogan, weather, sync state and airline branding.

## Canonical fixture
Product-authored UI remains English-only. Current Home fixture uses canonical labels such as `Add Flight`, `View Logbook`, `Search logbook`, `Current Period`, `Recent Flights`, `Activity`, `Totals`, `7 days`, `28 days`, `90 days`, `Custom`.

## Content contract
Each string must have a semantic job:
- destination/action labels name the actual action/destination;
- section labels identify the data scope;
- range labels identify the actual period policy;
- operational data remain data, not marketing copy;
- runtime state copy appears only when the implementation can distinguish that state.

Do not add “premium” tone through greetings, slogans or decorative aviation language. Do not invent `Saved`, `Synced`, `Offline`, search counts/results or other state claims because the static composition has visual room for them.

## Stress integration
Use the canonical fixture unchanged for Type/Layout fit tests first. Source/user Unicode and locale-sensitive date/numeric rendering remain stress inputs even though product-authored UI is English-only. If geometry fails, recomposition precedes semantic abbreviation.

## CRITIQUE / falsifiers
FAIL if:
- `Search logbook` is rewritten to imply unsupported behavior;
- range labels no longer match product calculation policy;
- visual fit causes ambiguous abbreviations;
- brand voice adds unsupported user identity/status;
- accessibility payload and visible label describe different action/state truth.

## Validation
Static expert critique can establish semantic consistency only. Runtime visible+a11y payload must be checked against I102 authority. Linguistic comprehension, trust and pilot preference require human evidence and remain OPEN.

## HANDOFFS
Type/Layout receive immutable-first fixture strings; Interaction owns actual state/action truth; Web compares visible and accessibility payloads in production; Color must not require color-dependent wording.

## OPEN
Runtime payload, localization architecture beyond current English-authored UI, linguistic review, AT comprehension and representative-pilot task evidence.