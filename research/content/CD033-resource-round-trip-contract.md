# CD033 — Bounded ARB Resource Contract

Evidence type: PRACTICE / CRITIQUE / DEPENDENCY / OPEN

## RELATED DOMAIN CHECK
I014 owns outcome truth; L019 owns expansion geometry; C028 owns non-color/focus evidence; W026 binds runtime capture IDs; Type must accept required literals later. This study does not claim linguistic or human comprehension evidence.

## Executed artifact
`CD033-resource-contract-fixture.arb` is a concrete ARB-format fixture containing semantic message IDs, metadata, a plural placeholder and a date/time placeholder. The three save-state titles deliberately preserve pending, outcome-unknown and known-failure distinctions from I013/I014.

## Round-trip gate
A real resource gate requires more than valid-looking JSON. Required execution is: parse ARB with the target localization toolchain; generate resources; render plural/date-time cases using authoritative locale data; export/import or equivalent deterministic reconciliation; compare message IDs, placeholders, metadata and semantic revision; then bind the generated message to W026 capture IDs.

## Reconciliation invariants
Message IDs are stable identifiers; translators must not merge unknown outcome with known failure; placeholders must survive with type/role intact; source changes require semantic revision tracking; locale formatting is produced by locale data/tooling rather than hand-authored English assumptions.

## Current result
**CONCRETE FIXTURE CREATED / REAL ARB ROUND TRIP OPEN.** Connector-only GitHub writing cannot execute Flutter gen-l10n, ICU locale data or a TMS. Therefore CD029's production resource gate is not closed.

## HANDOFFS TO OTHER SPECIALISTS
W026 binds generated message ID/revision when executable. L019 stress-tests expansion. I014 reviews any wording that implies retry/commit truth. UX integration keeps linguistic review and human comprehension OPEN.