# Candidate 03 — Layout / Spatial Review — 2026-09-20

Status: **CHANGES REQUIRED BEFORE OWNER REVIEW**

Evidence reviewed:
- Candidate 03 Flutter implementation at `bf2f45a4f676f2473e0ab5536ca6ab7e2d0f1046`
- 390×844 code-mirror render
- current L106 geometry constraints

This review does not consult prior Home candidates.

## Findings

### Works

- Macro hierarchy is clear: compact period masthead, Search, a dominant Recent Flights field, a split analytical field, then primary commands.
- Recent Flight rows preserve stable operational axes while giving Route more visual weight.
- Activity and Totals share one lower field without turning into independent cards.
- The concept does not rely on a global fixed coordinate system; its comparison axes are local to the active data regions.
- The layout reads as one composed surface rather than a stack of containers.

### Problems

1. **The command rail is visually detached from the working surface.**
   The flexible spacer leaves a large dead region between Activity/Totals and Add Flight/View Logbook. On the reviewed 844px viewport, this feels less like deliberate breathing room and more like an unowned area.

2. **Activity period control is under-resolved inside the half-width panel.**
   Four labels compete for a narrow column. In the current review render, the compact line is already near its useful width limit. The Flutter Wrap may reflow `Custom`, changing the lower-field height and balance.

3. **The lower split needs stress against real width variation.**
   Total values such as `1,163+55` fit at 390px, but narrow width, larger text and different resolved fonts can collapse the two-column balance.

4. **The current masthead has an aggressive asymmetry.**
   The large monthly value dominates the center while the year metric is compressed at the right. This is a coherent thesis, but Type review must reduce the scale or establish a stronger proportional relation.

## Required correction

- Remove the large unowned spacer; keep commands in the content flow rather than visually floating at the bottom.
- Redesign the Activity period selector for the half-width context, preferably a compact 2×2 or another geometry that gives all four options equal legitimacy.
- Allow the lower analytical field to stack at an explicit breakpoint and under enlarged text.
- Re-render after the type-scale correction.

Verdict: **NOT OWNER-REVIEW ELIGIBLE YET.**
