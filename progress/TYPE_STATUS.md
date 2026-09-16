# Typography / Type Design Specialist Status

Operating state: **ACTIVE — STAGE 2 PRACTICE / T021 CLOSED / T022 MATURE-FONT ROLE SYSTEM OPEN**  
Governance sync: 2026-09-16  
Primary path: `research/type/`  
Active study: `T022`

## Current level
Stage 1 **PASS**; Stage 2 **PRACTICE / NOT PASSED**.

Authority: T019 Stage 1; T020 Stage 2 entry; T021 operational-family authorship and route decision.

## T021 closure
`T021-bespoke-vs-product-roboto-route-comparison.md` closes the current LogMate whole-family bespoke route.

The live LogMate main repository was checked directly. Current product typography is exact bundled proportional `LogMateRoboto`: `Roboto-Regular.ttf` and `Roboto-Medium.ttf`, with `NotoSansKR-wght.ttf` also bundled. `pubspec.yaml` declares `LogMateRoboto` at 400/500 and `LogMateNotoSansKR` at 400; `lib/theme/logmate_theme.dart` applies `LogMateRoboto` at ThemeData/TextTheme level. No current `LogMateRobotoMono` / `RobotoMono` asset is present, so mono is not the current product control.

T021 normalized bespoke evidence reached semantic architecture 11/11 PASS, exact 36/36 build and 14/17/24 raster, but both A/B failed professional drawing coherence. Route comparison found no established operational width, ambiguity or role-coverage advantage sufficient to justify replacing the mature integrated Roboto baseline. B's slashed zero remains a separable feature hypothesis, not a whole-family justification.

**T021 verdict: CLOSED — stop full bespoke-family repair for current LogMate scope; retain proportional LogMateRoboto as product baseline.** Custom type may return only under a new bounded identity/display hypothesis.

## Evidence chain learned
`repertoire → semantic architecture → executable sensitivity → coverage/build → intended-size raster → drawing validity → product-route comparison → role contract`

T021 also established that spacing/kerning work is conditional on the candidate family surviving drawing and product-route gates. A rejected family does not need to be polished merely to complete a curriculum checklist.

## Stage 2 snapshot
- Stage 1 foundations: **PASS**
- coherent glyph-family authorship exercise: **EXECUTED; custom product route REJECTED after evidence**
- bounded repertoire/build: **36/36 PASS**
- normalized semantic architecture: **11/11 PASS**
- exact CI reproducibility: **PASS**
- intended-size raster: **14/17/24 EXECUTED**
- product-route comparison: **EXECUTED**
- whole-family bespoke LogMate route: **STOP / CLOSED**
- mature-font role system: **T022 OPEN**
- human readability/recognition: **DEFERRED / NOT CLAIMED**
- native Flutter feature/shaping proof: **OPEN**

## T022 scope — mature product typography, not rejected-family continuation
1. establish exact product-role inventory for identifiers, airports, aircraft, registration, time/duration, cumulative totals, labels and prose;
2. test proportional vs tabular figure behavior for comparison-critical numeric roles while retaining proportional text elsewhere;
3. inspect punctuation/time/total alignment and determine whether alignment belongs to font feature, formatting, column geometry, or a combination;
4. test bounded ambiguity mechanisms without global monospace or whole-family replacement;
5. verify actual Flutter/native support and behavior before product recommendation;
6. analyze kerning/classes only where the selected mature-font role actually exposes a residual need;
7. produce multiple role-system alternatives and defend the selected direction under explicit product criteria, satisfying the Stage-2 comparison method rather than forcing a custom-family artifact.

## Product controls
- Current control: exact bundled proportional `LogMateRoboto` 400/500.
- Korean companion: bundled `LogMateNotoSansKR` 400; mixed-script weight/fallback seam remains a transfer concern.
- Generic/system Roboto is not an exact product artifact when binary-level claims matter.
- Generic monospace must not be labeled as a LogMate product control.

## HANDOFFS
- Layout/Interaction: keep flexible column geometry; numeric alignment is a joint font-feature/column-layout contract.
- Web: rejected bespoke A/B metrics are historical research evidence only; preserve metric-flexible layout.
- Content: preserve literal airport/registration/flight/time strings in T022 proof corpora.
- Color: ambiguity remains typographic/structural; do not encode character distinction by color.

## Evidence boundary
No claim of Roboto universal superiority is made. No human pilot readability/recognition, native-device, browser equivalence, or exact Flutter OpenType-feature PASS is yet established. T021 closed a product route because its custom candidates did not earn continuation under the available evidence; T022 now studies the mature baseline at the role-system level.