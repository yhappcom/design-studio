# CD093 — Undo-scope command language contract

## PURPOSE
Advance the complete content system from branch eligibility to simultaneous history scopes and shortcut semantics.

## RELATED DOMAIN CHECK
I074 owns contextual Undo routing; L078 owns spatial association; C087 owns visual reinforcement; W086 owns runtime provenance; T055 owns rendering constraints.

## SOURCE / SYNTHESIS
WAI-ARIA APG documents Ctrl+Z / Command+Z as conventional Undo assignments. Flutter Actions/Shortcuts resolves an intent through focused context. Therefore the string `Undo` cannot itself select which history mutates.

## CONTENT MODEL
Source payload:
`command=undo + invocation_path + scope_id + eligible_inverse + changed_object + result + current_focus + persistence_truth`.

Protected distinctions:
- configuration Undo ≠ text-editor Undo ≠ browser Back;
- shortcut recognized ≠ action eligible;
- unavailable ≠ failed ≠ superseded;
- Undo applied ≠ Saved/Synced;
- current focus ≠ recovery owner;
- conventional chord ≠ universal global history.

## PRACTICE
English/Korean architecture should support unqualified `Undo` when scope is unambiguous and scope-qualified realization when simultaneous histories make ambiguity material. Do not prematurely freeze literal translations; actual EN/KO runtime and linguistic review remain OPEN.

Candidate semantic patterns for later testing include object/consequence qualification rather than implementation jargon, e.g. recovery of display arrangement versus edited text. Visible brevity and richer accessibility payload may differ while preserving the same truth.

## CRITIQUE
Reject strings that imply a stale inverse remains available, use “Back” as a synonym for Undo, announce “Saved” for local mutation, or expose `scope_id` engineering terminology to users without need.

## VALIDATION
Feed identical semantic payloads through button and shortcut invocation. Verify message truth does not change merely because input path changes. Stress 200%, compact widths and EN/KO. Human comprehension, shortcut discoverability and linguistic quality require later human review.

## HANDOFFS TO OTHER SPECIALISTS
Type receives truthful scope-qualified stress strings; Layout receives minimum semantic content; Color receives exact eligibility states; Web must verify visible and accessibility payloads from actual resolved scope.
