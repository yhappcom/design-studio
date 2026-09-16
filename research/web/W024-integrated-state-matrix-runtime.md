# W024 — integrated six-state Chromium transfer matrix

Classification: **TRANSFER VALIDATION + RUNTIME EXECUTION + CROSS-DOMAIN INTEGRATION**

## Purpose
Extend W023 on the same coherent professional-record surface instead of accumulating unrelated Chromium micro-tests. The new specimen renders all canonical certainty/recovery states together: pending, confirmed, known failure, outcome unknown, offline/stale, and conflict.

## RELATED DOMAIN CHECK
- Type T022: mature/system typography remains the runtime control; experimental H/O/n/o drawings are not loaded.
- Color C025: requires all semantic states, not only unknown/confirmed, before broader contextual conclusions.
- Layout L016: requires narrow-width survival and focus/recovery geometry.
- Interaction I011: requires distinct state truth and safe authorized action.
- Content CD030: requires semantic wording to remain distinct across the complete state set.
- UX: system consistency is testable; discoverability, cognitive load, trust and task performance remain human evidence.

## Environment
Headless Chromium `/usr/bin/chromium` through Playwright Python. Exact W024 HTML was loaded with `page.set_content()` because host policy still blocks ordinary local/HTTP navigation. Tested widths: 1280, 390, 320 CSS px. Additional media run: 390×844 with dark scheme + forced colors + reduced motion.

## Executed state/action matrix
For every width, the rendered semantic state and available recovery/action were:

| State | Rendered title | Available action |
|---|---|---|
| pending | Saving record | none |
| confirmed | Record confirmed | Edit record |
| known failure | Save failed | Try again |
| outcome unknown | Save status unknown | Check record |
| offline/stale | Offline — record not synced | View local record |
| conflict | Record conflict | Compare versions |

The six states therefore remain behaviorally distinct in the rendered fixture. In particular, known failure exposes retry while outcome unknown does not; conflict exposes comparison rather than destructive replacement; pending exposes no competing action.

## Reflow execution
Across all 18 state×width cases:
- `body.scrollWidth > body.clientWidth` = false;
- status-container horizontal overflow = false.

This is bounded rendered evidence that the complete English state/recovery set survives 320 CSS px without horizontal clipping. It is not 200% browser-zoom equivalence and not real localization evidence.

## Forced colors + reduced motion
In the combined media run on conflict:
- state foreground: `rgb(255,255,255)`;
- state background: `rgb(0,0,0)`;
- state border: `rgb(255,255,255)`;
- focused Edit outline: `rgb(255,255,255)`;
- Edit control fully inside viewport: true;
- `(forced-colors: active)`: true;
- `(prefers-reduced-motion: reduce)`: true.

Authored semantic hues again collapse to system colors, while state title/body/action preserve semantic identity. This confirms the non-color fallback architecture across the newly exercised conflict state, but does not establish Windows High Contrast or cross-browser equivalence.

## Accessibility baseline
WCAG 2.2 remains the studio baseline. This execution records actual focus geometry and state semantics but does not convert a bounded browser fixture into a global conformance claim. Focus Appearance is AAA in WCAG 2.2; Focus Not Obscured (Minimum) is AA.

## CONTRADICTION / LIMIT REVIEW
- W023's next queue asked for pending/failure/offline/conflict coverage; W024 closes that bounded Chromium state-coverage gap.
- True route/history/Fetch remains OPEN because `set_content()` does not provide a normal HTTP origin and navigation remains blocked.
- Cross-browser, screen-reader/AT, physical-device and native Flutter transfer remain OPEN.
- No field performance evidence exists. No LCP/INP/CLS claim is made from this local run.

## UX integration verdict
The fixture now preserves the tuple `object + task + certainty + safe authorized action` across six canonical states at desktop and narrow widths. This is nonhuman workflow-consistency evidence only. It does not prove users notice, understand or correctly choose the actions.

## HANDOFFS TO OTHER SPECIALISTS
- Color: all-state authored/rendered semantics can now be audited without inventing state fixtures.
- Layout/Interaction: consume 18 no-overflow cases and the six-state action matrix; keep human discoverability open.
- Content: consume the rendered complete state vocabulary; ARB/locale round trip remains independent.
- Type: literals remain mature/system control; no custom-family transfer.

## Verdict
**W024 BOUNDED SIX-STATE CHROMIUM TRANSFER PASS. Web Stage 3 remains PRACTICE because route/network, cross-browser, AT, physical-device, field-performance and human evidence are still open.**