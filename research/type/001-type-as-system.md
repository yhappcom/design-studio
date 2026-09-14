# Study 001 — Type Is a System, Not a Set of Drawings

Status: FOUNDATION STUDY / not a completed gate.

## SOURCE — professional education scope

### University of Reading
The MA Communication Design: Typeface Design Pathway combines practical development with historical/theoretical study and frames typeface work as defining, planning, and designing a multiscript family, including character complement and family relationships.

Source: https://www.reading.ac.uk/ready-to-study/study/2026/typography-and-graphic-communication-pg/ma-typeface-design

### KABK Type and Media
The programme explicitly studies letterform contrast, rhythm, proportion, weight, type history, font technology, digitising, and tool development across print, screens, and interactive media.

Source: https://www.kabk.nl/en/programmes/master/type-and-media

## SOURCE — spacing and kerning

Glyphs defines spacing as the sidebearing work that controls the general white space around glyphs, and kerning as a specific pair adjustment. Its guidance recommends establishing spacing first and delaying kerning until sidebearings can no longer solve the general rhythm.

Sources:
- https://glyphsapp.com/learn/spacing
- https://glyphsapp.com/learn/kerning
- https://handbook.glyphsapp.com/spacing-and-kerning/

The practical implication is that an attractive isolated glyph can still belong to a poor typeface if its sidebearings, counters, and repeated rhythm fail.

## SOURCE — font as software

Microsoft's OpenType specification shows that a digital font is more than outline geometry. It includes font tables, Unicode mapping, metrics, layout behavior, variation architecture, and rasterization-related behavior.

Source: https://learn.microsoft.com/en-us/typography/opentype/spec/

Google Fonts' production guidance separately treats outline quality, scalable/reproducible building, QA, local testing, and variable-font requirements as production concerns.

Sources:
- https://googlefonts.github.io/gf-guide/outlines.html
- https://googlefonts.github.io/gf-guide/build.html
- https://googlefonts.github.io/gf-guide/production.html

## SYNTHESIS

Professional type design operates simultaneously at several scales:

1. **glyph form** — contour, stress, joint, terminal, counter;
2. **glyph metrics** — sidebearings and advance widths;
3. **text rhythm** — repeated black/white texture in strings;
4. **family system** — coherent shapes, weights, widths, figure styles, punctuation;
5. **language behavior** — encoding, diacritics, shaping, fallback/multiscript concerns;
6. **rendering** — actual pixels at target sizes/platforms;
7. **software production** — tables, build process, QA, versioning.

A weakness at any layer can invalidate the apparent success of another.

## STUDIO JUDGMENT

The studio must stop evaluating custom type primarily through enlarged SVG specimens. Large vector specimens are useful for contour critique, but they are weak evidence for spacing, UI legibility, rasterization, family behavior, or production quality.

The correct unit of judgment changes with the problem:

- contour problem → glyph at large scale;
- rhythm problem → strings and paragraphs/data rows;
- UI problem → actual target size in realistic context;
- family problem → multiple glyph groups/weights/widths;
- production problem → built fonts across environments.

## PRACTICE GATE CREATED BY THIS STUDY

Before any bespoke type project proceeds to a full alphabet:

1. establish a small control set such as `H O n o`;
2. draw at least three genuinely different construction hypotheses;
3. space them using repeated strings before kerning;
4. evaluate counter/sidebearing rhythm in black/white;
5. test actual target sizes;
6. record why one hypothesis survives;
7. only then expand the character set.

For data-heavy products, add numeral/identifier control strings early, but do not let operational codes replace fundamental alphabet spacing exercises.

## OPEN

Still to study before this module can pass:

- historical stroke/contrast models and how they shape modern sans construction;
- formal optical correction and overshoot practice;
- Bézier curve quality through exercises;
- numeral system history and figure-style design;
- punctuation spacing and optical centering;
- cross-platform small-size rendering.
