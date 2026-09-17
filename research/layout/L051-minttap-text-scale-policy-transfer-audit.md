# L051 — MintTap Text-Scale Policy Product-Transfer Audit

Status: TRANSFER VALIDATION / STATIC PRODUCT EVIDENCE.

## RELATED DOMAIN CHECK
T029 identifies the compact-iOS scale cap without reclassifying it as kerning. C060 requires explicit state redundancy. I046 owns workflow continuity. W059 owns runtime artifacts. CD065 owns semantic truth.

## Product evidence
MintTap production source applies `MediaQuery.withClampedTextScaling(maxScaleFactor: 1.10)` on native iOS when shortest side is <=375. The product lab contains reflow-oriented components and long financial strings but has not yet been executed in this environment.

## SOURCE / STANDARD CHECK
WCAG 2.2 remains the web baseline. Flutter's current release guidance says the UI should remain legible and usable at very large text/display scale factors. Flutter also documents nonlinear scaling behavior on Android 14.

## CRITIQUE
A global 1.10 cap on compact iOS is not evidence that the composition works under user enlargement. It can suppress the exact geometry pressure needed to expose clipping, detached qualifiers, target crowding and hidden recovery controls. Therefore a clamp may only be justified as a bounded exception with separate accessibility evidence; it cannot be used as the default closure mechanism for L050.

## PRACTICE — protected groups
For MintTap the following remain indivisible semantic relationships even when they stack:
- metric label → value → basis/qualifier;
- field → validation/error → correction/recovery;
- state → available action → outcome/recovery;
- portfolio/holding identity → scope/filter context;
- total performance → sign/value → gross/net or estimate/finality qualifier.

Prefer vertical recomposition, progressive disclosure that preserves access, and larger scroll extent over shrinking or suppressing user scaling.

## Runtime acceptance
W059 must compare current production clamp with an unclamped diagnostic build/scenario. Record viewport, actual text scaler, line breaks, overflow, target geometry, focus visibility and whether protected groups remain adjacent. A clamp can remain only with explicit rationale and evidence that equivalent enlargement access is preserved.

## Evidence boundary
No claim that production currently fails WCAG/native accessibility; source inspection alone cannot establish rendered behavior. No physical-device, AT or human usability PASS.

## HANDOFFS
Type: do not repair resulting geometry with kerning. Content: do not shorten financial truth for fit. Interaction: verify focus/recovery remains reachable after recomposition. Web: make actual scaler part of artifact identity.