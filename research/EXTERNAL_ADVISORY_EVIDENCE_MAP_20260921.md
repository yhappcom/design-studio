# Design Studio — External Advisory Evidence Map

**Snapshot:** 2026-09-21  
**Baseline:** `main@1d0ebf27e498091ec926bbfb61165acbf1ed1760`  
**Purpose:** external-review routing layer for `STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`. This file does not replace canonical specialist evidence and makes no gate promotion.

## Evidence-reading rule

External reviewers should not infer confidence from document count. Review a claim against its canonical status, the most relevant closure/stop-rule evidence, and—where requested—the underlying source/practice/validation artifact. Static specification, runtime evidence, physical-device evidence, assistive-technology evidence, field telemetry and representative-human evidence are different classes.

The current global `progress/STATUS.md` is materially stale relative to the specialist status files: it still describes Color/Layout Stage 3 as not yet audited, Web as Stage 2 PRACTICE and Content as Stage 1, while the specialist files now record Color, Layout/Interaction, Web and Content at Stage 3 PRACTICE / NOT PASSED. For advisory work, use the specialist status files as the current maturity source until the coordinator reconciles global status. This map does not edit coordinator-owned status.

## 1. Typography / Type Design

**Current status:** `progress/TYPE_STATUS.md` — Stage 1 PASS; Stage 2 PRACTICE / NOT PASSED.

**Primary claim to challenge:** typography decisions must be based on actual rendering/fallback/metrics and the active custom-type work must preserve the causal gate `drawing → general spacing → residual kerning`.

**Best entry evidence:**
- `research/type/082-stage-closure-evidence-compression.md` — compresses the downstream product corpus and identifies T021 drawing as the upstream blocker.
- `research/type/090-pre-runtime-saturation-and-gate-stop-rule.md` — explains why more Candidate 05/07 static type notes add little information before drawing/runtime changes.
- `research/type/T021-architecture-reset-complete-ci-raster-review.md`
- `research/type/T021-normalized-architecture-ci-raster-review.md`
- `research/type/T021-outline-render-measured-summary.json`

**Do not infer:** T021 PASS, spacing PASS, kerning entry, production custom-font approval, exact runtime fallback/TextScaler behavior, AT or human PASS.

**High-value external challenge:** Is the drawing-first gate technically sound for the observed defects? Are the current T021 raster/outline measurements sufficient to decide drawing PASS, and what independent type-design evidence should be added before spacing begins?

## 2. Color

**Current status:** `progress/COLOR_STATUS.md` — Stage 1 PASS; Stage 2 PASS; Stage 3 PRACTICE / NOT PASSED.

**Primary claim to challenge:** semantic state hierarchy must survive color transformation and cannot rely on one accent/color channel; brand chroma yields to consequence-bearing salience.

**Best entry evidence:**
- `research/color/113-stage-3-closure-evidence-compression.md`
- `research/color/121-pre-runtime-saturation-and-state-evidence-stop-rule.md`
- `research/color/C024-stage3-transfer-closure-map.md`
- `research/color/C091-pointer-preview-cancel-commit-states.md`
- `research/color/119-candidate05-07-semantic-rank-contradiction-review.md`

**Do not infer:** production palette approval, actual high-contrast/forced-colors survival, calibrated-display/glare/night/observer validation or representative-human salience PASS.

**High-value external challenge:** Does the state taxonomy separate all materially different authority states without visual over-encoding? Which tests require native high-contrast, Web forced-colors, calibrated display, environmental light or human observers rather than static contrast analysis?

## 3. Layout / Spatial

**Current status:** `progress/LAYOUT_STATUS.md` — combined Layout/Interaction Stage 3 PRACTICE / NOT PASSED.

**Primary claim to challenge:** responsive/adaptive invariants should protect semantic/action relationships rather than absolute coordinates; fit pressure should trigger recomposition before semantic/type distortion.

**Best entry evidence:**
- `research/layout/104-stage-3-closure-evidence-compression.md`
- `research/layout/112-pre-runtime-saturation-and-geometry-evidence-stop-rule.md`
- `research/layout/L094-logmate-cross-surface-operational-geometry-synthesis-audit.md`
- `research/layout/110-candidate05-07-spatial-invariant-contradiction-review.md`
- relevant reproducible summaries under `research/layout/*-results-summary.json`

**Do not infer:** measured Candidate 05/07 adaptive geometry, physical-device/SafeArea closure, independent-platform transfer or human workflow PASS.

**High-value external challenge:** Are the protected relationships complete and falsifiable? Which relationships should be allowed to change representation at narrow width/max text, and which must remain spatially adjacent or action-proximate?

## 4. Interaction

**Current status:** shared `progress/LAYOUT_STATUS.md` — Stage 3 PRACTICE / NOT PASSED.

**Primary claim to challenge:** interaction evidence must distinguish requested action, pending/unknown outcome, authoritative result, persistence/sync truth, restored projection and recovery; visible controls are not proof of behavior.

**Best entry evidence:**
- `research/interaction/100-stage-3-closure-evidence-compression.md`
- `research/interaction/108-pre-runtime-saturation-and-authority-evidence-stop-rule.md`
- `research/interaction/I087-error-prevention-review-reversal-authority.md`
- `research/interaction/I088-import-preview-duplicate-resolution-commit-authority.md`
- `research/interaction/I090-logmate-synthesis-precedence-and-state-salience-contract.md`
- `research/interaction/106-candidate05-07-authority-contradiction-review.md`

**Do not infer:** exact route/focus/history/recovery execution, Search closure, AT behavior, discoverability, workload, trust or representative-pilot task performance.

**High-value external challenge:** Does the authority model cover ambiguous network/persistence outcomes without enabling unsafe duplicate mutation? Are Undo/Retry/restoration semantics causally correct under interruption and stale projections?

## 5. Web Design / Runtime Transfer

**Current status:** `progress/WEB_STATUS.md` — Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED.

**Primary claim to challenge:** product evidence needs exact provenance and a replication/transfer ladder; lab performance evidence must not be promoted to FIELD Core Web Vitals.

**Best entry evidence:**
- `research/web/113-stage-3-closure-evidence-compression.md`
- `research/web/121-stage3-evidence-saturation-and-execution-priority-gate.md`
- `research/web/W103-logmate-synthesis-runtime-transfer-and-evidence-promotion-gate.md`
- `research/web/W109-production-runtime-degradation-closure-manifest-20260920.md`
- `research/web/W056-accessibility-runtime-closure-harness.md`
- `research/web/W067-repair-to-browser-closure-ladder.md`

**Do not infer:** successful exact-source analyze/tests, Candidate 05/07 runtime closure, independent-engine/native transfer, physical-device/PWA PASS, screen-reader PASS, WCAG conformance or FIELD CWV.

**High-value external challenge:** Is the provenance packet sufficient for reproducibility? Does the proposed ladder separate same-build replication from independent transfer? Which service-worker/offline/update/device cases are missing for a PWA-capable product?

## 6. Content Design / UX Writing

**Current status:** `progress/CONTENT_STATUS.md` — Stage 1–2 PASS; Stage 3 PRACTICE / NOT PASSED.

**Primary claim to challenge:** language is an interface contract; wording must preserve object/state/action/consequence/recovery truth and must not invent or collapse implementation authority.

**Best entry evidence:**
- `research/content/119-stage-3-closure-evidence-compression.md`
- `research/content/127-pre-runtime-saturation-and-semantic-evidence-stop-rule.md`
- `research/content/CD076-end-to-end-localization-and-recovery-semantic-closure-corpus.md`
- `research/content/CD106-error-prevention-review-recovery-content-system.md`
- `research/content/CD107-import-preview-duplicate-resolution-content-system.md`
- `research/content/CD109-logmate-synthesis-semantic-density-and-brand-voice-audit.md`
- `research/content/125-candidate05-07-semantic-invariance-contradiction-review.md`

**Do not infer:** exact visible+a11y runtime parity, production brand voice approval, linguistic review, AT comprehension or representative-pilot comprehension/task PASS.

**High-value external challenge:** Does the semantic taxonomy preserve operational distinctions without creating unnecessary cognitive burden? Which terms require aviation-domain SME review, and which require representative-user comprehension evidence rather than expert copy critique?

## 7. Cross-cutting UX / Accessibility / Human Factors

There is no separate canonical UX specialist. Review must integrate canonical Type, Color, Layout/Interaction, Web and Content evidence rather than creating a sixth ownership silo.

**Shared closure fixtures:**
1. Home → Logbook → record → edit → cancel/commit → Back/Forward.
2. Search A → B → late-A rejection → result → record → Back/restore.
3. Add Flight invalid → correction → commit → persistence failure → Retry.
4. Non-drag reorder → save failure/retry → Undo → reload.
5. Offline create/edit → reconnect → authoritative refresh.

**Evidence boundary:** static expert/model critique may assess internal coherence and identify risks; it cannot establish human discoverability, comprehension, workload, trust, preference, professional acceptability or task performance. Accessibility design review likewise does not establish product WCAG conformance or AT interoperability without implementation evidence.

**High-value external challenge:** Which of the shared fixtures are ecologically valid for pilots? What representative-user sampling, task conditions, error opportunities, environmental conditions and measures are needed before human claims become defensible?

## 8. Cross-domain contradiction and dependency map

| Dependency | Canonical owner | Consumer | Failure if ignored |
|---|---|---|---|
| actual font metrics/fallback | Type | Layout, Content, Web | false fit/reflow conclusions |
| authoritative state/action/recovery | Interaction | Color, Content, Web | misleading success/error/retry semantics |
| protected spatial relationships | Layout | Type, Color, Interaction, Web | state/action cues detach after reflow |
| semantic state salience | Color | Layout, Content, Web | visually quiet design hides consequence |
| canonical wording/semantic payload | Content | Type, Layout, Web | geometry optimized against invented/shortened copy |
| runtime/browser provenance | Web | all peers | screenshots/tests cannot be tied to exact behavior |
| representative human evidence | cross-cutting | all peers | expert judgment mislabeled as usability evidence |

A contradiction found in runtime should be recorded once with exact provenance and handed back to the canonical owner; peer domains should reference that contradiction rather than independently rewriting the same fact.

## 9. Advisory evidence tiers

Use these tiers when asking an outsider to assess a claim:

- **Tier S — source/static:** standards, literature, calculations, static critique, design contracts.
- **Tier R — reproducible implementation/runtime:** exact build/source plus repeatable execution and captured state/geometry/a11y/rendering evidence.
- **Tier T — transfer:** independent engine/platform/device/environment replication where the claim depends on transfer.
- **Tier A — assistive technology:** real AT/browser/platform interoperability evidence.
- **Tier F — field:** representative production telemetry with provenance; for CWV this means representative RUM/aggregate, not Lighthouse/DevTools/CI.
- **Tier H — human:** appropriately sampled representative-user observation/measurement for comprehension, discoverability, workload, trust or task performance.

A higher tier is not universally “better”; it is required only when the claim depends on that evidence class. Reviewers should identify the minimum tier needed to falsify each disputed claim.

## 10. Recommended external-review order

1. Read `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`.
2. Read the relevant specialist status, not the stale global maturity table.
3. Read only the domain entry evidence above.
4. Select 3–5 consequential claims to challenge.
5. For each claim, state current evidence tier, missing evidence tier, plausible counterexample and falsification test.
6. Request underlying raw artifacts only when needed to audit that claim.
7. Return contradictions with exact cited file/section and required next evidence; avoid generic endorsement.

## RELATED DOMAIN CHECK

This map routes evidence across all five official specialist roles and cross-cutting UX/accessibility/human factors. It intentionally does not duplicate the full source arguments. The key newly surfaced contradiction is governance/status drift between coordinator-maintained `progress/STATUS.md` and current specialist statuses.

## HANDOFFS

- **Coordinator:** reconcile `progress/STATUS.md` with specialist status files before using global maturity externally.
- **All specialists:** preserve current evidence boundaries; do not treat this map as gate evidence.
- **External advisers:** use this map to choose claims and evidence, then critique the canonical files rather than the summary alone.
- **Product-transfer work:** attach exact runtime provenance before promoting static claims to runtime/transfer evidence.