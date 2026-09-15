# T017 — LogMate Operational Data Typography + Semantic Geometry Transfer

Status: **PROJECT TRANSFER / PRACTICE + CRITIQUE — reusable Type contract established; production font-family selection and Flutter/platform validation remain OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Transfer target: `yhappcom/logmate`, branch `design/design-studio-proposal`

## Purpose

This study records a live-product transfer from the Design Studio Typography program into LogMate.

It is not a new generic typography survey and not a bespoke-typeface project. The immediate product trigger is a rendered Opening Screen Draft 01 in which repeated route rows such as:

- `ICN → NRT        02:18`
- `NRT → ICN        02:31`
- `ICN → SIN        06:24`

showed unstable visual alignment because the airport-code glyphs use proportional advances. Tabular figures stabilized the time numerals but did not stabilize the alphabetic airport identifiers.

The project question is therefore broader than “which font looks better?”:

> Which LogMate information roles should rely on typeface behavior, which must be protected by semantic geometry, and what conservative Type system can keep operational data legible and comparable without turning the whole product into monospace typography?

This is a **TRANSFER VALIDATION + PROJECT-SPECIFIC SYNTHESIS** of existing Type evidence into an actual Flutter product.

---

## Product evidence checked

Canonical LogMate product/design source for this transfer:

- repository: `yhappcom/logmate`;
- branch: `design/design-studio-proposal`;
- `design-studio/02-onboarding/USER_REVIEW_OPENING_01.md`;
- `design-studio/02-onboarding/OPENING_SAMPLE_ROUTE_POLICY_01.md`.

The current LogMate review already establishes:

- mobile-portrait Opening hierarchy is broadly worth preserving;
- route rows shift because proportional glyph widths differ;
- tabular figures do not solve alphabetic airport-code geometry;
- Draft 02 must use explicit `DEP | arrow | ARR | time` alignment;
- font-candidate evaluation must enter the screen work earlier;
- regional sample data means the Type/layout system must survive airport-code substitutions rather than being tuned to one `ICN/NRT` fixture;
- mobile landscape, tablet portrait, tablet landscape and PWA/wide remain explicit transfer surfaces.

The regional sample policy also requires stress cases including `ICN`, `LHR`, `JFK`, `CDG`, `HND` and multiple form factors, and explicitly separates coarse-region familiarity from any inference of the pilot's actual base.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:

- `005-numerals-punctuation-systems.md`;
- `009-typography-as-information-architecture.md`;
- `T004-native-numeral-punctuation-renderer-proof.md`;
- `T005-latin-korean-mixed-script-fallback.md`;
- `T016-webfont-loading-fallback-metric-contract.md`;
- current `progress/TYPE_STATUS.md`.

Reusable findings:

- tabular figures are an advance-width contract for numeric comparison; they are not a general solution for alphabetic identifiers;
- `0/O`, `1/I/l`, `5/S`, `8/B` ambiguity is a legitimate operational-type question, but raster/design inspection is not human error-rate proof;
- same nominal type size does not imply identical apparent size or line geometry across fallback fonts/scripts;
- runtime fallback/loading states can materially change geometry;
- typography roles should be defined by information/task function rather than by technical-looking content alone.

Transfer decision:

- **TRANSFER VALIDATION + EXTENSION.** Existing evidence is reused rather than rediscovered; LogMate adds an actual aviation-ledger/identifier context and exposes where Type must coordinate with semantic layout geometry.

### Color

Evidence checked:

- current `progress/COLOR_STATUS.md`, Stage 1 PASS and its explicit boundary around physical/device/human validation.

Reusable finding:

- hierarchy/legibility cannot be inferred from an isolated font or glyph specimen; rendered Type participates in actual foreground/background and viewing conditions.

Scope:

- T017 establishes no Color threshold and makes no cockpit/night visibility claim. Night/cockpit validation remains a separate Color/device/human problem.

### Layout / Interaction

Evidence checked:

- `research/layout/L004-tabular-numerals-dense-comparison-transfer.md`;
- current `progress/LAYOUT_STATUS.md`.

Reusable findings:

- dense numeric comparison is a joint contract: number semantics + formatting + Type runtime behavior + Layout track allocation;
- Chromium transfer in L004 showed `tnum` can remove digit/decimal drift while also increasing intrinsic width enough to break a too-tight column;
- Layout must size from the approved production format and type feature, not from placeholder screenshots;
- Type is a spatial input, not decoration applied after geometry.

Transfer decision:

- **CONFIRMATION + PRODUCT EXTENSION.** LogMate repeats the same boundary in a different domain: Type owns identifier/numeral behavior; Layout owns semantic tracks and recomposition. Neither domain alone can guarantee the final row rhythm.

### Web Design

Evidence checked:

- current `progress/WEB_STATUS.md`, Stage 1 PASS through W009.

Reusable finding:

- exact production font loading, responsive recomposition, enlarged text, browser/device behavior and fallback remain runtime validation layers rather than assumptions from a static font specimen.

Transfer opportunity:

- LogMate PWA/wide surfaces should later reproduce the approved Type role system under actual browser font delivery/fallback, localization and text enlargement.

### Other / project implementation

LogMate is Flutter-based. T017 records a design contract, not a claim that every feature has already been verified in Flutter/Skia/CoreText/Web.

OPEN implementation layers include:

- exact Flutter text metrics for the selected family;
- Android/Skia rendering;
- iOS/CoreText rendering;
- PWA/browser font loading/fallback;
- text scaling up to the project target stress level;
- exact OpenType feature support in the selected font artifact;
- multilingual user-data fallback.

---

# 1. Observed failure — alphabetic identifier width is not a numeral problem

The Draft 01 route row visually couples four different semantic objects:

`DEP | direction | ARR | duration`

When rendered as proportional text, alphabetic glyph advances differ. A three-character airport code does not have one universal visual/advance width merely because all values contain three letters.

Examples to retain in stress testing:

- `ICN`
- `NRT`
- `SIN`
- `JFK`
- `LHR`
- `CDG`
- `HND`
- `DXB`
- `FRA`
- `LAX`

### SOURCE / prior evidence boundary

T004 and L004 establish `tnum` as numeric-spacing behavior. They do not establish fixed-width uppercase Latin alphabet behavior.

### SYNTHESIS

`tabular numeral support != fixed-width identifier support`.

Applying `tnum` correctly to `02:18` cannot by itself stabilize `ICN`, `LHR` or `JFK`.

### STUDIO JUDGMENT

Do not treat this as evidence that LogMate needs an all-monospace UI or a custom font.

The first response must be to separate the semantic objects and define stable anchors. Typeface selection then optimizes legibility, density and rhythm inside those protected regions.

---

# 2. Core transfer model

T017 adopts this project order:

`information role → semantic geometry → alignment/anchor → type behavior → OpenType feature → runtime/fallback validation → product observation`

Short form:

**Layout robustness → Type refinement.**

This order does not reduce Type responsibility. Type must still specify which behavior each role requires and must reject a font whose metrics, figures, punctuation or identifier forms are unsuitable. It simply prevents typeface choice from being used to hide a structural layout defect.

---

# 3. LogMate Type Role Matrix — provisional transfer contract

Exact point/sp sizes remain product-layout decisions and must be validated in rendered screens. The matrix therefore records role behavior rather than pretending an unmeasured final size is established.

| Role | Priority | Provisional behavior | Weight / case | Alignment | Numerals | Tracking | Fallback | Current issue |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Product name / temporary wordmark | identity | proportional | restrained display/UI weight; case as authored | context-dependent | default | optical only | primary Latin face | final identity treatment OPEN |
| Screen title | high hierarchy | proportional | semibold/bold only as hierarchy requires | start/center by composition | default | no width-fixing | UI fallback | exact scale OPEN |
| Section heading | hierarchy | proportional | medium/semibold | start | default | minimal | UI fallback | exact density OPEN |
| Body UI text | comprehension | proportional | regular | start | proportional default | normal | multilingual-safe fallback where needed | text scaling transfer OPEN |
| Airport code | operational identifier | proportional identifier by default | medium/semibold uppercase candidate | fixed semantic DEP/ARR anchor | digits rare/not governing | do not use tracking to fake equal width | primary Latin must cover role | font-candidate width/legibility audit OPEN |
| Flight number | operational identifier | proportional identifier by default | regular/medium uppercase as data dictates | semantic column | do not force `tnum` solely because digits occur | minimal | primary Latin | ambiguity audit OPEN |
| Aircraft type | operational identifier | proportional identifier | regular/medium uppercase | semantic column | default unless role proves comparison need | minimal | primary Latin | hyphen/figure rhythm OPEN |
| Registration | high-risk identifier | proportional identifier unless evidence supports alternate treatment | regular/medium uppercase | semantic column | identifier legibility outranks numeric alignment | minimal | primary Latin | `0/O`, `1/I/l`, `5/S`, `8/B` audit OPEN |
| Date | operational numeric/text | format-dependent | regular/medium | column; usually right or structured | `tnum` when repeated comparison is intended | normal | locale-aware | locale format width OPEN |
| Time / duration | comparison-critical numeric | tabular figures | regular/medium | right anchor | **`tnum` candidate/default for repeated rows** | normal | selected face must preserve behavior | colon + runtime proof OPEN |
| Career total | comparison-critical numeric | tabular figures | emphasis by hierarchy | right | **`tnum`** | normal | stable numeric fallback required | max magnitude stress OPEN |
| Landing count | comparison-critical numeric | tabular figures when columnar | regular/medium | right | **`tnum`** | normal | stable numeric fallback required | 1/11/111 etc. stress OPEN |
| Metadata | supporting | proportional | regular | start | role-dependent | normal | multilingual-safe | density/text scaling OPEN |
| Ledger header | schema | proportional | medium/semibold | matches data-column logic | labels not forced tabular | restrained | UI fallback | compactness OPEN |
| Ledger body | operational | mixed by column role | regular/medium | semantic columns | numeric columns use `tnum` where warranted | minimal | role-specific | exact production table OPEN |
| Crew name | human name | proportional | regular | start | default | normal | multilingual/Unicode fallback | long/mixed-script names OPEN |
| Remark / free text | reading | proportional | regular | start; wraps | proportional | normal | multilingual/Unicode fallback | RTL/combining/wrap OPEN |

### Key distinction

Technical-looking data does **not** automatically justify monospace.

The decision criterion is the task:

- repeated numeric comparison → tabular figure behavior is often justified;
- fixed-length operational identifier → prioritize unambiguous glyphs and stable semantic anchors;
- prose/name/free text → preserve proportional reading rhythm and multilingual flexibility.

---

# 4. Numeric contract

Minimum test strings retained for LogMate:

- `00:45`
- `02:18`
- `09:55`
- `12:40`
- `1,284:35`
- `9,999:59`
- `1`
- `11`
- `111`
- `8`
- `88`
- `888`

### TRANSFER VALIDATION from T004 + L004

For repeated time, duration, total and count columns, LogMate should treat tabular figures as the default candidate because stable digit advances support scan/comparison rhythm.

But the full contract is:

`number semantics + formatting + tabular feature + alignment + sufficient column width + runtime proof`.

`tnum` alone is not the whole solution.

### Width warning

L004 demonstrated that enabling `tnum` can increase intrinsic width. LogMate must therefore size time/total columns **after** activating the approved numeric feature and using realistic maximum values.

### Punctuation

Colon, comma, slash and hyphen must be inspected with the selected family because LogMate relies on them in time, duration, aircraft type and registration strings.

A font with good digits but weak compact punctuation can still be a poor operational choice.

---

# 5. Identifier legibility contract

Mandatory ambiguity groups:

- `0 / O`
- `1 / I / l`
- `5 / S`
- `8 / B`

Mandatory product strings:

- `KE704`
- `BA117`
- `AF264`
- `B737-900`
- `B737-8`
- `A320-200`
- `HL8301`
- `N12345`
- `G-EUOH`

### TRANSFER from T004

T004 demonstrated that deliberately differentiated forms can remain visibly distinct in a compact raster proof, but explicitly did **not** claim a measured reduction in human confusion.

LogMate therefore uses these ambiguity groups as a **font rejection/inspection criterion**, not as a fabricated recognition score.

### Slashed zero

A slashed zero remains conditional.

Do not enable it globally merely because the font exposes the feature. Consider it only if:

- `0/O` confusion is consequential in the exact identifier role;
- the selected font's default distinction is insufficient;
- the feature can be enabled reliably on target platforms;
- the marked zero does not introduce excessive coding/technical tone or punctuation confusion.

This remains OPEN pending candidate/platform audit.

---

# 6. Geometry Contract — Opening route row

The Opening route row must not be implemented as one visually spaced string whose internal alignment depends on glyph advances.

Semantic structure:

`DEP | arrow | ARR | flexible space | time`

Required invariants:

1. DEP has a stable start/slot.
2. Arrow/direction has its own stable slot/anchor.
3. ARR has a stable start/slot independent of DEP's ink width.
4. Time/duration has a stable right anchor.
5. Route-row baseline relationship is consistent across samples.
6. Airport-code ink may vary inside its semantic slot without moving later anchors.
7. Time uses the approved numeric behavior before final width is frozen.
8. Regional sample substitution must not require per-airport spacing hacks.
9. Font-family replacement must not destroy the semantic relationship.
10. Enlarged text or narrower widths must recompose deliberately rather than clip/overlap silently.

### What Type owns inside this contract

- candidate family metrics and apparent density;
- identifier letterforms and ambiguity;
- uppercase rhythm;
- punctuation and arrow compatibility where text glyphs are used;
- numeral system and `tnum` quality;
- weight availability;
- line metrics / baseline behavior;
- fallback and script coverage.

### What Layout owns

- actual track/anchor sizing;
- spacing between semantic objects;
- responsive recomposition;
- wrap/stack/scroll policy;
- preservation of task priority under narrower widths/text enlargement.

This is a dependency contract, not a transfer of responsibility away from Type.

---

# 7. View Logbook geometry and typography contract

The Opening failure is a small instance of the same problem that a ledger amplifies.

Representative View Logbook schema:

`DATE | FLT NO | AC TYPE | REG | DEP | ARR | BLOCK | PIC | SIC | NIGHT | LANDING | CREW | REMARK`

### Current Type policy

- **Do not make the whole ledger monospace.**
- Protect each semantic column with stable geometry.
- Use tabular figures where repeated numeric comparison justifies them.
- Keep identifiers proportional by default unless controlled evidence shows a materially better limited treatment.
- Keep names and free text proportional.

### Column-level transfer

| Column | Type behavior | Geometry behavior |
| --- | --- | --- |
| Date | tabular/structured numeric where comparison warrants | fixed/defined date column |
| Flight No | proportional identifier | semantic identifier column |
| Aircraft Type | proportional identifier | semantic identifier column |
| Registration | high-legibility proportional identifier | semantic identifier column |
| DEP | uppercase identifier | fixed semantic DEP column |
| ARR | uppercase identifier | fixed semantic ARR column |
| Block | tabular numeric | right-aligned numeric column |
| PIC | tabular numeric | right-aligned numeric column |
| SIC | tabular numeric | right-aligned numeric column |
| Night | tabular numeric | right-aligned numeric column |
| Landing | tabular numeric | right-aligned numeric column |
| Crew | proportional multilingual name | flexible text column/region |
| Remark | proportional multilingual prose | flexible/wrapping text region |

### SYNTHESIS

The desired system is not “all characters have equal width.”

It is:

**proportional UI + operational identifier rules + tabular numeric rules + semantic column geometry**.

---

# 8. Monospace decision boundary

### REJECT as default

Do not use a monospace family across the entire LogMate UI or ledger merely to make operational data look technical or aligned.

Reasons:

- inefficient use of mobile horizontal space;
- earlier wrapping of names/remarks;
- weaker natural word shape in prose;
- unnecessary visual separation from general UI typography;
- multilingual/fallback complexity;
- it solves some equal-advance questions by imposing a cost on roles that do not need equal advance.

### OPEN as limited alternative

A coordinated mono companion may be tested only for a tightly bounded identifier role if a controlled candidate comparison shows a material benefit in:

- scan rhythm;
- identifier distinction;
- compact repetition;
- production consistency.

If the benefit is marginal, keep one proportional family.

This preserves a conservative product direction and avoids an unnecessary dual-font system.

---

# 9. Conservative font-selection policy

LogMate should not use typeface novelty as a product differentiator at this stage.

### Selection rule

Prefer a mature, broadly deployed, well-documented UI family that satisfies the operational requirements with minimal special handling.

Do not select a family because it looks aviation-like, technical, cockpit-like or distinctive in isolation.

### Candidate-audit direction

The next product Type block should compare approximately 3–5 materially different but mature candidates using the same LogMate corpus. Roboto remains a control/baseline, not an assumed final choice.

Required comparison dimensions:

- airport-code width behavior;
- identifier ambiguity;
- tabular figure quality;
- colon/comma/slash/hyphen;
- baseline/line metrics;
- x-height/compactness;
- weight availability;
- Flutter rendering;
- Android/iOS/Web/PWA practicality;
- licensing/distribution practicality;
- fallback behavior;
- asset/loading cost where bundled/downloaded.

### Tie-break rule — STUDIO JUDGMENT

If two candidates perform similarly, prefer the less exotic, more mature, simpler-to-distribute family.

Do not create or commission a bespoke LogMate UI font unless controlled evidence shows that mature existing families cannot simultaneously satisfy important product requirements.

---

# 10. Multilingual / fallback contract

Product-authored LogMate UI is currently English-only, but user-entered/imported data must remain Unicode-safe.

Relevant future content includes:

- Crew names;
- Remarks;
- Notes;
- imported text.

Stress categories include:

- Korean;
- accented Latin;
- Cyrillic;
- Arabic / RTL;
- combining marks;
- mixed-script strings.

### Transfer from T005/T016

Do not assume equal nominal size, family naming or metric similarity means equivalent mixed-script geometry.

Do not use Latin x-height matching as a generic Korean/other-script fallback solution.

Fallback may change:

- apparent body size;
- ascent/descent and line box;
- advance widths;
- punctuation;
- wrapping;
- downstream geometry.

### Provisional policy

- Operational Latin identifiers should ideally remain within the selected primary face and not depend on emergency fallback.
- Crew/Remark/Notes must support multilingual fallback and flexible wrapping.
- Exact fallback pairs must be tested in the actual target stack before production lock.
- Arabic/RTL behavior is OPEN and must not be inferred from Latin/Korean evidence.

---

# 11. Platform transfer contract

T017 does not fabricate platform PASS.

### Flutter / Android

OPEN:

- exact selected-family metrics through Flutter text layout;
- Skia rasterization at target device densities;
- `FontFeature` behavior for the selected artifact;
- text scaling/enlarged-text behavior;
- baseline and line-height across real widgets.

### iOS

OPEN:

- CoreText rendering/metrics differences;
- fallback selection;
- line-height/baseline parity with Android;
- feature activation behavior for bundled/system fonts.

### Web / PWA

OPEN:

- actual `@font-face` delivery if a downloadable family is used;
- loading/failure fallback geometry;
- caching/preload/service-worker path;
- Chromium/Firefox/Safari comparison;
- 200% text/enlargement and responsive recomposition.

T016 proves that loading/failure fallback can itself be a different geometry state; LogMate must not approve only the preferred-loaded screenshot if PWA uses downloadable fonts.

---

# 12. Opening Draft 02 recommendation

## KEEP

- mobile-portrait macro hierarchy as a strong reference composition;
- route samples as a compact expression of the product's record grammar;
- duration on the route row;
- general UI prose as proportional typography;
- regionalized sample concept with deterministic fallback, without treating region as pilot base.

## CHANGE

- implement route rows as semantic fields rather than one spacing-sensitive string;
- stabilize DEP, arrow, ARR and time anchors;
- enable the approved tabular numeric behavior for repeated duration values before final width tuning;
- evaluate the screen using multiple airport-code stress fixtures rather than only `ICN/NRT`;
- separate general UI, identifier and numeric Type roles in tokens/styles;
- evaluate font candidates in the actual rendered screen, not only in specimen sheets.

## OPEN

- final primary family;
- exact airport-code weight/tracking;
- whether any limited mono companion is beneficial;
- slashed-zero use;
- exact line height/baseline tuning;
- final mobile-landscape/tablet/PWA type scales;
- exact multilingual fallback stack;
- Android/iOS/Web renderer parity;
- human identifier-recognition evidence.

### City labels

Code-primary + restrained city/metro labels remain an **optional comprehension variant**, not a Type requirement.

Add them only if the product review shows they materially improve route comprehension without damaging mobile density and hierarchy. Do not add them merely to repair type alignment.

---

# 13. Reusable Design Studio principles versus LogMate-specific decisions

## Reusable principle

Fixed-length identifiers do not become layout-stable merely because their character count is fixed.

## LogMate-specific application

`DEP | arrow | ARR | duration` receives explicit semantic anchors.

---

## Reusable principle

Tabular figures are appropriate for repeated numeric comparison, not for every string containing digits.

## LogMate-specific application

Block/PIC/SIC/Night/times/totals/counts are candidate/default `tnum` roles; `KE704`, `HL8301`, `B737-8` remain identifier roles.

---

## Reusable principle

Monospace is a functional tool, not a synonym for technical data.

## LogMate-specific application

Whole-product/whole-ledger monospace is rejected as the default; limited identifier mono remains an evidence-dependent option only.

---

## Reusable principle

Fallback is a rendered geometry state, not merely a character-coverage backup.

## LogMate-specific application

Multilingual Crew/Remark/Notes and future PWA delivery require exact fallback/runtime validation.

---

# 14. Validation plan — next executable Type block

The next LogMate Type block should perform a conservative candidate audit with the same corpus and fixed product roles.

Minimum corpus:

### Airport codes

`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`

### Flight / aircraft / registrations

`KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`

### Numeric / time

`00:45 02:18 09:55 12:40 1,284:35 9,999:59 1 11 111 8 88 888`

### Ambiguity

`0 O 1 I l 5 S 8 B`

Required outputs:

1. candidate width/metric comparison;
2. identifier-legibility inspection;
3. `tnum` and punctuation audit;
4. Opening route-row render comparison;
5. at least one representative View Logbook ledger comparison;
6. Flutter/runtime evidence where executable;
7. platform/fallback OPEN items where not executable;
8. one provisional baseline recommendation with explicit reject reasons for alternatives.

Human/user experiments remain deferred to app-development validation where instructed and must not be simulated.

---

# 15. Current evidence classification

## SOURCE / canonical evidence reused

- T004: numeral/punctuation system, `tnum`, ambiguity and renderer-layer limits;
- T005: real Latin/Korean mixed-script fallback and vertical-metric mismatch;
- T016: downloadable-font loading/failure/fallback geometry;
- L004: browser transfer of tabular figures and intrinsic-width cost;
- LogMate Draft 01 review and regional sample policy from the current product branch.

## TRANSFER VALIDATION

The same abstract Type concerns now alter an actual product decision:

- airport code cannot rely on numeric features;
- route-row geometry must be semantic;
- ledger numeric comparison needs `tnum` plus real width allocation;
- identifiers require glyph-disambiguation review;
- fallback/platform differences remain product QA states.

## SYNTHESIS

LogMate's operational typography system should be:

**proportional general UI + high-legibility operational identifiers + tabular comparison numerics + semantic geometry + explicit fallback/runtime validation**.

## STUDIO JUDGMENT

Prefer conservative mature type families and one-family solutions. Introduce a mono companion or bespoke type work only after controlled evidence demonstrates a material unresolved need.

## OPEN

- final font candidate/baseline selection;
- measured airport-code width variance by candidate;
- Flutter/Android/iOS/PWA renderer matrix;
- exact multilingual fallback stack;
- 200% enlarged-text stress in the app;
- human recognition/comparison evidence;
- production View Logbook density and form-factor transfer.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

Useful finding:

- Route and ledger alignment must protect semantic anchors independently of proportional identifier ink width.
- Numeric columns must be sized after the final numeric feature/format is active.

Canonical sections:

- Sections 6 and 7.

Transfer note:

- **CONFIRMS + EXTENDS L004** into an aviation-logbook product. Type is not asking Layout to make every character fixed-width; Layout should preserve semantic tracks while Type supplies role-appropriate metrics/features.

Scope limit:

- exact track widths and responsive recomposition remain Layout-owned and must be tested with the eventual production font.

### Color

Useful finding:

- T017 establishes text roles/geometry but no Night/cockpit luminance result.

Transfer note:

- preserve the distinction between Type legibility and physical low-light Color/device validation.

### Web Design

Useful finding:

- PWA/wide must reuse the same operational identifier/numeric semantics, but downloadable-font loading/fallback can create different geometry states.

Transfer note:

- apply T016's loaded/loading-fallback/failed-fallback model if LogMate Web uses downloadable fonts; test enlarged text and responsive table/ledger behavior with the selected production family.

### LogMate UI / product team

Immediate transferable contract:

- Draft 02 may proceed with semantic route columns and separate UI/identifier/numeric Type roles.
- Do not lock the final family, exact airport-code tracking, mono companion or slashed zero until the candidate audit is complete.
- Extend the same logic to View Logbook rather than treating Opening as a one-off fix.

---

# 16. Current transfer verdict

The structural/type-role contract is mature enough to guide Draft 02 without experimental typography.

However, the original LogMate Type Transfer Sprint completion condition requires a provisional production font baseline and candidate comparison. That evidence is not yet complete.

**NOT READY — BLOCKING TYPE ISSUE EXISTS**

Blocking issue:

> A mature-font candidate audit using the fixed LogMate corpus has not yet selected the provisional primary family or verified the exact identifier/numeric behavior in Flutter and target platform conditions.

This blocker does **not** prevent Draft 02 structural implementation. It prevents final typography lock and a claim that the complete Type Transfer Sprint is finished.
