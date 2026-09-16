# W029 — Browser transfer execution contract

Date: 2026-09-16
Evidence class: **TRANSFER VALIDATION protocol / execution pending**

## RELATED DOMAIN CHECK
- **Type:** T021 is still blocked on operational repertoire and pre-kerning drawing/general spacing. W029 therefore uses the mature system font and cannot advance Type gates.
- **Color:** C029 needs focus/state/overlay and forced-colors evidence. W029 records the shared capture dimensions but does not claim Color PASS without executed results.
- **Layout/Interaction:** L020 requires actual rectangles/reflow/reachability; I016 supplies the recovery oracle already backend-validated by W028.
- **Web:** W027+W028 now provide the true-origin workflow. W029 converts that surface into repeatable multi-engine browser execution.
- **Content:** CD035 supplies certainty-bound recovery semantics. W029 checks rendered state labels against the I016/CD035 classification, not prose preference.

## Runner
`W029-browser-capture-runner.py` launches the controlled backend and attempts the same workflow in Chromium, Firefox and WebKit. It records engine, viewport, route/history result, controlled outcome, immediate state, reconciled state, document scroll width and focused-action/sticky-layer intersection.

The minimum adversarial pair remains `drop-before` and `drop-after`: both must initially produce outcome-unknown at the browser boundary, then reconcile respectively to not-found and confirmed.

## Geometry / responsive checks
Baseline and 320 CSS px narrow runs are recorded separately. A narrow run is a reflow stress case; it is **not** labeled actual 200% browser zoom. Actual zoom, visual viewport changes, software keyboard and safe-area behavior require separate executable evidence.

## Accessibility/color boundary
The runner records focused-action geometry but does not equate DOM focus with screen-reader/AT evidence. Forced-colors/high-contrast must be executed and recorded as a separate C029 transfer. WCAG 2.2 remains the baseline; focus visibility and focus obscuration are separate checks.

## Performance boundary
W029 is a functional/layout lab harness. It does not generate field LCP/INP/CLS evidence. Any later Core Web Vitals field claim requires real field/RUM population and context.

## Evidence rule
A committed runner is not execution evidence. `W029-browser-capture-results.json` may be committed only after an actual run. Missing Playwright or browser engines must be recorded as blockers rather than converted into synthetic results.

## UX integration
The non-human workflow oracle is:
`dispatch → transport observation → certainty classification → safe action → reconciliation → authoritative state → rendered message/action → reachable/focused control`.
This can expose semantic and implementation contradictions. Discoverability, comprehension, workload, trust and professional task performance remain human-evidence OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- **Color:** consume executed capture IDs for C029 focus/overlay/forced-colors transfer.
- **Layout/Interaction:** consume viewport/rectangle/state results for L020/I016.
- **Content:** compare actual rendered labels/actions to CD035 semantic IDs after execution.
- **Type:** later replace the mature system font only after T021 closes and provide exact metrics/fallback evidence.
