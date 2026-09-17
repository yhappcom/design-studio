# W066 — First Executed MintTap Runtime Failures

Evidence class: **TRANSFER VALIDATION / EXECUTED-FAIL**

## OBSERVED EVIDENCE
Run `35255971379` on MintTap commit `27b8f3938350ed83e1380511bc357d0929b7f171` passed checkout, Flutter 3.47.4 setup, dependency resolution and severity-aware analysis. The widget matrix then executed for the first time and failed all three scenarios.

1. 390×844 baseline: `RenderFlex overflowed by 9.3 pixels on the right`.
2. 390×844 at 2.0 text scale with long/negative/partial/KRW stress: `RenderFlex overflowed by 47 pixels on the right`.
3. 1024×768 workflow: repeated Flutter assertions that `ListTile` ink/background may be invisible because a background-colored `DecoratedBox` sits between the tile and nearest `Material`.

Web build and manifest remained NOT EXECUTED because the widget step failed. Artifact upload succeeded.

## CRITIQUE
This is the first genuine product-lab runtime evidence in the chain. The phone failures are spatial/composition failures, not analyzer or Type-kerning failures. The wide failure exposes a Material/ink layering contract that can hide interaction feedback even when static appearance seems acceptable.

## RELATED DOMAIN CHECK
Type: do not compensate the overflows with kerning. Color: selected/ink feedback visibility depends on layer ownership. Layout: compact composition needs recomposition. Interaction: hidden ink/splash is feedback loss. Content: strings should not be shortened merely to silence overflow.

## HANDOFFS TO OTHER SPECIALISTS
Layout should locate the overflowing row and recompose; Interaction/Web should correct Material ownership around ListTile surfaces. Type and Content should preserve their existing contracts during repair.

## OPEN
No Web build/browser, independent engine, AT, physical-device, field LCP/INP/CLS or human PASS is claimed.