# L073 — Semantic Locus Reveal and Scroll Anchoring

## Purpose
Extend L072: after I069 identifies the correct semantic focus/recovery owner, determine whether spatial recomposition keeps that locus usable without unnecessary viewport displacement.

## RELATED DOMAIN CHECK
I069, Type T050, Color C081, Web W081 and Content CD087 checked. This is a Layout transfer of semantic-identity requirements, not a claim about Interaction state ownership.

## SOURCE / SYNTHESIS
WCAG 2.2 SC 2.4.11 requires focused UI not be entirely obscured by author-created content. SC 2.4.12 is the stronger AAA full-visibility criterion. The studio additionally needs professional-workflow continuity: visibility alone does not justify large scroll jumps or a semantically wrong locus.

## Spatial contract
For each mutation record viewport, 100%/200% text or zoom, safe-area/keyboard/sticky surfaces, before/after scroll offset, semantic focus/recovery ID, focus and target rectangles, visible fraction, nearest sticky/overlay rectangle, row height/wrap count and preceding/following semantic neighbors.

Evaluate four outcomes separately: correct identity + stable geometry; correct identity + necessary minimal reveal; correct identity + excessive displacement; wrong identity regardless of visual visibility.

## PRACTICE / CRITIQUE matrix
Use top/middle/bottom items, long labels, system groups, first/last boundary actions and Reset recovery. Repeat after reorder, hide/show, Reset/Undo and 200% recomposition. Prefer the smallest scroll adjustment that reveals the valid locus; do not freeze an absolute pixel threshold across viewport classes.

A visually smooth animation is not evidence of semantic continuity. A fully visible focus ring on the wrong field is FAIL. A correct field partly visible can satisfy WCAG AA yet still require product critique if repeated operation becomes spatially unstable.

## Reproducible validation
Two repetitions per executable mutation. Preserve raw before/after geometry and classify `STABLE`, `MINIMAL-REVEAL`, `EXCESSIVE-DISPLACEMENT`, `OBSCURED`, `WRONG-IDENTITY`, `BLOCKED`.

## OPEN
No runtime L073 execution yet. 200% browser transfer, forced colors, keyboard-height/physical-device conditions and human workload remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Interaction owns which semantic locus is correct. Web captures actual browser/runtime geometry. Color checks focus/recovery visibility. Content protects labels/status under recomposition. Type failures require reproduced font evidence, not density inference.