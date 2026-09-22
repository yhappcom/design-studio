# Candidate 10 — Field Deck

Status: **STATIC PORTFOLIO COMPLETE — CONCEPT / PROPOSAL ONLY**

## 개념

**Field Deck**은 LogMate를 조종사의 비행 전후 짧은 사용 세션에 맞춘 field-context operational workspace로 해석한다. Home은 상태 파악과 다음 기록 행동, Add Flight는 빠르고 정확한 수기 입력, View Logbook는 조밀한 검토를 담당한다.

이 후보는 앞선 후보들의 record strip, horizon band, progressive focus, directional flow, modular grid, timeline, folio, quiet utility, single-canvas를 템플릿으로 사용하지 않는다. 차별점은 **field context + readiness**를 primary thesis로 삼는 것이다.

## 제품 맥락 / 보호할 계약

Product authority는 `yhappcom/logmate` 최신 `main`의 `MASTER.md`다. LogMate는 READ-ONLY source로만 사용했다.

보존한 계약:
- Paper Logbook First
- Manual-first / Import-optional
- Local-first / Cloud-minimal
- Native + Tablet/EFB PWA
- English product-authored UI
- View Logbook LogMate Standard semantic projection
- landscape-only View Logbook, compact semantic widths, sticky header, shared horizontal offset, 36px row rhythm, neutral total hierarchy
- product OPEN decision은 시안이 임의로 닫지 않음

## Design thesis

현장 사용에서 사용자는 긴 탐색보다 현재 상태, 다음 행동, 빠른 기록, 검토를 짧게 반복한다. 따라서 Field Deck은 높은 정보 선명도, 얕은 navigation, 제한된 action accent, 넓은 tablet work area를 사용한다.

항공 사진/환경 이미지는 **optional editorial layer**다. 실제 weather, airport state, operational feed 또는 새로운 canonical data source를 의미하지 않는다.

## Visual language

- clear operational hierarchy
- shallow navigation
- broad tablet/EFB work area
- limited blue action cue
- low decorative chrome
- optional aviation/editorial context separated from authoritative data

## Typography

Product-authored UI는 mature proportional sans를 전제로 한다. Airport code, flight identifier, clock/duration, dense ledger cell처럼 operational scan role이 명확한 영역만 production-ready monospace 후보로 제한한다.

정확한 family/fallback, T021 drawing, TextScaler, arbitrary Unicode rendering은 OPEN이다.

## Color / state

Light와 Dark는 독립적인 surface hierarchy를 사용한다. Dark는 단순 색 반전이 아니다. Background / surface / rule / text / action contrast를 별도로 설계한다.

Pending, failure, unknown outcome, success, recovery는 하나의 blue accent로 합치지 않는다. Color-only semantic state는 허용하지 않는다.

## Layout / spatial

### Home
Mobile은 current context → key time → Add Flight → Recent Flights의 단일 흐름이다. Tablet/EFB는 left navigation + wide context/work area로 재구성한다.

### Add Flight
Mobile은 Basic → Details → Review를 단일열로 진행한다. Tablet/EFB는 동일 semantic order를 유지하면서 wider field composition으로 재배치한다.

### View Logbook
Tablet/EFB는 confirmed compact ledger가 primary work surface다. Mobile 표현은 portfolio visual-language continuity study이며 canonical landscape-only 계약을 변경하지 않는다.

## Interaction / recovery

Static concept은 저장 성공, sync 성공, offline authority, ambiguous outcome recovery를 주장하지 않는다. 실제 persistence/repository authority가 구현된 뒤 pending/failure/unknown/recovery를 연결해야 한다.

## Native + Tablet/EFB PWA adaptive

Tablet은 phone 확대가 아니다. Left navigation과 wide primary workspace를 사용한다. 실제 iOS/Android native와 served Tablet/EFB PWA에서 SafeArea, orientation, max text scaling, fallback, keyboard/pointer/touch, browser behavior를 검증해야 한다.

## Accessibility / content semantics

- product-authored UI: English
- semantic order와 visible order의 parity 필요
- accessible name/role/state/action 검증 필요
- focus visible / not obscured 검증 필요
- target geometry, keyboard/pointer/touch 검증 필요
- status/recovery announcement와 screen-reader order 검증 필요
- user/source Unicode 및 locale-sensitive rendering은 stress input으로 유지

## 12 environment mockups

| Screen | Mobile Light | Mobile Dark | Tablet/EFB Light | Tablet/EFB Dark |
|---|---|---|---|---|
| Home | included | included | included | included |
| Add Flight | included | included | included | included |
| View Logbook | included* | included* | included | included |

`*` Mobile View Logbook는 visual-language continuity study only. Product contract remains landscape-only.

Mockup board와 PDF는 모두 `CONCEPT / PROPOSAL`, `Not runtime evidence`로 표시했다.

## 차별점

Candidate 10은 field context와 readiness를 시각적/공간적 primary thesis로 둔다. 앞선 후보의 특정 layout template을 재사용하지 않는다. 특히 Tablet/EFB에서는 작업 전후 짧은 세션을 위한 left navigation + context/work surface를 사용한다.

## Trade-off / 위험

1. Aviation imagery가 실제 weather/airport operational authority를 암시할 위험.
2. 이미지가 과하면 전문 utility보다 lifestyle app처럼 보일 위험.
3. field-context emphasis가 Home mock/presentation shell의 값을 실제 계산 결과처럼 과장할 위험.
4. Dark appearance는 cockpit/night suitability 증거가 아님.
5. Wide tablet composition은 실제 reflow/text scaling에서 재검증 필요.

## OPEN validation

- resolved font/fallback/TextScaler/Unicode
- iOS/Android native runtime
- served Tablet/EFB PWA + independent browser
- SafeArea/orientation/reflow
- keyboard/pointer/touch
- focus/history/recovery
- high contrast / forced colors
- screen reader / AT
- physical glare/night/observer variation
- representative pilot scan, entry, paper transcription, trust, workload
- FIELD performance / representative RUM

## Canonical evidence / source refs

Product source:
- `yhappcom/logmate/AGENTS.md`
- `yhappcom/logmate/MASTER.md`

Design source:
- `yhappcom/design-studio/AGENTS.md`
- `progress/STATUS.md`
- `progress/TYPE_STATUS.md` — T090 pre-runtime stop rule
- `progress/COLOR_STATUS.md` — C121 runtime-evidence stop rule
- `progress/LAYOUT_STATUS.md` — I108/L112 pre-runtime stop rules
- `progress/WEB_STATUS.md` — W121 execution-priority gate
- `progress/CONTENT_STATUS.md` — CD127 semantic-evidence stop rule
- `case-studies/logmate/portfolio-candidates/README.md`

## Visual inspection

Final PDF was rendered to PNG at 180 dpi and all 3 pages were visually inspected. Checked: mockup presence, Korean glyph rendering, clipping, alignment, spacing, hierarchy, Light/Dark distinction, mobile/tablet adaptive distinction, and readable page composition. No blocking visual defect was found.

This is static portfolio evidence only. It does not create runtime/device/AT/FIELD/human PASS.