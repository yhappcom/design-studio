# T077 — Cross-surface signature transfer: type contract

Date: 2026-09-20
Status: PRACTICE / CONTRADICTION REVIEW

## Question
How can SC-A Calibrated Axis and SC-B Operational Dual Voice transfer across Home, View Logbook, Activity, Add Flight, import/review, and recovery surfaces without turning one screen's typography into a template?

## Sources and inherited evidence
- Signature Code Study: SC-A is local semantic calibration, not global coordinates; SC-B is a role distinction, not a mono aesthetic.
- T021 remains the upstream custom-type gate: drawing before general spacing before residual kerning.
- WCAG 2.2 remains the accessibility baseline; enlarged text and text-spacing transfer remain required evidence.

## Practice: transfer matrix
A signature transfer is typographically valid only when all applicable surfaces preserve these roles:
1. Product language: mature proportional text.
2. Operational comparison tokens: mature mono only where comparison stability is materially useful.
3. Source/user-authored text: fallback-safe proportional by default; do not coerce to mono for identity.
4. Numeric comparison: tabular figures may support a local axis but do not solve mixed alphanumeric comparison.
5. State/action/recovery text: preserve semantic clarity before compactness.

The same font size, weight, line-height, or mono percentage is NOT required across surfaces. Home summary, ledger rows, forms, import mapping, and recovery states have different density and hierarchy jobs.

## Critique / falsification
FAIL transfer if any of the following occurs:
- mono is spread to headings/body merely to make screens look related;
- operational identifiers lose distinction because proportional and mono roles collapse;
- a narrow layout is rescued by negative tracking, glyph narrowing, premature kerning, or semantic abbreviation;
- fallback changes destroy comparison geometry without the layout adapting;
- source/user strings are clipped to preserve a visual signature;
- enlarged/text-spacing states require a different semantic reading order.

## Reproducible validation
Use one shared fixture across Home, ledger, Activity, Add Flight, import/review, and recovery: dates, flight numbers, registrations, DEP/ARR, durations, PIC/SIC/PF/PM, long remarks/source labels, destructive/recovery strings. Record actual loaded font, feature settings, line boxes, wraps/truncation, comparison-axis geometry, and fallback result at baseline + enlarged text + WCAG text-spacing.

## Gate consequence
No Type stage promotion. T021 remains upstream. This study permits transfer testing with mature production/fallback faces; it does not authorize custom LogMate metrics or kerning.