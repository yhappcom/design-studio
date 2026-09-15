# Web Design Specialist Status

Operating state: **ACTIVE — STAGE 1 PASSED / STAGE 2 PRACTICE / W016 NATIVE-CUSTOM CHROMIUM TRANSFER EXECUTED**  
Governance sync: 2026-09-16  
Primary path: `research/web/`  
Next new-study ID: `W017`

## Current level
Stage 1 — Foundations: **PASS**  
Stage 2 — Intermediate Professional Practice: **PRACTICE / NOT PASSED**

Authority:
- W009 — Stage 1 Foundation closure
- W010 — Stage 2 entry audit
- W011 — iconography/non-text signal direct practice
- W012 — responsive Chromium runtime transfer / contradiction review
- W013 — navigation/history Chromium runtime transfer
- W014 — native vs custom button source-grounded runtime contract
- W015 — integrated task-state/recovery deterministic execution
- **W016 — native vs custom button actual Chromium transfer, 14/14**

The coordinator-maintained `progress/STATUS.md` is stale relative to specialist evidence and remains outside Web's writing boundary.

## Latest evidence — W016
Canonical:
- `research/web/W016-native-custom-button-chromium-transfer.md`
- `research/web/W016-native-custom-button-chromium-transfer.py`
- `research/web/W016-native-custom-button-chromium-results.json`

Reason: **TRANSFER VALIDATION + REPLICATION + CONTRADICTION REVIEW** of W014.

Playwright drove system Chromium **144.0.7559.96** against three controls: native button, click-only focusable `role=button`, and reconstructed custom button. Final result: **14/14 assertions PASS**.

Confirmed within Chromium:
- Tab reaches all three in controlled order;
- native button activates once on Enter and Space;
- click-only ARIA button exposes role/name but does not activate on Enter or Space;
- reconstructed custom activates once on Enter and Space;
- pointer activation works once for all three;
- keyboard-focused native button matches `:focus-visible` with a solid outline;
- Playwright ARIA snapshots expose all three as named buttons.

The first two runs exposed harness defects (12/14 then 13/14): a reset click changed focus, then blur retained tab-cycle position. The corrected harness reloads the controlled document before the focus-visible assertion and reaches 14/14. These failures are preserved as harness critique, not misclassified as product defects.

## Runtime evidence boundary
W012 provides responsive Chromium transfer. W013 provides navigation/history partial Chromium transfer with prior harness correction. W016 now provides actual Chromium keyboard/pointer/focus-visible/accessibility-snapshot control transfer.

W015 remains deterministic Python model validation, **not** Fetch/DOM/network/browser proof. True HTTP direct-entry/reload remains OPEN because the prior environment blocked loopback HTTP and `file://` navigation.

W016 does not prove screen-reader behavior, Firefox/Safari parity, disabled-state parity, physical touch/device behavior, forced-colors or enlarged-text behavior. `aria_snapshot()` is bounded browser/tool accessibility representation, not AT speech/navigation evidence.

## Stage 2 snapshot
| Requirement | Current state |
| --- | --- |
| task analysis / primary question | established |
| information hierarchy / IA | established; W004 + W013 partial runtime |
| dense vs low-density composition | strong; W002 executed |
| responsive/adaptive | PRACTICE + Chromium transfer W012 |
| forms/tables/search/settings/state | strong: W006 + W015 17/17 deterministic execution |
| typography across roles | established; exact production transfer open |
| iconography/non-text signals | W011 direct practice; runtime open |
| native/custom controls | **stronger: W014 contract + W016 Chromium 14/14** |
| component systems | strong conceptual practice |
| async/recovery | W015 executable model; real browser/network transfer open |
| comparative alternatives + explicit selection | strong |
| critique / KEEP-REWORK-REJECT | strong |
| cross-specialist handoff | strong |

Stage 2 is not passed. Actual browser/network/accessibility runtime coverage remains uneven.

## Four-specialist balance
- **Type:** Stage 1 PASS; Stage 2 PRACTICE. Shape-sensitive base metrics executed; pair-gap diagnostics + numerals/punctuation/accent breadth next.
- **Color:** Stage 1 PASS; **Stage 2 PASS**; Stage 3 entry not yet audited.
- **Layout / Interaction:** Stage 1 PASS; **Stage 2 PASS**; Stage 3 entry not yet audited.
- **Web:** Stage 1 PASS; Stage 2 PRACTICE through W016; native/custom Chromium transfer is now executed, while network/runtime breadth remains incomplete.

This cycle selected Web because Type had just completed shape-sensitive base-spacing correction while W014 had a directly executable Chromium blocker that could now be removed. Future cycles must re-evaluate all four again.

## Current OPEN / blockers
Highest-value gaps:
1. transfer W015 to real Fetch/DOM/network behavior including known failure vs outcome ambiguity;
2. true HTTP path direct-entry/reload/404/auth route validation when environment permits;
3. W011 accessible-name/target/enlargement/forced-color icon harness;
4. W007 request/paint/readiness/stability measurement;
5. broader integrated Stage 2 capstone/closure audit only after runtime breadth is credible.

Later/platform gaps: actual browser-UI zoom; exact production fonts/CDN/cache/service-worker behavior; Firefox/Safari/physical mobile parity; screen-reader/AT evidence; physical-device and field performance evidence.

Human findability/task/perceived-speed/icon-recognition evidence remains deferred to live project/app validation and is not simulated.

## Active next queue
1. Re-evaluate all four specialists before choosing the next study.
2. If Web remains highest value, prefer W015 Fetch/DOM/network Chromium transfer now that executable Chromium is available.
3. Compare that against Type's pair-gap/family-breadth work and Color/Layout Stage 3 entry needs.
4. Preserve failure → critique → revision evidence; never infer universal browser/AT PASS from Chromium success.

## HANDOFFS TO OTHER SPECIALISTS
### Type
W016 confirms that label/font customization does not require semantic-element replacement. Exact shipped-font/loading/wrapping transfer remains separate and should wait for stable family metrics.

### Color
Focus/state tokens must attach to behaviorally correct controls; semantic color cannot repair missing keyboard activation.

### Layout / Interaction
W016 independently confirms in Chromium that focusability/role exposure and activation behavior are separate contracts. The click-only ARIA control had button role/name yet failed Enter/Space activation.

## Latest checkpoint
- W009: **Stage 1 PASS**.
- W010: **Stage 2 entry accepted**.
- W012: **responsive Chromium runtime transfer executed**.
- W013: **navigation/history partial Chromium transfer executed; 10/11 → defect correction → 11/11**.
- W014: source-grounded native/custom contradiction review.
- W015: integrated task-state/recovery deterministic execution 17/17; browser/network transfer OPEN.
- W016: **native/custom actual Chromium transfer 14/14 after harness correction**.
- True HTTP direct-entry/reload: **OPEN**.
- Stage 2: **NOT PASSED**.
- Next new Web study ID: **W017**.
