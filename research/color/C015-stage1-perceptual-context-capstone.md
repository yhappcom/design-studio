# C015 — Stage 1 Perceptual-Context Capstone

Status: **FOUNDATION CAPSTONE / Stage 1 closure evidence complete; higher-stage device/browser/human/production validation remains open**

## Why this study exists

C014 audited the actual Master Curriculum and found that Color Stage 1 had been held open partly by later-stage requirements. It also identified a small set of real Foundation gaps that still had to be demonstrated rather than merely explained:

1. simultaneous contrast with an original specimen;
2. explicit grayscale-first hierarchy construction;
3. low-light and high-glare stress variants;
4. an `attractive swatches → context failure → revision` critique;
5. Color-relevant design-history / precedent literacy.

C015 closes those gaps without pretending that a static/browser specimen is human-perception, physical-display, or production validation.

Reproducibility artifacts:

- `C015-stage1-perceptual-context-specimen.html`
- `C015-stage1-perceptual-context-validation.py`
- `C015-stage1-perceptual-context-results.json`

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: current Type status through T014 and Color C009.
- Reusable finding: fixed semantic foreground/background values do not normalize actual rendered text mass; Type artifacts and fallback remain later transfer inputs.
- Replication / challenge / transfer opportunity: C015 keeps typography simple because the unresolved question is Color hierarchy/context, not Type rendering.
- Dependency / overlap: no Type PASS is inferred.

### Color
- Evidence checked: Study 008, C006, C007, C009, C011 and C014.
- Reusable finding: luminance-first hierarchy, contextual appearance, redundant state encoding, role-based color assignment and explicit evidence boundaries are already established.
- Replication / challenge / transfer opportunity: C015 turns the remaining theory/partial evidence into one explicit Foundation exercise.
- Dependency / overlap: direct closure of C014 and Study 008.

### Layout / Interaction
- Evidence checked: Layout L005 and Interaction I003 through current status.
- Reusable finding: geometry/state semantics must remain stable while Color is varied; visual state meaning cannot be repaired by color alone.
- Replication / challenge / transfer opportunity: C015 fixes content/geometry/state meaning and changes Color strategy only.
- Dependency / overlap: Layout/Interaction remain canonical owners of geometry and state meaning.

### Web Design
- Evidence checked: current Web status; no substantive W### evidence exists.
- Reusable finding: a controlled HTML specimen can serve as a Color exercise artifact, but it is not Web production validation.
- Implementation/application validation opportunity: later Web work can render the same cases across engines/devices.
- Dependency / overlap: no Web PASS is claimed.

### Other / Cross-cutting
- Historical/precedent sources checked:
  - Michel-Eugène Chevreul, *De la loi du contraste simultané des couleurs...*, 1839, Metropolitan Museum of Art collection record;
  - Josef Albers, *Interaction of Color*, first issued by Yale University Press in 1963; Yale/Albers Foundation descriptions of color-relativity exercises;
  - ISO/CIE 11664-1:2019 and CIE material on the 1931/1964 standard colorimetric observers.
- Reusable finding: historical contextual-color teaching and standardized colorimetry solve different problems and should not be collapsed into one model.

### Overlap decision
- **FOUNDATION CAPSTONE + ORIGINAL EXERCISE + PRECEDENT SYNTHESIS + FINAL GATE REVIEW**.
- Why: the user explicitly requested Stage 1 closure before further advanced expansion.

---

# PART 1 — History and precedent literacy

## Chevreul — contextual contrast as a design problem

The Metropolitan Museum of Art records Michel-Eugène Chevreul's 1839 publication *De la loi du contraste simultané des couleurs, et de l'assortiment des objets colorés, considéré d'après cette loi*.

Source:

`https://www.metmuseum.org/art/collection/search/900717`

The important Stage 1 lesson is not to import a nineteenth-century rule as a modern accessibility standard. The useful precedent is the recognition that color relationships are contextual: neighboring colors affect appearance and therefore color decisions cannot be judged only as isolated chips.

## Albers — color relativity as an exercise method

Yale University Press describes Josef Albers's *Interaction of Color* as originally published in 1963 and built around color studies demonstrating color relativity, intensity, temperature, boundaries, transparency and reversed grounds. The Albers Foundation likewise records the original 1963 Yale edition and its teaching context.

Sources:

- `https://yalebooks.yale.edu/book/9780300179354/interaction-of-color/`
- `https://www.albersfoundation.org/alberses/teaching/interaction-of-color`

The transferable method is **learning by controlled juxtaposition**, not copying Albers's compositions or treating his exercises as current colorimetry.

## CIE — standard measurement is a different layer

ISO/CIE 11664-1:2019 specifies standard colorimetric observers and their color-matching functions. CIE's standardization makes colorimetric measurements interoperable under defined observer/field conditions.

Source:

`https://www.cie.co.at/publications/colorimetry-part-1-cie-standard-colorimetric-observers-0`

### SYNTHESIS

The historical progression relevant to professional Color work is not a single linear theory:

`contextual/relational observation → controlled teaching exercises → standardized colorimetry → modern digital/accessibility/semantic systems`.

Each layer answers a different question.

### STUDIO JUDGMENT

Use historical precedent to sharpen questions and exercise design. Use current standards for normative/measurement claims. Do not turn historical color teaching into accessibility thresholds or production color-management rules.

---

# PART 2 — Original simultaneous-contrast specimen

The C015 HTML specimen places two center targets encoded as exactly:

`#808080`

on two different surrounds:

- `#202020`;
- `#E8E8E8`.

The validation harness confirms:

- left target RGB = `(128,128,128)`;
- right target RGB = `(128,128,128)`;
- encoded target identity = `true`;
- target relative luminance = `0.2158605001` in both locations.

### What is demonstrated

The exercise isolates context: the target stimulus is numerically identical while the surround differs.

### What is not demonstrated

The harness does not measure a human observer's magnitude of simultaneous contrast. Any claim that one target *appears* lighter/darker is source-grounded perceptual theory plus a classic stimulus construction, not measured participant evidence.

### Foundation consequence

A palette chip is not a complete appearance specification. UI Color must be reviewed on the actual surface, neighborhood, size and hierarchy where it will be used.

---

# PART 3 — Grayscale-first hierarchy construction

C015 constructs a hierarchy before adding hue/chroma.

Controlled grayscale roles:

- canvas `#F5F5F3`;
- surface `#FFFFFF`;
- primary text `#1E1E1E`;
- secondary text `#666666`;
- tertiary text `#8A8A8A`;
- primary grayscale action `#2A2A2A` with white content.

Measured ratios:

| Pair | Ratio |
| --- | ---: |
| primary text / canvas | `15.27:1` |
| secondary text / canvas | `5.26:1` |
| tertiary text / canvas | `3.16:1` |
| white / grayscale primary action | `14.35:1` |

The capstone then adds sparse chroma **after** information priority exists:

- primary action becomes `#155EEF` with white content: `5.41:1`;
- mint `#A8F0E9` is used as a selected/brand-supporting surface/marker with dark content rather than as white-text action fill: dark content contrast `12.85:1`.

### SYNTHESIS

Hue/chroma can reinforce hierarchy, but the basic information order should not disappear when chroma is removed.

### REJECT

Reject:

> “Make secondary content lighter until the interface feels premium.”

and:

> “Use the brand hue everywhere so users recognize the brand.”

Both can flatten or corrupt hierarchy even when individual swatches look attractive.

---

# PART 4 — Low-light design-stress variant

The same hierarchy is transferred to a reduced-luminance dark appearance:

- canvas `#0D1317`;
- surface `#151C21`;
- primary text `#E8EEF2`;
- secondary text `#AAB6BE`;
- structural boundary `#667680`;
- light-blue action `#5FB5FF` with dark content.

Representative bounded ratios:

| Pair | Ratio |
| --- | ---: |
| primary text / canvas | `15.98:1` |
| secondary text / canvas | `9.04:1` |
| primary text / surface | `14.71:1` |
| secondary text / surface | `8.32:1` |
| dark content / light-blue action | `8.50:1` |
| boundary / surface | `3.66:1` |

### Evidence boundary

This is a **design-stress variant**, not evidence that the scheme is comfortable in a dark cockpit, bedroom, OLED phone, or any specified nit/ambient-light condition.

The Foundation lesson is narrower: when appearance strategy changes, role ordering and critical pair relationships must be deliberately reconstructed rather than inverted mechanically.

---

# PART 5 — High-glare sensitivity stress

C015 uses a deliberately simple mathematical sensitivity diagnostic:

`Y_stressed = (1 - v)Y + v`

with white veiling fraction `v = 0.15`.

This pushes relative luminance toward white and therefore compresses contrast.

Measured examples:

| Pair | Baseline | Veiled diagnostic |
| --- | ---: | ---: |
| primary text / canvas | `15.27:1` | `4.62:1` |
| secondary text / canvas | `5.26:1` | `3.12:1` |
| light decorative boundary / white | `1.98:1` | `1.73:1` |
| white content / blue action | `5.41:1` | `3.26:1` |

### Important boundary

This is **not** an optical glare model, a display/nit simulation, or a WCAG re-test. It ignores reflections, display black level, angular geometry, pupil/adaptation, haze, wavelength effects and many other variables.

### What the exercise demonstrates

Pairs with smaller baseline margins are more vulnerable to contrast compression in this simple stress model. Therefore a product intended for difficult viewing conditions should not rely on barely sufficient subtle distinctions without actual environmental validation later.

---

# PART 6 — Attractive swatches can fail in context

C015 intentionally chooses four light, visually compatible swatches:

- mint `#A8F0E9`;
- pale blue `#B8D8FF`;
- warm cream `#FFD6A5`;
- pale coral `#FFADAD`.

As isolated chips they can look coherent. The failure is assigning each directly to filled controls/status blocks with white text merely because the palette is attractive.

White-content contrast:

| Fill | White text |
| --- | ---: |
| `#A8F0E9` | `1.29:1` |
| `#B8D8FF` | `1.47:1` |
| `#FFD6A5` | `1.36:1` |
| `#FFADAD` | `1.77:1` |

With dark content `#152028`, the same light colors produce much stronger pair contrast:

| Fill | Dark content |
| --- | ---: |
| `#A8F0E9` | `12.85:1` |
| `#B8D8FF` | `11.27:1` |
| `#FFD6A5` | `12.15:1` |
| `#FFADAD` | `9.32:1` |

### Revision

Do not discard a palette automatically because a naive role assignment fails. Reassign light colors to suitable surface/container/selection roles with appropriate content colors, or choose darker primitives where the semantic role requires a filled action.

### Foundation consequence

`palette attractiveness != semantic fitness != pair contrast != hierarchy quality`.

---

# PART 7 — Two unrelated product contexts

Study 008 requires applying the method to two unrelated contexts. C006 already satisfies this directly:

- finance analytics / portfolio tracking;
- dark operational record/logbook.

C015 does not duplicate C006. It reuses that evidence as required by the Master Curriculum's peer/reuse discipline.

---

# FINAL STAGE 1 GATE REVIEW

## Master Curriculum — Color-relevant visual foundations

| Requirement | Final evidence | Verdict |
| --- | --- | --- |
| color perception | Study 008 + C007 + C015 contextual specimen | **PASS** |
| luminance | Study 008 + C006/C007/C009 + C015 | **PASS** |
| simultaneous contrast | Study 008 theory + C015 original identical-target/different-surround specimen | **PASS** |
| broader contrast/hierarchy relationships | Study 008 + C006/C007/C009/C011 + C015 | **PASS** |
| design history / precedent literacy | C015 Chevreul → Albers → CIE distinction | **PASS** |
| original exercise rather than reading only | C004–C015 reproducible exercises; C015 specifically closes Foundation gaps | **PASS** |
| peer evidence checked/reused | C007 Layout transfer; C009 Type transfer; C011 Interaction transfer; C015 explicit reuse | **PASS** |

## Study 008 explicit PASS requirements

| Requirement | Final evidence | Verdict |
| --- | --- | --- |
| grayscale-first hierarchy exercise | C015 | **PASS** |
| representative text/non-text contrast | C006/C009/C011 | **PASS** |
| state understandable without hue | C011/C008 | **PASS** |
| low-light/high-glare stress variants | C015, bounded as design/math stress only | **PASS** |
| attractive swatches that fail in context | C015 | **PASS** |
| apply method to two unrelated product contexts | C006 | **PASS** |

---

# FOUNDATION VERDICT

**Color Stage 1 — Foundations: PASS.**

This PASS means the current Stage 1 gate is supported by explanation, original exercises, critique, cross-domain reuse and an explicit closure capstone.

It does **not** mean:

- Color as a whole is mastered;
- human perception/comfort has been validated;
- physical displays/environments are validated;
- browser/device/ICC production is complete;
- semantic systems/data visualization are complete;
- later-stage research can be skipped.

C014's stage correction remains in force: unresolved advanced Color evidence moves forward into Stage 2–4/5 backlog rather than being silently treated as Foundation failure.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- C015 closes Color Foundation without treating unresolved Type platform/shaping work as a Color Stage 1 blocker.
- Later Color production work must still use exact shipped Type artifacts for real text-role validation.

### Layout / Interaction
- C015 confirms that Color hierarchy can be isolated while geometry/state meaning remains fixed.
- Later project work should continue to combine Color roles with L/I canonical semantics rather than encode meaning with hue alone.

### Web Design
- C015's HTML is a Color exercise artifact, not Web validation.
- Stage 2+ should transfer the now-closed Foundation principles into real page/theme/browser/device contexts when substantive W### work exists.

---

# Next-stage implication

Do **not** resume the old spectral queue automatically.

With Stage 1 closed, the next work should begin by establishing a **Stage 2 entry plan** from the Master Curriculum, prioritizing project usefulness:

- palette/ramp construction with explicit authoring models;
- semantic color-role systems;
- interaction state/focus integration;
- gamut-aware production/fallback;
- viewing-condition/device-aware validation;
- multiple viable solutions and explicit selection criteria.

Existing C002/C006/C017/C001/C010 already provide an early bridge, so Stage 2 should begin with a gap audit rather than repeat them.