# C043 — Time Provenance and Clock-State Visual Contract

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION**

## Question
When audit/export/recheck workflows show multiple times, can visual hierarchy preserve the difference between event time, observation time, reconciliation time, snapshot-generation time and current-check time without implying false freshness?

## RELATED DOMAIN CHECK
- Type: T021 operational strings include numerals; repaired ambiguity-critical glyphs must survive timestamp and identifier density before product transfer.
- Layout/Interaction: I029/L033 own snapshot-to-live behavior and hierarchy; Color cannot redefine freshness.
- Web: W042 owns actual runtime/export evidence and browser media transfer.
- Content: CD048 owns timestamp semantics; locale formatting may reorder or expand time strings.
- UX: human salience and comprehension remain OPEN. This study evaluates deterministic cue precedence and degradation only.

Purpose: **TRANSFER VALIDATION** from C039–C042 into temporal provenance.

## Truth model
Color may reinforce, but never create, these distinctions: `eventOccurredAt`, `observedAt`, `reconciledAt`, `snapshotGeneratedAt`, `authorityConfirmedAt`, and `recheckedAt`.

A visually prominent recent timestamp must not make an older authoritative fact appear newer than it is.

## Visual precedence
1. current consequence or intervention state;
2. freshness or authority warning when action-relevant;
3. timestamp role label and value;
4. historical event chronology;
5. selection and focus;
6. brand or decorative emphasis.

Recency alone is not a semantic priority token.

## Degradation matrix
Test the same audit/recheck specimen under light/dark, grayscale, hue removal, background-color removal, icon removal, border/shape removal one at a time, forced-colors, print-color emulation, monochrome print, selected historical row plus keyboard focus plus current consequence, and long localized timestamps with explicit zone labels.

## Deterministic failures
FAIL when a timestamp color is the only cue distinguishing generated versus confirmed versus rechecked time; when a recent snapshot-generation time visually outranks an older authority-confirmed time without semantic warning; when historical success is stronger than a current changed/unavailable state; when selection/focus can be mistaken for freshness; or when grayscale/background loss removes the snapshot/current distinction.

## Accessibility boundary
WCAG 2.2 remains the screen baseline. Color-only meaning is insufficient; focus visibility and focus obscuration remain separate checks. Static PDF/print is not declared WCAG-conformant merely because the source page passes.

## Evidence boundary
No actual W042 artifact has been executed against this matrix. No observer, CVD participant, low-vision participant, physical-print or calibrated-display claim is made.

## HANDOFFS TO OTHER SPECIALISTS
Content must label timestamp role rather than depend on color. Layout keeps action-relevant freshness adjacent to consequence/action under reflow. Web captures computed style/media plus timestamp role/value in shared provenance. Type treats timestamp density as a post-repair operational-string stress case.
