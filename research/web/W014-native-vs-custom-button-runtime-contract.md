# W014 — Native vs Custom Button Runtime Contract

Date: 2026-09-16
Stage: Stage 2 Intermediate Professional Practice
Classification: **TRANSFER VALIDATION + CONTRADICTION REVIEW**

## Question

When a web design visually needs a button, what behavior is inherited from native HTML and what must be rebuilt when a generic element is styled and assigned `role="button"`?

This closes part of the W005 runtime gap without pretending that screen-reader, physical-device, Safari or Firefox evidence exists.

## RELATED DOMAIN CHECK

### Type
T021 is not materially geometry-dependent for this control comparison. Button labels still require exact font/loading/localization transfer later.

### Color
C017/C018 establish semantic state/color systems. This study deliberately does not use color as the sole carrier of focus or state; exact C017 browser transfer remains separate.

### Layout / Interaction
I001 and L010 establish that focus, state and operational ownership require separate evidence. W014 transfers that discipline to browser controls: visual resemblance is not behavioral equivalence.

### Web
W005 identified native/custom control behavior as a Foundation/Stage-2 concern; W010 left browser execution open. W012/W013 established the current rule that runtime claims need assertions and that harness defects must not be mistaken for design defects.

Deliberate repetition reason: **TRANSFER VALIDATION** of established interaction semantics in actual web-control implementation terms, plus **CONTRADICTION REVIEW** of the common assumption that `role="button"` supplies native behavior.

## SOURCE

W3C APG Button Pattern states that a focused button is activated by both Space and Enter and that post-activation focus depends on the action. MDN's ARIA button-role reference states that generic elements using `role="button"` require author-supplied focusability and keyboard handlers, while native `<button>` elements receive keyboard/focus behavior from the browser.

Authoritative references:
- W3C WAI-ARIA APG, Button Pattern: https://www.w3.org/WAI/ARIA/apg/patterns/button/
- MDN, ARIA button role: https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role

## Controlled implementation comparison

Three controls solve the same visible command:

A. Native: `<button type="button">Save</button>`.
B. Incomplete custom: `<div role="button" tabindex="0">Save</div>` with click handler only.
C. Reconstructed custom: same generic element plus explicit Enter/Space handling, Space default-prevention and visible focus styling.

Fixed criteria:
1. sequential keyboard focusability;
2. Enter activation;
3. Space activation;
4. pointer/click activation;
5. semantic role/name exposure in the DOM contract;
6. explicit focus-visible affordance;
7. disabled-state behavior must be separately specified rather than inferred from appearance.

## Findings

### A — native button

**KEEP as default design contract.** It has the smallest authored behavior surface and delegates baseline activation/focus semantics to HTML/browser behavior.

### B — click-only ARIA reconstruction

**REJECT.** `role="button"` changes semantics but does not manufacture native keyboard activation. A control can therefore look like A, appear in the tab sequence, and still fail Space/Enter behavioral parity.

### C — reconstructed custom button

**REWORK / conditional use only.** It can reproduce the bounded button contract, but every behavior becomes authored code and therefore a regression surface. It is justified only when native semantics cannot represent the required interaction, not merely because the visual treatment is unusual.

## STUDIO JUDGMENT

`visual customization != semantic customization != behavioral reconstruction`.

A product may heavily restyle a native button without abandoning its native element. The decision to replace the element must therefore be made from semantic/behavioral requirements, not from appearance.

For project reviews, require an explicit reason whenever a generic element replaces a native control. "Needed custom styling" is insufficient by itself.

## Reproducible assertion plan

A browser harness should assert independently:
- Tab reaches each enabled control in intended order;
- native A activates on Enter and Space;
- incomplete B does not satisfy the complete keyboard contract;
- reconstructed C activates exactly once on Enter and Space;
- pointer click activates all enabled controls exactly once;
- focus remains visible under `:focus-visible`;
- disabled native behavior and `aria-disabled` custom behavior are not treated as interchangeable without explicit event suppression/focus policy;
- accessible role/name is inspected with browser accessibility tooling when available.

The repository connector used in this run can write source artifacts but does not execute Playwright/Chromium. Therefore the above is a **reproducible contract and source-grounded contradiction review, not an executed browser PASS**. No execution count is fabricated.

## OPEN

- execute the assertion harness in Chromium when an executable environment is available;
- inspect accessibility tree role/name/state rather than inferring AT output;
- Firefox/Safari parity;
- actual screen-reader behavior;
- touch/physical-device behavior;
- native/custom select, checkbox, radio and dialog comparisons;
- forced-colors and enlarged-text transfer;
- human findability/recognition remains deferred to app-development validation.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Confirms the I001/L010 principle that semantics, focus and behavior are distinct assertions. A visually identical custom control can carry a larger operational failure surface.

### Color
Focus/state color tokens must be layered onto a correct control contract; color cannot repair missing keyboard behavior.

### Type
Restyling a native button does not itself require replacing the semantic element, so typography/font customization should not be used as justification for custom control reconstruction.

## Stage consequence

W014 narrows the W005 native/custom gap and establishes an implementation-review rule, but Web Stage 2 remains **NOT PASSED** because this run could not execute the browser harness. Highest-value next Web work is executable W014 control transfer or W006 integrated async/recovery runtime evidence.