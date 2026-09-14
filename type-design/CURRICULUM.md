# Professional Type Design Curriculum

This curriculum treats type design as a system of form, spacing, metrics, language support, software behavior, and rendering—not as isolated letter drawing.

## Foundation

Study and exercise:

- character vs glyph vs font
- anatomy and alignment zones
- UPM and metrics
- sidebearings and advance widths
- stroke/contrast models
- curve construction and Bézier discipline
- overshoot and optical correction
- spacing before kerning
- proofing at intended size
- numeral and punctuation systems

Required exercises include repeated control strings, not just isolated glyphs. The learner must explain black/white rhythm and show why the spacing works.

## Intermediate

- coherent uppercase/lowercase/numeral families
- punctuation and symbols
- kerning classes and exceptions
- proportional vs tabular figures
- weight and width systems
- interpolation fundamentals
- diacritics and composite construction
- screen-size compensation
- mixed UI/readout/data use cases

## Advanced

- family planning and character-set strategy
- OpenType layout literacy: GSUB/GPOS/GDEF
- vertical metrics and cross-platform behavior
- optical-size thinking
- variable-font architecture
- interpolation debugging
- hinting/rasterization concepts
- fallback/mixed-script strategy
- naming, licensing, and IP hygiene

## Production

- reproducible source
- deterministic builds
- fontmake/fontTools literacy
- automated QA
- proof generation
- versioning
- device/browser/platform validation
- no undocumented manual post-export corrections

## Authorship gate

A custom family is not worth making unless it is materially stronger than credible existing typefaces for its intended role.

Before approving a bespoke face, compare it against high-quality controls for:

- beauty
- legibility
- rhythm
- distinctiveness without novelty
- target-size rendering
- numeric behavior
- punctuation quality
- overall family coherence
- product fit

A bespoke typeface that is merely more unusual is a failure.
