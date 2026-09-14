# Study 013 — Perceptual Grouping as Spatial Grammar

Status: FOUNDATION STUDY / paired original exercise and critique included separately.

## Question

How should a layout use distance, containment, connection, alignment, and whitespace to communicate relationships without turning Gestalt principles into a decorative checklist?

## Scope

This study extends `research/006-grid-composition-hierarchy.md`. Study 006 establishes grid and alignment as relationship systems. This study moves one level earlier: **before a grid can organize a screen, the visual system must decide what belongs together, what is separate, and which regions form perceptual units.**

This is a Layout & Spatial Design foundation module. It does not prescribe a universal spacing scale or a house style.

---

## SOURCE — contemporary Gestalt research is broader than the familiar classroom list

Wagemans et al. review a century of research on perceptual grouping and figure-ground organization. The review covers classical grouping factors such as proximity, similarity, common fate, good continuation, closure, symmetry, and parallelism, as well as later factors such as common region and uniform connectedness. It also emphasizes that modern work has quantified and revised several early Gestalt ideas rather than treating the original laws as finished doctrine.

Sources:
- https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/
- https://pubmed.ncbi.nlm.nih.gov/22845751/
- DOI: 10.1037/a0029333

### SYNTHESIS

A professional interface designer should not use “Gestalt laws” as isolated slogans. The relevant design problem is **cue competition and cue cooperation**:

- distance may suggest one grouping;
- similarity may suggest another;
- a containing region may override both;
- physical connection may cause elements to be perceived as one unit;
- figure-ground assignment determines which region appears to own a boundary.

A layout therefore needs a coherent *grouping hypothesis*, not merely attractive spacing.

---

## SOURCE — proximity has measurable strength, but not a universal pixel threshold

Kubovy, Holcombe, and Wagemans quantitatively studied grouping by proximity in dot lattices. Their results show that the relative strength of a grouping organization falls approximately as a decreasing exponential function of relative inter-element distance. The effect was robust across the spatial-scale manipulations reported in the study.

Sources:
- https://pubmed.ncbi.nlm.nih.gov/9520318/
- https://www.sciencedirect.com/science/article/pii/S0010028597906733
- DOI: 10.1006/cogp.1997.0673

Earlier quantitative work by Kubovy and Wagemans likewise modeled proximity grouping probabilistically rather than as an all-or-nothing rule.

Source:
- https://journals.sagepub.com/doi/10.1111/j.1467-9280.1995.tb00597.x
- DOI: 10.1111/j.1467-9280.1995.tb00597.x

### SYNTHESIS

The transferable lesson is relational:

> Spatial grouping strength depends on the relationship among distances, not on a magic spacing token.

This does **not** mean the dot-lattice equations can be copied directly into UI spacing specifications. The experimental stimuli and interface tasks are different. The justified transfer is narrower: a designer should reason about **intra-group separation versus competing inter-group separation**, then validate the result in the product context.

### STUDIO JUDGMENT

Spacing tokens are implementation tools. They are not perceptual laws.

When a spacing system uses only a small token vocabulary, the designer still needs to ask whether the selected token creates a sufficiently clear relational difference in the actual composition. A nominally consistent 8/16/24 system can still create ambiguous grouping if neighboring structures compete.

---

## SOURCE — common region is an independent and powerful grouping cue

Palmer proposed **common region** as a grouping principle: elements located inside the same bounded region tend to be perceived together. In the reported demonstrations, common region could overcome other strong factors including proximity and similarity, and it could participate in hierarchical embedding.

Sources:
- https://pubmed.ncbi.nlm.nih.gov/1516361/
- https://www.sciencedirect.com/science/article/pii/001002859290014S
- DOI: 10.1016/0010-0285(92)90014-S

### SYNTHESIS

A card, panel, tinted surface, outline, or other enclosure is not neutral decoration. It adds a **containment claim**: “these elements belong to this region.”

This explains a recurring interface failure: adding cards around every local cluster can create too many perceptual objects, causing the user to read the page as a field of containers rather than as an information hierarchy.

### STUDIO JUDGMENT

Use a region when the boundary communicates something spacing alone cannot communicate reliably, for example:

- object ownership;
- a local interaction scope;
- a meaningful status surface;
- a nested sub-context;
- a persistent comparison unit.

Do not add a region merely because an item needs visual polish.

---

## SOURCE — uniform connectedness can establish perceptual units before later grouping

Palmer and Rock described **uniform connectedness** as a principle in which connected regions of homogeneous or smoothly changing properties tend to form initial perceptual units. Later review literature treats uniform connectedness as an important contribution to the problem of how entry-level elements themselves are formed before higher-order grouping.

Sources:
- https://pubmed.ncbi.nlm.nih.gov/24203413/
- DOI: 10.3758/BF03200760
- review discussion: https://pmc.ncbi.nlm.nih.gov/articles/PMC3482144/

### SYNTHESIS

Connection is stronger than casual adjacency because it can change the perceived object structure.

Interface examples include:

- segmented controls;
- connected timelines;
- input + attached unit/suffix treatment;
- joined toolbar clusters;
- graph nodes connected by edges.

The designer must decide whether connection means “one control with alternatives,” “multiple controls in one cluster,” or “objects related by a path.” A line or shared surface can accidentally imply stronger semantic unity than intended.

---

## SOURCE — platform guidance independently converges on relational grouping

Apple’s current Human Interface Guidelines recommend grouping related items and identify negative space, background shapes, color/material, and separators as possible means. The guidance also recommends giving important information sufficient space, aligning components to support scanning and hierarchy, and leaving enough space around controls so unrelated items do not become difficult to distinguish.

Source:
- https://developer.apple.com/design/human-interface-guidelines/layout

### SYNTHESIS

Platform guidance supports the same broad direction as perceptual research: layout communicates through **relative grouping, separation, alignment, and region structure**.

However, Apple HIG is platform guidance rather than a universal theory of perception. It is evidence for Apple-platform practice and a useful convergence point, not the source of the underlying perceptual claims.

---

## SOURCE — visual relationships must survive alternative presentation and reflow

WCAG 2.2 requires information, structure, and relationships conveyed through presentation to be programmatically determinable or available in text (1.3.1), requires a meaningful sequence when sequence affects meaning (1.3.2), and requires reflow without loss of information or functionality in the specified conditions (1.4.10), subject to documented exceptions.

Source:
- https://www.w3.org/TR/WCAG22/

### SYNTHESIS

A visual grouping cannot be considered structurally successful if its meaning disappears when:

- the layout reflows;
- text enlarges;
- the reading order changes for another language;
- assistive technology consumes the semantic structure rather than the pixels.

This creates an important distinction:

**visual grouping** = what appears related on the rendered surface;

**semantic grouping** = what the product structure says is related.

Professional layout requires the two to agree.

---

# Spatial grammar derived from the evidence

## 1. Group before aligning

Alignment is useful only after the designer knows which items constitute a perceptual and semantic group. Aligning unrelated items too strongly can create a false relationship.

## 2. Treat distance as a ratio inside a local field

Do not ask only, “Is this gap 16 px?” Ask:

- How does this gap compare with the gaps inside the intended group?
- How does it compare with the nearest competing group?
- Does the grouping survive a wider/narrower viewport?
- Does text expansion consume the intended separation?

## 3. Treat containment as a strong assertion

A visible container creates a region and therefore increases grouping pressure. Use it when the region has semantic value. Prefer spacing/alignment when a boundary would add unnecessary object structure.

## 4. Treat connection as object formation

Joining elements visually can make them read as one object or one mechanism. Do not connect controls merely to save space.

## 5. Design nested hierarchy deliberately

Perceptual grouping can be hierarchical. A screen may contain:

- page;
- section;
- object;
- field cluster;
- label/value pair.

Each level should not receive an equally strong boundary. If every level is boxed, hierarchy collapses into repeated containers.

## 6. Use redundant cues when failure cost is high, but avoid visual overstatement

Important relationships can use more than one cue — for example proximity + alignment, or spacing + heading. But stacking every cue (box + divider + tint + shadow + indentation + large gap) can make a minor grouping appear more important than it is.

## 7. Test cue conflict, not only the ideal state

A layout should be deliberately stressed by creating conflicts:

- proximity versus containment;
- similarity versus alignment;
- dense data versus generous whitespace;
- long text versus original spacing;
- visual order versus semantic/keyboard order.

If the wrong cue wins, the spatial grammar is unstable.

---

# Failure modes

- identical vertical gaps between label/value pairs and between unrelated sections;
- a card around every item, producing container noise;
- borders used where whitespace already communicates the grouping;
- strong alignment across semantically unrelated columns;
- a connected visual treatment applied to controls that act independently;
- decorative dividers that split a true semantic group;
- reflow that preserves component widths but destroys relationship order;
- mobile layouts that simply stack desktop columns without reconsidering grouping;
- arbitrary “8-point-grid compliance” cited as proof of perceptual quality;
- using Gestalt terminology after the fact to rationalize a composition that was never tested.

---

# Practice gate for this study

The paired Exercise 013 must demonstrate:

1. proximity as a controllable grouping cue;
2. a deliberate conflict in which common region competes with proximity;
3. connectedness changing the perceived unit structure;
4. a realistic UI grouping using intra-group and inter-group separation;
5. one over-containerized failure;
6. grayscale operation so color does not rescue weak spatial structure;
7. critique that distinguishes observed geometry from untested perceptual claims.

This block strengthens `Composition / visual grammar`; it does **not** by itself justify `PASS`. Human viewing, multilingual/enlarged-text stress, and rendered-device validation remain open.

---

# OPEN

1. Establish a repeatable method for measuring perceived grouping in realistic interface fragments rather than relying only on designer inspection.
2. Study figure-ground assignment more deeply, including border ownership and how elevation/material cues alter ownership.
3. Study visual mass, balance, and optical centering separately; they are related to spatial composition but not reducible to grouping.
4. Validate spatial grouping under CJK/Latin mixed scripts and RTL layouts.
5. Test whether the same grouping survives large-text/reflow conditions in an actual browser/app rendering environment.
