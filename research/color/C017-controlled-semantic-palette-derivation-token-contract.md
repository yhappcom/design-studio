# C017 — Controlled Semantic Palette Derivation & Token Contract

Status: **PRACTICE / CRITIQUE — three viable systems authored; C selected provisionally; browser/device/human transfer OPEN**

Owner: Color Specialist

## Question

Can one bounded operational/data-product color problem be solved by three materially different palette systems under identical semantic and geometry constraints, then selected by explicit criteria rather than taste?

## RELATED DOMAIN CHECK

### Type
Checked current `TYPE_STATUS.md` and C009. Text contrast is evaluated as a declared color-pair property only; exact font/raster/platform transfer remains Type/Web evidence. No typography PASS is inferred.

### Color
Checked Study 017, C002, C006, C010, C011, C015 and C016. C017 is the integrated authorship exercise C016 identified as the highest-value Stage 2 gap. It deliberately reuses the established semantic-token and gamut boundaries instead of repeating color-space theory.

### Layout / Interaction
Checked current Layout/Interaction status and the newer L008 evidence referenced by C016. Geometry and state meaning are held fixed. Focus, selected, pending, success, caution and critical remain interaction semantics; Color only encodes them.

### Web Design
Checked Web through W013. Web has real Chromium transfer evidence but no selected C017 contract yet. C017 therefore produces a concrete handoff for later CSS/theme/forced-colors/P3 transfer rather than claiming browser execution.

### Repetition classification
**TRANSFER + INTEGRATED PRACTICE.** C002/C006 established architecture and collision methods; C017 applies them to three whole-system alternatives and performs system-scale selection.

---

## Fixed product problem

Archetype: dense operational log/data application used for repeated scanning, editing and status review.

Fixed semantic inventory:
- canvas/background;
- surface;
- primary text;
- secondary text;
- boundary;
- primary action + on-action text;
- focus indicator;
- selected surface;
- success;
- caution;
- critical.

Fixed rules:
- color does not change geometry, iconography or copy;
- critical meaning must retain a non-color cue in product use;
- selected and focus remain distinct roles;
- status hues are not reused as generic action color;
- light and dark themes preserve role identity rather than numeric color identity;
- sRGB is the shipping baseline; Display-P3 is optional enhancement, not required for semantic correctness.

## Three authored directions

### A — restrained neutral + cyan-blue action

Intent: familiar application neutrality with one clear action accent and conventional separated status hues.

Light: bg `#F7F9FA`, surface `#FFFFFF`, text `#172126`, secondary `#56636A`, border `#C9D2D6`, action `#176B87`, on-action `#FFFFFF`, focus `#8A4FFF`, selected `#DCEFF5`, success `#19734A`, caution `#8A5A00`, critical `#B4232C`.

Dark: bg `#10181C`, surface `#162025`, text `#EEF4F6`, secondary `#B7C3C8`, border `#46545A`, action `#73C7E1`, on-action `#102126`, focus `#C2A8FF`, selected `#213A43`, success `#73C99D`, caution `#E0B65E`, critical `#FF9097`.

### B — brand-forward teal

Intent: stronger brand presence while keeping semantic status hues independent.

Light: bg `#F5FAF9`, surface `#FFFFFF`, text `#122321`, secondary `#50625F`, border `#C4D4D0`, action `#087A70`, on-action `#FFFFFF`, focus `#7048D7`, selected `#D5F1EC`, success `#1B7448`, caution `#875C00`, critical `#B12A35`.

Dark: bg `#0E1917`, surface `#132320`, text `#EFF7F5`, secondary `#B5C7C2`, border `#435A55`, action `#65D0C1`, on-action `#102421`, focus `#B7A0FF`, selected `#1D3D37`, success `#73CA99`, caution `#E1B85C`, critical `#FF919B`.

### C — low-chroma operational

Intent: reduce decorative chroma and reserve stronger hue differences for state/action recognition while preserving high luminance separation.

Light: bg `#F7F8F8`, surface `#FFFFFF`, text `#1B2224`, secondary `#596164`, border `#C9CED0`, action `#355F6B`, on-action `#FFFFFF`, focus `#654FB0`, selected `#E0EAED`, success `#3F6E55`, caution `#776027`, critical `#934149`.

Dark: bg `#14191B`, surface `#1A2022`, text `#F0F3F4`, secondary `#BCC3C5`, border `#4B5558`, action `#9BC3CF`, on-action `#172226`, focus `#B8AAE5`, selected `#29373B`, success `#9AC7AA`, caution `#D1BC86`, critical `#DFA0A6`.

---

## Reproducible contrast check

Method: WCAG relative-luminance contrast calculation on declared sRGB values. This is not a claim about exact rendered glyph accessibility.

Light-theme contrast against surface:

| Role | A | B | C |
|---|---:|---:|---:|
| primary text | 16.38 | 16.30 | 16.14 |
| secondary text | 6.20 | 6.45 | 6.33 |
| action | 6.02 | 5.21 | 7.00 |
| focus | 4.52 | 5.84 | 6.37 |
| success | 5.85 | 5.77 | 5.88 |
| caution | 5.93 | 5.90 | 6.02 |
| critical | 6.53 | 6.46 | 6.79 |
| on-action / action | 6.02 | 5.21 | 7.00 |

Dark-theme contrast against surface:

| Role | A | B | C |
|---|---:|---:|---:|
| primary text | 14.92 | 14.97 | 14.79 |
| secondary text | 9.19 | 9.24 | 9.23 |
| action | 8.67 | 8.80 | 8.72 |
| focus | 8.16 | 7.36 | 7.79 |
| success | 8.34 | 8.25 | 8.73 |
| caution | 8.70 | 8.70 | 8.83 |
| critical | 7.64 | 7.58 | 7.63 |

All three are intentionally viable controls rather than one good option and two strawmen.

## Semantic collision critique

### A
KEEP: strong conventional role recognition; action/status separation; high contrast margins.

REWORK: focus at 4.52:1 is the narrowest declared pair in the experiment and gives less margin than B/C; cyan-blue action can become visually dominant in dense tables.

Verdict: **KEEP as conventional control, not selected.**

### B
KEEP: strongest brand continuity; selected surface and action family are coherent; status hues remain separate.

REWORK: action is intentionally saturated relative to the rest of the system, increasing risk that brand/action chroma dominates dense operational content. Token use discipline becomes more important.

Verdict: **KEEP as brand-forward alternative, not selected for the bounded operational archetype.**

### C
KEEP: highest light-theme action/on-action margin of the three; strongest light-theme focus margin; lower chroma reduces competition between chrome and data; semantic status roles remain distinguishable by hue family and luminance while requiring redundant non-color cues for critical meaning.

REWORK: deliberately muted status hues may be less immediately salient in some physical viewing conditions; that cannot be settled without device/environment/human evidence.

Verdict: **PROVISIONAL SELECT.**

## Selection rationale

C is provisionally selected for this bounded operational/data archetype, not as a universal Design Studio palette.

Reasons:
1. hierarchy is least dependent on decorative chroma;
2. declared contrast margins are consistently strong, including action/focus;
3. light/dark role continuity is straightforward;
4. action, focus and status families remain semantically separated;
5. sRGB values already satisfy the baseline contract, so P3 is unnecessary for correctness;
6. lower-chroma chrome reduces implementation risk in dense data surfaces where color should not compete with information.

A remains the safer conventional fallback when familiarity is more important than low-chroma operational restraint. B becomes preferable when brand expression is a first-order product requirement.

## Token contract

Primitive values may change; semantic names are the stable implementation interface.

Required semantic tokens:
`color.bg.canvas`, `color.bg.surface`, `color.text.primary`, `color.text.secondary`, `color.border.default`, `color.action.primary`, `color.action.onPrimary`, `color.focus.ring`, `color.selection.bg`, `color.status.success`, `color.status.caution`, `color.status.critical`.

Theme resolution maps each semantic token to the selected light/dark primitive. Components must consume semantic tokens rather than palette-step names.

### Shipping/gamut contract

- baseline: explicit sRGB values above;
- Display-P3: **not authored in C017** because no role requires extra gamut to preserve meaning;
- if future P3 enhancement is introduced, sRGB remains the complete semantic fallback;
- out-of-gamut clipping must never create the only distinction between two semantic roles;
- forced-colors/user override behavior remains a separate Web transfer gate.

## Failure conditions

Reopen selection if:
- exact rendered text/control combinations lose required contrast margin;
- selected/focus/status roles collide under real component adjacency;
- dark theme creates excessive status salience or insufficient boundary separation;
- physical glare/low-light/device tests materially reverse the low-chroma advantage;
- brand requirements make C too weak for the actual product;
- browser forced-colors or system-color substitution exposes role dependencies hidden by authored color.

## Evidence boundary

**SOURCE reused:** existing canonical Color science/contrast/gamut/token studies and peer interaction semantics.

**PRACTICE:** three complete light/dark semantic systems authored under identical constraints.

**CRITIQUE:** A/B/C evaluated with KEEP/REWORK/SELECT decisions and explicit trade-offs.

**STUDIO JUDGMENT:** C is the provisional operational-data direction; A and B remain valid alternatives under different priorities.

**OPEN:** exact browser CSS execution, P3 enhancement need, Firefox/Safari/OS parity, physical displays/ambient conditions, real CVD/human observers, product-specific brand fit.

No human or physical-device evidence is simulated.

## HANDOFFS TO OTHER SPECIALISTS

### Type
C017 provides declared pair contracts only. Exact font weight/raster/fallback conditions must be checked before production accessibility conclusions.

### Layout / Interaction
C confirms that state meaning can remain fixed while visual chroma strategy changes. Product specimens should test selected/focus/status adjacency without redefining interaction semantics.

### Web Design
C is ready for independent browser TRANSFER VALIDATION: CSS light/dark token resolution, forced-colors, `color-scheme`, system-color substitution, zoom/enlarged text adjacency, and optional P3 fallback only if a real enhancement is later justified.

## Stage 2 implication

C017 closes C016's largest integrated-authorship gap: multiple viable whole-system solutions, explicit criteria, whole-system critique, provisional selection and a shipping baseline contract now exist.

It does **not** by itself prove Color Stage 2 PASS. The next audit should determine whether browser/device-aware transfer evidence already present in C009–C011 plus C017 is sufficient for the exact Stage 2 gate or whether one focused transfer exercise is still required.