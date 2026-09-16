# CD026 — Versioned semantic diff, channel invariance and fallback execution

Classification: **STAGE 3 PRACTICE / EXECUTED STRUCTURAL TRANSFER VALIDATION**

## Purpose
Extend CD025 beyond single-snapshot structural lint into version-aware semantic governance, cross-channel certainty invariance, fallback semantic preservation and typed locale-sensitive variables.

## RELATED DOMAIN CHECK
- **Type T022:** operational identifiers remain literal typed material; CD026 keeps them separate from locale-formatted count/date-time/duration values.
- **Color C023:** state meaning remains verbal/structural and is not inferred from hue.
- **Layout L014 / Interaction I009:** I009 remains authoritative for lifecycle certainty and safe action. CD026 checks that channel projection cannot mutate that certainty; L014 remains authoritative for rendered preservation under reflow.
- **Web W021:** browser execution is still OPEN in the current environment. CD026 produces deterministic fixtures that can later be bound to W021 without inferring state from displayed English.
- **Content CD023–CD025:** CD023 defined semantic identity/change propagation; CD024 specified executable failures; CD025 proved bounded single-snapshot lint and mutation detection. CD026 deliberately extends rather than repeats those checks.

## Executed model
A versioned JSON fixture adds:
- previous semantic-contract snapshots for stable message IDs;
- explicit certainty values on eligible channel projections;
- typed `count`, `datetime`, `duration`, and `operational_literal` variables;
- semantic annotations on source and fallback realizations.

The runner compares current records with previous contracts across:
`concept_id`, `state_id`, `action_id`, `certainty`, required semantic set and variable signature.

A changed contract under the same stable message ID is rejected as `INCOMPATIBLE_MESSAGE_ID_REUSE`. This is intentionally stricter than wording comparison: wording may change while semantic identity remains stable; semantic identity may not silently change because English happens to remain plausible.

## Cross-channel certainty rule
Each eligible channel projection declares or inherits authoritative certainty. If a notification/email/history projection changes `unknown` to `failed`, `confirmed`, or any other different certainty, lint emits `CHANNEL_CERTAINTY_MISMATCH`.

This is structural evidence for the invariant, not proof that a real notification runtime obeys it.

## Fallback semantic-preservation rule
Locale/fallback fixtures declare the semantic requirements they realize. The checker rejects any realization that drops required certainty, object, safe action, freshness, count or time-context semantics.

This does not judge translation quality. It proves only that the declared semantic contract and required placeholders survive the bounded fixture.

## Typed locale-sensitive variables
CD026 separates:
- `operational_literal` — not freely localized as prose;
- `count` — locale-realized numeric/count value;
- `datetime` — locale-realized temporal value;
- `duration` — locale-realized duration value.

The checker rejects unknown variable types and rejects count/date-time/duration values incorrectly marked as non-localized literals. Actual CLDR formatting correctness remains outside this structural runner.

## Execution result
The clean baseline produced **zero lint errors**.

Seven adversarial mutations were then executed. All seven produced the expected failure class:

| Mutation | Expected failure | Result |
| --- | --- | --- |
| change `record.save.confirmed` certainty while reusing ID | `INCOMPATIBLE_MESSAGE_ID_REUSE` | PASS — detected |
| strengthen outcome-unknown notification to failed | `CHANNEL_CERTAINTY_MISMATCH` | PASS — detected |
| fallback drops certainty/safe-action semantics | `FALLBACK_SEMANTIC_LOSS` | PASS — detected |
| count marked non-localizable | `LOCALIZABLE_TYPE_MARKED_LITERAL` | PASS — detected |
| datetime replaced by unknown type | `UNKNOWN_VARIABLE_TYPE` | PASS — detected |
| duration placeholder removed from fallback | `MISSING_VARIABLE` | PASS — detected |
| actionable external projection loses revalidation | `EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING` | PASS — detected |

Therefore the CD026 runner is not only self-consistent against a golden fixture; it rejects controlled violations of version, channel, fallback and typed-variable contracts.

## SYNTHESIS
A production-grade content system needs at least two independent identities:
1. **semantic identity** — what product truth/action/consequence a message represents;
2. **linguistic realization** — how a locale/channel expresses that identity.

A string diff cannot reliably stand in for a semantic diff. Conversely, a semantic diff does not establish linguistic quality.

## STUDIO JUDGMENT
Treat message IDs as semantic API identifiers, not convenient translation keys. A wording-only revision can retain identity; a material state/action/certainty/required-semantics/variable-schema change requires explicit migration, versioning or a new semantic ID rather than silent reuse.

Fallback is also a semantic operation, not merely a missing-string convenience. A fallback that removes the qualifier distinguishing unknown from failed is invalid even if it is grammatically fluent.

## CONTRADICTION / LIMIT
CD026 does **not** prove:
- actual locale plural categories;
- locale-specific date/time/duration formatting;
- grammatical agreement around typed variables;
- actual bidi shaping/order;
- +40% rendered geometry;
- notification delivery/freshness behavior;
- browser/native binding;
- translator comprehension;
- screen-reader/AT behavior;
- human comprehension/trust/task performance.

Those remain separate evidence classes.

## HANDOFFS TO OTHER SPECIALISTS
- **Web:** consume `message_id`, `state_id`, certainty and typed variables directly when W021 runtime execution becomes available; do not derive state from English text.
- **Interaction:** CD026 confirms a structural guard against certainty mutation but does not redefine I009 lifecycle behavior.
- **Layout:** rendered fallback/expansion may not delete required semantics to regain fit.
- **Type:** operational literals remain a distinct data class; count/date-time/duration are locale-formatted content and may change width substantially.
- **Color:** certainty identity remains available independently of semantic color.

## Gate effect
Stage 3 evidence is materially stronger: executable validation now covers bounded single-snapshot integrity, adversarial mutation, versioned semantic identity, cross-channel certainty, fallback semantic requirements and typed locale-sensitive variables.

Stage 3 remains **PRACTICE / NOT PASSED**. The next high-value Content block is production localization workflow architecture: source-of-truth ownership, TMS handoff, translator context, state/message versioning, review/QA gates, fallback/release policy and change propagation. Runtime browser/native/AT/human evidence remains OPEN and must not be simulated.
