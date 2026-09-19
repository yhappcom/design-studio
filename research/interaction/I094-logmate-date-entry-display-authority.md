# I094 — LogMate Date Entry / Display Authority

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Separate canonical date identity, editable control state, display representation and commit truth for H3.

## RELATED DOMAIN CHECK
T076, C107, L098, W107 and CD113 checked. Existing I093 record/focus/action continuity is reused.

## AUTHORITY CHAIN
`canonical date identity ≠ localized/browser display ≠ editable control text/UI ≠ validated draft ≠ committed record ≠ persisted/synced state`.

Browser-native date controls may display locale-dependent UI while exposing a normalized date value. An application-authored formatted string may use an explicit locale. Neither visible ordering nor width proves commit/persistence.

## PRACTICE
Validate: open existing record → focus date → edit → invalid/valid state → cancel/commit → route leave/return → Undo where supported. Repeat with native-control and authored-display representations where the product actually uses them. Preserve record ID, field identity, focus/recovery ownership and canonical date through representation changes.

## CRITIQUE
Do not parse product truth back from a localized display string when a canonical value already exists. Do not treat browser formatting change as user mutation.

## SYNTHESIS
Date representation belongs to presentation; mutation authority belongs to the record/state model. This boundary prevents locale/browser behavior from becoming accidental business logic.

## OPEN
Actual LogMate date-control implementation, user preference policy, physical iPad/mobile behavior, AT and human comprehension.

## HANDOFFS TO OTHER SPECIALISTS
- Content: label/format explanation must reflect actual date policy.
- Layout: width adaptation cannot change edit/recovery ownership.
- Web: provenance must capture canonical value and rendered presentation separately.