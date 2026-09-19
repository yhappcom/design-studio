# LogMate Integration Principles — 2026-09-19

Status: **PHASE 2 COMPLETE — INTEGRATED PRE-DESIGN PRINCIPLES / NO VISUAL STYLE SELECTED**

Inputs:
- `EVIDENCE_MAP_20260919.md`
- `CONTRADICTION_REGISTER_20260919.md`
- T073 / C104 / I091 / L095 / W104 / CD110
- current LogMate MASTER/specs and visual-identity restart
- owner clarifications recorded 2026-09-19

This artifact integrates the audited evidence. It does not select a palette, font family, component style, final navigation architecture, or UI concept.

## 1. Current owner clarifications carried into synthesis

1. **Remark is arbitrary-language user/source text.**
   - English-only applies to LogMate-authored UI.
   - Remark may contain any language/script.
   - Design and Type must preserve Unicode/shaping/fallback behavior instead of forcing an English or monospace treatment.

2. **Activity period semantics are 7 / 28 / 90 days + Custom.**
   - Current concept work may keep `7 days / 28 days / 90 days / Custom`.
   - Reintroducing a shared `Last` prefix is a later detail, not a current invariant.

3. **Bottom navigation is preferred for the next Home concept.**
   - Home has sufficient space to explore it.
   - This is a composition/exploration direction, not closure of NAV-001.
   - Exact destinations, persistence and whole-app navigation architecture remain OPEN.

4. **The visual canvas remains blank.**
   - Round-1 A/B/C, Concept C, fixed-character cells and prior decorative grammar do not seed the next concept.
   - Product semantics and confirmed interaction/ledger contracts remain intact.

---

# 2. Integrated principles

## IP01 — Product truth before visual authorship

Visual authorship may reorganize emphasis, rhythm, surface behavior and expression, but it may not rewrite professional meaning, state truth, data identity, consequence, recovery, calculation meaning or confirmed interaction semantics.

Failure condition:
- a cleaner screen changes what Block, Flight, Inst, Route, save/persistence state, recovery, or another confirmed concept means.

Sources:
E01/E21/E37/E54/E56; I091; CD110.

## IP02 — Two typographic voices, not one brand font everywhere

LogMate may use a restrained proportional UI voice for interface language and an exact mature mono operational-data voice where confirmed. The operational voice exists to stabilize comparison, not to make the application look technical.

Rules:
- repeated Flight uses mono operational treatment plus carrier / number+suffix zoning;
- View Logbook body retains its regular mono/code role;
- general labels, prose, controls, Crew/Remark and ordinary free text are not blanket mono;
- Remark must remain arbitrary-language Unicode/fallback safe;
- comparison numerics outside mono roles may use tabular figures when appropriate.

Failure condition:
- a type choice improves visual uniformity while causing identifier jitter, script failure, semantic flattening or production geometry dependence on the unfinished custom font.

Sources:
E05–E16/E51/E59; T073; CR01–CR10/CR34/CR47.

## IP03 — Stable geometry means stable relationships, not frozen screens

Comparable operational values keep stable local axes and semantic boundaries. Responsive/adaptive composition may move regions, but Date/Flight/Route/duration comparison must not visibly wander because of glyph widths or ad-hoc alignment.

Rules:
- Flight internal zones remain stable;
- ledger header/body/totals share semantic column boundaries;
- whole-string Flight centering remains rejected;
- stable axes do not require identical absolute coordinates across Home, Activity and View Logbook.

Failure condition:
- a responsive or aesthetic change causes the same semantic family to lose its comparison axis.

Sources:
E16–E18/E50/E55; L095; T073.

## IP04 — Calm comes from governed density

LogMate does not equate premium quality with emptiness. Dense professional information is acceptable when hierarchy, grouping, target geometry, alignment and reading order are controlled.

Rules:
- whitespace performs structural work;
- remove visual competition before removing useful data;
- enlarged/narrow conditions recompose before shrinking or semantically damaging content;
- the dense ledger may use controlled two-dimensional scrolling where its meaning requires it, while surrounding forms/controls reflow normally.

Failure condition:
- “cleaner” appearance is achieved by hiding useful professional data, making text impractically small, or applying the ledger exception to unrelated surfaces.

Sources:
E18–E26; L095; T073; CR11–CR15.

## IP05 — Consequence and focus outrank brand salience

Brand color, motion and signature treatments operate only after focus, selection, invalid/ambiguous state, warning/recovery, success and persistence remain correctly distinguishable.

Rules:
- one accent cannot be the sole carrier of brand + focus + selection + success;
- required state meaning survives authored-color loss;
- motion may reinforce but never exclusively communicate state;
- a quiet visual system reduces decorative chroma before it reduces functional salience.

Failure condition:
- a user cannot distinguish consequential states without the brand color or animation.

Sources:
E27–E38; C104; I091; W104.

## IP06 — Low chrome is conditional, not ideological

Borders, cards, dividers and filled surfaces may be removed when alignment, whitespace, labels, target geometry and state already make the relationship unambiguous. Functional boundaries remain where removing them creates uncertainty.

Failure condition:
- visual reduction weakens grouping, touch-target understanding, focus location or edit/recovery ownership.

Sources:
E25/E33/E34; L095; C104.

## IP07 — Interaction is direct, reversible and semantically equivalent

Different input mechanics may differ visually, but they converge on the same semantic object and mutation.

Rules:
- recovery remains discoverable where a truthful inverse exists;
- drag is not identity until a required non-drag single-pointer path exists;
- browser/framework lifecycle is not save/sync/product state;
- visual transitions must preserve state truth with reduced motion.

Failure condition:
- a signature interaction changes transaction semantics, hides recovery or depends on one input mode.

Sources:
E35–E38; I091; W104.

## IP08 — Content is precise; authored language and user data are separate layers

LogMate-authored interface copy remains English-only. User/source content preserves its own language and identity.

Rules:
- do not translate or normalize Remark/source evidence for visual consistency;
- period semantics remain 7 / 28 / 90 days + Custom; exact `Last` prefix treatment is deferred;
- established professional terminology is not shortened merely to fit;
- voice may be quiet/non-theatrical only after state/action/consequence/recovery truth is complete.

Failure condition:
- visual fit or tone changes domain meaning, rewrites user evidence, or turns a current copy detail into a product-semantic decision.

Sources:
E21–E24/E38/E51/E52/E58/E59; CD110; CR41/CR42/CR47.

## IP09 — Identity must transfer as a rule, not as copied Home geometry

A LogMate design code must survive Home, View Logbook, Activity, Add Flight and relevant configuration/import surfaces without requiring identical composition.

Rules:
- Home may be spacious while ledger is dense;
- a signature must adapt to forms and state-heavy surfaces;
- a Home-only decoration is a surface treatment, not brand code.

Failure condition:
- the recognizable idea disappears or becomes obstructive outside Home.

Sources:
E39/E47; L095; W104; CR25/CR26.

## IP10 — Runtime fallback is part of the design

A candidate is not robust if it works only in a static screenshot or only when fonts, network, route lifecycle and authored colors behave ideally.

Rules:
- font fallback must preserve meaning and workable geometry;
- forced colors and reduced motion preserve operation;
- reflow/enlarged text is evaluated as real behavior;
- browser/native evidence is kept distinct from human evidence.

Failure condition:
- failure/fallback states destroy semantic identity or geometry.

Sources:
E40–E43; T073/C104/W104.

## IP11 — Brand character comes from repeatable discipline

LogMate's authorship should emerge from standards, reduction, stable geometry, typographic discipline, predictable interaction and a small number of transferable codes—not luxury styling or aviation decoration.

Explicitly not evidence of quality:
- cockpit/dial/runway motifs;
- black/gold or metallic styling;
- serif merely as a luxury cue;
- glass/blur/material simulation;
- all-monospace styling;
- thin rules everywhere;
- excessive emptiness;
- Round-1 visual fragments.

Sources:
E44–E49; BRAND_PHILOSOPHY_RESET; CR30–CR32/CR40.

## IP12 — Evidence maturity remains visible

A principle may guide concept creation before production validation only when its unverified boundaries stay explicit.

Still OPEN:
- exact production mono family;
- large-text dense-ledger adaptation;
- locale-date width budget;
- runtime/independent-engine/device proof;
- representative-pilot scanning/workload/comprehension;
- NAV-001 final whole-app navigation semantics;
- SEARCH-001 Home suggestion/autocomplete/result-entry behavior.

The owner-preferred Home bottom-navigation region may be explored now without pretending those NAV-001 details are closed.

---

# 3. Cross-surface application test

| Principle family | Home | View Logbook | Activity | Add Flight | Customize / Import |
|---|---|---|---|---|---|
| Semantic truth | preserve families/Block meaning | preserve field/totals semantics | preserve period meaning | preserve entry semantics | preserve state/provenance |
| Type roles | UI + operational mono rows | dense mono body + UI headers | UI + repeated operational rows | proportional form/UI | proportional UI + source data fallback |
| Stable geometry | local repeated-row axes | shared columns/offsets | local comparison axes | form alignment/reflow | mapping/state relationships |
| Density | calm summary composition | dense ledger allowed | compact summary/filter | form legibility | dense but grouped |
| State salience | nav/search/action/focus | selection/focus/scroll state | selected period/detail state | validation/recovery | reorder/import ambiguity/recovery |
| Content | English authored UI | English headers + arbitrary Remark data | period copy detail flexible | English labels/helpers | English authored UI + source evidence |
| Identity transfer | rule, not decoration | survives density | survives filtering | survives forms | survives complex states |

No row above defines a final visual treatment.

---

# 4. Owner-direction notes for the next phase

These are not universal principles but must shape the upcoming Design Corridor:

- Next Home concept should **include a bottom-navigation region by default**.
- The region must be visually integrated without consuming or destabilizing the Home information families.
- Its presence does not determine final navigation destinations or whole-app architecture.
- Activity currently keeps the shorter period labels without repeated `Last`.
- Remark is treated as arbitrary-language user text in all typography/geometry stress.

---

# 5. Gate result

**Integration Principles: COMPLETE for concept-generation synthesis.**

No material contradiction was found that requires returning to Evidence Map / Contradiction Register.

Allowed next phase:
`Design Corridor -> Operational Geometry Contract -> Signature Code Study`

Still prohibited:
- drawing a new Home/UI concept before those remaining pre-design phases are completed;
- reusing Round-1 A/B/C as visual starting material;
- silently closing NAV-001, SEARCH-001 or runtime/type/accessibility OPEN items.
