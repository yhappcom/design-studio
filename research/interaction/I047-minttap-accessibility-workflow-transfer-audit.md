# I047 — MintTap Accessibility Workflow Transfer Audit

Status: TRANSFER VALIDATION / STATIC PRODUCT EVIDENCE; human and AT execution OPEN.

## RELATED DOMAIN CHECK
L051 owns scale/reflow geometry; T029 rendering classification; C060 redundant state; W059 runtime identity; CD065 semantic state language.

## Product workflow under test
Start → Portfolio → Holding → Add Transaction → Insights/ROC/Tax → Settings.

## CRITIQUE
Accessibility is not a collection of isolated screen checks. Enlarged text, localization and partial/ambiguous financial states can change whether actions remain discoverable, focus remains visible, and recovery remains reachable. The production compact-iOS clamp can mask these interaction consequences and therefore must be compared against an unclamped diagnostic scenario rather than accepted as interaction closure.

## Integrated workflow cases
1. Start with no portfolio → create/continue.
2. Portfolio → holding with negative total performance and positive distributions.
3. Add transaction → validation error → correction → success.
4. Async/pending → known failure → retry.
5. Ambiguous outcome → verify/reconcile before retry.
6. Partial/unavailable data → explanation and non-destructive continuation.
7. ROC estimated → final transition without rewriting history as if always final.
8. Tax adjustment positive/negative → consequence and history continuity.
9. Settings locale/currency change → return without losing task context.
10. Destructive action → confirmation/recovery path.

## WCAG/Flutter anchors
WCAG 2.2 adds Focus Not Obscured (Minimum) and Target Size (Minimum) for web. Flutter's current accessibility testing guidance provides Android/iOS target, label and contrast guideline APIs and recommends TalkBack/VoiceOver plus platform inspectors. These are complementary; automated checks do not prove task usability.

## Runtime oracle
For each case capture: initial state, focused/active control, action, announced/visible feedback, resulting state, available recovery, history/back behavior, and whether promotional/ad surfaces interrupt first-value completion. Any silent state change, blind retry after ambiguous outcome, hidden focused control, unreachable recovery, or state wording inconsistent with actual behavior is failure.

## Evidence boundary
No AT, physical-device, discoverability, workload, comprehension or representative-user PASS.

## HANDOFFS
W059 packages traces; Content supplies exact state language; Layout preserves visible adjacency; Color must not be the sole state channel; Type must preserve necessary labels at scale.