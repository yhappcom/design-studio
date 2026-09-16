# T022 — Mature Product Typography Role System Entry

Classification: **STAGE 2 PRACTICE / PRODUCT TYPOGRAPHY SYSTEM / ENTRY CONTRACT**

## Why T022 changed
T021 closed the current full bespoke-family route after semantic architecture and build success did not survive the drawing/product-route gate. T022 therefore must not become post-hoc polishing of rejected glyphs.

The Stage-2 learning target now moves to a more realistic product problem: how a mature proportional family should be assigned and configured across distinct operational roles without collapsing the whole interface into monospace or assuming that every alignment problem belongs inside a font.

## SOURCE — live LogMate baseline
Current live main bundles proportional `LogMateRoboto` Regular 400 and Medium 500 plus `LogMateNotoSansKR` 400. ThemeData and TextTheme use `LogMateRoboto`. No current Roboto Mono product asset was found.

This makes the exact bundled Roboto family the canonical product control for T022.

## Core question
**Which typography behaviors belong to which LogMate information roles, and which problems should be solved by font features versus formatting versus layout geometry?**

## Role inventory to validate
1. Airport codes: `ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`
2. Flight identifiers: `KE704 BA117 AF264`
3. Aircraft types: `B737-900 B737-8 A320-200`
4. Registrations: `HL8301 N12345 G-EUOH`
5. Clock values: `00:45 02:18 09:55 12:40`
6. Duration/cumulative values: `1,284:35 9,999:59`
7. Comparison-critical numeric columns: repeated hours, totals, page totals and cumulative totals
8. Labels/header/prose: Date, Type, Reg, Flight, DEP, ARR, Block, Night, Inst, Remark and localized equivalents
9. Ambiguity controls: `0/O`, `1/I/l`, `5/S`, `8/B`
10. Mixed-script labels/remarks where Korean fallback participates.

## Alternative systems — required Stage-2 comparison
### Alternative P — proportional everywhere
Use the current proportional Roboto behavior for all roles. Alignment is owned entirely by column geometry/formatting.

Purpose: minimum-complexity control.

### Alternative R — role-specific numeric features
Keep proportional Roboto for prose and identifiers; request tabular figures only for comparison-critical numeric/time/total roles if the exact product font + Flutter path support the behavior reproducibly.

Purpose: separate reading rhythm from numeric column alignment.

### Alternative M — bounded mono/identifier treatment
Keep proportional product typography globally but allow a narrowly scoped mono/identifier treatment only if exact product evidence later demonstrates a recognition/alignment problem that P/R cannot solve.

Purpose: stress alternative, not default recommendation. No current product mono artifact exists, so this alternative is not yet executable as an exact product control.

## Measurement contract
For P and R, test exact bundled Roboto artifact where binary-level evidence is required. Record:
- per-string advance at intended ledger sizes;
- digit advance equality under default behavior and any requested tabular behavior;
- punctuation advance/placement for `: , -`;
- equal-length time string widths;
- cumulative-value alignment consequences;
- airport/identifier width variance;
- whether feature activation changes only intended roles;
- fallback/mixed-script seam separately from Latin metrics.

Do not use a generic font as a substitute for exact product binary evidence.

## Ownership matrix
| problem | first owner | Type contribution |
| --- | --- | --- |
| numeric columns fail to line up | Layout + Type | test tabular figures and stable formatting |
| airport strings vary in width | Layout | do not fake equality with tracking; Type measures consequences |
| 0/O confusion | Type + Content/task context | test available glyph/feature mechanisms; human validation later |
| cumulative total overflow | Layout + formatting | Type supplies exact advances/stress values |
| Korean/Latin visual mismatch | Type | fallback/weight/metric seam analysis |
| column collapse at larger text | Layout | Type provides metric stress evidence; do not solve by artificially narrow custom font |
| pair-specific ugly spacing | Type | inspect only after role/feature selection; kerning analysis if genuinely residual |

## Gate sequence
`exact product artifact → role corpus → default metrics → feature availability → exact feature behavior → layout consequence → role alternatives → selected system rationale → native transfer → human validation when available`

## PASS criteria for T022
T022 is not PASS merely because `tnum` exists in a font table.

Required before closure:
1. exact current product Roboto binary inspected for relevant OpenType feature support;
2. exact operational role corpus measured under default behavior;
3. P and R alternatives executed; M only if an exact bounded mono artifact becomes legitimate;
4. figure/punctuation consequences documented at target sizes;
5. feature support distinguished from Flutter/native activation behavior;
6. product role recommendation defended by explicit criteria, not aesthetics alone;
7. residual kerning/class needs enumerated only after the mature-font role system stabilizes;
8. mixed-script/fallback implications recorded;
9. human/device claims left OPEN unless actually executed.

## First experiment
Inspect the exact bundled `Roboto-Regular.ttf` for GSUB/GPOS feature inventory and figure metrics. Determine whether tabular figures are default, feature-selected, absent, or otherwise encoded. Then build an artifact-level P/R comparison before touching LogMate source code.

## RELATED DOMAIN CHECK
- Layout/Interaction owns cell allocation, overflow and text-scale response jointly with Type metrics.
- Web must not infer Flutter/native feature activation from browser CSS support.
- Content preserves literal operational values and formatting semantics.
- Color is outside glyph ambiguity repair.

## HANDOFFS TO OTHER SPECIALISTS
No layout token change is requested yet. T022 will hand off measured product-font advances and role-specific feature requirements only after exact artifact inspection. Current product typography remains unchanged during research.