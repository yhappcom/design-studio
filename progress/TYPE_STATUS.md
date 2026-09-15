# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T018`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, Unicode/text normalization boundaries, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, `mark`/`mkmk` anchor-chain release QA, Unicode normalization-sensitive subset closure, Hangul NFC↔NFD structural package transfer, bounded Chromium canonical-equivalent Hangul cluster matching/render transfer, downloadable-webfont loading/failure/fallback geometry with a controlled metric-matching revision, and **a live LogMate transfer contract for operational identifiers, tabular numerics, semantic geometry, conservative font selection and multilingual/runtime boundaries**.

Major unresolved gates remain: external broad QA/sanitizers; direct HarfBuzz trace; Firefox/Safari/native platform shaping; real HTTP/CDN/cache/service-worker font delivery; non-proportional production fallback calibration; production Korean and complex-script systems; vertical writing; three-master/multi-axis/CFF2 work; components/diacritics/family coherence; complete naming/style linking; hinting strategy; mixed-script line layout; and human reading/recognition evidence.

---

## Canonical evidence

Legacy:

- `research/type/001-type-as-system.md`
- `research/type/002-metrics-spacing-optical-rhythm.md`
- `research/type/003-stroke-contrast-bezier-optics.md`
- `research/type/005-numerals-punctuation-systems.md`
- `research/type/009-typography-as-information-architecture.md`

T-series:

- `T001-web-typography-fallback-metrics-reflow-transfer.md`
- `T002-raster-proof-redraw-cycle.md`
- `T003-minimal-font-renderer-matrix.md`
- `T004-native-numeral-punctuation-renderer-proof.md`
- `T005-latin-korean-mixed-script-fallback.md`
- `T006-production-outline-audit.md`
- `T007-variable-interpolation-source-compatibility.md`
- `T008-production-build-release-qa.md`
- `T009-webfont-subset-feature-contract.md`
- `T010-variable-webfont-axis-contract.md`
- `T011-layout-multiscript-release-contract.md`
- `T012-mark-mkmk-anchor-release-contract.md`
- `T013-normalization-sensitive-subset-contract.md`
- `T014-hangul-normalization-subset-contract.md`
- `T015-hangul-browser-canonical-cluster-transfer.md`
- `T016-webfont-loading-fallback-metric-contract.md`
- `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`

T016 reproducibility artifacts:

- `research/type/T016-webfont-loading-fallback-metric-contract.py`
- `research/type/T016-webfont-loading-fallback-metric-contract-results.json`

Generated experimental font binaries/screenshots remain runtime outputs, not product assets or source authority.

---

## Latest controlled block — T016 webfont loading / fallback metric contract

T016 was selected only after rechecking the top queue item. `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`, and Python `uharfbuzz` were unavailable. No external QA, sanitizer, or direct HarfBuzz PASS is claimed.

Chromium `144.0.7559.96`, Playwright, and fontTools were available. T015 had already demonstrated that structural package evidence does not automatically predict browser rendering, so T016 moved to the next executable production gap: **the actual downloadable-font lifecycle**.

### SOURCE

- CSS Fonts Level 4 defines font block/swap/failure periods and `font-display`; it explicitly notes that fallback metrics can create reflow and advises closer metric matching where appropriate.
- CSS Font Loading Level 3 defines `FontFaceSet.status`, `check()`, and `ready` for observing font availability/loading completion.
- CSS Fonts Level 5 defines `size-adjust` as a multiplier for glyph outlines and metrics used to harmonize font designs at the same nominal `font-size`.

### Controlled specimen

Mixed Latin/Hangul string:

`AB7C101 HL8301 99,999+59 가각 비행기록`

Synthetic deterministic WOFF2 pair:

- preferred: Latin `460u`, Hangul `420u`, space `300u`;
- fallback: exact `1.25×` corresponding metrics.

Fallback was available before measurement. Preferred face used `font-display: swap` and was requested through `@font-face`; Playwright intercepted the request.

Matrix:

1. unadjusted fallback + delayed successful preferred (`1000ms`);
2. unadjusted fallback + preferred request aborted;
3. fallback with `size-adjust:80%` + delayed successful preferred;
4. fallback with `size-adjust:80%` + preferred request aborted.

Probes at `32px`:

- nowrap width;
- 500px wrapping-row height;
- downstream marker position;
- `document.fonts.status`;
- primary/fallback `document.fonts.check()`.

### Failure A — unadjusted loading fallback changed product geometry

During preferred loading:

- primary check false;
- fallback check true;
- width `541.1719px`;
- row `76.7813px` high (two lines);
- downstream marker top `115.1719px`.

After preferred loaded:

- primary check true;
- width `440.0469px`;
- row `38.3906px` high (one line);
- marker top `76.7813px`.

The successful swap therefore changed nowrap width by about `101.125px`, changed a 500px row from two lines to one, and moved following content by about `38.3906px`.

### Failure B — failed preferred made fallback geometry persistent

When the preferred request was aborted:

- primary check remained false;
- width remained `541.1719px`;
- row remained `76.7813px`.

A failed webfont is therefore a stable typography/layout state, not merely a temporary loading artifact.

### Revision — proportional metric matching

With `size-adjust:80%` on the deliberately proportional fallback:

During loading:

- width `439.9531px`;
- row `38.3906px`;
- marker top `76.7813px`.

After preferred loaded:

- width `440.0469px`;
- row and marker unchanged.

Width delta was about `0.0938px`.

When the preferred failed, the adjusted fallback retained the same one-line geometry (`439.9531px`).

### Bounded assertion result

`12/12` experiment-local assertions were true.

This is **not** a Foundation PASS metric.

### SYNTHESIS

T016 adds:

`font artifact integrity → font request state → fallback selection/metrics → optional swap → rendered geometry → layout consequence`.

A web typography role may therefore have materially distinct states:

1. preferred loaded;
2. fallback visible while preferred loads;
3. fallback persistent because preferred failed.

A preferred-font screenshot validates only the first state.

T016 also establishes a narrow controlled mitigation result: when fallback metrics differ from preferred metrics by a known proportional factor, `size-adjust` can sharply reduce swap-driven geometry change.

### STUDIO JUDGMENT

- Treat font loading and font failure as typography QA states when downloadable fonts are used.
- Do not choose `font-display` only as a performance flag; it determines visible Type states and whether later swaps can alter layout.
- Metric matching is risk reduction, not proof of design equivalence. It does not normalize x-height, Hangul body, stroke mass, punctuation, shaping, or readability.
- Robust layout and Type-side metric calibration are complementary. If modest metric variation breaks the product, Layout may need semantic recomposition rather than ever-more-exact fallback tuning.
- Production decisions require exact preferred/fallback fonts, scripts, content, delivery path, `font-display`, and target browsers/devices.

### OPEN

- FontBakery/Fontspector/OTS broad QA and exception policy;
- direct HarfBuzz glyph/cluster tracing;
- real HTTP/CDN/cache/service-worker/preload behavior;
- cache-warm/cold comparison;
- `font-display: block`, `fallback`, `optional`;
- ascent/descent/line-gap override transfer;
- real non-proportional Latin/Hangul fallback pairs;
- production Korean corpus/line breaking;
- Firefox/Safari/DirectWrite/CoreText/Android/Skia/Flutter;
- actual zoom/text enlargement;
- page-level CLS/performance evidence;
- human reading/recognition/task evidence.

### Evidence level

**PRACTICE + CRITIQUE / deterministic synthetic WOFF2 pair + real Chromium `@font-face` request path via Playwright interception + delayed success + abort failure + FontFaceSet state checks + wrapping/downstream geometry + controlled `size-adjust` revision; 12/12 bounded assertions true.**

T016 is **not PASS**.

---

## Latest live-product transfer — T017 LogMate operational typography / semantic geometry

Canonical:

- `research/type/T017-logmate-operational-data-typography-semantic-geometry-transfer.md`

Transfer target:

- `yhappcom/logmate`, branch `design/design-studio-proposal`;
- current Opening Draft 01 user review and regional sample-route policy.

### Trigger

LogMate's rendered Opening route rows exposed a real product failure: proportional uppercase airport codes visually shift even though every code has three letters. Tabular figures stabilize durations but do not stabilize alphabetic identifier widths.

### Transfer contract

T017 establishes:

`information role → semantic geometry → alignment/anchor → type behavior → OpenType feature → runtime/fallback validation → product observation`.

Short form:

**Layout robustness → Type refinement.**

This does not move the problem out of Type. Type remains responsible for identifier legibility, metrics, figures, punctuation, line metrics, fallback and platform behavior; Layout owns semantic tracks/anchors and responsive recomposition.

### LogMate operational Type synthesis

The provisional product system is:

**proportional general UI + high-legibility operational identifiers + tabular comparison numerics + semantic column geometry + explicit fallback/runtime validation**.

Current project decisions:

- whole-product / whole-ledger monospace: **REJECT as default**;
- airport code: proportional identifier by default, protected by DEP/ARR semantic slots;
- time/duration/career totals/landing counts and comparison-centric ledger numeric columns: `tnum` candidate/default subject to production-font/runtime proof;
- `KE704`, `HL8301`, `B737-8` etc.: identifier roles, not automatically tabular merely because digits occur;
- `0/O`, `1/I/l`, `5/S`, `8/B`: mandatory candidate audit groups;
- Crew/Remark/Notes: proportional + multilingual/Unicode-safe fallback;
- regional sample substitution must not require per-airport spacing hacks;
- Draft 02 may proceed structurally, but final typography lock remains blocked until candidate/platform audit.

### Evidence classification

- **TRANSFER VALIDATION:** T004/T005/T016 + Layout L004 are applied to an actual aviation-logbook product.
- **SYNTHESIS:** operational identifier and numeric roles are separated instead of using one generic “technical data” style.
- **STUDIO JUDGMENT:** prefer mature, conservative families and one-family solutions; introduce a mono companion or bespoke font only after controlled evidence shows a material unresolved need.
- **OPEN:** final family, airport-code measured width variance, Flutter/Android/iOS/PWA rendering, exact fallback stack, enlarged-text stress and human recognition evidence.

### Current transfer verdict

T017's structural/type-role contract is usable for Draft 02, but the full LogMate Type Transfer Sprint is not finished.

**NOT READY — BLOCKING TYPE ISSUE EXISTS**

Blocking issue: a mature-font candidate audit using the fixed LogMate corpus has not selected the provisional primary family or verified exact identifier/numeric behavior in Flutter and target platform conditions.

This blocks final typography lock, not Draft 02 structural implementation.

---

## Foundation module status

| Module | Status | Remaining gate |
| --- | --- | --- |
| Type anatomy / metrics | PRACTICE / CRITIQUE | broader family/role and target-platform validation |
| Stroke / contrast / construction | PRACTICE / CRITIQUE | broader coherent family extension and role transfer |
| Bézier / outline discipline | PRACTICE / CRITIQUE | complex curves/components/diacritics and family proof |
| Multi-master / interpolation | PRACTICE / CRITIQUE | three-master/multi-axis/CFF2/components/variable anchors |
| Optical correction | PRACTICE / CRITIQUE | broader family/axis/platform intended-size proof |
| Rasterization / rendering | PRACTICE / CRITIQUE | Chromium bounded evidence exists; CoreText/DirectWrite/Skia/Firefox/Safari/device + hinting strategy open |
| Spacing / kerning / GPOS | PRACTICE / CRITIQUE | broader classes/complex shaping/cross-browser proof open |
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence; T017 adds direct LogMate role transfer |
| Typography as information architecture | CRITIQUE | T017 adds live-product role/geometry transfer; production reflow/localization/enlarged-text transfer remains open |
| Web fallback / metric transfer | **PRACTICE / CRITIQUE** | T016 adds delayed/failed downloadable-font geometry + proportional metric-matching proof; real delivery/cache/cross-browser/zoom open |
| Mixed-script / fallback / normalization | **PRACTICE / CRITIQUE** | T005 + T011–T017 cover structural and project-transfer boundaries; production Korean/line boxes/cross-platform/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T016 span source→interpolation→binary→package→browser shaping/loading states; external broad QA and production target integration open |

---

## Peer evidence currently affecting Type

### Color

C009's retained conclusion is still relevant: fixed semantic Color does not normalize actual Type rendering. T017 also explicitly refuses to infer cockpit/night legibility from typography alone; physical/device/human low-light validation remains separate.

### Layout / Interaction

L003 showed browser font selection can cross wrap thresholds and standalone font measurements are not production geometry proof. T016 confirmed that through downloadable-font states. L004 additionally showed that browser `tnum` can improve numeric alignment while increasing intrinsic column width. T017 **transfers and extends** these findings into LogMate route and ledger geometry.

### Web Design

Web is now Stage 1 PASS through W009. T017 retains Web/PWA as a later runtime transfer layer for exact font delivery/fallback, responsive ledger behavior and enlarged-text stress; no PWA production PASS is inferred.

---

## Active next queue

1. **T018 — LogMate conservative font candidate audit:** compare approximately 3–5 mature families using the fixed airport/flight/aircraft/registration/time/total/ambiguity corpus; measure airport-code width behavior, inspect identifier distinction, verify `tnum`/punctuation, render Opening + representative View Logbook, and choose one provisional baseline with explicit reject reasons.
2. Transfer the selected LogMate candidate into executable **Flutter/Android** conditions first where available; keep iOS/CoreText and Web/PWA parity OPEN until executable evidence exists.
3. **External broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
4. Transfer T016 to real non-proportional Latin/Hangul font pairs and measure whether `size-adjust` plus ascent/descent/line-gap overrides reduce layout shifts without unacceptable script mismatch.
5. Direct HarfBuzz glyph/cluster trace and cross-browser/platform replication: Firefox/Safari/Windows/macOS/Android/Flutter.
6. Production Korean transfer using a real Korean font and larger corpus: conjoining Jamo, fallback, line breaking and mixed-script line boxes.
7. Real HTTP/CDN/cache/preload/service-worker plus `font-display` mode transfer through Web/live-product work.
8. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
9. Broaden variable-family compatibility and Type→Layout regression against exact shipped artifacts.
10. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

T017 establishes no Night/cockpit luminance result. Keep physical low-light/device/human validation separate from Type role/geometry decisions.

### Layout / Interaction

T017 transfers L004 into LogMate: protect semantic DEP/arrow/ARR/time and ledger tracks independently of proportional identifier ink width, and size numeric tracks only after the approved numeric feature/format is active. Do not convert the whole ledger to fixed-width type merely to stabilize columns.

### Web Design

If LogMate PWA uses downloadable fonts, reproduce T016's preferred-loaded / loading-fallback / failed-fallback states with the final family and apply T017's same operational role semantics under responsive/enlarged-text conditions.

### LogMate UI / product team

Draft 02 may proceed with semantic route columns and separate UI / identifier / numeric Type roles. Final family, airport-code exact weight/tracking, mono companion and slashed-zero decisions remain OPEN until T018.

## Handoff rule

Answer peer requests with canonical Type evidence or new investigation as appropriate. Do not silently replace peer ownership or edit peer canonical files without authorization.

---

## Latest checkpoint

- T002: raster failure→redraw.
- T003: compiled TrueType renderer matrix.
- T004: research numeral/punctuation + tabular proof.
- T005: Latin/Korean fallback transfer.
- T006: production outline audit + CFF/TTF transfer.
- T007: two-master interpolation compatibility/adversarial correspondence.
- T008: generated-variable-font release QA.
- T009: static WOFF2/subset `tnum` semantic contract.
- T010: variable WOFF2/subset axis-semantic contract.
- T011: `kern` + language-bound `locl` + multi-script cmap + line-metric package contract.
- T012: `mark`/`mkmk` + exact anchor-chain package contract.
- T013: Latin NFC/NFD normalization-sensitive subset closure.
- T014: Hangul NFC/NFD structural package transfer + deterministic rebuild proof.
- T015: bounded Chromium canonical-equivalent Hangul cluster transfer.
- T016: delayed/failed downloadable-font lifecycle; unadjusted swap changed mixed-script width by ~101.125px and a 500px row 2→1 lines; proportional `size-adjust:80%` reduced width delta to ~0.0938px with stable row/downstream geometry; 12/12 bounded assertions true.
- **T017: LogMate live-product transfer — semantic route/ledger geometry, operational identifier vs tabular-numeric roles, conservative font policy, multilingual/runtime boundaries, and explicit Draft 02 handoff.**
- Next Type study ID: `T018`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
