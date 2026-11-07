# CrewConnex ParserProfile — 통합 연구 규격

Status: **RESEARCH ONLY / synthesis-proposal 0.1.0 / NOT PRODUCT APPROVED / NOT IMPLEMENTED** (2026-11-07). LogMate Production Parser OPEN. This research document does not replace LogMate MASTER, docs/specs/import-contract.md, or docs/specs/crewconnex-parser-plan.md.

## 1. 공통 경계와 단계

CrewConnex PDF/검증된 TSV는 **기존 활성 Firebase UID 소유 FlightRecord**에 대한 crew snapshot 및 BLH 원본 증거·교차 검증 전용이다. 새 FlightRecord, 표준 Block/합계, 운항일, 기록 순서, PIC/SIC, PF/PM, operating/deadhead, 승무원 이름을 자동 생성하거나 교정하지 않는다. 원본 PDF, 사번, 사번 파생 해시, 개인정보는 별도 연구 저장소나 영구 데이터, 백업/Sync/로그에 보관하지 않는다.

처리 경로: source selection -> verified immutable ParserProfile detector -> physical text/field admission -> raw observation + locator -> independent date/subject/revision authentication -> owner UID + active Flight + unique full-key comparison -> explicit review -> *source-only* atomic evidence receipt. 어느 단계에서든 불명확하면 생성/덮어쓰기 없이 HOLD. 외부 Import에는 LogMate 내부 Sync의 LWW 자동 덮어쓰기를 적용하지 않는다.

## 2. Immutable ParserProfile 연구 필수 계약

| 속성 | 필수 의미 |
| --- | --- |
| profileId / profileVersion / reportFamily | 정확히 검증한 출력 계열과 범위, 변경 시 새 immutable 버전 |
| detector | 원본 PDF 형식/제목/정확한 열 header/본문·페이지 구조·섹션 소속; 단순 PDF 생성일은 publication 증거 아님 |
| extractionMap | 원본 Date, Activity, From/To, BLH 또는 Blk Hrs, 항공기, clock, crew raw columns; 지원되지 않는 mapping 없음 |
| provenance | raw source SHA-256, profile version, source page + primary TR/TD/page-local MCID 또는 검증된 text-object coordinate, raw label |
| validation | Date/clock/raw-code syntax, Sum/보조표/비비행 배제, blank/continuation, 페이지 경계 및 중복 locator 검증 |
| authority | 운항연도·Publication/revision·report subject/owner·carrier·기존 활성 Flight를 각기 독립 확인 |
| review/receipt | conflict/duplicate/ambiguous/unmatched state, user decision, evidence-head 및 Flight revision CAS, idempotent receipt, rollback |

제안 결과 상태: **FAIL_DOCUMENT** (알 수 없거나 손상된 양식, zero evidence/Flight writes), **DETACHED_HOLD** (구조는 유효하지만 year/subject/UID/date/Flight 미인증), **MATCH_REVIEW** (인증 후보 있으나 사용자 확인 필요), **SOURCE_EVIDENCE_COMMITTED** (승인 + 원자적 저장 성공). 이 상태명은 연구용 제안이며 운영 API enum 승인 아님.

## 3. Skia printer PDF 독립 profile

실제 2026년 6·7·8월 두 페이지 샘플: 본문 TR 40/44/42, 비행 형태 후보 18/22/22=62. 월별 header TD 34/30/31, 후보 own Date 35/62, 누락 27/62, Pairing 30/62. 62건의 Activity·From·To·BLH·ACReg 위치는 310/310 확인됐고, Activity 상대 TD offset은 각각 +3/+7/+13/+15. **상대 offset, TD6/7/8 크기 또는 숫자 Activity만으로 output family를 인증하면 안 된다.**

Detector는 원본별 ToUnicode CMap, 정확한 header, Tagged PDF Table -> TR -> TD -> NonStruct -> page-local MCID, 원본 fingerprint, 페이지·Sum·보조표 구분, 물리적 필드 소속을 함께 확인한다. Date·Pairing·crew 유무는 독립적으로 보존한다. 한 줄 crew leaf 26건은 물리적 anchor TR 간격 1=22, 2=2, 3=2; 6/7 leaf는 31/5건. Leaf는 승무원 인원도 이름도 아님. 4개의 non-adjacent case와 nonflight barrier로 인해 이전 행에서 crew, Date, Pairing을 무조건 상속할 수 없다. 페이지 경계를 넘는 상속도 미승인. 직원번호는 일시적 alignment에만 사용하며 이름 없으면 CrewParticipant.name을 채우지 않는다.

## 4. PDC-generator 14-column PDF 독립 profile

하나의 실제 8월 원본(39,612 bytes): 본문 48 Activity (숫자형 26, 비비행 22), 31 own Date cells 및 31 ordered groups, 495 text operators. 열: Date, Pairing, DC, C/I(L), C/O(L), Activity, From, STD(L), STD(B), To, STA(L), STA(B), AC/Hotel, Blk Hrs. Crew 이름/ACReg 독립 열은 없음. observed numeric Activity는 3자리 8건 + 4자리 18건으로, 1/2/5자리 숫자를 다른 비행으로 자동 받아들이지 않는다.

Activity가 비비행이면 From/To/clock 유무와 상관없이 FlightRecord를 만들지 않는다. PDF 렌더/페인트/좌표 grid, 비행 및 비비행 분류, Date group C/I/C/O 위치, 잘못된 operator, Sum/footer 차단이 필요하다. Local/Base offset은 관찰된 하나의 출력물에서 52/52 UTC+09 base-relative pattern과 양립하지만 다른 base/DST로 전이 불가. 직접 zone·dayOffset 검증이 없으면 네 raw clock만 보존한다. PDF CreationDate는 Publication/revision 인증 근거가 아니다.

C532는 실제 원본에서 C426 엄격 검사 **DETACHED_HOLD**와 원본 의존 55/55 adversarial 검사 실행을 기록했다. C533의 21/21은 **합성** 그룹 위치 변형. C512의 **별도 원본 기반 21개 변형 PDF를 C426 동일 strict 경로 + 독립 PDF renderer**로 재생하는 것은 OPEN이다. 하나의 원본/원본 변형 연구용 oracle를 운영 Dart 파서로 승격하지 않는다.

## 5. TSV 및 다른 형식 경계

Clipboard TSV는 Date, Activity, From, To, BLH, Emp.#, CC, Pos.의 정확한 header와 탭 셀 수, multiline list cardinality, 검증된 pipe repeat 및 Sum/Crew Notes/Report Notes/Accounts 비행 제외를 요구한다. 지원 계열과 출처 없는 추정 continuation은 HOLD. 공개 원본 TSV P1이나 일반 변형 PASS는 없다. 주간 HTML frame-source(P3 제3자 가이드)와 calendar link UI(P4)는 현재 승인된 PDF/TSV 프로필이 아니며 로그인·스크래핑 권한을 주지 않는다.

## 6. 매칭/충돌 처리 안전표

| 조건 | 연구 제안 결과 |
| --- | --- |
| Header/텍스트/구조/field ownership 불일치, 비정상 이동, 잘린 PDF | FAIL_DOCUMENT / writes 0 |
| Date 없음, year/Publication/subject/UID 미확인, 반복 key, 달력 범위 불완전 | DETACHED_HOLD / writes 0 |
| Nonflight, Sum, auxiliary, unknown code | Flight 후보 제외; unknown numeric shape는 strict fail |
| 후보 0개 또는 여러 개 | MATCH 미승인; 사용자 검토 또는 HOLD |
| 후보 1개지만 4자리 year, UID, active Flight 또는 revision 검증 없음 | HOLD; partial-key uniqueness는 authority 아님 |
| 소유권·활성 Flight·원본 의미·사용자 확인 완료 | 기존 Flight에 한정한 증거 저장 후보 |
| 같은 BLH지만 roster snapshot/fingerprint/profile/locator 변화 | revision notice/review, silent overwrite 금지 |
| wrong UID, deleted Flight, stale FlightRevision/EvidenceHead, 중간 실패 | zero partial writes, previous receipt/current ledger 보존 |

## 7. 검증 매트릭스 및 제품화 전제

**Real source gate:** Skia 3개월, 2페이지·Sum·MCID·27 Date missing·26 pipe·19 Preview 외 항목; PDC 원본+정확한 C512 21 변형을 독립 렌더러와 함께 확인. **Synthetic-only:** 오염된 header, cross-page MCID collision, type mismatch, 비비행 4 clock, 임의 C/I-C/O 좌표, 불명확 year, revised crew but equal BLH. **Product runtime (NOT EXECUTED):** 실제 Dart/Flutter local Import and Sembast file-backed owner-bound evidence-only receipt; FlightRevision/EvidenceHead CAS, 멱등성, rollback/reopen/retry, deletion/restore/new UID/backup/Sync isolation. 모든 FAIL/HOLD에서 기존 Flight/aggregate/total/outbox 무변경.

이 문서는 설계 적합성을 정리한 연구 제안이며 실제 제품 결정을 새로 승인하지 않는다. 상세 원본 근거: [C194](crewconnex/C194_INTEGRATED_PHYSICAL_LINEAGE_AND_AUGUST_COMPANY_GATE.md), [C195](crewconnex/C195_INTEGRATED_AUGUST_DATE_GEOMETRY_ADMISSION_GATE.md), [C233](crewconnex/C233_INTEGRATED_PROFILE_AND_SOURCE_ONLY_EVIDENCE_GATE.md), [PDC profile](crewconnex/PDC_GENERATOR_PROFILE_RESEARCH_V1.json), [C426](crewconnex/C426_PDC_NATIVE_PDF_TEXT_ADMISSION.mjs), [evidence register](EVIDENCE_DECISION_REGISTER_20261107.md).

## RELATED DOMAIN CHECK

Type/Color 전문분야 현재 상태 확인: byte-level 파서 의미와 직접 관련 없음. Layout/Interaction은 review/HOLD/conflict/recovery action, Content는 source certainty 및 error wording, Web은 PWA/native 파일 선택·오프라인 profile 배포의 검증 담당. 연구 자료를 런타임 UX PASS로 오인하지 않는다.

## HANDOFFS TO OTHER SPECIALISTS

Engineering: 별도 source-only schema/receipt/CAS 구현 승인은 LogMate MASTER 및 명시적인 Work에 귀속. Interaction/Content: DATE_UNKNOWN, OWNER_UNVERIFIED, REVIEW_CONFLICT, UNSUPPORTED_LAYOUT를 구분하는 명확한 상태/복구 문구 필요. Web: offline old-profile PWA와 native 업데이트 시나리오 별도 검증.
