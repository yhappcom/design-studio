# C023 — Contextual focus and non-text transfer contract

Classification: **STAGE 3 PRACTICE / TRANSFER VALIDATION DESIGN**

## Purpose
Advance beyond C022 authored text/state ratios into the unresolved contextual color problems that require rendered geometry: focus indicators, control boundaries and forced-colors survival.

## RELATED DOMAIN CHECK
- Type T022 keeps ambiguity structural/typographic, never color-coded.
- L014 defines actual focus/adjacent-surface geometry under recomposition and sticky UI.
- I009 defines which controls are available in each certainty state.
- W021 is the browser transfer surface.
- CD024 keeps state meaning verbal/semantic when authored hue disappears.

## Contextual pair model
A focus token cannot be certified against an abstract 'adjacent surface'. Runtime validation must enumerate the actual surfaces it touches: page background, card/panel, state banner, action/control surface and sticky/transient region.

For each rendered focus/control instance record:
1. authored foreground/border/focus value;
2. exact adjacent rendered background(s);
3. component/focus geometry and thickness/area assumptions;
4. computed contrast where WCAG 2.2 non-text contrast applies;
5. whether a non-color shape/boundary remains perceivable;
6. forced-colors computed mapping and system-color behavior;
7. whether focus remains visible when sticky/transient UI overlaps nearby content.

## Failure conditions
- focus passes on page background but disappears against a state banner/card it actually intersects;
- component boundary relies on a low-contrast fill with no other boundary where a boundary is required to identify the control;
- forced-colors removes both authored hue and the non-color/state carrier;
- disabled styling communicates availability only by reducing contrast;
- known failure/outcome unknown become indistinguishable when color is transformed and their required verbal/icon carriers are absent.

## WCAG boundary
Use WCAG 2.2 as the normative studio baseline. Exact applicability and exceptions for non-text contrast/focus criteria are assessed against the rendered component, not generalized from C022's text-pair table. Focus Appearance remains distinct from Focus Not Obscured and is not silently promoted to an AA requirement.

## Gate
C023 is ready for W021 browser transfer. It does not PASS contextual focus/non-text behavior until actual rendered adjacent surfaces and forced-colors output are inspected/calculated.

## HANDOFFS TO OTHER SPECIALISTS
- Web: return exact computed surfaces/forced-color behavior.
- Layout: return overlap/adjacency geometry when focus crosses surfaces.
- Interaction: availability semantics remain independent of contrast reduction.
- Content: preserve verbal state identity when hue is unavailable.
- Type: no character distinction by hue.

## Evidence boundary
No browser parity, physical display, CVD/low-vision observer, AT or human salience PASS is claimed.