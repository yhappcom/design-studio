# CD025 — Executable content-system transfer

Classification: **STAGE 3 PRACTICE / EXECUTED STRUCTURAL VALIDATION**

## Purpose
Execute the bounded CD024 contract rather than adding another prose-only schema. This block serializes a small professional-record message inventory, implements deterministic lint, runs a mutation suite, and records what the execution does and does not prove.

## RELATED DOMAIN CHECK
- **Type:** latest T022 dual-track work preserves operational strings as typed material. CD025 therefore treats flight numbers as `operational_literal`, not localizable prose.
- **Color:** C023 makes verbal/non-color state identity necessary under forced-color and non-text transfer. CD025 does not use hue as a state oracle.
- **Layout / Interaction:** I009 remains authoritative for `pending`, `confirmed`, `known_failure`, `outcome_unknown`, `offline_stale` and safe recovery. CD025 consumes those state distinctions rather than inventing a parallel state machine. L014's qualifier-preservation rule is retained as a later rendered-transfer dependency.
- **Web:** W021 is execution-ready but browser runtime is blocked in the current connector environment. CD025 therefore executes only content-structure checks and leaves browser reflow/bidi/status binding OPEN.
- **Content:** CD020–CD024 define schema, inventory stress, cross-channel continuity, governance and the executable target. CD025 is deliberate **TRANSFER VALIDATION + REPLICATION BY EXECUTION**, not another conceptual summary.

## Artifacts
- `CD025-bounded-content-inventory.json` — five-message bounded inventory with semantic registries, typed variables, channel policy and English/pseudo/RTL fixtures.
- `CD025-content-lint.py` — deterministic structural lint + mutation suite.

## Bounded inventory
The executable set deliberately includes:
1. save pending;
2. save confirmed;
3. save known failure;
4. save outcome unknown;
5. offline/stale data.

It is intentionally small enough to inspect and large enough to exercise the highest-risk distinctions from CD011–CD024.

Operational literals use `flight_number` with `localize=false` and `bidi_isolate=true`. The external projection for outcome-unknown is `current_state_sensitive` and requires revalidation.

## Executed baseline
The serialized baseline was loaded and run through the lint logic.

Result:

`baseline: PASS []`

This means the bounded inventory produced zero structural failures under the implemented rules. It is **not** a claim of linguistic, browser, native, translator, AT or human quality.

## Executed mutation suite
Six intentionally corrupted variants were executed to prove that the checker can reject known bad structures rather than merely return PASS on its own fixture.

| Mutation | Expected failure | Observed |
|---|---|---|
| unregistered state `savingish` | `UNKNOWN_STATE` | detected |
| confirmed English fixture drops `{flight_number}` | `MISSING_VARIABLE` | detected |
| operational flight number marked localizable | `LITERAL_LOCALIZED` | detected |
| outcome-unknown changed to blind retry | `UNSAFE_BLIND_RETRY` | detected |
| actionable notification loses revalidation | `EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING` | detected |
| RTL confirmed fixture removes LTR isolation | `RTL_LITERAL_NOT_ISOLATED` | detected |

All six mutation expectations were observed in execution.

## What became stronger than CD024

### 1. The schema is no longer hypothetical
CD024 said a future runner should reject structural defects. CD025 proves a bounded serialized inventory can be consumed by deterministic checks and that the checks distinguish a valid baseline from six controlled invalid mutations.

### 2. Outcome-unknown safety is machine-checkable at one layer
The runner rejects `state_id=outcome_unknown` combined with `action_id=retry_save`. This does not prove the product backend is safe, but it prevents one class of content/configuration regression from silently authorizing blind retry.

### 3. Channel freshness is part of content configuration
An actionable notification must carry freshness + revalidation policy in this bounded model. Removing revalidation is a deterministic failure rather than a reviewer's optional comment.

### 4. Literal identifiers are first-class metadata
A flight number cannot be marked as freely localizable prose, and RTL fixtures must include explicit isolation around the literal placeholder. This operationalizes the Type/Content/i18n boundary.

## CONTRADICTION / limitation found during execution
CD024's required-failure list is broader than this first runner. The current implementation does **not yet prove**:
- certainty strengthening by comparing multiple channel projections semantically;
- incompatible message-ID reuse across version history;
- fallback deletion of consequence/recovery/safe action through a formal semantic-diff engine;
- actual +30–40% geometric expansion tolerance;
- actual bidi rendering correctness;
- count/date-time/duration locale formatting correctness.

The correct conclusion is therefore **partial executable coverage**, not “CD024 fully passed.”

## STUDIO JUDGMENT — validation ladder
For content-system infrastructure, evidence should progress through:

`schema review → serialized fixture → structural lint → negative/mutation tests → rendered transfer → runtime/state integration → localization workflow → AT/human evidence where the claim requires it`

A linter that only passes a golden fixture is weak evidence. Mutation/adversarial cases are required to demonstrate that failure conditions are actually reachable.

## Next executable gap
The highest-value next Content work is not another conceptual taxonomy. Extend the runner with:
1. versioned semantic-contract snapshots to detect incompatible ID reuse;
2. per-channel semantic assertions preventing certainty strengthening;
3. fallback semantic requirements for certainty/consequence/recovery/safe action;
4. typed plural/date-time/duration fixture validation;
5. a generated fixture package consumable by W021 without Web inferring state from English.

Actual text expansion, clipping, focus/status behavior and bidi rendering remain Web/runtime transfer work. Native Flutter behavior remains separately OPEN.

## HANDOFFS TO OTHER SPECIALISTS

### Web
Consume `message_id`, `state_id`, typed variables and locale fixture rather than parsing English. Return actual rendered pseudo/RTL/reflow/status contradictions to Content.

### Interaction
I009 remains authoritative. If the product authorizes a different safe action for outcome-unknown, update the state/action contract first; Content lint should then change to match it rather than independently redefining safety.

### Type
Use the literal `flight_number` fixture and future registration/airport/time literals as shaping/metric stress material. Localization metadata must not rewrite those values as prose.

### Layout
The runner can prove qualifiers exist in the message source; only rendered transfer can prove they remain perceivable after reflow. Do not resolve overflow by deleting certainty/recovery qualifiers.

### Color
No content-system PASS depends on authored color. Verbal state identity remains independent.

## Evidence boundary
**EXECUTED:** JSON serialization, deterministic baseline lint, six controlled mutation detections.  
**NOT EXECUTED / OPEN:** browser rendering, actual bidi layout, actual pseudo-expansion geometry, native runtime, TMS/translator workflow, notification delivery, screen reader/AT, human comprehension/trust/task performance, backend/network truth.

Stage 3 remains **PRACTICE / NOT PASSED**.
