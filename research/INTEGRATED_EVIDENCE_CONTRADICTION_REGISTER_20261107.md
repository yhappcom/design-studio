# Design Studio — 통합 증거·모순·OPEN 등록부

**기준:** 2026-11-07 · Design Studio main@3264d490e80e46121d515200bac24ba977e0360b · LogMate main@f4bcd2f7b7e77039e29653baa1cc93797673885b
**분류:** COORDINATOR CONTRADICTION REVIEW / ACTION REGISTER. 원본 증거 교체나 새로운 PASS가 아니다.
**상태:** RESOLVED = 해석/우선순위 해결; SCOPED = 서로 다른 범위의 규칙; SUPERSEDED = 오래된 주장; OPEN = 추가 근거 필요; BLOCKER = 특정 승격 금지.

## 1. 판단 우선순위

1. 저장소 운영: Design Studio AGENTS + canonical 전문분야 STATUS; coordinator는 전체 STATUS/통합 nav만 정합화.
2. LogMate의 현재 제품 기능·결정: **LogMate MASTER**와 그에 연결된 current specs; 과거 스냅샷과 mock/code가 이를 대체할 수 없다.
3. Design Studio 전문 근거: owning specialist의 최신 study + 자체 evidence; 9월 통합/외부 자문은 탐색/연결.
4. 제품 케이스·시안: proposal, static review, code-rendered owner aesthetic review, runtime, device, AT, human을 별도 단계로 기록.
5. CrewConnex 시장·파서 문서: 연구상 관측만; import 제품 정책·release 승인은 LogMate MASTER/Import contract에 따른다.

## 2. 현행 통합 등록부

| ID | 충돌·위험 | 현재 판정 | 적용 범위 및 우선권 | 닫기 위한 증거/행동 |
|---|---|---|---|---|
| DS-G01 | 전체 STATUS는 Web Stage 2, Content Stage 1, Color/Layout Stage 3 미진입이라는 오래된 상태 | **RESOLVED (문서 정합화)** | 2026-09-20 전문분야 상태 우선; Stage 3 PASS 아님 | 글로벌 STATUS 새 snapshot 발행; 향후 specialist 변경 시 coordinator sync |
| DS-G02 | 9월 external-advisory 개별 문서의 baseline commit이 서로 다름 | **SCOPED** | authorship provenance이며 동일 frozen baseline 주장 아님 | 외부 발송 시 package-level ref 하나 표기 |
| DS-G03 | 독립 연구 스트림 문서/ID 반복 | **OPEN process risk** | T090/C121/I108/L112/W121/CD127 정적 포화; R/T/A/H/F 미확보 | 다음 note는 new evidence/contradiction/transfer에만 생성 |
| DS-T01 | T021 custom glyph 완료 이전 spacing/kerning 또는 production font으로 승격 | **BLOCKER** | Type drawing → general spacing → residual kerning; mature-font 대조 | complete-source bounded drawing PASS 이후 순차 검증 |
| DS-C01 | 브랜드/selected/focus/saved/sync를 하나의 accent로 처리 | **RESOLVED rule / R OPEN** | semantic roles 구분 + non-color redundancy | light/dark/high-contrast/forced-colors에서 rendered state injection |
| DS-L01 | compact ledger 2D geometry를 모든 reflow/large-text에 고정 | **SCOPED / R OPEN** | dense ledger는 의미 유지한 2D scroll 가능; 주변 form은 별도 재구성 | 실제 max text/fallback/SafeArea/target/focus geometry 측정 |
| DS-I01 | “Save” press, 로컬 지속, 서버 sync, ambiguous outcome을 같은 결과로 노출 | **RESOLVED rule / R OPEN** | authoritative result 이전 성공 표현 금지; retry는 causally safe일 때만 | exact app failure injection, idempotent/unknown/recovery/reopen |
| DS-W01 | CI step 시작 전 실패를 테스트 FAIL이라고 기록 | **RESOLVED classification** | NON-EXECUTION; 성공적인 analyze/test/golden runtime evidence 별도 | 같은 source/build에서 runner 실행과 재현 결과 확보 |
| DS-W02 | Lighthouse/CI synthetic을 FIELD CWV로 분류 | **RESOLVED boundary / F OPEN** | LAB와 representative F 분리 | 대표성·출처 있는 RUM/aggregate 필요 |
| DS-U01 | static contrast/visual inspection으로 WCAG·AT·pilot UX PASS 선언 | **BLOCKER for promotion** | A/H는 독립 증거, WCAG는 해당 criterion별 실제 구현 검증 | screen reader + 대표 조종사 real tasks, 명시적 criteria |
| LM-P01 | 9월 LogMate pre-auth/local-only 설계 메모 vs 현행 Account-required Auth | **SUPERSEDED by product** | 2026-11-07 MASTER §0: Firebase UID account required; onboarding 선택 정확히 3개 | 과거 시안/포트폴리오의 auth/setup 상태 current-contract 재검토 |
| LM-P02 | auto sync/hotspot 추정 vs 현재 Manual Sync-only | **SUPERSEDED by product** | MASTER §0 + Sync contract: explicit Manual Sync, 단 승인된 제한 read-only change check는 별도 | 시안/문구에서 자동 payload sync 성공 암시 제거 |
| LM-P03 | 과거 최근 기간/월별 totals 표현 vs 최신 7/28/90-day rolling Activity | **SUPERSEDED / scoped** | MASTER의 2026-10-29 W-003; month/year totals는 별도 scope | Home mock fixture/period labels 업데이트 및 실제 계산과 비교 |
| LM-P04 | Home Totals 1 metric/가변 grid vs 2026-10-30 3-slot current contract | **SUPERSEDED / scope** | always three horizontal slots; initial Total Block/+ /+; empty +/+/+; eligible metrics 제한 | 01–10 static portfolio의 current-contract applicability 감사 |
| LM-P05 | Welcome/Auth UI를 브랜드 재설계 시안이 마음대로 변경 | **BLOCKER** | MASTER §0의 Welcome UI LOCKED와 Figma visual acceptance 별도 승인 | 명시적 owner direction 전에는 auth visual override 금지 |
| LM-P06 | portfolio 01 수동 교체 PDF 전달 vs canonical index 'reconciliation required' | **OPEN artifact gap** | 01 문서 존재; PDF chat artifact와 git source/metadata 정합화 없음 | PDF 존재/버전/source commit/검토 판정 및 01 index 수동 reconcile |
| LM-P07 | portfolio 02–10 'complete'와 GitHub의 PDF/render source 부재 | **SCOPED / OPEN reproducibility** | STATIC PORTFOLIO COMPLETE **기록**은 있으나 chat binary가 canonical source라고 증명되지 않음 | 9개 PDF·12 screen visual 실제 파일·해상도·문구를 재검증, 복구 가능한 artifact manifest |
| LM-P08 | 01–10에서 서로 다른 디자인 설명 vs 실제 시각·공간 독립성 | **OPEN evaluation** | concept naming은 evidence가 아님; 2026-09-20 Home code candidate 번호와 별개 | 동일 화면/데이터/viewport 세트에서 blind comparative similarity/contract review |
| LM-P09 | 모바일 portrait View Logbook concept vs current landscape-only product contract | **SCOPED with warning** | 일부 portfolio는 visual continuity study only; production screen approval 아님 | 출시 목표 화면·orientation contract와 screen taxonomy 분리 |
| LM-P10 | Home에 weather/airport/current flight/upcoming/unsaved derived metric이 시각 표시되는 일부 시안 | **OPEN scope/authority risk** | editorial 이미지는 actual operational feed/record calculation authority가 아님 | MASTER 현재 기능과 fixture 비교, unsupported data/control 제거 또는 concept-only 표시 |
| LM-P11 | current Search UI affordance vs 실제 personal-logbook Search 미구현 | **OPEN implementation** | LogMate MASTER current; I108 Search-001 gate | implemented Search route/results/error/return + same-build behavior evidence |
| LM-P12 | Home/View mock 계산을 실제 ledger result로 오인 | **OPEN acceptance** | MASTER current Core Logbook User-Facing Completion; 실제 기존 repository 일부 구현과 shell 구별 | real same-UID Add/Edit → aggregate → Home/View projection verify |
| CC-01 | PDC original 30 Date vs 31 groups | **SUPERSEDED** | C502/C546 기준 31 printed Date/31 structural groups | 외부 요약·fixtures에서 30 주장 금지 |
| CC-02 | Skia crew leaf 26/32/4 vs 26/31/5 | **SUPERSEDED** | C540/C547 최신 leaf 분포; leaf ≠ crew persons | source version 표기; 개인/직무 자동 추론 금지 |
| CC-03 | CrewConnex tracked airlines 21 vs A1/A2 'confirmed' 20 | **RESOLVED scope** | 21 tracked = 20 A1/A2 + 1 B; pilot band는 19 rows | market report에서 분모 명시 |
| CC-04 | C532 original+55 strict tests done vs C512 21 original-derived PDFs strict path done으로 오인 | **OPEN exact test** | C532 real original bound done; C533 21 synthetic != C512 21 exact original-derived strict + independent renderer | G1 exact C512 replay with independent renderer |
| CC-05 | 43/43 Preview source links를 authenticated UID Flight binding으로 오인 | **BLOCKER** | source position value matches != same UID/year/publication/revision/active Flight | G2 authenticated source/owner/year/revision/coverage |
| CC-06 | CrewConnex BLH/crew를 canonical Block/Flight creation에 반영 | **BLOCKER** | source-only evidence; no auto Flight create/Block/total change | G3 evidence-only double CAS/receipt/rollback native tests; G4 lifecycle/G5 UI/G6 lawful transfer |

## 3. 중복 연구 정리 원칙 (삭제 금지)

- 상세 근거는 owning domain 원본과 roster C### artifacts에 그대로 남긴다. 요약 문서는 링크와 current decision만 유지한다.
- 정적 evidence stop 규칙을 교차 적용한다. 새 문서가 **독립 검증/새 원본/실행 반증**을 제공하지 못한다면 작성보다 실행 준비/실제 테스트를 선택한다.
- 기존 연구와 다른 결론은 원문을 덮어쓰지 않고 SUPERSEDED/SCOPED/CONTRADICTION으로 관리한다.
- older brand/candidate snapshot은 provenance와 반례의 가치가 있으나 최신 MASTER를 자동 갱신하지 않는다.

## 4. 상태 전환 및 책임

| Gate | 소유 | 닫는 최소 근거 | 현재 |
|---|---|---|---|
| DS-G01 최신 전체 상태 | Coordinator | 전문분야 STATUS와 전역 상태 일치 | 이번 통합에서 문서 정합화, 이후 변경 감시 |
| Type T021 | Type | complete-source drawing review + spacing→kerning | OPEN |
| Cross-domain Stage 3 | Type/Color/Layout+Interaction/Web/Content | one exact-build shared runtime packet + replication + necessary transfer | OPEN |
| Portfolio 01–10 reproducibility | Design coordinator + owner as needed | 동일 provenance로 원본 mockup/PDF 복구 및 12환경 artifact inspection | OPEN |
| LogMate product application | LogMate product owner/engineering | MASTER versioned acceptance; authorized runtime | OPEN by feature |
| CrewConnex production import | LogMate product/engineering | G0–G6 applicable evidence and explicit approval | OPEN |
| Accessibility / human | subject experts and representative pilots | A/H evidence bound to shipped behavior | OPEN |

## RELATED DOMAIN CHECK

Type T090, Color C121, Layout L112, Interaction I108, Web W121, Content CD127, cross-cutting external advisory 15 claims, LogMate Design Corridor/portfolio and current MASTER, roster Nov 7 research/evidence register를 교차 대조했다. 본 파일은 static conclusions를 다시 작성하는 연구가 아니라 **버전-권한-수용 기준의 contradiction review**이다.

## HANDOFFS TO OTHER SPECIALISTS

- 모든 분야: DS-G01 정합화 이후 최신 evidence 상태 변경을 coordinator에게 전달.
- Type/Web: exact family/fallback/TextScaler evidence; Color/Layout/Interaction/Content: 한 화면 state ownership/geometry/copy parity 공동 테스트.
- LogMate: LM-P01–12는 **제품 권한 확인/검토 제안**이며 해당 repo 수정/기능 승인 아님.
- CrewConnex: CC-01–06은 Nov 7 canonical roster synthesis/implementation gate를 링크; 원본 PDF·personnel은 이 통합본에 복제하지 않음.
