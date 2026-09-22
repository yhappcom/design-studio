# Candidate 03 - Skyline Focus

Status: STATIC PORTFOLIO PROPOSAL / runtime-device-AT-human OPEN

## 한 줄 개념

복잡함을 숨기고 현재 작업에 필요한 정보만 전면에 두는 **progressive-focus logbook**. Candidate 01의 record-strip/datum, Candidate 02의 horizon-deck와 달리, 정보의 양을 줄이는 것이 아니라 **현재 단계의 정보만 강하게 드러내고 나머지는 후퇴시키는 focus hierarchy**가 핵심이다.

## 제품 맥락과 보존 계약

- LogMate `MASTER.md`가 current product authority다.
- 개인 Pilot Logbook / Paper Logbook First / Manual-first / Import-optional / Local-first / Cloud-minimal을 보존한다.
- Native iOS/Android와 Tablet/EFB PWA는 동등한 1차 target이다.
- Product-authored UI는 English, user/source Unicode는 보존한다.
- 구현 존재를 제품 결정으로 승격하지 않는다.
- View Logbook Standard의 confirmed semantics와 landscape ledger contract를 보존한다.
- persistence/schema/sync conflict/zoom 등 MASTER OPEN은 닫지 않는다.

## Design thesis

조종사의 주의는 화면 전체에 균등하게 분산될 필요가 없다. Home에서는 최근 28일과 다음 행동, Add Flight에서는 현재 입력 단계, View Logbook에서는 현재 읽고 있는 ledger projection이 가장 높은 시각적 우선순위를 가진다. 나머지 정보는 삭제하지 않고 낮은 contrast/밀도/공간 우선순위로 후퇴시킨다.

## Visual language

- 큰 장식 카드 대신 한 개의 primary focus zone + 낮은 강도의 supporting zone.
- 둥근 게이지나 cockpit mimicry는 브랜드 장식이 아니라 summary focus를 보여주는 제한적 도형으로만 사용.
- mobile은 단일 focus stack, tablet/EFB는 sidebar + primary canvas + secondary insight rail로 재구성.
- View Logbook는 장식 언어를 억제하고 compact ledger의 semantic column boundary와 fixed-width behavior를 우선.

## Typography

Product-authored labels/navigation/instructions는 mature proportional sans를 전제로 한다. Operational identifiers, airport codes, clock/duration, ledger cells에는 production-ready monospace 후보를 제한적으로 사용한다. 정확한 family/fallback/TextScaler는 OPEN이며 custom type drawing을 production dependency로 가정하지 않는다.

## Color / state

Light는 white/near-white canvas와 deep navy text, 제한된 blue accent. Dark는 near-black navy canvas와 구분 가능한 surface 단계로 구성한다. Accent는 primary action/current navigation을 보조하지만 focus/success/sync를 동일 의미로 합치지 않는다. invalid/pending/offline/failure/unknown/recovery는 color-only가 아닌 text/icon/boundary redundancy가 필요하다.

## Home

Mobile: greeting -> 28-day focus -> compact supporting metrics -> Recent Flights -> primary Add Flight. Tablet: sidebar + large 28-day focus canvas + Recent Flights + secondary insight rail. Tablet은 phone 확대가 아니라 정보 역할을 세 영역으로 재배치한다.

## Add Flight

Flight / Details / Summary의 단계적 focus를 사용한다. 현재 단계만 높은 salience를 갖고, 다음 단계는 존재만 표시한다. 실제 persistence가 없는 현재 구현을 Saved/Sync success로 표현하지 않는다. validation ownership과 unknown mutation outcome/recovery는 runtime contract가 필요하다.

## View Logbook

Mobile concept는 검색/선택 진입을 간결하게 보여주는 companion projection이며, canonical View Logbook의 confirmed landscape-only compact ledger는 Tablet/EFB composition에서 중심 작업면으로 표현한다. Standard semantics, sticky header, 36px row rhythm, neutral total hierarchy, shared horizontal offset, compact column widths를 훼손하지 않는다. Zoom은 OPEN이다.

## Adaptive approach

- Mobile: single-focus vertical stack.
- Tablet/EFB: navigation rail + primary work canvas + optional secondary context rail.
- Fit pressure는 type distortion이나 semantic abbreviation보다 reflow/recomposition/detail transfer로 해결한다.
- Dark는 단순 inversion이 아니라 surface/rule/contrast hierarchy를 다시 설정한다.

## Accessibility / content semantics

Visible hierarchy가 accessibility hierarchy를 대체하지 않는다. semantic order, accessible names/roles/states/actions, focus visibility/not-obscured, non-drag alternatives, status/recovery announcements는 runtime/AT 검증이 필요하다. English UI와 arbitrary Unicode/source strings를 분리해 다룬다.

## 12 environment visual set

Home, Add Flight, View Logbook 각각에 대해 Mobile Light, Mobile Dark, Tablet/EFB Light, Tablet/EFB Dark concept mockup을 제작한다. 모든 mockup은 CONCEPT / PROPOSAL이며 runtime screenshot이 아니다.

## Candidate differentiation

- Candidate 01: record-strip/datum continuity 중심.
- Candidate 02: horizontal horizon deck와 넓은 운영 시야 중심.
- Candidate 03: **progressive focus / selective salience** 중심. 같은 데이터를 모두 동등하게 보여주지 않고 현재 task의 attention hierarchy를 설계한다.

## Trade-offs / risks

- focus zone이 과도하면 supporting information discoverability가 떨어질 수 있다.
- 28-day visual focus가 실제 제품 의미보다 통계를 과대평가할 수 있다.
- dark appearance가 cockpit/night suitability 증거로 오인될 수 있다.
- mobile View Logbook concept는 canonical landscape-only View Logbook contract와 혼동되지 않도록 runtime IA에서 명확히 구분해야 한다.

## OPEN validation

Resolved font/fallback/TextScaler/Unicode, native + served PWA reflow, SafeArea/orientation, keyboard/pointer/touch, focus/history/recovery, high-contrast/forced-colors, screen reader, physical glare/night, representative pilot scan accuracy/completion/trust/workload, FIELD performance는 모두 OPEN이다.

## Provenance

Product source: `yhappcom/logmate` latest `main`, `AGENTS.md`, `MASTER.md` (read-only).

Design source: `yhappcom/design-studio` latest `main`, `AGENTS.md`, `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`, relevant LogMate case-study research, portfolio candidate index.
