# I028 — Audit Export Provenance Contract

Evidence purpose: **STAGE 3 SYSTEMS PRACTICE + TRANSFER VALIDATION**.

## RELATED DOMAIN CHECK
C041 covers visual truth after export; L031 covers current/history locality; W040 covers durable reconstruction; CD046 covers event semantics; Type remains provisional.

## Problem
A professional audit view can reconstruct correctly in-app yet lose truth when exported/shared. A static artifact cannot imply that its state is live or current unless that is actually established.

## Export truth model
Every exported audit artifact should be able to identify:
- subject/object identity;
- artifact generation time and its semantics;
- authoritative revision or explicit unknown/unavailable status;
- included event IDs and operation/correction-chain identity where applicable;
- event observation/reconciliation timestamps without rewriting prior uncertainty;
- whether the artifact is a snapshot and how current truth can be rechecked;
- omitted/unavailable history explicitly, rather than silently disappearing.

## Safety rules
1. Export never converts `outcomeUnknown` into failure or success.
2. Historical event truth is immutable; later reconciliation is linked as a later event.
3. A static export is not a live authority surface.
4. Retry/compensation remain distinct operations.
5. If provenance required for a professional claim is missing, the export states the limitation.

## Reconstruction test
Given only the durable export plus its declared provenance, a non-human audit should be able to reconstruct event order, distinguish historical observation from current consequence, and identify where authority is unknown. This does not prove human comprehension.

## Evidence boundary
No production signing, tamper resistance, legal-record compliance, human comprehension or professional regulatory acceptance is claimed.

## HANDOFFS TO OTHER SPECIALISTS
L032 owns export hierarchy; C041 owns non-color visual survival; W041 owns browser print/download/runtime provenance; CD047 owns snapshot/provenance language.