# T021 — LogMate Operational Glyph Coverage Audit

Status: **EXECUTED — LIVE-PROJECT TRANSFER AUDIT / FAMILY-BREADTH BLOCKER QUANTIFIED**  
Companion artifacts:
- `T021-logmate-operational-glyph-coverage-audit.py`
- `T021-logmate-operational-glyph-coverage-results.json`

## Purpose

After the T021 pair-gap method contradiction review removed the uncalibrated rule `270–300u AV gap => primitive drawing defect`, the next question is concrete:

> Does the current T021 mini-family contain enough of the actual LogMate operational corpus to compare it credibly with the product's proportional Roboto baseline and exact airport-only Roboto Mono interim control?

This is a **TRANSFER VALIDATION + COVERAGE AUDIT**, not a font-quality judgment.

---

## RELATED DOMAIN CHECK

### Type
Checked T017–T020, the LogMate Type identity directive, T021 broader mini-family build harness, and the new pair-gap method validation.

The current built T021 repertoire demonstrated by `T021-broader-mini-family-prekerning-transfer.py` is:

`H O n o A V T L I + space`

No unbuilt glyph is inferred as available.

### Color
Current Color evidence does not change character-set coverage. Keep Color constant during Type comparisons.

### Layout / Interaction
Semantic columns remain valid independent of candidate family. Layout should not freeze around a custom candidate whose actual operational character set is incomplete.

### Web Design
Exact Web/browser transfer is premature until the candidate can render the real LogMate corpus without fallback replacing most of the intended glyphs.

### LogMate live project
The current product uses an exact `LogMateRobotoMono` airport-code role as an **interim deterministic control**, not a final Type identity. That control can remain while T021 earns sufficient breadth for a direct comparison.

---

## Corpus

Airport codes:

`ICN NRT SIN JFK LHR CDG HND DXB FRA LAX`

Identifiers:

`KE704 BA117 AF264 B737-900 B737-8 A320-200 HL8301 N12345 G-EUOH`

Numbers/time:

`00:45 02:18 09:55 12:40 1,284:35 9,999:59 1 11 111 8 88 888`

Ambiguity:

`0/O · 1/I/l · 5/S · 8/B`

---

## Result

### Airport uppercase coverage

The airport corpus requires 16 distinct uppercase letters:

`A B C D F G H I J K L N R S T X`

Current T021 proves only five of those:

`A H I L T`

Coverage: **5/16 = 31.25%**.

Missing:

`B C D F G J K N R S X`

### Identifier uppercase coverage

The identifier corpus requires 11 distinct uppercase letters:

`A B E F G H K L N O U`

Current T021 covers:

`A H L O`

Coverage: **4/11 = 36.36%**.

### Digits and punctuation

Current T021 contains **none** of the required operational digits `0–9`, nor `-`, `,`, or `:`.

Therefore it cannot yet render the core flight-number, aircraft-type, registration, duration or career-total corpus as its own Type system.

### Ambiguity set

Required audit characters:

`0 1 5 8 B I O S l`

Current T021 covers only:

`I O`

Coverage: **2/9 = 22.22%**.

### Whole corpus character coverage

Across the bounded corpus, 33 distinct non-space characters are required. Current T021 directly covers only:

`A H I L O T`

Coverage: **6/33 = 18.18%**.

This number is a bounded corpus-coverage measure, not a statement about a production font's full character-set requirement.

---

## Interpretation

### SYNTHESIS

The present T021 candidate is too narrow for a product-facing identity decision.

The main blocker is now empirically clearer:

`experimental primitive quality question → method calibrated → actual operational family breadth is insufficient`

### STUDIO JUDGMENT

Do not open a broad kerning program or declare a LogMate custom Type direction while roughly four-fifths of the bounded operational corpus still cannot be rendered by the candidate itself.

Do not solve the gap by rapidly drawing unrelated glyphs one-by-one merely to increase a percentage. The next family extension should preserve a coherent construction/spacing system and deliberately target high-value LogMate coverage.

---

## Next construction order

A practical next uppercase expansion should prioritize the missing airport set because airport codes are the current live UI identity/control seam:

`B C D F G J K N R S X`

Then add identifier-specific uppercase not already covered:

`E U`

Next add:

- digits `0–9`;
- `-`, `:`, `,`;
- lowercase `l` for ambiguity inspection;
- one accented construction path as already required by Stage 2 breadth work.

This order is not a final production character-set plan. It is the shortest evidence path to a valid LogMate control comparison.

---

## Kerning eligibility consequence

T022 remains **NOT OPEN**.

Reason:

- not because `AV` measured 270–300u;
- because the current family cannot yet expose residual pair behavior across the actual operational repertoire.

Kerning becomes meaningful only after base drawings/spacing exist for enough product-relevant glyphs to show recurring class behavior and true exceptions.

---

## HANDOFFS TO OTHER SPECIALISTS

### Layout / Interaction
Keep the airport-type seam replaceable. Current exact mono control can stabilize UI work, but its metrics should not be treated as the immutable final geometry of a future Type identity.

### Web Design
Delay exact custom-family Web transfer until the candidate can render the bounded airport/identifier/numeric corpus without extensive fallback. When that threshold is reached, test exact loading/fallback and responsive effects.

### Color
No change. Hold visual salience/color constant during the upcoming Type identity comparison.

---

## Verdict

**NOT READY — OPERATIONAL GLYPH BREADTH IS THE CURRENT TYPE BLOCKER**

The immediate research target is no longer arbitrary A/V gap reduction. It is a coherent expansion from the current mini-family to enough real LogMate glyphs to support target-size, operational, and identity comparison against both product controls.
