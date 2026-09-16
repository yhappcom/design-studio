# T022 — Role-system transfer and gate review

Classification: **STAGE 2 PRACTICE / CROSS-DOMAIN TRANSFER / GATE REVIEW**

## Purpose
Advance T022 without violating the exact-binary requirement. The current connector can verify repository text and contracts but does not expose the bundled font binary for FontTools measurement in this run, so exact feature/advance results are not invented. The useful next work is to harden the product-role decision and transfer gates around the pending artifact experiment.

## RELATED DOMAIN CHECK
- Color C023 confirms character ambiguity is never repaired with hue.
- Layout L014 now explicitly treats numeric alignment as joint font-feature + column-geometry work and keeps airport/identifier widths natural.
- Interaction I009 requires recovery identifiers to remain stable through state changes.
- Web W021 uses mature/fallback typography but browser OpenType behavior is not Flutter proof.
- Content CD024 types flight/registration/airport/time values as operational data rather than freely localized prose.

## Role-system decision criteria
Alternative P (proportional everywhere) remains the minimum-complexity control. Alternative R (tabular behavior only for comparison-critical numeric/time/total roles) may beat P only if exact bundled LogMateRoboto plus Flutter/native transfer proves stable intended-role behavior without harming punctuation/locale formatting. Alternative M remains unjustified until a legitimate exact mono artifact and a bounded problem survive P/R.

### P should remain selected when
- default figure advances already support the actual column design;
- layout geometry can align numeric columns without fragile tracking/string padding;
- feature activation is unavailable or inconsistent in Flutter/native;
- role-specific feature complexity adds no measurable structural benefit.

### R may be selected when
- exact product binary exposes suitable figure behavior;
- equal-length numeric/time strings gain stable comparison geometry;
- punctuation (`: , -`) remains coherent;
- only intended numeric roles change;
- 200% text/locale/fallback stress remains acceptable in Layout transfer;
- Flutter/native activation is reproducible.

### M remains a later exception when
A persistent bounded recognition/alignment defect remains after P/R and an exact mono/identifier artifact can be evaluated. Global monospace is not a default LogMate identity strategy.

## Measurement handoff required from exact binary
Before recommendation, record at intended sizes:
- digit advances 0–9 default and requested feature mode;
- widths for `00:45 02:18 09:55 12:40`;
- widths for `1,284:35 9,999:59`;
- punctuation advances for colon/comma/hyphen;
- airport/identifier width variance as a natural-layout stress, not a failure by itself;
- relevant GSUB/GPOS feature inventory;
- whether the feature changes only intended glyphs/roles.

## Mixed-script gate
`LogMateRoboto` 400/500 plus `LogMateNotoSansKR` 400 creates a separate mixed-script weight/metric seam. Do not infer Korean role parity from Latin measurements. Mixed Korean/Latin labels and remarks require rendered/native transfer; the fallback seam may be more consequential than Latin numeric feature choice.

## Kerning boundary
T021's rejected bespoke family never reaches kerning. T022 may inspect kerning only after a mature role configuration is selected and only for residual pair-specific problems in roles that actually use it. Numeric column alignment must not be 'fixed' through kerning.

## Current gate
**T022 remains OPEN at exact product artifact inspection.** Cross-domain ownership and decision criteria are now stronger, but exact LogMateRoboto feature/advance measurement and Flutter/native activation are still required before P/R selection.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: do not freeze numeric cell widths before exact P/R metrics and 200% stress.
- Content: keep operational values typed/literal; locale formatting of counts/date/time is a separate semantic decision.
- Web: browser feature behavior may be comparative evidence only, not native proof.
- Color: no hue-based ambiguity mechanism.

## Evidence boundary
No exact font-binary metric, OpenType-feature, Flutter activation, human recognition or physical-device PASS is claimed in this review.