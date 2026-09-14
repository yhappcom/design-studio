# T014 — Hangul Normalization-Sensitive Subset Contract

Status: **PRACTICE + CRITIQUE / Hangul NFC↔NFD subset transfer + reproducible WOFF2 structural QA complete; HarfBuzz/browser/platform shaping remains OPEN**

## Why this study exists

T013 proved with a Latin combining-mark specimen that canonical Unicode equivalence does not guarantee identical codepoint or subset closure. T014 asks whether that conclusion transfers to **algorithmically decomposed Hangul syllables**, where a precomposed syllable and a sequence of conjoining Jamo are canonically equivalent but require different `cmap` coverage.

The originally queued external QA/sanitizer block could not be executed because `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` are unavailable in the current environment. No external QA or shaping PASS is claimed. The highest-value executable gap was therefore Korean normalization/package transfer.

Reproducibility artifacts:

- `T014-hangul-normalization-subset-contract.py`
- `T014-hangul-normalization-subset-contract-results.json`

Generated font binaries are experiment outputs only and are not committed product assets.

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: T005 mixed Latin/Korean fallback; T011–T013 package, layout-feature, mark-chain, and normalization contracts.
- Reusable finding: T013 established `canonical equivalence ≠ identical codepoint sequence ≠ identical subset closure`.
- Transfer opportunity: test that statement on Hangul's standardized algorithmic decomposition rather than assume the Latin diacritic specimen generalizes.
- Dependency: actual Hangul shaping and fallback still require HarfBuzz/browser/platform evidence.

### Color
- Evidence checked: C009 Type→Color transfer.
- Reusable finding: fixed Color tokens do not normalize fallback/rendering or spatial footprint.
- Transfer consequence: normalization-driven fallback or missing-glyph behavior must be resolved before a Color role is judged from final rendered text.
- Scope: T014 makes no contrast or Color threshold claim.

### Layout / Interaction
- Evidence checked: L003 mixed-script fallback/reflow transfer and current Layout status.
- Reusable finding: Korean fallback differences can cross real wrap thresholds; browser layout must use actual delivered font/content state.
- Transfer consequence: normalization form is now an additional Type prerequisite before localized width/reflow evidence is trusted.
- Scope: T014 does not claim browser width or line-breaking behavior.

### Web Design
- Evidence checked: current Web status; no substantive `W###` study exists.
- Implementation opportunity: validate exact shipped WOFF2 against real CMS/API/database normalization, browser font fallback, `@font-face`, zoom, OS, and device matrices.
- Scope: this study is not Web/browser PASS.

### Other / cross-cutting
- Unicode UAX #15 was checked for NFC/NFD and Hangul-specific canonical decomposition rules.
- OpenType `cmap` specification was checked for the character-code→default-glyph-index contract.

### Overlap decision
- **TRANSFER VALIDATION + ADVERSARIAL PACKAGE QA.**
- Reason: T013's Latin result is materially relevant but insufficient to certify Korean product behavior. T014 deliberately repeats the normalization method on Hangul and tests packaged WOFF2 closure.

---

## SOURCE

Unicode Standard Annex #15 defines NFC and NFD normalization. Full canonical decomposition uses decomposition mappings and special algorithmic rules for Hangul syllables.

OpenType `cmap` defines mappings from character codes to default glyph indices. A font can therefore be valid and parseable while lacking codepoints required by one runtime normalization representation.

Primary references:

- Unicode UAX #15: `https://www.unicode.org/reports/tr15/`
- OpenType `cmap`: `https://learn.microsoft.com/en-us/typography/opentype/spec/cmap`

---

## Controlled Hangul normalization cases

Python Unicode data version: `15.1.0`.

Two syllables were chosen to exercise both LV and LVT decomposition:

| Syllable | NFC | NFD |
| --- | --- | --- |
| `가` | `U+AC00` | `U+1100 U+1161` |
| `각` | `U+AC01` | `U+1100 U+1161 U+11A8` |

Both NFD sequences normalize back to their NFC syllables.

A synthetic 1000-UPM TrueType source contains exactly the relevant precomposed syllables and conjoining Jamo. Three feature-neutral subsets are generated and packaged as WOFF2:

1. `nfc_only` — U+AC00/U+AC01;
2. `nfd_only` — U+1100/U+1161/U+11A8;
3. `dual` — both representations.

The experiment audits parseability, resulting `cmap`, glyph closure, SHA-256, and independent rebuild identity. It does **not** claim actual Jamo composition/shaping quality because HarfBuzz/browser shaping was unavailable.

---

## Failure A — NFC-only package

`nfc_only.woff2` is parseable and contains:

- U+AC00 `가`;
- U+AC01 `각`.

It does **not** contain:

- U+1100;
- U+1161;
- U+11A8.

Therefore both selected syllables pass the bounded NFC coverage contract and fail the canonically equivalent NFD coverage contract.

SHA-256: `a13f632702b25230fe16164dc337b38a45349af7a59a711bad1b39cdf528e344`.

### Consequence

A product pipeline that subsets from normalized NFC fixture text can produce a valid package that does not structurally cover canonically equivalent decomposed Hangul arriving later.

---

## Failure B — NFD-only package

`nfd_only.woff2` is parseable and contains:

- U+1100 choseong kiyeok;
- U+1161 jungseong a;
- U+11A8 jongseong kiyeok.

It omits U+AC00 and U+AC01. Therefore both selected syllables pass the bounded NFD coverage contract and fail NFC coverage.

SHA-256: `fb9514bc55ec557217c2a1659c36c032a666d374b382c40f7ab6e3705c0edfac`.

### Consequence

The reverse assumption also fails: a Jamo-closure package does not automatically cover ordinary precomposed Hangul text.

---

## Revision — dual-normalization package

`dual.woff2` contains all five required codepoints:

- U+AC00;
- U+AC01;
- U+1100;
- U+1161;
- U+11A8.

It passes both bounded NFC and NFD structural-coverage contracts.

SHA-256: `769b9fa37bf8ad2a62d9063c9eba5708eca5c6de357fdbe20b7d0b36d82b0702`.

This is **not** a universal recommendation to duplicate every canonical representation in every production font. It demonstrates what is required when both forms are allowed to reach shaping.

---

## Reproducibility failure → revision

The first harness version produced correct closure results but different WOFF2 hashes on repeated runs. The changing value came from font timestamps, so it could not support a reproducible-package claim.

The revised harness fixes `head.created` and `head.modified`, disables timestamp recalculation, builds the three packages twice in independent directories, and compares hashes.

Final result:

- `nfc_only`: rebuild hash identical;
- `nfd_only`: rebuild hash identical;
- `dual`: rebuild hash identical;
- `all_rebuild_hashes_identical = true`.

### SYNTHESIS

Research harness reproducibility is itself part of evidence quality. A semantically correct font experiment should not quietly use nondeterministic binary outputs when SHA identity is part of the reported evidence.

---

## SYNTHESIS

T014 independently confirms T013's normalization principle for Hangul:

`canonical equivalence ≠ identical codepoint sequence ≠ identical font subset closure`.

It also sharpens the product chain:

`content normalization boundary → required codepoint representation → subset closure → shaping/fallback → layout/rendering → human/product result`.

For Hangul specifically, the boundary can separate precomposed syllable coverage from conjoining-Jamo coverage. A parseable WOFF2 can satisfy one side and fail the other.

---

## STUDIO JUDGMENT

Before approving a Korean production subset, define where normalization is guaranteed:

- content authoring/CMS;
- API/service boundary;
- database/storage;
- client application;
- immediately before shaping.

If the system guarantees NFC before shaping and that guarantee is tested operationally, a narrower NFC-oriented subset may be legitimate. If external/user/imported content can reach shaping as NFD, the shipped artifact must be tested against that runtime form or the pipeline must normalize it deliberately.

Do not infer actual Hangul visual equivalence from `cmap` alone. Conjoining-Jamo shaping, fallback-run behavior, line boxes, renderer/platform differences, and production font design remain separate gates.

---

## PROJECT READINESS TEST

Use T014 when a Korean app/web product:

- subsets fonts from observed text/corpus;
- accepts user-generated or imported Unicode text;
- moves text through macOS/iOS, web, backend, database, or third-party systems with uncertain normalization behavior;
- uses custom Korean webfonts with fallback;
- treats exact package size and coverage as release criteria.

Required project inputs:

1. actual text-source normalization behavior;
2. exact production font/subset toolchain;
3. exact shipped WOFF2/TTF/OTF;
4. supported Korean content classes;
5. fallback stack;
6. target browser/OS/app shaping engine.

Reject release evidence that only says “Korean glyphs are present” without specifying which runtime representation was tested.

---

## OPEN

- HarfBuzz shaping of the exact NFC/NFD/dual artifacts;
- browser behavior and fallback-run fragmentation when one representation is absent;
- production Korean font with real conjoining-Jamo design and shaping behavior;
- whole-Hangul-syllable/Jamo coverage strategy, not only `가/각`;
- compatibility Jamo and NFKC/NFKD policy where relevant;
- real CMS/API/database/platform normalization observation;
- CoreText/DirectWrite/Skia/Flutter/browser transfer;
- Korean line breaking and mixed-script line-box transfer;
- external FontBakery/Fontspector/OTS QA;
- human-visible failure evidence.

T014 is **not PASS**.

---

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Useful finding: Korean normalization mismatch can change glyph availability/fallback while semantic Color tokens remain unchanged.
- Transfer: evaluate Color-role robustness only after exact shipped artifact and runtime normalization/fallback state are pinned.
- Scope limit: no contrast/readability threshold is inferred.

### Layout / Interaction
- Useful finding: L003 Korean fallback/reflow testing gains an additional prerequisite — the normalization representation reaching shaping.
- Transfer: localized wrap/density regression should use exact shipped fonts and realistic NFC/NFD content states when the product does not enforce one form.
- Scope limit: T014 has no browser width or line-break evidence.

### Web Design
- Useful finding: an NFC-only webfont subset can be structurally valid yet miss canonically equivalent decomposed Hangul; the inverse also holds.
- Application consequence: verify actual content normalization and exact WOFF2 in target browsers with `@font-face`, fallback, zoom/DPR, OS/device, and network loading states.
- Scope limit: no Web PASS or shaping PASS.

## Evidence level

**PRACTICE + CRITIQUE / synthetic Hangul TrueType → three WOFF2 subset contracts + two adversarial one-form failures + dual-form revision + deterministic rebuild proof.**

No external sanitizer, HarfBuzz, browser/platform, production-font, or human PASS is claimed.