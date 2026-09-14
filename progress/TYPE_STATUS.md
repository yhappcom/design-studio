# Typography / Type Design Specialist Status

Operating state: **ACTIVE — RESEARCH MAY RESUME**  
Governance sync: 2026-09-15  
Primary path: `research/type/`  
Next new-study ID: `T017`

This file is maintained by the Typography / Type Design Specialist. The specialist must not update global `progress/STATUS.md` directly.

## Operational mission

Type research exists to improve real app, web and product decisions. Research volume is not the objective. Live-project output must translate evidence into project-specific guidance on font choice, hierarchy, metrics, spacing, numerals, localization, fallback, Unicode/text normalization boundaries, source/build quality, package/release integrity, OpenType behavior, variable axes, rendering, accessibility, implementation trade-offs, validation and failure conditions.

## Current level

Current curriculum stage: **Stage 1 — Foundation**  
Overall state: **PRACTICE / CRITIQUE**  
Foundation: **NOT PASSED**

The program now has controlled evidence across source construction, raster behavior, numerals/punctuation, mixed-script fallback, production outline QA, two-master interpolation, variable-font binary QA, static/variable WOFF2 subset semantics, `kern`/`locl` package contracts, `mark`/`mkmk` anchor-chain release QA, Unicode normalization-sensitive subset closure, Hangul NFC↔NFD structural package transfer, bounded Chromium canonical-equivalent Hangul cluster matching/render transfer, and **downloadable-webfont loading/failure/fallback geometry with a controlled metric-matching revision**.

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

T016 reproducibility artifacts:

- `research/type/T016-webfont-loading-fallback-metric-contract.py`
- `research/type/T016-webfont-loading-fallback-metric-contract-results.json`

Generated experimental font binaries/screenshots remain runtime outputs, not product assets or source authority.

---

## Latest completed block — T016 webfont loading / fallback metric contract

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
| Numerals / punctuation | PRACTICE / CRITIQUE | production figures, browser shaping, localization, human evidence |
| Typography as information architecture | CRITIQUE | production reflow/localization/enlarged-text transfer |
| Web fallback / metric transfer | **PRACTICE / CRITIQUE** | T016 adds delayed/failed downloadable-font geometry + proportional metric-matching proof; real delivery/cache/cross-browser/zoom open |
| Mixed-script / fallback / normalization | **PRACTICE / CRITIQUE** | T005 + T011–T016 cover structural and bounded Chromium transfer; production Korean/line boxes/cross-platform/human evidence open |
| Source/build/release pipeline | **PRACTICE / CRITIQUE** | T006–T016 span source→interpolation→binary→package→browser shaping/loading states; external broad QA and production target integration open |

---

## Peer evidence currently affecting Type

### Color

C009's retained conclusion is still relevant: fixed semantic Color does not normalize actual Type rendering. T016 adds a loading-state dimension — the rendered face/geometry can change while Color tokens remain unchanged.

### Layout / Interaction

L003 showed browser font selection can cross wrap thresholds and standalone font measurements are not production geometry proof. T016 **confirms and extends** that result with real downloadable-font state: the same controlled row changed two lines→one across a delayed swap.

### Web Design

W001 now exists at PRACTICE + CRITIQUE. Its browser-native model supports treating font loading/failure as runtime participation rather than assuming author-perfect pixels. T016 provides a concrete Type→Web transfer contract for future production font delivery/cache/zoom/browser testing.

---

## Active next queue

1. **T017 — external broad QA + sanitizer integration** when FontBakery/Fontspector/OTS or equivalent executables are available; keep universal/spec/vendor-policy checks separate from studio semantic assertions.
2. Transfer T016 to **real non-proportional Latin/Hangul font pairs** and measure whether `size-adjust` plus ascent/descent/line-gap overrides reduce layout shifts without creating unacceptable apparent-size/script mismatch.
3. Direct HarfBuzz glyph/cluster trace and cross-browser/platform replication: Firefox/Safari/Windows/macOS/Android/Flutter.
4. Production Korean transfer using a real Korean font and larger corpus: conjoining Jamo, fallback, line breaking and mixed-script line boxes.
5. Real HTTP/CDN/cache/preload/service-worker plus `font-display` mode transfer through Web/live-product work.
6. Extend attachment QA into ligature marks, multiple mark classes, cursive attachment and production complex scripts.
7. Study vertical-writing release semantics where project relevance justifies it.
8. Broaden variable-family compatibility: three masters, multiple axes, richer `avar`, components/diacritics, variable anchors, overlap strategy and CFF2.
9. Type→Layout regression against exact shipped artifacts.
10. Broader family coherence and human reading/recognition evidence after target rendering/layout stabilizes.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

Pin font loading state (`preferred loaded` / `fallback visible` / `preferred failed`) when Type materially affects rendered Color judgments. T016 establishes no Color threshold.

### Layout / Interaction

T016 confirms L003 with a downloadable-font lifecycle: `541.1719px → 440.0469px` changed a 500px controlled row from two lines to one and moved following content `38.3906px`. Validate loading/failure states and robust recomposition; do not tune only the preferred-loaded state.

### Web Design

Reproduce T016 using production `@font-face` delivery, selected `font-display`, real CDN/cache/preload/service-worker behavior, actual content, zoom, target browsers/devices, and page-level layout-shift/performance tooling. Playwright-intercepted Chromium evidence is not Web production PASS.

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
- **T016: delayed/failed downloadable-font lifecycle; unadjusted swap changed mixed-script width by ~101.125px and a 500px row 2→1 lines; proportional `size-adjust:80%` reduced width delta to ~0.0938px with stable row/downstream geometry; 12/12 bounded assertions true.**
- Next Type study ID: `T017`.
- Overall Type state remains **Stage 1 / PRACTICE + CRITIQUE / Foundation NOT PASSED**.
