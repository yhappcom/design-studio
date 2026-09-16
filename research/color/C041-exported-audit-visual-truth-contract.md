# C041 — Exported Audit Visual Truth Contract

Evidence purpose: **STAGE 3 SYSTEMS PRACTICE + TRANSFER VALIDATION**.

## RELATED DOMAIN CHECK
Type T021 remains provisional; exported evidence must use mature fallback. I027/L031 define durable event truth/current-history separation. W040 defines browser reconstruction provenance. CD046 defines durable audit semantics.

## Problem
A durable audit trail can be correct in-app yet become misleading when printed, exported to PDF/image, copied, or viewed without theme/state CSS. Export is therefore a semantic transfer, not a screenshot convenience.

## Contract
Exported audit material must preserve, without hue alone:
1. current authoritative consequence versus historical event;
2. confirmed / unknown / conflict / intervention-required distinctions;
3. selected/focused UI state must not be serialized as event meaning;
4. chronology and event identity;
5. warning/status boundaries in grayscale and user-color-loss conditions.

## Adversarial matrix
Evaluate light, dark-to-print, grayscale, background removal, icon loss, and high-contrast/forced-color-derived exports where supported. Contrast, semantic distinguishability, focus visibility and focus obscuration remain separate verdicts. Focus styling should normally disappear from a static export unless focus itself is the subject of evidence.

## Failure conditions
- green historical success dominates a current intervention-required consequence;
- row selection survives export and appears to mean confirmed;
- status becomes indistinguishable after grayscale/background removal;
- brand emphasis outranks safety/authority state;
- exported color legend is the only explanation of event meaning.

## Evidence boundary
This is a transfer contract, not executed browser/print/PDF evidence. Physical print, calibrated display, low-vision/CVD observer and human salience evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W041 should capture computed/exported appearance; L032 should preserve current/history hierarchy; CD047 must provide non-color labels; Type remains on mature fallback until T021 gates pass.