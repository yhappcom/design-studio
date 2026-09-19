# T081 — LogMate Search/Retrieval Rendering Stress

Date: 2026-09-20

## RELATED DOMAIN CHECK
I099/L103/C112/W112/CD118 checked. T081 owns rendering constraints only. T021 remains the upstream custom drawing gate.

## PRACTICE CORPUS
Stress mature proportional/fallback rendering with product-authored English plus source/user Unicode:
- `Search logbook`, `Flight number`, `Registration`, `Departure`, `Arrival`;
- `KE123`, `HL8083`, `RKSI → RKPK`, `1:35`, dates under the existing T076 contract;
- `Searching…`, `18 results`, `No results`, `Search unavailable`, `Working offline`, `Retry`, `Clear search`, `Filters`;
- long registration/source labels, mixed punctuation, numerals and user/source text.

Capture actual family/fallback, advance, wrap, truncation, line height and L103 protected geometry at baseline/narrow/enlarged/text-spacing states.

## CRITIQUE RULES
Search fit cannot justify negative tracking, glyph narrowing, semantic abbreviation, reduced enlargement or premature kerning. Operational mono is permitted only for already-approved comparison roles; search controls/status do not become mono merely for visual identity.

T021 remains frozen-width/sidebearing, kerning-OFF drawing work. Required sequence remains **drawing → general spacing → residual kerning**.

## FAILURE CONDITIONS
Fallback changes result identity readability; truncation hides differentiating operational tokens without recovery; typography makes status look like a result; active result relies on weight alone where state semantics are needed; layout fit is achieved by violating the T021 sequence.

## EVIDENCE BOUNDARY
No custom-font, exact production mono, search-runtime, cross-browser, AT or human recognition PASS is claimed.