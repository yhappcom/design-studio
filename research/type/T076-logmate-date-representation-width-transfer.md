# T076 — LogMate Date Representation Width Transfer

Status: **STAGE 2 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Resolve the Type side of H3 without using provisional custom metrics or kerning to force date strings into a preferred ledger width.

## RELATED DOMAIN CHECK
C106, I093/L097, W106 and CD112 checked. Web/browser date display and application-authored date formatting are separate realizations; canonical date identity must not be inferred from rendered width.

## SOURCE
HTML date controls normalize the underlying value to `yyyy-mm-dd` while user-visible presentation can vary with browser/OS locale. `Intl.DateTimeFormat` can produce locale-sensitive application-authored representations. Therefore one stored date can legitimately produce different visible strings and widths.

## PRACTICE
Stress one canonical date identity across at least:
- `2026-09-19` canonical numeric form;
- compact numeric ordering variants used only as test fixtures;
- month-name realization such as `Sep 19, 2026`;
- browser-native date-control presentation;
- enlarged text and text-spacing override;
- proportional UI face and exact mature mono control/fallback.

Measure rendered width, wrapping and alignment, but do not treat equal width as semantic equivalence.

## CRITIQUE
Failure modes: narrowing glyphs, negative tracking, premature kerning, or replacing a required date representation solely to preserve a fixed column. These hide a Layout/Content decision inside Type.

## SYNTHESIS
Date width is a representation variable. Type must provide defensible metrics and fallback behavior; Layout decides how variable width is absorbed, Content defines allowed representation, and Web verifies actual browser/runtime realization.

## OPEN
- Exact production mono/fallback (H1).
- Exact product date-display policy and any user preference.
- Actual browser/native widths in production runtime.
- Human scan/comprehension evidence.

T021 remains upstream: widths/sidebearings frozen, kerning OFF; drawing → general spacing → residual kerning.

## HANDOFFS TO OTHER SPECIALISTS
- Layout/Web: size date zones from real mature-font/browser realizations, not provisional T021 metrics.
- Content: do not shorten/change date semantics to rescue a preferred width.
- Color: date-width adaptation must not alter semantic-state salience.