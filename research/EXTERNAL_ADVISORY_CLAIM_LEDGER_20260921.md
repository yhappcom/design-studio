# Design Studio — External Advisory Claim & Falsification Ledger

**Snapshot:** 2026-09-21  
**Baseline checked before authorship:** `main@7e03ed6a284382a8f9c4b686c60d0822f9364146`  
**Purpose:** turn the static synthesis and evidence map into an auditable claim-level review instrument.  
**Authority:** routing/synthesis only. Canonical specialist studies and status files remain authoritative; this ledger makes no gate promotion.

## Why this ledger exists

The synthesis explains the studio's position and the evidence map routes reviewers to files. External advice still needs a smaller unit of analysis: a **claim that can be challenged, a current evidence class, a counterexample, and a falsification path**. This ledger supplies that unit so reviewers can disagree precisely rather than endorse or reject an entire domain.

Evidence tiers follow `EXTERNAL_ADVISORY_EVIDENCE_MAP_20260921.md`: **S** source/static, **R** reproducible implementation/runtime, **T** independent transfer, **A** assistive technology, **F** representative field telemetry, **H** representative human evidence. A claim does not automatically require every tier.

## Claim ledger

| ID | Owner | Claim under review | Current evidence | Minimum next evidence needed | Plausible counterexample / failure | Primary canonical entry evidence |
|---|---|---|---|---|---|---|
| TY-01 | Type | Active custom-type defects must be resolved in causal order: drawing → general spacing → residual kerning. | S + static/raster practice | complete-source bounded drawing review; then spacing evidence before kerning | measured defects are predominantly spacing rather than outline construction, or mature-font comparison shows the drawing criterion is misdiagnosed | `research/type/082-stage-closure-evidence-compression.md`; `research/type/T021-architecture-reset-complete-ci-raster-review.md`; `research/type/T021-outline-render-measured-summary.json` |
| TY-02 | Type | Product typography decisions require actual resolved family/fallback/metrics rather than nominal font declarations. | S + static transfer contracts | R with exact build, requested/resolved family, fallback, TextScaler and geometry | runtime resolution is stable and materially equivalent across target conditions, making the assumed fallback risk immaterial | `research/type/090-pre-runtime-saturation-and-gate-stop-rule.md`; T089 fixture referenced by current Type status |
| CO-01 | Color | Material state meaning must not depend on a single color/accent channel. | S + static/system practice | R under actual states plus supported accessibility transformations; A where nonvisual parity is claimed | redundant cues disappear after reflow/platform transformation or create competing hierarchy that reduces comprehension | `research/color/113-stage-3-closure-evidence-compression.md`; `research/color/C024-stage3-transfer-closure-map.md` |
| CO-02 | Color | Brand/decorative chroma must yield to consequence-bearing state salience. | S + studio judgment | R state-injection comparison; H if perceptual priority/comprehension is claimed | quieter treatment improves task accuracy or stronger consequence color produces false urgency/alert fatigue | `research/color/121-pre-runtime-saturation-and-state-evidence-stop-rule.md`; `research/color/119-candidate05-07-semantic-rank-contradiction-review.md` |
| LA-01 | Layout | Responsive invariants should preserve semantic/action relationships, not identical coordinates. | S + reproducible static/system practice | R measured geometry under narrow/SafeArea/max-text/fallback; T when platform behavior is material | a supposedly protected adjacency becomes harmful at narrow width and a representation change produces better continuity | `research/layout/104-stage-3-closure-evidence-compression.md`; `research/layout/L094-logmate-cross-surface-operational-geometry-synthesis-audit.md` |
| LA-02 | Layout | Fit pressure should trigger recomposition/disclosure before type distortion or semantic abbreviation. | S + cross-domain synthesis | R with real strings, resolved metrics and adaptive geometry; H where comprehension trade-off is claimed | controlled abbreviation is domain-standard, unambiguous and measurably superior to recomposition for expert workflows | `research/layout/112-pre-runtime-saturation-and-geometry-evidence-stop-rule.md`; Content/Type dependencies |
| IN-01 | Interaction | Requested action, pending/unknown outcome, authoritative result, persistence/sync truth and restored projection must remain distinguishable when system authority differs. | S + state-machine/system practice | R failure/interruption injection with exact authority/provenance | implementation guarantees collapse some states atomically, making visible distinctions unnecessary or harmful | `research/interaction/100-stage-3-closure-evidence-compression.md`; `research/interaction/I090-logmate-synthesis-precedence-and-state-salience-contract.md` |
| IN-02 | Interaction | Recovery must be causally safe under ambiguous outcomes; blind Retry must not risk duplicate mutation. | S + static/system practice | R with unknown-outcome, retry, idempotency/reconciliation and restoration evidence | backend/client contract proves idempotency or transactional semantics that eliminate the duplicate-mutation risk | `research/interaction/I087-error-prevention-review-reversal-authority.md`; `research/interaction/108-pre-runtime-saturation-and-authority-evidence-stop-rule.md` |
| WB-01 | Web | Runtime evidence is reviewable only when tied to exact source/build, environment and state provenance. | S + extensive harness/closure design | R with same-build replication packet; T for portability claims | required provenance fields are excessive and do not alter diagnosis/reproducibility, or omit a material variable | `research/web/W103-logmate-synthesis-runtime-transfer-and-evidence-promotion-gate.md`; `research/web/113-stage-3-closure-evidence-compression.md` |
| WB-02 | Web | Same-build replication and independent transfer are distinct evidence steps. | S + methodology | R repeated primary run followed by T independent engine/platform where claim depends on transfer | observed behavior is specification-guaranteed and independent transfer adds no material uncertainty reduction | `research/web/W067-repair-to-browser-closure-ladder.md`; `research/web/121-stage3-evidence-saturation-and-execution-priority-gate.md` |
| WB-03 | Web | Lighthouse/DevTools/CI/synthetic measurements are LAB; FIELD CWV requires provenance-bearing representative RUM/aggregate. | S + methodology | F for any field-performance claim | telemetry sample is nonrepresentative or aggregation hides route/device/network populations, invalidating the field inference | `research/web/113-stage-3-closure-evidence-compression.md`; `research/web/121-stage3-evidence-saturation-and-execution-priority-gate.md` |
| CT-01 | Content | User-facing wording must preserve object → state → action → consequence → recovery truth and must not invent implementation authority. | S + system/content practice | R visible+a11y payload mapped to actual action/destination/outcome | explicit wording of every distinction overloads expert users; progressive disclosure or domain convention preserves truth more efficiently | `research/content/119-stage-3-closure-evidence-compression.md`; `research/content/CD106-error-prevention-review-recovery-content-system.md` |
| CT-02 | Content | Product logic must not depend on English strings/grammar; user/source Unicode and locale-sensitive representations remain stress inputs even for English-only authored UI. | S + static corpus/system practice | R with source/user Unicode, date/numeric and fallback/reflow stress | product scope explicitly constrains source data so a stated stress class is impossible, or platform canonicalization changes the relevant boundary | `research/content/CD076-end-to-end-localization-and-recovery-semantic-closure-corpus.md`; `research/content/127-pre-runtime-saturation-and-semantic-evidence-stop-rule.md` |
| UX-01 | Cross-cutting | Static expert/model critique can assess coherence and risks but cannot establish representative discoverability, comprehension, workload, trust, preference or task performance. | S + governance/methodology | H with appropriate representative sampling/tasks/environment for human claims | none that converts non-human critique into human evidence; challenge should target whether the proposed human method is adequate | `AGENTS.md`; `research/EXTERNAL_ADVISORY_EVIDENCE_MAP_20260921.md` |
| UX-02 | Cross-cutting | Accessibility-oriented static review does not establish actual product WCAG conformance or AT interoperability. | S + static/system practice | R implementation checks plus A where AT interoperability is claimed | a specific criterion is fully decidable from source/static evidence; this narrows the required test, not the general boundary | `AGENTS.md`; `research/web/W056-accessibility-runtime-closure-harness.md`; current specialist status boundaries |

## Advisory response schema

For each challenged claim, ask the adviser to return:

1. **Claim ID and verdict:** supported / conditionally supported / unsupported / wrongly scoped.
2. **Reason:** the strongest argument, not a preference statement.
3. **Evidence audited:** exact canonical files/sections or external sources.
4. **Counterexample:** a realistic condition under which the claim fails or becomes unnecessary.
5. **Missing evidence class:** S/R/T/A/F/H only when actually needed.
6. **Falsification test:** the smallest test capable of changing the conclusion.
7. **Decision consequence:** what product/design decision should change if the claim is falsified.
8. **Confidence and boundary:** where the adviser would not generalize the conclusion.

This schema intentionally asks for contrary evidence and decision consequences. Generic approval such as “looks good” is not useful advisory evidence.

## Cross-domain dependency checks

Before accepting an external contradiction, verify that it is assigned to the canonical owner rather than the most visible surface:

- text fit may originate in Type metrics, Content payload or Layout allocation;
- apparent color failure may originate in incorrect Interaction authority or Layout cue separation;
- recovery copy may be correct linguistically but invalid because Interaction cannot establish the outcome;
- browser screenshots may appear correct while Web provenance or accessible payload disproves parity;
- human preference cannot by itself override an operational/accessibility requirement without examining task consequence.

Record one contradiction with exact provenance and reference it across peer domains instead of generating parallel versions of the same fact.

## Current governance/status contradiction

`progress/STATUS.md` remains materially behind current specialist status files. It reports Color/Layout before Stage 3 entry, Web at Stage 2 and Content at Stage 1, whereas current specialist statuses place Color, Layout/Interaction, Web and Content at Stage 3 PRACTICE / NOT PASSED. External reviewers must use specialist statuses for current maturity until the coordinator reconciles the global file. This ledger does not modify coordinator-owned status.

## RELATED DOMAIN CHECK

Checked current governance, global status, all five specialist statuses, research index, static synthesis and external advisory evidence map at the baseline above. The ledger deliberately spans Type, Color, Layout, Interaction, Web, Content and cross-cutting UX/accessibility/human evidence while preserving canonical ownership.

## HANDOFFS

- **External advisers:** select a bounded set of claim IDs and return claim-level contradictions using the response schema.
- **Coordinator:** reconcile global maturity metadata before the package is represented externally as a current studio-status snapshot.
- **Specialists:** if an adviser falsifies or narrows a claim, evaluate the contradiction in the owning canonical research path; do not edit this routing ledger as a substitute for canonical research.
- **Product transfer:** attach exact runtime provenance to any R/T/A/F evidence used to promote or reject a static claim.
