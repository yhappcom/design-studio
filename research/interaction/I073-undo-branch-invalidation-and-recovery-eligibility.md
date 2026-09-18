# I073 — Undo branch invalidation and recovery eligibility

## Question
After an Undo changes configuration history, what happens when the user performs a new mutation before any older recovery path is invoked? I072 protected newer focus/action agency; I073 extends that protection to the **history branch itself**.

## RELATED DOMAIN CHECK
- **Type:** T054 keeps causal-recovery strings subordinate to T021 drawing → spacing → kerning gates.
- **Color:** C085 separates restored/current-focus/newer-agency/recovery states.
- **Layout/Interaction:** I065–I072 define transaction identity, Undo scope, baseline provenance, semantic focus ownership and intervening-action causality; L076 measures geometry only after semantic ownership is known.
- **Web:** W085 requires transaction eligibility and current focus owner in served-runtime evidence.
- **Content:** CD091 requires inverse transaction, eligibility and intervening-action truth; unavailable, failed and superseded are distinct.
- **Purpose:** `TRANSFER VALIDATION` of the existing causal model into branching history; not a repetition of single-step Undo.

## Sources and boundary
**SOURCE — Flutter focus:** FocusScope keeps a focus history and may return focus to a previously focused node; focus requests take effect after build. Framework focus history is therefore real runtime state, but it is not the product's configuration Undo history and must not be treated as such.

**SOURCE — WCAG 2.2:** WCAG remains the accessibility baseline. Predictability/focus/status criteria constrain observable behavior, but WCAG does not prescribe an application Undo-stack algorithm.

**STUDIO JUDGMENT:** Branch semantics below are a product-contract hypothesis requiring runtime and later human validation.

## Branch model
Represent each accepted configuration mutation as `tx_id`, with `parent_tx_id`, `inverse_of`, `branch_id`, `eligibility`, and `projection_hash`.

Sequence:
1. `S0 --A--> S1`
2. `S1 --B--> S2`
3. `Undo(B) --> S1` (`U_B`, inverse_of=B)
4. user performs new mutation `C`: `S1 --C--> S3`

At step 4 the old forward branch containing B is no longer the current causal branch. Unless the product explicitly implements Redo/history navigation, a recovery affordance must not silently target B as though it were still the current inverse candidate.

### Required distinctions
- `eligible`: inverse target is still on the current recovery branch and prerequisites hold.
- `consumed`: inverse already applied.
- `superseded`: a newer branch-defining mutation replaced the recovery path.
- `no-op`: invocation would produce no semantic change under the defined contract.
- `failed`: eligible operation was attempted but did not complete.

These states are not interchangeable.

## Acceptance matrix
| Scenario | Required history result | Focus/agency rule |
|---|---|---|
| A → B → Undo B | B consumed; A may remain eligible per product scope | invocation locus/current agency preserved per I071/I072 |
| A → B → Undo B → C | C becomes current branch head; B must not reappear as ordinary Undo target | C/current focus agency wins |
| A → Undo A → no-op interaction | no branch fork unless interaction mutates configuration | no fabricated history |
| A → Undo A → focus-only move | focus change alone does not resurrect A or create config tx | newer focus agency preserved |
| A → Undo A → Reset | Reset is its own transaction/baseline contract; prior recovery eligibility must be explicit | Reset locus policy applies |
| stale recovery control invoked | no hidden mutation; status reports unavailable/superseded truth | do not steal focus merely to report status |

## Reproducible runtime ledger
For every step capture: `scenario_id`, `step`, `tx_id`, `parent_tx_id`, `branch_id`, `inverse_of`, `eligibility_before/after`, `semantic_order`, `visibility`, `projection_hash`, `current_focus_semantic_id/action_id`, `invocation_locus`, `status_payload`, `runtime_exception`.

Run each executable family twice. A repeated final projection without matching branch/eligibility provenance is not replication.

## Critique / failure conditions
FAIL if:
- a consumed/superseded transaction remains visually or programmatically actionable as current Undo;
- a stale control mutates a non-current branch without explicit history-navigation semantics;
- focus-only activity is incorrectly recorded as configuration mutation;
- a new configuration mutation is discarded because an older Undo path was assumed authoritative;
- status says failed when the action was actually unavailable/superseded;
- branch repair moves focus back to an older object despite newer user agency without explicit workflow rationale.

## UX integration
This reduces a professional-workflow risk: an operator can make a correction, Undo it, continue editing, and otherwise be exposed to a recovery control whose causal target no longer matches the visible work. The analysis is non-human; predictability/comprehension/workload remain OPEN.

## OPEN
- actual LogMate non-drag reorder + Undo implementation;
- whether product exposes one-level Undo, stack Undo, or any Redo/history UI;
- primary/independent browser execution, 200%, forced colors;
- screen-reader, physical-device and representative-pilot evidence.

## HANDOFFS TO OTHER SPECIALISTS
- **Content:** expose `eligible/consumed/superseded/no-op/failed` without inventing persistence.
- **Color:** stale/superseded recovery must not retain success/actionable paint.
- **Layout:** disappearing/replaced recovery controls need stable locus without semantic deception.
- **Web:** browser manifest must record branch and eligibility provenance, not only final state.
- **Type:** new recovery wording is transfer corpus only; do not compress unfinished Type to fit it.
