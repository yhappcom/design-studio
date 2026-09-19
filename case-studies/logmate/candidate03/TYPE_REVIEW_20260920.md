# Candidate 03 — Typography / Type Review — 2026-09-20

Status: **CHANGES REQUIRED BEFORE OWNER REVIEW**

Evidence reviewed:
- LogMate restore-point-derived Flutter implementation branch `design/home-candidate-03-code-20260920`
- implementation commit `bf2f45a4f676f2473e0ab5536ca6ab7e2d0f1046`
- 390×844 code-mirror render produced from the same geometry/tokens
- current T084 / Type status constraints

This review does not consult prior Home candidates.

## Findings

### Works

- Repeated Recent Flight data uses an operational mono role and keeps stable Date / Flight / Route / Block axes.
- Flight carrier and number remain separately zoned.
- Product-authored labels remain proportional.
- The visual hierarchy is restrained; no decorative type family is being used to manufacture premium character.
- The Recent rows are the clearest type-role expression in the concept.

### Problems

1. **Mono has spread beyond the strongest confirmed operational roles.**
   Current Period, Activity and Totals summary values are all rendered in mono. Those values need stable numeric comparison, but the current synthesis permits proportional tabular figures outside confirmed mono roles. Using mono across nearly every numeric value weakens the intended dual voice and makes the whole Home feel more code-like than necessary.

2. **Current-period value scale is very dominant.**
   `42+15` at the current masthead size is legible, but it becomes the strongest typographic object on Home. That may be acceptable only if Current Period is intended to outrank Recent Flights. The product contract does not require that hierarchy.

3. **Exact production mono remains OPEN.**
   The review render uses a mature system mono substitute. No production-family conclusion is permitted.

4. **Scaled-text behavior is not yet evidenced.**
   The lower two-column field and the large Current Period value need enlarged-text and fallback stress.

## Required correction

- Keep operational mono for repeated Flight/Date/Route/Block rows.
- Move Current Period / Activity / Totals summary numerics to proportional tabular figures.
- Reduce the masthead value dominance slightly unless Layout review establishes a product reason for it.
- Re-render at baseline before promotion.

Verdict: **NOT OWNER-REVIEW ELIGIBLE YET.**
