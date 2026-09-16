# C026 — W024 six-state rendered semantic matrix audit

Classification: **TRANSFER VALIDATION + CALCULATION CHECK + SYSTEMS PRACTICE**

## Purpose
Extend C025 from sampled unknown/confirmed contexts to the complete W024 state vocabulary without adding new palette breadth.

## RELATED DOMAIN CHECK
- Type T022: ambiguity remains non-color.
- Layout L016/L017: rendered adjacency and narrow geometry determine context.
- Interaction I011/I012: state/action truth is upstream of color.
- Web W024: supplies the actual six-state runtime surface.
- Content CD030/CD031: textual state identity must survive hue loss.
- UX: contrast arithmetic is not human salience/comprehension evidence.

## Authored pair calculation
Independent WCAG 2.x relative-luminance calculations for W024 foreground/background state pairs:

| State | Light | Dark |
|---|---:|---:|
| pending | 8.08:1 | 10.08:1 |
| confirmed | 7.28:1 | 9.93:1 |
| known failure | 8.24:1 | 9.41:1 |
| outcome unknown | 7.13:1 | 10.74:1 |
| offline/stale | 7.22:1 | 9.84:1 |
| conflict | 8.07:1 | 9.70:1 |

All six bounded text/state pairs exceed 7:1 in both authored themes. This is a pair-level calculation, not a global component/accessibility PASS.

## Rendered forced-colors transfer
W024's combined dark + forced-colors run on conflict returned white text/border on black background, with white focus outline. Authored conflict purple disappears, yet `Record conflict` and `Compare versions` preserve the state/recovery meaning. This extends the non-color fallback evidence from C025 to a state where confusing the meaning with generic warning/destructive action would be operationally risky.

## Semantic collision review
KEEP:
- failure remains distinct from outcome unknown;
- offline/stale remains distinct from outcome unknown;
- conflict remains its own semantic namespace;
- pending has no competing recovery color/action;
- forced-colors survival depends on text/structure, not hue identity.

OPEN:
- contextual border/focus contrast for every component adjacency, especially overlapping/sticky surfaces;
- Windows High Contrast and non-Chromium system-color mapping;
- physical display/CVD/low-vision observer evidence;
- human noticeability and state-recognition evidence.

## Stage interpretation
C026 materially broadens Stage 3 system transfer: all six canonical semantic state pairs now have authored light/dark calculations and a coherent Chromium runtime fixture. It still does not close Stage 3 because cross-browser/platform, physical/observer and broader contextual component evidence remain incomplete.

P3 remains deferred; no current product problem justifies increasing gamut complexity before these transfer gaps close.

## HANDOFFS TO OTHER SPECIALISTS
- Web: retain the six-state text/structure fallback and current sRGB system as transfer control.
- Layout: return exact component adjacency when sticky/overlay patterns are added.
- Interaction: keep failure/unknown/offline/conflict action semantics distinct.
- Content: preserve state nouns/actions when hues collapse.

## Verdict
**C026 SIX-STATE AUTHORED/CHROMIUM SYSTEM TRANSFER PARTIAL PASS; Stage 3 remains PRACTICE.**