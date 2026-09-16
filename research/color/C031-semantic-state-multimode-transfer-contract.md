# C031 — Semantic-State Multimode Transfer Contract

Date: 2026-09-16
Evidence: SYSTEMS PRACTICE / TRANSFER VALIDATION CONTRACT / OPEN

## RELATED DOMAIN CHECK
- **Type:** T021 ambiguity remains independent; state color must not compensate for unreadable glyphs.
- **Layout/Interaction:** I017 owns certainty/action enablement; L021 owns focus/overlay geometry.
- **Web:** W029/W030 own browser execution provenance.
- **Content:** CD036 owns state/action language; Color must preserve meaning when hue is unavailable.

## Problem
C029/C030 correctly separate contrast, focus obscuration and forced-colors, but Stage 3 needs a reusable state-transfer contract that tests the *same semantic state* across ordinary theme, forced colors, no-color/redundant coding and focus/overlay stress without silently changing Interaction truth.

## State set
Minimum shared states: idle/available; pending; outcome-unknown; confirmed/success; known rejection/failure; reconciled-not-found; conflict/review-required; disabled/unavailable.

For each semantic ID record independently:
1. authored foreground/background pair and computed contrast where applicable;
2. non-text boundary/indicator pair where the indicator conveys state;
3. non-color carrier (text, icon shape, border/pattern, position or other redundant cue);
4. focus indicator visibility and overlap result;
5. forced-colors/high-contrast result using system colors or preserved semantics;
6. light/dark/system theme mapping;
7. selected/pressed/disabled distinctions where interactive;
8. provenance: browser/OS/mode/capture ID.

## Acceptance logic
- A contrast PASS does not imply state distinguishability.
- Hue separation does not imply semantic survival.
- Forced-colors survival does not imply ordinary-theme contrast.
- DOM focus does not imply visible or unobscured focus.
- A disabled appearance may not be used for outcome-unknown when an authoritative reconciliation action remains available.
- Color never changes I017's action enablement contract.

WCAG 2.2 remains the studio accessibility baseline. SC 2.4.11 Focus Not Obscured (Minimum) is treated as a geometry/accessibility check distinct from focus appearance and color contrast; stronger observations remain separately labeled.

## Critique cases
1. `Outcome unknown` and `Known failure` share the same red treatment: FAIL semantic collision even if both contrast ratios pass.
2. `Confirmed` uses green only, with no text/icon distinction: FAIL redundant-semantic requirement for the studio system.
3. Forced colors collapses custom fills but text/state labels remain distinct and focus survives: possible transfer PASS for semantic survival, not a global Color PASS.
4. Sticky action bar covers the focused reconciliation control: Layout/focus-obscuration failure; Color cannot repair it.

## UX integration
This contract reduces state-confusion risk in non-human analysis. It does not establish perceived salience, comprehension, CVD user performance, low-vision performance or professional task success. Those remain HUMAN EVIDENCE OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- **Interaction/Content:** provide stable semantic IDs and enabled actions.
- **Layout:** provide focus/overlay rectangles for the same capture ID.
- **Web:** execute the multimode matrix in actual browsers/OS modes.
- **Type:** provide valid text rendering only after its own gate.
