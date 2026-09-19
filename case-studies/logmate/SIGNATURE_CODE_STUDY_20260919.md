# LogMate Signature Code Study — 2026-09-19

Status: **PHASE 5 COMPLETE — SIGNATURE CANDIDATES DEFINED / NEW UI CONCEPT GATE UNLOCKED**

Upstream authority:
- `INTEGRATION_PRINCIPLES_20260919.md`
- `DESIGN_CORRIDOR_20260919.md`
- `OPERATIONAL_GEOMETRY_CONTRACT_20260919.md`
- audited Evidence Map / Contradiction Register
- owner concept-phase clarifications

Purpose: identify repeatable LogMate-specific design behaviors that can create authorship across surfaces without becoming decoration, copying Round-1 concepts, or violating operational geometry.

A signature code is accepted for concept exploration only if it:
1. has a functional reason;
2. transfers across multiple major surfaces;
3. survives density changes;
4. does not depend on one color, one screen or one animation;
5. remains compatible with accessibility and runtime fallback;
6. does not require an unresolved product decision to be falsely closed.

---

# 1. Candidate SC-A — Calibrated Axis

## Definition

Repeated information is organized around deliberate semantic starts, ends and baselines. The axis may be visible or invisible; the **relationship** is the code.

Examples of transfer:
- Home Recent rows: stable Date / Flight / Route / duration relationships;
- View Logbook: canonical semantic column boundaries;
- Activity: stable comparison groups and repeated-row axes;
- Add Flight: controlled label/value and paired-field relationships;
- Customize/import: source → target → state/action relationships.

## Why it is LogMate-relevant

LogMate's professional character depends on records being easy to compare. Precision is therefore expressed through alignment discipline rather than decorative instrument styling.

## Critical constraint

Calibrated Axis does **not** mean:
- permanent rails;
- vertical rules everywhere;
- identical screen coordinates;
- copying Concept C;
- a visible “datum line” on every screen.

The strongest form of this code may be visually quiet.

## Disposition

**RETAIN AS PRIMARY SIGNATURE CANDIDATE.**

It transfers across all major surfaces and directly reinforces the product's operational function.

---

# 2. Candidate SC-B — Operational Dual Voice

## Definition

LogMate distinguishes interface language from operational record data through disciplined typographic roles:

- proportional UI voice for authored interface language;
- exact mono operational voice where comparison requires it;
- tabular proportional numerics where appropriate;
- fallback-safe proportional free text for Remark/Crew/source text.

Flight retains carrier + number/suffix zoning inside the mono role.

## Why it is LogMate-relevant

The distinction is functional and repeatable. The interface speaks normally; operational records read with calibrated regularity.

## Critical constraint

This is not:
- all-monospace styling;
- terminal aesthetics;
- aviation-instrument cosplay;
- permission to force arbitrary-language Remark into mono.

Exact production families remain OPEN.

## Disposition

**RETAIN AS PRIMARY SIGNATURE CANDIDATE.**

It is transferable and complements SC-A without requiring decorative motifs.

---

# 3. Candidate SC-C — Quiet Functional Boundary

## Definition

At rest, LogMate uses only the boundaries required to understand grouping and ownership. A boundary may become more explicit when interaction/state requires it: focus, selection, validation, ambiguity, recovery or active editing.

The recognizable behavior is:
**quiet by default, explicit when function demands it.**

## Transfer

- Home: sections can remain open/low-chrome while controls/states are clear;
- View Logbook: real grid/column boundaries remain because the ledger needs them;
- Activity: selected period gains local state ownership without turning the entire selector into decorative chrome;
- Add Flight: field/focus/error ownership becomes explicit when needed;
- Customize/import: state/provenance boundaries remain strong enough for safe editing.

## Critical constraint

Cannot rely on color alone. Cannot remove a boundary that is required for discoverability or state ownership.

## Disposition

**RETAIN AS SUPPORTING SIGNATURE CANDIDATE.**

It needs visual/runtime validation because excessive reduction can become ambiguous.

---

# 4. Candidate SC-D — Measured Transition and Recovery

## Definition

State changes are direct, local and proportionate to their consequence. When a truthful inverse exists, recovery is immediate and discoverable. Motion, if used, reinforces continuity rather than providing spectacle.

## Transfer

- Activity selection;
- Add Flight validation/editing;
- Customize reorder/toggle/reset;
- import ambiguity/commit/Undo;
- navigation/focus restoration.

## Critical constraint

- motion is never the sole state carrier;
- drag cannot become the identity while the required non-drag alternative is missing;
- browser lifecycle cannot masquerade as save/sync truth.

## Disposition

**RETAIN AS INTERACTION SIGNATURE CANDIDATE.**

This can contribute to LogMate authorship but should not be used as the only recognizable visual code.

---

# 5. Candidate SC-E — Home Bottom Dock

## Definition

A bottom-navigation region is present in the next Home concept, following current owner preference.

## Why it is not a brand signature yet

- NAV-001 remains open;
- landscape ledger may have a different navigation composition;
- exact destinations and persistence are unknown;
- a bottom bar is common platform grammar and therefore weak as distinctive identity by itself.

## Disposition

**USE AS HOME CONCEPT DIRECTION; DO NOT PROMOTE AS LOGMATE SIGNATURE CODE.**

Its styling may consume the actual signature codes, but the presence of the dock is not itself the brand.

---

# 6. Explicitly rejected signature shortcuts

## Always-visible rails / grooves / datum lines

Rejected as a required signature.
Reason:
- risks recreating Round-1/Concept-C language;
- confuses an alignment relationship with a decorative line;
- weak cross-surface fitness.

## Accent stripe / accent-everywhere system

Rejected.
Reason:
- easily collides with focus/selection/success/error semantics;
- too dependent on authored color.

## Global monospace

Rejected.
Reason:
- harms role differentiation;
- creates a technical costume rather than a functional data voice;
- unsuitable for arbitrary-language Remark/source text.

## Luxury-material styling

Rejected:
- black/gold;
- metallic;
- glass;
- watch-index/dial grammar;
- camera/luggage grooves;
- ornamental micro-rules.

Reason:
surface borrowing is not evidence of quality or product authorship.

## Aviation motif system

Rejected:
- runway;
- cockpit;
- altimeter;
- aircraft silhouettes as layout grammar;
- pilot-watch imitation.

Reason:
domain credibility must come from correct operational information and workflow.

---

# 7. Cross-surface transfer matrix

| Code | Home | View Logbook | Activity | Add Flight | Customize / Import | Result |
|---|---|---|---|---|---|---|
| SC-A Calibrated Axis | strong | intrinsic | strong | adaptable | strong | primary candidate |
| SC-B Operational Dual Voice | strong | intrinsic | strong | bounded | bounded/source-safe | primary candidate |
| SC-C Quiet Functional Boundary | strong | bounded by ledger grid | strong | strong | must stay explicit | supporting candidate |
| SC-D Measured Transition/Recovery | moderate | state-dependent | strong | strong | very strong | interaction candidate |
| SC-E Home Bottom Dock | Home-specific | not proven | not defining | not defining | not defining | surface direction only |

No candidate above has a production PASS. This matrix establishes conceptual transfer only.

---

# 8. Candidate signature stack for new concept generation

All new UI concepts should preserve the two primary codes:

1. **Calibrated Axis**
2. **Operational Dual Voice**

Concepts may vary in how strongly they express:

3. **Quiet Functional Boundary**
4. **Measured Transition and Recovery**

This creates room for materially different concepts without violating the integrated system.

The concepts must **not** vary by reintroducing rejected shortcuts.

---

# 9. How future concepts may differ

New concepts can be materially different by changing:
- macro hierarchy and section composition;
- spatial rhythm;
- proportion;
- surface visibility;
- typographic scale contrast;
- how SC-A is made perceptible without literal rails;
- how SC-C reveals state;
- amount and location of restrained brand expression;
- bottom-navigation visual integration;
- motion character within the interaction constraints.

They must not differ by changing product semantics or breaking operational geometry.

---

# 10. Required pre-review stress

Before owner aesthetic review, every concept must first pass:

- Flight wide/narrow carrier + variable number/suffix stress;
- canonical numeric date stress;
- DEP/ARR and registration stress;
- ordinary and cumulative duration stress;
- arbitrary-language Remark/source-text stress;
- baseline/enlarged text geometry review;
- focus/selection/error/recovery state review;
- Home + View Logbook + Activity + Add Flight transfer check.

A concept that fails these is rejected before aesthetic preference is considered.

---

# 11. Signature-code gate

**Signature Code Study: COMPLETE.**

Primary candidates:
- SC-A Calibrated Axis;
- SC-B Operational Dual Voice.

Supporting candidates:
- SC-C Quiet Functional Boundary;
- SC-D Measured Transition and Recovery.

Surface-specific owner direction:
- SC-E Home Bottom Dock — use in next Home concept, not a brand code.

The mandatory pre-design sequence is now complete:

`Evidence Map -> Contradiction Register -> Integration Principles -> Design Corridor -> Operational Geometry Contract -> Signature Code Study`

## Next allowed phase

**New UI concept generation from the visual white canvas.**

Requirements:
- do not seed from Round-1 A/B/C;
- do not treat Concept C as preference/baseline;
- include a Home bottom-navigation region by default;
- preserve current 7/28/90/Custom period realization without forcing repeated `Last`;
- stress arbitrary-language Remark as user/source text;
- preserve all operational geometry invariants before aesthetic review.
