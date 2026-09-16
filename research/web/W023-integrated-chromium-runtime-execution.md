# W023 — W021 integrated Chromium runtime execution

Classification: **TRANSFER VALIDATION + RUNTIME EXECUTION + CONTRADICTION REVIEW**

## Purpose
Execute the previously blocked W021/W022 integration surface in a real headless Chromium runtime instead of adding another static contract.

## Environment
- browser binary: container-installed Chromium (`/usr/bin/chromium`)
- driver: Playwright Python
- execution mode: headless
- artifact: exact current `W021-integrated-runtime-specimen.html` content loaded with `page.set_content()` because file:// and localhost navigation were blocked by the host administrator
- viewport cases: 1280×800, 800×900, 390×844; additional strict 320 CSS px reflow stress
- media cases: dark color scheme, reduced motion, forced colors

This is actual browser rendering/DOM/CSS execution, but not Firefox/Safari, physical-device, screen-reader, backend/network or human evidence.

## RELATED DOMAIN CHECK
- Type T022: W021 intentionally retains mature/system typography; experimental control glyphs are not substituted.
- Color C024: requires rendered contextual theme/forced-color evidence.
- Layout L015: requires responsive/reflow/focus geometry and adjacency evidence.
- Interaction I010: requires certainty/safe-action invariance.
- Content CD029: requires semantic identity to survive expansion/RTL; this specimen is not the ARB round trip.
- UX: nonhuman end-to-end state/recovery continuity can be tested; discoverability/workload/trust cannot.

## Executed results
### Responsive composition
- 1280 desktop: record list computed `display:block`.
- 800 tablet: record list computed `display:none` under the <=850 rule.
- 390 phone: record list computed `display:block` under the <=560 override.

This confirms the authored responsive rules execute as written. It does **not** prove that hiding the list at tablet width is a good product IA decision; W021 already scoped that as a bounded specimen limitation.

### Keyboard sequence and focus geometry
At desktop/tablet/phone, sequential Tab navigation reached:
`Records → Search → Settings → Check record → Pseudo-expand → RTL stress → Edit record`.
The disabled `Save again` control was correctly omitted from sequential focus while disabled.

`Edit record` remained fully inside the viewport in the measured desktop/tablet/phone cases. This is evidence against complete focus obscuration for that measured control/cases only, not a universal WCAG conformance claim.

WCAG 2.2 SC 2.4.11 requires a keyboard-focused component not be entirely hidden by author-created content. The W3C criterion remains the normative acceptance reference; W023 records measured geometry rather than replacing that criterion.

### Certainty and safe-action transition
Fresh phone execution:
- before verification: state class `status unknown`; `Save again` disabled;
- after `Check record`: state class `status confirmed`; `Save again` enabled; status text becomes `Record confirmed / The saved record matches this device.`

This confirms I010's key bounded invariant in the specimen: an unknown outcome does not expose blind retry, while successful verification changes certainty before retry becomes available.

### Long-content stress
After `Pseudo-expand`, the status container had no horizontal overflow at desktop/tablet/phone. At strict 320 CSS px, body `scrollWidth == clientWidth == 320` and the expanded status also had no horizontal overflow.

This is rendered reflow evidence for this English pseudo-expanded fixture. It is not real locale evidence and does not replace CD029 resource transfer.

### RTL / operational literals
After RTL stress:
- root `dir=rtl` executed;
- operational literal computed direction remained `ltr`.

This confirms the bounded CSS bidi-isolation mechanism executes in Chromium. It does not prove all Arabic/localized content or assistive-technology reading order.

### Dark scheme
At 390×844 with dark scheme:
- root foreground computed `rgb(242,245,247)`;
- root background computed `rgb(16,20,24)`;
- focused Check button outline computed `rgb(140,200,255)`.

These are rendered/computed values for C024 follow-up, not contextual contrast PASS by themselves.

### Forced colors
Chromium accepted `forced_colors='active'`. Unknown-state status computed:
- text `rgb(0,0,0)`;
- background `rgb(255,255,255)`;
- border `rgb(0,0,0)`.

This confirms the authored forced-colors rule is active and collapses authored state hues to system colors while retaining textual state identity and a border. It does not establish cross-browser/Windows High Contrast equivalence.

### Reduced motion
With reduced-motion active, sampled control computed transition duration and animation duration were both `0s`, consistent with the authored media rule.

## CONTRADICTION / LIMIT REVIEW
1. The earlier status said browser runtime was blocked in the available environment. That statement is now outdated: direct browser navigation is blocked, but Chromium + Playwright execution is possible by injecting the exact artifact content. Integrated browser evidence therefore advances.
2. True route/history/Fetch/network evidence remains blocked by navigation policy and was not fabricated.
3. Tablet list hiding is technically confirmed but remains an IA/product-design OPEN, not a positive UX finding.
4. The first automation attempt that reused `set_content` to reset the same page did not reliably re-execute the transition script; the state-transition verdict above comes from a fresh page execution and is the valid result.

## Cross-domain verdicts
- Layout: bounded responsive/reflow geometry **TRANSFER EVIDENCE GAINED**, no Stage 3 PASS.
- Interaction: unknown→verified→retry authorization invariant **TRANSFER EVIDENCE GAINED**.
- Color: dark and forced-colors computed evidence **GAINED**; contextual contrast calculation still belongs to Color.
- Content: pseudo-expansion and RTL literal survival **GAINED**; ARB/locale semantics remain OPEN.
- Accessibility: focus sequence/visibility geometry evidence **GAINED**; no screen-reader/AT or global conformance PASS.
- Performance: no field evidence. No LCP/INP/CLS claim is made; local execution is not field Core Web Vitals.

## HANDOFFS TO OTHER SPECIALISTS
- Color: consume exact dark/forced-colors computed values and inspect contextual focus/non-text relationships.
- Layout/Interaction: consume 320px reflow, tablet list recomposition, focus geometry and verified state transition.
- Content: consume expansion/RTL results but continue CD029 resource round-trip separately.
- Type: no custom candidate transfer occurred; W021 remains mature/system control evidence.

## Next Web gate
Do not open another isolated Chromium micro-test. Next integrated Web work should either:
1. add route/history/network behavior in an environment where navigation/HTTP is permitted; or
2. broaden the same integrated specimen to Firefox/Safari/AT/physical mobile when executable.

**W023 verdict: INTEGRATED CHROMIUM TRANSFER PARTIAL PASS; NETWORK/CROSS-BROWSER/AT/PHYSICAL/FIELD/HUMAN EVIDENCE OPEN.**