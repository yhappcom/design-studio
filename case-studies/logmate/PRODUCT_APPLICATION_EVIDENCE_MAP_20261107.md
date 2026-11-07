# LogMate — Design Studio 제품 적용 증거 지도

**기준:** 2026-11-07 · Design Studio main@3264d490e80e46121d515200bac24ba977e0360b · LogMate main@f4bcd2f7b7e77039e29653baa1cc93797673885b
**유형:** CASE-STUDY APPLICATION MAP / STUDIO ADVICE (제품 변경 승인/런타임 PASS 아님).
**경계:** 제품 진실은 LogMate MASTER 및 연결 current specs에서 읽음. Design Studio는 제안/근거/검증 계획만 저장. LogMate repository **write 금지**.

## 1. 계약 우선순위 및 2026-11-07 현재 보존 사항

[LogMate MASTER](https://github.com/yhappcom/logmate/blob/main/MASTER.md) 제품 권한:
- Firebase **account-required**, owner=Firebase UID, verified first use; Account-free/local-only 과거 논의는 superseded. 로컬 우선 저장과 계정 필수는 모순이 아니라 **인증/소유 vs 데이터 저장·오프라인 접근 범위**가 다른 계약.
- Apple / Google / Email+Password; Welcome UI LOCKED, Figma visual acceptance 별도. 실제 signed-out Welcome에 임의 행동/문구 추가 금지.
- 인증 뒤 setup 정확히 3개: Start a new logbook / Enter Previous Total / Import existing logbook. 이후 Import도 가능하되 production coordinator OPEN. 최초 제품 preview는 shipped 실제 기능 기반으로 **deferred**.
- Manual Sync only: 인증 사용자 명시 요청 전에는 payload Push/Pull/Apply 없음. 1회 경량 read-only change check의 한정 허용 범위와 background/automatic sync를 구분.
- Native Phone=Mobile, Native Tablet 및 지원 Tablet/EFB PWA=Tablet; Light/Dark 각 composition 내부. Desktop presentation V1 out of scope.
- Home Activity는 local-current-day inclusive 7/28/90 calendar-day windows (Operational Date Flight-only), 월·연간 조회와 의미가 다름.
- Home Totals Customize 가로 3슬롯, 최초 Total Block | + | +, 명시 empty + | + | +, 0–3 selected, semantic metric+scope and duplicate rule. 합산·zero/absent 및 scope authority와 일치해야 함.
- Canonical ledger와 projection은 실제 구현/현재 acceptance별로 구분. 현재 personal Search, production Import, production Manual Sync는 미완료 범위가 명시됨. Figma final과 임시 Flutter shell/fixture를 동일시하지 말 것.
- English product-authored UI; 사용자/원본 Unicode 값 및 locale-sensitive 날짜·숫자 stress는 보존. Paper Logbook First, 실제 기록/합계와 source evidence 구분.

## 2. 제품 표면 × 전문 연구 × 다음 증거

| 제품 표면 / 기능 | 확정된 제품 의미 및 OPEN | 적용할 Design Studio 연구 | 최소 실행 증거 / 주의 |
|---|---|---|---|
| Welcome/Auth | UID account-required, 3 peer auth, locked Welcome UI, verified session; provider acceptance 일부 OPEN | Type T090, Color C121, Content CD127, Interaction I108, Web W121 | Figma ↔ Flutter visual acceptance, actual identity/branch/errors/focus/large text; 예전 no-login proposal 금지 |
| Initial Setup/Previous Total | 3 choices, no-baseline ≠ 0, Previous Total 수정·reconcile; Import coordinator OPEN | CD119/127, I100/108, L104/112 | actual source-driven strings, zero/absent + mutation/cancel/recovery, baseline once, onboarding progress |
| Home activity | 7/28/90-day rolling, canonical Flight-only Operational Date | C121, Type T090, L112, CD127, W120 | same-build date boundary, 7/28/90 + month separate, correct local day, source/provenance for cards |
| Home Totals Customize | fixed 3 horizontal slots and eligible typed metrics; empty distinction; non-drag alternative | L112/I108, Color C121, CD127, Type T090 | max text/SafeArea, 0–3 states, reorder/focus/Undo/reload, actual totals, config Manual Sync integration OPEN |
| Add/Edit Flight | current domain/repo capabilities must be reused; authority of canonical record/receipt vs shell | I107, CD126, C120, L111, T089, W120 | invalid→correct→commit→failure/unknown→safe recovery; same UID/ledger; actual no duplicate mutation |
| View Logbook | canonical Standard semantic projection and dense ledger; landscape-only in current cited case | Type T090, Layout L112, I108, Content CD127 | date/type/reg/flight/DEP/ARR/block/night/inst/remark identity, shared offset, totals, large-text/2D scrolling/focus |
| Search/results | personal Search not implemented; visual search affordance is not closure | I108, L112, CD127, W121 | Query A→B supersession, zero/error/offline, result→record→Back context; ONLY after actual Search support |
| Import/review | source truth must not silently create inferred fields; production Import OPEN | I100/108, CD119/127, C121, Web W121 | preview, selection, uncertain field HOLD, duplicate resolution, batch rollback, accessible recovery; product contract priority |
| Local/Manual Sync & configuration | Local-first with UID; user-triggered Manual Sync; production path OPEN | I107, C120, CD126, W120 | Saved locally ≠ Synced, ambiguous result/idempotency, delta/cursor/revision/conflict, offline lifecycle; no auto payload assumptions |
| Tablet/EFB PWA | first-class tablet presentation, offline/service-worker/input/platform specific runtime OPEN | Web W120/121, Layout L111/112, Type T090 | served PWA, portrait/landscape, standalone/storage/update, keyboard/pointer/touch, independent browser, physical EFB |
| Accessibility/Human | WCAG 2.2 baseline; no actual product conformance/human pass claimed | All; HCI + AT external packets | screen reader & spoken status, non-drag/target/focus, pilot transcription/error/recovery task metrics |

## 3. 두 개의 Candidate 05/07 스트림을 분리할 것

**A. 2026-09-20 Home visual-only code candidate.** Frozen Home IA/data fixtures/operational columns. Code-first render, 390×844 Light/Dark, independent six-domain review, coordinator owner-aesthetic eligibility. [Protocol](CODE_FIRST_RENDER_REVIEW_PROTOCOL_20260920.md); [code candidate 05](candidate05/COORDINATOR_GATE_20260920.md); [code candidate 07](candidate07/POST_RENDER_REVIEWS_20260920.md). 이 계열의 C120/I107/L111/W120/CD126 런타임 시험 지시는 **이 코드를 뜻한다**. Aesthetic review PASS는 shipped runtime PASS가 아니다.

**B. 이후 전체 제품 포트폴리오 Candidate 01–10.** [인덱스](portfolio-candidates/README.md). Conceptual Home/Add Flight/View Logbook + Mobile Light/Dark, Tablet/EFB Light/Dark 총 12환경 시안 설명/대화 PDF. 02–10 static-complete 기록; 01 index reconciliation OPEN. 이 series의 05 Waypoint Grid와 07 Folio Ledger는 위 A의 05 Ivory Instrument/07 Linebook과 **다른 산출물**이다.

### 포트폴리오 현재 비교 가능성 감사

| 확인 항목 | 문서로 확인한 범위 | 남은 평가 |
|---|---|---|
| 번호/개념 문서 | 01–10 각 Markdown 존재 | 01 PDF 버전/source ref 정합화 |
| PDF | 02–10 대화 artifact 생성/검사되었다고 index 기록 | canonical GitHub에는 PDF binary/독립 renderer 재현 경로 없음. 접근 가능한 실제 PDF/PNG 확보 시 직접 재검증 |
| 12환경 | 각 파일에 선언·인덱스 완료 기록 | 실제 mockup 해상도/정확한 문자열/상태와 Tablet recomposition을 공통 시험표로 확인 |
| 차별성 | 개념 서술은 10개로 구분 | visual grammar+layout independence는 같은 화면·값·viewport로 cross-candidate 비교 필요 |
| 최신 제품과 정합성 | 다수가 paper-first/English/native+PWA 원칙 기술 | 현재 계정필수/3 setup/Manual Sync/Home 7·28·90/3-slot/locked Welcome 등 재대조 |
| runtime/AT/human | 모든 후보 static CONCEPT | PASS 없음, 새 실제 구현/원본 빌드가 필요 |

특히 포트폴리오의 scenic aircraft imagery, pilot greeting, weather-like field, unsupported current total, “saved” action, 모바일 portrait ledger는 컨셉 제안일 수 있지만 **실제 제품 기능/데이터**로 승격하면 안 된다.

## 4. cross-domain 적용 공동 시나리오

**S1 Account/setup:** signed out → provider → verified UID → choice → Previous Total / Import (구현 범위 분리) → Home. Type/Content의 실제 라벨, Focus/AT, Data source truth와 auth/session recovery.

**S2 Add/Edit ↔ projection:** real existing UID flight → Edit → cancel/commit → reopen → Home/View; invalid→correction→failure/unknown→safe Retry. 각각 authoritative persistence 여부가 관찰되어야 한다.

**S3 Customize:** 0/1/2/3 slots → Add/Replace/Remove → non-drag reorder → error/undo/reload → no-baseline distinction → cross-device config only when Manual Sync shipped.

**S4 Search:** A→B, late A discard, zero/error/offline, record/Back; 현재 product Search 미구현이므로 **BLOCKED**, mock UI로 실행 PASS 금지.

**S5 Responsive/PWA:** 동일 확인된 데이터·언어·상태를 Mobile Light/Dark와 Tablet EFB Light/Dark에 재배치; no card-for-card scaling, actual font fallback/text scaling/Unicode/accessibility, offline/reconnect.

**S6 CrewConnex source-review:** source-only observed BLH/crew on authenticated same-UID existing Flight; unsupported/ambiguous => HOLD with zero canonical writes. 파서 G0–G6와 별도 product implementation authorization 필요.

## 5. 시안 선정 권고 — 현재는 KEEP/REWORK/REJECT를 보류

원본 PDF/시안과 현재 LogMate exact build가 동일한 비교 fixture로 감사되기 전 **단독 1위나 생산 디자인 승인**을 발표하지 않는다. 선정 가중치 초안: product truth/authority correctness (gate), information scan/workflow (major), visual authorship/independence, type/color/semantic quality, mobile+tablet adaptive, implementation/accessibility risk. Gate 실패 시 aesthetics 점수로 보상하지 않는다.

## 6. RELATED DOMAIN CHECK

Type T089/T090, Color C120/C121, Layout L111/L112, Interaction I107/I108, Web W120/W121, Content CD126/CD127 + LogMate 9월 Design Corridor, code-first review, 현재 LogMate MASTER, 01–10 포트폴리오 인덱스/07·10 내용을 확인. 본 파일은 제품 적용 mapping이며 새로운 product schema/policy가 아니다.

## 7. HANDOFFS TO OTHER SPECIALISTS

- LogMate owner/engineering: product authority drift 목록과 validation fixtures 전달; 구현·정책 변경은 별도 승인.
- Type/Color/Layout/Interaction/Content: 같은 빌드에 같은 fixture를 올려 실제 불일치만 각 owning study에 반영.
- Web: platform/runtime provenance와 offline PWA/AT execution을 공통 packet으로 보존.
- Portfolio coordinator: PDF+mockup source/index reconciliation, latest MASTER compatibility, true cross-candidate visual review.
