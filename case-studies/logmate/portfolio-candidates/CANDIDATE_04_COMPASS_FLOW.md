# Candidate 04 — Compass Flow

Status: STATIC PORTFOLIO PROPOSAL / runtime-device-AT-human validation OPEN

## 한 줄 개념
복잡한 로그북을 `Orient → Capture → Build → Review`의 방향성 있는 작업 흐름으로 재구성한다.

## 제품 맥락
- Product source: `yhappcom/logmate` current `main`의 `AGENTS.md`, `MASTER.md`를 READ-ONLY로 사용한다.
- LogMate는 개인 Pilot Logbook companion이며 paper logbook과 공존한다.
- manual-first, import-optional, local-first, cloud-minimal, Native + Tablet/EFB PWA를 보존한다.
- implementation 존재를 product decision으로 승격하지 않는다. MASTER의 OPEN은 OPEN으로 유지한다.

## Design thesis
Compass Flow는 이전 후보의 record-strip, horizon band, progressive-focus를 반복하지 않는다. 핵심은 **directional workflow**다. 사용자가 Home에서 현재 위치와 다음 행동을 파악하고, Add Flight에서 입력을 단계적으로 capture하며, View Logbook에서 누적 결과를 review하는 흐름을 하나의 명확한 방향성으로 연결한다.

## Visual language
- open canvas + 명확한 directional cue + 제한된 functional surface
- 항공 계기판/cockpit chrome을 모사하지 않는다.
- Home은 orientation과 next action, Add Flight는 capture/build, View Logbook는 review에 맞게 서로 다른 밀도를 사용한다.
- 태블릿/EFB는 navigation rail + primary workspace + contextual side field로 재구성하며 모바일 확대판으로 만들지 않는다.

## Typography
제품 authored UI는 English. mature proportional sans를 UI/labels/instructions에 사용하고 operational identifier, airport code, clock/duration, dense ledger cell만 production-ready monospace 후보로 제한한다. 정확한 family/fallback/TextScaler는 OPEN.

## Color / state
Light는 neutral bright canvas와 deep navy text, 제한된 blue action accent를 사용한다. Dark는 near-black navy surface 계층과 분리된 rules를 사용한다. Color는 semantic truth가 아니며 focus/current/invalid/pending/offline/failure/success/recovery를 하나의 accent 의미로 합치지 않는다.

## Layout / spatial
- Mobile: single directional task stream.
- Tablet/EFB: navigation rail + work canvas + contextual next-action/summary field.
- Fit pressure는 intrinsic room → redistribution → wrap → recomposition/detail transfer 순으로 처리한다.
- View Logbook의 confirmed compact ledger는 content START에 고정하고 viewport를 채우기 위해 column을 임의 확장하지 않는다.

## Interaction / recovery
requested action, pending/unknown outcome, authoritative result, restored projection, recovery를 구분한다. Retry는 현재 authority가 반복 실행을 안전하게 허용할 때만 사용한다. navigation/back/focus restoration은 runtime validation 대상이다.

## Home 적용
Home은 최근 28일 orientation, recent flights, next action을 한 흐름으로 묶는다. 통계를 장식 dashboard로 만들지 않고 다음 작업으로 연결되는 context로 사용한다.

## Add Flight 적용
Flight → Details → Summary 단계는 capture/build 방향을 명확히 한다. static concept은 persistence success를 주장하지 않는다. invalid/pending/failure/unknown/recovery는 실제 ledger/repository contract와 함께 검증한다.

## View Logbook 적용
LogMate Standard의 confirmed semantic projection과 landscape compact-ledger 계약을 우선한다. directional visual language는 ledger boundary와 totals hierarchy를 침범하지 않는다. Zoom은 OPEN.

## Native + Tablet/EFB PWA adaptive
Home/Add Flight/View Logbook 각각 Mobile Light, Mobile Dark, Tablet/EFB Light, Tablet/EFB Dark를 concept mockup으로 제시한다. Tablet은 sidebar/context field를 가진 재구성이다. PWA install/update/offline/storage/background behavior는 이 static candidate의 evidence가 아니다.

## Accessibility / content semantics
visible hierarchy와 accessibility hierarchy를 동일시하지 않는다. semantic order, accessible name/role/state/action, focus visibility/not-obscured, target geometry, non-drag alternatives, status/recovery announcements는 runtime/AT validation 대상이다. authored UI는 English이며 user/source Unicode는 보존한다.

## 기존 후보와 차별점
- 01 Flight Strip Atlas: record identity/datum 중심이 아님.
- 02 Horizon Deck: 수평 band/overview 중심이 아님.
- 03 Skyline Focus: selective salience 자체보다 end-to-end directional workflow를 디자인 원리로 사용.

## Trade-off / 위험
- directional metaphor가 과하면 불필요한 navigation chrome이 될 수 있다.
- next-action emphasis가 사용자의 자유 탐색을 약화할 수 있다.
- tablet context field가 낮은 우선순위 정보를 단지 공간이 있다는 이유로 노출할 위험이 있다.
- Dark appearance는 cockpit/night suitability 증거가 아니다.

## OPEN validation
Resolved font/fallback/TextScaler/Unicode, iOS/Android native, served PWA, SafeArea/orientation, keyboard/pointer/touch, focus/history/recovery, high-contrast/forced-colors, screen reader/AT, physical glare/night, representative pilot scan/completion/trust/workload, FIELD performance는 모두 OPEN.

## Representative screen compositions
최종 포트폴리오에는 Home, Add Flight, View Logbook 각각 Mobile Light/Dark + Tablet/EFB Light/Dark = 12 environment-specific concept mockups를 포함한다. 모든 mockup은 `CONCEPT / PROPOSAL`이며 runtime screenshot이 아니다.

## Canonical evidence paths
- `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`
- `research/EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md`
- `research/EXTERNAL_ADVISORY_PACKAGE_TRACEABILITY_AUDIT_20260921.md`
- `case-studies/logmate/DESIGN_CORRIDOR_20260919.md`
- `case-studies/logmate/portfolio-candidates/README.md`

## Evidence boundary
이 후보는 static design proposal이다. runtime/device/AT/human/FIELD PASS를 주장하지 않는다.
