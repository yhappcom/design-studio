# C032 — Redundant State-Cue Independence Audit

Date: 2026-09-16
Evidence: **SYSTEMS PRACTICE / CONTRADICTION REVIEW / EXECUTION OPEN**

## RELATED DOMAIN CHECK
- **Type:** text labels must remain legible and unambiguous; Color cannot repair unfinished glyphs.
- **Layout/Interaction:** I018 owns state/action truth and L022 owns visibility/obscuration geometry.
- **Web:** W031 owns runtime transfer; browser execution remains blocked in the current environment.
- **Content:** CD037/CD038 semantic IDs and labels provide the non-color channel.
- **UX:** end-to-end state recognition requires redundant cues, but human salience/comprehension is not inferred.

## Problem
A multimode matrix can still produce false confidence if every redundant cue ultimately depends on the same visual mechanism. C032 therefore audits **cue independence** rather than merely counting cues.

## Cue classes
For each consequential state record whether meaning is available through:
1. explicit text/state label;
2. action availability/disabled state governed by Interaction;
3. structural placement/grouping;
4. icon/shape/pattern where semantically appropriate;
5. authored color;
6. focus indication;
7. browser/OS forced-color substitution.

Two cues are not independent merely because they look different. Example: a red border plus red icon is one color-dependent failure family if both lose distinction under forced colors. Likewise an icon whose accessible name is missing is not a nonvisual semantic backup.

## Adversarial matrix
Test at minimum: neutral, pending, outcome-unknown, confirmed, known rejection, conflict, reconciled-not-found. For each state ask:
- remove authored hue: is the state still named?
- remove iconography: does text/action truth survive?
- force system colors: is meaning preserved without relying on original palette?
- obscure one visual region: is focus/recovery still reachable? Geometry verdict belongs to L022.
- localize/expand text: does the color token remain attached to the same semantic ID rather than string matching?

## WCAG boundary
WCAG 2.2 remains the baseline. SC 2.4.11 Focus Not Obscured (Minimum) is a geometry/visibility requirement and is not satisfied by contrast alone. C032 therefore refuses a composite “accessibility score.” Contrast, focus visibility, obscuration, semantic redundancy and forced-colors survival are separate verdicts.

## Current result
**AUDIT MODEL READY / RUNTIME EVIDENCE OPEN.** C031 provides the transfer matrix; C032 adds a failure-independence critique so that multiple correlated visual cues cannot masquerade as robust redundancy.

## HANDOFFS TO OTHER SPECIALISTS
- **Interaction/Content:** supply authoritative semantic IDs and enabled actions.
- **Layout:** supply overlap/visibility verdicts.
- **Web:** execute removal/forced-color/localization conditions against shared capture IDs.
