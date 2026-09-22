# Candidate 07 - Folio Ledger

Status: STATIC PORTFOLIO PROPOSAL. Runtime/device/AT/FIELD/human validation remains OPEN.

## 한 줄 개념

**Paper-logbook-first를 시각적 구조로 번역한 digital folio:** dashboard보다 기록장에 가깝고, card stack보다 page/rule/margin/index를 중심으로 구성한다.

## 제품 맥락 / 문제

LogMate는 종이 로그북을 대체하는 finalized ledger가 아니라 기록·계산·검색·import·종이 전사를 지원하는 개인 Pilot Logbook companion이다. Manual-first, import-optional, local-first, cloud-minimal, Native + Tablet/EFB PWA, English-authored UI가 현재 제품 원칙이다. View Logbook의 confirmed Standard semantics와 paper-alignment page/total policy를 보존한다.

## Design thesis

이 후보는 01 record-strip datum, 02 horizon band, 03 progressive focus, 04 directional workflow, 05 modular waypoint grid, 06 temporal layering을 반복하지 않는다. 핵심은 **folio/page architecture**다.

- Home: dashboard가 아니라 현재 기간과 최근 기록을 보여주는 folio index.
- Add Flight: 하나의 새 기록을 작성하는 ruled entry sheet.
- View Logbook: paper transcription을 돕는 compact digital folio spread.
- Mobile: single folio page로 collapse.
- Tablet/EFB: left folio margin/index + primary sheet로 recompose.

종이 질감의 skeuomorphism을 복제하지 않고 margin, rule, folio number, page hierarchy만 구조적 단서로 사용한다.

## Visual language

- open warm-neutral sheet / charcoal night sheet
- 얇은 horizontal rules와 folio margin
- 낮은 corner-radius, 최소한의 bounded surface
- red-brown folio/index accent + restrained blue action accent
- scenic aviation hero, cockpit chrome, card-everything, oversized KPI dashboard를 배제

## Typography

Product-authored labels/instructions는 mature proportional sans를 전제로 한다. Flight identifier, airport code, clock/duration, dense ledger cell처럼 operational role이 확정된 영역에만 production-ready monospace 후보를 제한적으로 적용한다. T021 custom drawing, exact family/fallback, TextScaler/Unicode behavior는 OPEN이며 static candidate가 production font를 확정하지 않는다.

## Color / state

Light는 warm paper-neutral과 dark ink, Dark는 charcoal sheet와 warm light ink로 구성한다. Blue는 primary action/current navigation 보조, red-brown은 folio/index cue에 제한한다. Focus/current/invalid/pending/offline/failure/success/recovery는 hue 하나로 통합하지 않는다. Dark는 단순 반전이 아니며 rule/surface contrast를 별도 조정한다.

## Layout / spatial system

- Mobile: one-page reading order, start-edge margin, rule rhythm.
- Tablet/EFB: persistent folio margin/index + primary work sheet; mobile 확대판이 아니다.
- Home: 28-day period -> recent folios -> action.
- Add Flight: one entry sheet with stable field baselines.
- View Logbook: confirmed semantic columns, compact widths, shared horizontal offset, sticky header, 36px row rhythm, neutral totals hierarchy를 우선한다.

## Interaction / recovery

Visual continuity는 persistence authority를 뜻하지 않는다. Add Flight의 save/pending/unknown/recovery는 canonical ledger/repository가 실제 구현될 때 authority와 함께 검증해야 한다. Retry는 반복이 안전한 경우에만 사용한다. Focus/history/route restoration, keyboard/pointer/touch, non-drag alternatives는 runtime OPEN이다.

## Home 적용

Home은 통계 dashboard가 아니라 folio index로 취급한다. 28 Days / Block를 현재 folio context로 읽고 Recent Flights는 날짜 margin + route/time row로 표현한다. Total/career data는 구현·계산 authority가 없는 값을 성공적으로 계산된 것처럼 과장하지 않는다.

## Add Flight 적용

Flight entry는 ruled sheet다. Date / Flight / From-To / Aircraft / Block 등 canonical semantics를 안정된 baseline에 배치한다. Tablet은 두 field columns를 사용할 수 있지만 semantic order는 linear하게 유지한다. persistence success는 시안에서 주장하지 않는다.

## View Logbook 적용

LogMate Standard의 Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark semantics와 landscape-only compact ledger contract를 우선한다. Folio language는 margin/page cue와 rule rhythm에만 남고 ledger semantics를 장식으로 덮지 않는다. Page Total / Previous Total / New Total은 neutral hierarchy를 유지한다. Zoom은 OPEN이다.

## Native + Tablet/EFB PWA adaptive

Mobile은 single folio page, Tablet/EFB는 margin/index + work sheet로 recompose한다. Same domain input은 same semantic/calculation/projection 결과를 가져야 하며 adapter/responsive UI만 달라질 수 있다는 제품 원칙을 유지한다. Served PWA, independent browser, SafeArea/orientation, background/sync behavior는 static mockup으로 검증하지 않는다.

## Accessibility / content semantics

Visible hierarchy는 accessibility hierarchy를 대체하지 않는다. semantic order, accessible name/role/state/action, focus visibility/not-obscured, target geometry, keyboard/pointer/touch, status/recovery announcement, screen-reader reading order는 runtime/AT OPEN이다. Product-authored UI는 English를 유지하고 source/user arbitrary Unicode는 stress input으로 보존한다.

## 기존 후보와 차별점

Candidate 07은 데이터 시각화나 dashboard composition이 아니라 **paper transcription relationship을 page architecture로 승격**한다. 이전 후보의 strip, horizon, focus zone, directional flow, modular grid, timeline stack을 템플릿으로 사용하지 않는다.

## Trade-off / 위험

- folio metaphor가 강하면 종이 로그북 대체/법적 finalized ledger로 오인될 수 있다.
- warm paper surface가 generic productivity/notebook aesthetic으로 보일 수 있다.
- rule density가 enlarged text/reflow에서 과밀해질 수 있다.
- folio/page cue가 실제 page/Previous Total authority보다 앞서 보이면 잘못된 persistence/calculation 신뢰를 만들 수 있다.
- Dark appearance는 cockpit/night suitability evidence가 아니다.

## OPEN validation

- exact resolved font/fallback, TextScaler, arbitrary Unicode
- iOS/Android native + served Tablet/EFB PWA adaptive runtime
- landscape/portrait/SafeArea/narrow/reflow
- keyboard/pointer/touch, focus/history/recovery
- high-contrast/forced-colors and screen-reader/AT
- physical display/glare/night/observer variation
- representative pilot scan accuracy, entry completion, paper transcription support, trust/workload/discoverability
- FIELD performance / representative RUM

## Representative screen compositions

Portfolio visual includes 12 environment-specific expressions:

1. Home - Mobile Light
2. Home - Mobile Dark
3. Home - Tablet/EFB Light
4. Home - Tablet/EFB Dark
5. Add Flight - Mobile Light
6. Add Flight - Mobile Dark
7. Add Flight - Tablet/EFB Light
8. Add Flight - Tablet/EFB Dark
9. View Logbook - Mobile Light concept
10. View Logbook - Mobile Dark concept
11. View Logbook - Tablet/EFB Light
12. View Logbook - Tablet/EFB Dark

All are **CONCEPT / PROPOSAL**, not runtime screenshots. The canonical View Logbook product screen remains landscape-only; mobile logbook expressions are portfolio continuity studies and must not be read as a product-contract change.

## Canonical evidence / provenance

Product source (READ-ONLY):
- `yhappcom/logmate/AGENTS.md` @ latest main
- `yhappcom/logmate/MASTER.md` @ latest main

Design source:
- `yhappcom/design-studio/AGENTS.md`
- `progress/STATUS.md`
- `progress/TYPE_STATUS.md`
- `progress/COLOR_STATUS.md`
- `progress/LAYOUT_STATUS.md`
- `progress/WEB_STATUS.md`
- `progress/CONTENT_STATUS.md`
- `case-studies/logmate/portfolio-candidates/README.md`

Relevant current status boundaries: Type T090, Color C121, Interaction/Layout I108/L112, Web W121, Content CD127 all keep exact runtime/AT/device/human uncertainty open; static portfolio work does not promote those gates to PASS.