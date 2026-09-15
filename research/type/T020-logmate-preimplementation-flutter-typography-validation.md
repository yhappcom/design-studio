# T020 — LogMate Pre-Implementation Flutter Typography Validation

Status: **LIVE-PRODUCT TRANSFER / PRE-IMPLEMENTATION CONTRACT — implementation-ready Type decisions established; exact Flutter/native product validation remains OPEN**

Owner: Typography / Type Design Specialist  
Canonical path: `research/type/`  
Transfer target: `yhappcom/logmate`, branch `design/design-studio-proposal`  
Parents: `T017-logmate-operational-data-typography-semantic-geometry-transfer.md`, `T018-logmate-conservative-font-candidate-audit.md`

## Purpose

T017 established the LogMate operational-data Type model. T018 selected Roboto as the conservative provisional family and rejected blanket monospace. T020 moves those decisions forward **before final UI completion** so Opening Draft 03 and View Logbook do not continue on an unstable font/weight contract.

Question:

> What Type package, role matrix, numeric/identifier behavior, fallback rule and geometry acceptance contract can be safely specified now, while leaving genuinely runtime/device/human questions OPEN?

Evidence classification: **TRANSFER VALIDATION + PRE-IMPLEMENTATION SPECIFICATION + FAILURE ANALYSIS**. This is not a bespoke-font project and not a native-device PASS.

---

## RELATED DOMAIN CHECK

### Type

Checked T004, T005, T016, T017, T018, T019 and current Type status.

Reused:
- role semantics precede font styling;
- `tnum` is a numeric-comparison contract, not an alphanumeric fixed-width solution;
- fallback can change geometry;
- exact package/weight identity matters;
- no evidence justifies a LogMate custom font or blanket mono family.

Classification: **TRANSFER VALIDATION + EXTENSION**.

### Color

Checked current Color Stage 1 PASS and the retained device/environment boundary. Weight choice is not cockpit/night-readability proof. Physical display, glare and low-light validation stay OPEN.

### Layout / Interaction

Checked current Layout/Interaction status and L004 tabular-numeral dense-comparison transfer.

Reused:
- `tnum` and track allocation are a joint contract;
- a correct Type feature can expose an under-sized column;
- enlarged-text failure should be handled by track/recomposition policy rather than shrinking or forcing mono.

New handoffs from T020: the current 19px Flight carrier zone is too tight after proportional transfer, and the Type column supports compact aircraft codes but not all full model strings.

### Web Design

Checked current Web status. PWA/Web remains a target runtime for exact font delivery, fallback and text-scaling transfer. Chromium control evidence below does not substitute for Flutter Web/native parity.

### Product implementation

Checked current LogMate branch state at study start:
- `pubspec.yaml`;
- `lib/theme/logmate_theme.dart`;
- `lib/main.dart` Draft 03 Opening;
- `lib/screens/view_logbook_screen.dart`;
- `lib/localization/date_formats.dart`;
- latest branch commits.

Human observation remains **DEFERRED TO APP-DEVELOPMENT VALIDATION**. No recognition/error-rate result is simulated.

---

## 1. Current product state

### SOURCE — package

Current `pubspec.yaml` declares:
- `LogMateRoboto` Regular 400;
- `LogMateRoboto` Medium 500;
- `LogMateNotoSansKR` variable file, declared as weight 400.

Current theme asks for 600, 700 and 800 in addition to 400/500. The authored role system and bundled static Roboto package therefore do not match.

### SOURCE — Opening Draft 03

Current route geometry:

`DEP 44 | connector 46 | ARR 44 | flexible | TIME 68`

- DEP right-aligned;
- ARR left-aligned;
- connector is CustomPaint geometry, not a font glyph;
- TIME uses `FontFeature.tabularFigures()`;
- Total time also uses tabular figures.

Verdict: **KEEP**.

### SOURCE — View Logbook

View Logbook still forces generic `fontFamily: 'monospace'` for most data values and the carrier portion of Flight. This remains **REWORK**.

Current columns:
- Date 64;
- Type 60;
- Registration 84;
- Flight 84;
- DEP/ARR 50 each;
- Block/Night/Instrument 96 each;
- row height 36.

---

## 2. Font provenance audit

### SOURCE — exact Git blob identity

| Product asset | LogMate Git blob SHA | Bytes |
| --- | --- | ---: |
| Roboto Regular | `2c97eeadffe1a34bd67d3ff1c3887fd53e22c2ca` | 171,676 |
| Roboto Medium | `1a7f3b0bba45b7470a4240c3ec67595eeeb02192` | 172,064 |
| Noto Sans KR variable | `b386890ba945e1f39448a6b59f20c5d194f58808` | 10,414,588 |

Roboto Regular/Medium exactly match Google Fonts commit `724bf98e9f5cb98a1d3d5044f45a2e286b817401`, the 2017 v2.137-era Apache-licensed Roboto family package.

The same official snapshot contains the missing matching Bold:

| Matching weight | Official blob SHA | Bytes |
| --- | --- | ---: |
| Roboto Bold 700 | `d3f01ad245b628f386ac95786f53167038720eb2` | 170,760 |

The LogMate Noto Sans KR blob exactly matches the current Google Fonts `NotoSansKR[wght].ttf`. Current metadata identifies it as OFL, Korean primary script, with Korean, Latin, Latin-ext, Cyrillic and Vietnamese subsets and `wght` 100–900.

### SYNTHESIS

The smallest-risk package correction is **not** migration to current variable Roboto. Add the matching historical Bold 700 from the same family snapshot already used by LogMate.

Mixing current variable Roboto with historical static 400/500 would introduce a family-generation change for which there is no product need.

---

## 3. Flutter source contract

Current official Flutter documentation establishes:
- static weight/style requests should have corresponding imported files;
- when a requested weight/style has no matching static file, Flutter may simulate/extrapolate and authors should avoid relying on it;
- `fontFamilyFallback` is an ordered fallback list after the primary family;
- `FontFeature.tabularFigures()` exposes OpenType `tnum` when supported;
- platform text scaling is represented by `TextScaler`; controlled linear scale is not a substitute for actual runtime scaling;
- automatic `FontWeight` control of a variable font `wght` axis became stable in Flutter 3.41.

References:
- https://docs.flutter.dev/cookbook/design/fonts
- https://api.flutter.dev/flutter/painting/TextStyle-class.html
- https://api.flutter.dev/flutter/painting/TextStyle/fontFamilyFallback.html
- https://api.flutter.dev/flutter/dart-ui/FontFeature/FontFeature.tabularFigures.html
- https://api.flutter.dev/flutter/widgets/Text/textScaler.html
- https://docs.flutter.dev/release/breaking-changes/font-weight-variation

The repository Dart SDK constraint does not prove the exact deployed Flutter engine version. T020 therefore does **not** assume variable-weight fallback behavior above 400 for every target build.

---

## 4. Provisional product font package contract

### KEEP

Primary family: **Roboto**, existing v2.137 static family.

### CHANGE

Product-authored UI package:
- 400 Regular — existing;
- 500 Medium — existing;
- 700 Bold — add matching v2.137 file.

Normalize authored weights:
- ordinary current 600 → **500**;
- current 800 → **700**;
- current 700 → keep, now backed by a real Bold file.

### REJECT for now

- dependence on synthetic 600/800;
- latest variable Roboto migration merely for convenience;
- second mono family for technical atmosphere;
- custom LogMate font production.

### STUDIO JUDGMENT

`400 / 500 / 700` is sufficient for the current product hierarchy while keeping package behavior explicit and conservative.

---

## 5. LogMate Type Role Matrix v1

| Role | Size | Weight | Type behavior | Numeric behavior | Alignment / case | Fallback | Decision |
| --- | ---: | ---: | --- | --- | --- | --- | --- |
| Product name | 17 | 700 | Roboto proportional | default | authored case | primary | exact 700 |
| Opening statement | 27/31/34 adaptive | 700 | proportional | default | start; current tight tracking provisional | primary | exact Bold recheck |
| Screen title | 20 | 700 | proportional | default | composition-owned | primary | KEEP |
| Section/control title | 15–17 | 500 | proportional | role-dependent | task-owned | primary | 600→500 |
| Body/helper | 15 | 400 | proportional/wrapping | proportional | start | user-data roles explicit fallback | KEEP |
| Button label | 15 | 500 | proportional | default | control-owned | primary | 600→500 |
| Opening airport | 17 | 500 | proportional identifier | none | uppercase; DEP right / ARR left; tracking 0 | primary Latin | KEEP |
| Opening time | 17 | 500 | Roboto | **tnum** | right | primary | KEEP |
| Opening total time | 32 | 700 | Roboto | **tnum** | composition-owned | primary | exact 700 |
| Ledger header | 15 | 500 | proportional | none | column-owned | primary | KEEP |
| Ledger airport | 15 | 400 | proportional identifier | none | semantic column | primary Latin | remove mono |
| Aircraft type | 15 | 400 | proportional identifier | none | semantic column | primary Latin | format/width OPEN |
| Registration | 15 | 400 | proportional identifier | no forced tnum | semantic column | primary Latin | remove mono |
| Flight carrier | 15 | 400 | proportional identifier | default | semantic sub-zone | primary Latin | remove mono |
| Flight number sub-zone | 15 | 400 | proportional identifier | **tnum numeric sub-zone** | sub-zone | primary Latin | split retained |
| Block/Night/Instrument | 15 | 400 | Roboto | **tnum** | right | primary | remove mono |
| Page/Previous Total | 15 | 400/500 | Roboto | **tnum** | right | primary | explicit role |
| New Total | 15 | 500 | Roboto | **tnum** | right | primary | 600→500 |
| Date | 15 | 400 | Roboto | **tnum** where repeated numeric comparison is intended | locale order | primary | KEEP |
| Crew name | 15 | 400 | proportional | default | start | Roboto → Noto Sans KR → system | fallback seam |
| Remark/free text | 15 | 400 | proportional/wrapping | default | start | Roboto → Noto Sans KR → system | fallback seam |

These sizes are product-transfer tokens, not human-readability PASS.

---

## 6. Controlled geometry validation

### Method

Direct Flutter execution was unavailable in this research environment: `flutter` and `dart` executables were absent. The next executable layer used:
- headless Chromium;
- explicit local Roboto Regular/Medium/Bold controls;
- `font-synthesis:none`;
- actual LogMate strings;
- current Draft 03/View Logbook track sizes;
- linear font-size stress factors `1.0, 1.10, 1.20, 1.25, 1.30, 1.50, 2.0`.

The harness explicitly loads each face before measurement.

Artifacts:
- `T020-logmate-preimplementation-type-contract.py`;
- `T020-logmate-preimplementation-type-contract-specimen.html`;
- `T020-logmate-preimplementation-type-contract-results.json`.

### Evidence boundary

The executable control uses installed open-source Roboto v2.138, while product package identity is separately verified as v2.137 by Git blob identity. Pixel thresholds are therefore **pre-implementation risk indicators**, not exact Flutter acceptance numbers.

The scale factors are controlled linear font-size stress and are **not** claimed to equal Flutter `TextScaler` behavior.

---

## 7. Opening Draft 03 results

### Airport 44px slot

At 17px / Medium control:
- all 10 airport codes fit at 1.0×;
- widest: `HND` ≈ 35.28px;
- normal slack ≈ 8.72px;
- all fit at 1.20×;
- `HND` crosses the slot by 1.25× stress;
- all fail at 2.0×.

Derived control threshold: ≈ **1.247×**.

Verdict: **KEEP at normal scale; not an enlarged-text-safe fixed-width contract.** Under actual large text the row must gain space or recompose. Do not narrow the font to protect the track.

### Time 68px slot

At 17px / Medium + `tnum`:
- all test times fit normally;
- widest ≈ 43.16px;
- all remain within 68px through 1.50× linear stress;
- all fail at 2.0×.

Verdict: **KEEP**. Airport is the earlier Opening constraint.

### Connector

Painted geometry no longer participates in font fallback/glyph-width risk.

Verdict: **KEEP** from Type dependency perspective.

---

## 8. View Logbook proportional-transfer results

Existing content widths after padding are approximately:
- DEP/ARR 42px;
- Registration 76px;
- Type 52px;
- numeric total 84px;
- Date 56px;
- Flight content 68px, currently 19px carrier + 2px gap + remaining number region.

### Airport

All test airports fit 42px normally under proportional Roboto control.

Verdict: **proportional Roboto viable at normal scale.**

### Registration

`HL8301`, `N12345`, `G-EUOH`, `UR-82060` all fit normally. `UR-82060` is limiting at ≈65.28px and crosses 76px around the 1.2× stress.

Verdict: normal-scale KEEP; enlarged text needs track/recomposition policy.

### Aircraft Type

Current mock projection values `B738`, `B38M`, `B77W` fit. Full transfer strings do not all fit:
- `B737-900` ≈64.08px >52px;
- `A320-200` ≈64.52px >52px;
- `B737-8` fits.

Verdict: **OPEN DATA-FORMAT/GEOMETRY CONTRACT.** Either View Logbook intentionally uses a compact standardized designator, or the Type column must widen/adapt. Do not silently truncate full type data and do not hide the conflict with a narrower font.

### Flight carrier/number split

At 15px proportional Roboto:
- current 19px carrier zone is slightly too narrow for `AA` and `BA`;
- max carrier ≈19.58px;
- max tested number/suffix `1234A` ≈43.52px;
- total Flight content remains 68px.

A provisional **20px carrier + 2px gap + 46px number** split fits the entire tested normal-size corpus without increasing the outer 84px column.

Verdict: **CHANGE 19/2/47 → provisional 20/2/46** after proportional transfer. Exact Flutter TextPainter validation is required before production freeze.

### Numeric totals

The current 84px numeric content width fits normal values including `99,987+29` / `99,999+59`; limiting Medium control ≈71.36px. The two large totals cross the current width around 1.2× linear stress.

Verdict: **96px outer numeric columns are normal-scale draft geometry only.** At enlarged text, allow wider tracks/local horizontal scrolling/recomposition; do not force smaller Type.

### Date

Compact numeric formats `09.02`, `02/09`, `9/2`, `12.31`, `31/12` fit the 56px content width normally.

Verdict: KEEP normal-scale contract; validate the real locale set in Flutter.

---

## 9. Numeric contract v1

Use explicit `FontFeature.tabularFigures()` for:
- Opening duration;
- Opening total time;
- Block/Night/Instrument and future PIC/SIC duration columns;
- Page/Previous/New totals;
- vertically compared counts;
- compact numeric date columns when repeated comparison requires it;
- the explicitly separated numeric sub-zone of Flight number.

Do not automatically apply `tnum` to:
- airport code;
- registration;
- aircraft type;
- whole unparsed mixed identifiers;
- crew names;
- remarks/prose.

The Chromium control produced zero digit-advance spread with explicit `tnum`. Explicit `tnum` remains part of the semantic contract even if a current font happens to have equal default digit advances.

---

## 10. Identifier contract v1

Default:
- Roboto proportional;
- tracking 0 for operational codes unless a specific role proves otherwise;
- semantic columns/sub-zones;
- uppercase only where actual identifier data is uppercase;
- no generic monospace;
- no global slashed zero.

Mandatory audit corpus remains:
- airport `ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`;
- flight `KE704 BA117 AF264` plus current `7C132 / 7C1123 / KE28 / AA1234A`;
- aircraft `B737-900 B737-8 A320-200` plus compact designators;
- registration `HL8301 N12345 G-EUOH UR-82060`;
- ambiguity `0/O`, `1/I/l`, `5/S`, `8/B`.

Human error-rate claims remain OPEN.

---

## 11. Fallback / multilingual contract v1

The exact LogMate `NotoSansKR-wght.ttf` matches current Google Fonts Noto Sans KR. Current metadata covers Korean plus Latin/Latin-ext/Cyrillic/Vietnamese and exposes weight 100–900. It does **not** establish Arabic coverage.

For user-entered/imported human text roles such as Crew and Remark, provisional chain:

`LogMateRoboto → LogMateNotoSansKR → platform fallback`

Use Flutter's ordered `fontFamilyFallback` where the role needs multilingual data.

### Conservative weight boundary

Until the actual target Flutter engine/version is verified, use this Noto Sans KR fallback seam primarily for **regular 400 user-data roles**. Do not assume 500/700 variable fallback parity across every target build merely because the source file exposes a `wght` axis.

### Arabic / RTL

If Arabic/RTL becomes an explicit supported requirement, add and validate an appropriate script-capable family rather than assuming Noto Sans KR covers it. Platform fallback may render missing scripts, but metrics/design then vary by platform.

OPEN:
- exact mixed Latin/Korean Flutter line boxes;
- combining-mark/normalization stress with product strings;
- Arabic/RTL family and bidi UI behavior if required;
- iOS/Android/Web fallback parity.

---

## 12. Draft implementation specification

### `pubspec.yaml`

```yaml
fonts:
  - family: LogMateRoboto
    fonts:
      - asset: assets/fonts/Roboto-Regular.ttf
        weight: 400
      - asset: assets/fonts/Roboto-Medium.ttf
        weight: 500
      - asset: assets/fonts/Roboto-Bold.ttf
        weight: 700
```

Keep `LogMateNotoSansKR` as the multilingual fallback asset pending exact runtime validation.

### Theme normalization

- `w800 → w700`;
- `w700 → w700` with real file;
- ordinary `w600 → w500`;
- use w700 only where hierarchy materially needs it.

### View Logbook

- remove `fontFamily: 'monospace'` from `_valueStyle` and `_LedgerFlightIdentifier`;
- use main Roboto;
- attach `tnum` only to numeric comparison roles;
- provisionally update Flight carrier/number split to 20/2/46;
- resolve whether `Type` means compact designator or full model before freezing width;
- retain horizontal scrolling for true 2-D ledger comparison when enlarged tracks exceed viewport.

### Opening

- retain semantic DEP/connector/ARR/time structure;
- retain 17/500 airport and time roles provisionally;
- retain `tnum` on time;
- retain painted connector;
- do not claim 44px airport slots are valid for enlarged text; provide a text-scaling adaptation path.

---

## 13. Complete now vs OPEN

### PRE-IMPLEMENTATION COMPLETE

- Roboto provisional main family;
- exact product Roboto provenance;
- matching 700 family asset identified;
- 400/500/700 package strategy;
- 600/800 synthesis-removal strategy;
- Type Role Matrix v1;
- identifier contract;
- numeric `tnum` contract;
- Draft 03 Opening stress map;
- View Logbook proportional-transfer failure map;
- Flight internal-zone revision;
- aircraft Type format/width conflict;
- Noto Sans KR fallback strategy/scope boundary;
- reproducible Chromium/fontTools control harness/results.

### OPEN — PRODUCT/RUNTIME VALIDATION

- direct Flutter/Skia run using actual v2.137 400/500/700 binaries;
- Flutter `TextPainter` exact widths/baselines;
- actual `MediaQuery.textScalerOf` / nonlinear platform text scaling;
- row-height/recomposition at accessibility sizes;
- Android physical rendering;
- iOS/CoreText physical rendering;
- Flutter Web/PWA delivery/cache/failure/fallback;
- exact mixed-script line metrics with product Noto asset;
- Firefox/Safari/WebKit parity where PWA matters;
- human identifier-recognition and dense-ledger scan evidence;
- real low-light/cockpit visibility.

These OPEN items do not block UI from using the pre-implementation contract. They block only final production/platform/human claims.

---

## 14. KEEP / CHANGE / OPEN

### KEEP
- Roboto provisional family;
- Opening semantic route geometry;
- painted route connector;
- explicit `tnum` on comparison numerics;
- proportional airport identifiers;
- current overall size hierarchy unless integration exposes failure.

### CHANGE
- add matching Roboto Bold 700;
- remove unsupported 600/800 authored weights;
- remove blanket generic monospace from View Logbook;
- explicitly assign `tnum` numeric roles;
- Flight split 19/2/47 → provisional 20/2/46;
- role-level multilingual fallback for user data.

### OPEN
- full vs compact aircraft Type projection;
- exact scaled-text track policy;
- Flutter baselines/line heights;
- final supported user-data scripts;
- slashed zero only if live-product evidence justifies it;
- product-stage human/device validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction

1. Opening 44px airport track is normal-scale viable but not enlarged-text invariant; adaptation/recomposition is required.
2. Proportional View Logbook exposes current 19px Flight carrier sub-zone failure; 20/2/46 fits tested normal corpus without enlarging the outer Flight column.
3. Type 60px is valid for compact codes such as `B738/B38M/B77W`, not all full strings such as `B737-900/A320-200`.
4. 96px total columns are normal-scale viable but lose margin quickly under controlled enlargement.

These are **TRANSFER VALIDATION / LIMITATION** findings, not a reason to return to monospace.

### Color

Real 700 changes stroke density. Re-check final text/background pairs and dark mode on actual devices after integration. Do not infer low-light comfort.

### Web Design

For PWA transfer, reproduce the final 400/500/700 package and explicit fallback in actual browser delivery states. T020 is not CDN/cache/service-worker validation.

### LogMate UI / implementation

UI can proceed using Type Role Matrix v1 and the package contract. Final sign-off should run the OPEN Flutter/native regression matrix rather than re-open family selection unless implementation evidence contradicts T020.

---

## Final pre-implementation verdict

**READY FOR LOGMATE PRE-IMPLEMENTATION TYPE HANDOFF.**

The unresolved work is runtime/product validation, not a missing Type direction.
