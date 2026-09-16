# T023 — Product String Gate Contract

Evidence type: SYNTHESIS / TRANSFER VALIDATION / DEPENDENCY / OPEN

## RELATED DOMAIN CHECK
CD032/CD033 supply semantic literals and localization expansion; L019 supplies geometry stress; W026 will supply browser/font-loading evidence; C028 cannot repair glyph ambiguity; I014 owns action/state truth. T022 drawing remains before spacing/kerning.

## Purpose
T022's custom drawing track is intentionally blocked before spacing. Product work still needs a safe Type contribution, so T023 defines the independent mature-font transfer gate without consuming immature custom glyphs.

## String corpus classes
Operational identifiers and airport/flight-like uppercase strings; dates/times/durations; decimal and tabular-looking numeric data; pending/failure/unknown/conflict state titles; recovery actions; long localization-expanded labels; punctuation and ambiguous glyph sets including I/l/1, O/0, S/5 where relevant.

## Gate order
For custom drawing: T022 drawing PASS → spacing → kerning → repertoire. T023 does not bypass that order. It tests only mature shipped/product-font candidates for coverage, feature availability, fallback, numeric alignment, wrapping and target-size rendering.

## Evidence contract
Record exact font/version/source, actual supported OpenType features rather than assumptions, fallback chain, platform/runtime, string fixture, size/weight/line-height, wrap/overflow and ambiguous-glyph observation. Human recognition remains separate evidence.

## Current result
**PRODUCT-STRING TRANSFER CONTRACT PASS / PLATFORM EXECUTION OPEN.** This gives Web/Layout/Content a safe Type interface while T022 remains unfinished.

## HANDOFFS TO OTHER SPECIALISTS
CD033 supplies resource-generated strings; W026 records font/runtime evidence; L019 consumes measured wrapping rather than frozen widths. No specialist should treat T023 as approval of T022 custom glyphs.