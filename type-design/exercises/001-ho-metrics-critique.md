# Exercise 001 Critique — H/O Metrics Control

Status: PRACTICE / REWORK REQUIRED

Related specimen:
- `type-design/exercises/001-ho-metrics-three-hypotheses.svg`

Research basis:
- `research/002-metrics-spacing-optical-rhythm.md`

## Exercise intent

Test whether the studio can separate:

- visible contour;
- sidebearing;
- advance width;
- internal counter;
- overshoot;
- repeated sequence rhythm;

before introducing kerning or a product-specific visual identity.

This is intentionally not a LogMate typeface exercise.

## Hypothesis A — neutral grotesk / moderate width

Concept:
- moderate width;
- low contrast;
- broad round counter;
- symmetric nominal bearings;
- moderate O overshoot.

### KEEP

- Straight/round contrast is easy to inspect.
- `H/O` width parity makes advance-width behavior legible as a controlled variable.
- Round form extends beyond nominal cap zone, correctly treating overshoot as an optical question rather than a coordinate error.

### REWORK

- The O is built from simple rounded rectangles, not production-quality Bézier contours. Therefore this artifact cannot support a Bézier-quality PASS.
- Equal advance widths make the experiment clean, but they also hide the question of whether proportional width differences improve text color.
- The specimen currently shows a short repeated sequence, not enough language texture.

### REJECT as evidence for mastery

- The artifact does not prove raster quality.
- It does not prove word spacing, lowercase rhythm, or family coherence.
- It must not be used as a visual direction for any product.

## Hypothesis B — narrow architectural / higher vertical emphasis

Concept:
- reduced width;
- similar nominal sidebearing logic;
- relatively tall/narrow internal counter;
- stronger vertical texture.

### Observation

Even with a similar straight/round spacing rule, narrowing the contour changes the perceived white-space distribution. The metric number cannot be judged independently from the counter and outer silhouette.

This supports the research claim that spacing is not a numeric cleanup layer: form and metric design are coupled.

### KEEP

- Useful contrast against A because the texture becomes visibly more vertical without changing the basic exercise logic.

### REWORK

- The specimen uses a scaled group for expedience. That distorts stroke relationships and is not acceptable as professional type drawing practice.
- A future version must redraw the narrow hypothesis natively rather than transform the broad one.

### REJECT

- Do not infer that narrowness is more 'premium', more 'technical', or more appropriate for data. This exercise tests rhythm only.

## Hypothesis C — broad humanist oval / asymmetric optical balance

Planned construction:
- broader O than H;
- mild asymmetric stress;
- optical rather than numerically mirrored bearings if required by curve/stress distribution;
- differentiated advance widths.

### Failure finding

C was specified but not actually drawn in the first specimen.

That means the exercise does **not** satisfy its own 'three hypotheses' brief.

This is preserved deliberately as failure evidence rather than rewritten as success.

**Disposition: REWORK.** The next metrics exercise must include a genuinely redrawn C and cannot reuse geometric scaling as a substitute.

## Classification drill: drawing vs spacing vs kerning

### Scenario 1
`HOH`, `OOH`, `HOOH`, and unrelated round-adjacent strings all feel too open around O.

Likely first diagnosis: **spacing**. Inspect O bearings and shape-space relationship.

### Scenario 2
Most rhythm is even but `VA` creates an exceptional wedge of white.

Likely diagnosis after spacing is stable: **kerning**.

### Scenario 3
O looks too small even when top/bottom coordinates equal H cap/baseline.

Likely diagnosis: **optical drawing/alignment**, potentially overshoot—not sidebearing.

### Scenario 4
A narrow O seems too dark at the joins after horizontal scaling.

Diagnosis: **drawing/construction failure**. Do not repair with spacing.

## What this exercise actually proves

It provides practice evidence for:

- distinguishing contour from metric box;
- advance width / LSB / RSB reasoning;
- spacing-before-kerning classification;
- overshoot as an optical compensation concept;
- critique that rejects invalid construction shortcuts.

It does **not** prove:

- Bézier mastery;
- professional optical correction;
- lowercase spacing;
- actual font editor competence;
- rasterization quality;
- complete Stage 1 type foundations.

## Next exercise

1. Redraw three H/O hypotheses without geometric scaling shortcuts.
2. Add `n/o` controls.
3. Generate longer proof strings.
4. Compare at at least three intended pixel sizes.
5. Record drawing vs spacing vs kerning diagnoses before any pair kerning.
6. Only after that consider promoting spacing/metrics from PRACTICE toward CRITIQUE/PASS.
