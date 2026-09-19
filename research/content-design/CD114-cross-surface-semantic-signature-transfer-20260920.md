# CD114 — Cross-surface semantic signature transfer

Date: 2026-09-20
Status: Stage 3 PRACTICE / COMPLETE-SYSTEM TRANSFER DESIGN

## Purpose
Ensure LogMate's content system transfers across Home, ledger, Activity, Add Flight, import/review, and recovery without using terse copy as a substitute for coherent semantics.

## Content invariants
Across surfaces preserve:
1. canonical object/field identity;
2. actual state and validation truth;
3. action and scope;
4. consequence when material;
5. recovery availability/result;
6. committed vs Saved/Synced distinction;
7. source/user-authored evidence without silent rewriting.

Product-authored LogMate UI remains English-only. Source/user Unicode and locale-sensitive numeric/date behavior are stress inputs, not a requirement to localize product-authored UI.

## Voice transfer
The candidate voice remains precise / quiet / operational / non-theatrical. It is not production-approved. 'Quiet' means semantic economy: remove words with no job, but never delete object, state, consequence, or recovery information required to act correctly.

## Contradiction review
FAIL if the same concept changes terminology between Home and detail; if terse labels hide scope; if Saved/Synced is used for local commit; if import ambiguity is called an error; if browser-restored/autofilled values are described as validated; or if representation changes alter professional field meaning.

## Reproducible fixture
Use one canonical content fixture through Home summary, ledger row/detail, Add Flight form/error/review, import mapping/preview, destructive/recovery, offline/save/sync states. Compare visible label, accessible name/description, status payload, object/action/recovery references, truncation recovery, and route-return terminology.

## Human boundary
Comprehension, trust, perceived professionalism, cognitive load, and pilot terminology preference remain HUMAN evidence; deterministic consistency is necessary but not sufficient.