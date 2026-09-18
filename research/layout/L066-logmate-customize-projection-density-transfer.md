# L066 — LogMate Customize Projection & Density Transfer

Date: 2026-09-18
Mode: **TRANSFER VALIDATION + CONTRADICTION REVIEW**
Stage: 3 PRACTICE / NOT PASSED

## Question
Can a professional logbook let pilots change visible ledger fields without confusing presentation configuration with record truth, while keeping the ledger usable across narrow landscape widths and dense optional-field combinations?

## SOURCE
LogMate `docs/specs/logbook-configuration-spec.md` on `main` defines a zero-configuration Standard projection, 35 top-level selectable items, grouped Route/Takeoff-Landing/Approach/Simulator-FSTD presentation units, immediate presentation-only changes, stable hidden order, at least one visible item, and the invariant that hiding a column does not delete record data or provenance. The current implementation is explicitly a temporary mock/session shell; persistence, Sync and real FlightRecord projection remain NOT IMPLEMENTED.

Current widget tests provide executable spatial evidence that header/body/totals share horizontal offsets, totals remain aligned after semantic reorder, total-only projections remain geometrically safe, and horizontal overflow appears/disappears when visible columns change. This is stronger than a static mock but not production-data or device evidence.

WCAG 2.2 remains the accessibility baseline. Reflow permits exceptions where two-dimensional layout is required for usage or meaning; a professional ledger can legitimately retain horizontal scrolling, but surrounding controls and explanatory content should not inherit that exception automatically.

## PRACTICE — projection-pressure matrix
Treat configuration as a projection over stable semantic identity, not a free-form table builder. Test at least these families:

1. **Standard** — Date/Type/Reg/Flight/Route/Block/Night/Inst/Remark.
2. **Minimum** — one visible top-level item; no orphan totals or unusable chrome.
3. **Totals-heavy** — Block/Night/Instrument plus other total-eligible duration fields when implemented.
4. **Operational-wide** — Ramp Out, T/O Time, L/D Time, Ramp In, Route, PF/PM, Duty Code.
5. **Qualification-wide** — PIC/SIC/PICUS/SPIC/Multi-Pilot/Cross-Country/Solo/Dual/Instructor/Examiner.
6. **Group-heavy** — all renderer-controlled field groups enabled.
7. **Long-content** — 7-character Flight, long registration, long Remark, cumulative 99,999+59 total capacity.

For each family record: leaf count, intrinsic ledger width, horizontal-scroll need, header/body/total x-alignment, frozen/sticky regions if any, vertical indicator safety, focus order, and whether a field-group move preserves child adjacency.

## CRITIQUE
A width-adaptive ledger must not solve density by silently dropping semantic leaves, collapsing Type+Registration, replacing DEP/ARR with an ambiguous stored `Route`, or abbreviating distinct time semantics into one generic Flight Time. Those would be semantic failures, not responsive solutions.

The current horizontal ledger is plausibly an essential two-dimensional structure, but that judgment must remain scoped to the ledger. Customize controls themselves should reflow and remain operable without requiring simultaneous two-axis navigation.

## REPRODUCIBLE VALIDATION CONTRACT
A future product-transfer run passes this study only when the same configuration identity is exercised through:

- Standard → wide → minimum → Reset → Standard;
- reorder of a total-bearing item with header/body/total alignment preserved;
- group reorder/toggle with children preserved as one semantic unit;
- width changes at phone/tablet landscape sizes;
- 200% text / enlarged text for surrounding controls;
- keyboard/pointer/touch-equivalent reorder path;
- real FlightRecord projection after that layer exists.

Record `EXECUTED-PASS`, `EXECUTED-FAIL`, `BLOCKED`, or `NOT-EXECUTED` per scenario. Do not inherit the job-level result.

## RELATED DOMAIN CHECK
- **Type:** compact headers and cumulative durations create real metric pressure; do not solve it with unfinished custom-font spacing/kerning.
- **Color:** SHOWN/HIDDEN, selection, drag lift, insertion and focus states require visible + non-color identity.
- **Interaction:** immediate mutation, reorder, Reset and hidden≠deleted semantics are behavioral contracts.
- **Web:** browser/runtime must verify horizontal ledger behavior and non-drag reorder alternatives.
- **Content:** labels must preserve semantic distinctions between Route group vs DEP/ARR leaves, Block vs Actual, Inst vs IFR vs Actual Inst.

## HANDOFFS TO OTHER SPECIALISTS
Interaction should own reorder equivalence and immediate-change/recovery behavior. Content should own terminology and hidden≠deleted explanation. Web should validate WCAG 2.2 dragging/target/reflow behavior in the PWA. Type should stress compact headers without compensating for layout pressure. Color should validate state visibility under themes/forced colors.

## OPEN
- Real FlightRecord projection and persistence.
- Configuration Sync and cross-device conflict behavior.
- Exact breakpoint/composition policy.
- Keyboard/single-pointer non-drag reorder implementation.
- AT, physical-device and representative-pilot evidence.

## Conclusion
The next Layout advance is not another generic grid exercise. It is a projection-density transfer: preserve professional semantic identity while proving that configuration extremes remain spatially coherent. Current mock/widget evidence is useful but insufficient for Stage 3 PASS.