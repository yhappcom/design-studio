# Candidate 04 — Color Review R1 — 2026-09-20

Status: **CHANGES REQUIRED BEFORE OWNER REVIEW**

Evidence reviewed:
- Candidate 04 dark/light deterministic renders
- implementation commit `3f7618b0f533d88f4291ca01c8cb854787ef3c0c`
- current Color constraints

No prior Home candidate was consulted.

## Findings

### Works
- Graphite concept is materially expressed through luminance structure, not decorative effects.
- Large colored surfaces are absent.
- Brand accent is limited to wordmark/focus/selection.
- Dark mode hierarchy is coherent and quiet.

### Blockers
1. The current brand green `#00A693` against the light canvas `#F3F1EC` is approximately 2.7:1. It is used as wordmark text and therefore is too weak for small text treatment.
2. The current tertiary colors are also too weak for small Search placeholder text in both appearances:
   - dark tertiary `#74766F` on `#11120F` ≈ 4.08:1;
   - light tertiary `#8A8C84` on `#F3F1EC` ≈ 3.02:1.

## Required correction
- Use appearance-calibrated accent values while preserving the mint identity:
  - light accent around `#007C70` or darker;
  - dark accent may retain the brighter mint family.
- Raise tertiary text contrast:
  - dark tertiary at least around `#80827B`;
  - light tertiary around `#6B6E67` or darker.
- Re-render both appearances after correction.

Verdict: **NOT OWNER-REVIEW ELIGIBLE UNTIL COLOR CORRECTION.**