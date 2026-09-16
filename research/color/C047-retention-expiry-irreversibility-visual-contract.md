# C047 Retention Expiry and Irreversibility Visual Truth Contract

Evidence mode: SYSTEMS PRACTICE / TRANSFER VALIDATION.

## Problem
C046 distinguishes deletion and restore uncertainty. A further failure appears when a deleted item is recoverable only for a bounded period: countdown emphasis, warning color, disappearance, disabled controls or historical success styling can imply recoverability or irreversible expiry without authoritative evidence.

## RELATED DOMAIN CHECK
Type T021 remains provisional and supplies only discrimination constraints. I033/L037 own existence and recovery behavior; the next interaction/layout contract owns retention authority and expiry transition. W046 provides runtime provenance. CD052 owns wording and already forbids unsupported recovery promises.

## Visual truth precedence
1. current authoritative existence/recoverability;
2. consequential action availability;
3. retention/expiry certainty and evidence state;
4. historical deletion/recovery events;
5. countdown/time metadata;
6. focus, selection and brand emphasis.

A red countdown, faded row, hidden Restore control, success icon, elapsed client timer or sorted position MUST NOT independently establish that recovery remains available or has expired.

## Required states
Distinguish recoverable-confirmed, expiry-approaching-confirmed, expiry-outcome-unknown, recovery-unavailable-confirmed, authority-unavailable, and policy-unknown. The distinction must survive hue removal, grayscale, forced colors, background removal, focus/selection changes and static export.

## Adversarial matrix
Test client clock skew; tab suspension crossing an expiry boundary; offline display after expiry; policy revision while screen is open; locale/timezone change; countdown reaching zero before authority confirmation; reload/history/export after expiry.

## Acceptance
Visual state may change to irreversible/unavailable only from authoritative recoverability evidence. A local countdown reaching zero may trigger recheck/blocking, not fabricate confirmation.

## Evidence boundary
No runtime artifact, calibrated display, CVD/low-vision observer or human salience/task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Interaction supplies the recoverability oracle; Layout keeps current consequence adjacent to retention evidence; Web must execute boundary crossings; Content must not translate local time passage into confirmed expiry.