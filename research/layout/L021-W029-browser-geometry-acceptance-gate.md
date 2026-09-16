# L021 — W029 browser geometry acceptance gate

Evidence type: **TRANSFER VALIDATION GATE / EXECUTION OPEN**

## RELATED DOMAIN CHECK
W029/W030 own execution provenance; C030 owns color/focus visual interpretation; I016 owns recovery state; CD035 owns labels; Type T021 metrics remain unavailable for custom-font width freeze.

## Accepted geometry evidence
Only an actually executed browser capture may close a L020/L021 case. Record viewport dimensions, document scroll width, target/action rectangles, sticky/overlay rectangles, focus target reachability and route/state context.

### Required distinctions
- 320 CSS px narrow viewport = responsive/reflow stress, **not actual 200% zoom**.
- DOM rectangle intersection = geometric obscuration evidence, not proof of perceived visibility.
- Headless engine evidence = browser-engine transfer, not physical-device evidence.
- visual viewport/safe-area/software keyboard require environments that expose those conditions; do not infer them from reduced layout viewport alone.

## Recovery geometry
For each I016/CD035 recovery state, the safe next action must remain reachable without two-dimensional scrolling for ordinary content. Sticky/fixed layers must not make the focused recovery action entirely unavailable. Long/localized strings may increase height; truncating semantic truth to preserve preferred geometry is not an acceptable repair.

## Current result
**GEOMETRY ACCEPTANCE GATE READY / EXECUTION OPEN.** W030 documents the failed repository-transfer attempt in the current container. No L020/L021 browser geometry PASS is claimed.

## HANDOFFS
C030 consumes overlap geometry; Web supplies engine/version/capture provenance; Content supplies full strings; Type later supplies valid product metrics after T021.