# C034 — Forced-colors system-color transfer

Evidence: **SOURCE → SYSTEMS PRACTICE / TRANSFER VALIDATION OPEN**

## RELATED DOMAIN CHECK
- Type T021 owns glyph recognition; forced colors cannot repair glyph ambiguity.
- Layout L024 owns focus/overlay geometry and spatial association.
- Interaction I020 owns state/action truth.
- Web W033 owns actual browser execution/provenance.
- Content CD039 owns textual semantic survival.

## Source update
Current CSS Color 4 defines system-color keywords as user/browser/OS color choices and notes that forced-colors mode constrains pages to a user-chosen palette; system colors expose those choices so authored UI can integrate with that palette. WCAG 2.2 remains the studio accessibility baseline. Focus visibility, focus obscuration and semantic availability remain separate verdicts.

## Systems practice
C033's degradation ladder is extended with a concrete forced-colors transfer rule. For every semantic state in the W033 fixture record:
1. authored light/dark appearance;
2. forced-colors active state and computed system-color behavior;
3. whether state meaning survives without authored hue;
4. whether text/control boundaries remain identifiable;
5. whether focus remains visible;
6. whether focused geometry is obscured — owned by Layout, not inferred from Color;
7. whether any `forced-color-adjust` exception exists and why.

`forced-color-adjust: none` is treated as an exception requiring evidence, not a default technique. Preserving brand color is not sufficient justification when it overrides user-selected contrast behavior.

## Critique oracle
- If semantic meaning disappears with authored hue, fail semantic redundancy and hand off to Content/Interaction/Layout.
- If meaning survives but a boundary/focus cue disappears, classify Color/rendering separately.
- If focus is visible but hidden behind sticky content, Color does not PASS the Layout criterion.
- If a browser substitutes system colors differently, record engine provenance rather than normalizing screenshots into one expected palette.

## Evidence boundary
This note is source-grounded systems practice. No actual forced-colors browser execution, calibrated display, CVD/low-vision observer, perceived salience or human task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture computed styles plus screenshots under forced-colors. Layout supplies overlap rectangles. Content supplies text-only semantics. Interaction supplies authoritative state/action IDs. Type supplies identifier rendering only after T021.