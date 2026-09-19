# Candidate 03 — Interaction Review — 2026-09-20

Status: **FAIL / INTERACTION BLOCKERS BEFORE OWNER REVIEW**

Evidence reviewed:
- Candidate 03 Flutter implementation at `bf2f45a4f676f2473e0ab5536ca6ab7e2d0f1046`
- 390×844 code-mirror render
- current I102 interaction constraints

This review does not consult prior Home candidates.

## Blocking findings

1. **View all / Details are not interactive controls in the Flutter implementation.**
   They are rendered as plain Text. The screen visually promises navigation that the current implementation does not provide.

2. **Month navigation target is too small.**
   The current `_MonthStep` uses a 26×24 box. Visible glyph size may be small, but the interactive target must be materially larger.

3. **Activity period targets are too small.**
   The options use only text padding inside a Wrap. They do not provide robust touch-target geometry.

4. **Search target height is undersized.**
   The visual field is 38px high. The interaction area should be raised to the established control/touch-target expectations.

5. **Bottom commands are semantically clear but need explicit route/action wiring evidence.**
   Their 48px rail is directionally acceptable, but this static preview cannot claim route/state restoration.

## Positive findings

- Add Flight and View Logbook are visually equal rather than implying an unsupported hierarchy.
- Activity selection uses weight + underline + color, avoiding color-only state.
- No SEARCH-001 suggestion/result behavior is invented.
- The command rail is distinguishable from app-wide navigation because it contains task actions rather than destination tabs.

## Required correction

- Replace View all / Details Text with semantic InkWell/TextButton-like controls with at least 44px target height.
- Increase month-step touch target to at least 40–44px while keeping the glyph visually restrained.
- Give each Activity period option a minimum 44px interaction target; a 2×2 control is acceptable if Layout review uses that geometry.
- Raise Search interaction height to at least 44px.
- Preserve route/search behavior as OPEN; do not fabricate navigation state.

Verdict: **FAIL UNTIL INTERACTION GEOMETRY IS CORRECTED AND RE-RENDERED.**
