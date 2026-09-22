# Candidate 08 — Compass Quiet

Status: **STATIC PORTFOLIO COMPLETE — CONCEPT / PROPOSAL ONLY**

## 한 줄 개념

**조용한 집중 — 필요한 것만, 더 선명하게.**

## Product context / problem

LogMate는 종이 로그북과 공존하는 개인 Pilot Logbook companion이다. Manual-first, import-optional, local-first, cloud-minimal이며 iOS/Android native와 Tablet/EFB PWA가 동등한 1차 타겟이다. 구현 존재를 제품 결정으로 승격하지 않고 `yhappcom/logmate`의 `MASTER.md`를 제품 권한으로 사용한다.

Candidate 08은 01 record strip, 02 horizon band, 03 progressive focus, 04 directional workflow, 05 modular grid, 06 temporal layering, 07 folio metaphor를 변형하지 않는다.

## Design thesis

LogMate의 전문성은 aviation decoration이 아니라 정확한 operational information, 안정적인 hierarchy, 빠른 수기 입력, 종이 전사에 필요한 검토성에서 나온다. 따라서 **quiet utility / subtractive hierarchy**를 identity로 삼는다. 새 시각 구조물을 계속 추가하는 대신 불필요한 시각 신호를 제거하고, 현재 중요한 정보와 행동만 대비로 남긴다.

## Visual language

- low-chrome open canvas
- thin semantic rules
- 제한된 functional surface
- restrained action accent
- Home은 calm, Add Flight는 task-focused, View Logbook는 dense ledger로 서로 다른 density를 허용
- cockpit/instrument chrome, stock dashboard/card-stack, decorative aviation containers를 identity로 사용하지 않음
- 포트폴리오 표지의 aviation imagery는 concept framing일 뿐 runtime product surface 의존성이 아님

## Typography

- product-authored labels/navigation/instructions: mature proportional sans proposal
- operational identifier / airport code / clock-duration / dense ledger cell: mature production monospace 후보만 제한 사용
- arbitrary user/source text: fallback-safe proportional treatment
- exact production family/fallback/TextScaler/custom T021: **OPEN**
- blanket monospace, fixed character cells, negative tracking rescue: 제외

## Color / state

- Light: neutral-dominant bright canvas + dark text + restrained functional accent
- Dark: 단순 inversion이 아니라 surface/rule contrast를 재구성
- accent 하나에 brand + focus + current + success + sync 의미를 합치지 않음
- invalid/pending/offline/failure/unknown/success/recovery는 redundant cue와 explicit semantics가 필요
- calibrated night/glare/observer behavior: **OPEN**

## Layout / spatial system

### Mobile

single task column. 필요한 정보와 action만 높은 salience를 유지하고 secondary context는 낮은 visual mass로 후퇴한다.

### Tablet / EFB PWA

sidebar/navigation + wider work canvas로 recompose한다. 모바일 확대판이 아니다. 공간이 넓다는 이유만으로 낮은 우선순위 정보를 새로 노출하지 않는다.

Fit pressure는 typography distortion/semantic abbreviation보다 reflow → recomposition → detail transfer 순으로 해결한다.

## Interaction / recovery

- action은 owning object와 함께 위치
- static mockup은 Saved/Sync/persistence authority를 주장하지 않음
- pending, failure, unknown outcome, authoritative result, recovery를 collapse하지 않음
- Retry는 repetition이 안전한 authority에서만 허용
- focus/history/restoration/recovery behavior는 runtime evidence 전까지 **OPEN**

## Surface application

### Home

최근 기간 요약, recent flights, Add Flight를 짧은 scan path로 연결한다. 불필요한 dashboard ornament를 제거한다. Tablet은 left navigation + summary/work area + recent records로 recompose한다.

### Add Flight

Flight / Details / Summary 단계와 field ownership을 명확히 하되 field chrome을 최소화한다. Manual-first capture를 보존하며 persistence/sync 성공을 시안이 주장하지 않는다.

### View Logbook

현재 CONFIRMED LogMate Standard 의미와 landscape compact-ledger 계약을 우선한다. Date | Type | Reg | Flight | DEP | ARR | Block | Night | Inst | Remark 의미를 임의로 변경하지 않는다. header/body/totals semantic boundaries, sticky header, shared horizontal offset, 36px rhythm, neutral total hierarchy를 보존한다. Zoom은 **OPEN**이다.

Mobile View Logbook mockups are portfolio continuity studies only and do not change the production landscape-only contract.

## Representative visual mockups

PDF/portfolio board contains 12 environment expressions:

| Surface | Mobile Light | Mobile Dark | Tablet/EFB Light | Tablet/EFB Dark |
|---|---|---|---|---|
| Home | included | included | included | included |
| Add Flight | included | included | included | included |
| View Logbook | included* | included* | included | included |

`*` Mobile View Logbook is a visual-language continuity study, not a product-contract change.

## Accessibility / content semantics

- authored UI remains English
- arbitrary source/user Unicode remains a stress input
- semantic order is independent from visible layout
- accessible name/role/state/action, focus visible/not-obscured, target geometry, keyboard/pointer/touch, non-drag alternatives, status/recovery announcements require runtime/AT evidence
- color is never the only semantic cue

## Difference from prior candidates

01 record atom / datum; 02 horizon band; 03 salience zone; 04 directional sequence; 05 modular work zones; 06 temporal layer; 07 folio metaphor. Candidate 08 instead makes **subtractive hierarchy itself the authored identity**. It creates character by removing unnecessary signals rather than adding a new metaphor or container system.

## Trade-offs / risks

- subtraction can become generic or look unfinished if type/spacing/grouping execution is weak
- low chrome can weaken affordance if ownership is not explicit
- scenic aviation imagery in portfolio framing must not become a runtime dependency
- dark appearance is not evidence of cockpit/night suitability
- summary emphasis must not imply calculation/persistence authority that does not exist

## OPEN validation

- resolved font/fallback/TextScaler/Unicode
- iOS/Android native exact runtime
- served Tablet/EFB PWA + independent browser
- SafeArea/orientation/reflow
- keyboard/pointer/touch
- focus/history/recovery and failure/unknown authority
- high-contrast / forced-colors
- screen reader / AT
- physical glare/night/observer variation
- representative pilot scan accuracy, entry completion, paper transcription, trust, workload
- FIELD performance / provenance-bearing RUM

No runtime/device/AT/human/FIELD PASS is claimed.

## Canonical evidence / provenance

Product source (READ-ONLY):
- `yhappcom/logmate/AGENTS.md` — latest `main`
- `yhappcom/logmate/MASTER.md` — latest `main`

Design source:
- `yhappcom/design-studio/AGENTS.md`
- `progress/STATUS.md`
- `progress/TYPE_STATUS.md`
- `progress/COLOR_STATUS.md`
- `progress/LAYOUT_STATUS.md`
- `progress/WEB_STATUS.md`
- `progress/CONTENT_STATUS.md`
- `research/README.md`
- `case-studies/logmate/DESIGN_CORRIDOR_20260919.md`
- `case-studies/logmate/portfolio-candidates/README.md`

The current specialist pre-runtime stop rules are respected. Static mockups do not manufacture runtime, accessibility, device, field, or human evidence.

## PDF artifact

`LogMate_Candidate_08_Compass_Quiet_KR.pdf` generated as chat artifact. PDF source includes a representative portfolio board with all 12 required environment mockups. Rendered pages were visually inspected after generation for mockup presence, clipping, glyph rendering, hierarchy, Light/Dark differentiation, mobile/tablet recomposition, and readability.