# C060 — MintTap Locale/Polarity Product-Transfer Audit

Status: TRANSFER VALIDATION / CONTRADICTION REVIEW; runtime execution OPEN.

## RELATED DOMAIN CHECK
T029/T028 define truth-bearing numeric/string pressure; L050/I046 preserve adjacency and state; W059 owns runtime proof; CD065 owns semantic labels.

## Product evidence
MintTap `lib/localization/trend_color_scheme.dart` defines locale-dependent signed trend colors: default positive green / negative red, while Korean/Japanese positive is red and negative blue. Zero uses a neutral color. The isolated lab separately defines brand mint, positive/negative, warning/info, and estimated/partial/unavailable roles.

## CRITIQUE
Locale-aware market convention is a legitimate presentation concern, but sign meaning cannot be recoverable only from the locale-dependent hue. The source already preserves numeric sign, which is useful redundancy. The lab's separation of brand from outcome polarity and availability/certainty is structurally stronger than treating one accent as generic success.

A specific contradiction case remains mandatory: high cumulative distributions with negative total performance. Both can be simultaneously true; neither brand mint nor distribution emphasis may imply overall positive performance.

## Acceptance matrix
Static and later runtime review must include: positive, negative, zero; ko/ja versus other locale convention; high-income + negative total return; estimated/final; partial/unavailable; gross/net; tax adjustment. For every case, remove hue mentally or via grayscale/high-contrast diagnostics and verify the state remains recoverable from sign, label, icon/shape or explicit wording.

## WCAG boundary
WCAG 2.2 is the current baseline. Automated contrast or grayscale diagnostics do not establish human comprehension. Flutter's current accessibility guidance also recommends colorblind/grayscale testing.

## Evidence boundary
No rendered contrast, forced/high-contrast, device gamut, calibrated display, observer or human PASS. Source inspection establishes architecture/risk only.

## HANDOFFS
Content must keep explicit state words where hue loss would otherwise erase meaning. Layout must preserve those labels adjacent to values. Web must capture actual computed/rendered colors and accessibility state under W059.