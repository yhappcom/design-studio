# CD063 — Complete Financial Content Acceptance

Status: STAGE 3 PRACTICE / TOOLCHAIN-READY CONTRACT

## PURPOSE
Unify forms, states, onboarding, retrieval/history/export, tone and localization into one executable content acceptance model for the financial product transfer.

## CONTENT SYSTEM
Every user-facing string is classified by object, measure, scope, polarity, certainty, availability, basis, time, consequence, action and recovery as applicable. The same dimensions must survive visible UI, accessible names/announcements, validation/errors, history/export and locale changes.

## SCENARIOS
Onboarding/empty portfolio; add/edit transaction; validation failure and correction; high-income + negative total performance; zero; estimated vs final ROC; partial/unavailable data; tax adjustment; history/export; KRW/USD; long localized labels; pending/ambiguous/retry states where the underlying product supports them.

## ACCEPTANCE
Do not use distribution as a synonym for profit/return. Gross/net and estimated/final remain explicit when material. Partial/unavailable is not rewritten as zero. Error copy names the problem and valid recovery only when the Interaction contract supports it. Tone never overstates certainty. String shortening may remove redundancy but not semantic dimensions needed for financial truth.

## TOOLCHAIN CONTRACT
CD059 remains OPEN until these strings complete a real Flutter localization/ARB/TMS-equivalent round trip. The run must preserve keys/placeholders/plurals/selects, capture source and rendered locale output, and log discrepancies/revisions. Static translations do not equal toolchain PASS or linguistic review.

## RELATED DOMAIN CHECK
T026 owns render/fallback pressure; C057 visual state redundancy; L048/I044 grouping/recovery; W057 runtime artifacts. Content does not redefine underlying state truth.

## HANDOFFS TO OTHER SPECIALISTS
Any fit problem goes to Type/Layout first. Any ambiguous state goes to Interaction. Any visual-only state goes to Color. Any implementation mismatch goes to Web.

## OPEN
No real localization round trip, linguistic review, AT comprehension or representative-human task evidence is claimed.