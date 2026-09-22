# Candidate 02 - Horizon Deck

Status: STATIC PORTFOLIO COMPLETE / CONCEPT PROPOSAL / runtime-device-AT-human OPEN

## 한 줄 개념
한눈에 다음 비행을 준비하는 수평적 운영 데크.

## Design thesis
Candidate 01의 record-strip/datum 언어를 반복하지 않는다. Horizon Deck은 수평 band와 단계적 정보 노출을 핵심 구성 원리로 삼는다. Home은 orientation과 next action을 우선하고, Add Flight는 입력 단계와 field ownership을 분명히 하며, View Logbook는 Home 장식을 이식하지 않고 독립적인 dense scan surface로 유지한다.

## Visual language
- wide horizontal bands and open fields
- low container count; no card-everything grammar
- mobile = single vertical reading flow
- tablet/EFB = navigation field + work field recomposition, not scaled phone UI
- no cockpit/dial/altimeter control metaphor; horizon is a spatial hierarchy idea only

## Typography
Proportional UI typography for authored labels/prose/controls; mature mono only for confirmed operational roles such as flight identifier, airport code, clock/duration and ledger cells. Exact production families, fallback and TextScaler behavior remain OPEN.

## Color / state
Neutral light work field with restrained navy/blue hierarchy; dark uses separate surface/rule contrast rather than simple inversion. Accent is not allowed to collapse brand, focus, selection, success and sync into one semantic role. Exact production palette and physical night/glare behavior remain OPEN.

## Home
Orientation -> key time -> recent flights -> next action/navigation. Tablet/EFB uses sidebar plus a broad summary/work field and therefore materially recomposes the phone layout.

## Add Flight
Flight / Details / Summary task segmentation. Static controls do not imply persistence. Invalid, pending, unknown outcome, authoritative result and recovery remain distinct runtime contracts.

## View Logbook
Preserves current LogMate Standard semantics: Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark. Dense ledger remains left/start anchored and is not stretched merely to fill viewport. Decorative Home horizon language is not transferred into the ledger.

## 12-environment visual set
The portfolio render contains Home, Add Flight and View Logbook in:
1. Mobile Light
2. Mobile Dark
3. Tablet/EFB Light
4. Tablet/EFB Dark

Total: 12 environment-specific visual expressions. All are CONCEPT / PROPOSAL, not runtime screenshots.

## Adaptive approach
Semantic order is protected while wider viewports permit recomposition. Tablet is not a magnified phone. Fit pressure should trigger redistribution/reflow/recomposition before type distortion or semantic abbreviation.

## Accessibility / content
Product-authored UI remains English. User/source Unicode remains valid stress input. Color is never sole state carrier. Focus visibility, non-drag alternatives, accessible name/role/state/action, screen-reader order, enlarged text and supported high-contrast/forced-colors remain runtime/AT validation items.

## Differentiation from Candidate 01
Candidate 01 used flight-record continuity and datum alignment as the visual atom. Candidate 02 instead uses broad horizon bands, orientation hierarchy and progressive disclosure. It intentionally avoids inheriting Candidate 01's strip/datum composition.

## Trade-offs / risks
- horizon imagery/bands can become decorative aviation theming if overused;
- Home summary can overstate statistics relative to actual workflow;
- dark visual calm is not evidence of cockpit/night optimization;
- tablet information abundance can encourage unnecessary exposure merely because width exists.

## OPEN validation
Resolved fonts/fallback, TextScaler/Unicode, native and served-PWA reflow, tablet portrait/landscape, keyboard/pointer/touch, route/history/focus/recovery, high-contrast/forced-colors, screen reader, physical glare/night, representative-pilot scan accuracy/completion/trust/workload and FIELD performance all remain OPEN.

## Provenance
Product source: `yhappcom/logmate` current `main`, especially `AGENTS.md` and `MASTER.md`; LogMate is READ-ONLY for this work.

Design source: `yhappcom/design-studio` current `main`, especially `AGENTS.md`, `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`, `case-studies/logmate/DESIGN_CORRIDOR_20260919.md`, and the portfolio-candidate index.

PDF artifact generated in chat: `LogMate_Candidate_02_Horizon_Deck_KR.pdf`. The rendered PDF was visually inspected after generation; all three pages rendered without clipping/broken Korean glyphs, and the portfolio board visibly contains all 12 requested environment mockups.
