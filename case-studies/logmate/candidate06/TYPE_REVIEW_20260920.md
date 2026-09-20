# Candidate 06 — Typography / Type Review — 2026-09-20

Status: **PASS FOR OWNER AESTHETIC REVIEW / PRODUCTION TYPE OPEN**

Evidence reviewed:
- branch `design/home-candidate-06-visual-only-20260920`
- corrected Flutter source commit `218a1a44d591d65daee5e4ef5fcc7be6738b41bd`
- final deterministic 390×844 light/dark renders
- current Type constraints

No prior Home candidate was consulted.

## Findings

- Product-authored UI remains proportional.
- Operational mono is limited to repeated Date / Flight / Route / Block data.
- Flight keeps carrier + number zoning.
- Current Period / Activity / Totals values use proportional tabular figures.
- The concept avoids decorative display typography; hierarchy comes from weight, scale and spacing.
- Restoring separate `Block Time`, `This month`, and `This year` labels preserves semantic clarity and avoids copy-driven visual novelty.
- Section labels remain sentence case and are visually distinct from operational rows without turning into a second brand font.

## Risks / OPEN

- exact production proportional family;
- exact production mono/fallback;
- nonlinear scaling;
- text-spacing/fallback metrics;
- representative-human perception of the intentionally quiet hierarchy.

No static type blocker remains.

Verdict: **PASS FOR OWNER AESTHETIC REVIEW.**