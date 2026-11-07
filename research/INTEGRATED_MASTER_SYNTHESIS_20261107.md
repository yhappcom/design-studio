# Design Studio — 통합 연구 마스터 종합본

**통합 기준:** 2026-11-07 · Design Studio main@3264d490e80e46121d515200bac24ba977e0360b · LogMate main@f4bcd2f7b7e77039e29653baa1cc93797673885b
**분류:** COORDINATOR SYNTHESIS / NAVIGATION / STUDIO JUDGMENT (신규 독립 실험 아님)
**저장소 경계:** Design Studio만 통합 문서를 갱신. LogMate는 READ-ONLY 제품 권한.
**중요:** 원본 연구, 전문분야 STATUS, 제품 MASTER가 이 문서보다 우선한다. 이 종합본 자체로 어떠한 Stage/제품 검증 PASS도 발생하지 않는다.

## 1. 결론과 적용 방식

현재 Design Studio는 다섯 전문분야(Type, Color, Layout+Interaction, Web, Content)의 Stage 1–2 기반을 구축했고, 대부분 Stage 3에서 **정적 설계의 포화 → 실제 실행 증거 확보**로 병목이 이동했다. 중복 설명 문서를 추가해 성숙도를 올리기보다 동일한 제품 빌드에 대해 여러 분야가 공동으로 반증 가능한 테스트를 수행해야 한다.

한 줄 원칙: **외형 보존보다 제품의 의미·권한·결과·복구·증거의 정확성을 먼저 보존한다.**

통합 산출물 역할:
1. 이 문서: 최신 연구 결론과 판단 범위.
2. [통합 근거·모순 등록부](INTEGRATED_EVIDENCE_CONTRADICTION_REGISTER_20261107.md): 충돌·OPEN·SUPERSEDED와 해소 조건.
3. [LogMate 제품 적용 증거 지도](../case-studies/logmate/PRODUCT_APPLICATION_EVIDENCE_MAP_20261107.md): 화면/기능별 제품 권한과 디자인 전이 조건.
4. [실행 검증·연구 로드맵](INTEGRATED_EXECUTION_ROADMAP_20261107.md): 실행 순서, 산출물, 신규 연구 개시/중단 기준.
5. [전체 STATUS](../progress/STATUS.md): coordinator의 최신 분야별 상태 요약.

역사적 2026-09-21 [정적 연구/외부 자문 종합](STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md), [evidence map](EXTERNAL_ADVISORY_EVIDENCE_MAP_20260921.md), [15-claim ledger](EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md), [role packets](EXTERNAL_ADVISORY_REVIEW_PACKETS_20260921.md), [traceability audit](EXTERNAL_ADVISORY_PACKAGE_TRACEABILITY_AUDIT_20260921.md)는 삭제/덮어쓰기하지 않는다. 해당 자료의 작성 당시 baseline은 역사적 provenance이며 최신 전문분야 상태를 대체하지 않는다.

## 2. 거버넌스 및 성숙도

- 전문분야 5개, 운영상 연구 스트림 6개(Type, Color, Layout, Interaction, Web, Content). Layout/Interaction은 **한 명의 소유자**이나 공간과 시간/행동 증거를 별도 관리한다.
- Accessibility, Human Factors, UX integration은 현재 **cross-cutting**; 임의로 독립 Stage/PASS를 만들지 않는다.
- Stage: 1 Foundation → 2 Intermediate → 3 Advanced/Systems → 4 Production & Authorship → 5 Research & Advisory.
- 2026-11-07에 읽은 최신 전문분야 파일은 모두 2026-09-20 governance sync를 표기한다. 이는 연구 상태에 대한 최신 확인 파일이지 이후 개별 제품 검증이 전혀 없다는 단정은 아니다.

| 분야 / 권한 파일 | 현재 단계 | 이미 자문 가능한 정적 결론 | 다음 결정적 증거 / OPEN |
|---|---|---|---|
| Type / [TYPE_STATUS](../progress/TYPE_STATUS.md) | S1 PASS; S2 PRACTICE **NOT PASSED** | glyph/metric/operational roles, fallback, 문자열 fit, 인과적 font gate | T021 complete-source bounded drawing; drawing → general spacing → residual kerning; exact resolved font/TextScaler |
| Color / [COLOR_STATUS](../progress/COLOR_STATUS.md) | S1/S2 PASS; S3 PRACTICE **NOT PASSED** | semantic tokens, role/salience, non-color redundancy, color management | C120 실제 state injection과 C121 stop rule; light/dark, native high contrast vs web forced-colors, reflow/환경 |
| Layout + Interaction / [LAYOUT_STATUS](../progress/LAYOUT_STATUS.md) | S1/S2 PASS; S3 PRACTICE **NOT PASSED** | protected relationships, responsive recomposition, action/authority/recovery | I107/L111 exact runtime; route/focus/history, SafeArea/max text/fallback, Search 구현, 사람 |
| Web / [WEB_STATUS](../progress/WEB_STATUS.md) | S1/S2 PASS; S3 PRACTICE **NOT PASSED** | browser/product transfer, provenance packet, LAB/FIELD 구분 | W120 exact build execution; same-build replication; second platform; served PWA, device, AT, human |
| Content / [CONTENT_STATUS](../progress/CONTENT_STATUS.md) | S1/S2 PASS; S3 PRACTICE **NOT PASSED** | terminology, object/state/action/consequence/recovery, localization-ready semantics | CD126 visible+a11y+authority parity, Unicode/date/numeric/fallback/reflow, linguistic/AT/human |

### 연구 포화에 대한 독립적 수렴

[T090](type/090-pre-runtime-saturation-and-gate-stop-rule.md), [C121](color/121-pre-runtime-saturation-and-state-evidence-stop-rule.md), [I108](interaction/108-pre-runtime-saturation-and-authority-evidence-stop-rule.md), [L112](layout/112-pre-runtime-saturation-and-geometry-evidence-stop-rule.md), [W121](web/121-stage3-evidence-saturation-and-execution-priority-gate.md), [CD127](content/127-pre-runtime-saturation-and-semantic-evidence-stop-rule.md)은 공통적으로 **Candidate 05/07 기존 Home 코드 기반 연구의 새로운 정적 설명 문서만으로는 미해결 사실을 줄이지 못한다**고 판단했다. 이 Candidate 번호는 2026-09-20 코드 기반 Home 리뷰 스트림이며, 이후 01–10 whole-product portfolio 스트림의 동일 번호와 다르다.

## 3. 재사용 가능한 공통 불변 조건

1. **제품 권한:** 현재 제품 MASTER/approved contracts가 사용자 결정과 기능 범위를 통제; 시안·연구·코드 shell은 새 정책을 정하지 않는다.
2. **식별성:** record identity ↔ 값, query ↔ status ↔ results, action ↔ 대상, destination ↔ current location, error/recovery ↔ 원래 object의 관계를 보호한다.
3. **상태 권한:** requested → pending/unknown → authoritative result → local persisted/synced projection → recovery를 실제 보증 범위에서 구분한다. 색/문구/모션으로 근거 없는 성공을 만들지 않는다.
4. **적응형 레이아웃:** 동일 좌표가 아니라 protected relationship, reading order, action reachability를 보존한다. 먼저 공간/재흐름/재구성/상세 이동으로 fit을 해결한다.
5. **타이포그래피:** 실제 loaded/resolved family + fallback + TextScaler + 임의 Unicode와 운영 숫자/식별자의 비교 가능성을 검토한다. T021이 완료되기 전 custom metric을 생산 기준으로 삼지 않는다.
6. **색/상태:** 브랜드색은 시스템 결과를 증명하지 못한다. current/focus/invalid/pending/offline/failure/evidenced success/recovery/stale은 역할별 text/shape/position/AT 단서가 필요하다.
7. **콘텐츠 의미:** object → state → action → consequence → recovery. 짧은 문구를 위해 semantic job을 삭제하지 않는다.
8. **접근성:** WCAG 2.2를 기준으로 하지만 시안 평가=실제 WCAG 적합성이나 AT 상호운용성을 뜻하지 않는다.
9. **검증 출처:** exact source/build, runtime 환경, route/network, data revision, visible+a11y, focus/geometry, authoritative persistence/rollback 등 provenance를 보존한다.
10. **사용자 검증:** 전문가/모델 비평과 대표 사용자 실험은 별개의 증거이다. LAB 성능과 FIELD CWV도 별개이다.

## 4. 실제 적용 연구의 두 갈래

### A. LogMate 제품 디자인

- 제품 소스의 현재 권한: [LogMate MASTER](https://github.com/yhappcom/logmate/blob/main/MASTER.md) (읽기 전용); 이 문서에서 확인한 범위는 현재 계정 필수/UID ownership, local-first + **명시 Manual Sync**, 인증 뒤 정확한 3개 setup choice, Home 7/28/90-day rolling Activity, Home Totals 3-slot Customize, Native Mobile + Tablet/EFB PWA, English-authored UI/Unicode source data이다.
- 위 내용은 일부 9월 디자인 케이스의 이전 제품 상태와 다를 수 있으므로 과거 시안보다 **2026-11-07에 읽은 MASTER**가 우선한다.
- 9월 brand reset + Design Corridor + code-first independent specialist review는 유효한 방법/제한으로 유지한다. 생산 폰트/팔레트/최종 시각 승인/실기기 결과까지 확정한 것은 아니다.
- [포트폴리오 후보 인덱스](../case-studies/logmate/portfolio-candidates/README.md)는 01–10 개념 문서를 포함. 02–10은 **STATIC PORTFOLIO COMPLETE** 기록, 01은 수동 복구/인덱스 reconciliation OPEN. PDF는 대화 artifact로 전달되어 저장소 tree의 reproducible binary evidence가 아니다. 시안 자체에 대한 교차 비교/현행 MASTER 적합성 감사가 필요하다.
- 9월 코드 렌더 Home Candidate 05/07의 owner aesthetic review eligibility는 전체 제품 포트폴리오 Candidate 05/07이나 production UI 승인과 **다른 증거**다.

### B. CrewConnex / roster parser intelligence

- [2026-11-07 로스터 통합](../case-studies/logmate/market-research/roster-systems/RESEARCH_SYNTHESIS_20261107.md)은 독립적으로 성숙한 연구 트랙이다. 이번 Design Studio 전체 통합은 352k자 수준의 revalidation queue나 수많은 C-number 원본을 재요약하지 않고 **통합 navigation + G0–G6 acceptance**만 연결한다.
- 세 달 Skia 62 numeric flight-shaped candidates / 310 physical locators, curated Preview 43/43 unique value links, PDC original 31 Date groups, tracked CrewConnex airlines 21(A1/A2 20)는 **그 명시된 자료 범위 안에서만** 유효하다.
- CrewConnex의 BLH/crew evidence는 확인된 기존 Flight에 대해 source-only 보조 증거이며 자동 Flight 생성·canonical Block 수정 권한이 아니다. Operational year/subject/UID/revision, exact original-derived tests, evidence-only atomic CAS/rollback, native/PWA lifecycle는 OPEN. [구현 준비도](../case-studies/logmate/market-research/roster-systems/IMPLEMENTATION_READINESS_20261107.md) 참조.
- 파서 연구 결과를 디자인 일반 원칙이나 production parser 승인으로 승격하지 않는다.

## 5. 현재 주요 위험과 조직적 판단

- 글로벌 상태 문서의 stage drift는 이번 coordinator 정합화 대상으로 삼는다(세부 단계 기준은 항상 전문분야 STATUS).
- older static synthesis와 newer specialist statuses는 작성 시점이 다르다. 내용 모순으로 자동 취급하지 않고 versioned evidence로 보존한다.
- 최신 LogMate MASTER를 확인하지 않고 9월 후보의 no-login/automatic sync/period/total/preview 등을 생산 사양으로 추정하면 제품 계약을 위반할 수 있다.
- 하나의 mockup board에 12개 환경을 표시해도 해당 화면의 **실제 깨짐·상태·접근성·실행**을 입증한 것은 아니다.
- 포트폴리오의 “독립 디자인 개념”은 논리 설명이 아니라 동일 조건의 시각/구조 비교로 검증해야 한다.
- C-번호가 증가해도 CrewConnex의 G2/G3를 닫았다는 의미가 아니다.

## 6. 권한 및 증거 승격 규칙

| Tier | 의미 | 충분한 예 | 주의 |
|---|---|---|---|
| S | SOURCE / static / calculation / expert critique | 표준·원본·bounded fixture·정적 시안 | runtime/사용자 결과 불가 |
| R | exact build runtime repeatability | 해당 소스/빌드·환경에 연결된 테스트/행동 | 다른 플랫폼 PASS 불가 |
| T | independent transfer | 두 번째 엔진/기기·동일 의미 비교 | 사람/AT PASS 불가 |
| A | actual assistive technology | 실 screen reader / keyboard / spoken result | 정적 accessibility review 대체 불가 |
| F | representative FIELD | provenance-bearing RUM/대표 사용자 측정 | Lighthouse/CI LAB ≠ F |
| H | representative human | 실제 조종사 task/error/recovery 평가 | 전문가 모의 평가 ≠ H |

PASS는 해당 claim의 gate가 실제 증거를 충족할 때만 사용한다. 미실행 CI는 NON-EXECUTION이다. 제품 승인·구현 권한은 Design Studio 연구 통합에서 생기지 않는다.

## 7. 결론 / 다음 실행 단위

**첫 순서:** 최신 source/build·product authority 확인 → 기존 연구의 충돌 등록 → 실제 대표 시나리오 1개를 6개 전문 연구 스트림이 공동 검증 → 같은 빌드 반복 → 독립 플랫폼 → 물리기기/AT/대표 사용자.

**연구 운영:** 새 file/ID를 만들기 전에 새 증거·새 제품 조건·반증 가능성이 있는지 확인한다. 동일 계약의 문장 재정리는 진행량으로 세지 않는다. 기존 예약작업은 이 문서가 직접 변경하지 않는다.

## RELATED DOMAIN CHECK

- Type: T021/T090; Color: C120/C121; Layout: L111/L112; Interaction: I107/I108; Web: W120/W121; Content: CD126/CD127.
- Cross-cutting: AGENTS, WCAG boundary, 2026-09-21 external 15-claim ledger; LogMate brand/portfolio case; CrewConnex Nov 7 G0–G6 research.
- 중복 목적: 분야별 원본을 다시 저술하지 않고 버전/권한/증거와 제품 연계의 **coordination contradiction review**만 한다. 원본의 저작/결론을 그대로 보존한다.

## HANDOFFS TO OTHER SPECIALISTS

- Type: T021 complete-source drawing 또는 exact resolved-font provenance가 생기면 먼저 갱신.
- Color/Layout/Interaction/Content: 한 빌드/한 authority fixture에서 상태·geometry·문구 충돌을 공동 평가.
- Web: 실행 packet의 source/build, browser/device/AT/field tier 분리와 독립 transfer를 관리.
- Product owner/LogMate engineering: 실제 구현 Work와 정책 승인·릴리즈 PASS는 LogMate의 권한 체계에서 별도 결정.
