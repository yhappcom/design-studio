# L047 — Accessibility Reflow and Protected Semantic Groups

Status: TRANSFER VALIDATION / PRACTICE
Date: 2026-09-17

## SOURCE
WCAG 2.2 baseline retains reflow/resize requirements; WCAG guidance frames 320 CSS px as the narrow reflow reference for web content. Flutter exposes text scaling, high contrast, accessibility-service and window information through MediaQuery/SafeArea primitives.

## PRODUCT PRACTICE
Define protected groups that may change geometry but not semantic order: label→value→basis/qualifier; outcome→scope→period; field→error→correction; state→action→recovery. At narrow width or large text, pairs become stacks before text shrinks or qualifiers disappear. Sticky/navigation/ad surfaces may not obscure focused controls or split first-value groups.

## CRITIQUE
Responsive success is not 'no overflow'. A layout can fit while separating a qualifier from its value, moving recovery away from an error, or placing monetization inside a decision block. Those are semantic layout failures.

## REPRODUCIBLE VALIDATION
Use exact W055 build/scenario IDs. Capture narrow/wide, default/max text scaling, long locale strings, keyboard focus, partial/unavailable and negative/ambiguous scenarios. Record reading order, focus visibility, protected-group adjacency, two-dimensional scrolling and first-value/ad boundary.

## RELATED DOMAIN CHECK
T025 defines string/render pressure; C056 state redundancy; I043 focus/recovery continuity; W056 executable evidence; CD062 content-state contract.

## Gate effect
No Stage 3 PASS until runtime artifacts and representative-human evidence required by the curriculum exist.