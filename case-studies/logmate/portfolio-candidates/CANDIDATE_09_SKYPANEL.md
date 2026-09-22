# Candidate 09 — SkyPanel

Status: STATIC PORTFOLIO COMPLETE / CONCEPT PROPOSAL

## Thesis

SkyPanel treats each primary LogMate surface as one dominant operational canvas rather than a collection of cards, widgets, strips, timelines, folios, or modular zones. Home is a status-and-recent-flight canvas; Add Flight is a capture canvas; View Logbook is a ledger canvas.

This direction is materially different from Candidates 01–08. Its differentiation is structural, not palette/font/radius variation.

## Product boundary

- Product source: `yhappcom/logmate` latest `main`, READ-ONLY.
- Product authority: `MASTER.md`.
- Preserve Simple is Best, Paper Logbook First, Manual-first, Import-optional, Local-first, Cloud-minimal, Native + Tablet/EFB PWA and canonical semantics/customizable presentation.
- Product-authored UI remains English.
- Current Home data is a mock/presentation shell and must not be represented as calculation/persistence evidence.
- View Logbook keeps the confirmed LogMate Standard semantic projection and landscape-only compact-ledger contract. Zoom remains OPEN.

## Visual language

- Broad flat work surface rather than card-everything.
- Restrained rules and strong alignment.
- Shallow navigation around one primary canvas.
- Optional aviation editorial band is limited to Home and does not become cockpit chrome.
- Proportional sans for authored UI; operational identifiers, airport codes, clock/duration and dense ledger cells are the only intended monospace candidate roles. Exact production family/fallback/TextScaler remain OPEN.
- Light and Dark use separately designed semantic surfaces; Dark is not a simple inversion.

## Surface application

### Home

Mobile uses one continuous vertical canvas for 28-day context and recent flights. Tablet/EFB recomposes into sidebar + wide primary canvas. Mock values remain presentation-only.

### Add Flight

Mobile preserves a linear semantic field order. Tablet/EFB recomposes field pairs into a two-column work canvas. The concept does not claim persistence, Sync, or save-success authority.

### View Logbook

The visual language yields to the confirmed compact ledger: Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark, left/start anchoring, sticky header, shared horizontal offset, 36px row rhythm and neutral totals hierarchy. Mobile expressions are visual-language continuity studies only; the product contract remains landscape-only.

## 12-environment visual set

Home, Add Flight and View Logbook each include Mobile Light, Mobile Dark, Tablet/EFB Light and Tablet/EFB Dark: 12 environment-specific expressions total. Tablet/EFB is an adaptive recomposition, not a magnified phone.

## Accessibility / adaptive implications

Fit pressure should be solved through reflow, recomposition or detail transfer rather than type distortion or semantic abbreviation. Semantic order, accessible name/role/state/action, focus visibility/not-obscured, target geometry, keyboard/pointer/touch, status/recovery announcement and screen-reader order require runtime/AT validation.

## Trade-offs

A wide single canvas can create excess empty space on large viewports, and an editorial Home band can compete with operational content if over-emphasized. Dark appearance is not evidence of cockpit/night suitability.

## OPEN validation

Resolved font/fallback/TextScaler/Unicode; iOS/Android native; served Tablet/EFB PWA and independent browser; SafeArea/orientation/reflow; keyboard/pointer/touch; focus/history/recovery; high-contrast/forced-colors; screen reader/AT; physical glare/night; representative-pilot scan/completion/trust/workload; FIELD performance.

## Portfolio artifact

`LogMate_Candidate_09_SkyPanel_KR.pdf` — Korean portfolio narrative with English product-authored UI and 12 environment mockups. Visuals are CONCEPT / PROPOSAL, not runtime/device evidence.