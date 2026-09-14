# Exercise L001 Critique — Figure/Ground, Balance, Tension, Optical Centering

Status: CRITIQUE

Paired artifact: `product-design/exercises/L001-figure-ground-balance-optical-centering.svg`

Research basis: `research/layout/L001-figure-ground-balance-optical-centering.md`

## Purpose

This critique evaluates whether the exercise demonstrates the methods established in L001 without overstating what a static SVG can prove. The exercise is intentionally grayscale and comparative so that geometry, boundary context, and spatial relationships can be inspected without hue becoming a rescue cue.

---

# Evidence classification

## Directly measured or constructed

- identical panel/frame dimensions where stated;
- explicit shared edges and closed contours;
- equal or intentionally changed edge clearance in Panel C;
- fixed 120×120 visual boxes in Panel D;
- declared bounding-box center and area-centroid reference in Panel D;
- visual-child offset separated from the control hit-box concept in Panel E;
- closed popover contour and overlap relationship in Panel E.

## Inferred but not measured from people

- which region viewers actually assign border ownership to;
- whether B1 feels more balanced than B2;
- whether C2 creates more perceived tension than C1;
- which triangle candidate appears best centered;
- whether the popover is detected faster or understood more accurately;
- whether the visual-child offset improves perceived centering at intended device size.

## Not tested

- response time;
- forced-choice preference;
- eye movement;
- low-vision/magnification use;
- real browser or native-app rasterization;
- device pixel ratio effects;
- RTL mirroring;
- Korean/Latin label expansion;
- keyboard/focus behavior;
- assistive-technology interpretation.

The exercise therefore supports `PRACTICE / CRITIQUE`, not `PASS`.

---

# Panel A — Border ownership

## Observation

A1 presents a single shared divider between visually similar regions. A2 closes a contour around one object. A3 introduces overlap/T-junction-style context to create a stronger foreground candidate.

## KEEP

- The panel correctly varies contextual ownership cues rather than merely changing divider thickness.
- It extends Study 014’s grouping work into a distinct figure–ground question.
- It makes the central professional issue inspectable: a boundary should not be treated as semantically neutral when one side is intended to be the object.

## REWORK

A later artifact should isolate specific cues more rigorously:

1. closure only;
2. luminance difference only;
3. T-junction/occlusion only;
4. shadow/elevation only;
5. closure + shadow conflict;
6. selection tint competing with parent-card boundary.

The current panel combines multiple visual effects in A3, so it is useful for transfer but not clean enough for a causal perceptual claim.

## REJECT

Reject a future rule such as “always close the foreground contour” or “use shadows to establish ownership.” The correct cue depends on the product object model and interaction scope.

---

# Panel B — Geometric mass baseline

## Observation

B1 uses two same-sized rectangular masses arranged symmetrically around the vertical center line. B2 changes shape structure while keeping the composition approximately centered around the same frame axis.

The point is not to prove that one is balanced. The point is to expose a methodological distinction:

- geometric centering can be inspected;
- perceptual balance remains a viewer judgment.

## KEEP

- The panel prevents “visual balance” from becoming an untraceable taste statement.
- It provides a baseline suitable for later computational extension.
- It aligns with the research evidence that balance ratings and aesthetic preference are related but not identical constructs.

## REWORK

The next version should compute exact area-weighted centroids from the SVG geometry and print the values in the artifact. B2 currently communicates the method but does not constitute a formally controlled equal-centroid experiment.

A stronger follow-up would create three pairs:

- equal area + equal centroid + different shape;
- equal area + shifted centroid;
- equal centroid + different edge density/detail.

Reviewers could then rate balance while the designer remains blind to candidate labels.

## REJECT

Do not create a studio “visual mass equation” by assigning arbitrary numeric weights to contrast, detail, semantic importance, and area. Those factors can be logged, but combining them requires validation.

---

# Panel C — Tension as causal hypothesis

## Observation

The object and directional orientation are kept similar while clearance to the right frame edge is reduced.

## KEEP

- The panel improves critique vocabulary: instead of “this feels tense,” it names a candidate mechanism—directional content with reduced clearance / blocked affordance space.
- It encourages a control variant rather than aesthetic debate around one composition.

## REWORK

A later study should vary edge clearance parametrically rather than comparing only two states. Candidate clearances might be expressed relative to object width, but no threshold should be promoted before observation.

A second useful manipulation is to reverse the object direction while holding position constant. If the tension judgment follows direction rather than position alone, that is stronger evidence for an affordance-space interpretation.

## REJECT

Reject “near edge = bad.” Edge pressure can be intentional in editorial or expressive compositions. The failure condition is accidental conflict with the intended hierarchy or action meaning.

---

# Panel D — Optical centering

## Observation

Three right-pointing triangle placements are shown in identical visual boxes:

- D1: bounding-box reference;
- D2: area-centroid reference;
- D3: positive horizontal optical-candidate offset.

D3 is explicitly labeled as a candidate rather than a corrected truth.

## KEEP

This is the most transferable method in the exercise:

1. declare the geometric reference;
2. generate controlled offset alternatives;
3. compare at intended size;
4. accept an optical correction only after comparison;
5. keep visual correction separate from interaction geometry.

This avoids the common production failure where an icon is “nudged until it looks right” with no record of the original reference or the offset.

## REWORK

The exercise must be rendered at actual use sizes such as 16, 20, 24, 32, and 44 CSS/device-independent units. A correction that is compelling at 120 px may disappear or reverse under rasterization at smaller sizes.

A proper next experiment should:

- render 0/±δ candidates;
- randomize order;
- hide the offset values from reviewers;
- collect forced-choice “most centered” judgments;
- repeat next to a text label and standalone;
- mirror the directional icon for RTL where semantically appropriate.

## REJECT

Reject a universal `+1 px` or `+2 px` icon correction token. Optical correction belongs to a specific source shape and rendering context unless broader validation supports reuse.

---

# Panel E — Realistic transfer

## Observation

The panel applies the research to a low-density command/data surface:

- a summary card uses restrained hierarchy and a section divider;
- a play-like triangle is visually offset inside a fixed control box;
- a popover is given closed contour/overlap cues consistent with independent interaction scope.

## KEEP

- The exercise demonstrates cross-context transfer rather than leaving the work at abstract perceptual shapes.
- Interaction ownership is acknowledged: popover geometry should match its independent action/state scope.
- The icon’s visual child and hit geometry are conceptually separated, which is important for target accessibility.

## REWORK

The UI fragment still needs a running implementation to validate:

- actual hit boxes;
- focus ring geometry;
- keyboard navigation;
- opening/closing state;
- escape/dismissal behavior;
- text expansion;
- native/browser rendering;
- focus and border interaction when the popover overlaps adjacent content.

## REJECT

Reject the assumption that a strong outline automatically solves popover figure–ground. Real surfaces may use material, elevation, dimming, motion, and spatial separation; the correct combination must fit platform and product context.

---

# Cross-context transfer critique

## Dense data

The L001 method transfers well only if optical corrections do not disrupt shared baselines and scan structure. In dense tables, geometric consistency can matter more than individual icon “beauty.” Any correction must therefore be evaluated inside the row/column system, not in isolation.

## Low-density controls

Optical correction has more room to matter because a single large control can carry substantial visual mass. The fixed-hit-box / moved-visual-child pattern is particularly useful here.

## Editorial / expressive layouts

The method should diagnose rather than neutralize tension. An editorial composition may intentionally use asymmetry and edge pressure. The critique question is whether the tension is authored and reproducible, not whether everything is centered.

---

# KEEP / REWORK / REJECT summary

## KEEP

- distinguish border geometry from ownership perception;
- use geometric centroids as baselines, not perceptual truth;
- replace vague “tension” language with a causal hypothesis;
- declare the centering reference before optical correction;
- compare symmetrical offset candidates;
- preserve target/semantic bounds while adjusting a visual child when appropriate;
- transfer abstract exercises into realistic UI fragments;
- label static self-critique as lower-grade evidence than human/rendered validation.

## REWORK

- exact centroid calculations printed in the artifact;
- parametric edge-distance series;
- cue-isolated border-ownership variants;
- blinded reviewer comparisons;
- intended-size raster proofs;
- real browser/native rendering;
- multilingual/RTL transfer;
- focus/keyboard/state validation for layered UI.

## REJECT

- “designer eye” as sole proof;
- balance = symmetry;
- center = bounding-box center in every case;
- universal optical-offset tokens;
- fake perceptual formulas with unvalidated weights;
- using shadows/cards/borders as universal ownership recipes;
- treating static layout proof as interaction proof.

---

# Gate result

**Result: three Foundation modules materially advanced; no PASS.**

Recommended status changes:

- `Figure-ground / border ownership`: `IN STUDY NEXT` → `PRACTICE / CRITIQUE`
- `Visual mass / balance / tension`: `NOT YET ESTABLISHED` → `PRACTICE / CRITIQUE`
- `Optical centering`: `NOT YET ESTABLISHED` → `PRACTICE / CRITIQUE`

Why no PASS:

- no blinded human comparison;
- no exact controlled balance dataset;
- no actual-size raster/device proof;
- no multilingual/RTL transfer;
- no repeated failure → revision → re-test cycle.

The work closes a conceptual Foundation gap and supplies a reusable critique method, but it does not yet satisfy the curriculum’s demonstration standard across contexts.
