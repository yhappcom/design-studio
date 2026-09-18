# L065 — LogMate Auth Reflow Positive Control

Date: 2026-09-18  
Purpose: `TRANSFER VALIDATION` + `CONTRADICTION REVIEW`

## PRODUCT EVIDENCE
LogMate Design Review Render run `35293644138`, commit `11cbe36f…`, provides an unusually useful same-run comparison. The older onboarding-auth journey fails at 200% text with 41 px bottom overflow for intent landscape, 41 px for create-error portrait, and 147 px for verify-error landscape. The V4 journey in the same run passes 200% verify/reset/sign-in/create error scenarios, asserts that large-text content precedes actions instead of clipping under them, and switches keyboard-height presentation to continuous reflow.

## CRITIQUE
The same product, SDK and typography context contains both failure and repair architecture. This directly supports structural recomposition over pixel shaving or font compression. The decisive invariant is not preservation of ordinary-screen geometry; it is preservation of content/action order and reachability under constrained height and enlarged text.

## SYSTEMS PRACTICE
Use a two-regime layout contract:
1. ordinary geometry may preserve the intended composition;
2. constrained-height / large-text geometry must permit continuous reflow and scrolling where required, keeping semantic content before dependent actions.

Breakpoints should be triggered by content/constraint failure, not device labels. Measure available height/width, content extent, action extent and safe-area/keyboard reservation. Reject fixed-height arrangements that pass ordinary golden images but fail 200% text.

## REPRODUCIBLE VALIDATION
Run paired ordinary + 200% scenarios for portrait/landscape, keyboard-up and short-height. Record exact viewport, text scaler, state, overflow owner/amount and action reachability. Require zero overflow plus preserved semantic order. V4 is a positive control, not human-usability proof.

## RELATED DOMAIN CHECK
- Type: T043 shows no need for Type compensation.
- Color: state visibility must survive recomposition.
- Interaction: recovery/action reachability is behavioral, not only spatial.
- Web: Chrome 200% recovery reachability is supporting browser evidence.
- Content: error/recovery strings remain intact.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should bind focus/recovery order to the reflow model. Web should test the same constraint-triggered recomposition in served runtime. Content should retain complete state/recovery semantics.

## EVIDENCE BOUNDARY
No representative-device, Safari/Firefox, AT or human workload/discoverability PASS is claimed.