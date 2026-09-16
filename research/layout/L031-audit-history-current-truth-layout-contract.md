# L031 — Audit History + Current Truth Layout Contract

Evidence purpose: **SYSTEMS PRACTICE + RESPONSIVE TRANSFER specification**.

## RELATED DOMAIN CHECK
I027 defines durable event truth; C040 owns visual encoding; CD045/CD046 own wording; W039/W040 owns runtime capture; Type metrics remain provisional.

## Spatial problem
A history surface can be chronologically complete yet operationally unsafe if old success, current intervention, and selected history compete at the same hierarchy. The layout must distinguish **current authoritative consequence** from **historical sequence** without hiding either.

## Contract
Priority order for professional recovery surfaces:
1. affected object identity;
2. current authoritative consequence/certainty;
3. safe current action or explicit no-safe-action state;
4. correction-chain summary and stop reason;
5. chronological event history;
6. event detail/provenance.

Selection/focus within history must not visually displace current truth. On 320 CSS px, actual 200% zoom, localization expansion and reduced visual viewport, event identity + state + time semantics must remain associated; detail may disclose progressively, but current consequence and safe action cannot be pushed behind ambiguous historical success.

Measure bounding rectangles for current-truth region, focused/selected history row, sticky layers and safe action. Record overflow, occlusion and action reachability separately.

## Gate
Specification ready; actual browser geometry, physical-device and human scan/discoverability evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W040 should capture these rectangles with I027 event IDs; C040 uses the same rows for visual degradation; Content must preserve event semantics under localization; Type must rerun only after T021 drawing/spacing acceptance.