# Exercise 014 Critique — Perceptual Grouping as Spatial Grammar

Status: CRITIQUE

Paired artifact: `product-design/exercises/014-perceptual-grouping-spatial-grammar.svg`

Research basis: `research/014-perceptual-grouping-spatial-grammar.md`

## Purpose

The exercise tests whether basic spatial relationships can communicate grouping in grayscale without relying on color, decoration, or a component library. It is deliberately not a polished product screen. The goal is to expose the spatial mechanisms themselves.

## What is measured versus what is inferred

Measured in the artifact:

- Panel A uses a 30-unit within-pair distance and 70-unit between-pair distance.
- Panel B intentionally places the nearest two dots across region boundaries at 30 units while dots inside a region are 81 units apart.
- Panel C keeps comparable element scale while changing the object structure from separate circular controls to one connected segmented surface.
- Panel D uses multiple levels of spacing without enclosing every metric.
- Panel E adds boundaries at page-section, row, and item levels to deliberately inflate region strength.

Not measured:

- actual user response time;
- grouping-choice probability;
- eye movement;
- comprehension accuracy;
- performance with low vision or magnification;
- behavior after localization or real platform text scaling.

Therefore this artifact is visual design evidence, not a human-subject perceptual experiment.

---

## Panel A — Proximity only

### Observation

The construction provides repeated pairs with a visibly smaller local gap than the nearest competing gap. No region, connector, color, or typography is allowed to establish the pair relationship.

### KEEP

- one variable is isolated reasonably well;
- grayscale prevents chromatic similarity from rescuing the grouping;
- repeated geometry makes the intended grouping inspectable rather than anecdotal.

### REWORK

The 30:70 distance selection is an exercise parameter, not a validated UI ratio. A later rendered experiment should vary the ratio progressively and collect forced-choice grouping responses rather than assuming one threshold.

### REJECT

Do not turn 30:70, or any simplified ratio derived from this drawing, into a spacing-system prescription.

---

## Panel B — Common region versus proximity

### Observation

The shortest distance occurs across two separate regions. If the viewer groups by shortest distance alone, the middle pair should dominate. If common region dominates, the two elements inside each region should form the stronger units despite greater internal separation.

### KEEP

This is the strongest panel conceptually because it creates **cue conflict** rather than presenting a cooperative ideal state. It is closer to the kind of ambiguity that causes real interface failures.

### REWORK

The regions use both fill and outline. A follow-up should separate these cues:

1. outline only;
2. fill discontinuity only;
3. subtle material/elevation boundary;
4. no explicit region.

That will distinguish boundary ownership from general tonal similarity.

### REJECT

A card is not automatically justified because it makes a group easier to see. Region strength must correspond to a semantic region in the product.

---

## Panel C — Connectedness changes the unit model

### Observation

Three visually similar circular controls are first shown as independent objects and then embedded into one continuous segmented surface.

### KEEP

The exercise makes a useful interaction-layout connection: spatial connection changes not only appearance but the likely conceptual model of the control cluster.

### REWORK

A real interaction prototype must test:

- whether the connected version behaves as mutually exclusive options;
- focus order and keyboard operation;
- pointer/touch hit regions;
- whether selected state remains legible without relying on connection alone.

### REJECT

Do not connect independent destructive or heterogeneous actions simply to make a toolbar compact. Shared chrome can imply shared behavior.

---

## Panel D — UI spacing hierarchy

### Observation

The panel uses typography, alignment, and whitespace to construct multiple relationship levels:

- label → value;
- value pair → metric row;
- metric row → section;
- section → next section.

Individual metrics are not boxed.

### KEEP

- hierarchy is carried by more than one restrained cue;
- shared alignment supports comparison and scanning;
- the composition demonstrates that strong containment is unnecessary for every group;
- the example is close enough to a dense product context to reveal transfer beyond abstract dots.

### REWORK

This panel still needs:

- long Korean and English labels;
- RTL adaptation;
- 200% text-size/reflow proof where applicable;
- narrow-width recomposition;
- realistic data extremes such as very long durations or multi-digit counts.

### REJECT

Do not preserve the current two-column arrangement when width or text growth makes the grouping ambiguous. Relationship preservation has priority over coordinate preservation.

---

## Panel E — failure through container inflation

### Observation

The same broad information is wrapped at several nested levels. This repeatedly introduces region boundaries that are stronger than the underlying semantic differences.

### KEEP

Keep this as negative evidence. The studio needs explicit failure examples rather than only polished successful directions.

### REWORK

A later comparison should measure whether users overestimate independence among nested items or whether scan time increases relative to a spacing/alignment version.

### REJECT

Reject the assumption that additional surfaces always increase clarity. Containment has perceptual cost: it creates objects and competes for hierarchy.

---

# Cross-panel synthesis

## 1. Spacing is relational, not nominal

The exercise supports a design method in which spacing is evaluated against neighboring separations rather than only against token names. This is a studio method derived from perceptual evidence; it is not a claim that the current geometry establishes universal thresholds.

## 2. Containment must earn its strength

Common region is visually powerful enough that cards, panels, and tinted surfaces should be treated as structural decisions. The stronger the region cue, the stronger the semantic grouping should be.

## 3. Connection can alter the conceptual object

Connected surfaces and lines can imply a single mechanism or shared state space. Layout and interaction cannot be separated at this point.

## 4. Hierarchy needs unequal grouping strength

A page with several nested levels should not represent every level with equally strong borders. Different levels need different grouping strength, otherwise the visual hierarchy flattens into repeated containers.

## 5. Grayscale is a useful spatial stress test

Because this exercise does not use hue to distinguish groups, any surviving hierarchy must come from geometry, type, value contrast, alignment, region, and connection. Grayscale is not sufficient accessibility validation, but it is useful for exposing reliance on decorative color.

---

# KEEP / REWORK / REJECT summary

## KEEP

- cue-isolation exercises before full-screen styling;
- explicit cue-conflict tests;
- separation of abstract perceptual probes from realistic UI transfer;
- negative evidence showing over-containerization;
- grayscale as one spatial robustness test;
- measured geometry documented alongside design interpretation.

## REWORK

- render the UI fragment in a browser/app rather than SVG only;
- introduce multilingual and enlarged-text stress;
- separate outline/fill/elevation forms of common region;
- collect human forced-choice or task evidence where practical;
- test semantic reading/focus order alongside visual grouping.

## REJECT

- magic spacing ratios;
- “Gestalt checklist” justification after styling;
- card-per-group as a default composition strategy;
- assuming visual grouping automatically equals semantic grouping;
- claiming foundation PASS from static designer inspection alone.

---

# Gate result

**Result: evidence added; no PASS.**

The exercise materially strengthens `Composition / visual grammar` by adding perceptual grouping, cue conflict, region strength, connection, and container-failure evidence. It remains at `CRITIQUE` until the spatial relationships survive realistic rendering, text expansion/localization, and at least one observation method beyond self-critique.
