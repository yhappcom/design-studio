# W018 — Progressive Readiness, Geometry Stability & Narrow-Text Chromium Transfer

Status: **PRACTICE / CRITIQUE — EXECUTED 8/8**  
Evidence intent: **TRANSFER VALIDATION + INDEPENDENT VALIDATION + CONTRADICTION REVIEW**  
Date: 2026-09-16

## PURPOSE

Transfer W007's design claim that first paint, truthful data visibility, task readiness and stable continuation are distinct into an actual Chromium specimen, while also integrating the still-open W017 long-label/enlarged-text stress.

The higher-priority W015 real Fetch/network gap remains blocked by the previously observed execution-environment navigation policy. W018 therefore tests the next executable runtime gap rather than fabricating network evidence.

## RELATED DOMAIN CHECK

### Type
`progress/TYPE_STATUS.md` was checked. T021 is still at drawing validity FAIL, so W018 uses system UI text and makes no custom-font transfer claim. The long operational action string is retained rather than shortened to protect geometry.

### Color
`progress/COLOR_STATUS.md` was checked. Color Stage 2 is PASS. W018 does not depend on authored hue and adds no color claim.

### Layout / Interaction
`progress/LAYOUT_STATUS.md` and W007's reuse of I002 were checked. W018 preserves the distinction between visible/pending content and an actually enabled consequential action. Reserved geometry is tested as a spatial stability contract, not merely visual polish.

### Web
W007, W012, W015 and W017 were checked. W018 is direct browser TRANSFER VALIDATION of W007 and integrates a narrow/200%-text stress similar to W017 without repeating icon semantics.

### Content Design
`progress/CONTENT_STATUS.md` was checked. CD011's state-certainty boundary supports keeping `Loading…` separate from `Ready to confirm`; W018 does not invent outcome semantics.

## METHOD

Playwright drove local Chromium **144.0.7559.96** with a deterministic in-document asynchronous specimen. No network transport is involved.

Two otherwise parallel regions were compared:
- **bad/unreserved:** asynchronous record content inserts into zero-reserved space;
- **good/reserved:** the same content inserts into a 72px reserved task region.

Timeline events were explicit: first animation frame → data visible → task-ready/action enabled. A separate 320 CSS px viewport with root text enlarged to 200% tested the long action label, horizontal overflow and keyboard reachability.

## FAILURE → HARNESS CORRECTION

The first measurement reported both bad and good button movement as 44px. This was a **measurement confound**, not a product finding: the good region sat below the bad region, so movement in the bad region translated the whole good section.

The harness was corrected to measure button position **relative to its own section**, not absolute document position. Re-execution produced bad=44px and good=0px. This correction is retained as CONTRADICTION REVIEW of the first measurement method.

## RESULTS

Final: **8/8 assertions PASS**.

Measured timeline in this run:
- first frame: 86.4ms;
- data visible: 185.6ms;
- task ready: 325.1ms.

The exact millisecond values are environment/run-specific and are not performance targets. The transferable evidence is ordering: visible structure preceded data, and visible data preceded safe task readiness.

Geometry comparison:
- unreserved region button movement: **44px**;
- reserved region button movement: **0px** relative to its own section.

Narrow/text stress:
- viewport: **320×900 CSS px**;
- root font size: **200%**;
- document horizontal overflow: **false**;
- both long action labels fit their 262px button boxes by wrapping;
- keyboard Tab reached an enabled native button.

## CRITIQUE

### Confirmed
W007's model survives this bounded browser transfer: **paint ≠ data visibility ≠ task readiness**. A design that looks present before the consequential action is operable needs explicit pending/readiness semantics.

Reserved geometry materially protected the tested control from asynchronous displacement. The experiment also shows that a long operational label can survive a narrow + enlarged-text condition when controls wrap instead of enforcing one-line geometry.

### Important measurement limitation
The PerformanceObserver `layout-shift` aggregate was 0 in this headless run even though direct geometry measurement found a 44px displacement in the bad region. W018 therefore does **not** use the observed CLS value as proof of absence of instability. Direct task-relative geometry was the reliable bounded diagnostic here.

### Not proved
- actual browser zoom (root font-size enlargement is not browser zoom);
- network Fetch, response loss or outcome ambiguity;
- real LCP/INP production performance;
- Firefox/Safari parity;
- screen reader/AT behavior;
- physical touch/device behavior;
- human perceived speed, trust or task performance.

## STUDIO JUDGMENT

For task-oriented web products, performance review should specify at least three separate milestones where relevant: **first truthful structure, data/state visibility, task readiness**. A single `loaded` or spinner-disappeared milestone is too coarse when controls become safe later.

Async regions adjacent to active controls should reserve or otherwise stabilize expected geometry when the content bounds are knowable. Where they are not knowable, the layout must recompose without moving an active/targeted control unexpectedly.

Long consequential labels should be allowed to wrap under narrow/enlarged-text conditions rather than being semantically shortened solely to maintain one-line component geometry.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
W018 transfers I002/W007 state separation into Chromium: readiness is a behavioral milestone distinct from paint. The 44px→0px relative-control comparison is useful evidence for reserving async task geometry.

### Content Design
CD011's semantic distinction is compatible with the runtime result: pending and ready states should remain linguistically distinct; wording must not imply readiness before the action is operational.

### Type
The long label survived through wrapping using system UI type. Future stable T021 candidates can be transfer-tested without shortening the string.

### Color
No new color dependency; readiness and stability remain understandable without color.

## OPEN

1. W015 real Fetch/DOM/network known-failure vs outcome-unknown transfer when navigation policy permits.
2. True HTTP direct-entry/reload/404/auth route validation.
3. Actual browser zoom rather than root-font enlargement.
4. Real production PerformanceObserver/LCP/INP/CLS evidence on a deployed product.
5. Firefox/Safari, AT, physical-device and human evidence.

## FILES
- `W018-progressive-readiness-stability-chromium-transfer.py`
- `W018-progressive-readiness-stability-chromium-results.json`
