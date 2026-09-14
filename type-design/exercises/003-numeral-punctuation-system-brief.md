# Exercise 003 — Numeral / Punctuation System Brief

Status: PRACTICE BRIEF / DRAWING NOT YET COMPLETE

Research basis:
- `research/005-numerals-punctuation-systems.md`

## Objective

Design and evaluate a numeral/punctuation system without using an existing typeface as a drawing source and without deciding a product-specific visual style.

The exercise is intentionally about **system behavior** before beauty or brand expression.

## Construction constraint

Choose one explicit construction hypothesis and state it before drawing:

- low-contrast constructed;
- writing-derived expansion;
- hybrid optical construction.

Do not mix the `0` from one hypothesis, `1` from another, and punctuation from a third simply because individual forms look attractive.

## Phase A — default proportional figures

Draw native `0–9`.

Evaluate:

- common apparent height;
- common apparent weight;
- counter openness;
- curve/straight transitions;
- family relationship across `2/3/5`, `6/9`, `0/8`;
- spacing in `00112233445566778899`.

No kerning may be added during this phase.

## Phase B — tabular metric conversion

Create a fixed-advance version while preserving the figure identity.

Forbidden shortcut:
- horizontally stretch/compress contours merely to fill the common cell.

Instead adjust:
- sidebearings;
- optical centering;
- only where justified, small contour compensation.

Required proof:

`0000 1111 2222 8888`

`0123456789`

`101010 808080`

The visual centers should feel stable even when the contours have different widths.

## Phase C — punctuation subset

Draw and space:

`: + , . / -`

Required contexts:

`23:59`

`1+05`

`12+40`

`99,999+59`

`-12.5`

`12/34`

The punctuation may not be judged only in isolation.

## Phase D — ambiguity alternatives

Produce three zero strategies against the *same* surrounding system:

A. unmarked zero distinguished by proportion/counter

B. slashed zero alternate

C. restrained internal mark/datum alternate

Evaluate all three in:

`0O 00 OO O0 8080`

and in long mixed strings.

Do not assume A, B, or C is superior before raster testing.

## Phase E — optical-size proof

Render the same strings at three roles:

- compact data size;
- normal UI/data size;
- large display/readout size.

Classify each failure as one of:

- contour/construction;
- spacing;
- optical compensation;
- ambiguity;
- punctuation scale/position;
- rasterization.

At least one failure must trigger a redraw and a second proof.

## Evaluation matrix

| Question | Evidence required |
| --- | --- |
| Is the family coherent? | full `0–9` line and mixed punctuation strings |
| Are tabular figures truly usable? | fixed advances + optically stable cells |
| Is `0/O` distinction sufficient? | mixed ambiguity strings at compact size |
| Is punctuation subordinate but clear? | `23:59`, `99,999+59`, decimals/slashes |
| Does beauty survive function? | display proof without losing small-size legibility |
| Does function survive beauty? | compact proof without military/OCR/code-font drift |

## Current critique

No visual result exists yet, therefore no aesthetic conclusion is permitted.

**KEEP**
- The exercise separates proportional, tabular, punctuation, and ambiguity questions.
- The zero strategy is explicitly comparative rather than ideological.

**REWORK required next**
- Produce native outlines.
- Produce target-size raster evidence.
- Record a failure/redraw cycle.

**REJECT**
- Declaring a slashed or unmarked zero mandatory before evidence.
- Borrowing recognizable figure solutions from multiple existing families.
- Evaluating only isolated giant numerals.

This brief advances the topic from `NOT STARTED` to `IN STUDY`; it does not justify `PRACTICE` until actual drawing evidence exists.