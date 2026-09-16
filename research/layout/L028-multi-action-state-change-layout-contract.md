# L028 — Multi-action state-change layout contract

Date: 2026-09-16
Purpose: **SYSTEMS PRACTICE / RESPONSIVE TRANSFER CONTRACT**

## RELATED DOMAIN CHECK
I024 owns temporal action truth; C037 owns cue precedence; W037 records browser geometry/runtime; CD043 owns changing-state language; Type metrics remain provisional until T021.

## Spatial requirement
When multiple actions on one object diverge in availability, layout must keep each action attributable to its own evidence/consequence. A global banner or distant status label cannot be the sole explanation for a local blocked mutation.

## Dynamic-state checks
Across baseline, 320 CSS px reflow, actual 200% zoom, localization expansion and reduced visual viewport where executable, record:
- object/evidence/action bounding rectangles;
- reading/focus order;
- action movement after pending/conflict/reconciliation state changes;
- sticky/fixed overlap;
- whether the explanation for a newly blocked action remains adjacent/traceable;
- whether a control disappearing/reordering causes focus loss or accidental activation risk.

Prefer stable placement with state change over unnecessary control relocation. When an action must disappear, focus destination and recovery path belong to Interaction/Web evidence, not visual guesswork.

## Evidence boundary
DOM geometry is not perceived association. 320 CSS px is not actual 200% zoom. Headless execution is not physical-device evidence. Human discoverability and cognitive load remain OPEN.

## HANDOFFS
W037 supplies executed rectangles and focus transitions; I024 supplies expected enabled/blocked transitions; C037 checks visual contradiction; CD043 supplies local explanations.