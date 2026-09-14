# Study L001 — Figure–Ground, Visual Balance, Tension, and Optical Centering

Status: FOUNDATION STUDY / paired original exercise and critique included separately.

## Question

How should a product designer reason about figure–ground assignment, border ownership, visual mass, balance, compositional tension, and optical centering without reducing them to decorative rules or unsupported “designer eye” claims?

## Scope

This study advances three adjacent unfinished Foundation items in `curriculum/MASTER_CURRICULUM.md`:

1. figure–ground / border ownership;
2. visual mass / balance / tension;
3. optical centering.

It extends `research/layout/014-perceptual-grouping-spatial-grammar.md`, which established grouping, common region, connectedness, and cue conflict. L001 focuses on a different question: once regions and objects exist, **which side appears to own a contour, how does a composition distribute perceptual weight, and when does geometric centering fail to predict perceived centering?**

This is not a universal style guide. It defines a reusable method for diagnosing spatial composition.

---

## RELATED DOMAIN CHECK

### Type evidence checked

- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/009-typography-as-information-architecture.md`

Useful transfer: typography already distinguishes measurable geometry from optical judgment and treats alignment/hierarchy as relational rather than purely coordinate-driven. L001 reuses that distinction for non-text spatial composition. It does not duplicate Type’s glyph-specific optical correction work.

### Color evidence checked

- `research/color/008-color-luminance-contrast-hierarchy.md`

Useful transfer: luminance can alter salience and apparent weight, but L001 deliberately begins in grayscale and does not infer perceptual mass from luminance alone. Color remains a future transfer variable rather than a hidden rescue cue.

### Layout / Interaction evidence checked

- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/014-perceptual-grouping-spatial-grammar.md`

Study 014 already identifies border ownership as an open gap and warns that region cues can compete with proximity. L001 directly extends that gap instead of re-summarizing grouping laws.

### Additional cross-cutting evidence checked

- `research/004-accessibility-reflow-targets-focus.md`

Transfer: optical adjustment must not change hit targets, semantic order, focus geometry, or reflow behavior in ways that undermine accessibility.

### Overlap classification

`EXTENSION + METHOD COMPARISON` — the work extends grouping into figure–ground and compares geometric balance measures with perceptual judgments rather than treating either as sufficient.

### Dependencies / handoffs created

- Type: optical-centering protocol may transfer to icons paired with labels and glyph-like symbols.
- Color: later work should test whether luminance/chroma systematically shifts perceived mass in realistic UI fragments.
- Interaction: layering and border ownership must agree with interaction ownership (popover, sheet, selected region, drag target, etc.).

---

# Part I — Figure–ground and border ownership

## SOURCE — border ownership is represented as a side-of-figure signal

Zhou, Friedman, and von der Heydt recorded neurons in macaque visual cortex and found many cells, especially in V2, whose responses to an edge depended on which side of that edge belonged to the figure. The response depended on image context extending beyond the classical receptive field.

Primary source:
- Zhou H, Friedman HS, von der Heydt R. *Coding of border ownership in monkey visual cortex*. Journal of Neuroscience. 2000;20(17):6594–6611. DOI: 10.1523/JNEUROSCI.20-17-06594.2000
- https://pubmed.ncbi.nlm.nih.gov/10964965/

Qiu and von der Heydt later reported that V2 neurons combine stereoscopic depth information with global contour configuration: local depth order and Gestalt-style configuration can reinforce or oppose one another in the same neural response.

Primary source:
- Qiu FT, von der Heydt R. *Figure and ground in the visual cortex: V2 combines stereoscopic cues with Gestalt rules*. Neuron. 2005;47(1):155–166. DOI: 10.1016/j.neuron.2005.05.028
- https://pubmed.ncbi.nlm.nih.gov/15996555/

### SYNTHESIS

A contour is not merely a line separating two regions. Perception tends to assign the contour to one side as the boundary of a figure. The assignment depends on broader context, not only the local stroke.

For interface work, the justified transfer is not “V2 tells us how to draw cards.” The transfer is narrower:

> When two surfaces share a boundary, the designer must decide which surface is meant to be the perceptual object and ensure surrounding cues support that ownership.

This matters for:

- popovers over underlying content;
- sheets and drawers;
- selected rows inside tables;
- nested cards;
- sticky headers crossing content;
- drag-and-drop targets;
- comparison panels sharing separators.

## SOURCE — figure assignment is cue-dependent and contextual

Peterson and Salvagio experimentally examined convexity as a figure cue. Convexity bias was weak for a single edge but became stronger with contextual repetition under specific region-homogeneity conditions, supporting a competitive/contextual account rather than a single universal “convex = figure” rule.

Primary source:
- Peterson MA, Salvagio E. *Inhibitory competition in figure-ground perception: context and convexity*. Journal of Vision. 2008;8(16):4. DOI: 10.1167/8.16.4
- https://pubmed.ncbi.nlm.nih.gov/19146271/

Stevens and Brookes showed that local concave-cusp geometry can influence figure–ground assignment, again demonstrating that boundary configuration can matter independently of a simple region label.

Primary source:
- Stevens KA, Brookes A. *The concave cusp as a determiner of figure-ground*. Perception. 1988;17(1):35–42. DOI: 10.1068/p170035
- https://pubmed.ncbi.nlm.nih.gov/3205668/

### STUDIO JUDGMENT

Do not teach figure–ground as a checklist of “smaller, convex, enclosed, higher contrast = figure.” Treat those as potentially cooperating or competing cues.

The reusable diagnostic is:

1. identify the intended foreground object;
2. identify every cue that could claim the shared boundary;
3. create a conflict variant where one cue is reversed;
4. verify whether the intended ownership survives;
5. if ownership matters to task interpretation, test with people rather than relying only on designer inspection.

### Failure modes

- divider lines that appear to belong to the wrong row;
- a selected surface whose border visually merges with its parent card;
- modal/popup elevation that is too weak to establish an independent object;
- nested containers where each boundary makes an equally strong ownership claim;
- background panels with stronger edge closure than the foreground controls they contain.

---

# Part II — Visual mass and balance

## SOURCE — perceived balance is holistic and not reducible to one physical feature

Locher, Smets, and Overbeeke asked design-trained participants to classify three-dimensional forms by perceived balance under visual and haptic conditions. A balance dimension emerged when participants attended globally to the structure, and the authors concluded that visual balance was a holistic property derived from a synthesis of stimulus information.

Primary source:
- Locher P, Smets G, Overbeeke K. *The contribution of stimulus attributes of three-dimensional solid forms and level of discrimination to the visual and haptic percept of balance*. Perception. 1995;24(6):647–663. DOI: 10.1068/p240647
- https://pubmed.ncbi.nlm.nih.gov/7478905/

Hübner and colleagues compared computational balance measures with human balance and preference ratings. A deviation-of-center-of-mass measure predicted balance ratings better than one alternative balance measure, while aesthetic preference depended on additional properties such as homogeneity. The key implication is that **balance and liking are not the same variable**.

Primary source:
- Hübner R, Fillinger MG. *Comparison of Objective Measures for Predicting Perceptual Balance and Visual Aesthetic Preference*. Frontiers in Psychology. 2016. PMID: 27014143.
- https://pubmed.ncbi.nlm.nih.gov/27014143/

Gershoni and Hochstein tested pictorial balance in Japanese calligraphy and found that a symmetry-axis mechanical-weight model correlated poorly with first-fixation balance judgments compared with the richer pattern of human ratings. Their interpretation emphasizes global organization, grouping, object recognition, orientation structure, closure, and completion.

Primary source:
- Gershoni S, Hochstein S. *Measuring pictorial balance perception at first glance using Japanese calligraphy*. i-Perception. 2011;2(6):508–527. DOI: 10.1068/i0472aap
- https://pubmed.ncbi.nlm.nih.gov/23145242/

### SYNTHESIS

A useful engineering-style balance calculation can detect some compositional asymmetries, but it is not a perceptual oracle.

For a flat composition, an area-weighted centroid can be computed as:

`Cx = Σ(Ai × xi) / ΣAi`

`Cy = Σ(Ai × yi) / ΣAi`

where `Ai` is the area (or another explicitly chosen weight proxy) and `(xi, yi)` is each element’s centroid.

This is useful as a **diagnostic baseline** because it makes geometry inspectable. It must be labeled correctly:

- measured: the chosen proxy’s centroid;
- inferred: perceived visual mass;
- unknown until tested: whether viewers judge the composition as balanced.

### STUDIO JUDGMENT — visual mass ledger

For interface critique, use a “mass ledger” before making an optical correction. Record candidate contributors separately:

- occupied area;
- luminance contrast against background;
- edge density / internal detail;
- typographic density;
- isolation (large surrounding whitespace can make a small object salient);
- position relative to frame edges/center;
- repetition and grouping;
- semantic salience (e.g. destructive action, alert badge, primary value).

Do **not** collapse these into a fake universal numeric formula unless the weights have been empirically validated for the context.

## Balance is not symmetry

The empirical literature supports a preference for symmetry in many stimulus classes, but symmetry is neither universally preferred nor equivalent to perceptual balance. Different categories and tasks change the result.

Relevant primary evidence:
- Bertamini M et al. *Symmetry preference in shapes, faces, flowers and landscapes*. PeerJ. 2019;7:e7078. DOI: 10.7717/peerj.7078
- https://pubmed.ncbi.nlm.nih.gov/31245176/

The study found a general preference for symmetry in shapes and faces, but not in landscapes, where natural non-perfectly-symmetric images were preferred. This is a useful warning against making symmetry a universal quality rule.

### STUDIO JUDGMENT

For product layouts, “balanced” means the composition’s competing visual forces do not unintentionally pull attention away from the intended hierarchy. An intentionally asymmetric composition can be well balanced if the asymmetry serves task structure.

---

# Part III — Compositional tension

“Tension” is used loosely in design discourse, so this study operationalizes it instead of treating it as a mystical visual property.

## SOURCE — conflicting depth cues can create perceived tension

Pratt discussed paintings/drawings in which incompatible depth cues produced ambiguity and described the resulting experience as visual tension. The paper is useful mainly because it connects tension to **cue conflict**, not because it provides a universal UI metric.

Source:
- Pratt F. *The contribution of colour to three-dimensional ambiguities in paintings and drawings*. Perception. 1979;8(2):157–173. DOI: 10.1068/p080157
- https://pubmed.ncbi.nlm.nih.gov/471680/

## SOURCE — framing preference depends on object meaning and “affordance space”

Palmer, Gardner, and Wickens experimentally studied preferred vertical framing of single objects. Preferred placement depended on object orientation and typical relation to the observer; the authors proposed that people preferred the object’s “affordance space” to be centered in the frame.

Primary source:
- Palmer SE, Gardner JS, Wickens TD. *Aesthetic issues in spatial composition: effects of vertical position and perspective on framing single objects*. Journal of Experimental Psychology: Human Perception and Performance. 2012;38(4):865–884. DOI: 10.1037/a0027736
- https://pubmed.ncbi.nlm.nih.gov/22428674/

### SYNTHESIS

Useful compositional “tension” is better treated as an observable **conflict or directional pull** created by relationships such as:

- insufficient clearance to a frame edge;
- directional content pointing into a blocked or empty area;
- figure/ground cues disagreeing about ownership;
- visual mass concentrated away from intended hierarchy;
- a strong diagonal or directional shape conflicting with alignment structure.

The designer should name the mechanism rather than merely saying “it feels tense.”

### STUDIO METHOD — tension diagnosis

When “tension” is reported in critique:

1. identify the claimed directional pull or cue conflict;
2. make a neutralized control version;
3. vary one causal factor at a time (edge distance, orientation, enclosure, contrast, mass distribution);
4. compare the versions at intended size;
5. if the design decision is consequential, collect forced-choice or rating evidence from multiple viewers.

---

# Part IV — Optical centering

## SOURCE — people can estimate centers of mass accurately, but systematic shape-dependent errors remain

Baud-Bovy and Soechting asked participants to identify the equilibrium point of asymmetric 2D shapes. Participants were broadly accurate and consistent, yet their errors were systematic: judgments were influenced by shape, with a tendency toward the center of an inscribed circle rather than the true physical center of mass for the tested forms.

Primary source:
- Baud-Bovy G, Soechting JF. *Visual localization of the center of mass of compact, asymmetric, two-dimensional shapes*. Journal of Experimental Psychology: Human Perception and Performance. 2001;27(3):692–706. DOI: 10.1037/0096-1523.27.3.692
- https://pubmed.ncbi.nlm.nih.gov/11424655/

Firestone and Keil likewise found systematic biases in perceived balance/tipping points for shapes, reinforcing that physically correct balance and perceived balance can diverge.

Primary source:
- Firestone C, Keil FC. *Seeing the tipping point: Balance perception and visual shape*. Journal of Experimental Psychology: General. 2016;145(7):872–881. DOI: 10.1037/xge0000151
- https://pubmed.ncbi.nlm.nih.gov/27348290/

### SYNTHESIS

“Center” has multiple valid definitions:

- bounding-box center;
- area centroid;
- physical center of mass (for real objects);
- alignment center of a layout box;
- perceived or optical center.

They may coincide for simple symmetric shapes and diverge for asymmetric ones.

### STUDIO JUDGMENT — optical centering protocol

Optical centering is a **correction procedure**, not permission for arbitrary nudging.

Use this sequence:

1. **Start geometric.** Place the object at the declared geometric center (bounding-box or area centroid; record which).
2. **Inspect at intended size.** A correction visible only at 800% zoom is not automatically relevant at 16–24 px.
3. **Create symmetric alternatives.** Compare `0`, `+δ`, `−δ` rather than editing one direction until it “looks right.”
4. **Blind the comparison when feasible.** Randomize candidate order for reviewers.
5. **Preserve interaction geometry.** Keep hit target and semantic bounds stable while moving only the visual child when appropriate.
6. **Record the delta.** An optical offset is a design token or component parameter only when its use case is defined.
7. **Re-test across contexts.** A correction for a standalone icon may fail next to text, inside a dense toolbar, or in RTL mirroring.
8. **Do not universalize the delta.** Different shapes require different corrections.

### Common UI cases

- play triangle inside a circular button;
- chevron inside a square hit target;
- asymmetric logo mark inside a top bar;
- icon + label pairs with unequal visual density;
- badges attached to an icon corner;
- numerals or symbols with asymmetric side bearings.

### Failure modes

- centering an asymmetric glyph by bounding box and assuming the problem is solved;
- applying a “1 px optical nudge” to every icon family;
- changing the touch target together with the visual offset;
- judging at design-tool zoom rather than intended physical/rendered size;
- compensating for a poor source asset with offsets instead of fixing the asset;
- using optical correction to mask a broken grid or inconsistent padding system.

---

# Cross-context application rules

## Context A — dense data interface

- use borders only when ownership or comparison scope needs explicit separation;
- compare measured geometric balance with task hierarchy rather than seeking symmetry;
- optical corrections should be subordinate to scan alignment and numeric comparability;
- edge tension caused by dense clipping or near-touching separators is usually a spacing/reflow issue, not a reason to add decoration.

## Context B — low-density command surface

- a single primary control may carry disproportionate visual mass intentionally;
- asymmetric icons may need optical correction inside larger hit targets;
- a popover or modal must establish independent figure ownership without relying on shadow alone;
- directional controls need enough “affordance space” that their orientation does not feel blocked by the frame.

## Context C — editorial / promotional composition

- balance may be intentionally dynamic rather than neutral;
- edge pressure, asymmetry, and diagonal structure can be expressive;
- the same methods still apply: identify which cue creates the effect and distinguish intentional tension from accidental hierarchy failure.

---

# Practice gate for L001

The paired exercise must include:

1. an ambiguous shared border and at least two variants that change ownership cues;
2. a measured geometric-mass comparison where the centroid is explicitly calculated or held constant;
3. a deliberate off-balance/tension variant with the causal change isolated;
4. an asymmetric symbol shown with bounding-box center, area-centroid center, and a labeled optical-candidate offset;
5. at least one realistic UI fragment applying the method;
6. grayscale construction so hue cannot rescue hierarchy;
7. critique that separates measurement, perception hypothesis, and actual evidence.

This work can advance the three modules to `PRACTICE / CRITIQUE`, but static artifact + self-critique alone do not justify Foundation PASS.

---

# OPEN

1. Run a small blinded human comparison of optical-centering candidates at intended sizes.
2. Test figure–ground ownership with realistic shadows/elevation and without them.
3. Validate visual-balance judgments with multiple observers rather than designer-only inspection.
4. Test whether luminance/chroma shifts perceived mass in the same composition using Color’s canonical evidence.
5. Test icon optical offsets next to short/long Latin, Korean, and RTL labels.
6. Verify whether corrections survive real browser/mobile rasterization and device pixel ratios.
7. Develop a repeatable critique sheet that records geometric centroid, optical candidate delta, intended hierarchy, and reviewer preference separately.

---

## HANDOFFS TO OTHER SPECIALISTS

### To Type

Use the geometric-vs-perceived-center distinction when evaluating asymmetric symbols, punctuation, icons paired with text, and glyph-like UI marks. Do not import spatial offsets into font metrics without Type-specific proof.

### To Color

L001 deliberately controls hue. A useful next Color transfer test is to hold geometry constant while varying luminance/chroma to measure whether balance or ownership judgments shift.

### To Interaction

For popovers, sheets, selected states, drag targets, and nested regions, visual border ownership should correspond to interaction ownership. If the visual figure does not match the state/action scope, treat it as a cross-domain defect.
