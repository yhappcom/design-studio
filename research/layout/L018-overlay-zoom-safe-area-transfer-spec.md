# L018 — Overlay, 200% Zoom and Safe-Area Transfer Specification

Evidence type: SYNTHESIS / PRACTICE / TRANSFER VALIDATION / OPEN

## RELATED DOMAIN CHECK
L017 proved bounded 1280/390/320 no-horizontal-overflow geometry in Chromium. C027 identifies focus/overlap adjacency as the next color dependency. W024 is the executable integrated surface. I012 owns action truth. CD031 owns state wording. T022 metrics remain unsuitable for numeric width freeze.

## Next-stage geometry matrix
The next spatial transfer must combine, rather than separately micro-test: 200% browser zoom; 320 CSS px-equivalent reflow; sticky header/footer; software-keyboard-reduced viewport where executable; safe-area inset simulation; long/localized strings; and focus traversal to every recovery action.

Pass conditions are structural: no essential control clipped or unreachable; no horizontal two-dimensional scrolling for ordinary text/task content; focused actions not fully obscured by authored layers; state title, consequence and recovery action preserve reading order; fixed/sticky regions do not consume the remaining task viewport; and safe-area padding does not create inaccessible off-screen actions.

## Design judgment
The current 320px result is not a substitute for 200% zoom. Likewise a CSS safe-area simulation is not physical-device evidence. These evidence classes remain separate.

## Current result
**SPECIFICATION COMPLETE / EXECUTION OPEN.** Human workload, discoverability and physical keyboard/device behavior remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Color consumes actual overlap adjacency. Web executes the combined matrix. Content supplies long/localized strings without geometry-driven semantic shortening. Interaction validates focus/action order. UX integration checks whether recovery remains coherent across viewport disruption.
