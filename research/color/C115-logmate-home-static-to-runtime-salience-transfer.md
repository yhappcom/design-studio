# C115 — LogMate Home static→runtime semantic-salience transfer

Date: 2026-09-20
Purpose: **TRANSFER VALIDATION / PROJECT APPLICATION**
Upstream: C114 and the latest Home white-canvas draft review.

## RELATED DOMAIN CHECK
Type T083/T084, Interaction I101, Layout L105, Web W114, Content CD120 checked. The Home draft is a concrete fixture, not proof of runtime state behavior.

## Project evidence
The draft deliberately uses a warm neutral canvas and scarce brand green, rejects a large colored hero, and states that functional focus/selection/error/recovery outrank brand accent.

## PRACTICE — salience budget
For the coded Home, classify every colored element before aesthetic tuning:
1. orientation/current location when applicable;
2. focus;
3. consequence-bearing state (invalid/error/unknown/recovery);
4. active selection/control state;
5. informational status;
6. brand accent;
7. decoration.
Higher-numbered roles may not visually outrank lower-numbered consequence-bearing roles merely to make the screen feel premium.

The current static fixture contains almost no negative/error state, so a visually successful static render is weak evidence for C114. Runtime promotion requires injected focus, invalid/error, offline/pending and recovery specimens without changing the base composition.

## CRITIQUE / falsifiers
FAIL if:
- brand green becomes the only cue for selection/current/focus;
- scarcity of chrome also removes necessary non-color state boundaries;
- night theme is produced by naive inversion that changes semantic rank;
- forced-colors destroys state identity because the design relied on authored color alone;
- success color appears before authoritative persistence/sync evidence.

## Validation ladder
Static render → state-injected static critique → coded light/night → forced-colors → enlarged/text-spacing with actual font fallback → runtime pending/error/recovery. Record semantic IDs and non-color boundaries with screenshots/computed state; do not call this WCAG conformance or human salience evidence.

## HANDOFFS
Web should capture the state-injected Home under the same provenance packet as W114. Layout must preserve non-color grouping when decorative fills are absent. Content must not use color-dependent instructions.

## OPEN
Actual coded states, forced-colors/browser/device transfer, calibrated-display/glare/night evidence, representative-human salience/comprehension.