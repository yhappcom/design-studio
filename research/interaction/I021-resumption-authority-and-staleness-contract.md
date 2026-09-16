# I021 — Resumption authority and staleness contract

Evidence: **SYSTEMS PRACTICE / UX INTEGRATION / PRODUCT CONTRACT OPEN**

## RELATED DOMAIN CHECK
Type T021 protects identifier discrimination; Color C034 protects state cues under user color overrides; Layout L024 protects resumption priority/reachability; Web W033 owns runtime route/cache provenance; Content CD039 owns wording and typed variables.

## Problem
I020 ensures a returning surface exposes identity, certainty, consequence and safe action. A remaining failure mode is **stale-but-plausible resumption**: browser history, cached DOM, local state or restored navigation can display a coherent prior state that is no longer authoritative.

## Contract
Every resumed professional workflow must distinguish:
1. **presentation restored** — UI state was restored from history/cache/local memory;
2. **authority checked** — authoritative source was queried or a documented freshness contract remains valid;
3. **freshness known** — revision/version/updated-at or equivalent proves what state is being shown;
4. **authority unavailable** — the product cannot currently establish freshness;
5. **conflict** — restored/local and authoritative states differ.

A restored screen is not evidence of authoritative freshness. A successful route restoration is not a successful reconciliation.

## Action safety
- `presentationRestored + authorityUnchecked` → do not expose destructive/retry action whose safety depends on current state.
- `authorityUnavailable` → name the limitation; preserve last-known identity/state separately from current certainty.
- `conflict` → compare/resolve path; never silently replace one version if user work could be lost.
- `authorityChecked + current` → enable actions according to the product contract.

## Non-human validation oracle
For reload, back/forward, bfcache-like restoration, offline return and later deep link, record: object ID, local revision, authoritative revision, authority-check attempt/result, certainty state, enabled actions, conflict status and history/detail path.

## Human evidence boundary
This oracle can detect unsafe state/action contradictions. It cannot establish whether pilots notice staleness, understand revision language, recover context efficiently or trust the workflow. Those remain product-stage human evidence.

## HANDOFFS TO OTHER SPECIALISTS
Web must expose route/cache/restoration provenance and authority-check events. Content must distinguish last-known from current without overstating freshness. Layout must prioritize stale/conflict warnings without hiding identity/actions. Color must not use hue as the only stale/conflict cue. Type must keep revision/object identifiers discriminable.