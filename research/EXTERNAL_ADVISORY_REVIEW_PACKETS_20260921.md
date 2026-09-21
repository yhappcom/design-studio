# Design Studio — Role-Specific External Advisory Review Packets

**Snapshot:** 2026-09-21  
**Baseline checked before authorship:** `main@af579a7c1929a383e42f4a454f9e090da76b9f18`  
**Purpose:** convert the integrated synthesis, evidence map and claim ledger into bounded review packets that can be sent to outside specialists without requiring a full-repository review.  
**Authority:** routing/synthesis only. Canonical specialist research/status remains authoritative. No gate promotion is made here.

## Use rule

Send one packet to a reviewer whose competence matches the packet. Do not ask a reviewer to approve Design Studio as a whole. Ask them to challenge the listed claims, audit the listed canonical evidence, identify missing counterevidence, and specify the smallest evidence capable of changing their conclusion.

For every packet, attach:
1. `STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md` for orientation;
2. the relevant specialist status file(s);
3. only the primary evidence listed below initially;
4. `EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md` for claim IDs and response schema.

Underlying raw artifacts should be supplied only when the reviewer needs them to audit a specific claim. Document count is not confidence.

Evidence tiers: **S** source/static; **R** reproducible implementation/runtime; **T** independent transfer; **A** assistive technology; **F** representative field telemetry; **H** representative human evidence.

---

## Packet A — Type Design / Typography Engineering

### Reviewer profile
Type designer or font engineer competent in outline construction, spacing/kerning, metrics, fallback/rendering and production font behavior. UI typography expertise is useful but does not replace drawing/spacing expertise for T021.

### Claims to challenge
- **TY-01:** current custom-type defects should be resolved in causal order `drawing → general spacing → residual kerning`.
- **TY-02:** product typography decisions require actual resolved family/fallback/metrics rather than nominal font declarations.
- Cross-domain dependency: fit pressure must not be silently repaired by semantic shortening or layout assumptions before real type metrics are known.

### Primary evidence
- `progress/TYPE_STATUS.md`
- `research/type/082-stage-closure-evidence-compression.md`
- `research/type/090-pre-runtime-saturation-and-gate-stop-rule.md`
- `research/type/T021-architecture-reset-complete-ci-raster-review.md`
- `research/type/T021-outline-render-measured-summary.json`

### Questions
1. Is drawing-first the correct diagnosis for the bounded T021 defects, or is spacing already the dominant variable?
2. What objective/independent evidence should be required before declaring drawing PASS and entering general spacing?
3. Are widths/sidebearings-frozen and kerning-off controls sufficient to isolate drawing quality?
4. Which glyph/string corpus is missing for an operational aviation/logbook interface?
5. When would a mature production family be preferable to continuing the custom family?
6. Which runtime variables must be captured before comparing Candidate 05/07 typography?

### Do not ask this reviewer to certify
Product usability, color salience, interaction authority, WCAG conformance or production runtime behavior unless they independently have that competence/evidence.

### Minimum useful return
Claim verdict for TY-01/TY-02, strongest counterexample, missing drawing/spacing evidence, smallest falsification test, and a recommendation on whether custom-type work should continue before product transfer.

---

## Packet B — Color Science / Accessibility Color

### Reviewer profile
Color scientist, color-management specialist, or accessibility specialist with demonstrated competence in semantic UI color, contrast, high-contrast/forced-colors behavior and—where claimed—display/environmental validation.

### Claims to challenge
- **CO-01:** material state meaning must not depend on a single color/accent channel.
- **CO-02:** brand/decorative chroma yields to consequence-bearing state salience.
- Boundary claim: native high-contrast, Web forced-colors, calibrated display, environmental light and human observer evidence are distinct validation classes.

### Primary evidence
- `progress/COLOR_STATUS.md`
- `research/color/113-stage-3-closure-evidence-compression.md`
- `research/color/121-pre-runtime-saturation-and-state-evidence-stop-rule.md`
- `research/color/C024-stage3-transfer-closure-map.md`
- `research/color/119-candidate05-07-semantic-rank-contradiction-review.md`

### Questions
1. Does the semantic-state taxonomy over-encode states that should instead be communicated through structure/content?
2. Which state pairs genuinely require visual differentiation under expert workflows?
3. Are proposed non-color redundancies robust under reflow and platform accessibility transformations?
4. Which tests are decidable statically and which require runtime, calibrated-display, glare/night or observer evidence?
5. Could stronger consequence color increase false urgency or alert fatigue?
6. What evidence should be required before approving a production palette rather than merely a semantic architecture?

### Minimum useful return
CO-01/CO-02 verdicts, state-taxonomy corrections, missing environmental/platform tests, and one concrete falsification case for the salience hierarchy.

---

## Packet C — HCI / Interaction / Human Factors

### Reviewer profile
HCI/interaction specialist with experience in asynchronous state, error prevention/recovery, professional or safety-relevant workflows. Aviation human-factors competence is strongly preferred for ecological-validity claims.

### Claims to challenge
- **IN-01:** requested action, pending/unknown outcome, authoritative result, persistence/sync truth and restored projection must remain distinguishable when authority differs.
- **IN-02:** recovery must be causally safe under ambiguous outcomes; blind Retry must not risk duplicate mutation.
- **UX-01:** static expert/model critique cannot establish representative discoverability, comprehension, workload, trust, preference or task performance.
- Layout dependency: protected semantic/action relationships should survive adaptive recomposition without requiring identical coordinates.

### Primary evidence
- `progress/LAYOUT_STATUS.md`
- `research/interaction/100-stage-3-closure-evidence-compression.md`
- `research/interaction/108-pre-runtime-saturation-and-authority-evidence-stop-rule.md`
- `research/interaction/I087-error-prevention-review-reversal-authority.md`
- `research/interaction/I090-logmate-synthesis-precedence-and-state-salience-contract.md`
- `research/layout/104-stage-3-closure-evidence-compression.md`

### Questions
1. Does the authority model distinguish materially different states or expose implementation detail that users need not see?
2. Under what transaction/idempotency guarantees can Retry safely collapse the proposed recovery distinctions?
3. Are Undo, restoration and stale-projection rules causally correct after interruption?
4. Are the five shared closure scenarios ecologically valid for real pilot/logbook work?
5. Which user groups, experience levels, environments and task/error conditions are required for representative human validation?
6. Which measures should be behavioral (error, completion, recovery), subjective (trust/workload) or observational (discoverability)?

### Minimum useful return
IN-01/IN-02/UX-01 verdicts, authority-model counterexample, proposed representative-user protocol boundary, and the three highest-risk workflows to test first.

---

## Packet D — Responsive Layout / Accessibility Geometry

### Reviewer profile
Senior product/layout designer or accessibility specialist experienced in responsive/adaptive systems, enlarged text, zoom/reflow, target/focus geometry, SafeArea/insets and dense professional interfaces.

### Claims to challenge
- **LA-01:** responsive invariants should preserve semantic/action relationships rather than identical coordinates.
- **LA-02:** fit pressure should trigger recomposition/disclosure before type distortion or semantic abbreviation.
- **UX-02:** accessibility-oriented static review does not establish actual product conformance or AT interoperability.

### Primary evidence
- `progress/LAYOUT_STATUS.md`
- `research/layout/104-stage-3-closure-evidence-compression.md`
- `research/layout/112-pre-runtime-saturation-and-geometry-evidence-stop-rule.md`
- `research/layout/L094-logmate-cross-surface-operational-geometry-synthesis-audit.md`
- `research/layout/110-candidate05-07-spatial-invariant-contradiction-review.md`

### Questions
1. Are the protected relationships complete, or are some relationships incorrectly treated as spatial invariants?
2. At what point should adjacency become representation change, disclosure or a detail surface?
3. When is domain-standard abbreviation preferable to recomposition?
4. What runtime geometry should be measured under max text, fallback, SafeArea/insets and local scrolling?
5. Which focus/target/reading-order claims cannot be established from screenshots?

### Minimum useful return
LA-01/LA-02 verdicts, protected-relationship corrections, a narrow-width/max-text counterexample, and a minimum runtime geometry capture plan.

---

## Packet E — Web / PWA / Runtime Validation

### Reviewer profile
Senior web/PWA engineer-designer or browser-platform specialist competent in service workers, navigation/history, accessibility runtime, cross-engine behavior, offline/update/storage behavior, performance measurement and reproducible diagnostics.

### Claims to challenge
- **WB-01:** runtime evidence is reviewable only when tied to exact source/build, environment and state provenance.
- **WB-02:** same-build replication and independent transfer are distinct evidence steps.
- **WB-03:** Lighthouse/DevTools/CI/synthetic are LAB; FIELD CWV requires representative provenance-bearing RUM/aggregate.
- Cross-domain claim: Web should return exact runtime contradictions to canonical peer owners rather than treating screenshots as closure.

### Primary evidence
- `progress/WEB_STATUS.md`
- `research/web/113-stage-3-closure-evidence-compression.md`
- `research/web/121-stage3-evidence-saturation-and-execution-priority-gate.md`
- `research/web/W103-logmate-synthesis-runtime-transfer-and-evidence-promotion-gate.md`
- `research/web/W056-accessibility-runtime-closure-harness.md`
- `research/web/W067-repair-to-browser-closure-ladder.md`
- `research/web/W109-production-runtime-degradation-closure-manifest-20260920.md`

### Questions
1. Which provenance fields are essential, redundant or missing for reproducibility?
2. When is same-build replication sufficient and when is independent engine/platform transfer required?
3. Which service-worker update, offline, cache invalidation, storage/eviction and installed-PWA cases are missing?
4. Does the proposed accessibility runtime evidence separate DOM/semantics/focus evidence from actual AT interoperability?
5. What sampling/segmentation is required before RUM supports a FIELD CWV claim?
6. Which failures should be classified as NON-EXECUTION rather than negative product evidence?

### Minimum useful return
WB-01/02/03 verdicts, corrected provenance schema, missing PWA/browser cases, and the smallest credible replication/transfer ladder.

---

## Packet F — Content Design / Localization / Professional Terminology

### Reviewer profile
Senior content designer/UX writer or localization architect. For aviation terminology and professional acceptability, include an aviation SME or representative pilot separately rather than assuming content expertise supplies domain authority.

### Claims to challenge
- **CT-01:** wording must preserve object → state → action → consequence → recovery truth and must not invent implementation authority.
- **CT-02:** product logic must not depend on English strings/grammar; source/user Unicode and locale-sensitive representations remain stress inputs even for English-only authored UI.
- Human boundary: expert copy critique does not establish representative comprehension or professional acceptability.

### Primary evidence
- `progress/CONTENT_STATUS.md`
- `research/content/119-stage-3-closure-evidence-compression.md`
- `research/content/127-pre-runtime-saturation-and-semantic-evidence-stop-rule.md`
- `research/content/CD076-end-to-end-localization-and-recovery-semantic-closure-corpus.md`
- `research/content/CD106-error-prevention-review-recovery-content-system.md`
- `research/content/CD109-logmate-synthesis-semantic-density-and-brand-voice-audit.md`

### Questions
1. Does the semantic taxonomy preserve product truth without exposing unnecessary system detail?
2. Which distinctions can be progressively disclosed without creating false authority?
3. Which terminology needs aviation-SME review and which needs representative-user comprehension testing?
4. Does the localization architecture separate message/state selection from locale realization sufficiently?
5. Which Unicode/date/numeric/source-data cases are genuinely in product scope and which are speculative?
6. What evidence should precede production voice approval?

### Minimum useful return
CT-01/CT-02 verdicts, terminology/state-taxonomy corrections, localization failure cases, and a list separating SME-review terms from human-comprehension test terms.

---

## Packet G — Accessibility / AT Integration Review

### Reviewer profile
Accessibility specialist with implementation and assistive-technology testing experience across the product's target platforms. Static WCAG knowledge alone is insufficient for interoperability claims.

### Claims to challenge
- **UX-02:** static accessibility review cannot establish actual product WCAG conformance or AT interoperability.
- **CO-01:** material states need redundancy beyond color where meaning must survive transformation/nonvisual access.
- Cross-domain parity: visible object/state/action and accessible name/role/state/action should describe the same product truth.

### Primary evidence
- `AGENTS.md`
- current five specialist status files
- `research/web/W056-accessibility-runtime-closure-harness.md`
- `research/color/113-stage-3-closure-evidence-compression.md`
- `research/interaction/100-stage-3-closure-evidence-compression.md`
- `research/content/119-stage-3-closure-evidence-compression.md`

### Questions
1. Which WCAG 2.2 criteria can be substantially assessed statically and which require execution?
2. What platform/browser/AT combinations are necessary for claims relevant to the target product?
3. How should visible+a11y semantic parity be captured and compared after state transitions?
4. Which focus/status/recovery cases are highest risk under AT?
5. Are forced-colors/native high-contrast tests being incorrectly treated as substitutes for screen-reader/AT evidence?

### Minimum useful return
UX-02 verdict, a platform/AT matrix scoped to actual product targets, parity-test method, and prioritized AT scenarios.

---

## Cross-review conflict protocol

External advisers may disagree. Do not resolve disagreement by majority vote.

For each contradiction:
1. identify the affected claim ID;
2. preserve the adviser's exact boundary and evidence;
3. assign the contradiction to the canonical owner;
4. determine whether it changes S-level synthesis or requires R/T/A/F/H evidence;
5. run the smallest falsification/replication test capable of discriminating the competing explanations;
6. update canonical research first; update routing/synthesis documents only afterward.

Examples:
- a content adviser proposing shorter copy cannot override Interaction authority; test whether the shortened form preserves the same state/consequence/recovery truth;
- a visual designer preferring a quieter error color cannot override consequence visibility; test salience/redundancy under actual states;
- a type adviser may legitimately falsify the drawing-first diagnosis, but that contradiction belongs in Type before downstream geometry is redesigned;
- an HCI preference result does not by itself establish accessibility or operational safety.

## Current known package-level contradiction

`progress/STATUS.md` is coordinator-maintained and remains stale relative to specialist status files. It still reports Color/Layout before Stage 3 entry, Web at Stage 2 and Content at Stage 1, while current specialist files place Color, Layout/Interaction, Web and Content at Stage 3 PRACTICE / NOT PASSED. External packets must therefore use the specialist status files for current maturity until coordinator reconciliation. This document does not modify `progress/STATUS.md`.

## RELATED DOMAIN CHECK

This packet layer was prepared after checking current governance, global status, all five specialist statuses, the research index, the integrated synthesis, evidence map and claim ledger. It preserves the five-specialist architecture and treats UX/accessibility/human factors as cross-cutting rather than inventing new canonical ownership.

## HANDOFFS

- **Coordinator:** reconcile global status before publishing a single current maturity table externally.
- **External-advisory coordinator:** match reviewer competence to one bounded packet; request adversarial claim-level review rather than generic endorsement.
- **Specialists:** evaluate returned contradictions in the owning canonical path before changing synthesis documents.
- **Product transfer:** use external advice to prioritize falsification; do not convert expert opinion into runtime, AT, field or human evidence.