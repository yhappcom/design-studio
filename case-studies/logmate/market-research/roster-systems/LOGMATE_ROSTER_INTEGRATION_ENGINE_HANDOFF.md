# LogMate Roster Integration Engine — Incremental Research Handoff

Version: **0.1 — 2026-11-24**
Authority: DESIGN STUDIO RESEARCH / development-start recommendation only. Not product policy, implementation authorization, or release approval.

## 1. Executive decision

Do not delay all development until the entire airline/system corpus is mature. The transferred Jeju Air CrewConnex native transport evidence supports beginning an isolated acquisition foundation, subject to a separately authorized LogMate Work. The approved PDF/TSV import contract explicitly covers local files, not live calendar acquisition; a new product scope/contract is required before integration. No canonical FlightRecord creation, actual Block promotion, or automatic change/delete is approved by this research. Overall release: **HOLD**.

Read-only product baselines observed this cycle: AGENTS blob e0b35a1806b99053646bd502c663530822530740; MASTER blob 58743a24623bfb6daf7e16be7f28d4afc2a83e4d; CrewConnex parser plan blob f4c09f17d991800852fd078f8c4f172fd297b971; Manual/Automatic Delta Sync contract blob 1b7441bf6bf06bcd8953ff87c7660de159e2c19e. Product tree e03680b151f5004513c7f763f80c0ea3d1d90dae. Static SourceEvidence dd4f6f01, SourceEvidenceHistory fb222a52, CrewParticipant d5c7e6cf, Sembast repository 11fb8e76 and canonical ledger test 65d384ac sampled, not executed. Product MASTER and approved Work govern implementation. Existing Sync contract does not establish roster payload support; local binding is not remote convergence. Existing PDF/TSV evidence-only boundaries remain unchanged.

## 2. Transferred baseline vs newly acquired evidence

**USER-REPORTED TEST / transferred actual test report, not independently rerun:** 2026-11-24 Jeju Air deployment: HTTPS GET with Accept: text/calendar; WebCal-to-HTTPS conversion; normal TLS, no relay, calendar permission or airline credentials. macOS URLSession default request failed (90.982 s, zero bytes); Accept trials HTTP 200 (9.916/4.153 s). Dart HttpClient iOS Simulator 4/4 and Android Emulator 4/4 HTTP 200, 32197 bytes, 123 VEVENT with required fields. Physical iPhone receipt user-confirmed without detailed logs; physical Android not verified. No causal isolation of Accept header. No source token retained. Provisional individual/duty classification and timestamp/UID observations require independent original parsing. Do not regard successful connection as approved parser or product acceptance.

**REAL ORIGINAL:** private PDF/XLSX directory metadata read only, no bytes decoded. Actual ICS, Export v0.5, Mobile Probe v0.1, platform logs and before/after snapshots not obtained this cycle. Repository root and recursive tree inspection found no matching named probe/export paths in the sampled product tree; this is not proof of absence from other authorized locations. Previous approved private-byte executor/independent renderer blocker unchanged. No repetition of original C512/C426 or prior synthetic PDF counts.

**OFFICIAL DOCUMENT:** RFC 5545 §3.1 requires unfolding before parsing; even incorrectly split UTF-8 byte sequences need restoration. §3.8.7.2 distinguishes DTSTAMP semantics based on METHOD; equal timestamps alone cannot certify vendor revision stability. RFC 9110 §15.4.5 makes 304 a conditional response, not an empty replacement representation. Source links: https://www.rfc-editor.org/rfc/rfc5545.html ; https://www.rfc-editor.org/rfc/rfc9110.html .
**THIRD-PARTY DOCUMENT:** Flight Crew View FLICA guide describes user browser authentication and individual month ICS files handed to app, not proof of airline-issued live feed or direct reusable HTTPS client: https://help.flightcrewview.com/support/solutions/articles/16000194745-flica-ics-schedule-import-info-troubleshooting- . NAVBLUE help search result refers to calendar download and up to 12-hour reflection; direct open redirected to Skywise landing page, so current detailed instructions not independently retrieved. Existing documentary lead only: https://n-raido.support.navblue.aero/support/solutions/articles/35000188427-download-roster . CAE and other deployments remain open in this cycle. No sample-grade or legacy CSV change based on these leads.

**SYNTHETIC EXECUTED:** V8 transient research model 10/10 expected outcomes: split UTF-8 restored before decoding, decode-first failure, tab fold, remove only one continuation whitespace, invalid UTF-8 rejected; 304 with matching prior validator is UNCHANGED, 304 without prior snapshot or matching validator HOLD, malformed 200 preserves prior snapshot, valid 200 stages only. Novelty: byte-level encoding boundary and conditional HTTP response admission, not PDF mutation or receipt-chain test. Model only; no real HTTP request, Dart parser, file-backed store or product test. Reproduce reference model below.

## 3. Development units and Acceptance Criteria

| Unit | Development-start research recommendation | Release | Required acceptance |
|---|---|---|---|
| H01 Feed Client / Dart HTTPS | GO for isolated development proposal (transport feasibility transferred) | HOLD | User-provided URL; HTTPS-only validated scheme, normal TLS, no relay; verified response, redacted errors; physical iOS/Android tests; no canonical writes. |
| H02 URL, secure storage, failure/retry | GO for bounded foundation proposal; feature verification pending | HOLD | Reject downgrade, userinfo, malformed URI and unsafe redirects; never forward secrets cross-origin; secret storage scoped to owner/source; revoke/delete/wipe tests; single concurrent request, bounded timeout/retry/backoff, byte/decompression limits, wrong MIME/login HTML/truncation rejection; last good preserved. 304 only with correct cached representation and validator; no empty-snapshot replacement. |
| H03 Generic ICS and adapter interface | GO for foundation proposal, not parser verification | HOLD | Byte-level unfolding before UTF-8 decode, escaped text, component boundaries, required fields and duplicate singleton checks; malformed input fail closed; UTC/TZID/floating/all-day differentiated; recurrence identity distinct; unsupported recurrence/time semantics HOLD; no vendor semantic inference from syntax. |
| H04 CrewConnex Flight/Duty | Parallel research/development | HOLD | Authorized original and independent parser; duty grouping vs individual legs, non-flight/unknown, duplicated descriptions, source profile version, no actual-flight inference. |
| H05 Normalized Roster Model | Parallel, subject to product policy | HOLD | Separate roster store and canonical ledger; typed time semantics, raw source evidence and owner scope, explicit unknowns; no raw private files or staff identifiers persisted; no silent totals. |
| H06 Snapshot reconciliation | Parallel | HOLD | Before/after real snapshots; stable/reassigned UID, recurrence ID, changed/reordered events, DTSTAMP semantics, coverage movement, incomplete response; absence is not cancellation; ambiguity/review; atomic staging and idempotent replay. |
| H07 Other airline/system reuse | Parallel discovery | HOLD | Actual per-deployment authority, distinguish direct feed from file/portal/third-party; sample, parser, change behavior separate. |
| H08 Native–EFB Roster Sync | Parallel feasibility/contract research | HOLD | Owner/pairing isolation, token-free payload, stale/invalid snapshot preserve, replay/rollback, offline reopen, backup/restore/wipe; no assumption current Sync supports roster payload. Browser CORS and managed EFB direct fetch separately tested. |
| H09 Canonical logbook mapping | HOLD automatic operations | HOLD | Verified actual-time semantics and source authority, exact owner/date/flight/route 0/1/many, active unique Flight, explicit review, double CAS/receipt/atomic no-write failure; approved policy first. |
| H10 Integration/release | HOLD | HOLD | Authorized actual Dart product tests, physical platforms, security/recovery, independent original-derived and product lifecycle gates, approved scope. |

Every GO above is a *research recommendation to initiate an isolated development unit*, not an approved Work, actual implementation or production PASS. Product Work must establish current SHA, scope, permissions, acceptance and tests. No product code changes here.

## 4. Proposed dataflow and platform separation

Native: secure source registration -> HTTPS Feed Client or local file -> response admission -> generic ICS parser -> versioned source adapter -> normalized roster staging -> validated reconciliation -> separate roster store. Review/approved mapping is the only possible boundary to existing Logbook engine; not yet authorized for ICS. Preserve source-only PDF/TSV policy.

EFB PWA: prefer evaluating Native -> owner-scoped token-free roster payload -> authorized existing/extended sync -> offline PWA roster view. Do not transfer subscription URL/token without explicit separate approval. Native HTTPS does not prove browser CORS, redirect security, MDM or EFB availability. Current Sync contract does not prove new roster type, retention or transport. Direct PWA acquisition HOLD. Existing ledger, totals, revisions and outbox must not change from roster refresh; no sync LWW shortcut from external import.

## 5. Reproducible synthetic research reference (not product)

Transient V8 code model; no network and no private inputs:
```js
const decode = bytes => decodeURIComponent(Array.from(bytes,
  b => "%" + b.toString(16).padStart(2,"0")).join(""));
const unfold = bytes => {
  const out = [];
  for (let i=0;i<bytes.length;i++) {
    if (bytes[i]===13 && bytes[i+1]===10 &&
        (bytes[i+2]===32 || bytes[i+2]===9)) { i+=2; continue; }
    out.push(bytes[i]);
  }
  return decode(out);
};
const ascii = s => Array.from(s,c=>c.charCodeAt(0));
const split = [...ascii("SUMMARY:"),0xed,13,10,32,0x95,0x9c,...ascii("\r\n")];
const admission = (status,valid,prior,validator) =>
  status===304 ? (prior && validator ? "UNCHANGED":"HOLD") :
  status===200 && valid ? "STAGE":"PRESERVE";
// Test matrix: unfold(split) == "SUMMARY:한\r\n"; decode(split) throws;
// unfold(ascii("DESCRIPTION:ABC\r\n\tDEF\r\n")) == "DESCRIPTION:ABCDEF\r\n";
// unfold(ascii("DESCRIPTION:ABC\r\n  DEF\r\n")) == "DESCRIPTION:ABC DEF\r\n";
// unfold([0xed,13,10,32,0xff]) throws.
// admission(304,false,true,true)=UNCHANGED; (304,false,false,true)=HOLD;
// (304,false,true,false)=HOLD; (200,false,true,true)=PRESERVE;
// (200,true,true,true)=STAGE.
```
This simplified model does not implement an RFC-complete parser, real validator scoping, transport or durable transaction. Test exact vendor/parser code and persisted cache in approved product Work. No general parser PASS.

## 6. Outstanding decisions and next work

- Acquisition: transferred evidence for one native deployment; independent source and physical-device acceptance OPEN.
- Interpretation/reconciliation: actual original and change snapshots OPEN; no UID, DTSTAMP, actual Block or coverage verdict.
- Engine integration/release: HOLD; authorized Work required. Existing G0–G6/O01–O08 not closed; C194 historical sync debt unchanged.
- Next connected work: H01–H03 acceptance package using authorized Export v0.5/Mobile Probe v0.1, logs and sanitized original metadata; execute real response admission and ICS parsing regressions, then before/after source diff when available. In parallel verify lawful NAVBLUE/CAE/FLICA paths (official evidence and actual sample acquisition); keep PDF gates and source-only persistence research. If access blocked, document concrete recovery and pivot to distinct feasible work, not repeated transport hypotheses.
- Allocation: CrewConnex semantics/reconciliation 25%, other systems 25%, PDF/Excel/TSV 30%, generic ICS/reconciliation 15%, synthesis/handoff 5%; flexible. Version changes only on material evidence/decision.

## RELATED DOMAIN CHECK
Web specialist: browser/CORS/managed EFB validation and support claims; Layout/Interaction and Content: review/conflict/staleness/error flows, not visual approval; Typography/Color not materially implicated. No product/design authorization inferred.

Navigation: [Research plan](RESEARCH_PLAN_20261004.md), [Synthesis](RESEARCH_SYNTHESIS_20261107.md), [ParserProfile](PARSER_PROFILE_SPEC_20261107.md), [Evidence register](EVIDENCE_DECISION_REGISTER_20261107.md), [Readiness](IMPLEMENTATION_READINESS_20261107.md), [Revalidation queue](REVALIDATION_QUEUE.md). Legacy index grades unchanged pending real delta.
