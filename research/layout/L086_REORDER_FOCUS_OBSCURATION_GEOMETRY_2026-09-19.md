# L086 — Reorder Focus / Obscuration Geometry

Date: 2026-09-19
Stage: Stage 3 PRACTICE / NOT PASSED
Related: I082, I081/L085

## Purpose
Transfer I082 focus ownership into measurable spatial evidence for long-list reorder, sticky surfaces, autoscroll, drag proxies and 200% reflow.

## Geometry ledger
For each I082 scenario record viewport, sticky header/footer, focused component, visible focus indicator, drag proxy, source row, candidate destination, recovery control and non-drag Move control rectangles.

Measure at baseline and 200%:
- intersection of focused component with viewport after author-created overlays;
- amount and cause of any obscuration;
- proxy/focus overlap;
- scroll displacement before/after focus restoration;
- target dimensions and applicable WCAG 2.2 SC 2.5.8 PASS clause;
- wrapping/clipping and safe-area collisions.

## Acceptance model
WCAG 2.2 SC 2.4.11 AA is the minimum: the focused component must not be entirely hidden by author-created content. Studio practice should additionally minimize partial obscuration and avoid using the AA minimum as a design target.

Focus geometry does not define mutation ownership. Autoscroll geometry does not define destination truth. Drag-proxy position does not define focus. Stable semantic identity from I082 remains authoritative.

## Failure conditions
- focused control fully hidden behind sticky author content;
- focus ring visible on a proxy while actual focus is elsewhere in a way that misstates interaction locus;
- 200% reflow causes recovery or Move controls to become clipped/obscured;
- automatic focus restoration causes uncontrolled scroll jump that loses source/result context;
- target-size evidence omits the exact SC 2.5.8 clause relied upon.

## Evidence boundary
No rendered product or conformance PASS is claimed. Physical-device and human context-loss/overshoot evidence remain OPEN.