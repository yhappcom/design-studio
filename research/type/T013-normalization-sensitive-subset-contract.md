# T013 — Normalization-sensitive subset contract

Status: **PRACTICE + CRITIQUE / NOT PASS**  
Date: 2026-09-15  
Primary question: can a parseable WOFF2 subset preserve the intended combining-mark behavior for one Unicode normalization form while failing the canonically equivalent form?

## Why this block

The highest-priority queue item remains external broad QA / sanitizer integration. At the start of this block `fontbakery`, `fontspector`, `ots-sanitize`, and `hb-shape` were still unavailable in the execution environment, so no external-QA or shaping PASS is claimed.

The next executable high-value gap from T012 was the product text-normalization boundary. T012 showed that cmap survival and zero-width marks do not certify attachment semantics. T013 asks a different release question: **what if the product, CMS, API, database, keyboard, or browser-facing content path supplies a canonically equivalent Unicode sequence in a different normalization form than the subset seed?**

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: T009–T012 package/subset semantic contracts, especially T012 `mark`/`mkmk` attachment-chain QA.
- Reusable finding: exact shipped-artifact QA must inspect semantic behavior rather than source glyph names or parseability alone.
- Extension: T013 keeps layout features intact and changes only the Unicode normalization coverage contract.

### Color
- Evidence checked: C009 Type→Color rendered-role transfer.
- Reusable finding: rendered ink can change while Color tokens remain fixed.
- Relevance here: a missing normalized-form mapping/attachment can alter or replace glyph output without any Color change. No Color threshold is inferred.

### Layout / Interaction
- Evidence checked: L003/L004 Type-driven wrap/numeric geometry transfer and current Layout status.
- Reusable finding: Type failures should be resolved before Layout compensates for their downstream geometry.
- Relevance here: a normalization/coverage failure can create fallback, `.notdef`, or different glyph geometry before layout measurement begins.

### Web Design
- Current status still has no substantive `W###` evidence.
- Implementation opportunity: real webfont subsetting must be tested against the normalization behavior of actual content sources, browser shaping, framework/CMS pipelines, and fallback stacks.

### Other / cross-cutting
- Unicode Standard Annex #15 (Unicode 17.0.0, Revision 57) defines normalization forms; NFC performs canonical decomposition followed by canonical composition, while NFD is canonical decomposition.
- OpenType `cmap` maps character codes to default glyph indices; codepoints not mapped by the font resolve to the missing-glyph path.

### Overlap decision
**EXTENSION + TRANSFER VALIDATION.** T013 deliberately extends T012 rather than repeating it. T012 asked whether attachment semantics survive packaging; T013 asks whether canonically equivalent content representations remain covered after subsetting.

## SOURCE

1. Unicode Standard Annex #15 defines canonical equivalence and the normalization forms. For the controlled string used here, Python Unicode data confirms:
   - NFD: `U+0041 U+0301 U+0307` (`A + COMBINING ACUTE + COMBINING DOT ABOVE`)
   - NFC: `U+00C1 U+0307` (`LATIN CAPITAL LETTER A WITH ACUTE + COMBINING DOT ABOVE`)
   These are canonically equivalent under NFC normalization.
2. OpenType `cmap` is the character-to-default-glyph mapping. A package can therefore be syntactically valid while lacking the codepoint required by a canonically equivalent input representation.
3. T012 already established structurally that `mark` and `mkmk` attachment contracts are separate from simple character coverage.

Primary references:
- Unicode Standard Annex #15, Unicode 17.0.0, Revision 57: https://www.unicode.org/reports/tr15/
- OpenType `cmap` table, OpenType 1.9.1: https://learn.microsoft.com/en-us/typography/opentype/spec/cmap

## Controlled font and package contract

A synthetic 1000-UPM TrueType source contains:

- `A` — U+0041, advance `600u`;
- `Aacute` — U+00C1, advance `600u`;
- `acutecomb` — U+0301, advance `0u`;
- `dotabovecomb` — U+0307, advance `0u`.

GPOS provides:

- `mark`: acute/dot mark class attaches to `A` at `[300,700]`;
- `mark`: acute/dot mark class attaches to `Aacute` at `[300,880]`;
- `mkmk`: dot attaches to acute through `[100,0] → [100,220]`.

Three feature-preserving subsets are generated and packaged as WOFF2:

1. **NFD-only seed** — subset text `U+0041 U+0301 U+0307`;
2. **NFC-only seed** — subset text `U+00C1 U+0307`;
3. **dual-normalization seed** — union of both representations.

No generated font binary is committed. The reproducibility script and measured JSON are canonical evidence.

## Measured result

Environment:

- Python `unicodedata`: Unicode `15.1.0`;
- fontTools `4.63.0`;
- external tools found: none of `fontbakery`, `fontspector`, `ots-sanitize`, `hb-shape`.

### Source WOFF2

The full source package contains all four codepoints and passes both bounded structural contracts:

- NFD coverage + zero advances + `acute → A` mark attachment + `dot → acute` mkmk attachment;
- NFC coverage + zero dot advance + `dot → Aacute` mark attachment.

### Failure A — NFD-only subset

The package is parseable WOFF2 and retains:

- U+0041, U+0301, U+0307;
- both zero-width combining marks;
- required NFD mark/mkmk attachment structures.

It **does not contain U+00C1**. Therefore:

- NFD contract: **PASS in this bounded structural audit**;
- canonically equivalent NFC contract: **FAIL**.

The resulting WOFF2 SHA-256 is `e1d54762761c710b6e2a5ca102716354d6d7805fcb953fd8c49195b6569dc53f`.

### Failure B — NFC-only subset

The package is parseable WOFF2 and retains:

- U+00C1 and U+0307;
- zero-width dot;
- `dot → Aacute` mark attachment.

It **does not contain U+0041 or U+0301**. Therefore:

- NFC contract: **PASS in this bounded structural audit**;
- canonically equivalent NFD contract: **FAIL**.

The resulting WOFF2 SHA-256 is `2e9793f2f0b5af988ced4c0409351f6498d4f67a092402b5d559341513071518`.

### Revision — dual-normalization subset

The dual subset contains U+0041, U+00C1, U+0301 and U+0307 and preserves both structural attachment paths.

- NFD contract: **PASS in this bounded structural audit**;
- NFC contract: **PASS in this bounded structural audit**.

The resulting WOFF2 SHA-256 is `d23fe5c3a84dc2b320520e6c48a269fa6eabc9a732963ab5819bfbf307833795`.

The measured JSON records all cmap entries, post-subset glyph names, anchors, package hashes, package sizes and derived assertions.

## SYNTHESIS

The controlled result supports:

`canonical text equivalence ≠ identical codepoint sequence ≠ identical subset closure`.

Combined with T012:

`character closure ≠ normalization-form closure ≠ metric identity ≠ feature binding ≠ anchor identity ≠ complete attachment chain ≠ shaping/rendering integration`.

A font package may be parseable, retain all layout features relevant to the representation it was seeded with, and still fail when canonically equivalent text arrives in another normalization form.

This is **not** evidence that every product must ship duplicate NFC+NFD coverage. It is evidence that the normalization boundary must be explicit.

## STUDIO JUDGMENT

For subsetted fonts used with combining marks or precomposed/decomposed alternatives:

1. define where text normalization occurs — ingestion, storage, server, build, client, rendering boundary, or nowhere;
2. identify the normalization forms actually allowed to reach shaping;
3. seed/subset against that real content contract rather than an assumed string representation;
4. if the pipeline does not guarantee one form, regression-test canonically equivalent forms that matter to supported languages/content;
5. verify required `cmap` coverage and OpenType attachment/substitution behavior in the **exact shipped package**;
6. keep structural package QA separate from HarfBuzz/browser/platform shaping and fallback validation;
7. do not treat a successful WOFF2 parse or one-form fixture as universal language support.

For a tightly controlled pipeline that guarantees normalized NFC before shaping, requiring NFD closure may be unnecessary package weight. Conversely, a pipeline that accepts unnormalized/user-generated text should not assume NFC-only subset fixtures represent all runtime input.

## Failure conditions this study adds

A release should fail the studio semantic gate when any required runtime representation can reach shaping but the shipped package lacks one or more of:

- required codepoint coverage for that representation;
- required zero/nonzero advances;
- required script/langsys feature binding;
- required mark/anchor attachment path;
- expected fallback policy when coverage is intentionally external.

## OPEN

- HarfBuzz/browser shaping of NFC/NFD exact artifacts;
- browser/font-fallback behavior when only one normalized representation is covered;
- canonical combining-class reorder stress beyond this simple sequence;
- Hangul decomposition/composition and Korean production relevance;
- Arabic/Indic normalization and shaping interactions;
- CMS/database/API/framework normalization behavior in real products;
- normalization of filenames/user identifiers/search versus display text — separate product concerns;
- external FontBakery/Fontspector/OTS QA;
- human-visible failure/reading evidence.

## Evidence level

**PRACTICE + CRITIQUE / synthetic TrueType source + feature-preserving subsets + WOFF2 packaging + Unicode NFC/NFD transformation + structural cmap/GPOS audit + two adversarial one-form subsets + dual-form revision.**

No external sanitizer, shaping engine, browser, platform, device or human PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS

### Color
- Useful finding: normalization/subset mismatch can alter or remove rendered glyphs while semantic Color values remain unchanged.
- Transfer note: extends C009's warning that Color cannot normalize Type/rendering failures.
- Scope limit: no Color contrast/salience threshold is inferred.

### Layout / Interaction
- Useful finding: confirm required normalization-form coverage and attachment semantics before measuring localized wrap/density/geometry.
- Transfer note: extends L003's Type→Layout dependency from fallback metrics into Unicode representation/package closure.
- Scope limit: T013 does not define responsive/layout policy.

### Web Design
- Useful finding: subset fixtures must match the actual normalization contract of CMS/API/database/client input, not merely the source text used during the build.
- Validation consequence: test exact WOFF2 with NFC/NFD cases that can really reach the browser, then inspect browser shaping/fallback/zoom/localization behavior.
- Scope limit: no browser PASS is claimed.

## Reproducibility

Run:

```bash
python T013-normalization-sensitive-subset-contract.py
```

The script emits `T013-normalization-sensitive-subset-contract-results.json`. Generated TTF/WOFF2 binaries are temporary local evidence only and are intentionally not committed.
