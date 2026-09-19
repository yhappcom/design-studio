# I093 — LogMate Large-Text Ledger Interaction Contract

Status: **STAGE 3 PRACTICE / TRANSFER VALIDATION — no gate promotion**

## PURPOSE
Define how ledger interaction survives enlarged text and adaptive representation without changing semantic identity, action availability or recovery truth.

## RELATED DOMAIN CHECK
Type T075, Color C106, Layout L096, Web W105 and Content CD111 checked. WCAG 2.2 Reflow, Target Size (Minimum), Focus Not Obscured and Text Spacing are treated as independent constraints, not a single accessibility score.

## INTERACTION INVARIANTS
Representation may change; these may not silently change:
- record semantic ID;
- selected record ID;
- focused control/object identity;
- edit/delete/open-detail action meaning;
- validation state;
- transaction/inverse availability and expiry;
- status/recovery message truth;
- sort/filter state.

Horizontal table scrolling, row expansion, stacked detail, disclosure, or a dedicated record detail view are representation choices, not new records or new actions.

## PRACTICE SCENARIOS
Execute the same stable IDs through:
1. baseline ledger → enlarge text → open record → return;
2. baseline selected row → enlarge → verify selection identity;
3. focused row action → enlarge/reflow → verify focus remains meaningful and visible;
4. invalid/editing row → enlarge → correction → commit;
5. delete/Undo available → enlarge → Undo → verify inverse/projection;
6. sort/filter → enlarge → open detail → return;
7. horizontal-scroll representation → sticky header/column → keyboard traversal;
8. pointer target audit after reflow; WCAG 2.2 SC 2.5.8 minimum target/spacing remains applicable.

## CRITIQUE
A common false adaptation is to replace a dense row with a visually simpler card that drops sort/comparison context, changes action placement unpredictably, or makes the entire row a competing target. Another is to retain the table but let sticky headers/columns cover focused controls. Both preserve pixels better than workflow and are rejected.

## SYNTHESIS
Large-text adaptation is successful only when **semantic continuity** survives representation change. The user may see fewer columns at once or enter a detail representation, but record identity, state, action consequence and recovery must remain stable and discoverable.

## HUMAN-EVIDENCE BOUNDARY
No claim is made that pilots prefer horizontal scrolling, row expansion or detail transfer, nor that one has lower cognitive load. Those require representative-human evidence.

## OPEN
- Actual LogMate ledger implementation.
- Focus restoration and sticky-region runtime evidence.
- Physical touch/iPad target evidence.
- Screen-reader and representative-pilot evidence.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: choose adaptation by semantic continuity, not card/table fashion.
- Web: capture semantic IDs, focus, selection, transaction and geometry before/after adaptation.
- Content: labels/actions must preserve meaning when moved into disclosure/detail.
