# W016 — Native vs Custom Button Chromium Transfer

Date: 2026-09-16  
Stage: Stage 2 Intermediate Professional Practice  
Classification: **TRANSFER VALIDATION + REPLICATION + CONTRADICTION REVIEW**

## Question
Does W014's source-grounded native/custom button contract survive actual Chromium keyboard, pointer, focus-visible and accessibility-snapshot execution?

## RELATED DOMAIN CHECK

### Type
Current Type status is Stage 2 PRACTICE. Exact label geometry remains Type/Web production transfer work; this test intentionally holds typography irrelevant to control semantics.

### Color
Color Stage 2 is PASS. Focus is not validated by color contrast here; the bounded assertion checks that the keyboard-focused native control matches `:focus-visible` and receives a non-none outline. Exact C017 palette transfer remains separate.

### Layout / Interaction
Layout/Interaction Stage 2 is PASS. I001/L010's separation of visual appearance, focus, semantics and behavior is directly transferred. This study does not redefine interaction ownership.

### Web
W014 explicitly left browser execution OPEN. W012/W013 established that runtime claims need executable assertions and that harness defects must be separated from product defects. W015 added deterministic state execution but did not close browser runtime breadth. W016 therefore executes the exact next gap rather than adding theory.

Deliberate repetition reason: **TRANSFER VALIDATION** of W014 in Chromium, **REPLICATION** of its three-control comparison, and **CONTRADICTION REVIEW** of the assumption that `role="button"` provides native activation.

## SOURCE refresh
Fresh official-source verification on 2026-09-16 found the contract unchanged: W3C APG requires Space and Enter activation for a focused button, while MDN states that adding `role="button"` does not provide typical button functionality such as click/keyboard handling and recommends native HTML buttons where possible.

References:
- https://www.w3.org/WAI/ARIA/apg/patterns/button/
- https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Reference/Roles/button_role

## Executed method
Canonical harness: `W016-native-custom-button-chromium-transfer.py`.  
Canonical result: `W016-native-custom-button-chromium-results.json`.

Environment: Playwright Python driving system Chromium **144.0.7559.96**, headless.

Controls:
- A native `<button type="button">`;
- B `<div role="button" tabindex="0">` with click handler only;
- C same generic element with explicit Enter/Space reconstruction.

Assertions cover sequential Tab focus, Enter/Space activation, pointer activation count, native `:focus-visible` outline, and Playwright ARIA snapshots for role/name.

## Executed result
**14/14 assertions PASS.**

Observed:
- Tab sequence reached native → incomplete custom → reconstructed custom.
- Native activated exactly once on Enter and Space.
- Click-only ARIA control activated zero times on Enter and Space despite being focusable and exposed as a button.
- Reconstructed custom activated exactly once on Enter and Space.
- All three activated once by pointer click.
- Keyboard focus on the native button matched `:focus-visible` and computed a solid outline.
- ARIA snapshots exposed all three as named buttons.

This directly demonstrates the key W014 distinction in Chromium: **semantic exposure does not imply behavioral parity**.

## Harness failure → correction evidence
The first run was 12/14 because a reset click at `(1,1)` itself hit/focused the native button, shifting the subsequent Tab sequence. After replacing that reset, the run became 13/14; the remaining focus-visible assertion failed because programmatic blur retained the browser's tab-cycle position. The final harness reloads the controlled document before the focus-visible assertion and reaches 14/14.

These were harness defects. They are preserved as critique because treating them as control defects would have produced a false conclusion.

## CRITIQUE

### KEEP
Native button as the default command control. In this bounded Chromium transfer it provides focusability and keyboard activation without authored reconstruction.

### REWORK / conditional
Custom role=button only when the semantic/behavioral need cannot be represented by a native element. It requires explicit keyboard and disabled/focus policy and expands regression surface.

### REJECT
Click-only `role="button"` as a substitute for native behavior. Chromium exposed the role/name while Enter/Space activation remained absent.

## Evidence boundary
This is actual Chromium runtime evidence, not universal browser or AT proof. Playwright `aria_snapshot()` verifies Chromium/Playwright accessibility representation for the bounded elements; it does not prove screen-reader speech or navigation. Disabled-state parity, Firefox/Safari, physical touch/device behavior, screen readers, forced-colors, enlarged text and human findability remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Confirms under actual Chromium that focusability/role exposure and activation behavior are separate contracts. A control can satisfy semantic exposure while failing keyboard action.

### Color
A visible focus token must attach to a behaviorally correct control; color cannot compensate for missing activation behavior.

### Type
Font/label styling does not justify replacing native semantics. Exact typography can be transferred independently after Type's family metrics stabilize.

## Stage consequence
W016 closes W014's principal Chromium execution gap and materially strengthens Web Stage 2 runtime breadth. Web Stage 2 remains **NOT PASSED**: W015 still needs real Fetch/DOM/network transfer, true HTTP direct-entry/reload remains open, W011 icon/accessibility runtime remains incomplete, and Firefox/Safari/AT/device breadth is not established.

Highest-value next Web work, if balance selects Web again, is W015 real browser/network transfer rather than another source-only control study.
