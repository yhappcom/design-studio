# LogMate Portfolio Candidate 06 - Timeline Stack

Status: STATIC PORTFOLIO PROPOSAL / runtime-device-AT-human-FIELD validation OPEN

## 한 줄 개념
시간이 쌓여 경력이 되는 개인 로그북: 현재 작업, 최근 기록, 누적 경력을 시간의 층으로 읽게 하는 temporal-stack 디자인.

## 제품 맥락 / 문제
LogMate는 개인 Pilot Logbook companion이며 종이 로그북을 대체하지 않는다. Manual-first, import-optional, local-first, cloud-minimal이며 native iOS/Android와 tablet/EFB PWA가 동등한 1차 타겟이다. Home 구현은 현재 presentation shell이고 canonical ledger/persistence/calculation engine은 아직 제품 구현 완료 상태가 아니다. 따라서 이 후보는 화면 존재를 데이터 authority로 오인하지 않는다.

## Design thesis
이전 후보의 record-strip, horizon-band, progressive-focus, directional workflow, modular grid를 반복하지 않는다. Timeline Stack은 flight record를 시간 순서의 사건으로 보고 `오늘/최근 -> 기간 맥락 -> 누적 경력`을 서로 다른 temporal layer로 조직한다. 사용자가 과거 기록과 현재 입력, 누적 결과의 관계를 빠르게 파악하는 것이 핵심이다.

## Visual language
- 수직/수평 timeline rhythm과 date marker를 구조적 cue로 사용한다.
- Home은 현재 시점에서 최근 기록과 누적 맥락으로 내려가는 시간층을 갖는다.
- Add Flight는 1 Flight -> 2 Details -> 3 Summary의 진행 sequence를 명시적으로 보여준다.
- View Logbook에서는 장식 timeline을 제거하고 confirmed compact ledger semantics를 우선한다.
- cockpit/instrument mimicry, card-everything, decorative aviation chrome은 피한다.

## Typography
Product-authored labels/navigation/instructions는 mature proportional sans를 전제로 한다. Operational identifier, airport code, clock/duration, dense ledger cell 등 확정된 operational role에만 production-ready monospace 후보를 제한한다. Exact family, resolved fallback, TextScaler, Unicode stress는 OPEN이다.

## Color / state
Light는 밝은 neutral canvas와 deep navy text, 제한된 blue action/current cue를 사용한다. Dark는 near-black/navy surface 단계와 rule contrast를 다시 설계한다. Focus/current/selection/invalid/pending/offline/failure/evidenced success/recovery를 하나의 accent 의미로 합치지 않으며 color-only state를 금지한다.

## Layout / spatial system
Mobile은 단일 temporal stack으로 collapse한다. Tablet/EFB는 navigation rail + temporal summary + record table/secondary context로 recompose한다. Tablet은 phone 확대가 아니다. Fit pressure는 type distortion/semantic abbreviation보다 reflow, redistribution, recomposition, detail transfer로 해결한다.

## Interaction / recovery
Requested action, pending/unknown outcome, authoritative result, restored projection, recovery를 구분한다. Add Flight의 Next/Save 계열 affordance는 persistence success의 증거가 아니다. Unknown mutation outcome에 blind Retry를 기본값으로 두지 않는다. Route/history/focus restoration은 runtime OPEN이다.

## Home 적용
Home은 현재 날짜/최근 28일 context, recent flights, cumulative career context를 시간층으로 배치한다. 최근 flight list의 date marker가 temporal identity를 강화한다. Tablet은 sidebar와 wider recent-flight table, career context를 병렬화한다.

## Add Flight 적용
단계 progression을 명확히 하되 현재 product OPEN인 persistence/schema/source semantics를 닫지 않는다. Mobile은 one-step-at-a-time, Tablet은 primary form + supporting context를 사용한다. Validation/pending/unknown/recovery는 실제 runtime authority와 함께 검증한다.

## View Logbook 적용
LogMate Standard의 Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark 의미, landscape-only, compact width, start anchoring, sticky header, shared horizontal offset, 36px row rhythm, neutral totals hierarchy를 우선한다. Timeline motif는 ledger semantics를 침범하지 않는다. Zoom은 OPEN이다.

## Native + Tablet/EFB PWA adaptive
Mobile Light/Dark와 Tablet/EFB Light/Dark를 별도 composition으로 설계한다. Tablet은 navigation rail과 넓은 work canvas를 사용한다. PWA install/update/service-worker/storage durability/background behavior는 정적 시안으로 capability claim하지 않는다.

## Accessibility / content semantics
Visible hierarchy와 accessibility hierarchy를 동일시하지 않는다. Semantic order, accessible name/role/state/action, focus visible/not-obscured, target geometry, keyboard/pointer/touch, non-drag alternative, status/recovery announcement는 runtime/AT validation 대상이다. Product-authored UI는 English를 유지하며 source/user Unicode는 stress input으로 보존한다.

## Representative visual compositions
Portfolio visual board는 다음 12개 environment expression을 포함한다.
- Home: Mobile Light / Mobile Dark / Tablet-EFB Light / Tablet-EFB Dark
- Add Flight: Mobile Light / Mobile Dark / Tablet-EFB Light / Tablet-EFB Dark
- View Logbook: Mobile Light / Mobile Dark / Tablet-EFB Light / Tablet-EFB Dark

모든 시안은 CONCEPT / PROPOSAL이며 runtime screenshot이 아니다.

## 기존 후보와 차별점
01 Flight Strip Atlas는 record identity/datum, 02 Horizon Deck은 horizontal band, 03 Skyline Focus는 selective salience, 04 Compass Flow는 directional workflow, 05 Waypoint Grid는 stable modular work-zone을 중심으로 한다. 06 Timeline Stack은 temporal layering와 accumulated-career reading을 핵심으로 하며 이전 후보를 palette/font/radius 수준에서 변형한 것이 아니다.

## Trade-off / 위험
- timeline cue가 과도하면 professional logbook보다 activity feed처럼 보일 수 있다.
- career accumulation visualization이 실제 계산 engine이 존재하는 것처럼 오해될 수 있다.
- date marker가 ledger density를 침범하면 scan efficiency를 낮출 수 있다.
- Dark appearance는 cockpit/night suitability 증거가 아니다.
- Mobile View Logbook 표현은 canonical landscape-only runtime contract와 혼동되지 않아야 한다.

## OPEN validation
- resolved font/fallback/TextScaler/Unicode
- iOS/Android native exact runtime
- served PWA + independent browser
- SafeArea/orientation/reflow
- keyboard/pointer/touch/focus/history/recovery
- high contrast / forced colors
- screen reader / AT
- physical device glare/night
- representative pilot scan accuracy, completion, trust, workload
- FIELD performance with representative provenance-bearing RUM

## Canonical evidence / provenance
Product source (READ-ONLY): `yhappcom/logmate` latest main, especially `AGENTS.md` and `MASTER.md`.

Design source: `yhappcom/design-studio` latest main, especially `AGENTS.md`, `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`, external-advisory evidence/claim/traceability materials, relevant LogMate case-study research, and `case-studies/logmate/portfolio-candidates/README.md`.

Static evidence never upgrades runtime/device/AT/human/FIELD claims to PASS.