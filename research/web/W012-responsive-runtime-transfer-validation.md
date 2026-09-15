# W012 — Responsive Runtime Transfer Validation / W003 Contradiction Review

Status: **TRANSFER VALIDATION / EXECUTED CRITIQUE**

## Research question

Can W003's relationship-ownership model survive actual Chromium execution, and does its prepared assertion model correctly distinguish **local overflow capability** from **overflow that is actually required**?

This is deliberate repetition for **TRANSFER VALIDATION + CONTRADICTION REVIEW**. Web's current largest relative weakness is runtime execution depth, so this study executes an existing authored specimen rather than opening another theory topic.

## RELATED DOMAIN CHECK

### Type
Checked current Type status through T021. Type has Stage 1 PASS and deeper executed raster evidence; exact production-font geometry remains separate from this system-font W003 run.

### Color
Checked current Color status through C015. No Color claim is being re-proved. The specimen keeps structural distinctions independent of hue.

### Layout / Interaction
Checked current Layout/Interaction status through L007/I006. W012 transfers the relationship/ownership model into a real browser and checks source/focus sequence plus overflow ownership. It does not claim AT or human validation.

### Web
Checked W003 and its companion specimen/harness. W003 explicitly left reproducible Chromium results OPEN. W012 executes that gap and critiques the assertion contract.

## EXECUTION

Environment:
- Chromium `144.0.7559.96`
- Playwright Python binding
- four cases: 1180px wide, 820px mid, 390px narrow, 390px narrow + long English/Korean label stress
- same authored W003 CSS/DOM behavior

Measured highlights:

| case | viewport | document width | main container | aside container | main CQ cols | aside CQ cols | table overflow |
|---|---:|---:|---:|---:|---:|---:|---|
| wide | 1180 | 1180 | 734.41 | 305.59 | 2 | 1 | no |
| mid | 820 | 820 | 474 | 206 | 2 | 1 | yes |
| narrow | 390 | 390 | 308 | 308 | 1 | 1 | yes |
| narrow + long | 390 | 390 | 308 | 308 | 1 | 1 | yes |

Focus/source sequence stayed stable in all four cases:
`Add transaction → Export → Compare portfolios → More actions → transaction table`.

No case produced document-level horizontal overflow.

## CONTRADICTION REVIEW

The prepared W003 harness reports **15/16** assertions because `table_overflow_is_local` was defined as:

`table has active horizontal overflow AND document still fits viewport`.

That is too strong for the wide case. At 1180px the table fits its allocated region, so active overflow is correctly absent. The design contract is not “the table must always overflow locally”; it is:

1. the table wrapper owns horizontal overflow when intrinsic table width exceeds allocation;
2. the document must not acquire horizontal overflow from the table;
3. when enough local width exists, no unnecessary scrollbar/overflow should be required.

Therefore the single failed assertion is an **ASSERTION-MODEL DEFECT**, not a responsive-layout failure.

Corrected predicate:

`document_fits_viewport AND (table_scroll_width <= table_client_width OR local_scroll_container_can_own_overflow)`

with an additional stress-case assertion that mid/narrow allocations actually trigger local overflow.

## CRITIQUE

### KEEP
- W003's page-global vs component-local ownership distinction.
- Same viewport / different allocation test: at 1180px, main container stays 2 columns while aside recomposes to 1.
- Page-global media recomposition at 390px.
- Stable source/focus sequence across recomposition.
- Local table containment without document overflow.
- Long bilingual label stress did not create document overflow.

### REWORK
- W003 harness assertion semantics for table overflow.
- Future integrated harnesses must distinguish **capability/ownership** from **state activation**.
- Long-label stress should additionally measure clipping, overlap and control target geometry rather than only document width.

### REJECT
- Treating “overflow exists” as success at every viewport.
- Treating a single boolean assertion failure as proof of design failure without inspecting what the assertion actually encodes.

## STUDIO JUDGMENT

A reusable Web validation rule follows:

`owner correctness != state activation`.

A component can correctly own a fallback mechanism even when that fallback is inactive in roomy conditions. Browser tests should assert the **condition under which a mechanism activates**, not merely its perpetual presence.

This transfers beyond tables to disclosure, truncation, scrolling, sticky behavior, compact navigation, and error/recovery UI.

## Evidence level

`SOURCE/peer evidence → existing Web specimen → actual Chromium execution → measured result → failed assertion → contradiction classification → revised validation contract`.

This is real browser execution. It is not Firefox/Safari/mobile/AT/human evidence.

## OPEN

- patch and rerun the canonical W003 harness with the corrected overflow predicate;
- execute W004 history/navigation and W005 native/custom semantic controls;
- integrated W006/W011 state/icon/target/enlargement harness;
- actual browser UI zoom;
- Firefox/Safari/physical mobile;
- accessibility-tree/screen-reader transfer where appropriate;
- human task evidence remains deferred to live project validation.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Responsive tests should distinguish exact font-induced activation thresholds from ownership of the responsive mechanism. Exact production-font transfer remains Type-owned.

### Color
The same distinction applies to forced-color/theme fallbacks: capability should exist, but activation must be tested under the condition that invokes it.

### Layout / Interaction
W012 confirms L/W ownership reasoning in Chromium and adds a testing caution: fallback ownership and fallback activation are separate assertions. This is relevant to overlays, disclosure, retry and compact-state transitions.
