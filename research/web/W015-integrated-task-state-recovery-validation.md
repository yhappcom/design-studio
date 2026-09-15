# W015 — Integrated Task-State Recovery Validation

Status: **PRACTICE / CRITIQUE — DETERMINISTIC EXECUTION, BROWSER TRANSFER OPEN**  
Owner: Web Design Specialist  
Canonical path: `research/web/`

## Question
Can W006's complete-surface distinctions survive an executable state model without collapsing filtered-empty, invalid, pending, confirmed, known-failure, outcome-unknown, partial and stale/offline states into generic `loading/error/success`?

Reason for repeat work: **TRANSFER VALIDATION + INDEPENDENT VALIDATION + CONTRADICTION REVIEW.** W006 is a design contract and I002 owns the interaction semantics; W015 independently executes a Web-owned integrated model rather than re-summarizing either study.

## RELATED DOMAIN CHECK

### Type
Checked current `progress/TYPE_STATUS.md`. Type is Stage 2 PRACTICE and its latest broader-family transfer falsified a shared-cap spacing model. Reusable lesson: implementation convenience must not be mistaken for sufficient semantic/design resolution. W015 does not freeze text geometry or claim production-font transfer.

### Color
Checked current `progress/COLOR_STATUS.md` (Stage 2 PASS). C017/C018 support semantic state systems but color cannot repair a false state model. W015 deliberately validates state meaning without depending on color.

### Layout / Interaction
Checked current `progress/LAYOUT_STATUS.md` (Stage 2 PASS) and `I002-latency-pending-optimistic-retry.md`. W015 transfers I002's accepted/pending/confirmed/failed/outcome-unknown distinctions into a complete Web task surface. It does not redefine Interaction ownership.

### Web
Checked W006 and W012–W014. W012/W013 provide actual Chromium transfer in other areas; W014 explicitly leaves execution open. W015 targets the next status-listed executable gap: W006 integrated task-state/recovery execution.

## Executed method

`W015-task-state-recovery-model.py` implements a minimal deterministic surface with independent dimensions for data/results, criteria, editable input/validation, operation state, retry safety and freshness. It runs fixed assertions rather than screenshots or taste judgments.

Executed locally with Python 3. Result: **17/17 assertions passed**. Canonical output is `W015-task-state-recovery-results.json`.

Validated invariants:
- filtered-zero remains distinct from initial/failed acquisition and retains query criteria;
- invalid submission preserves input and does not enter pending;
- valid submission enters pending without exposing retry as safe;
- confirmed completion is explicit;
- known non-commit failure can expose a retry-safe path in this bounded model;
- outcome-unknown is not mislabeled failure and blocks blind retry pending verification;
- partial refresh preserves prior usable data while marking incompleteness;
- offline/stale mode preserves cached data while exposing freshness provenance.

## CRITIQUE

### KEEP
Independent state dimensions and the W006/I002 rule that `known failure != outcome unknown`. The deterministic model demonstrates that these distinctions are implementable without one global page enum.

### REWORK
The model is intentionally small. It has no concurrent edits, request cancellation, operation IDs, real HTTP status/transport ambiguity, focus/status announcements, URL criteria persistence or region-level DOM ownership. Those belong in browser/network transfer rather than being inferred from this oracle.

### REJECT
A single `loading | error | success` page state as the default architecture for a search/filter/edit surface. It cannot truthfully represent the simultaneously valid combinations exercised here.

## Evidence boundary

This is **reproducible deterministic model validation**, not browser proof. No claim is made about Fetch, AbortController, DOM events, native form submission, browser history, accessibility tree, screen readers, service workers, real offline transitions, Firefox/Safari, or physical devices. Human task/perceived-speed evidence remains deferred to project/app validation and is not simulated.

## HANDOFFS TO OTHER SPECIALISTS

### Interaction
W015 independently confirms that I002's outcome-unknown distinction remains necessary when embedded in a Web search/edit surface. Real API idempotency and operation-identity transfer remain open.

### Color
Semantic pending/failure/unknown/freshness tokens should map onto these distinct states rather than merge them by visual similarity.

### Type
Status/recovery labels are structural content. Exact production font/fallback/localization geometry should be tested only after Type's current family/spacing work stabilizes.

## Conclusion
W006's integrated state/recovery contract survives a deterministic executable transfer at **17/17 assertions**. This materially strengthens Web Stage 2 practice, but it does not close the principal Web weakness: actual browser/network/accessibility runtime breadth.

Next Web work, if balance selects Web again, should prefer a browser-executable W014/W015 transfer or W011 icon/accessibility harness when the environment permits. If browser execution remains unavailable, do not manufacture a PASS; re-evaluate Type Stage 2 and the Stage 3 entry needs of Color/Layout.
