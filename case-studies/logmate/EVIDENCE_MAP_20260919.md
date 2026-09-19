# LogMate Design Evidence Map — 2026-09-19

Status: **SYNTHESIS GATE — FINAL FULL AUDIT COMPLETE FOR CURRENT VISUAL-IDENTITY WORK**  
Companion: `CONTRADICTION_REGISTER_20260919.md`  
Gate: `DESIGN_SYNTHESIS_GATE_20260919.md`

## 0. Review scope

This map was produced after re-reading the Design Studio governance/index/status layer, the current specialist synthesis inputs, the relevant foundational studies, the LogMate-specific transfer studies, and the current LogMate product contracts.

The purpose is not to summarize every file in the repository. It is to include every materially relevant finding that can change the LogMate visual-identity, operational-data geometry, interaction-state, content, responsive, accessibility, runtime, or evidence-promotion decision.

### Governance / status reviewed
- `AGENTS.md`
- `progress/STATUS.md`
- `progress/TYPE_STATUS.md`
- `progress/COLOR_STATUS.md`
- `progress/LAYOUT_STATUS.md`
- `progress/WEB_STATUS.md`
- `progress/CONTENT_STATUS.md`
- `research/README.md` and all specialist READMEs
- `methods/PROJECT_ENGAGEMENT.md`

### Foundational evidence reviewed or re-traced through current synthesis
Type:
- `001-type-as-system.md`
- `002-metrics-spacing-optical-rhythm.md`
- `005-numerals-punctuation-systems.md`
- `009-typography-as-information-architecture.md`

Color:
- `008-color-luminance-contrast-hierarchy.md`
- `C002-semantic-color-role-token-architecture.md`
- `C007-fixed-geometry-color-density-salience.md`
- `C015-stage1-perceptual-context-capstone.md`
- `C023-contextual-focus-nontext-transfer-contract.md`

Layout:
- `006-grid-composition-hierarchy.md`
- `014-perceptual-grouping-spatial-grammar.md`
- `L002-whitespace-density-spatial-rhythm.md`
- `L004-tabular-numerals-dense-comparison-transfer.md`
- `L005-color-driven-density-salience-transfer.md`
- `L012-three-surface-spatial-system.md`

Interaction / accessibility:
- `004-accessibility-reflow-targets-focus.md`
- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`
- `I041-owner-review-gate-and-internal-iteration.md`
- `I042-integrated-workflow-internal-review-gate.md`

### LogMate-specific transfer / synthesis reviewed
Type:
- `LOGMATE_TYPE_IDENTITY_LIVE_PROJECT_DIRECTIVE.md`
- T017 operational geometry transfer
- T018 conservative font audit
- T020 Flutter typography validation
- T021 operational family / glyph coverage chain
- T044 dense-ledger compact-header transfer
- **T072 synthesis operational-string geometry boundary**

Color:
- C074 auth transfer
- C075 Customize state visibility
- **C103 brand-salience / semantic-state contradiction audit**

Layout / Interaction:
- L065 auth reflow
- L066 Customize density
- L093 import mapping geometry
- **L094 cross-surface operational geometry synthesis**
- I061 auth transfer
- I062 Customize reorder/recovery
- I089 import mapping authority
- **I090 synthesis precedence/state-salience**

Web:
- W074 auth runtime
- W075 Customize browser closure
- **W103 synthesis runtime/evidence-promotion gate**

Content:
- CD080 auth transfer
- CD081 Customize semantic governance
- CD108 import mapping uncertainty/localization
- **CD109 synthesis semantic density/brand voice**

Project case study:
- `README.md`
- `BRAND_PHILOSOPHY_RESET_20260919.md`
- `DESIGN_SYNTHESIS_GATE_20260919.md`

### Current LogMate product authority checked
Repository: `yhappcom/logmate`

- `MASTER.md`
- `docs/specs/ui-contract.md`
- `docs/specs/search-interaction-spec.md`
- `docs/specs/logbook-configuration-spec.md`
- `design/HOME_CURRENT_SNAPSHOT.md`
- `design/DECISIONS.md`
- visual-identity restart documents

### Current external authority rechecked
- Flutter official custom-font and `TextStyle.fontFamily` documentation: exact family names/assets are the reliable custom-font path; fallback is ordered and platform fallback may occur.
- W3C WCAG 2.2 current guidance: Reflow, Non-text Contrast, Focus, Target Size, Dragging Movements remain applicable by scope.

### Audit provenance note
- `AGENTS.md` assigns canonical specialist status to `TYPE_STATUS.md`, `COLOR_STATUS.md`, `LAYOUT_STATUS.md`, `WEB_STATUS.md`, and `CONTENT_STATUS.md`.
- Those specialist status files are synchronized to 2026-09-19 and identify T072 / C103 / I090+L094 / W103 / CD109 as the current LogMate synthesis inputs.
- `progress/STATUS.md` remains coordinator-synced to 2026-09-16 and contains older maturity summaries. For this case study, dated specialist status plus the underlying study is used for current specialist maturity; stale aggregate lines are not allowed to downgrade or overwrite newer specialist evidence.

## 1. Evidence authority order

For the current project synthesis:

1. **Owner-confirmed / canonical LogMate product contract**
2. **Normative accessibility/platform requirement**
3. **Current cross-specialist synthesis evidence**
4. **Current specialist transfer evidence**
5. **Foundational design evidence**
6. **Implementation/static/browser evidence**
7. **Historical/rejected visual experiments**

A historical specialist recommendation cannot silently override a later owner-confirmed product decision.

---

# 2. Evidence Map

| ID | Finding | Evidence class | Primary source(s) | Scope / implication | Maturity |
|---|---|---|---|---|---|
| E01 | Professional/domain meaning must not be invented or collapsed for visual convenience. | CANONICAL PRODUCT | LogMate MASTER; CD081/CD109 | Visual design cannot merge Block/Actual/Inst/IFR etc. or shorten away distinct semantics. | CONFIRMED |
| E02 | Home product semantics, information families and confirmed IA/interaction relationships are preserved as structural baseline; the current candidate's visual composition is not the final visual baseline. | CANONICAL PRODUCT / OWNER | Home snapshot; visual restart; ui-contract | New identity work may re-author composition/appearance where the restart reopens the visual layer, but may not silently change confirmed product structure or behavior. | CONFIRMED / SCOPED |
| E03 | Home Current Period metric identity is Block Time. | CANONICAL PRODUCT / OWNER | MASTER; ui-contract | Visual hierarchy may change; semantic identity may not. | CONFIRMED |
| E04 | View Logbook Standard uses Date / Type / Reg / Flight / DEP / ARR / Block / Night / Inst / Remark. | CANONICAL PRODUCT | ui-contract | Dense-ledger stress corpus is fixed enough for synthesis. | CONFIRMED |
| E05 | View Logbook ledger body uses regular monospace/code at w400; Date, Flight, DEP/ARR, Block/Night/Inst are included. | CANONICAL PRODUCT | ui-contract §View Logbook ledger typography | Historical proportional-identifier recommendations cannot override this role. | CONFIRMED |
| E06 | Flight identifier = 2-char IATA carrier + 1–4 digit number + optional suffix; carrier and number/suffix have distinct fixed starts. | CANONICAL PRODUCT | ui-contract | Even with mono, whole-string centering is not the Flight geometry. | CONFIRMED |
| E07 | Repeated Home/Activity Flight identifier is to use the mono operational-data treatment to eliminate glyph-width jitter, while retaining Flight internal zoning. | OWNER CLARIFICATION 2026-09-19 | current owner direction; companion contradiction register | Applies where repeated Flight rows are presented; does not imply all app text is mono. | CONFIRMED FOR SYNTHESIS |
| E08 | Home Date and DEP/ARR had already converged to selective monospace w400 candidate treatment. | OWNER-REVIEW CANDIDATE | Home snapshot / D019 refinement F | New identity work should treat mono operational data as an established direction, subject to exact production-family selection. | CURRENT DIRECTION |
| E09 | Product-authored general UI does not become blanket monospace. | CANONICAL + SYNTHESIS | ui-contract scope; Type role research | UI labels, prose, controls and free text remain role-driven/proportional unless later evidence changes them. | SUPPORTED |
| E10 | The actual production mono family must be explicit/deterministic; generic `fontFamily: 'monospace'` is not a strong cross-platform contract. | PLATFORM + TYPE | Flutter official font docs; T018/T072; prior Home review | Choose/register exact mature mono asset before production promotion. | OPEN IMPLEMENTATION |
| E11 | Custom/bespoke LogMate type is not production-ready. T021 remains blocked/in practice. | TYPE EVIDENCE | TYPE_STATUS; T021 chain; T072 | Identity work must not freeze geometry around unfinished custom metrics. | CONFIRMED BOUNDARY |
| E12 | Typography roles precede font choice. Identity/UI/data roles can use different behavior without requiring multiple decorative fonts. | SUPPORTED DESIGN PRINCIPLE | Type 009 | Allows restrained mixed role system: proportional UI + exact mono operational data + tabular numeric summaries. | SUPPORTED |
| E13 | Font metrics, sidebearings, advance width and visible contour are different layers; target-size raster matters. | SUPPORTED DESIGN PRINCIPLE | Type 001/002 | Static vector or nominal size cannot certify scan rhythm. | SUPPORTED |
| E14 | Tabular figures equalize numeric advance when supported; they do not solve alphabetic/mixed identifiers. | TYPE + LAYOUT EVIDENCE | Type 005; L004; T072 | Use tnum for comparison numerics outside mono-ledger roles when appropriate. | SUPPORTED |
| E15 | tnum can increase intrinsic width; Layout must budget using production formatting and active font feature. | EXECUTED TRANSFER | L004 | Numeric alignment is Type+Layout contract, not a font-only setting. | EXECUTED / BOUNDED |
| E16 | Repeated operational data needs stable comparison axes. | CROSS-SPECIALIST SYNTHESIS | L094; T072; I090 | Date/Flight/DEP/ARR/Reg/durations cannot visibly jitter across rows. | SUPPORTED |
| E17 | Stable axes do not mean globally fixed screen coordinates. | CROSS-SPECIALIST SYNTHESIS | L094; I090 | Responsive recomposition may change regions while preserving local comparison logic. | SUPPORTED |
| E18 | View Logbook is legitimately two-dimensional/dense; horizontal scroll may be required when semantic width exceeds viewport. | PRODUCT + ACCESSIBILITY-SCOPED | ui-contract; L066; WCAG reflow exception | Do not crush/truncate columns merely to avoid horizontal scroll. | SUPPORTED |
| E19 | Surrounding controls/forms do not automatically inherit the ledger's two-dimensional exception. | LAYOUT / WEB | L066; W075/W103 | Home/Add Flight/Customize should reflow ordinarily. | SUPPORTED |
| E20 | 200%/enlarged-text failure cannot be repaired by shrinking text, negative tracking or forcing a condensed/mono aesthetic. | TYPE + LAYOUT | T018/T020/T044; L094 | Recompose, expand or change presentation; exact large-text ledger strategy remains to validate. | SUPPORTED / IMPLEMENTATION OPEN |
| E21 | Required professional strings are protected; fit pressure is not permission to rename or abbreviate arbitrarily. | CONTENT + TYPE | CD081/CD109; T044/T072 | Geometry adapts before semantics are damaged. | SUPPORTED |
| E22 | Abbreviations are acceptable only when established, unambiguous and governed. | CONTENT | CD109 | Compact ledger headers may be short; ad-hoc shortening is rejected. | SUPPORTED |
| E23 | User/source evidence and professional identifiers must not be translated/rewritten for visual convenience. | CANONICAL / CONTENT | MASTER Language/Locale; ui-contract; CD108/CD109 | Source/user identifiers preserve their original evidence. Product-authored LogMate UI remains English-only; numeric date locale ordering is a separate presentation contract. | CONFIRMED |
| E24 | Current product date contract is numeric/locale-ordered; textual mock dates such as `Sep 02` are not canonical date evidence. | CANONICAL PRODUCT | ui-contract date locale section | New visual fixtures must use DateFormats contract rather than historical mock wording. | CONFIRMED |
| E25 | Whitespace is structural, not synonymous with low density. Dense aligned data can be calm. | LAYOUT / HUMAN-FACTORS SYNTHESIS | L002; L005 | Premium restraint must not force unnecessary sparsity. | SUPPORTED |
| E26 | Density has multiple causes: geometry, grouping, color salience, feature competition and semantic complexity. | LAYOUT/COLOR | L002/L005/C007 | Diagnose before adding whitespace or removing data. | SUPPORTED |
| E27 | Luminance hierarchy should work before decorative hue hierarchy. Low-noise does not mean faint text. | COLOR | Color 008 | Premium/calm direction must retain strong primary information. | SUPPORTED |
| E28 | Brand color must have a defined role and must not be sprayed across utility navigation or every heading. | COLOR | Color 008; C103 | Accent is scarce resource. | SUPPORTED |
| E29 | Focus, invalid/destructive/ambiguous/recovery, selection/context, ordinary hierarchy, brand, decoration form a salience precedence; brand comes after consequential state. | CROSS-SPECIALIST COLOR/INTERACTION | C103; I090 | Brand treatment cannot compete with focus/error/recovery. | SUPPORTED |
| E30 | A signature accent cannot simultaneously mean brand, focus, selection and success. | CONTRADICTION-RESOLVED PRINCIPLE | C103 | Role-separated tokens + non-color cues required. | SUPPORTED |
| E31 | Light/dark/night continuity should preserve semantic relationships, not identical literal values. | COLOR | C103; C002 | Identity code should be relational. | SUPPORTED |
| E32 | Forced-colors/user overrides may remove authored color; semantic operation must survive structurally. | COLOR/WEB/NORMATIVE | C103; W103; WCAG | Color cannot be sole brand/state carrier. | SUPPORTED |
| E33 | Visible mark and interactive target are separate layers. | ACCESSIBILITY FOUNDATION | 004 accessibility | Small refined icons/actions may keep larger hit geometry. | SUPPORTED |
| E34 | Focus is positional information and cannot be visually suppressed for cleanliness. | NORMATIVE / INTERACTION | WCAG; 004; I090 | Design Corridor must reserve a real focus treatment. | SUPPORTED |
| E35 | Motion may reinforce transition but cannot be the only state channel; reduced-motion path must preserve truth. | INTERACTION / WEB | I090; W103 | Signature motion, if any, is secondary. | SUPPORTED |
| E36 | Drag interaction cannot become a brand signature while required non-drag single-pointer equivalence remains unimplemented. | NORMATIVE / INTERACTION | WCAG 2.2; I090; W075 | Reorder gesture remains implementation work, not identity code. | OPEN BLOCKER |
| E37 | Interaction salience follows consequence/state ownership, not generic brand emphasis. | CROSS-SPECIALIST | I090; C103; CD109 | Quiet design must still make consequential state obvious. | SUPPORTED |
| E38 | Calm brand voice cannot soften warnings/recovery until consequence becomes vague. | CONTENT | CD109 | Tone is subordinate to truth. | SUPPORTED |
| E39 | A durable brand code must transfer by rule across Home, View Logbook, Activity, Add Flight and relevant configuration surfaces; copying one composition is not transfer. | SYNTHESIS GATE | L094; W103; brand research | Home-only motif cannot be promoted as brand identity. | SUPPORTED |
| E40 | Static visual coherence is not runtime evidence. | WEB EVIDENCE | W103 | Native/browser/font-load/reflow failures override screenshot confidence. | SUPPORTED |
| E41 | Font-load/fallback state is part of geometry validation. | TYPE/WEB/PLATFORM | T072; W103; Flutter docs | Exact family and fallback behavior must be captured. | SUPPORTED |
| E42 | Physical-device glare/night, representative-pilot scanning/workload, trust/premium perception remain human/device evidence gaps. | EVIDENCE BOUNDARY | specialist statuses; brand study | Do not claim these from static prototypes. | OPEN |
| E43 | Owner review is valuable for design direction but is not representative-user usability evidence. | PROCESS | I041/I042 | Present coherent candidates after deterministic contradictions are removed. | SUPPORTED |
| E44 | Brand research converges on standards, reduction, coherence, repeatable codes, longevity, detail discipline and tool character—not luxury ornament. | PROJECT RESEARCH | Brand philosophy reset | “Premium” must emerge from execution standards, not gold/serif/metal/cockpit motifs. | SUPPORTED |
| E45 | LogMate identity should be professional/non-theatrical; aviation expertise is expressed through correct operational data/workflow, not cockpit cosplay. | PROJECT RESEARCH + OWNER DIRECTION | brand reset; project case study | Explicit anti-motif constraint. | SUPPORTED |
| E46 | Reduction means removing workless elements, not creating emptiness or hiding professional information. | BRAND + LAYOUT + CONTENT | brand reset; L002; CD109 | Minimalism is not the target style. | SUPPORTED |
| E47 | A design code should be a repeated rule/behavior, not a one-screen decoration. | BRAND SYNTHESIS | RIMOWA/LAMY/NOMOS synthesis; gate | Candidate codes must survive cross-surface transfer. | SUPPORTED |
| E48 | The frozen Round-1 A/B/C concepts are rejected and cannot seed the next visual direction. | OWNER | visual restart | No rail/serif/ruled-search inheritance by default. | CONFIRMED |
| E49 | Equal per-character fixed-cell experiment is rejected because of artificial letter/number spacing. | OWNER / RENDERED REVIEW | D019 history | Do not restore character-cell approach to solve identifier jitter. | CONFIRMED REJECTED |
| E50 | Whole-string Flight centering is rejected; internal Flight zoning remains. | OWNER / PRODUCT | D019; ui-contract | Prevents short/long flight strings from moving the semantic start points. | CONFIRMED |
| E51 | LogMate product-authored UI is English-only. Device language does not translate UI copy; locale affects numeric date ordering/presentation only. | CANONICAL PRODUCT | MASTER §8; ui-contract Language/Locale; D-007 | Future visual fixtures and content studies must not introduce Korean or other translated product labels as canonical LogMate UI. | CONFIRMED |
| E52 | Home Activity quick-period canonical literals are `Last 7 days`, `Last 28 days`, `Last 90 days`, `Custom`. | CANONICAL PRODUCT | MASTER UI/Navigation; ui-contract; D-009 | `7 days / 28 days / 90 days` in the Home snapshot is current-candidate shorthand, not authority to rewrite the product label contract. | CONFIRMED |
| E53 | Whole-app navigation architecture remains NAV-001 OPEN. | CANONICAL PRODUCT OPEN | MASTER §7 / OPEN decisions | The current Home candidate containing no bottom navigation does not decide sidebar vs bottom tabs vs push-route architecture for the product. | OPEN — DO NOT INFER |
| E54 | The 2026-09-19 blank-canvas restart is a **visual-layer reset**, not a product reset. | OWNER / CANONICAL SCOPE | visual restart; MASTER; ui-contract | Preserve confirmed View Logbook semantics/geometry, Flight semantics, Add Flight semantics, Activity semantics, Search boundaries, English-only policy and accessibility/platform contracts while re-authoring visual expression. | CONFIRMED |
| E55 | View Logbook retains confirmed dense-ledger geometry: normal 36px header/body/total rhythm; LEFT/START anchoring; compact semantic widths summed rather than stretched; sticky header; header/body/totals share semantic column boundaries and horizontal offset; horizontal scroll is used when semantic width exceeds available content width. | CANONICAL PRODUCT | MASTER View Logbook; ui-contract View Logbook | Visual identity may restyle the ledger but cannot silently erase these confirmed geometry contracts. Large-text/native adaptation remains separately OPEN. | CONFIRMED NORMAL-PRESENTATION CONTRACT |
| E56 | Add Flight's current stock card/Material visual treatment is superseded, but confirmed entry semantics and task-specific interactions remain product authority. | CANONICAL PRODUCT / VISUAL RESET | MASTER implementation matrix; ui-contract Add flight entry UI shell | Visual redesign may replace styling/composition without inventing new field semantics, automatic calculations, airport-search behavior or save semantics. | CONFIRMED / VISUAL TREATMENT OPEN |
| E57 | Home Search and Add Flight airport lookup are separate contracts. Home suggestion/autocomplete/result structure remains SEARCH-001 OPEN; Add Flight airport lookup has confirmed task-specific offline behavior. | CANONICAL PRODUCT | MASTER; search-interaction-spec; ui-contract | Visual identity work must not use Add Flight autocomplete as evidence that Home Search autocomplete/suggestions are confirmed. | CONFIRMED BOUNDARY / SEARCH-001 OPEN |
| E58 | The latest Content synthesis voice (`precise`, `quiet`, `operational`, `non-theatrical`, consequence-explicit, recovery-forward) is a PROJECT-SPECIFIC CANDIDATE, not approved production copy. | CONTENT SYNTHESIS | CD109 | It may inform later Integration Principles but cannot override canonical terminology/state truth or be treated as owner-approved voice. | CANDIDATE / NOT PASS |
| E59 | T072/L094/CD109 EN/KO or localization stress references are specialist stress methodology, not LogMate product-language authority. | EVIDENCE-SCOPE RECONCILIATION | T072; L094; CD109; MASTER §8; ui-contract | For LogMate UI fixtures use English product copy, canonical numeric date locale formats, and Unicode/source-data stress where source/user evidence requires it. | RESOLVED SCOPE |
| E60 | The Home snapshot's `no bottom navigation implied by this candidate` is surface-candidate evidence only. | CURRENT CANDIDATE / PRODUCT OPEN | Home snapshot; MASTER NAV-001 | It may describe the current Home candidate but cannot be promoted to app-wide IA. | SCOPED |
| E61 | Current specialist synthesis authority is T072 / C103 / I090+L094 / W103 / CD109 as recorded by the 2026-09-19 specialist status files. | STUDIO GOVERNANCE / EVIDENCE PROVENANCE | AGENTS; specialist status files | Older global-status maturity prose and earlier specialist studies remain history unless independently still applicable; they do not outrank later owner/canonical product decisions. | CONFIRMED PROVENANCE |

---

## 3. Current synthesis baseline

The evidence supports the following **inputs**, not yet the final Design Corridor:

- General UI: role-driven proportional typography.
- Repeated operational row data: deterministic mono role where owner/product contract specifies it.
- Flight: mono operational data **plus** stable carrier / number+suffix zones.
- Comparison numerics outside mono-ledger roles: tabular figures when comparison requires stable digit advances.
- Dense ledger: preserve semantic columns and controlled horizontal scrolling when necessary.
- Responsive identity: preserve relationships/axes, not identical coordinates.
- Color: neutral operational field first; accent/state roles separated.
- Interaction: consequence/focus/recovery salience outranks brand calm.
- Content: semantic truth and established professional terminology outrank fit; product-authored UI is English-only.
- Date presentation: numeric locale ordering uses the canonical `DateFormats` contract; language localization is not implied.
- Activity: canonical quick-period labels are `Last 7 days / Last 28 days / Last 90 days / Custom`.
- Navigation: current Home has no bottom nav, but whole-app navigation architecture remains NAV-001 OPEN.
- Visual reset: re-author the visual layer while preserving confirmed semantics, IA/interaction contracts and dense-ledger geometry.
- Add Flight/Search: confirmed Add Flight semantics survive restyling; Home Search suggestion behavior remains SEARCH-001 OPEN and separate from airport lookup.
- Identity: repeatable, restrained, cross-surface rules; no luxury or aviation decoration shortcut.
- Evidence: no cross-surface brand code promoted from static Home alone.

## 4. Remaining evidence gaps and scoped OPEN product decisions

1. Exact production mono family for Flutter/iOS/Android/PWA.
2. Native/runtime measurement of the mono Flight zoning and long identifier corpus.
3. Exact large-text/reflow strategy for dense ledger.
4. Cross-surface render proof of candidate design codes.
5. Forced-colors and independent-engine transfer for web/PWA.
6. Physical-device glare/night review.
7. Representative-pilot scanning/workload/comprehension evidence when app implementation is ready.
8. NAV-001 — whole-app navigation architecture; do not infer it from the Home candidate.
9. SEARCH-001 — Home Search suggestion/autocomplete/result-entry behavior; do not infer it from Add Flight lookup.

These gaps do not block creation of Integration Principles and later Design Corridor/Geometry/Signature studies as **candidate contracts** where their scope is unaffected. They do block production/human PASS claims and block any rule that would silently decide NAV-001, SEARCH-001, or the other listed OPEN implementation questions.
