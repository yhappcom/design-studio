# C022 — Exact pair calculation and collision audit

Classification: **EXECUTED VALIDATION + TRANSFER PREPARATION**

## RELATED DOMAIN CHECK
- Type T021 has reached executable architecture PASS but bespoke A/B drawing FAIL; color is not used to repair identifier ambiguity.
- L013/I008 require state identity and safe action to survive recomposition.
- W021 is the browser transfer target for these aliases.
- CD021 requires verbal certainty/state identity independent of hue.

## Method
WCAG 2.x relative-luminance contrast was calculated from the exact C021 sRGB hex pairs using sRGB channel linearization and `(Llighter + 0.05)/(Ldarker + 0.05)`. This is a deterministic numeric audit of authored pairs, not browser, physical-display, CVD or human evidence.

## Exact results
| Role | Light contrast | Dark contrast |
|---|---:|---:|
| primary text | 16.29:1 | 16.89:1 |
| secondary text | 7.76:1 | 11.49:1 |
| action | 7.67:1 | 13.35:1 |
| confirmed | 7.28:1 | 9.93:1 |
| known failure | 8.24:1 | 9.41:1 |
| outcome unknown | 7.13:1 | 10.74:1 |
| offline/stale | 7.22:1 | 9.84:1 |

All listed foreground/background text pairs exceed 7:1 in this calculation. This does **not** imply that every future component, icon, border, disabled state, focus indicator, overlay or composited surface passes; each rendered pair still requires its actual background.

## Collision audit
1. `known failure` and destructive action must remain different semantic tokens even if a later palette gives them related red-family hues.
2. `outcome unknown` cannot be collapsed into generic warning because I008 changes permitted action: blind retry remains blocked.
3. `offline/stale` is not equivalent to outcome-unknown. Local persistence may be known while server freshness is not.
4. Focus remains a separate interaction role and must be checked against every adjacent rendered surface; the current C021 focus row is intentionally not reducible to one contrast number because its background is contextual.
5. Status colors remain separate from data-series palettes.

## Transfer gate
C021 candidate text/state pairs are numerically mature enough for W021 transfer. Web must test computed styles under light/dark, forced colors, focus, pseudo-localization and recomposition. Forced-colors acceptance remains semantic/control/focus survival, not authored-hue preservation.

## Verdict
**C022 exact text-pair calculation: PASS for the bounded C021 pairs. Stage 3 remains OPEN.** Browser transfer, non-text contrast in actual components, P3/fallback, physical displays, CVD/low-vision observers and human salience remain unproven.

## HANDOFFS TO OTHER SPECIALISTS
- Web: transfer these exact aliases; test contextual focus/non-text pairs rather than assuming this table covers them.
- Layout/Interaction: preserve state/action distinctions under recomposition.
- Content: keep explicit state labels and safe-action language.
- Type: no color dependency is introduced.