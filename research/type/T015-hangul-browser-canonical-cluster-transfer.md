# T015 — Hangul Canonical-Equivalent Cluster Matching in Chromium

Status: **PRACTICE + CRITIQUE / T014 browser-transfer validation complete in bounded Chromium; cross-browser/platform/HarfBuzz CLI/external sanitizer evidence remains OPEN**

## Why this study exists

T014 established a structural release fact: an NFC-only Hangul package and an NFD-only Hangul package have different `cmap` closure even when their text is canonically equivalent. T014 explicitly left browser shaping open.

T015 tests the highest-value unresolved consequence: **does missing exact input codepoint coverage necessarily produce a browser fallback/render failure, or can the browser's cluster-matching/shaping stack resolve canonically equivalent Hangul representations?**

The queued external broad-QA block was checked first. `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`, and Python `uharfbuzz` were unavailable in the execution environment. No external sanitizer or direct HarfBuzz PASS is claimed. Chromium + Playwright were available, so the next queued shaping/browser transfer could be executed.

Canonical reproducibility artifacts:

- `research/type/T015-hangul-browser-canonical-cluster-transfer.py`
- `research/type/T015-hangul-browser-canonical-cluster-transfer-results.json`

Generated TTF/WOFF2 binaries and PNG screenshots are runtime outputs only and are not product assets or canonical source authority.

---

## RELATED DOMAIN CHECK

### Typography / Type

- Evidence checked: T005 mixed Latin/Korean fallback; T013 normalization-sensitive subset contract; T014 Hangul NFC/NFD structural package contract; T011–T012 package/GPOS evidence through the current Type status.
- Reusable finding: T014 proves `canonical equivalence ≠ identical codepoint sequence ≠ identical cmap/subset closure`, but explicitly does **not** prove browser failure.
- Replication / challenge / transfer opportunity: transfer the exact T014 question from structural package inspection into browser font matching and raster output.
- Dependency or overlap: this is a **TRANSFER VALIDATION + LIMITATION/REFINEMENT** of T014, not a replacement of T014's structural result.

### Color

- Evidence checked: `research/color/C009-type-rendering-color-contrast-transfer.md` and current Color status.
- Reusable finding: fixed Color tokens do not normalize Type/fallback/rendering state; C009 requires actual rendered Type conditions before Color robustness is inferred.
- Transfer opportunity: determine whether normalization-form differences actually change the rendered glyph/fallback state in Chromium before predicting a Color consequence.
- Scope: no Color contrast/readability threshold is inferred.

### Layout / Interaction

- Evidence checked: `research/layout/L003-type-fallback-density-reflow-transfer.md` and current Layout status.
- Reusable finding: actual browser font selection can move wrap/row-height thresholds, and font-table/standalone measurements are not browser-layout proof.
- Transfer opportunity: determine whether NFC/NFD Hangul representation creates different browser geometry under deliberately asymmetric font coverage.
- Scope: T015 measures bounded inline width and raster identity, not production line breaking or full layout behavior.

### Web Design

- Evidence checked: `progress/WEB_STATUS.md`; no substantive `W###` study exists at this checkpoint.
- Reusable finding: Web is the eventual owner of production `@font-face`, loading/failure, cross-browser/OS/device, zoom and page-system validation.
- Implementation/application opportunity: repeat T015 with the exact shipped product webfont, real content pipeline, network loading states, Safari/Firefox/Edge, browser zoom, and target devices.
- Scope: Chromium/Linux evidence is not Web PASS.

### Other / cross-cutting

- Unicode UAX #15 was checked for canonical NFC/NFD equivalence and Hangul algorithmic decomposition.
- CSS Fonts Module Level 4 was checked for character/cluster matching. It explicitly distinguishes exact character-map support from cluster matching and includes a rule for a multi-codepoint sequence canonically equivalent to a single character.

### Overlap decision

- **TRANSFER VALIDATION + ADVERSARIAL REVIEW + LIMITATION OF A PRIOR INFERENCE.**
- Why: T014's structural failure is real, but product decisions require knowing whether a target shaping/browser stack can bridge the representation difference. This is exactly the open gate T014 named.

---

## SOURCE

### Unicode normalization

Unicode UAX #15 defines NFC/NFD and algorithmic Hangul canonical decomposition/composition.

Primary reference:

- `https://www.unicode.org/reports/tr15/`

For the bounded string:

- NFC: `가각` → `U+AC00 U+AC01`
- NFD: `가각` → `U+1100 U+1161 U+1100 U+1161 U+11A8`

These strings are canonically equivalent.

### CSS Fonts cluster matching

CSS Fonts Module Level 4 states that ordinary font matching uses the font character map, but cluster matching is more specialized. For a multi-codepoint cluster, if the sequence is canonically equivalent to a single character and the font supports that character, the user agent can select that font for the sequence and use the canonically equivalent glyph. The specification also warns that font matching does not assume all text is normalized or denormalized and that authors must choose fonts appropriate to real content.

Primary reference:

- `https://www.w3.org/TR/css-fonts-4/` — sections 5.2–5.4, especially **Cluster matching**.

### SOURCE consequence

Exact `cmap` membership remains a valid binary/package fact, but **the input sequence's codepoints are not necessarily the final glyph-selection boundary in a browser**. Canonical-equivalent cluster matching and shaping can intervene.

---

## Controlled browser specimen

Environment:

- Chromium `144.0.7559.96` on Debian GNU/Linux 13;
- Playwright Python;
- fontTools `4.63.0`;
- Python Unicode data `15.1.0`;
- system fallback: `NanumGothic`;
- CSS sizes: `16px`, `40px`;
- DPR: `1`, `2`;
- no remote network font loading;
- generated fonts embedded as WOFF2 data URLs.

Three synthetic fonts deliberately separate structural coverage:

1. **NFC-only**: `U+AC00`, `U+AC01`; advances `420u`, `680u`.
2. **NFD-only**: `U+1100`, `U+1161`, `U+11A8`; advances `260u`, `310u`, `370u`.
3. **Dual**: both codepoint sets.

The advance systems are intentionally different. At 40px the two-syllable expected widths are:

- NFC path: `(420 + 680) / 1000 × 40 = 44px`;
- NFD/Jamo path: `(260 + 310 + 260 + 310 + 370) / 1000 × 40 = 60.4px`.

This makes it possible to distinguish which synthetic font path Chromium actually used rather than relying only on `getComputedStyle(font-family)`, which exposes the declared family list rather than per-glyph fallback attribution.

The harness also includes:

- mixed Latin + Hangul: `AB가각12` versus `AB가각12`;
- an unsupported control: NFD `간` = `U+1100 U+1161 U+11AB`, where the NFC-only font contains neither the Jamo sequence nor canonically equivalent `U+AC04`.

Each relevant pair is compared by DOM width and isolated PNG SHA-256/pixel equality.

---

## RESULT A — NFC-only font renders NFD identically

Despite the NFC-only font lacking `U+1100/U+1161/U+11A8` in its `cmap`, Chromium rendered the NFD input `가각` exactly like NFC `가각`.

At `40px`:

- NFC input width: `44px`;
- NFD input width: `44px`;
- expected NFC custom-font width: `44px`;
- isolated PNG hashes: identical;
- changed pixels: `0`.

The same equality held at `16px` and at DPR `1` and `2`.

### TRANSFER VALIDATION

T014's statement that the NFC-only WOFF2 **structurally lacks NFD Jamo codepoints remains correct**. What T015 rejects is the stronger inference:

> “Missing exact NFD Jamo cmap entries necessarily means canonically equivalent NFD text will fall back or render differently in Chromium.”

That inference is false in this bounded browser case.

### SYNTHESIS

`exact input codepoint coverage failure` does not automatically imply `browser rendering failure` when canonical-equivalent cluster matching/shaping can map the cluster to available glyphs.

---

## RESULT B — NFD-only font also rendered NFC identically in Chromium

The NFD-only font contains the three conjoining Jamo but omits `U+AC00/U+AC01`.

Chromium nevertheless rendered NFC `가각` identically to NFD `가각` in the bounded test.

At `40px`:

- NFD input width: `60.40625px`;
- NFC input width: `60.40625px`;
- expected Jamo custom-font width: `60.4px` before browser fractional layout;
- isolated PNG hashes: identical;
- changed pixels: `0`.

This held at 16/40px and DPR1/2.

### Important source/implementation distinction

CSS Fonts explicitly describes the decomposed-sequence → canonically equivalent single-character cluster case. T015's reverse NFC → NFD-only result is **observed Chromium implementation/shaping evidence**, not a universal claim that every browser/platform must decompose every precomposed character into a font's available components.

### STUDIO JUDGMENT

Do not turn one Chromium behavior into a package contract. Treat it as target-stack evidence that must be replicated on Safari/CoreText, Firefox, Windows/DirectWrite, Android/Skia/Flutter, and any product-specific runtime before relying on it.

---

## RESULT C — dual package chooses a stable equivalent result

The dual font includes both precomposed syllables and Jamo. NFC and NFD inputs rendered identically across all four size/DPR conditions.

At `40px`, both were `44px`, matching the precomposed-glyph advance path rather than the `60.4px` synthetic Jamo path.

This is bounded evidence that Chromium's shaping/font-matching stack resolves the canonically equivalent representations to the same result when both are available in this specimen.

It does **not** prove which internal shaping stage or exact engine rule produced that choice because `hb-shape`/`uharfbuzz` were unavailable and browser-internal glyph IDs were not independently extracted.

---

## RESULT D — mixed Latin + Hangul remains identical

`AB가각12` and `AB가각12` were tested with the NFC-only synthetic font first and `NanumGothic` fallback behind it.

Across 16/40px and DPR1/2:

- width equality: PASS in all bounded conditions;
- isolated raster equality: PASS in all bounded conditions.

### RELATED DOMAIN consequence

This directly limits a naive Type→Layout/Color prediction. A normalization-form difference does not itself prove changed geometry or rendered mass in a browser. The actual target font-matching/shaping stack must be measured.

---

## RESULT E — unsupported control proves the harness can observe a real coverage boundary

NFD `간` contains `U+11AB`, which is absent from the NFC-only font, and its canonical equivalent `U+AC04` is also absent.

At 40px the control rendered at approximately `37.609375px`, not the supported `가각` custom path's `44px`, and its raster hash differed.

This matters because the main equalities are not caused by a test harness that always normalizes every string before rendering. The browser handled the canonically supported clusters differently from a genuinely unsupported cluster.

---

## Validation matrix

Four conditions were tested:

| Condition | NFC-only NFC↔NFD | NFC-only mixed NFC↔NFD | NFD-only NFC↔NFD | Dual NFC↔NFD | Unsupported control differs |
| --- | --- | --- | --- | --- | --- |
| 16px / DPR1 | identical | identical | identical | identical | yes |
| 16px / DPR2 | identical | identical | identical | identical | yes |
| 40px / DPR1 | identical | identical | identical | identical | yes |
| 40px / DPR2 | identical | identical | identical | identical | yes |

The harness records **40/40 bounded assertions true**.

This count is an experiment-local assertion total, **not a Foundation PASS metric**.

---

## SYNTHESIS

T013–T015 now require a stricter distinction:

`canonical equivalence ≠ identical codepoint sequence ≠ identical cmap/subset closure`

but also:

`different cmap/subset closure ≠ automatic target-rendering divergence`.

The updated production chain is:

`content representation → binary cmap/feature closure → target cluster matching/shaping → fallback/glyph selection → rendered geometry/raster → layout/color consequence → human/product result`.

A structural package audit answers what the font contains. It does **not** fully answer what a browser will render for canonically equivalent text.

---

## STUDIO JUDGMENT

1. **Keep structural and runtime gates separate.** T014 is still valuable for package provenance and explicit closure. T015 shows that structural absence can be bridged by a target renderer.
2. **Do not over-package solely from fear.** A dual NFC+NFD subset should not be mandated universally if the actual target stack/content contract can be proven safely with a narrower package.
3. **Do not rely on browser rescue without replication.** Chromium/Linux evidence is insufficient to remove codepoints from a production cross-platform font when Safari/CoreText, Firefox, Android/Skia/Flutter, native app stacks, or imported data are targets.
4. **Normalize deliberately when the product owns the boundary.** Explicit NFC normalization may still be the simpler operational contract for storage/search/cache/subset consistency, even when a browser can render canonical equivalents.
5. **Use exact shipped artifacts.** Generic statements about “Hangul support” are weaker than tests using the exact package, content representation, fallback stack, browser/OS, and product geometry.

---

## PROJECT READINESS TEST

For a Korean app/web product, release evidence should answer separately:

- What normalization forms can reach shaping?
- What does the exact shipped font's `cmap` contain?
- What does the target browser/native shaping stack actually render for canonically equivalent forms?
- Does unsupported content trigger fallback, tofu, or a different metric path?
- Are mixed Latin/Korean width, wrap, and line-box results stable at real product sizes?
- Are the same results reproduced on every supported platform where the package decision depends on them?

A `cmap` audit alone is insufficient for runtime PASS; one Chromium rendering alone is insufficient for cross-platform package minimization.

---

## OPEN

- direct HarfBuzz CLI/`uharfbuzz` glyph-ID and cluster trace of the same synthetic binaries;
- Firefox and Safari/WebKit replication;
- Windows DirectWrite/Edge and macOS/iOS CoreText transfer;
- Android/Skia/Flutter transfer;
- production Korean font with real Jamo design, GSUB/GPOS and larger corpus;
- line breaking and line-box behavior under realistic Korean paragraphs;
- real `@font-face` network loading, `font-display`, cache and failure states;
- exact product content-pipeline normalization observations;
- compatibility Jamo/NFKC policy where relevant;
- external FontBakery/Fontspector/OTS QA;
- human-visible reading/recognition evidence.

T015 is **not PASS**.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color

- Useful finding/context: normalization-form mismatch does not automatically change rendered glyph/raster state in Chromium when canonical-equivalent cluster matching succeeds.
- Canonical section: T015 Results A–D.
- Confirmation / contradiction / transfer note: **limits** the earlier risk inference from T014/C009; Color should measure the actual rendered target state rather than assume fallback from `cmap` absence alone.
- Scope limit: Chromium/Linux only; no human readability or contrast threshold claim.

### Layout / Interaction

- Useful finding/context: L003's rule becomes stronger — actual browser font selection/shaping, not package coverage alone, determines geometry near wrap thresholds.
- Canonical section: T015 Results A–E and Synthesis.
- Confirmation / contradiction / transfer note: **confirms L003's browser-transfer principle** and limits the idea that NFC/NFD structural closure alone predicts width/reflow.
- Scope limit: no paragraph wrapping, Korean line-breaking, zoom, or production-layout PASS.

### Web Design

- Useful finding/context: CSS Fonts canonical-equivalent cluster matching can bridge deliberately asymmetric Hangul `cmap` coverage in Chromium, but this is implementation-dependent evidence.
- Web application / validation consequence: production Web should test exact shipped WOFF2 under real normalization, `@font-face`, fallback, loading/failure, browser/OS/device and zoom conditions before using subset minimization as a release decision.
- Confirmation / contradiction / transfer note: **direct browser transfer of T014; structural failure did not become rendered failure in this Chromium specimen.**
- Scope limit: no substantive W### evidence or cross-browser PASS.

---

## Evidence level

**PRACTICE + CRITIQUE / synthetic asymmetric Hangul WOFF2 fonts + Chromium 144 browser font matching/shaping + 16/40px × DPR1/2 + mixed-script transfer + unsupported control + DOM geometry + pixel-identity validation; 40/40 bounded assertions true.**

No external sanitizer, direct HarfBuzz trace, cross-browser/platform, production-font, line-layout, or human PASS is claimed.
