# W041 — Audit Export / Print Runtime Transfer Contract

Evidence purpose: **STAGE 3 RUNTIME TRANSFER CONTRACT**.

## RELATED DOMAIN CHECK
I028 defines export provenance truth; L032 defines static hierarchy; C041 defines visual truth after color/theme loss; CD046 defines event semantics; Type custom candidate remains blocked from product transfer.

## Runtime target
Extend W040's durable audit reconstruction through `history/deep-link → export/print → static artifact → return/recheck current truth`.

## Required execution scenarios
- browser print preview / print stylesheet;
- PDF generation path when product-supported;
- download/export path when product-supported;
- light and dark source states;
- localized expansion and long identifiers;
- page-break stress;
- independent browser engine before cross-browser claims.

## Provenance capture
Record commit SHA, browser/engine/version, route, object/event IDs, authoritative and presented revision, locale/resource revision, export generation timestamp semantics, media mode, viewport/zoom, computed styles relevant to C041, page/box geometry relevant to L032, and artifact hash where available.

## Runtime assertions
1. export reconstructs from durable truth, not selected component memory;
2. current consequence and historical events remain distinct;
3. print CSS does not remove non-color state labels;
4. hidden/collapsed content is either intentionally omitted and disclosed or included according to product contract;
5. page breaks do not detach event identity from certainty/consequence;
6. static artifact declares snapshot limitations and recheck path where appropriate.

## Performance boundary
Export generation timings are lab/functional diagnostics. They are not field LCP/INP/CLS. Field Core Web Vitals require real field/RUM population evidence.

## Evidence boundary
No executed W041 artifact exists yet. No cross-browser, Safari, PDF fidelity, printer, AT, physical-device or human UX PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
C041 consumes computed/exported visual evidence; I028 consumes provenance; L032 consumes page geometry; CD047 consumes actual export strings and fallback behavior.