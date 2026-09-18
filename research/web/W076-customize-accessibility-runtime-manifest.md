# W076 — Customize accessibility runtime manifest

## Purpose
Turn W075's browser-closure backlog into one scenario-level runtime manifest. This avoids accumulating isolated Chromium micro-tests and prevents harness/build success from being promoted to product/browser PASS.

## RELATED DOMAIN CHECK
T045 supplies rendering constraints; C076 state orthogonality; L067 candidate spatial architectures; I063 input-path equivalence; CD081 semantic IDs/content governance.

## SOURCE
WCAG 2.2 SC 2.5.7 requires a non-drag single-pointer equivalent for non-essential dragging. SC 2.5.8 requires 24×24 CSS-pixel targets or a listed exception. These are evaluated at the rendered interaction layer, not from source intent alone.

## MANIFEST
Each browser run records:
- build/commit and scenario ID;
- browser engine/version and viewport;
- text scale/zoom/theme/forced-colors state;
- semantic field IDs and before/after order;
- input path: drag / single-pointer non-drag / keyboard;
- target bounding boxes and spacing evidence;
- focus before/after and accessible names/status;
- runtime console/exceptions;
- screenshot/DOM or framework semantics artifact;
- result: EXECUTED-PASS / EXECUTED-FAIL / NOT-EXECUTED / BLOCKED.

## EXECUTION LADDER
1. widget/runtime equivalence where implemented;
2. production Web build;
3. served HTTP runtime in primary engine;
4. same semantic scenarios in an independent engine;
5. 200% text/zoom + light/night/forced-colors;
6. reload/offline/sync-conflict only after persistence/Sync exist.

No step inherits PASS from a lower layer.

## PERFORMANCE EVIDENCE
Performance remains secondary to the current functional/accessibility blocker. Lighthouse, DevTools and CI traces are LAB. LCP/INP/CLS become FIELD only with provenance-bearing aggregate/RUM evidence tied to the actual product population/context.

## OPEN
The repository currently records no implemented non-drag reorder, independent-engine, persisted Customize, screen-reader, physical-device, field-CWV or human usability PASS. Those remain OPEN/NOT IMPLEMENTED as applicable.

## HANDOFFS TO OTHER SPECIALISTS
I063's transition ledger becomes the behavioral oracle. C076/L067/T045/CD081 provide acceptance dimensions; failures return to their canonical owner rather than being patched locally in Web.