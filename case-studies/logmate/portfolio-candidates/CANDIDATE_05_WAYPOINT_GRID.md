# Candidate 05 — Waypoint Grid

Status: STATIC PORTFOLIO PROPOSAL

## 한 줄 개념

**비행기록을 `orientation → capture → review`의 waypoint로 배치하고, 반복 업무를 modular work zones로 조직하는 structured workspace.**

## Product boundary

- Product source: `yhappcom/logmate` latest `main`; `AGENTS.md` and `MASTER.md` read-only.
- Design source: `yhappcom/design-studio` latest `main`.
- Product-authored UI remains English; portfolio narrative is Korean.
- Manual-first, import-optional, local-first, cloud-minimal, Paper Logbook First, native + tablet/EFB PWA remain product constraints.
- Implementation existence is not promoted to product authority. MASTER OPEN items remain OPEN.

## Design thesis

Waypoint Grid treats the product as a set of stable work zones rather than a dashboard, strip system, horizon band, or single-focus canvas. Each zone has a clear job and can recompose by viewport without changing semantic identity. The grid is relational: record identity stays with its values, actions stay with their owning object, and ledger columns preserve their semantic boundaries.

## Visual language

- open neutral canvas with bounded work zones only where grouping/action ownership needs it;
- rectilinear modular rhythm with modest corner treatment, avoiding card-everything decoration;
- repeated waypoint-sized markers for progress/current work, not aviation-instrument mimicry;
- stronger structural rules in dense ledger surfaces, quieter boundaries on Home;
- Tablet/EFB uses navigation rail + primary grid + contextual utility rail; mobile collapses to one semantic column.

## Typography

Mature proportional sans is the default for authored UI. Production-ready monospace is reserved for confirmed operational roles such as flight identifiers, airport codes, clock/duration values and dense ledger cells. Exact family, fallback, TextScaler and Unicode resolution remain OPEN.

## Color / state

Light uses a low-chroma neutral canvas, deep navy text and limited blue action/current-location accent. Dark uses distinct near-black/navy surfaces and visible rule contrast rather than a simple inversion. Focus/current/invalid/pending/offline/failure/evidenced success/recovery must remain semantically distinct and may not rely on color alone.

## Home

Home is a compact operational overview: last-28-day context, small role/time readouts, recent flights and the next useful action. Tablet distributes these into a primary overview grid plus recent-flight work zone; mobile preserves semantic order in a single column. Statistics are context, not proof of a calculation engine.

## Add Flight

Add Flight uses a clear staged capture flow with a stable field grid. Tablet may expose a contextual quick-select utility rail; this is a design proposal only and does not close canonical source/persistence behavior. Invalid, pending, unknown outcome and recovery remain separate runtime authority states.

## View Logbook

The grid language becomes most literal in View Logbook but remains subordinate to the confirmed LogMate Standard contract: Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark, compact widths, left/start anchoring, sticky header, shared horizontal offset, 36px row rhythm, neutral totals hierarchy, landscape-only tablet/EFB contract. Zoom remains OPEN.

## Adaptive approach

Representative mockups cover Home, Add Flight and View Logbook in Mobile Light, Mobile Dark, Tablet/EFB Light and Tablet/EFB Dark (12 environment expressions). Tablet is an adaptive recomposition, not a scaled phone.

## Accessibility / content semantics

Visible hierarchy does not replace accessibility hierarchy. Runtime must verify semantic order, accessible name/role/state/action, focus visibility/not-obscured, target geometry, keyboard/pointer/touch behavior, status/recovery announcements and non-drag alternatives where applicable. Authored UI remains English while user/source Unicode is preserved as stress input.

## Difference from 01–04

- 01: record-strip / datum relationship.
- 02: horizon band / broad situational deck.
- 03: progressive focus / selective salience.
- 04: directional end-to-end flow.
- **05: modular waypoint grid / stable work-zone architecture.**

## Trade-offs / risks

A modular grid can become a generic dashboard if every region is boxed. Utility rails may expose low-priority data merely because space exists. Compact grids can also overstate precision or implemented authority. Dark appearance is not evidence of cockpit/night suitability.

## OPEN validation

Resolved fonts/fallback/TextScaler/Unicode; native iOS/Android; served PWA and independent browser transfer; SafeArea/orientation/reflow; keyboard/pointer/touch; focus/history/recovery; high-contrast/forced-colors; screen reader/AT; physical glare/night; representative-pilot scan accuracy/completion/trust/workload; and FIELD performance remain OPEN.

## Canonical evidence paths

- `AGENTS.md`
- `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`
- `research/EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md`
- `research/EXTERNAL_ADVISORY_PACKAGE_TRACEABILITY_AUDIT_20260921.md`
- `case-studies/logmate/DESIGN_CORRIDOR_20260919.md`
- `case-studies/logmate/portfolio-candidates/README.md`

## PDF artifact

Korean portfolio PDF is generated as a chat artifact and includes the 12-environment concept board. It is a STATIC CONCEPT / PROPOSAL, not runtime/device/AT/human evidence.