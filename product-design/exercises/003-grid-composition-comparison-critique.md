# Exercise 003 Critique — Grid / Composition Comparison

Status: PRACTICE / SELECTED DIRECTION FOR FURTHER TESTING

Related specimen:
- `product-design/exercises/003-grid-composition-comparison.svg`

Research basis:
- `research/006-grid-composition-hierarchy.md`

## Intent

Use identical content to separate the effects of:

- symmetry;
- repeated modules;
- shared datums;
- asymmetric hierarchy;
- one controlled grid break.

This is not a visual-language proposal for a product.

## A — symmetric modular grid

### KEEP

- Strong repeatability.
- Easy to understand the underlying module.
- Useful as a control because support metrics can be compared cleanly.

### REWORK

- Equal module treatment gives four support facts too much parity with the dominant total.
- The composition is orderly but weaker at answering "what matters first?"
- Symmetry here is an organizational default rather than a semantic necessity.

### Lesson

A grid can improve neatness while still weakening hierarchy.

## B — asymmetric hierarchy on shared datums

### KEEP

- Strongest first read: the large total is unambiguous.
- Secondary metrics still share alignment, allowing fast comparison.
- Latest record and index use the same datum family without becoming equal-sized containers.
- Asymmetry is content-driven rather than decorative.

### Risk

- At narrow widths, the three support facts may need a different responsive composition rather than simple compression.

### Disposition

**KEEP as the strongest foundation hypothesis.**

This does not mean asymmetric layouts are generally superior. It means the information hierarchy in this specific exercise is asymmetric.

## C — controlled grid break

### KEEP

- Demonstrates that a dominant element may span beyond the base module while surrounding content preserves order.
- The break remains legible because there is only one major interruption.

### REWORK

- The filled background used to reveal the spanning region risks becoming a decorative crutch.
- A stronger next test should remove the fill and ask whether scale/space alone can justify the break.
- The break must be retested at a narrow format. If it collapses into ordinary full-width content, its value may be low.

### Lesson

A grid break only has meaning when the rest of the system is sufficiently stable for the exception to register.

## Comparison result

The exercise supports three distinct findings:

1. **Order is not hierarchy.** A symmetrical grid can be tidy but still distribute emphasis poorly.
2. **Asymmetry can remain highly systematic.** B uses fewer visible boxes than A while preserving more useful semantic alignment.
3. **Exceptions require scarcity.** C works only because the spanning move is rare and structurally anchored.

## What the exercise does not prove

- responsive behavior;
- large-text behavior;
- multilingual expansion;
- touch-target behavior;
- color/luminance hierarchy;
- that B is a reusable house style;
- that grid-breaking is inherently premium or expressive.

## Required next proof before PASS

1. recompose B for a narrow/mobile frame without scaling;
2. remove the visible fill from C and test whether the break still works;
3. repeat the exercise using a second unrelated information set, such as a form or editorial article;
4. test large type and long labels;
5. document which alignments are semantic and which are disposable at a breakpoint.

## Status implication

This is sufficient to move:

- `Composition / visual grammar` → **PRACTICE**;
- `Grid / alignment systems` → **PRACTICE**.

Neither is ready for PASS.