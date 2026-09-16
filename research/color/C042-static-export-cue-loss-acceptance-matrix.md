# C042 — Static Export Cue-Loss Acceptance Matrix

Evidence purpose: **TRANSFER VALIDATION PREPARATION** from C041 into executable W041 artifacts.

## RELATED DOMAIN CHECK
Type T021 remains provisional; I028/L032 define provenance/static hierarchy; W041 owns print/export runtime; CD047 owns snapshot semantics.

## Problem
Interactive UI can rely on focus, hover, selection, theme surfaces and transient state. PDF/print removes some or all of those channels. C041 established the truth requirement; C042 makes the loss conditions testable.

## Acceptance matrix
For each W041 artifact capture the same event under: screen color, print-color emulation, grayscale, backgrounds disabled where supported, forced-colors screen precursor, and selected-row styling removed. Judge independently:

- current authoritative consequence remains distinguishable from historical success;
- snapshot provenance remains visible without hue;
- intervention-required does not become visually weaker than stale success;
- selection/focus styling is not misread as event certainty;
- boundaries and text labels survive background loss;
- text/non-text contrast and semantic distinguishability are separate verdicts.

WCAG 2.2 remains the accessibility baseline for applicable screen-rendered criteria. A print/PDF artifact is not declared WCAG-conformant merely because its source page passes screen checks.

## Failure injection
Deliberately remove authored hue, status icon, background fill and selection indicator one at a time, then in pairs. If two purportedly redundant cues disappear through the same export transformation, they are not independent redundancy for that artifact.

## Evidence record
Use shared `runId`, `eventId`, `artifactId`, browser/engine/version, media mode, locale/resource revision, computed foreground/background/border values when available, and artifact hash. Record `PASS/FAIL/NOT-EXECUTED` per condition; do not collapse them into one accessibility verdict.

## OPEN
No W041 artifact is executed in this run. Physical print, calibrated display, CVD/low-vision observer and human salience evidence remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
W041 must emit the artifact/media identity required here. L032 should provide page-region geometry. CD047 must preserve non-color state labels. I028 provides immutable event provenance.