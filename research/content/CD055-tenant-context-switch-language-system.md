# CD055 Tenant Context Switch Language System

Evidence mode: **STAGE 3 SYSTEMS PRACTICE / TRANSFER VALIDATION**.

## Goal
Keep identity, tenant/workspace context, object availability and authorization semantically distinct during context switches and stale-cache recovery.

## SOURCE
OWASP distinguishes authentication from authorization and requires exact-object/request authorization. Multi-tenant guidance requires verified tenant context; therefore a displayed workspace name or authenticated session alone cannot support copy that asserts access to a particular object/action.

## RELATED DOMAIN CHECK
I036 owns context/action truth; L040 owns hierarchy/focus; C049 owns visual encoding; W049 owns runtime/cache evidence; Type must render unchanged strings with mature fallback until T021 closes.

## Semantic resources
Keep separate concepts/resources for:
- `currentContextConfirmed`
- `switchingContext`
- `contextAuthorityUnavailable`
- `showingPriorContextData`
- `objectNotAuthorizedInCurrentContext`
- `objectUnavailableInCurrentContext`
- `actionUnavailableUntilContextConfirmed`
- `contextSwitchFailed` only when failure is established
- `contextSwitchOutcomeUnknown` when outcome is ambiguous

Do not collapse these into generic “Access denied”, “Not found”, “Signed out”, or “Switch failed”. Do not say “Your data” when tenant/workspace ownership is the relevant scope.

## Localization contract
Context names are data, not translatable UI copy. Resource grammar must tolerate long names, bidi isolation where applicable, pseudo-expansion and locale change during/after switch. Do not concatenate fragments such as `Switching to` + context name when target languages require different grammar; use parameterized complete messages.

## Retrieval/export
History and export must identify the context/snapshot provenance without implying it is the viewer's current context. A prior-context record remains historical truth even after access is revoked, subject to product/security policy on whether it may be displayed.

## Validation matrix
Pseudo-expansion; missing-resource/fallback; A→B and rapid A→B→A; same object ID across contexts; authorization denied vs object unavailable; context authority unavailable; offline stale content; export/history. Actual Flutter/TMS/ARB round trip remains required.

## Evidence boundary
No localization-toolchain, linguistic-review, AT or human comprehension/task PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W049 binds resource revision/locale to runtime context; L040 stress-tests long strings; C049 ensures meaning survives cue removal; Type must not alter semantic strings to rescue provisional geometry.