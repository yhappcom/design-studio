# LogMate Design Corridor — 2026-09-19

Status: **PHASE 3 COMPLETE — VISUAL BEHAVIOR CORRIDOR / NO UI CONCEPT DRAWN**

Upstream authority:
- `EVIDENCE_MAP_20260919.md`
- `CONTRADICTION_REGISTER_20260919.md`
- `INTEGRATION_PRINCIPLES_20260919.md`
- current LogMate product contracts and visual-identity restart

Purpose: define the visual territory that future LogMate concepts may explore without selecting a specific style, palette, production font, component library, or Round-1-derived composition.

---

# 1. Corridor character

Future LogMate concepts must feel:

- **exact** — alignment, repetition and state behavior are deliberate;
- **calm under density** — data may be dense without becoming visually noisy;
- **professional** — domain credibility comes from correct operational information and behavior;
- **quietly authored** — recognizable choices repeat without demanding attention;
- **durable** — avoid visual fashion as the primary source of identity;
- **direct** — controls and state transitions reveal what can happen and what just happened.

These are behavioral constraints, not instructions to imitate an existing product category.

---

# 2. Composition corridor

## Allowed

- clear hierarchy through proportion, alignment, spacing, typography and selective surface contrast;
- low-chrome compositions where grouping remains unmistakable;
- different density profiles by surface:
  - calmer Home;
  - dense View Logbook;
  - compact Activity;
  - task-focused Add Flight;
  - explicit state ownership in Customize/import;
- responsive recomposition that preserves semantic order and comparison relationships;
- section composition authored from the blank canvas rather than inherited from the rejected Home concepts;
- a bottom-navigation region in the next Home concept as the owner-preferred exploration default.

## Required boundary for Home bottom navigation

The next Home concept should reserve and visually integrate a bottom-navigation region because the owner considers the available space sufficient.

This does **not** decide:
- final destinations;
- number of destinations;
- app-wide persistence;
- whether every form/detail/landscape surface uses the same navigation;
- NAV-001.

The composition must therefore be able to change the nav information architecture later without requiring the Home identity to be rebuilt.

## Not allowed

- using a stock dashboard/card stack as the default composition grammar;
- copying Round-1 A/B/C section geometry;
- using Concept C rails/divisions as a hidden starting grid;
- forcing every surface into the same composition;
- adding decorative containers merely to make the screen look designed.

---

# 3. Typography corridor

## Allowed / expected

- proportional interface typography for product-authored labels, controls, prose and most non-operational roles;
- exact mature mono treatment for confirmed operational-data roles;
- Flight carrier + number/suffix zoning inside the mono role;
- tabular figures where proportional summary numerics need stable digit advances;
- a fallback-safe proportional treatment for Remark, Crew and other arbitrary user/source text;
- arbitrary-language/script input in Remark without treating that content as localized product UI.

## Open

- exact production proportional family;
- exact production mono family;
- custom LogMate type production use;
- exact scale/weight pairing outside already confirmed product contracts.

## Not allowed

- blanket monospace application;
- global serif as a luxury shortcut;
- typography that depends on unfinished T021 metrics;
- fixed per-character cells;
- whole-string Flight centering;
- negative tracking or microtype reduction used to rescue a failing layout;
- Latin-only assumptions for Remark/source text.

---

# 4. Color corridor

## Allowed

- neutral-dominant operational fields;
- restrained brand/accent usage;
- relational light/dark or light/night systems where semantic roles remain stable;
- state-specific tokens and non-color cues;
- stronger local salience when focus, invalidity, ambiguity, warning or recovery requires it.

## Open

- exact hue family;
- production light/dark palette;
- whether a single recognizable brand hue is ultimately needed;
- calibrated night/glare behavior pending real-device evidence.

## Not allowed

- one accent meaning brand + focus + selection + success;
- using low contrast as a synonym for premium;
- black/gold, metallic or aviation-instrument color mimicry as a shortcut;
- color-only state communication;
- claims of cockpit/night optimization from static dark screenshots.

---

# 5. Surface and boundary corridor

## Allowed

- whitespace/alignment as the first grouping mechanism;
- visible boundaries only where they improve grouping, ownership, state or target understanding;
- local surfaces for active/selected/edited/error/recovery regions;
- denser rule/grid treatment in the actual ledger when it supports the confirmed ledger model.

## Not allowed

- card-everything grammar;
- thin rules everywhere as a premium motif;
- permanent rails/grooves/bezels as brand decoration;
- hiding a necessary functional boundary for visual cleanliness;
- importing ledger grid density into ordinary forms merely for consistency.

---

# 6. Shape and control corridor

The corridor does not freeze radii, corner systems or control silhouettes yet.

## Allowed

- restrained geometry with consistent reasons;
- visible mark and larger interactive target as separate layers;
- platform-stable icons or primitives;
- control shape variation when semantic role justifies it.

## Not allowed

- novelty geometry without interaction value;
- cockpit, dial, altimeter, runway, aircraft or watch-control metaphors;
- tiny interactive marks with tiny hit targets;
- making every action look equally primary.

---

# 7. Motion corridor

## Allowed

- restrained transition feedback that clarifies continuity, ownership or completion;
- local motion attached to an actual state change;
- reduced-motion alternatives that preserve the complete semantic result.

## Not allowed

- motion as the sole carrier of state;
- decorative kinetic identity;
- animation that delays direct data work;
- using motion smoothness as proof of save/sync/completion.

Exact duration/easing is not selected in this phase.

---

# 8. Content corridor

## Product-authored UI

- English-only;
- professional aviation terminology remains stable;
- consequential state/recovery copy remains explicit;
- candidate voice: precise, quiet, operational, non-theatrical.

## User/source content

- not forced to English;
- Remark may contain any language/script;
- imported/source identifiers remain evidence, not brand copy.

## Activity periods

The semantic set remains:
- 7 days;
- 28 days;
- 90 days;
- Custom.

Current concept work may omit repeated `Last`. A shared `Last` prefix can be reconsidered later without changing the period model.

---

# 9. Density corridor by surface

| Surface | Density corridor | Primary failure to avoid |
|---|---|---|
| Home | calm summary + fast entry/navigation | decorative dashboard or excessive emptiness |
| View Logbook | dense, calibrated, scan-oriented | semantic compression/jitter |
| Activity | compact comparison/filtering | oversized dashboard treatment |
| Add Flight | task-focused form density | card stacking and weakened field/state ownership |
| Customize/import | explicit state/provenance density | low-chrome ambiguity |

This is not a component specification.

---

# 10. Identity corridor

A future LogMate identity may emerge from:

- calibrated operational axes;
- deliberate dual typographic voice;
- disciplined local density;
- boundaries that appear for functional reasons;
- state transitions that are direct and recoverable;
- repeated small details that survive every major surface.

A future LogMate identity may **not** depend on:

- one decorative line;
- one color applied everywhere;
- one Home composition;
- aviation decoration;
- luxury-brand surface mimicry;
- custom typography that is not production ready.

---

# 11. Evidence boundaries

Concept exploration may proceed inside this corridor while these remain OPEN:

- exact production font families;
- large-text ledger adaptation;
- locale-date width;
- NAV-001 final navigation semantics;
- SEARCH-001 Home Search interaction structure;
- production palette;
- runtime/browser/native transfer;
- physical glare/night evidence;
- representative-pilot usability/brand perception.

The bottom-navigation region is explicitly allowed/preferred in the next Home concept despite NAV-001 remaining open.

---

# 12. Corridor gate

**Design Corridor: COMPLETE.**

The corridor contains no Round-1 visual dependency and does not close the listed OPEN product/runtime decisions.

Next allowed phase:
`Operational Geometry Contract`

Still prohibited:
- drawing a new Home/UI concept;
- selecting a production palette/font;
- promoting a Home-only motif to brand code.
