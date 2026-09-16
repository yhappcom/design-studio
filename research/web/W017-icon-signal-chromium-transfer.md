# W017 — Icon / Non-Text Signal Chromium Transfer

Status: **PRACTICE / CRITIQUE — 12/12 CHROMIUM ASSERTIONS AFTER FAILURE→REVISION**  
Date: 2026-09-16  
Owner: Web Design Specialist

## Purpose

The balance review selected Web because Color and Layout/Interaction are Stage 2 PASS while Type and Web remain Stage 2 PRACTICE, and Web still has uneven browser/runtime evidence. The first target was W015 real Fetch/DOM/network transfer. Two navigation attempts were blocked by the execution environment (`ERR_BLOCKED_BY_ADMINISTRATOR`), so no HTTP/network PASS is claimed. Per the blocker rule, the same Web block moved to the next highest-value executable gap: W011 icon/non-text signal runtime transfer.

Reason for repeat work: **TRANSFER VALIDATION + REPLICATION + CONTRADICTION REVIEW.** W011 defined a non-human validation matrix but did not execute it in a browser.

## RELATED DOMAIN CHECK

### Type
Current Type is Stage 2 PRACTICE with a live LogMate operational-family expansion contract. W017 keeps visible labels under 200% enlargement rather than solving geometry pressure by deleting text. Exact font transfer remains Type-owned.

### Color
Color Stage 2 is PASS. W017 transfers the established resilience principle by checking forced-colors control boundaries and retaining textual warning meaning rather than relying on authored hue.

### Layout / Interaction
Layout/Interaction Stage 2 is PASS. W017 preserves separation among SVG visual owner, button semantic/action owner, disclosure state and controlled region. `aria-expanded` is tested as state, not inferred from chevron appearance.

### Web
Directly transfers W011's executable matrix into Chromium 144.0.7559.96. W016 already established native/custom control behavior; W017 focuses on icon naming, target geometry, enlargement, disclosure and forced colors.

### Content Design
The active Content specialist is Foundation-stage. W017 preserves visible action/warning language and does not substitute icon-only signaling for consequential text.

## Executed harness

Canonical files:
- `W017-icon-signal-chromium-transfer.py`
- `W017-icon-signal-chromium-results.json`

The specimen uses native buttons, decorative SVGs (`aria-hidden=true`), one icon-only button with explicit accessible name, one disclosure control, a textual warning, `currentColor`, 32px minimum control boxes, 200% root text enlargement, keyboard Tab focus and Chromium forced-colors emulation.

Final result: **12/12 assertions PASS**.

Confirmed in this bounded Chromium transfer:
- three controls expose non-empty button names;
- decorative SVGs are removed from the naming path;
- all tested targets remain at least 24×24 CSS px;
- disclosure changes `aria-expanded` and the controlled region together;
- visible labels remain present at 200% text enlargement in the narrow specimen;
- keyboard-Tab focus has a visible solid outline;
- forced-colors emulation preserves a control boundary;
- warning meaning remains explicit text.

## Failure → critique → revision

The first icon harness run reached **11/12**. Keyboard focus visibility failed because the specimen had no explicit `:focus-visible` treatment. This was a specimen defect, not a browser defect.

Adding `:focus-visible` still produced 11/12 when the harness used programmatic `.focus()`. That method did not establish the intended keyboard modality for this check. The harness was corrected to blur and press Tab. Only the final **12/12** run is accepted.

This is useful contradiction evidence: a declared focus style is not sufficient proof if the validation method does not reproduce the input modality the design claims to support.

## Blocked W015 transfer

A real loopback HTTP server and a route-intercepted HTTPS navigation were both attempted before W017. Chromium navigation was blocked by the environment administrator. Therefore this run does **not** claim Fetch/network ambiguity transfer, direct-entry/reload, 404/auth behavior, or real HTTP semantics.

The blocker remains OPEN rather than being replaced by a synthetic network PASS.

## CRITIQUE

### KEEP
- native semantic button ownership;
- visible label + decorative SVG as default;
- explicit accessible name for bounded icon-only exceptions;
- `currentColor` and non-color warning text;
- target box larger than glyph bounds;
- programmatic disclosure state.

### REWORK
- integrated long-localized-label collision testing;
- selected/current/error/pending variants;
- actual browser zoom rather than root-font-size enlargement;
- pointer/touch and tooltip behavior;
- exact accessibility-tree/AT behavior beyond Playwright ARIA snapshot.

### REJECT
- treating an SVG title, hue, glyph shape or hover tooltip as the sole semantic contract;
- claiming network/browser-route evidence from the blocked W015 attempt;
- claiming focus-visible validation from programmatic focus alone.

## Evidence boundary

This is actual Chromium DOM/CSS/accessibility-snapshot/forced-colors transfer, not human recognition, screen-reader speech/navigation, Firefox/Safari parity, physical-device touch behavior, actual OS high-contrast observation, or network transport validation. Human validation remains deferred to app/project stage.

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Confirms in Chromium that disclosure semantics belong to the control/region state contract rather than icon appearance.

### Color
Confirms bounded forced-colors resilience when control boundary and warning meaning do not depend on authored hue alone.

### Type
Confirms the Web implementation should recompose/preserve labels under enlargement rather than silently delete them; exact font geometry remains open.

### Content Design
Consequential status remained textual while iconography stayed supplemental; future wording changes should preserve the same semantic ownership.

## Verdict

W011's runtime gap is materially reduced: **12/12 bounded Chromium assertions PASS after a real failure→revision cycle**. Web Stage 2 remains **NOT PASSED** because the larger Fetch/DOM/network and route/runtime breadth is still blocked/incomplete.
