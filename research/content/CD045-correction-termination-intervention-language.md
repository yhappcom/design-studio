# CD045 — Correction termination and intervention language

Date: 2026-09-16
Evidence class: **CONTENT SYSTEMS PRACTICE / semantic closure extension**

## RELATED DOMAIN CHECK
I026 owns the actual stop/escalation condition; L030 owns placement; C039 owns visual precedence; W039 owns runtime binding; Type must render chain/object/revision identifiers without ambiguity.

## Semantic IDs
Keep distinct resources for:
- `correctionPending`
- `correctionOutcomeUnknown`
- `correctionConfirmed`
- `correctionNotApplied`
- `correctionStoppedAuthorityChanged`
- `correctionStoppedSafetyUnknown`
- `interventionRequired`
- `viewCorrectionHistory`

## Content invariant
The terminal surface answers, in this order: what object is affected; what is currently known; what the product tried to correct; why automatic correction stopped; what safe action remains; where the user can inspect history.

Do not say “fixed”, “restored”, “failed” or “try again” unless system truth supports that exact claim. `correctionOutcomeUnknown` cannot offer another mutating retry merely to reduce friction. `interventionRequired` must name the safe next step or state that no safe automated action is available.

Localization may alter grammar/order but may not erase operation identity, upgrade uncertainty, collapse intervention-required into generic error, or imply that historical optimistic success is current truth.

## Toolchain cases
When actual localization tooling is available, execute pseudo-expansion, long object IDs, plural/select where used, missing-resource fallback and long localized intervention explanation. Bind resource revision/locale to W039 run IDs.

## HANDOFFS TO OTHER SPECIALISTS
W039 binds resources to runtime states; L030 stress-tests expansion; C039 verifies non-color survival; Type consumes unchanged identifiers/strings as operational proof material.

## Evidence boundary
Static resource contracts are not Flutter/TMS round-trip, linguistic review, comprehension, or human task evidence.
