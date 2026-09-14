# Study 005 — Numerals and Punctuation as Systems

Status: FOUNDATION STUDY / drawing practice still required before PASS.

## Question

What changes when numerals and punctuation are designed as a coordinated text-and-data system rather than as isolated decorative glyphs?

## SOURCE — figure style is multi-dimensional, not one default truth

OpenType defines separate features for lining figures (`lnum`), oldstyle figures (`onum`), proportional figures (`pnum`), and tabular figures (`tnum`). These are independent typographic dimensions rather than one linear quality ladder.

Microsoft OpenType feature registry:
- https://learn.microsoft.com/en-us/typography/opentype/spec/featurelist
- https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt

Glyphs' figure-set documentation likewise treats proportional/tabular and lining/oldstyle as combinable systems. It also makes clear that a font can choose any one set as its default and provide the others as alternates.

Source:
- https://glyphsapp.com/learn/figure-sets

### Studio consequence

Do not say "tabular is better" or "proportional is more elegant" in the abstract.

Choose by task:

- changing values in aligned columns often benefit from tabular widths;
- running prose usually benefits from proportional rhythm;
- lining vs oldstyle is a vertical/text-color decision, not a data-accuracy decision;
- a product may need multiple figure behaviors inside one typographic system.

## SOURCE — tabular width is a metric contract, not a contour recipe

The OpenType `tnum` feature substitutes proportional figures with tabular forms. The important behavior is equalized advance width for alignment.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/features_pt

### Studio synthesis

Equal advance width does **not** mean:

- equal visible contour width;
- equal left/right sidebearing;
- geometric centering of every digit;
- identical counter area;
- permission to stretch narrow figures until they fill the cell.

A tabular system still needs optical distribution inside each fixed cell.

The narrow `1`, broad `0/8`, open `4`, and asymmetric `2/5` must remain recognizably themselves while the advances align.

## SOURCE — slashed zero is an alternate, not a universal default

OpenType registers the `zero` feature as **Slashed Zero**. Its function is to replace the lining zero with a slashed alternate when `0/O` ambiguity matters. Microsoft notes that this feature is discretionary and is generally expected to be off by default.

Source:
- https://learn.microsoft.com/en-us/typography/opentype/spec/features_uz

### Studio consequence

The existence of an OpenType `zero` feature proves two useful things:

1. `0/O` ambiguity is a legitimate functional problem;
2. a slash is one established solution, but it does not have to be the permanent default form.

For product-specific data typography, the correct decision must come from actual ambiguity, size, density, and aesthetic tests — not from ideology for or against slashed zero.

## Punctuation is not leftover geometry

A data-oriented type system often fails first in punctuation rather than digits.

Critical cases include:

- colon in `23:59`;
- plus in `1+05` and `99,999+59`;
- comma in long cumulative values;
- period for decimals/versioning;
- slash in dates, ratios, or alternate notations;
- hyphen/minus distinction where mathematics and identifiers coexist.

### Optical questions

For each mark, test:

- vertical optical center relative to figures;
- apparent weight against the numeral stroke;
- sidebearing/advance behavior;
- whether the mark disappears at compact size;
- whether it becomes too loud at display size;
- whether semantic distinction survives (`-` vs `−`, `/` vs a slash inside zero, colon vs two tiny dots).

A mathematically centered plus or colon can still appear visually low/high because the surrounding digits do not distribute mass symmetrically.

## Ambiguity should be solved as a family

The high-risk set for dense Latin/data UI includes:

- `0 / O`
- `1 / I / l`
- `5 / S`
- `8 / B`

Do not solve each pair with unrelated novelty marks. The family should use compatible strategies such as:

- proportion;
- aperture/counter shape;
- terminal structure;
- stem presence;
- width;
- optional alternate features when necessary.

A solution is weak if each ambiguity pair looks borrowed from a different genre.

## Foundation proof strings

The next numeral exercise must include, at minimum:

`00112233445566778899`

`010101 808080 111888`

`0O 1I 5S 8B`

`23:59`

`1+05 12+40 999+59 99,999+59`

`-12.5 / 12-34`

These strings test different failure modes: repeated rhythm, ambiguous forms, punctuation scale, and width stress.

## Four independent tests

### 1. Contour test
Can each figure be identified in isolation without gimmick dependence?

### 2. Cell test
If figures are tabular, does each contour sit optically inside a common advance rather than merely mathematically centered?

### 3. Sequence test
Do repeated figures and mixed strings create stable color and rhythm?

### 4. Semantic punctuation test
Do marks remain subordinate but unmistakable in their actual use contexts?

## Transfer to UI design

The lesson generalizes beyond fonts:

- alignment contracts and visual shape are separate layers;
- equal layout cells do not require identical internal geometry;
- an alternate behavior may be context-specific rather than globally default;
- small separators and operators can control comprehension disproportionately;
- ambiguity should be solved systematically, not through isolated decorative fixes.

## Practice required before PASS

1. draw a complete native `0–9` set under one explicit construction model;
2. produce both proportional and tabular metric proofs without changing the basic identity arbitrarily;
3. design at least `: + , . / -` as a coordinated punctuation subset;
4. compare default zero vs slashed/internal-mark alternatives in identical contexts;
5. raster-test compact, normal, and display sizes;
6. record at least one redraw triggered by sequence/raster evidence;
7. prove that ambiguity improvements do not make the family feel like unrelated borrowed glyph solutions.

Until then, `Numerals / punctuation` is source-grounded but not complete.