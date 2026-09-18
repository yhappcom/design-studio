# I067 — Reset Baseline Provenance & Commit Boundary

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION + CONTRADICTION REVIEW** of I066. A Reset action is not defined until its target baseline and commit boundary are explicit.

## RELATED DOMAIN CHECK
Type T048 protects recovery strings; Color C079 separates invalidation states; L070 models recovery lifetime; W079 owns served-runtime interruption evidence; CD085 protects Reset≠Undo≠erase. No separate UX owner exists.

## SOURCE
WCAG 2.2 remains the W3C conformance baseline. Guideline 3.2 requires predictable operation; SC 3.2.2 constrains unexpected context changes caused by changing a control. W3C supplemental cognitive guidance recommends predictable back/undo and avoiding loss of prior work. These sources do not select a LogMate Reset policy; that is product truth.

## Problem
`Reset` can mean factory defaults, current preset defaults, session-entry state, last saved state, or last synced state. Those are materially different targets. I066 cannot close Reset/Undo interaction while the baseline is anonymous.

## Baseline model
Record `baseline_id`, `baseline_kind`, `baseline_version`, `source`, `captured_at`, `current_order`, `current_visibility`, `dirty_relative_to_baseline`, `commit_boundary`, `undo_relation`.

Candidate baseline kinds to test rather than assume:
1. product default;
2. named preset default;
3. session-entry snapshot;
4. last persisted user configuration — future only;
5. last reconciled/synced configuration — future only.

## Required sequences
- customize → Reset → compare exact semantic order/visibility with declared baseline;
- customize A → customize B → Reset;
- move → Undo → Reset;
- move → Reset → Undo attempt;
- Reset while already at baseline;
- navigate away/back before and after Reset;
- future only: persistence/sync version changes baseline while a session is open.

## Acceptance
- Reset target is identified by semantic baseline, never by current list indices.
- No-op Reset creates no fake mutation/success history.
- Reset does not erase flight data or entry-field configuration.
- Undo relationship to Reset is explicit and deterministic.
- Navigation does not silently change which baseline Reset targets.
- Future persistence/sync truth cannot be inferred from local application.

## CRITIQUE
A generic Reset label can appear simple while concealing a high-impact provenance decision. Conversely, adding confirmation to every Reset may add friction without evidence. Confirmation, preview, Undo, or immediate reset must be selected from actual consequence/risk and runtime evidence.

## OPEN
Current LogMate persistence/Sync truth is absent. No Reset baseline policy, confirmation policy, runtime, AT or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
Content receives baseline naming/consequence truth; Layout receives reset/recovery surface pressure; Color receives no-op/changed/invalidated states; Web receives navigation/version manifest requirements; Type receives final strings only after semantics are fixed.