# CD092 — Recovery branch eligibility language contract

## Purpose
Extend CD091 from intervening-action causality to I073 branch replacement. Content must describe the recovery action that is **currently eligible**, not the one that used to be eligible.

## RELATED DOMAIN CHECK
Type T054/T021, Color C086, Layout L077, Interaction I073 and Web W085 checked. This is `TRANSFER VALIDATION`; Interaction remains owner of branch/eligibility truth.

## Source-truth payload
`current_tx_id`, `branch_id`, `eligible_inverse_tx_id`, `eligibility_state`, `changed_object_id`, `result`, `current_focus_object/action`, `recovery_scope`, `persistence_truth`, optional `position/group/visibility`.

Strings never infer eligibility from the previous displayed message.

## Protected invariants
- eligible ≠ consumed ≠ superseded ≠ no-op ≠ failed;
- Undo applied ≠ Saved/Synced;
- restored object ≠ focused object;
- changed object ≠ recovery-control locus;
- branch replacement ≠ failure;
- hidden ≠ deleted;
- display configuration ≠ flight data.

## Message-system practice
For `A → B → Undo B → C`, the visible concise message may report C's actual consequence and expose only C's currently valid recovery action. A richer accessibility payload may include object/result/position where useful. It must not continue to announce an Undo for B if B is no longer eligible.

If a stale control is invoked, wording must follow actual Interaction truth: `unavailable` or `superseded` when that is known, not a generic `Couldn't undo` failure. If product chooses to silently remove stale controls, no message is invented solely to narrate internal history.

## Localization stress
English/Korean runtime corpus should include concise and expanded forms for move/hide/show/reset/undo, eligibility loss, no-op and boundary rejection. Variables are typed; semantic IDs and professional abbreviations are not constructed by English word order. At 200%, necessary consequence wording may wrap rather than be shortened into false certainty.

## Accessibility / tone
Status information should be available without forcing focus merely to announce it. Avoid chatty repeated announcements for internal branch bookkeeping. Human AT comprehension and announcement preference remain OPEN.

## Failure conditions
FAIL if copy advertises stale recovery, calls supersession a failure, fabricates focus return, says Saved/Synced without persistence truth, or shortens away a material consequence/recovery distinction.

## OPEN
Actual EN/KO product strings, runtime localization, linguistic review, screen-reader comprehension and representative-pilot task evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Type receives real branch/recovery strings as later transfer corpus; Layout receives worst-case wrapping; Color receives semantic eligibility names; Web must compare visible and accessibility payloads against I073 runtime truth.
