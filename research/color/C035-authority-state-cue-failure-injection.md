# C035 — Authority-State Cue Failure Injection

Date: 2026-09-16
Evidence class: **SYSTEMS PRACTICE / ADVERSARIAL VALIDATION / RUNTIME OPEN**

## RELATED DOMAIN CHECK
Type T021 owns glyph discrimination; I021 owns authority/freshness truth; L025 owns priority/occlusion; W034 owns browser provenance; CD040 owns the semantic labels.

## Research question
Can current-confirmed, last-known, authority-unavailable and conflict remain distinguishable when authored visual channels degrade independently?

## Failure-injection matrix
For every shared W034 run ID, test independently:
1. authored hue available;
2. hue neutralized while text/structure remain;
3. icon/shape cue removed;
4. border/background cue removed;
5. forced-colors active with system colors;
6. keyboard focus traverses state and recovery controls;
7. sticky/overlay geometry approaches focused control;
8. dark/light theme switch where implemented.

Record semantic ID, rendered text, computed foreground/background/border, focus visibility, overlap rectangle, forced-color-adjust value, and whether meaning survives without the removed cue.

## Critique rules
- A state is not robust merely because one remaining color differs numerically.
- Text that names the state can preserve semantics, but poor spatial association is a Layout failure rather than a Color PASS.
- A visible focus indicator can still fail if entirely obscured; C035 consumes L025 geometry rather than inferring it from color.
- `forced-color-adjust:none` is an exception requiring a demonstrated semantic need and separate contrast/focus evidence.

## Current result
Protocol is reproducible; runtime evidence is OPEN. No Stage 3 PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
L025 receives any association/occlusion failures; CD040 receives semantic-label failures; W034 records engine provenance; Type receives glyph ambiguity only when text rendering itself is the failure.
