# C036 — Partial-authority cue composition critique

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / CRITIQUE PROTOCOL**

## RELATED DOMAIN CHECK
I022 defines which facts are known and which actions are safe; L026 owns association/proximity; W035 owns runtime provenance; CD041 owns semantic wording; Type owns glyph discrimination. Color only evaluates visual encoding and degradation.

## Problem
C035 can remove individual cues, but a product can still fail by composing individually valid cues into a misleading hierarchy. The high-risk case is a partially authoritative object that visually resembles a globally confirmed object because the dominant surface/background cue overwhelms a smaller uncertainty cue.

## Composition audit
For each shared state (`confirmed`, `lastKnown`, `partial`, `unavailable`, `conflict`) record four independent layers:
1. **surface/base** — neutral container/background;
2. **state boundary/marker** — authored non-text distinction;
3. **semantic text/action** — non-color truth;
4. **focus/selection** — interaction state, never reused as authority state.

Critique fails when focus/selection color can be mistaken for authority, when a confirmed surface token is inherited by a partial child without a local uncertainty marker, or when conflict and destructive-action color compete for the same visual channel without textual distinction.

## Adversarial matrix
Run each state under: normal light, normal dark, hue removed, icon/shape removed, forced-colors, focused control, selected row, sticky overlay intersection, and 200% zoom/reflow capture. Verdicts remain separate for contrast, state distinguishability, focus visibility and obscuration.

## Transfer rule
A partial-authority design is acceptable only if the affected object/action remains locally identifiable when the strongest authored color cue is removed. Global banners cannot substitute for local association where only some fields/actions are uncertain.

## Evidence boundary
No runtime, forced-colors, CVD/low-vision observer, calibrated-display or human salience PASS is claimed. C036 is ready to consume W035 executed captures.

## HANDOFFS
L026 must provide local geometry; I022 provides fact/action dependency; CD041 provides exact semantic IDs; W035 provides engine/run provenance. Any failure caused by ambiguous glyphs returns to Type rather than being patched with stronger color.
