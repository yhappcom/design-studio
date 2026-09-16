# CD041 — Partial Authority and Evidence Language

Date: 2026-09-16
Evidence class: **SYSTEMS PRACTICE / CONTENT CLOSURE / TOOLCHAIN OPEN**

## RELATED DOMAIN CHECK
I022 owns truth/action safety; L026 owns proximity; C035 owns visual cue survival; W035 owns runtime provenance; T021 owns rendering and cannot justify shortening semantic truth.

## Gap
CD040 distinguishes last-known/current/unavailable/conflict. I022 exposes a finer case: the product may know some authoritative facts while an action-critical fact remains unknown. Generic “Up to date” or “Couldn’t refresh” copy would collapse that state.

## Semantic IDs
Maintain distinct resources for:
- `authorityChecking`;
- `authorityCurrentConfirmed`;
- `authorityUnavailableLastKnown`;
- `authorityPartial`;
- `authorityConflict`;
- `authorityEvidenceExpired` only when product policy supplies a real freshness rule.

## Content contract
Each resource must identify, where relevant: object; what is known; what is not confirmed; evidence time/event; consequence for the affected action; safe next action. Do not imply that all fields are current because one request succeeded.

## Localization invariants
Translations may reorder clauses but must not:
- convert partial into confirmed;
- convert unavailable/unknown into failed or unchanged;
- remove which fact remains unconfirmed when action safety depends on it;
- strengthen an evidence timestamp into a guarantee of currentness;
- expose Retry when I022 does not permit it.

## Toolchain tests
Actual localization execution must cover long object IDs, plural/select where used, date/time with named event semantics, pseudo-expansion, missing resource/fallback, and semantic-ID/revision trace into W035 captures.

## Evidence boundary
Static resource architecture is not ARB/ICU/TMS round-trip evidence and not human comprehension evidence. Both remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
L026 validates association under expansion; W035 binds resource IDs to runtime states; C035 verifies meaning survives color degradation; Type uses unchanged strings in later proofing.
