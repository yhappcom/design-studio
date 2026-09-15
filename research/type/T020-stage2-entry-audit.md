# T020 — Typography / Type Design Stage 2 Entry Audit

Status: **STAGE 2 ENTRY AUDIT — existing bridge evidence mapped; Intermediate Professional Practice NOT PASSED**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`

## Purpose

T019 closed the exact Master Curriculum Stage 1 gate. The next task is not to continue accumulating advanced font-engineering studies without structure; it is to map the exact Stage 2 requirements against existing evidence, identify what is already reusable, and isolate the smallest set of genuine Intermediate-practice gaps.

This is an **ENTRY AUDIT + EVIDENCE MAP**, not a Stage 2 PASS claim.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- `curriculum/MASTER_CURRICULUM.md` Stage 2;
- `progress/TYPE_STATUS.md` through T019;
- legacy Studies 001/002/003/005/009;
- T002–T010 family/rendering/interpolation bridge evidence;
- T016 webfont loading/fallback geometry;
- T017/T018 LogMate live-product transfer.

Reusable finding:
- Type already has meaningful evidence for interpolation fundamentals, screen rendering, figure-feature behavior and multi-role product typography, but most of it is isolated or transfer-oriented rather than a coherent Stage 2 family-system exercise.

### Color

Evidence checked:
- current Color Stage 1 closure state and its Stage 2 boundary.

Reusable finding:
- Stage progression must not confuse advanced evidence accumulated early with completion of the current gate. Type applies the same rule here.

### Layout / Interaction

Evidence checked:
- L003 fallback/reflow transfer;
- L004 tabular-numeral dense-comparison transfer;
- LogMate fixed-cell/enlarged-text handoff reflected in T018.

Reusable finding:
- Type alternatives must be judged inside actual information geometry. A typographic solution that improves one glyph metric but damages comparison, wrapping or enlarged-text behavior is not automatically the selected direction.

### Web Design

Evidence checked:
- W001/W009 status implications already consumed by T019;
- T016 Type→Web loading/fallback transfer.

Reusable finding:
- browser transfer can test a Type system, but Web implementation evidence does not substitute for Type-owned family coherence, spacing, kerning or figure-system proof.

### Other / standards

Current CSS Fonts Level 5 was rechecked for `size-adjust`, `ascent-override`, `descent-override`, and `line-gap-override`. These remain useful later transfer tools for fallback metric harmonization, but they do not close Stage 2 family-design requirements.

### Overlap decision

**AUDIT + SYNTHESIS.** No new mechanism is introduced merely to increase study count. Existing evidence is reused where it genuinely satisfies part of Stage 2; unresolved requirements are kept OPEN.

---

## SOURCE — exact Stage 2 Type requirements

The Master Curriculum Stage 2 Type Design block requires:

1. coherent glyph families;
2. spacing systems and control strings;
3. kerning classes and exceptions;
4. figure styles: proportional/tabular, lining/oldstyle where relevant;
5. diacritics and punctuation systems;
6. weight/width relationships;
7. interpolation fundamentals;
8. screen rendering and small-size compensation.

The shared Stage 2 Information/Product block also includes typography systems across multiple roles.

The Stage 2 gate requires **multiple solutions to the same problem** and a defended selected direction using explicit criteria, including correctly borrowed adjacent-specialist evidence.

---

## Stage 2 entry matrix

| Requirement | Existing bridge evidence | Entry verdict | What is still needed |
| --- | --- | --- | --- |
| coherent glyph families | Exercises 001/002; T003/T006 controls | **PARTIAL** | one coherent mini-family specimen with shared construction rules, repeated forms and explicit outlier handling |
| spacing systems + control strings | Studies 001/002; Exercise 001; T006 metrics audit | **PARTIAL** | systematic control-string set across letters/numerals/punctuation; sidebearing decisions revised from proof |
| kerning classes + exceptions | basic spacing/kerning principles exist | **OPEN** | real class model, representative pairs, exception rationale, proof before/after |
| figure styles | Study 005; Exercise 003; T004; T009; T018 `tnum` transfer | **PARTIAL / STRONG BRIDGE** | coherent proportional/tabular set in one family; lining/oldstyle only if a use case justifies it; compare alternatives rather than feature existence alone |
| diacritics + punctuation systems | Study 005; T012/T013 attachment work | **PARTIAL** | coherent base/diacritic/punctuation family treatment and spacing/proof, not only anchor/package integrity |
| weight/width relationships | T007/T010 variable interpolation | **PARTIAL / STRONG BRIDGE** | design-level relationship proof across a coherent glyph set, including intermediate-weight critique rather than only technical interpolation validity |
| interpolation fundamentals | T007/T010 | **SUPPORTED FOR ENTRY** | retain as bridge; integrate into family exercise rather than repeat generic mechanism research |
| screen rendering + small-size compensation | T002/T003/T004/T018 | **PARTIAL / STRONG BRIDGE** | multiple coherent solutions at target sizes with explicit KEEP/REWORK/REJECT selection criteria |
| typography across multiple product roles | Study 009; T017/T018 LogMate | **PARTIAL / STRONG BRIDGE** | consolidate role hierarchy into an explicit Type system and compare at least two viable role-system directions |
| Stage 2 gate: multiple solutions + defended selection | Exercise 001/002 contain alternatives; T018 compares candidates | **PARTIAL** | one integrated Stage 2 exercise must deliberately generate alternatives across family/spacing/role decisions and select with explicit criteria + peer evidence |

### SYNTHESIS

Stage 2 is not blocked by lack of advanced production tooling. The largest missing evidence is more basic and more important: **a coherent family-scale exercise that joins drawing, spacing, kerning, figures, diacritics/punctuation, weight relationship, small-size proof and critique into one system.**

T007/T010 and T012–T016 are useful early advanced evidence, but they cannot substitute for this Intermediate family-system practice.

---

## Highest-value Stage 2 work sequence

### T021 — coherent mini-family + spacing/control-string system

Build a deliberately bounded Latin core rather than a production character set. Recommended minimum:
- repeated-form controls: `H O n o`;
- diagonal/round/vertical stress: `A V T L I` plus selected lowercase;
- numerals `0–9`;
- core punctuation needed for spacing proof;
- at least one accented-letter construction path.

Required evidence:
- at least **three** coherent design/spacing directions or materially different hypotheses;
- explicit construction rules and repeated-form reuse;
- control strings for sidebearings before kerning;
- intended-size raster/browser proof;
- KEEP / REWORK / REJECT critique with explicit criteria.

### T022 — kerning classes/exceptions + figure alternatives

Using the selected T021 direction:
- define classes only where shared behavior is actually defensible;
- prove representative class pairs and exceptions;
- compare proportional vs tabular figures inside the same family;
- add oldstyle figures only if a product/editorial use case makes them relevant rather than treating them as mandatory decoration.

### T023 — weight/interpolation + diacritic/punctuation coherence

Extend the same system rather than opening an unrelated research font:
- at least two masters and meaningful intermediate instance proof;
- repeated-form and spacing consistency across weight;
- diacritic/punctuation optical relationship across weights;
- target-size critique and failure documentation.

### T024 — multi-role typography-system alternatives

Transfer the family/system knowledge into at least two viable role systems for a product surface, preferably LogMate if the live design state is suitable:
- hierarchy;
- operational identifiers;
- numeric comparison;
- dense ledger;
- labels/supporting text;
- enlarged-text/fallback constraints.

Select one direction using explicit criteria and Layout/Color/Web evidence.

This sequence is provisional. A live LogMate implementation need can pre-empt it.

---

## Stage 2 critique criteria

Future exercises should not select a direction because it is merely cleaner or more attractive. Record criteria such as:

1. family coherence — repeated forms and terminals behave as a system;
2. spacing rhythm — acceptable before pair-specific kerning;
3. exception cost — how many special cases the system creates;
4. numeral/punctuation task fit;
5. weight/interpolation continuity;
6. target-size raster robustness;
7. role hierarchy and dense-data performance;
8. localization/fallback risk;
9. implementation complexity and reversibility;
10. peer-domain consequences for Layout, Color and Web.

A selected solution should state what it sacrifices as well as what it improves.

---

## STUDIO JUDGMENT

The correct next Type learning phase is **less fragmented font-engineering exploration and more integrated family/system practice**.

Reason:
- Stage 1 already established concepts and original exercises;
- several Stage 3/4-like mechanisms were explored early;
- the exact Stage 2 gate is about professional comparative practice and defended selection;
- coherent system construction is the clearest current gap.

This does not discard T006–T018. Those studies become stress tests and production-aware constraints for the Stage 2 exercises.

---

## OPEN

Stage 2 remains **NOT PASSED**.

Primary OPEN items:
- coherent mini-family proof;
- systematic control strings;
- kerning class/exception model;
- integrated figure-style alternatives;
- diacritic/punctuation family coherence;
- design-level weight relationship proof;
- integrated small-size compensation alternatives;
- one explicit multi-solution Stage 2 gate exercise with defended selection.

Later-stage items remain later-stage and are not reintroduced as Stage 2 blockers unless the current exercise depends on them:
- FontBakery/OTS/Fontspector;
- native cross-platform parity;
- full mixed-script systems;
- production family naming/build/release;
- human recognition/scan studies.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Stage 2 Type exercises should hold Color stable while drawing/spacing alternatives are compared, then test final role systems with actual Color hierarchy rather than judging isolated black glyphs only.
- No Color Stage 2 evidence is claimed here.

### Layout / Interaction
- T021–T024 should reuse L003/L004 constraints: fallback and numeric feature choices can alter geometry, while enlarged-text failure must not be disguised by smaller or narrower type.
- Layout should receive exact selected artifacts when the Type system reaches transfer stage.

### Web Design
- T016 remains the loading/fallback transfer baseline. Stage 2 family exercises should not become browser implementation studies, but final selected artifacts should later be tested through actual Web delivery.

---

## Final checkpoint

- Stage 1 PASS remains valid.
- **Stage 2 entry audit complete.**
- Existing bridge evidence is substantial but fragmented.
- Stage 2 Type Design: **NOT PASSED**.
- Highest-value next new study: **T021 — coherent mini-family + spacing/control-string system with multiple alternatives and explicit critique.**
