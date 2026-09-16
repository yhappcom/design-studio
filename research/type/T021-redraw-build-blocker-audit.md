# T021 — Redraw Build Blocker Audit

Status: **EXECUTED ATTEMPT / DETERMINISTIC SOURCE DEFECT FOUND / REDRAW RASTER NOT CLAIMED**  
Date: 2026-09-16  
Owner: Typography / Type Design Specialist

## Purpose

Continue the large T021 redraw block after the first operational raster proved that cmap coverage did not establish coherent glyph construction.

## Executed finding

A second-pass redraw/build attempt was made in the available FontTools/Pillow execution environment. Before raster validation, the build exposed a deterministic repertoire/metrics defect: the canonical operational harness declares `UPPER='ABCDEFGHIJKLMNOPRSTUVX'`, which includes `M`, while its `widths` dictionary has no `M` entry and the build loop indexes it with `widths[c]` rather than a fallback. The executable result is therefore a `KeyError: 'M'` before the expanded font can be built.

This means the previous source-level claim that the harness itself reproducibly encodes the complete bounded uppercase target was too strong. The earlier locally executed equivalent did produce a bounded TTF, but the exact canonical source now requires repair before it can be treated as reproducible proof.

## Additional source-level construction defect

Even after adding an M width, the current `boxglyph` has no explicit `M` branch. Its default branch draws a filled rectangular cap box. Therefore merely adding a width would remove the exception but would still fail the drawing-validity gate. M needs an actual construction, not an exception suppression.

The same rule applies to any repertoire member that reaches a generic fallback drawing: build success is not design completion.

## Methodological correction

The T021 chain is tightened again:

`declared repertoire → complete metric map → explicit glyph construction → executable build → cmap coverage → raster drawing validity → general spacing → pair residual → kerning`

A repertoire declaration must be cross-checked against both metrics and construction dispatch before an executable-family claim is made.

## KEEP / REWORK / REJECT

- **KEEP:** bounded operational corpus, kerning-off discipline, 14/17/24px proof matrix, failure classification.
- **REWORK:** canonical harness repertoire/width/construction consistency; M requires explicit drawing; previously identified C/G/B/D/R/S/n/figure structural redraw remains required.
- **REJECT:** treating a declared uppercase string or cmap target as evidence that every glyph has a valid construction path.

## Next large block

Repair the canonical generator so every bounded repertoire member has (1) a metric entry and (2) an explicit non-placeholder construction. Then execute the exact generator, not an informal equivalent; rerender 14/17/24px; inspect the full operational corpus; revise base spacing only after drawing validity; enumerate pair-specific residuals only after spacing stabilizes. T022 remains blocked.

## Evidence boundary

No second-pass raster PASS is claimed. The attempted redraw did not complete the build. Human/native/browser evidence remains deferred.
