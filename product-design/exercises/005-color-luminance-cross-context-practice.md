# Exercise 005 — Color and Luminance Cross-Context Practice

Status: CRITIQUE COMPLETE / further rendered-device evidence still required for foundation PASS.

## Purpose

Test whether hierarchy survives removal of hue, adverse viewing conditions, and transfer between unrelated information contexts. This exercise operationalizes `research/008-color-luminance-contrast-hierarchy.md`; it does not define a house palette.

## Standards baseline

WCAG 2.2 distinguishes color dependence, text contrast, and non-text contrast. For normal text the AA contrast floor is 4.5:1; large text has a 3:1 floor. Color must not be the only visual means of conveying information. WCAG 2.2 focus appearance additionally gives a useful stress criterion for visible focus: an indicator area at least equivalent to a 2 CSS-pixel perimeter and 3:1 change contrast.

Primary references:
- https://www.w3.org/TR/WCAG22/#use-of-color
- https://www.w3.org/TR/WCAG22/#contrast-minimum
- https://www.w3.org/TR/WCAG22/#non-text-contrast
- https://www.w3.org/TR/WCAG22/#focus-appearance

## Context A — operational departure board

Information set: destination, scheduled time, gate, status, one selected row.

### Variant A1 — hue-dependent (REJECT)

- all text uses similar luminance;
- status is distinguished only by green/amber/red;
- selected row is blue text only;
- separators carry most grouping work.

Failure prediction: grayscale removes status meaning and selection. A user with reduced color discrimination must infer state from position or memory.

### Variant A2 — luminance-first (KEEP)

Semantic channels:
- destination/time: primary text, highest stable text contrast;
- gate: secondary but still comfortably readable;
- status: explicit word plus icon shape; hue is redundant enhancement;
- selected row: 2 px outline plus selection marker, not hue alone;
- separators: low priority because alignment and spacing establish groups.

Representative contrast probes, calculated from WCAG relative-luminance formula:

| Foreground | Background | Ratio | Role | Judgment |
| --- | --- | ---: | --- | --- |
| `#111111` | `#FFFFFF` | 18.88:1 | primary text | KEEP |
| `#595959` | `#FFFFFF` | 7.00:1 | secondary text | KEEP |
| `#767676` | `#FFFFFF` | 4.54:1 | quiet normal text | boundary case; REWORK if thin/small |
| `#A0A0A0` | `#FFFFFF` | 2.61:1 | decorative rule only | REJECT for required text/component boundary |
| `#005FCC` | `#FFFFFF` | 6.23:1 | accent text | KEEP for text, but not sole state signal |

Ratios are evidence for conformance floors, not proof of hierarchy quality.

### Stress: simulated glare

Model the failure as loss of subtle tonal differences rather than pretending a screenshot reproduces real glare. Remove the faint separator and compress secondary/primary differentiation. Required state remains recoverable because status has words/icons and selection has geometry.

KEEP: explicit status, outline selection, alignment.
REWORK: any metadata sitting close to the 4.5:1 floor if it is operationally important.
REJECT: subtle rules as the only row grouping.

### Stress: low light

Avoid turning the entire surface into maximum black/white contrast. Preserve strong local text contrast but reduce large-area luminance jumps. Accent frequency is reduced so status does not become a field of glowing chroma.

## Context B — reading/research library

Information set: article title, author/date metadata, reading status, saved state, topical tag.

This context deliberately has a different perceptual objective: sustained reading and calm scanning rather than rapid operational exception detection.

### Variant B1 — palette-led (REJECT)

A visually attractive set of desaturated tag colors gives each topic a distinct hue while titles, metadata, and saved state have nearly equal luminance. In a swatch sheet the palette looks coherent; in context it fails because topical color competes with the title and saved state disappears in grayscale.

### Variant B2 — structure-led (KEEP)

- title hierarchy comes from type role, spacing, and luminance;
- metadata is quieter but readable;
- saved state uses icon shape + accessible name/state, with hue optional;
- topical tags are tertiary and may lose chroma without losing document identity;
- grouping survives grayscale because whitespace and baseline rhythm do the work.

## Cross-context critique

### KEEP

1. Define semantic priority before choosing hue.
2. Require state redundancy: text, shape, geometry, or position must survive color removal.
3. Treat numerical contrast as a floor; inspect local competition and information priority separately.
4. Make low-light and glare tests role-specific rather than applying one global dimming filter.

### REWORK

The operational board needs actual device/display tests before its near-threshold secondary text can be accepted. The reading context needs enlarged-text testing because a quiet metadata role can become spatially dominant after wrapping.

### REJECT

- a universal four-gray palette;
- “premium = low contrast”;
- green/amber/red without redundant status semantics;
- declaring a palette successful from isolated swatches.

## Transferable conclusion

Color-system quality is demonstrated by preservation of semantic priority when chroma is unavailable or environmental conditions degrade it. Different products can therefore use radically different palettes while sharing the same validation method.

## Remaining evidence before PASS

- render at least one context and inspect it on real displays under controlled bright/low-light conditions;
- add a measured non-text component example rather than only text probes;
- verify the chosen focus/state geometry in an interactive artifact.
