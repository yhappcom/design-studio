# L034 — Temporal Provenance and Chronology Layout Contract

Status: **STAGE 3 PRACTICE / SYSTEMS EXTENSION**

## RELATED DOMAIN CHECK
I030 owns temporal behavior and ordering semantics. C043 owns visual cue precedence. W042/W043 own browser/export/recheck runtime evidence. CD048/CD049 own timestamp language and localization. T021 metrics remain provisional.

Purpose: **TRANSFER VALIDATION** of L031–L033 from snapshot/current hierarchy into multi-clock chronology.

## Spatial problem
Audit screens can contain several legitimate times for one event. Spatial proximity must not imply that snapshot generation, authority confirmation and event occurrence are the same fact.

## Information spine
For a selected object:

`object identity → current authoritative consequence → freshness/certainty → safe current action → snapshot provenance → chronology basis → event history → per-event provenance`

Within an event row/card:

`event identity → event/state label → primary chronological time → secondary provenance times → certainty/source → detail`

The primary chronological time is chosen by Interaction/product truth, not by whichever string is shortest.

## Reflow requirements
At narrow width, 200% zoom, long locale strings, long identifiers and explicit zone names:

- timestamp role label stays attached to its value;
- current consequence remains above historical chronology;
- event rows may grow vertically rather than truncate role/source meaning;
- page breaks must not orphan a timestamp from its event identity or certainty;
- a selected historical event must remain visually distinct from current authoritative state;
- recheck action remains adjacent to the freshness statement it resolves.

## Static export
Print/PDF may repeat object identity, snapshot provenance and chronology basis in page headers/continued sections when a page break would otherwise make history ambiguous. Repetition is acceptable when it prevents false association; it must not imply a new event.

## Deterministic failures
FAIL if a zone/source label wraps into the next event; if current state falls below a long history list; if two timestamps align as an unlabeled table pair whose roles become ambiguous; if responsive order changes chronology semantics; or if page break separates an event from its certainty/provenance.

## Evidence boundary
No W043 geometry capture exists yet. This is not human scanning, discoverability or workload evidence.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture bounding boxes and reading order for timestamp role/value pairs. Content should provide role labels that can expand without abbreviation-only dependence. Color should preserve hierarchy after hue/background loss. Type should not be production-bound until T021 repair and spacing gates close.
