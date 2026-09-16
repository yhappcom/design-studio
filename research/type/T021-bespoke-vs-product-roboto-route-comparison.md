# T021 — Bespoke vs Current Product Roboto Route Comparison

Classification: **EXECUTED PRODUCT-ROUTE REVIEW / T021 CLOSURE DECISION**

## SOURCE — current product control
The live `yhappcom/logmate` main repository was checked directly after the normalized A/B raster failure.

Current bundled font assets are:
- `assets/fonts/Roboto-Regular.ttf` — repository blob `2c97eeadffe1a34bd67d3ff1c3887fd53e22c2ca`, 171,676 bytes;
- `assets/fonts/Roboto-Medium.ttf` — blob `1a7f3b0bba45b7470a4240c3ec67595eeeb02192`, 172,064 bytes;
- `assets/fonts/NotoSansKR-wght.ttf` — blob `b386890ba945e1f39448a6b59f20c5d194f58808`.

`pubspec.yaml` declares `LogMateRoboto` at weights 400/500 and `LogMateNotoSansKR` at 400. No `LogMateRobotoMono` / `RobotoMono` asset is present in the current product repository. Therefore the previously discussed airport-only mono control is not the current main product font contract and must not be represented as one.

`lib/theme/logmate_theme.dart` sets `fontFamily: 'LogMateRoboto'` at ThemeData level and applies the same family to the TextTheme. The product control for this comparison is therefore the exact bundled proportional Roboto family, not a generic system Roboto and not a generic monospace substitute.

## SOURCE — bespoke route evidence
The normalized T021 successor proved:
- semantic architecture 11/11 PASS;
- same bounded operational corpus 36/36, `missing=[]`;
- kerning OFF;
- deterministic 14/17/24px specimens;
- exact CI execution;
- both custom A/B directions FAIL professional drawing coherence.

Observed custom-route failures remain concentrated in `5/S`, `8/B`, `1/I/l`, round/bowl relations, several figures and overall word texture. B's slashed zero is a concrete differentiator, but not sufficient evidence by itself for a whole custom family.

## Method
This is a route comparison, not a popularity contest and not a human-recognition experiment. Criteria are constrained to evidence already available from the live product and T021:
1. drawing maturity at intended sizes;
2. operational ambiguity mechanisms;
3. width/density consequences;
4. product-role coverage;
5. multilingual/fallback implications;
6. implementation and maintenance burden;
7. identity differentiation;
8. reversibility of the decision.

No human readability, pilot recognition, native-device or browser equivalence claim is made here.

## Comparison

| criterion | normalized bespoke A/B | exact current product Roboto | evidence consequence |
| --- | --- | --- | --- |
| Drawing maturity | FAIL at 14/17/24 target proof | mature shipped font asset; no T021 evidence of comparable primitive drawing defects | current bespoke cannot displace product control on drawing evidence |
| 0/O mechanism | B has explicit slashed zero; A plain | no custom LogMate slashed-zero mechanism established here | bespoke has one concrete ambiguity hypothesis, but benefit is unvalidated with humans |
| 1/I/l, 5/S, 8/B | structurally distinct but drawing FAIL | no T021 evidence of product-blocking failure | bespoke does not establish a net ambiguity advantage |
| Operational width | A/B are proportional; earlier exact measurements were broadly near Roboto but string-specific | current proportional baseline | no evidence that custom route solves a width problem requiring a new family |
| Numeric comparison | custom figure system exists but drawing is unresolved | product can use role-specific numeric feature/layout strategy without whole-family redesign | figure needs should remain a role/feature problem until contrary evidence |
| Product-role breadth | bounded research repertoire only | already covers live UI roles and 400/500 weights | bespoke scope is materially narrower |
| Korean/multilingual | no production fallback family or mixed-script seam proof | product already bundles Noto Sans KR alongside Roboto | bespoke would add fallback-seam and weight-matching work |
| Implementation | new font production, QA, licensing/source/version pipeline, native/browser validation required | already bundled and declared | bespoke has substantial incremental production cost |
| Identity | potentially distinctive, especially B technical traits | intentionally conventional | bespoke's principal remaining upside is identity, not demonstrated operational necessity |
| Reversibility | high while research-only | high; current control can remain while identity experiments continue separately | no need to force a family decision now |

## Width evidence already established
Earlier exact local comparison against Roboto Regular over airports, identifiers and numeric strings found candidate-vs-Roboto width deltas of approximately **-9.7% to +4.2%, mean -0.6%**. The normalized successor similarly remained a proportional system. This does not prove layout equivalence, but it falsifies a simple claim that a custom family is required because Roboto is globally too wide or because custom geometry automatically yields a density advantage.

## SYNTHESIS
The T021 bespoke route has succeeded as a learning and diagnostic instrument but has not earned product-family continuation.

The important distinction is:
- **type authorship capability:** T021 produced executable architecture, controlled consumers, full bounded encoding and intended-size proof;
- **product need:** current evidence does not show a LogMate operational problem that requires replacing the mature proportional Roboto control with a bespoke text family.

A custom family would currently exchange a mature, already-integrated product asset for unresolved drawing, incomplete role coverage, new multilingual seams and a much larger QA surface. The one clearly differentiated mechanism — B's slashed zero — is separable from the decision to author an entire family.

## STUDIO JUDGMENT — route decision
**KEEP current proportional `LogMateRoboto` as the product text/ledger baseline.**

**STOP the T021 full bespoke-family route.** Do not continue serial A/B glyph repair under T021.

**RETAIN custom type as a narrower future identity/display research route only if a concrete product role is identified** — e.g. wordmark, display/title treatment, or a deliberately bounded operational identifier style. Such work must start from a new hypothesis and must not inherit an assumption that the whole logbook requires custom typography.

This is a product-development route judgment, not a claim that Roboto is universally more readable or aesthetically superior.

## T021 closure
T021 can now close without spacing/kerning work on the rejected bespoke family. The earlier spacing and T022 blockers were conditional on a custom family surviving the drawing/product-route gate. It did not.

What T021 established:
1. coherent-family design requires semantic architecture, not parameter labels;
2. coverage/build success is upstream of drawing validity, not equivalent to it;
3. target-size raster can reject a technically complete family;
4. ambiguity mechanisms must be separable from whole-family authorship decisions;
5. product typography must compare benefit against integration, fallback and QA cost;
6. a mature current control is a legitimate experimental baseline, not an obstacle to originality.

**T021 status: CLOSED — custom full-family route rejected for current LogMate product scope; current proportional Roboto retained as control.**

## T022 boundary
T022 may now open, but its scope must be reframed. It must not continue kerning a rejected custom family. The useful Stage-2 question is **role-specific numeral/identifier behavior in the mature product baseline**:
- proportional vs tabular figures;
- numeric comparison columns vs prose/identifier roles;
- punctuation and time/total alignment;
- whether any bounded ambiguity treatment is justified without switching the whole UI to monospace;
- kerning/class analysis only where the selected mature-font role actually needs it.

## OPEN
- Exact native Flutter shaping/feature support for the proposed role-specific figure strategy remains to be executed.
- Human pilot recognition/readability testing remains deferred.
- The exact current product Roboto binary should be used for any future artifact-level metric/raster test; this review verified its repository identity and integration but did not claim a new binary-level native render comparison.
- 200% text-size stress remains a Layout/product geometry concern, not a reason to create a narrower custom font.

## RELATED DOMAIN CHECK
- **Layout/Interaction:** keep flexible column geometry; solve comparison alignment by numeric role and column design, not global monospace.
- **Web:** do not adopt the rejected bespoke family; preserve metric-flexible layout and current mature control until a new bounded identity role earns transfer.
- **Content:** preserve literal airport, registration, flight and time tokens in future proofs.
- **Color:** ambiguity must remain typographic/structural; color is not a substitute.

## HANDOFFS TO OTHER SPECIALISTS
Layout/Web may treat the T021 A/B metrics as historical research evidence only. They are not product tokens. Future Type handoff will focus on mature-font role contracts and exact figure behavior rather than a new whole-family geometry.