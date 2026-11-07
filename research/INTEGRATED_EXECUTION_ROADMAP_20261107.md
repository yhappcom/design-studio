# Design Studio — 통합 실행 검증 로드맵 및 연구 운영 규칙

**기준:** 2026-11-07 · Design Studio main@3264d490e80e46121d515200bac24ba977e0360b · LogMate main@f4bcd2f7b7e77039e29653baa1cc93797673885b
**유형:** COORDINATOR EXECUTION PLAN / PROPOSAL — 본 문서 자체는 실행 결과·예약작업 변경·LogMate write authorization이 아니다.
**관련:** [마스터 종합](INTEGRATED_MASTER_SYNTHESIS_20261107.md), [증거·모순 등록부](INTEGRATED_EVIDENCE_CONTRADICTION_REGISTER_20261107.md), [LogMate 적용 지도](../case-studies/logmate/PRODUCT_APPLICATION_EVIDENCE_MAP_20261107.md).

## 원칙

- 각 회차를 파일 수/연구 ID로 평가하지 말고 **이전의 OPEN을 닫거나 분명하게 좁힌 실질 증거**로 평가한다.
- 하나의 exact build/fixture에서 여러 분야가 공동으로 결과를 수집한 뒤 owner별 판단을 분리한다.
- 설계 계약과 제품 정책의 충돌이면 먼저 현행 LogMate MASTER를 읽고 제품 owner 결정을 요청한다.
- 실제 실행이 불가능하면 NON-EXECUTION으로 분류하고 재현 조건/차단 이유를 기록한다. 우회하여 PASS를 만들지 않는다.
- human/AT/physical-device/FIELD는 독립 evidentiary tier. static-only를 해당 tier로 승격 금지.
- 본 로드맵은 기존 사용자 승인 예약업무의 시간/횟수/활성화를 직접 변경하지 않는다.

## 실행 순서와 최소 산출물

| 순서 | 목표/담당 | 완료 증거 | FAIL/HOLD 조건 |
|---|---|---|---|
| P0 — Coordinator 통합 메타데이터 | STATUS 최신화, index/등록부 연결, source HEAD 고정 | 글로벌 STATUS 일치; open register + provenance | specialist 변경을 덮어쓰거나 과거를 조용히 삭제 |
| P1 — Product contract reconciliation | LogMate owner/DS coordinator | 2026-11-07 MASTER 기준 화면·상태·기간·sync·setup 차이 판정 | mock UI가 확정/구현이라고 주장 |
| P2 — exact-build shared execution | Web execution + five domain reviewers | source/commit/build/toolchain + analyze/tests + twice reproduced native scenario | CI runner 미실행, 불명확한 fixture/provenance |
| P3 — adaptive & platform transfer | Type/Color/Layout/Interaction/Content/Web | light/dark, mobile/tablet, max text/fallback, safe area, high contrast; second native; served PWA/independent engine | 같은 스크린샷 반복, viewport 확대만, 플랫폼별 authority 불일치 |
| P4 — accessibility / device / people | External AT/HCI + product owner | real AT output, physical offline/night/glare, representative pilot tasks and sampling | simulated human, screenshot WCAG claim, lab as FIELD |
| R — CrewConnex parser G0–G6 | Roster research + separately authorized LogMate engineering | source family/strict parser test; owner authentication; evidence-only atomic CAS; lifecycle/release | 본인/연도/개정판 미확인, Flight/Block 자동 변경, PDF 일반화 |

P2–P4의 실행은 LogMate 별도 Work/권한 및 실제 소스 접근이 필요하다. 통합 문서를 만드는 이번 작업은 P0만 수행한다.

## 공통 test/observation 패킷 (W120 + T089/C120/I107/L111/CD126 통합)

필수 필드:
- PRODUCT REF: MASTER commit/절, 승인된 feature scope, scenario ID, trace ID.
- BUILD: exact repo HEAD, branch, dependency lock, device runtime/build hash, app mode, test runner executed status.
- PLATFORM: iOS/Android/served Flutter Web engine/version, phone/tablet layout, viewport/insets/orientation, locale/appearance, network/offline/standalone state.
- TYPE: requested and resolved family, fallback events, actual TextScaler, string corpus incl. ID/date/Unicode, truncation/line breaks.
- COLOR: focus/current/selected/invalid/pending/offline/failure/evidenced success/recovery semantic ID, non-color cue after transform.
- SPATIAL: target/focus rectangles, clipping/occlusion, sticky/header/ledger shared offsets, reading/action order, local scroll.
- INTERACTION: route/history/navigation, keyboard/touch/pointer/IME, requested action→authority/unknown→recovery, idempotency/replay.
- CONTENT/AT: actual visible text, accessible name/role/state/value/announcements, matching semantic action and result.
- DATA: owner UID, masked record/source IDs, ledger/revision/operation/receipt/dedup/checkpoint status, negative no-write assertion when applicable.
- EVIDENCE TIER: S/R/T/A/F/H; observed PASS/FAIL/HOLD/NON-EXECUTION, reproducibility and reviewer.

민감 개인자료/crew names 및 비공개 원본을 Design Studio에 복제하지 않는다. 검증에는 privacy-safe abstracted manifest/trace만 남긴다.

## 대표 시나리오(하나의 build로 여러 분야 동시 평가)

1. **Auth/setup**: startup gate → signed-out Welcome → email existing/new branch → verified UID → initial three choices, zero/unset/Previous Total, fail-closed wrong owner. 실제 구현된 분기만 실행.
2. **Home/View Add/Edit**: 실제 동일 UID Flight → invalid→correct→commit→route/reopen → Home/View totals/projection → cancel/failure/unknown outcome and recovery. No duplicate record.
3. **Customize**: 0–3 slot; add/replace/remove/non-drag reorder/Undo; duplicate metric+scope reject, missing vs 0, focus/position restoration; config sync는 production Manual Sync 구현 때만.
4. **Search**: query A→B late A reject→results→record→Back restore. Current Search not implemented => BLOCKED, no synthetic closure.
5. **PWA offline and theme/adaptive**: supported Tablet/EFB PWA Light/Dark, portrait/landscape, keyboard/pointer, max text, Unicode source, service worker/update/storage, explicit Manual Sync; no automatic payload sync.

모든 시나리오에서 정상·실패·결과 불명·복구를 분리한다. 원본 프로토타입 PASS는 동일 구현의 복제 증거가 아니다.

## Gate / 실행 순서의 구체적 판정

A. exact-source analyze/relevant widget+golden+accessibility tests: successful runner 수행이 evidence; pre-runner CI stop은 NON-EXECUTION.
B. primary native app same-build twice: 실제 authority/geometry/strings/focus trace를 반복 확보.
C. failure/unknown/recovery injection + max scaling/fallback/light-dark/narrow/SafeArea; 치명적 state loss면 FAIL.
D. second native platform과 served Flutter Web independent engine: portability claim에 필요한 기능/환경만 비교.
E. physical device/EFB PWA/offline/AT/human: sampling, limitations, residual OPEN 기록.
F. FIELD performance: representative RUM/aggregate가 확보된 경우에만 F로 분류; synthetic만 있으면 LAB.

## 포트폴리오 01–10 실무 정리

1. GitHub 문서 10개와 chat-delivered PDF 메타데이터를 manifest화. 01은 status reconcile. PDF가 repo에 없으면 absent/remote chat artifact로 정직하게 표시.
2. 12환경의 **실제** 화면 mockup 확보 여부/해상도/텍스트/clip/fake value/접근성·태블릿 recomposition을 확인. 같은 보드 한 장을 여러 페이지로 재인용한 것도 분명히 표기.
3. 현행 MASTER 기반 canonical scenario fixture를 별도로 만들고 각 후보의 semantic deviation을 조목조목 기록.
4. 독립성을 색/아이콘/사진만으로 측정하지 말고 spatial grammar, data hierarchy, interaction, adaptive behavior로 평가.
5. 정적 후보는 KEEP FOR EXPERIMENT / REWORK / REJECT 정도로 판정. 최종 production 시각 승인과 혼동 금지.

## CrewConnex 연구를 별도로 운영할 이유

파서 시장/물리 source 분석은 그래픽 디자인 Stage와 다른 acceptance 체계다. 2026-11-07 [roster synthesis](../case-studies/logmate/market-research/roster-systems/RESEARCH_SYNTHESIS_20261107.md)와 [readiness](../case-studies/logmate/market-research/roster-systems/IMPLEMENTATION_READINESS_20261107.md)를 기준으로 단위 실행:
- G1 exact C512 original-derived 21 strict parser+independent renderer 재현 (C532 original+55는 이미 done).
- G2 source operational year/subject+UID/revision/unique active flight 인증 및 August comparator coverage.
- G3 evidence-only source snapshot + dual CAS, append-only receipt, rollback/crash/reopen; canonical Flight/Block/total mutation = 0.
- G0/G4/G5/G6 source family/lifecycle/UX/lawful format transfer를 별도로 확인.
- 증거 불충분 시 DETACHED_HOLD; 자동 Date/crew/PIC/SIC/Block 추정 금지.
- 같은 tiny question을 여러 예약 회차에 쪼개지 말고 관련 source/strict test/persistence validation을 하나의 connected high-information-gain cycle로 결합.

## 새 연구 시작/중단 decision table

| 조건 | 결정 |
|---|---|
| 이미 존재하는 static claim의 재진술만 가능 | STOP: 기존 canonical 링크 사용 |
| 새 source, counterexample, verified material contradiction | OPEN bounded research; falsification test 명시 |
| exact code runtime과 이전 static claim의 충돌 | TRANSFER VALIDATION 또는 REVISIT, owner에 handoff |
| verified negative product test | FAIL scoped, 수정/재검증; 전체 Stage 자동 재설정 금지 |
| runner 미기동 / 원본 접근 없음 | NON-EXECUTION / BLOCKED. PASS나 FAIL로 변환 금지 |
| 제품 정책 OPEN, 구현 가능하지만 방향 미확정 | owner decision 필요 범위만 HOLD; 나머지 독립 검증 진행 |
| 실사용·실기기 증거가 없음 | A/F/H OPEN 보존 |
| 동일 기능이 이미 구현된 근거 확인 | 재구현 금지, gap/기능 연결/실제 acceptance 우선 |

## 1-cycle 보고 규격

- 검증 기준과 exact source/build; 오늘 새로 확보한 **실제** evidence.
- 바뀐 claim/OPEN ID와 영향받는 제품 surface.
- PASS/FAIL/HOLD/NON-EXECUTION + 재현 조건, negative no-write/authority 검증.
- 다른 전문분야로의 HANDOFFS; 다음 가장 큰 정보이득의 **연결된** 실행 패킷.
- commit/file diff summary. 주기적인 상태만 확인한 경우 연구 완료를 주장하지 않는다.

## RELATED DOMAIN CHECK

Type T089/T090, Color C120/C121, Layout L111/L112, Interaction I107/I108, Web W120/W121, Content CD126/CD127, cross-cutting UX and external review, product MASTER, CrewConnex G0–G6. 공통 실행 패킷은 중복 연구가 아니라 peer-source evidence의 **독립 transfer falsification**을 목표로 한다.

## HANDOFFS TO OTHER SPECIALISTS

- Web: shared run packet/orchestration/transfer/FIELD boundary.
- Type/Color/Layout/Interaction/Content: 각각 해당 runtime observation을 자신의 canonical study로 reconcile, 새 계약 무단 생성 금지.
- Product owner: LogMate 변경/디자인 최종 승인/출시 판단은 별도 권한과 release gate에서 진행.
- Roster researcher: G1/G2/G3 중심 실질 통합 사이클, source privacy boundary.
