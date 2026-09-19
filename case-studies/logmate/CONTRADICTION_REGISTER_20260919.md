# LogMate Design Contradiction Register — 2026-09-19

Status: **SYNTHESIS GATE — CURRENT MATERIAL CONTRADICTIONS AUDITED**  
Evidence base: `EVIDENCE_MAP_20260919.md`

Disposition vocabulary:
- **RESOLVED** — current synthesis has a clear precedence/scope answer.
- **SCOPED** — both rules remain valid in different roles/surfaces.
- **OPEN** — missing evidence blocks final rule.
- **BLOCKER** — do not promote affected design code until resolved.
- **SUPERSEDED** — historical conclusion remains evidence but no longer governs the current product role.

## Register

| ID | Contradiction / tension | Class | Resolution / current rule | Status |
|---|---|---|---|---|
| CR01 | Historical T017/T018/T020 preference for proportional operational identifiers vs current View Logbook mono body contract. | Authority / evidence-level | Current owner/canonical product contract wins. Historical studies remain useful for geometry/fallback warnings but no longer govern View Logbook Date/Flight/DEP/ARR/body typography. | **RESOLVED / historical role SUPERSEDED** |
| CR02 | T072 says mixed identifiers should not be solved by blanket mono vs owner decision that repeated Flight identifiers use mono. | Scope | T072 correctly rejects **blanket app-wide mono**. Current product uses a **specific operational-data mono role**, not blanket mono. Flight also retains semantic zoning. | **SCOPED / RESOLVED** |
| CR03 | Home snapshot lists mono only for Date and DEP/ARR, while owner now confirms Flight mono as well. | Document conflict | Owner clarification on 2026-09-19 supersedes the older snapshot typography detail for future identity work. Structural snapshot remains useful for IA, not this typography detail. LogMate restart branch `b52bb43c...` updates the UI contract/restart/foundation accordingly. | **RESOLVED — docs updated** |
| CR04 | View Logbook generic `fontFamily: 'monospace'` can vary by platform vs need for exact premium/stable rendering. | Evidence-level | Design intent = mono; production technique = exact registered mature mono family with explicit weights/fallback. Generic family is prototype-only. | **OPEN IMPLEMENTATION / BLOCKER for production type contract** |
| CR05 | Mono Flight characters can be equal width but short/long whole identifiers still shift if centered. | Geometry | Keep carrier zone + gap + number/suffix zone fixed starts. Mono solves internal glyph advance variance; zoning solves variable-length semantic start positions. | **RESOLVED** |
| CR06 | Equal per-character layout cells stabilize origins but produced unacceptable spacing. | Aesthetic/function | Fixed-cell experiment rejected. Do not restore. Use actual mono role + semantic zones. | **RESOLVED / REJECTED** |
| CR07 | Whole-string intrinsic centering vs stable Flight comparison. | Geometry | Whole-string centering rejected; internal zoning is canonical. | **RESOLVED** |
| CR08 | Home mock dates such as `Sep 02` vs canonical numeric locale date presentation. | Product contract | Future visual fixtures follow `DateFormats` numeric locale contract. Historical textual mock date is non-canonical fixture evidence only. | **RESOLVED** |
| CR09 | Numeric stability vs desire to make every number monospace. | Scope | View Logbook body follows mono contract. Standalone summary metrics/current period use role-driven typography + tnum where comparison benefits. Do not blanket-mono every numeric occurrence. | **SCOPED** |
| CR10 | tnum alignment benefit vs increased intrinsic width. | Priority tension | Activate the correct numeric feature first, then size/recompose layout around production strings. Do not disable alignment merely to save a few px. | **RESOLVED principle / exact widths OPEN** |
| CR11 | Fixed compact ledger geometry vs 200% text/reflow. | Hard at same geometry | Baseline compact ledger may retain dense 2D semantics; large-text path must recompose/expand/scroll rather than shrink type. Exact product strategy remains to implement/test. | **OPEN / BLOCKER for large-text production claim** |
| CR12 | WCAG reflow vs essential two-dimensional ledger. | Scope | Ledger may qualify for controlled 2D scrolling when meaning requires it; surrounding controls/forms do not inherit the exception. | **SCOPED / RESOLVED** |
| CR13 | Stable data axes vs responsive/adaptive recomposition. | Scope | Preserve within-region comparison axes and semantic order; do not preserve identical whole-screen coordinates. | **RESOLVED** |
| CR14 | Dense professional information vs “premium whitespace”. | Priority tension | Calmness comes from hierarchy/alignment/reduced competition, not arbitrary emptiness. Protect useful professional data first. | **RESOLVED principle** |
| CR15 | Required semantic strings vs narrow layout. | Priority tension | Recompose/wrap/allocate width before semantic shortening. Only established governed abbreviations may be used. | **RESOLVED principle** |
| CR16 | Brand distinctiveness vs unfinished custom LogMate font. | Evidence-level | Custom type cannot be required for identity until T021 and downstream gates close. Use mature production controls now. | **RESOLVED for current phase** |
| CR17 | Brand identity vs mono operational-data role potentially feeling “technical”. | Priority tension | Mono is a functional data voice, not the whole brand. Identity must also emerge from proportional UI, spacing, color, interaction and composition. | **SCOPED** |
| CR18 | Calm/premium palette vs focus/error/ambiguous/recovery salience. | Priority tension | Consequence-bearing state wins. Reduce decorative chroma before state salience. | **RESOLVED** |
| CR19 | One signature accent used for brand, focus, selection and success. | Hard semantic collision | Prohibit role collision. Separate brand/accent and semantic-state tokens; use redundant non-color cues. | **RESOLVED / prohibited** |
| CR20 | Light/dark brand consistency vs identical color values. | Scope | Preserve relational role and perceived hierarchy; literal values may differ by appearance/environment. | **RESOLVED** |
| CR21 | Quiet separators/low chrome vs discoverable grouping and controls. | Priority tension | Whitespace/alignment may replace chrome only when grouping/target/state remains unambiguous. Functional boundaries stay when needed. | **RESOLVED principle** |
| CR22 | Brand signature motion vs reduced motion and state truth. | Hard if motion is sole carrier | Motion may reinforce continuity only. Static/reduced-motion state and focus must remain complete. | **RESOLVED constraint** |
| CR23 | Drag/reorder as signature interaction vs WCAG dragging alternative. | Normative | Cannot promote drag itself as a brand code until equivalent non-drag single-pointer path exists where applicable. | **OPEN / BLOCKER** |
| CR24 | Minimal content vs professional consequence/recovery clarity. | Priority tension | “No words without a job” — not “fewest words”. Consequential state/recovery wording cannot be removed for visual calm. | **RESOLVED principle** |
| CR25 | Brand consistency across surfaces vs identical component/composition reuse. | Scope | Brand codes transfer as rules/relationships, not copied Home geometry. Surface-specific composition is allowed. | **RESOLVED** |
| CR26 | Home-only visual success vs design-code promotion. | Evidence-level | No brand code is promoted until it survives View Logbook, Activity, Add Flight and relevant configuration surfaces. | **RESOLVED process rule** |
| CR27 | Static Chromium/browser evidence vs Flutter/iOS/Android/PWA production rendering. | Evidence-level | Static/browser findings can reject obvious failures but cannot certify native parity. Follow W103 promotion ladder. | **OPEN / production gate** |
| CR28 | Exact brand type vs font-load/fallback failure. | Runtime | Fallback must preserve meaning and workable geometry; exact family/load state recorded in validation. | **OPEN validation** |
| CR29 | Sparse color identity vs forced-colors/user override. | Runtime/accessibility | Semantic operation and identity hierarchy must remain understandable when authored color disappears. | **OPEN runtime proof; principle resolved** |
| CR30 | Aviation visual identity vs cockpit/pilot-watch motif borrowing. | Brand integrity | Domain expertise is conveyed through correct data/workflow, not cockpit cosplay. Decorative aviation motifs remain prohibited. | **RESOLVED / prohibited** |
| CR31 | Luxury-brand inspiration vs copying luxury styling (serif/gold/metal/thin rules). | Brand integrity | Transfer standards/reduction/discipline/design-code method only. Do not copy surface motifs as evidence of premium. | **RESOLVED / prohibited** |
| CR32 | Minimalism as visual style vs rational reduction. | Brand/layout/content | Reduction is outcome of function and hierarchy. Empty/sparse appearance is not a target by itself. | **RESOLVED** |
| CR33 | Cross-surface semantic consistency vs literal visual sameness. | Scope | Preserve semantic identity, state truth and design-code logic; adapt geometry/content realization by surface. | **RESOLVED** |
| CR34 | Mono ledger + multilingual user/free text. | Scope | Controlled operational codes/values may use mono role; Crew/Remark/source text stay Unicode/fallback-safe proportional roles unless independently justified. | **RESOLVED** |
| CR35 | Arrow in Route as data glyph vs structural relation mark. | Scope | Arrow is structural relation mark; it need not inherit operational mono family. Alignment/contrast remains composition-owned. | **RESOLVED** |
| CR36 | Product date format changes by locale vs stable column geometry. | Priority tension | Use canonical formatter and stress supported locale formats; layout must budget the approved format rather than hard-code one mock string. | **OPEN exact geometry / principle resolved** |
| CR37 | Header/body/totals fixed 36px ledger rhythm vs font-family/scale changes. | Evidence-level | 36px baseline rhythm remains product contract at normal presentation; large-text/native transfer must verify whether alternate mode/recomposition is required. | **OPEN validation** |
| CR38 | Premium perception/trust claim vs no representative-pilot evidence. | Evidence-level | Owner review can select direction; do not claim representative premium/trust/usability until appropriate human evidence exists. | **RESOLVED evidence boundary** |
| CR39 | Glare/night-readability ambitions vs static Light/Dark screenshots. | Evidence-level | Static screenshots are not physical environment evidence. Device/glare/night validation remains later gate. | **OPEN validation** |
| CR40 | Old Round-1 concept C “least objectionable” vs clean restart. | Anchoring/process | C is not selected, preferred or a starting point. No rails/divisions from C inherit authority. | **RESOLVED / prohibited anchoring** |

## High-risk unresolved items

These are the contradictions most likely to create large rework if ignored:

### H1 — Exact production mono family
Design intent is now clear, but generic `monospace` is not deterministic enough for production.  
**Required before final typography contract:** exact font asset, weights, fallback, Flutter/iOS/Android/PWA render comparison.

### H2 — Large-text dense-ledger behavior
Normal compact geometry and 200% accessibility requirements cannot be assumed to coexist unchanged.  
**Required:** explicit adaptive ledger strategy and runtime validation.

### H3 — Date locale width contract
Canonical date formatting is numeric/locale-dependent; visual prototypes must stop tuning to `Sep 02`.  
**Required:** stress actual formatter outputs for supported locale orderings.

### H4 — Cross-surface identity transfer
No candidate signature code exists yet.  
**Required:** any future code must be tested on Home + View Logbook + Activity + Add Flight before promotion.

### H5 — Runtime evidence
Static/Chromium proof is insufficient for final native/PWA typography and state claims.  
**Required:** W103 promotion ladder.

## Resolved synthesis rules that may feed the next phase

1. Product/domain truth outranks visual fit.
2. Repeated operational Flight data uses mono treatment where confirmed, with semantic sub-zones retained.
3. General UI is not blanket mono.
4. Numeric comparison uses tnum where appropriate outside mono roles.
5. Stable axes are local semantic relationships, not frozen screen coordinates.
6. Dense ledger may scroll horizontally; surrounding UI reflows.
7. Protected strings are not shortened to rescue geometry.
8. Brand accent never replaces semantic-state salience.
9. Motion never carries state alone.
10. Design codes must transfer by rule across major surfaces.
11. Custom LogMate font is not a current dependency.
12. Historical Round-1 visuals and fixed-character-cell experiments remain rejected.

## Gate result

**Evidence Map: COMPLETE for current synthesis scope.**  
**Contradiction Register: COMPLETE for currently known material contradictions.**

This does **not** mean every implementation question is closed. It means unresolved questions are now explicit and no currently known material cross-domain contradiction is hidden inside the next design phase.

Next allowed phase under the synthesis gate:
`Integration Principles -> Design Corridor -> Operational Geometry Contract -> Signature Code Study`.

The next phase must consume this register rather than reopening resolved historical alternatives without new evidence.


## Reconciliation completion note

The owner clarification for repeated Flight identifiers was propagated to the LogMate visual-identity restart branch at commit `b52bb43cb87632ca5000760e2c95a5fc8581c7a7`.

This closes the documentation conflict identified by CR03. The remaining high-risk items H1–H5 are explicit implementation/runtime/cross-surface evidence gaps, not hidden contradictions.
