# L033 — Export-to-Live Recheck Spatial Continuity

Evidence purpose: **SYSTEMS PRACTICE / TRANSFER VALIDATION PREPARATION** paired with I029.

## RELATED DOMAIN CHECK
I029 owns recheck behavior; C042 owns cue-loss survival; W041 owns export/browser evidence; CD047 owns snapshot wording; Type metrics remain provisional.

## Spatial requirement
The static artifact and the live recheck surface must preserve a recognizable information spine without pretending they are the same temporal state:
`object identity → snapshot provenance → snapshot consequence → recheck path` in the artifact, then `object identity → current authority result → changed-since-snapshot consequence → safe actions → history` in live UI.

## Geometry oracle
At narrow width, 200% zoom, long localized strings and long IDs:
- object identity must remain adjacent to the snapshot/current state it qualifies;
- snapshot timestamp and authority timestamp cannot wrap into another event row;
- recheck affordance remains associated with the artifact/object, not a neighboring history item;
- changed-since-snapshot disclosure precedes consequential live actions in reading/visual order;
- page breaks may not orphan event certainty, timestamp or consequence from event identity;
- current truth remains visually dominant over historical success without requiring color alone.

## Static-to-live discontinuity risks
PDF page number is not live route identity; sticky headers disappear in print; table columns may collapse; long identifiers may wrap; locale may change between export and recheck. These are explicit transfer stresses rather than cosmetic defects.

## Evidence join
Use shared `artifactId`, `objectId`, `eventId`, `runId`, viewport/zoom, locale, page number and bounding boxes. A screenshot without identity/provenance is insufficient.

## OPEN
No browser/PDF geometry has been executed in this run. Human scanning, workload and physical-print evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W041/W042 should capture page and live-surface geometry under the same IDs. CD048 should preserve semantic ordering. C042 should test whether visual priority survives cue loss.