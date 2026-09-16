# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 3 PRACTICE / I016 BACKEND AMBIGUITY VALIDATED — L020 BROWSER GEOMETRY OPEN**
Governance sync: 2026-09-16
Canonical paths: `research/layout/`, `research/interaction/`
Active studies: L018–L020, I013–I016

## Current level
Stage 1 **PASS**; Stage 2 **PASS**; Stage 3 **PRACTICE / NOT PASSED**.

## Latest evidence
I016 independently validates the I015 recovery oracle against W028. `drop-before` and `drop-after` produced the same client-visible connection termination but reconciled to different authoritative outcomes (`not-found` versus `confirmed`). This makes outcome-unknown → reconciliation a tested controlled-backend invariant rather than a static state-model assertion.

L020 remains bound to W027 for viewport/visual viewport, actual 200% zoom, narrow reflow, sticky-layer focus intersection, keyboard-reduced viewport where executable and localization expansion. Those browser geometry captures are still OPEN.

## Active queue
1. Execute W027+W028 in a browser and collect L020 rectangles/reflow/action-reachability evidence.
2. Extend I016 from controlled fixture to documented product/backend idempotency and deduplication contracts when available.
3. Keep numeric width freeze blocked until valid Type/product metrics.
4. Add native Flutter transfer only on executable app surface.
5. Keep AT, physical-device, discoverability, workload and human task evidence OPEN.

## HANDOFFS
C029 consumes overlap geometry; Web W027/W028 owns browser/runtime fixture; CD034 consumes recovery truth; Type returns valid metrics only after T021.

## Evidence boundary
No Layout/Interaction Stage 3 PASS, browser geometry, native/product backend, AT, physical-device or human PASS is claimed.