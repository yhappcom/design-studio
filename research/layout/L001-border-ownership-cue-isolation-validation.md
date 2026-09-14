# L001 Validation — Border Ownership Cue Isolation With Identical Local Edge

Status: **PRACTICE + CRITIQUE / CONTROLLED STIMULUS VALIDATION — local-edge isolation and blinded test protocol established; human border-ownership judgments remain OPEN**

Owner: Layout, Spatial & Interaction Specialist  
Canonical parent study: `research/layout/L001-figure-ground-balance-optical-centering.md`

Reproducible artifacts:

- `research/layout/L001-border-ownership-specimen.html`
- `research/layout/L001-border-ownership-playwright.py`
- `research/layout/L001-border-ownership-results-summary.json`

## Objective

Strengthen L001's figure-ground / border-ownership method without pretending that browser pixels can decide which side people perceive as figure.

The experiment asks a narrower methodological question:

> Can Design Studio construct mirrored figure-ground stimuli in which the **central shared edge is pixel-identical** while only remote contextual cues change, so later human judgments can test context-driven border ownership without a local-edge confound?

This is a stimulus-isolation and human-test-readiness study, not a human perception result.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: `progress/TYPE_STATUS.md` through T005.
- Reusable finding: Type's renderer work distinguishes source geometry, raster result and perceived/optical judgment; L001 uses the same evidence separation.
- Replication / challenge / transfer opportunity: future icon+label/container cases can test whether type mass or text expansion changes ownership cues.
- Dependency or overlap: no font conclusion is claimed here.

### Color
- Evidence checked: `progress/COLOR_STATUS.md` through newly completed C007, plus C001/C002/C006.
- Reusable finding: Color C007 and Layout L005 independently confirm that feature fields can change while geometry is fixed; C001/I003 show color/shadow-only structure can disappear under user overrides.
- Replication / challenge / transfer opportunity: the present border-ownership stimulus deliberately uses one neutral palette so Color is not a hidden variable. Later tests can add luminance/chroma as an explicit second factor.
- Dependency or overlap: Color owns color salience/contrast conclusions; Layout owns spatial/contextual boundary structure.

### Layout / Interaction
- Evidence checked: parent L001; Study 014 grouping; current `progress/LAYOUT_STATUS.md`.
- Reusable finding: grouping cues cooperate or compete; shared boundary ownership is contextual; Interaction ownership should agree with perceptual object structure.
- Replication / challenge / transfer opportunity: isolate closure, contour-junction and attachment/continuity cues while keeping the central edge identical.
- Dependency or overlap: direct extension of L001.

### Web Design
- Evidence checked: `progress/WEB_STATUS.md`; no substantive W### study exists at this checkpoint.
- Reusable finding: Web should later test the same ownership problem in real cards, popovers, tables, sticky layers and overlays.
- Implementation/application validation opportunity: replace abstract stimuli with production page/component structures only after the cue-isolated baseline is understood.
- Dependency or overlap: this Chromium lab stimulus is not Web canonical product validation.

### Other / cross-cutting
- Evidence checked:
  - Zhou, Friedman & von der Heydt (2000), *Coding of border ownership in monkey visual cortex*, J Neurosci 20(17):6594–6611, DOI `10.1523/JNEUROSCI.20-17-06594.2000`;
  - von der Heydt & Zhang (2018), *Figure and ground: how the visual cortex integrates local cues for global organization*, J Neurophysiol 120(6):3085–3098, DOI `10.1152/jn.00125.2018`.
- Reusable finding: border-ownership responses can differ for locally identical edges because of wider image context; T/L contour junctions can contribute to figure-ground organization.
- Dependency or overlap: macaque neural evidence and psychophysical figure-ground theory justify the isolation logic, not a direct UI prescription.

### Overlap decision
- **EXTENSION + METHOD VALIDATION + HUMAN-TEST PREPARATION**.
- Why: L001 already established the theory. This block validates a reproducible stimulus set that can later collect actual observer evidence.

---

# SOURCE / SYNTHESIS BOUNDARY

## SOURCE

Zhou et al. showed border-ownership-selective responses where the local edge in the receptive-field region could be identical while wider context differed.

von der Heydt & Zhang later demonstrated that widely distributed contour features, including T- and L-junctions, can influence border-ownership representation.

## SYNTHESIS

For a controlled Design Studio test, the central edge should be held fixed while the surrounding contextual cue is manipulated.

## STUDIO JUDGMENT

A useful figure-ground validation should not compare two stimuli where border thickness, local contrast, color, central edge position and global enclosure all change simultaneously. That makes the causal cue uninterpretable.

---

# Controlled stimulus set

All stimuli use:

- identical 360×220 card bounds;
- identical 320×160 stage;
- identical neutral fills;
- identical 2px central vertical shared edge;
- identical central local crop;
- no shadow, hue or text-content manipulation inside the perceptual field.

Stimulus classes:

1. **B0 — baseline**: central edge only.
2. **E-L / E-R — enclosure pair**: remote top/bottom/outer contours close the left or right region while the central edge stays unchanged.
3. **T-L / T-R — contour-junction pair**: horizontal contours terminate at the central edge on one side; junctions sit outside the measured local crop.
4. **C-L / C-R — attachment/continuity pair**: remote tabs attach to one side of the field, changing global object context without changing the shared-edge crop.
5. **X-L / X-R — cue-conflict pair**: enclosure favors one side while contour-junction structure is placed on the opposite side.

The conflict pair is intentionally diagnostic. It is not assumed that one cue universally dominates.

---

# Failure → revision

## Initial failure

The first HTML version accidentally applied the T-junction class to both the outer card and the inner stage.

The automated local-crop comparison detected that:

- `T-L` vs `T-R` local crop differed by about **1.625%**;
- the conflict pair inherited the same contamination.

That would have invalidated the intended "same local edge, different context" method.

## Revision

The cue class was scoped only to the inner stage.

## Re-proof

After revision:

- all 9 stimuli share the same local-crop SHA-256:
  `610efe43d8fd9e7a7c7ff041157000ac8a5233e0f8c7be8be32cbb4726d48e2a`;
- `all_local_crops_equal_baseline = true`;
- every mirrored pair has `local_crop_diff_fraction = 0`;
- remote context remains materially different.

Remote-context pixel-difference fractions after masking the local crop:

- E-L vs E-R: about `2.24%`;
- T-L vs T-R: about `1.25%`;
- C-L vs C-R: about `3.89%`;
- X-L vs X-R: about `3.44%`.

The exact percentages are implementation checks, not perceptual effect sizes.

---

# What this validates

This block establishes that Design Studio now has a reproducible set where:

1. the shared edge under test is locally pixel-identical;
2. contextual structure differs outside that crop;
3. left/right variants are mirrored experimental controls;
4. cue-agreement and cue-conflict conditions can be compared without changing central edge color/thickness;
5. future observer responses can therefore be attributed more cleanly to wider context than to obvious local-edge differences.

# What this does **not** validate

It does not establish:

- which side human observers will assign as figure;
- the strength of any cue;
- whether UI cards behave like classic psychophysical stimuli;
- whether enclosure, junction or continuity cues have additive weights;
- any universal card/border/elevation recipe;
- aesthetic preference.

No human data were fabricated.

---

# Blinded human-test protocol

When observers are available:

## Task

Show one stimulus at a time at intended size with the stimulus ID hidden.

Prompt:

> Which side appears to be the object/figure that owns the central vertical boundary?

Response:

- Left
- Right
- Ambiguous / neither

Then collect confidence separately, e.g. 1–5.

Do **not** ask which version is prettier.

## Randomization

The harness stores deterministic example orders for seeds `101`, `202`, `303`, `404`. A real study should assign randomized order per observer and avoid presenting mirrored pairs consecutively where practical.

## Analysis plan

Analyze separately:

- baseline ambiguity rate;
- mirror consistency for E/T/C pairs;
- cue-agreement vs cue-conflict response shifts;
- left/right response bias independent of stimulus;
- confidence separately from forced-choice direction.

Do not pool aesthetic preference with border-ownership judgment.

## Decision gate

Only after observer data should Design Studio claim that a specific cue reliably changes perceived ownership in these rendered stimuli.

---

# PROJECT READINESS

## When to apply

Use this knowledge when a UI has adjacent or overlapping regions where task understanding depends on which surface is perceived as the object or owner:

- popover over page content;
- selected row inside a parent table/card;
- drawer/sheet over underlying content;
- nested cards;
- sticky header over scrolling content;
- drag target vs surrounding region;
- comparison panels sharing borders.

## What decision it changes

Before adding more border/shadow/color, identify the intended owner of the shared boundary and vary contextual cues one at a time.

## Failure mode

If a designer strengthens every cue simultaneously, the result may become visually heavy and still fail to reveal which cue was necessary.

## Current recommendation

For consequential ownership problems:

1. preserve a clear intended object structure;
2. test cue-isolated variants;
3. keep local edge properties controlled when diagnosing contextual ownership;
4. combine cues only after their role is understood;
5. validate with observers if misassignment can affect task interpretation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: local geometry can be held identical while wider context changes; future icon+label/text-container tests should isolate Type mass from boundary cues.
- Canonical section: Controlled stimulus set / Failure → revision.
- Confirmation / contradiction / transfer note: method transfer only.
- Scope limit: no Type behavior measured.

### Color
- Useful finding/context: this experiment intentionally neutralizes Color, complementing C007/L005 which isolate Color with geometry fixed.
- Canonical section: Controlled stimulus set.
- Confirmation / contradiction / transfer note: **COMPLEMENTARY FACTOR ISOLATION** — L005/C007 vary Color with fixed geometry; this block varies spatial context with fixed local edge/palette.
- Scope limit: no color-salience threshold or contrast recommendation.

### Layout / Interaction
- Useful finding/context: a central boundary can now be tested against remote enclosure/junction/continuity context without local-edge contamination.
- Canonical section: Re-proof / Blinded human-test protocol.
- Confirmation / contradiction / transfer note: strengthens L001 method, does not yet prove human ownership direction.
- Scope limit: observer validation still required.

### Web Design
- Useful finding/context: abstract ownership controls can be transferred to real popover/card/table/sheet/sticky-layer structures.
- Web application / validation consequence: keep local edge, content and Color controlled while changing only one contextual ownership cue in production-like browser prototypes.
- Confirmation / contradiction / transfer note: implementation transfer target.
- Scope limit: current specimen is an abstract Chromium lab control, not complete web UX evidence.

---

## OPEN

- blinded human ownership judgments for the current stimuli;
- realistic UI transfer with content and interaction states;
- Color/luminance as an explicit second factor;
- motion/appearance/disappearance and temporal ownership cues;
- touch/keyboard/focus implications where visual and interaction ownership diverge;
- cross-browser/device/physical-display replication.
