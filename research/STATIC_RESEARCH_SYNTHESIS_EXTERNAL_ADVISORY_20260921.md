# Design Studio — Static Research Synthesis & External Advisory Brief

**Snapshot:** 2026-09-21  
**Canonical baseline:** `main@644a1291af1bf783b222ef66a5418705ee09b7d3`  
**Purpose:** SYNTHESIS / external-advisory handoff / pre-product-transfer closure.  
**Scope:** Consolidates the studio's static and pre-runtime research without replacing canonical domain studies. It is an index and briefing layer, not a new specialist or a claim of production validation.

## How to read this brief

Design Studio has five official specialist roles: Type, Color, Layout/Interaction, Web Design, and Content Design/UX Writing. Accessibility, Human Factors, UX integration and research methodology remain cross-cutting. Canonical evidence remains in each specialist research directory and status file; when this brief conflicts with newer canonical evidence, the newer evidence wins.

Evidence labels retain studio meaning: **SOURCE** = source-established; **SYNTHESIS** = evidence-derived transferable principle; **STUDIO JUDGMENT** = design position/method; **OPEN** = unresolved; **DEPENDENCY** = requires another evidence stream; **REPLICATION / CONTRADICTION / TRANSFER VALIDATION** = validation intent. Static critique, model review, screenshots or document volume do not imply PASS where runtime, device, AT or human evidence is required.

## Executive synthesis

The static program has reached a useful transition point. Across all domains the dominant uncertainty has shifted from “what should the contract be?” to “does the contract survive exact implementation, platform behavior, adaptive stress and human use?”

The strongest shared principle is **preserve product truth before preserving appearance**. Visual concepts may differ materially, but semantic identity, state authority, action consequence, recovery, protected relationships, accessibility semantics and evidence provenance must remain coherent.

The studio therefore rejects several common shortcuts:
- immature type drawing repaired by tracking/kerning;
- semantic wording shortened merely to preserve geometry;
- color as the only carrier of state;
- absolute coordinates treated as responsive invariants;
- visible affordances treated as proof of implemented behavior;
- pending/failure/unknown outcomes collapsed into one status;
- synthetic or lab performance relabeled as field evidence;
- static expert critique relabeled as human usability evidence.

## Maturity snapshot

| Domain | Current canonical state | What static research can already support | What it cannot yet establish |
|---|---|---|---|
| Type | Stage 1 PASS; Stage 2 PRACTICE / NOT PASSED | rendering/fallback/fit diagnosis, product-string stress, gate discipline | T021 drawing closure, spacing/kerning progression, exact runtime font resolution, AT/human evidence |
| Color | Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED | semantic state architecture, contrast/color-management reasoning, redundant-cue design | runtime state survival across modes/reflow, physical environment/observer/human evidence |
| Layout/Interaction | Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED | protected relationships, adaptive/reflow reasoning, state/authority/recovery contracts | exact route/focus/history/recovery behavior, measured runtime geometry, Search closure, human workflow evidence |
| Web | Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED | browser-aware design contracts, runtime provenance model, closure ladder | exact candidate runtime closure, independent browser/platform/device/PWA/AT evidence, field CWV |
| Content/UX Writing | Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED | terminology/state/action/recovery architecture, localization-ready semantic contracts | runtime visible+a11y parity, production voice approval, linguistic/AT/human comprehension evidence |
| UX integration | cross-cutting, no separate canonical specialist | end-to-end consistency review across IA, flow, feedback, recovery, accessibility and professional workflow | representative discoverability, workload, trust, preference and task-performance evidence |

## 1. Typography / Type Design

### Consolidated findings
**SYNTHESIS:** typography is a rendering system, not a collection of nominal font values. Product decisions must account for requested and resolved family, fallback, glyph coverage, metrics, scaling, wrapping/truncation, numerals/punctuation and platform rendering.

**STUDIO JUDGMENT:** type-development gates are causal. For the active custom drawing work, **drawing → general spacing → residual kerning** is mandatory. Kerning, negative tracking, glyph narrowing or semantic abbreviation must not hide immature drawing or spacing.

**TRANSFER CONTRACT:** product strings are falsification fixtures. Operational identifiers, dates, search/status strings, navigation labels, reorder controls, offline/recovery messages and Unicode/source text should be replayed at baseline and enlarged text with actual resolved-font evidence.

### Open questions
T021 bounded drawing remains the upstream blocker. Exact Candidate 05/07 runtime font resolution, TextScaler behavior, production mono/fallback selection, AT behavior and human task evidence remain OPEN.

### External advice wanted
Ask type experts to challenge the drawing-gate methodology, adequacy of the operational corpus, criteria for spacing entry, fallback/metrics strategy, and whether the custom-type effort has a defensible product benefit versus mature production families.

## 2. Color

### Consolidated findings
**SYNTHESIS:** color should encode semantic rank, not become semantic truth. Focus, current location, selection, invalid/ambiguous, warning, pending, offline/degraded, failure, evidenced success, recovery and stale/superseded states require distinguishable ownership and appropriate non-color redundancy.

**STUDIO JUDGMENT:** decorative/brand chroma yields to functional salience. Current-location state must not be confused with focus; success should not be painted before persistence evidence; forced-color/high-contrast transformations must not remove the only state cue.

**TRANSFER CONTRACT:** compare semantic IDs and cue redundancy across light/dark, reflow, text scaling/fallback and supported accessibility modes without forcing Candidate 05/07 to share a palette.

### Open questions
Stage 3 requires rendered state injection. Native high-contrast and Web forced-colors remain separate evidence classes. Calibrated display, glare/night, observer variation and representative-human salience remain OPEN.

### External advice wanted
Ask color/accessibility experts to challenge semantic-state taxonomy, redundancy requirements, contrast/salience methodology, color-management assumptions and the planned environmental/observer validation.

## 3. Layout, Spatial & Interaction

### Consolidated findings
**SYNTHESIS:** responsive invariants are relationships rather than fixed coordinates. Protect object identity→values, query→status→results, item→reorder action→resulting position, destination→current-location cue and error/recovery→owning object.

**SYNTHESIS:** interaction authority must distinguish requested transition, pending/unknown outcome, authoritative result, restored projection and recovery. Visible controls or state labels are not evidence that the behavior exists.

**STUDIO JUDGMENT:** fit pressure should first trigger intrinsic room, redistribution, row growth/wrap, recomposition or disclosure/detail transfer—not Type distortion or semantic abbreviation.

**ACCESSIBILITY BASELINE:** WCAG 2.2 is the current normative studio benchmark. Relevant implementation validation includes focus visibility/not-obscured, target geometry, status communication and non-drag single-pointer alternatives where applicable.

### Open questions
Exact runtime route/focus/history/recovery evidence is missing. Narrow/SafeArea/max-text/fallback geometry must be measured in the real widget tree. Search remains outside closure until implemented. AT and representative-human discoverability, workload, trust and task performance remain OPEN.

### External advice wanted
Ask interaction/HCI experts to challenge the authority model, recovery/idempotency assumptions, adaptive relationship set, non-drag reorder model and whether the planned human study captures pilot workflow risk rather than generic preference.

## 4. Web Design

### Consolidated findings
**SYNTHESIS:** Web is the studio's principal implementation-transfer integrator, not a substitute for peer-domain ownership. It should expose where browser/runtime behavior confirms, limits or contradicts Type, Color, Layout/Interaction and Content contracts.

**PROVENANCE CONTRACT:** meaningful runtime evidence should bind exact source/build, platform/engine, viewport/insets/input/network, route/history, requested/resolved font, visible and accessibility payload, focus/state, geometry/order, transaction/persistence/recovery.

**VALIDATION LADDER:** exact-source analyze/tests → primary native runtime with same-build REPLICATION → failure/interruption injection → adaptive/accessibility stress → second native platform where relevant → served Flutter Web and independent browser → physical device/PWA → AT/human evidence.

**PERFORMANCE BOUNDARY:** Lighthouse, DevTools, CI and synthetic traces are LAB evidence. LCP/INP/CLS are FIELD evidence only when backed by provenance-bearing representative RUM/aggregate data.

### Open questions
Candidate 05/07 exact runtime closure is not established. Independent browser/native transfer, physical-device/PWA behavior, screen-reader evidence and representative field performance remain OPEN. CI failure before the relevant runner/test step is NON-EXECUTION, not product failure.

### External advice wanted
Ask web/PWA experts to review the provenance packet, replication ladder, service-worker/update/offline coverage, independent-engine strategy, accessibility test mix and RUM sampling/segmentation plan.

## 5. Content Design / UX Writing

### Consolidated findings
**SYNTHESIS:** language is part of the interface contract. The core diagnostic is **object → state → action → consequence → recovery**. Tone and brevity are subordinate to semantic fidelity.

**SEMANTIC ARCHITECTURE:** `product truth → semantic message contract → locale realization → surface realization → render/runtime realization`. State selects message; message text must never select state.

**STUDIO JUDGMENT:** Draft, Validated, Saving, Saved locally, Synced, Failed, Offline, Stale and Unknown outcome must remain distinct whenever product authority distinguishes them. Geometry pressure does not justify deleting a semantic job.

**LOCALIZATION BOUNDARY:** current LogMate product-authored UI is English-only, while user/source Unicode and locale-sensitive date/numeric representations remain mandatory stress inputs. English strings or grammar must not become product logic.

### Open questions
Exact-build visible strings and accessible name/role/state have not yet been reconciled against actual action/destination/outcome. Production voice, linguistic review, AT comprehension and representative-pilot comprehension/task evidence remain OPEN.

### External advice wanted
Ask content/localization experts to challenge terminology governance, state taxonomy, localization architecture, professional-domain wording, accessible naming parity and the proposed human comprehension protocol.

## 6. Cross-cutting UX synthesis

UX is deliberately not a sixth specialist in the current governance model. The integrated review asks whether the whole professional workflow remains coherent when domain contracts meet.

### End-to-end invariants
1. **Identity:** the same professional object remains identifiable through navigation, search, editing, reorder, failure and restoration.
2. **Authority:** requested action is separated from pending/unknown and authoritative result.
3. **State communication:** visual, linguistic and accessibility channels describe the same underlying truth without relying on color alone.
4. **Recovery:** failure/interruption offers only actions justified by current authority; blind Retry must not create duplicate mutations when outcome is unknown.
5. **Adaptive integrity:** narrow width, insets, scaling, fallback and reflow preserve protected semantic/action relationships rather than exact geometry.
6. **Navigation continuity:** route/history/focus restoration preserves context and agency.
7. **Accessibility parity:** visible meaning/action and accessible name/role/state/action remain aligned.
8. **Professional workflow:** optimization for visual quietness or compactness must not erase operationally important distinctions.

### Canonical closure scenarios
Use the same scenarios across domains:
- Home → Logbook → record → edit → cancel/commit → Back/Forward;
- Search A → B → reject late A → result → record → Back/restore;
- Add Flight invalid → correct → commit → persistence failure → Retry;
- non-drag reorder → save failure/retry → Undo → reload;
- offline create/edit → reconnect → authoritative refresh.

These scenarios are test fixtures, not claims that the current product already passes them.

## 7. Evidence already strong enough to advise projects

The static corpus is mature enough to support project diagnosis, alternative generation, implementation constraints and falsifiable acceptance criteria in:
- semantic state separation and recovery;
- responsive relationship preservation;
- typography/fallback/string-pressure diagnosis;
- semantic color and redundant cues;
- navigation/history/focus requirements;
- forms, validation, onboarding, retrieval/search and localization-ready content architecture;
- browser/runtime provenance planning;
- accessibility-oriented design review.

Advice should remain conditional whenever exact implementation, device, AT or human evidence is absent.

## 8. Evidence that must not be overstated

The studio does **not** currently claim:
- all specialist curricula are complete;
- Stage 3 PASS in any currently active Stage 3 domain;
- T021 drawing/spacing/kerning closure;
- Candidate 05/07 runtime PASS;
- WCAG conformance of an actual product;
- physical-device or independent-platform closure;
- screen-reader/AT PASS;
- representative pilot usability/comprehension/trust/workload PASS;
- production brand voice approval;
- FIELD Core Web Vitals without representative RUM.

## 9. External advisory package — recommended questions

When sending this brief to an outside adviser, include the relevant canonical studies and ask them to answer:
1. Which conclusions are well-supported, conditionally supported, or unsupported by the cited evidence?
2. Which important theories, standards, methods or counterexamples are missing?
3. Where has the studio confused specification quality with empirical validation?
4. Which planned runtime/device/AT/human tests have weak external validity or insufficient controls?
5. Which invariants are too rigid, too broad or likely to fail under real professional workflows?
6. What evidence would change the adviser's conclusion?
7. Which three unresolved risks should be tested first before production design decisions become expensive?
8. Are any domain boundaries creating blind spots or duplicated responsibility?
9. For aviation/professional workflows, which claims require subject-matter expert or representative-user evidence rather than design-expert judgment?
10. What should be removed from the research program because it adds documentation but little decision value?

Request critique and contrary evidence, not endorsement.

## 10. Minimum material to share with an adviser

Start with this brief, `AGENTS.md`, all five specialist status files and the relevant domain closure/stop-rule studies. Add raw harness/results only for claims the adviser is asked to audit. For a product-specific review, add exact source/build identifier, screenshots or recordings, runtime provenance, accessibility payload and the relevant workflow fixture. Avoid sending the entire corpus without a question: the repository is intentionally deep and the advisory task should be bounded.

## 11. Transition to product research

The static phase is not “finished knowledge.” It is a falsifiable baseline. Product research should now try to break it.

The next high-information steps are:
- Type: execute T021 bounded drawing in a complete-source environment, then spacing before kerning;
- all product-facing domains: execute the shared Candidate 05/07 runtime packet;
- capture contradictions once and route them back to the canonical owner;
- run independent platform/browser/device/AT transfer where material;
- defer human claims until representative evaluation exists;
- revise this synthesis only when evidence materially changes a conclusion.

## RELATED DOMAIN CHECK

This synthesis reviewed the latest specialist statuses and closure/stop-rule evidence for Type (T082/T090), Color (C113/C121), Interaction (I100/I108), Layout (L104/L112), Web (W113/W121) and Content (CD119/CD127), plus current governance and research indexing. It intentionally creates no new ownership and makes no gate promotion.

## HANDOFFS

- **All specialists:** use this document as an external-facing map, not as replacement canonical evidence.
- **Web/product transfer:** bind contradictions to exact runtime provenance before handing them back.
- **Coordinator:** if the studio later formalizes a phase boundary, this synthesis can inform—but does not itself modify—global curriculum or governance.
- **External advisers:** challenge evidence, assumptions, missing counterexamples and validation design; do not infer production PASS from the breadth of the static corpus.
