# T016 — Webfont Loading, Fallback Metrics, and Layout Stability Contract

Status: **PRACTICE + CRITIQUE / TYPE→WEB/LAYOUT TRANSFER VALIDATION — controlled Chromium evidence established; cross-browser/device/cache/human evidence remains OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Reproducibility:

- `research/type/T016-webfont-loading-fallback-metric-contract.py`
- `research/type/T016-webfont-loading-fallback-metric-contract-results.json`

## Research question

When a downloadable webfont is delayed or fails, how much can fallback metrics alter rendered geometry before/without the preferred face, and can a deliberately metric-matched fallback reduce that layout instability without claiming that the fallback and preferred designs are visually equivalent?

This study was selected after rechecking the nominal top queue item, external broad QA/sanitizer integration. `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`, and Python `uharfbuzz` were still unavailable in the execution environment. No external validator, sanitizer, or direct HarfBuzz PASS is claimed.

T015 had already shown that structural font evidence does not automatically predict Chromium output. The next highest-value executable gap was therefore real browser font-loading state: delayed `@font-face`, fallback rendering, successful swap, load failure, and metric-harmonized fallback.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:

- `progress/TYPE_STATUS.md` through T015;
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`;
- `research/type/T005-latin-korean-mixed-script-fallback.md`;
- `research/type/T009-webfont-subset-feature-contract.md`;
- `research/type/T015-hangul-browser-canonical-cluster-transfer.md`.

Reusable findings:

- loading fallback, script fallback, and package coverage are distinct states;
- exact metrics can alter geometry and wrapping;
- browser/rendering transfer is a separate evidence gate from font-table inspection;
- T015 reinforces that browser behavior must be measured rather than inferred only from binary structure.

Overlap decision:

- **EXTENSION + TRANSFER VALIDATION**. T016 does not repeat T015 shaping. It moves from embedded/exact artifact rendering to delayed downloadable-font lifecycle and fallback metric effects.

### Color

Evidence checked:

- `progress/COLOR_STATUS.md`, especially the retained C009 Type→Color transfer conclusion summarized there.

Reusable finding:

- rendered text appearance depends on actual Type state, not semantic Color tokens alone.

Transfer opportunity:

- a loading-state fallback can change glyph mass/geometry while Color tokens remain fixed. Color evaluation should therefore pin font-loading state when text appearance is material.

No Color contrast threshold or perceptual PASS is claimed.

### Layout / Interaction

Evidence checked:

- `progress/LAYOUT_STATUS.md`;
- `research/layout/L003-type-fallback-density-reflow-transfer.md`.

Reusable finding:

- L003 already demonstrated that valid font/fallback differences can cross wrap thresholds and that browser geometry must be measured in the actual layout stack.

T016 transfer:

- L003 used available font stacks without real downloadable-font lifecycle. T016 independently adds a delayed preferred-face transition and proves that the same surface can change row count and downstream position during `font-display: swap`.

### Web Design

Evidence checked:

- `progress/WEB_STATUS.md` through W001;
- W001's browser-native principle that final presentation is negotiated with browser/runtime conditions and should preserve relationships rather than assume one immutable rendering state.

Implementation/application opportunity:

- Web should transfer T016 into production `@font-face` delivery, actual HTTP/cache/service-worker/CDN behavior, real zoom, target browsers/devices, and page-level CLS/performance measurement.

T016 remains Type-owned evidence about font loading and metrics, not a Web Design production PASS.

### Other / cross-cutting

Authoritative sources checked:

- W3C CSS Fonts Module Level 4, especially the font display timeline, `@font-face`, `font-display`, and fallback guidance: https://www.w3.org/TR/css-fonts-4/
- W3C CSS Fonts Module Level 5, `size-adjust` and font metrics override model: https://www.w3.org/TR/css-fonts-5/
- W3C CSS Font Loading Module Level 3, `FontFaceSet.status`, `check()`, and `ready`: https://www.w3.org/TR/css-font-loading/

### Overlap decision

**EXTENSION + INDEPENDENT BROWSER TRANSFER VALIDATION.**

The useful new evidence is not another statement that fallback metrics differ. It is the measured transition across actual CSS font loading states, including a controlled mitigation and a failed-primary condition.

---

## SOURCE

### CSS font display timeline

CSS Fonts Level 4 defines three periods for downloadable fonts: block, swap, and failure. During applicable fallback periods, the user agent renders with a fallback face; if the desired face becomes available within a permitted swap period it can replace the fallback. The specification explicitly advises metric-compatible fallback choices to reduce large reflows.

`font-display: swap` is defined with an extremely short block period and an infinite swap period: content may appear in fallback and later rerender with the desired face.

### Font loading observability

CSS Font Loading Level 3 defines `FontFaceSet.status` as `loading`/`loaded`, `check()` as an availability check for matched fonts, and `ready` as a promise representing completion of font loading/layout work for the current set.

### Metric harmonization

CSS Fonts Level 5 defines `size-adjust` as a glyph-size multiplier applied to outlines and metrics while leaving computed CSS `font-size` unchanged. It exists specifically to help harmonize fonts used at the same nominal size. CSS Fonts also defines ascent/descent/line-gap overrides for line metrics.

These mechanisms do not assert visual-design equivalence between fonts; they alter metric/rendering scale behavior.

---

## Controlled specimen and method

### Environment

- Chromium `144.0.7559.96`;
- Linux headless browser;
- Playwright;
- Python `3.13.5`;
- fontTools `4.63.0`.

No Firefox, Safari/WebKit, CoreText, DirectWrite, Android/Skia, Flutter, or physical device is included.

### Synthetic fonts

Two deterministic 1000-UPM WOFF2 research fonts were generated from the same mixed Latin/Hangul character inventory.

Specimen:

`AB7C101 HL8301 99,999+59 가각 비행기록`

Preferred face:

- Latin-like glyph advances: `460u`;
- Hangul glyph advances: `420u`;
- space: `300u`.

Fallback face:

- every corresponding metric is exactly `1.25×` the preferred face.

The proportional construction is deliberate: it creates a controlled case in which `size-adjust:80%` should nearly neutralize the aggregate metric difference. This is a laboratory control, not a claim that real font pairs are proportional.

### Browser loading control

The fallback WOFF2 is embedded and settled before measurement. The preferred face is declared through:

```css
@font-face {
  font-family: T016Primary;
  src: url(https://font.test/primary.woff2) format("woff2");
  font-display: swap;
}
```

Playwright intercepts the font URL.

Success case:

- preferred response delayed by `1000ms`;
- first loading-state sample at `250ms` after applying the preferred-family class;
- final sample after `document.fonts.ready`.

Failure case:

- preferred request aborted;
- final sample after the font set settles.

This exercises Chromium's downloadable-font request/loading path, but the response is Playwright-intercepted rather than a production HTTP/CDN/cache path.

### Geometry probes

At `32px` type:

- nowrap specimen width;
- a `500px` wrapping row height;
- the top position of a marker immediately below the row;
- `document.fonts.status`;
- `document.fonts.check()` for primary/fallback.

Four cases were tested:

1. unadjusted fallback + delayed successful primary;
2. unadjusted fallback + failed primary;
3. `size-adjust:80%` fallback + delayed successful primary;
4. `size-adjust:80%` fallback + failed primary.

---

## Results

### A. Unadjusted delayed fallback produced a real layout transition

During preferred-face loading:

- `document.fonts.status = loading`;
- primary `check() = false`;
- fallback `check() = true`;
- nowrap width = `541.1719px`;
- 500px row height = `76.7813px` (two lines);
- marker top = `115.1719px`.

After preferred face loaded:

- primary `check() = true`;
- nowrap width = `440.0469px`;
- row height = `38.3906px` (one line);
- marker top = `76.7813px`.

Therefore the successful webfont swap changed the nowrap width by approximately `101.125px`, changed the row from two lines to one, and moved subsequent content upward by approximately `38.3906px` in this controlled specimen.

This is direct browser evidence that font loading state can be a layout state.

### B. Failed primary preserved the fallback geometry

When the preferred request was aborted:

- the font set settled;
- primary `check() = false`;
- fallback remained available;
- nowrap width remained `541.1719px`;
- row remained `76.7813px` high.

A failed primary is therefore not merely a transient loading state. The fallback geometry can become the stable product geometry for that session/runtime condition.

### C. Metric-matched fallback removed the controlled wrap transition

With the synthetic fallback declared at `size-adjust:80%`:

During loading:

- nowrap width = `439.9531px`;
- row height = `38.3906px`;
- marker top = `76.7813px`.

After preferred load:

- nowrap width = `440.0469px`;
- row height = `38.3906px`;
- marker top = `76.7813px`.

Width delta was approximately `0.0938px`; the line count and downstream marker position did not change.

### D. Metric-matched fallback also stabilized the failed-primary geometry

With the preferred face aborted and `size-adjust:80%` fallback active:

- primary `check() = false`;
- nowrap width = `439.9531px`;
- row height = `38.3906px`.

The failed-primary layout therefore remained almost identical to the successful preferred-face geometry in this proportional synthetic control.

### Bounded assertion result

`12/12` experiment-local assertions were true.

This count is **not** a Foundation PASS metric and does not establish production suitability of `size-adjust` for arbitrary font pairs.

Artifact hashes:

- preferred WOFF2 SHA-256: `1410770fe3468fab8a958c3f1c3af5ee7fa7dfb35adf5308a2fa5168329b5e9c`;
- fallback WOFF2 SHA-256: `cbe9f73f3ac9aca02e466d7b923cc1945d1ea49df7fb1afad7b9b27ba79e002c`.

---

## SYNTHESIS

T016 adds a new state dimension to the production chain:

`font artifact integrity → font request state → fallback selection/metrics → optional swap → rendered geometry → layout consequence`.

The same CSS typography role can therefore have at least three materially different geometry states:

1. preferred font loaded;
2. preferred font still loading and fallback visible;
3. preferred font failed and fallback persistent.

A preferred-font screenshot validates only state 1.

T016 also supports a narrower conclusion about metric matching:

> When fallback and preferred metrics differ by a known approximately proportional factor, a fallback metric adjustment can materially reduce swap-driven geometry changes.

It does **not** establish that one global scale factor can align real mixed-script font pairs. Real families may differ independently in Latin width, Hangul body scale, punctuation, numerals, vertical metrics, kerning, OpenType shaping, and raster mass.

---

## STUDIO JUDGMENT

### 1. Treat font loading/failure as a typography QA state

For web products using downloadable fonts, approve typography/layout against at least:

- preferred loaded;
- fallback while loading when the selected `font-display` policy can expose it;
- persistent fallback after load failure.

### 2. Do not choose `font-display` only as a performance flag

`font-display` changes what the user can see during font acquisition and whether later substitution can occur. It therefore changes typography and layout behavior, not only network performance.

### 3. Metric matching is risk reduction, not font-design equivalence

`size-adjust` and metric overrides can reduce geometry discontinuity, but they do not make x-height, Hangul body, stroke mass, spacing rhythm, punctuation, OpenType behavior, or readability equivalent.

### 4. Prefer robust layout before perfect fallback calibration

If a surface catastrophically fails from a modest metric difference, Layout should first consider whether its spatial relationship is too brittle. T016 complements L003 rather than replacing it: robust recomposition and Type-side metric matching are separate tools.

### 5. Exact project evidence is required

Production decisions should use the actual preferred font, actual fallback stack, actual scripts/content, actual `font-display` policy, actual browser/device targets, and real delivery path.

---

## Failure modes exposed

Reject or rework a release assumption when:

- only the fully loaded preferred font is screenshot-tested;
- fallback is considered a purely cosmetic state even though metrics can change wrapping;
- `font-display: swap` is adopted without testing post-swap reflow near critical thresholds;
- a load failure leaves persistent fallback geometry that the page never validates;
- one `size-adjust` factor is assumed to solve Latin, Hangul, numerals, punctuation, vertical metrics, and shaping without direct measurements;
- metric matching is used to excuse an intrinsically inappropriate fallback design;
- Layout shrinks or clips text solely to hide a font-loading transition;
- `document.fonts.ready` or `check()` is mistaken for visual/readability quality evidence.

---

## OPEN

- FontBakery/Fontspector/OTS broad QA and exception policy;
- direct HarfBuzz glyph/cluster tracing;
- real HTTP/CDN/cache/service-worker/preload behavior;
- cache-warm versus cache-cold sessions;
- `font-display: block`, `fallback`, and `optional` timing/behavior transfer;
- CSS metric overrides beyond the proportional `size-adjust` control;
- real non-proportional Latin/Hangul fallback pairs;
- production Korean fonts and larger mixed-script corpus;
- Firefox and Safari/WebKit;
- Windows DirectWrite/Edge, macOS/iOS CoreText, Android/Skia/Flutter;
- real browser zoom and text enlargement;
- page-level CLS/performance observation;
- human reading/recognition and task evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

Useful finding:

- font loading/failure can switch the actual rendered face and geometry while semantic Color values remain unchanged.

Transfer note:

- C009's Type-dependent rendering principle gains a lifecycle dimension: pin loaded/loading/failed font state when text-rendering appearance is under review.

Scope limit:

- T016 establishes no Color contrast or perceptual threshold.

### Layout / Interaction

Useful finding:

- L003's fallback-sensitive wrap risk now has an actual downloadable-font lifecycle reproduction: `541.1719px → 440.0469px` caused a controlled 2-line→1-line change and `38.3906px` downstream movement.

Transfer note:

- this **confirms and extends** L003. Layout should validate both robust recomposition and font-loading states rather than tune only the preferred face.

Scope limit:

- synthetic fonts and one Chromium environment; no production breakpoint is inferred.

### Web Design

Useful finding:

- preferred-loaded, visible-loading-fallback, and persistent-failed-fallback are separate browser typography states.

Web application/validation consequence:

- reproduce using actual `@font-face` files, chosen `font-display`, CDN/cache/preload/service-worker behavior, production content, actual zoom, target browsers/devices, and page-level layout-shift/performance tooling.

Transfer note:

- T016 supplies a bounded Type-owned browser contract for future W### integration. It is not Web production validation.

---

## Evidence level

**PRACTICE + CRITIQUE / deterministic synthetic WOFF2 pair + real Chromium `@font-face` request path via Playwright interception + delayed success + network abort + FontFaceSet state checks + wrapping/downstream geometry + controlled `size-adjust` mitigation; 12/12 bounded assertions true.**

T016 is **not PASS**.
