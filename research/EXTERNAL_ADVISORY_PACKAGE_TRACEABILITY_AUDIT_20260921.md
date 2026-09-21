# Design Studio — External Advisory Package Traceability Audit

**Snapshot:** 2026-09-21  
**Baseline audited:** `main@3b9cf04c0e4b5588e15c149ffda2b4b1d7f24001`  
**Purpose:** verify traceability and boundary consistency across the static synthesis, evidence map, claim ledger and role-specific review packets before external use.  
**Authority:** audit/routing only. Canonical specialist research and status remain authoritative. No gate promotion.

## Audit scope

Reviewed:
- `AGENTS.md`
- `progress/STATUS.md`
- all five specialist status files
- `research/README.md`
- `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`
- `research/EXTERNAL_ADVISORY_EVIDENCE_MAP_20260921.md`
- `research/EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md`
- `research/EXTERNAL_ADVISORY_REVIEW_PACKETS_20260921.md`
- latest `main` commits through the baseline above.

The audit asks four questions: (1) does every externally exposed claim have an owner and evidence route, (2) does every packet point back to claim-level falsification, (3) are evidence classes represented consistently, and (4) does any routing document silently promote maturity or validation.

## 1. Package chain

The external package now has four distinct layers. They should be used in this order rather than treated as four interchangeable summaries.

| Layer | File | Job | Must not be used as |
|---|---|---|---|
| Orientation | `STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md` | explain studio position, maturity and major open boundaries | canonical gate evidence |
| Evidence routing | `EXTERNAL_ADVISORY_EVIDENCE_MAP_20260921.md` | route domain claims to high-value canonical evidence and evidence tiers | proof that the routed claim passed |
| Falsification unit | `EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md` | expose bounded claims, counterexamples and minimum next evidence | replacement for owning specialist research |
| Reviewer delivery | `EXTERNAL_ADVISORY_REVIEW_PACKETS_20260921.md` | match claims/evidence/questions to reviewer competence | whole-studio approval instrument |

**Audit result:** chain is coherent. The review packets reference the ledger and synthesis; the ledger references the evidence map; all layers explicitly defer authority to canonical specialist evidence.

## 2. Claim-to-packet traceability

| Claim | Canonical owner | Evidence tier now | Primary external packet | Secondary cross-check | Missing evidence that prevents overclaim |
|---|---|---|---|---|---|
| TY-01 | Type | S + static/raster practice | A Type | D Layout where fit pressure propagates | complete-source drawing review; spacing only after drawing PASS |
| TY-02 | Type | S + static transfer contract | A Type | E Web/runtime | exact resolved family/fallback/TextScaler runtime |
| CO-01 | Color | S + systems practice | B Color | G Accessibility/AT | rendered transformations; A when nonvisual parity claimed |
| CO-02 | Color | S + studio judgment | B Color | C HCI where human salience is claimed | R state injection; H for perceptual/comprehension claims |
| LA-01 | Layout | S + static/system practice | D Responsive Layout | C HCI | measured adaptive runtime geometry; T where platform-material |
| LA-02 | Layout | S + cross-domain synthesis | D Responsive Layout | A Type + F Content | real strings/metrics/reflow; H if comprehension trade-off claimed |
| IN-01 | Interaction | S + state/system practice | C HCI/Interaction | F Content + E Web | R failure/interruption authority evidence |
| IN-02 | Interaction | S + state/system practice | C HCI/Interaction | E Web/runtime | R unknown-outcome/idempotency/reconciliation evidence |
| WB-01 | Web | S + harness methodology | E Web/PWA | all peer domains consume provenance | R same-build provenance packet |
| WB-02 | Web | S + methodology | E Web/PWA | domain-specific T consumers | R replication, then T only where portability claim requires it |
| WB-03 | Web | S + methodology | E Web/PWA | none required | F representative provenance-bearing RUM/aggregate |
| CT-01 | Content | S + content/system practice | F Content | C Interaction + G Accessibility | R visible+a11y payload mapped to authority |
| CT-02 | Content | S + corpus/system practice | F Content | A Type + E Web | R Unicode/date/numeric/fallback/reflow stress in actual scope |
| UX-01 | cross-cutting | S + methodology/governance | C HCI/Human Factors | all packets must respect boundary | H representative-user evidence for human claims |
| UX-02 | cross-cutting | S + accessibility/system practice | G Accessibility/AT | D Layout + E Web | R implementation evidence; A where AT interoperability claimed |

**Audit result:** all 15 ledger claims have at least one bounded reviewer packet and a stated missing-evidence boundary. No orphan claim was found.

## 3. Synthesis-to-ledger coverage

The integrated synthesis contains broad propositions that are intentionally more numerous than the 15 ledger claims. The ledger captures the propositions with the highest consequence or highest risk of being overgeneralized:

- Type rendering/fallback and causal drawing/spacing/kerning order → TY-01/TY-02.
- semantic color redundancy and consequence salience → CO-01/CO-02.
- protected responsive relationships and recomposition-before-distortion → LA-01/LA-02.
- authority/recovery distinctions → IN-01/IN-02.
- provenance, replication/transfer and LAB/FIELD performance → WB-01/WB-02/WB-03.
- semantic truth/localization architecture → CT-01/CT-02.
- human-evidence and accessibility-conformance boundaries → UX-01/UX-02.

Other synthesis statements such as navigation continuity, professional-workflow consistency and accessible visible/semantic parity are currently treated as integrated consequences of these claims rather than separate claims. This is acceptable for external routing **until** an adviser disputes one independently or product transfer exposes a contradiction. At that point, create a new bounded claim only if it has a distinct falsification path.

**Audit result:** no immediate need to proliferate claim IDs. The current ledger is deliberately sparse enough for review while covering the package's consequential boundaries.

## 4. Evidence-boundary consistency

The package consistently separates:
- **S** — source/static reasoning, standards, calculations, critique and design contracts;
- **R** — reproducible exact implementation/runtime;
- **T** — independent transfer where portability matters;
- **A** — real assistive-technology interoperability;
- **F** — representative production field telemetry;
- **H** — representative human observation/measurement.

Specific boundary checks:
1. Type never claims T021 closure or kerning entry; `drawing → spacing → kerning` remains intact.
2. Color never converts static contrast/state architecture into runtime high-contrast, forced-colors, observer or human PASS.
3. Layout/Interaction never converts static contracts into exact route/focus/history/recovery, Search, AT or human PASS.
4. Web consistently labels Lighthouse/DevTools/CI/synthetic evidence as LAB and requires representative provenance-bearing RUM/aggregate for FIELD CWV.
5. Content never converts expert copy critique into production voice, linguistic, AT-comprehension or representative-human PASS.
6. Cross-cutting UX explicitly rejects simulated human evidence and static-review claims of product WCAG/AT conformance.

**Audit result:** no evidence-class promotion contradiction was found among the four advisory layers.

## 5. Package-level contradiction: global maturity metadata

`progress/STATUS.md` remains materially stale relative to specialist status files. It reports:
- Color Stage 3 entry not yet audited;
- Layout/Interaction Stage 3 entry not yet audited;
- Web Stage 2 PRACTICE;
- Content Stage 1 Foundation not passed.

Current specialist statuses instead report:
- Type: Stage 2 PRACTICE / NOT PASSED;
- Color: Stage 3 PRACTICE / NOT PASSED;
- Layout/Interaction: Stage 3 PRACTICE / NOT PASSED;
- Web: Stage 3 PRACTICE / NOT PASSED;
- Content: Stage 3 PRACTICE / NOT PASSED.

The advisory package correctly warns reviewers to use specialist statuses for current maturity. Because `progress/STATUS.md` is coordinator-maintained, this audit does not modify it.

**External-use consequence:** do not send the global maturity table by itself. If `progress/STATUS.md` is attached, attach the five specialist statuses and state that specialist status controls current maturity until coordinator reconciliation.

## 6. Snapshot/baseline drift

The four advisory files were authored sequentially and therefore record different authorship baselines:
- synthesis: `644a1291...`;
- evidence map: `1d0ebf27...`;
- claim ledger: `7e03ed6a...`;
- review packets: `af579a7c...`.

This is **not a research contradiction**: each file states that newer canonical evidence wins. It is, however, a packaging risk if an external reviewer mistakes the embedded baseline for a frozen package version.

**Resolution for external use:** treat this audit's baseline `main@3b9cf04c0e4b5588e15c149ffda2b4b1d7f24001` as the first fully assembled package snapshot. Future external exports should record one package-level commit/ref in the cover note rather than rewriting historical authorship baselines in every component file.

## 7. Orphan-evidence audit

The advisory package intentionally does not enumerate every research artifact. Raw harnesses, JSON summaries and historical studies are discoverable through domain indexes and should be requested only to audit a disputed claim. Therefore, a canonical research file not named in the advisory map is not automatically “orphan evidence.”

For package purposes, evidence is orphaned only if it materially changes an externally exposed claim but is absent from its route. No such material orphan was identified in the current status/closure layer reviewed here.

This finding is bounded: it is a traceability audit of current canonical status/closure evidence, not a line-by-line re-adjudication of every historical source in the repository.

## 8. External-use readiness

The package is now structurally ready for bounded external advisory review **with one governance caveat**: current maturity must be taken from specialist statuses, not the stale global table.

Recommended send sequence:
1. state exact package commit/ref;
2. send the synthesis for orientation;
3. send one role-specific packet;
4. attach that specialist's current status and only the packet's primary evidence;
5. include the claim ledger response schema;
6. provide raw artifacts only when the adviser requests them for a specific claim;
7. route returned contradictions to the canonical owner before changing synthesis documents.

Do not request whole-studio endorsement. Request claim-level challenge, counterevidence and falsification advice.

## 9. Remaining organization work

High-value static organization is now narrow rather than open-ended:
1. coordinator reconciliation of `progress/STATUS.md`;
2. optional package cover/index that records a single frozen external-review commit when an actual adviser is selected;
3. incorporate real adviser contradictions when received;
4. stop generating additional advisory layers unless a traceability defect, new claim, new evidence or reviewer need appears.

Further summary documents without one of those triggers would add document volume rather than decision value.

## RELATED DOMAIN CHECK

Audited Type, Color, Layout, Interaction, Web, Content and cross-cutting UX/accessibility/human boundaries together. No new canonical ownership is created. Current specialist stop rules remain unchanged.

## HANDOFFS

- **Coordinator:** reconcile global maturity metadata before representing `progress/STATUS.md` as current externally.
- **External-advisory coordinator:** freeze one package-level commit/ref when selecting an adviser; use the packet matching reviewer competence.
- **Specialists:** evaluate returned contradictions in canonical research before any synthesis-layer revision.
- **Product transfer:** supply R/T/A/F/H evidence only with the provenance appropriate to that evidence class.
