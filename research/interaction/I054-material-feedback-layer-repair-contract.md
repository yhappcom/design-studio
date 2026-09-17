# I054 — Material Feedback-Layer Repair Contract

Evidence class: **SOURCE + TRANSFER VALIDATION PLAN**

## QUESTION
How should the I053 ListTile/DecoratedBox failure be repaired without treating a visual paint-order defect as merely cosmetic?

## SOURCE
Flutter's current InkWell documentation states that ink reactions paint on an ancestor Material. An opaque Container/Image/DecoratedBox between Material and InkWell can hide the splash. Flutter's Ink documentation gives two supported architectural directions: paint decoration on Material via Ink, or place a transparent Material above opaque graphics so the ink response paints on the visible material.

## PRACTICE — repair alternatives
A. Preferred when decoration belongs to the interactive surface: move the decoration to `Ink`/the Material surface and keep ListTile/InkWell on that material.
B. When opaque content must remain structurally separate: introduce a correctly bounded transparent Material above it for the interactive ink layer.
C. Do not solve by disabling splash/highlight or by changing only token colors; that removes feedback rather than repairing ownership.

## CRITIQUE
I053 is an interaction failure because pressed/selected feedback communicates action and state. A token can be semantically correct yet functionally absent when paint ownership hides it. Repair therefore requires both layer correctness and state visibility.

## REPRODUCIBLE VALIDATION
Under the same 1024×768 workflow fixture: assert no Material/ink ownership exception; activate the affected ListTile by pointer/tap and keyboard where supported; capture pressed/selected state; verify destination/action remains correct; verify focus remains visible and not obscured; verify no new hit-target or stacking regression.

## RELATED DOMAIN CHECK
Type is not causal. Color C066 owns semantic state color but depends on this visible paint surface. Layout L058 may change containment and must not recreate an opaque layer above Material. Web W066/W067 owns runtime/browser evidence. Content labels/actions must remain unchanged unless product semantics change.

## HANDOFFS TO OTHER SPECIALISTS
Color should evaluate rendered state contrast only after I054 establishes visible paint ownership. Layout should treat Material ownership as part of containment architecture. Web should add pointer/keyboard state capture after widget smoke.

## OPEN
No repaired run exists yet. Screen-reader comprehension, physical-device feedback perception and representative-user evidence remain OPEN.