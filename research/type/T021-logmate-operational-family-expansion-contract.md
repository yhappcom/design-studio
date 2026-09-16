# T021 — LogMate Operational Family Expansion Contract

Status: **STAGE 2 PRACTICE — CONSTRUCTION / SPACING CONTRACT ESTABLISHED; BUILD + RASTER PROOF NEXT**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Purpose

The latest executed coverage audit showed that the current T021 mini-family covers only 6/33 distinct non-space characters in the bounded LogMate corpus. This note converts that blocker into one coherent construction and validation contract. It deliberately avoids opening kerning before enough base glyphs exist.

This is not a production font plan and not a claim that a custom LogMate font should ship. It is the shortest evidence path to compare a distinctive candidate against the proportional Roboto baseline and the exact airport-only `LogMateRobotoMono` interim control.

## RELATED DOMAIN CHECK

### Type
Reuses T021 H/O/n/o, A/V/T/L/I, the lowercase `n` redraw, shape-sensitive metric correction, pair-gap method validation, and the executed operational coverage audit. The mature-font validation withdrew the unsupported rule that an absolute AV scanline gap is itself a drawing defect.

### Layout / Interaction
Airport codes, registrations, flight numbers and duration totals are operational identifiers inside semantic columns. Type width is therefore a layout input, but fixed cell geometry must not silently dictate the font design. Compare exact rendered widths after construction.

### Web
Browser delivery remains downstream. A candidate that cannot render the bounded corpus itself is not ready for Web loading/fallback transfer.

### Color
Hold color constant while glyph form, spacing and numeric behavior are compared.

### Content Design
The new Content Design domain is active in the studio. Type must preserve the literal operational tokens supplied by the product corpus; typography must not alter aviation abbreviations, identifiers or numeric notation merely to improve visual regularity.

---

## SOURCE / standards boundary

OpenType GPOS PairPos supports both individual-pair positioning (format 1) and class-pair positioning (format 2). The registered `kern` feature exists to correct combinations that remain optically inconsistent after the typeface has generally consistent inter-glyph spacing. This supports the T021 order: establish coherent drawings and base spacing first; use T022 for residual pair/class behavior rather than as a repair layer for unfinished primitives.

This contract does not prescribe a GPOS implementation yet.

---

## Construction system

Working direction remains **B — Balanced**, but only as a research direction.

Common geometry inherited from T021:
- UPM 1000;
- cap height 700;
- x-height 500;
- baseline 0;
- round overshoot approximately 12u caps / 10u lowercase;
- regular stem target approximately 85u;
- kerning OFF throughout this expansion;
- straight and round sidebearings may differ;
- advance width is shape-sensitive, not a shared cap-cell constant.

### Reuse families

The expansion must be constructed as related form families rather than 24 unrelated drawings.

1. **Round family:** `O → C/G/D/0` where structurally defensible. Reuse curve tension/overshoot, not identical width by default.
2. **Stem/bowl family:** `D → B`; bowl joins must be optically corrected rather than mechanically copied.
3. **Vertical/horizontal family:** `H/L/I/T → E/F`; retain stem/crossbar mass while allowing different right-side spacing.
4. **Diagonal family:** `A/V → X/K/N`; shared diagonal mass is a starting constraint, not a requirement for identical angles or widths.
5. **Curved diagonal family:** `S` is independent enough to require its own balance proof; do not derive it by arbitrary deformation of O.
6. **Hook family:** `J` shares I/T cap vocabulary but requires its own lower terminal and sidebearing proof.
7. **Open-bottom round family:** `U` reuses round-bottom optical logic, not O's full ellipse.
8. **Digit family:** `0–9` shares cap/figure rhythm but must preserve recognition differences, especially `0/O`, `1/I/l`, `5/S`, `8/B`.
9. **Punctuation:** `- : ,` must align to operational strings and numeric roles; punctuation sidebearings are task-specific rather than copied from letters.
10. **Lowercase ambiguity control:** `l` is included specifically for `1/I/l` comparison.
11. **Accented path:** build at least one base+mark construction (recommended `É` from E + acute) to prove component/anchor or equivalent construction logic; this is curriculum breadth evidence, not a claim that the bounded LogMate corpus requires É.

---

## Required repertoire for this T021 closure block

Existing proven/built repertoire is not assumed beyond the exact current T021 artifacts. The next executable candidate must contain at minimum:

### Airport / identifier uppercase
`A B C D E F G H I J K L N O R S T U V X`

### Lowercase controls
`n o l`

### Figures
`0 1 2 3 4 5 6 7 8 9`

### Operational punctuation
`- : ,`

### Curriculum accent path
`É` plus the construction elements needed to build it.

### Space / notdef
Required for a valid research font.

This set is intentionally bounded. It is not a production Latin character-set recommendation.

---

## Pre-kerning control corpus

The exact same candidate must render, with kerning disabled:

### Airports
`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`

### Identifiers
`KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`

### Time / totals
`00:45 02:18 09:55 12:40 1,284:35 9,999:59 1 11 111 8 88 888`

### Ambiguity
`0O 1Il 5S 8B`

### Spacing controls
Retain H/O/n/o and A/V/T/L/I controls so new product breadth does not erase earlier family evidence.

---

## Intended-size proof matrix

The build must be rendered at:
- 14px — dense/small operational stress;
- 17px — primary current T021 product-like comparison size;
- 24px — larger inspection size.

For every size record:
1. advance width for each full control string;
2. whether any glyph falls back or `.notdef` appears;
3. image/raster evidence from the exact candidate artifact;
4. repeated-pair rhythm notes;
5. ambiguity-pair visual notes, explicitly labeled designer inspection rather than human recognition evidence.

Human recognition/error testing remains deferred to app-stage validation.

---

## Spacing acceptance protocol

Before T022 may open, classify every observed issue in this order:

1. **DRAWING** — contour/counter/terminal/weight problem remains even when spacing context changes.
2. **GENERAL SPACING** — the same side of a glyph repeatedly creates excess/deficient space across multiple partners.
3. **PAIR-SPECIFIC RESIDUAL** — base drawing and sidebearings behave consistently elsewhere, but a particular geometry combination remains exceptional.

Only category 3 is eligible to seed T022 kerning.

No absolute scanline-gap threshold is used. Pair-gap geometry may describe where whitespace occurs, but mature-font validation already showed that magnitude alone is not a calibrated defect criterion.

---

## Figure-system bridge to T022

T021 must construct readable default figures first. T022 will then compare at least:
- proportional figures for ordinary text/identifier contexts;
- tabular figures for comparison-critical numeric columns/totals.

Do not make the whole family monospaced merely to align figures. The product already has semantic columns, and prior LogMate evidence supports explicit tabular behavior for comparison-critical numeric roles.

---

## Direct product comparison requirements

A custom candidate is not allowed to win by aesthetic assertion. Once the bounded candidate is built, compare it against:

- **Control B:** proportional Roboto product baseline;
- **Control A:** exact airport-only `LogMateRobotoMono` interim control when that exact artifact is available to the test environment.

Required comparison dimensions:
- operational corpus coverage;
- target-size raster stability;
- airport-code width/scan rhythm;
- identifier width and column pressure;
- numeric alignment behavior;
- ambiguity-set distinctness by designer inspection only;
- fallback dependence;
- implementation complexity and reversibility;
- whether the candidate provides a coherent identity difference that survives operational constraints.

If the exact product mono artifact is unavailable, a generic mono may be used only as a lab control and must not be mislabeled as the LogMate control.

---

## T021 closure gate

T021 may close only when all are true:

- bounded repertoire above is actually built;
- bounded LogMate corpus renders without fallback/notdef in the candidate;
- 14/17/24px raster proof exists;
- base spacing has been revised from repeated-context evidence;
- remaining pair-specific residuals are enumerated rather than repaired ad hoc;
- at least one accented construction path is demonstrated;
- B is either retained or replaced using rendered evidence;
- product-control comparison is sufficient to state what is gained and sacrificed;
- no human/browser/native claim is made without corresponding evidence.

Until then T022 remains blocked.

---

## HANDOFFS

### Layout / Interaction
Keep the airport font seam replaceable and avoid freezing column geometry around the temporary mono control. When the candidate exists, test exact widths in the real table before changing column allocation.

### Web Design
Wait for a no-fallback bounded candidate, then transfer the exact binary into loading/fallback/zoom/localization tests.

### Content Design
Preserve operational token syntax. If later terminology or label changes affect the test corpus, Type should rerun the corpus rather than silently substituting strings.

### Color
Keep semantic color unchanged through candidate/control comparisons.

---

## Verdict

**T021 remains IN PROGRESS, but the breadth blocker is now converted into a single executable construction/validation contract.**

Next substantive block should implement this repertoire and run the full pre-kerning product corpus. Do not return to isolated A/V gap tuning and do not open T022 early.