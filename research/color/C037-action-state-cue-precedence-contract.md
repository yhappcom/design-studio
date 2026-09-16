# C037 — Action-state cue precedence contract

Date: 2026-09-16
Purpose: **SYSTEMS PRACTICE / CONTRADICTION PREVENTION**

## RELATED DOMAIN CHECK
I023 owns whether an action is safe; L027 owns locality; W036 owns runtime provenance; CD042 owns semantic wording; Type owns glyph discrimination. Color must not visually overrule any of them.

## Problem
A locally correct authority marker can still be contradicted by stronger component styling: a vivid primary button may visually imply readiness while I023 says the action is blocked, or selection/focus styling may be mistaken for confirmed authority.

## Precedence model
Visual interpretation must preserve this order of truth:
1. action availability/safety from Interaction;
2. local authority/certainty state;
3. selection/focus/input modality;
4. brand/emphasis styling.

Brand emphasis never upgrades blocked/unknown/conflicting authority. Focus never means confirmed. Selection never means current. A disabled appearance is not the only acceptable blocked-action encoding, but any alternative must preserve text/non-color semantics and control affordance.

## Adversarial cases
For each W036 run ID test: blocked action + primary brand surface; focused blocked action; selected stale object; conflict state inside globally successful page; forced-colors substitution; dark/light theme inversion. Record whether the dominant visual cue contradicts the semantic/action oracle.

## Evidence boundary
This contract defines critique logic; it is not rendered browser evidence. Contrast, focus visibility, focus obscuration, semantic distinguishability and perceived salience remain separate verdicts. Human interpretation remains OPEN.

## HANDOFFS
W036 records computed/rendered state; I023 supplies expected action verdict; L027 supplies locality/occlusion; CD042 supplies explicit action/state text. Any mismatch is returned to the owning domain rather than repaired by arbitrary color changes.