# Exercise 006 — Typography as Information Architecture

Status: CRITIQUE COMPLETE / enlarged-text rendered proof still required.

## Purpose

Create and critique multiple typographic solutions for the same information, then transfer the method to a second category. The exercise tests semantic roles before font choice.

Primary references:
- https://developer.apple.com/videos/play/wwdc2020/10175/
- https://developer.apple.com/documentation/uikit/scaling-fonts-automatically
- https://developer.apple.com/design/human-interface-guidelines/lists-and-tables
- https://www.w3.org/WAI/WCAG22/Understanding/reflow.html

## Shared content set — expense review

- screen context: August expenses
- primary value: $4,286.40
- supporting facts: budget $5,000; remaining $713.60; 38 transactions; +7.2% vs July
- status: 86% of budget
- action: Review transactions
- dense rows: date / merchant / category / amount

Before selecting any font, define roles:

| Role | Why it exists | Scan behavior |
| --- | --- | --- |
| context | identifies period/object | once on entry |
| primary value | answers “how much?” | first fixation |
| comparison | interprets primary value | second pass |
| status | signals budget condition | exception scan |
| action | exposes next operation | intentional target |
| row label | identifies transaction | repeated vertical scan |
| amount | enables magnitude comparison | repeated column scan |
| metadata | disambiguates row | optional/detail scan |

## Solution A — size-dominant

Composition: very large primary value, medium context/status, small supporting facts and rows.

KEEP: immediate first fixation.

REWORK: supporting facts become too dependent on small text; enlarged text causes the large value to consume excessive vertical space.

REJECT as final direction: size alone does not sufficiently distinguish comparison, status, action, and table semantics.

## Solution B — weight/alignment-dominant

Composition: modest size range; weight separates context/value/metadata; stable columns align labels and amounts; whitespace separates summary from rows.

KEEP: economical variable use and strong numeric comparison.

REWORK: weight differences can become weak at low-quality rasterization or for users with reduced contrast sensitivity. Status needs a redundant semantic cue rather than a weight change alone.

## Solution C — role-separated, restrained differentiation

Composition:
- context: compact heading role;
- primary value: display/value role;
- comparison: body role with explicit sign/direction;
- status: text + semantic icon/label;
- action: control role, not styled as another heading;
- row names: body role;
- amounts: numeric role using tabular figures only where alignment is required;
- metadata: secondary body role.

Font family remains unspecified. The requirement is that the selected type system can satisfy these roles, including scalable UI text and stable numeric alignment.

KEEP as strongest hypothesis because each distinction has a semantic job and decorative duplication is minimized.

## Dense table geometry

Preferred wide geometry:

`DATE | MERCHANT (flex) | CATEGORY | AMOUNT (right aligned)`

Rules:
- amounts share a right edge and tabular figures when supported;
- merchant gets flexible width because identity is more important than category repetition;
- date may use compact formatting only if ambiguity is avoided;
- column headings remain explicit;
- grid lines are optional because column alignment and row spacing already encode structure.

Narrow adaptation:

`MERCHANT                         AMOUNT`
`date · category`

This is not a squeezed four-column table. It changes composition while preserving the primary comparison task.

## Enlarged-text stress model

At large accessibility sizes:
- context and supporting prose may wrap;
- primary value remains intact where feasible, but may reduce display-size differentiation rather than truncate;
- action remains a distinct target;
- each transaction row becomes a two- or three-line card-like row;
- amount stays associated with its merchant and is never pushed into an ambiguous neighboring row.

The test criterion is preservation of role relationships, not preservation of original coordinates.

## Removing duplicated typography

Rejected distinction: uppercase + extra tracking for every metadata label. Metadata is already separated by placement and lower priority. The extra casing/tracking does not add meaning and can impair word-shape reading. Remove it.

This directly satisfies the exercise requirement to delete a typographic distinction when another channel already carries the semantic difference.

## Second context — clinical appointment summary

Unrelated information set:
- appointment context;
- clinician/service;
- date/time;
- location;
- preparation instruction;
- status;
- reschedule action.

Transfer:
- date/time becomes the primary operational value rather than a monetary number;
- location and preparation cannot be demoted merely because they are “metadata” in another product;
- status again requires semantics beyond color;
- tabular figures may be unnecessary because values are not scanned in a comparative column.

This demonstrates why semantic roles cannot be copied mechanically between products.

## Cross-context critique

### KEEP

- define roles and scan order before fonts/tokens;
- use the fewest typographic variables that preserve semantic distinctions;
- design numeric features from the comparison task;
- adapt geometry when width/text size changes instead of shrinking type.

### REWORK

A rendered prototype is still needed to observe line breaks, actual font metrics, and Dynamic Type behavior. The current artifact proves the composition logic, not device performance.

### REJECT

- monospace as a generic signal of technical seriousness;
- fixed column geometry at narrow widths;
- token-first typography detached from content roles;
- assuming “metadata” always deserves the same low priority.

## Remaining evidence before PASS

- render all three expense solutions at normal and enlarged text sizes;
- inspect the dense-row adaptation with real font metrics;
- verify a second context under the same enlarged-text stress;
- record a failure → revision cycle from the rendered result.
