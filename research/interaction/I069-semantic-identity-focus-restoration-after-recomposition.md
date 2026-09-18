# I069 — Semantic-Identity Focus Restoration After Recomposition

## Purpose
Advance I068 from post-Reset locus observation to an implementation-independent rule for preserving the *same professional object* across reorder, hide/show, Reset and responsive recomposition. Index continuity is not identity continuity.

## RELATED DOMAIN CHECK
Type T021/T050, Color C081, Layout L072, Web W081 and Content CD087 checked. LogMate `b551ce4` confirms the current Customize shell has 35 top-level Known/system items, visible reorder, stable hidden order, system groups, immediate session application and no persistence. This is TRANSFER VALIDATION of the existing transaction/focus chain, not a new ownership structure.

## SOURCE
Flutter's current focus guidance treats FocusNode/FocusScopeNode as long-lived state objects, warns against allocating a new FocusNode on every build because focus may be lost, and states that requested focus changes take effect after the current build phase. FocusScope retains focus history, but that history does not prove application-level semantic identity after list mutation.

WCAG 2.2 remains the accessibility baseline. SC 2.4.11 requires a keyboard-focused component not be entirely hidden by author-created content; this is necessary but weaker than the studio's professional-workflow requirement that the intended field/action remain the locus after a mutation.

## State model
For every mutable Customize item define stable `semantic_id`. Record before and after mutation:
- semantic ID and action ID owning primary focus;
- list/group membership and visible/hidden state;
- semantic order and visual index;
- FocusNode/debug identity when observable;
- focus rectangle, target rectangle, scroll offset and obscuration;
- next available actions and recovery transaction.

Acceptance hierarchy:
1. **same object survives** → restore/retain focus on the same semantic object/action where still valid;
2. **same action disappears but object survives** → choose a deterministic valid action on the same semantic object;
3. **object becomes non-interactive/hidden** → choose a deterministic local recovery locus that preserves task context;
4. **bulk Reset invalidates local locus** → use an explicit Reset/recovery policy, never accidental list-index inheritance;
5. **boundary/no-op** → do not fabricate a focus mutation.

## PRACTICE / CRITIQUE protocol
Run identical vectors for drag, non-drag pointer and keyboard once available: A moves across B/C; A hides; A returns; group A changes projection; Reset; Undo; responsive/200% recomposition. A test that asserts only `index == n` is insufficient. Assert semantic ID before/after and separately record geometry.

Failure examples: focus remains on index 6 but index 6 now represents B; a rebuilt row silently creates a new transient focus node and drops focus; Reset moves focus to page body although a local valid recovery control exists; automatic scroll reveals the focused control but moves the user to an unrelated semantic object.

## Reproducible validation
Repeat each mutation family twice. Classify `IDENTITY-PASS`, `LOCAL-RECOVERY-PASS`, `IDENTITY-FAIL`, `BLOCKED`, or `NOT-EXECUTED`. A WCAG visibility pass does not automatically imply identity pass.

## OPEN
Current LogMate shell has no confirmed non-drag reorder implementation and no persistence/Sync. AT announcement quality, physical-device behavior, discoverability, workload and representative-pilot evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout: measure locus geometry only after semantic owner is known. Web: capture browser active/focus identity and DOM/semantics mapping. Content: status must name the actual affected object/result. Color: focus styling must follow semantic focus owner. Type: do not compress strings to mask locus/reflow failures.