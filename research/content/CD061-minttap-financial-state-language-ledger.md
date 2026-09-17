# CD061 — MintTap Financial State Language Ledger

Status: **TRANSFER VALIDATION / PRODUCT CONTENT SYSTEM / TOOLCHAIN + HUMAN EVIDENCE OPEN**  
Date: 2026-09-17  
Stage relevance: Stage 3 systems practice

## Question

How should a financial product preserve distinct economic concepts, evidence states and recovery language across dense dashboard, detail, entry, history and settings surfaces without letting brevity or layout pressure change product truth?

## SOURCE / PRODUCT EVIDENCE

MintTap product-transfer work exposes several concepts that are visually adjacent but semantically different:

- portfolio value;
- invested capital / cost basis;
- total performance;
- cumulative distributions;
- recovery/payback rate;
- gross vs net distributions;
- ROC estimate vs issuer-final ROC;
- tax refund/additional-tax adjustment;
- exchange-rate basis and date;
- ready / estimated / partial / unavailable data.

CD060 established that these concepts must not be collapsed. C055 separately shows that outcome polarity, certainty/finality and availability are independent semantic axes. I042 keeps actual state/action/recovery ownership in Interaction. T024 and L046 establish that required qualifiers must survive large-text recomposition rather than being shortened away.

## SYNTHESIS — semantic ledger

A product-wide content system should maintain at least these fields for every high-value financial message:

| Field | Question |
| --- | --- |
| object | What value/event is being described? |
| measure | Value, amount, rate, basis, adjustment, etc.? |
| scope | Portfolio, holding, distribution, tax year, transaction? |
| polarity | Positive, negative, zero, unknown? |
| certainty | Actual, estimated, provisional, final? |
| availability | Ready, partial, unavailable, failed? |
| basis | Gross/net, USD/KRW, exchange-rate basis, tax basis? |
| time | As-of, payment date, settlement date, year? |
| consequence | What changes because of this state? |
| action | What can the user do now? |
| recovery | If incomplete/failed, how can the user continue? |

Displayed wording may omit a field only when the omitted meaning is already unambiguous in the immediate semantic context. It must not be omitted merely to fit a preferred row geometry.

## Required language distinctions

### Outcome vs cash flow

`Cumulative distributions` is cash received/distributed. It is not automatically `profit` or `return`.

`Total performance` may be positive or negative independently of cumulative distributions.

### Gross vs net

Gross and net are calculation bases. A toggle or label must make the active basis recoverable from the current surface and from exported/history contexts where ambiguity would matter.

### Estimated vs final

`Estimated ROC` and issuer-final ROC are not interchangeable. Finality must be explicit where it changes tax-adjustment eligibility or interpretation.

### Partial vs unavailable

`Partial` means some relevant evidence exists but completeness is limited. `Unavailable` means the value cannot currently be established. Neither should be rewritten as generic `error` unless the underlying Interaction state is actually failure.

### Tax adjustment

A refund/additional-tax adjustment is a separate settlement event. It should not be silently merged into the label for an ordinary distribution. The user-facing language must preserve sign/direction, settlement date, amount/currency, and exchange-rate basis when those affect interpretation.

## PRACTICE — integrated MintTap Product Lab contract

The synthetic Product Lab should exercise at least:

1. high cumulative distributions + negative total performance;
2. positive and negative outcomes;
3. zero values;
4. KRW and USD long values;
5. gross and net states;
6. estimated ROC;
7. final ROC with tax-adjustment availability;
8. partial/unavailable exchange-rate or estimate state;
9. transaction save consequence;
10. history/export context where the original surrounding UI is absent.

For each scenario, Content should verify that the user-facing string still identifies the correct object/state/basis and does not borrow meaning from color or position alone.

## CRITIQUE

This ledger is a semantic-system artifact, not proof of comprehension. It does not establish:

- optimal English phrasing;
- Korean/Japanese/other linguistic naturalness;
- translation quality;
- screen-reader comprehension;
- representative investor understanding;
- trust or preference;
- production ARB/TMS round-trip integrity.

Those remain separate evidence gates.

## RELATED DOMAIN CHECK

### Type
T024 supplies the large-value/long-label stress corpus. Required qualifiers must survive nonlinear text scaling; Content must not shorten truth to rescue geometry.

### Color
C055 separates identity, financial polarity, certainty and availability. Content provides redundant non-color semantics for those axes.

### Layout / Interaction
L046 preserves semantic adjacency after reflow. I042 owns actual state, action, consequence and recovery; Content only names/explains those truths.

### Web
W055 must verify that accessible names, browser semantics, localization and runtime wrapping preserve the same ledger fields where material.

### UX integration
End-to-end coherence requires the same financial concept to retain meaning across Portfolio → Holding → Add Transaction → Insights/ROC/Tax → History/Settings, even when surface wording differs.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Use ledger-required strings as immutable semantic stress strings during scaling/raster checks.

### Color
Do not use color to replace `estimated`, `partial`, `unavailable`, sign or finality language.

### Layout / Interaction
Treat qualifier-value adjacency and save/recovery consequence as protected semantic groups.

### Web
Bind content checks to W055 scenario/build identity and report truncation, accessible-name or locale realization discrepancies.

## Gate effect

CD061 strengthens Stage 3 product-system transfer. Stage 3 remains **PRACTICE / NOT PASSED** until actual localization/toolchain realization, implemented-product QA, linguistic review where required and appropriate human evidence are obtained.