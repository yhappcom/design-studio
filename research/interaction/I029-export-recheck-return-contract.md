# I029 — Export Recheck Return Contract

Evidence purpose: **SYSTEMS PRACTICE / TRANSFER VALIDATION PREPARATION**.

## RELATED DOMAIN CHECK
C042 covers cue loss; L032 owns static hierarchy; W041 owns runtime/export; CD047 owns snapshot language; Type remains provisional.

## Problem
A static audit export can truthfully describe generation-time evidence yet become stale. The safe workflow therefore needs a defined return from artifact to live authority, not merely a disclaimer.

## Contract
Every export that can influence a later professional decision should expose enough stable identity to re-open or locate the live object without implying that the artifact itself is live. The return path must preserve `objectId`, relevant `eventId`/operation identity, snapshot generation time and authority-confirmed time where known.

Recheck outcomes are distinct: `currentConfirmed`, `changedSinceSnapshot`, `authorityUnavailable`, `objectUnavailable`, and `accessNotAuthorized`. None may be collapsed into generic failure.

A recheck must not mutate the object. Mutation actions remain governed by their own current authority dependencies.

## Deterministic oracle
Given artifact A at revision r1 and live authority r2:
1. opening/retrieving A preserves r1 snapshot semantics;
2. invoking recheck resolves the same object identity;
3. r2 is presented as current without rewriting A's historical event facts;
4. if r2 differs, changed-since-snapshot is explicit before any consequential action;
5. if authority cannot be reached, the system does not label r1 current;
6. returning to history preserves both r1 artifact provenance and r2 current truth.

## Failure cases
Broken deep link; reused object ID; permission loss; deleted/archived object; locale change; event unavailable; network timeout; authority revision changed during recheck.

## OPEN
No live backend, persistence, authorization or browser execution is available here. Human discoverability and comprehension remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W041/W042 runtime should execute this return path. CD048 should name the recheck outcomes without certainty inflation. Layout should keep snapshot/current truth spatially distinct. Color must not make stale artifact status appear current.