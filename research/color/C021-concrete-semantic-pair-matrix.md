# C021 — Concrete semantic pair matrix for multi-surface states

Classification: **PRACTICE + TRANSFER PREPARATION**

## Purpose
Move C020 from semantic architecture toward executable theme transfer without pretending that static hex authoring proves physical-display, CVD, forced-colors or human salience behavior.

## RELATED DOMAIN CHECK
- Type T021 remains drawing-invalid; color must not repair glyph ambiguity.
- L012/I007 supplies the consequential state inventory and requires non-color carriers.
- W020 requires theme/forced-color browser transfer.
- CD020 supplies stable state/message semantics independent of hue.

## Semantic pair contract
The system is authored as foreground/background **pairs**, not isolated swatches. Baseline roles:

| Role | Light fg | Light bg | Dark fg | Dark bg | Required non-color carrier |
|---|---|---|---|---|---|
| primary text | `#17212B` | `#FFFFFF` | `#F2F5F7` | `#101418` | text itself |
| secondary text | `#465462` | `#FFFFFF` | `#C4CDD5` | `#101418` | text itself |
| action | `#075E54` | `#FFFFFF` | `#9DE9DF` | `#101418` | label + control geometry |
| confirmed | `#165C36` | `#EAF7EF` | `#A8E6BF` | `#173023` | icon/text state label |
| known failure | `#8B1E1E` | `#FFF0F0` | `#FFB4AB` | `#3A1717` | icon + explicit failure/recovery text |
| outcome unknown | `#704C00` | `#FFF6D8` | `#FFD966` | `#332700` | uncertainty label + safe-action text |
| offline/stale | `#44515E` | `#EEF2F5` | `#D0D7DE` | `#252B31` | status text/icon + timestamp/context |
| focus indicator | `#005FCC` | adjacent surface | `#8CC8FF` | adjacent surface | visible outline/shape change |

These are **candidate sRGB authored values**, not production tokens.

## Pair-matrix rules
1. Text/state foreground must be evaluated against the exact surface it is rendered on; inherited assumptions are invalid.
2. Consequential states never depend on hue alone.
3. Status colors and data-series colors remain separate namespaces even when numeric values happen to match.
4. Dark theme is separately authored; it is not an inversion transform.
5. Focus is an interaction carrier, not a brand accent.
6. Disabled state must not be represented solely by insufficient contrast; semantic availability is owned by Interaction.
7. Wide-gamut candidates are deferred until an sRGB baseline survives browser transfer; P3 novelty is not itself product value.

## Adverse-state collision stress
The highest-risk collision is `outcome unknown` vs ordinary warning. I007 establishes that outcome-unknown has a stronger behavioral consequence: blind retry is blocked. Therefore visual similarity cannot collapse the states. Content must name uncertainty and the available safe action; Layout keeps that message adjacent to the affected object; Web exposes status semantics. Color is reinforcement only.

Known failure vs destructive action is also kept distinct at the semantic-token layer even if both use red-family values. Failure describes system state; destructive action describes action consequence.

## Forced-colors transfer contract
In forced-colors, authored semantic hues may disappear. Therefore the acceptance condition is not hue preservation. It is preservation of:
- visible text/state identity;
- visible focus indication;
- control boundaries where needed;
- state icons/labels or other non-color carriers;
- reading and action order.

Actual browser forced-colors behavior remains a Web transfer gate.

## Gate result
**STATIC PAIR-SYSTEM PRACTICE PASS; STAGE 3 NOT PASSED.**

C021 provides concrete values and collision rules sufficient for W021 transfer, but it does not establish normative contrast results, browser parity, physical-display behavior, CVD observer performance or human salience. Exact pair calculations should be executed in the next Color validation block rather than asserted from visual inspection.

## HANDOFFS TO OTHER SPECIALISTS
- Web: use these candidate aliases as W021 inputs, but return actual computed contrast/theme/forced-colors behavior.
- Layout/Interaction: preserve outcome-unknown as behaviorally distinct from warning/failure.
- Content: verbal identity remains mandatory when hue is unavailable.
- Type: no dependency on candidate hue for operational-string recognition.