# W102 — Served import mapping provenance and downstream invalidation

Status: **STAGE 3 PRACTICE / product runtime OPEN**

## RELATED DOMAIN CHECK
I089 defines mapping authority; L093 geometry; C102 visual state separation; CD108 semantic/localization contract; T071 downstream rendering corpus. Purpose: **TRANSFER VALIDATION** in the real served product, not another isolated Chromium micro-test.

## SOURCE
- WCAG 2.2 remains the W3C-recommended current WCAG 2 baseline. https://www.w3.org/WAI/standards-guidelines/wcag/
- W3C form guidance links labels/instructions and relationships to SC 1.3.1, 2.4.6, 3.3.2 and 4.1.2. https://www.w3.org/WAI/tutorials/forms/instructions/
- RFC 4180 documents CSV syntax and header ambiguity, not aviation field semantics. https://www.rfc-editor.org/rfc/rfc4180

## Closure ladder
Do not add an isolated browser specimen unless it resolves a product blocker. Required transfer order:
`LogMate implementation → production Web build → served primary engine → independent engine → 200% → forced colors → physical mobile/iPad where file-picker/runtime behavior matters`.

## Provenance manifest
For each scenario capture:
- build/commit/route/browser/version/viewport;
- fixture hash and file metadata;
- decoder/parser/source-system version;
- raw header + sample hash;
- mapping-rule ID/version;
- proposed target + confidence class + user resolution;
- normalized-record hash;
- validation/duplicate-rule versions and results;
- preview hash;
- transaction/inverse/projection hash if committed;
- semantic focus ID, visible/a11y status payload;
- L093 rectangles/obscuration/reflow;
- C102 rendered state identifiers.

## Critical invalidation assertion
If a source→target mapping or unit transform changes, all dependent downstream evidence must be regenerated or explicitly invalidated. A stale preview or duplicate classification after remapping is a hard FAIL even when the UI looks correct.

## Scenario families — REPLICATION ×2
1. documented exact mapping;
2. ambiguous mapping unresolved;
3. user resolves mapping;
4. remap after preview;
5. unit transform change;
6. exclude/restore field;
7. Back/Forward/reload before commit;
8. commit then batch Undo;
9. EN/KO, baseline/200%;
10. forced colors and independent engine.

## Performance evidence boundary
Lighthouse, DevTools and CI synthetic measurements remain **LAB**. LCP/INP/CLS become **FIELD** evidence only with provenance-bearing representative RUM/aggregate data. Mapping correctness must not be inferred from performance success.

## HANDOFFS TO OTHER SPECIALISTS
Return any browser/runtime contradiction to I089, geometry failure to L093, state collision to C102, semantic/localization failure to CD108 and rendering failure to Type with reproducible evidence.

## Evidence boundary
No real LogMate mapping runtime, cross-browser/device, screen-reader, field Core Web Vitals or human UX PASS is claimed.