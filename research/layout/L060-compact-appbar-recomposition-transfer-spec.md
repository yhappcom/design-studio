# L060 — Compact AppBar Recomposition Transfer Spec

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION

## Source localization
MintTap whole-app lab source places the brand wordmark, fixed horizontal gap and `PRODUCT LAB` badge in the AppBar title while also reserving an action button and trailing gap. This is a concrete fixed-width competition candidate consistent with the previously observed compact overflows. Source inspection narrows the repair target; it does not by itself prove the exact runtime RenderFlex owner.

## Repair hierarchy
1. Reproduce with the same runtime scenario and capture the failing RenderFlex stack/identity.
2. If AppBar title is confirmed, preserve the wordmark as primary identity and treat the lab badge as secondary metadata.
3. Prefer responsive recomposition: move secondary metadata below/outside the constrained title row, conditionally omit only non-production lab chrome, or provide a flexible/wrapping structure where platform AppBar geometry permits it.
4. Do not solve by shrinking typography, clipping, ellipsis of meaningful product text, or reducing target size.
5. Preserve action discoverability, reading order, focus order and minimum target geometry.

## Regression matrix
- 390×844 baseline.
- 390×844 enlarged text.
- long portfolio / signed large KRW and USD / partial-unavailable / estimated-final.
- 1024×768 workflow.
- light/dark where supported.

## Acceptance
No horizontal RenderFlex overflow; no avoidable two-dimensional scrolling; semantic adjacency and action reachability preserved. Human workload/discoverability remains OPEN.