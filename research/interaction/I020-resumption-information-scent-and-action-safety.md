# I020 — Resumption information scent and action safety

Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / HUMAN EVIDENCE OPEN**

## RELATED DOMAIN CHECK
Type T021 constrains rendered identifiers; Color C033 supplies redundant state cues; Layout L023 owns spatial continuity; Web W032 owns route/runtime restoration; Content CD038 owns certainty-preserving wording.

## Problem
I019 defines what state must survive interruption. I020 asks whether a returning user is given enough machine-verifiable context to choose a safe next action without assuming human comprehension.

## Non-human oracle
A resumed surface must expose, in inspectable order: object identity; last known operation/correlation identity; authoritative certainty; material consequence; unresolved conflict if any; safe available action; path to history/detail. If any field is unavailable, the interface must represent that absence rather than silently reconstruct certainty.

Unsafe patterns include: primary Retry while outcome is unknown; landing on a generic home route with no recoverable task reference; success styling with no authoritative confirmation; conflict resolution without showing which records differ; destructive action adjacent to stale context without renewed identification.

## Cognitive-load boundary
The oracle can count competing actions, duplicated state labels, missing identifiers and context switches. Those are structural diagnostics, not claims about perceived workload, comprehension, trust or discoverability. Human validation remains deferred to executable product testing.

## Validation matrix
Test fresh completion, response loss, reload, navigation away/back, later return, conflict, and unavailable history. For each, verify identity continuity, certainty, safe action set, history path and absence of contradictory semantic cues.

## HANDOFFS TO OTHER SPECIALISTS
Layout turns the oracle into spatial continuity/reachability checks. Content supplies semantic labels. Web executes route/history/runtime restoration. Color tests state-cue degradation. Type protects identifier discrimination.
