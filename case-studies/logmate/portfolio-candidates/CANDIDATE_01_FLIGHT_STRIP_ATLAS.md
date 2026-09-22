# LogMate Portfolio Candidate 01 - Flight Strip Atlas

Status: **DESIGN PROPOSAL / STATIC PORTFOLIO / NOT RUNTIME VALIDATED**  
Candidate: **01 / 10**  
Concept name: **Flight Strip Atlas**  
One-line concept: **A calm pilot workspace built from aligned operational strips and open paper-like fields, where records read as one continuous system rather than a stack of dashboard cards.**

## Provenance

- LogMate product source (READ-ONLY): `yhappcom/logmate@b551ce434ad72b1895033e0f3617c73b026d40ea`
- Design Studio design/research baseline: `yhappcom/design-studio@74dcb12d278c110dd682ac0ff8c4988aceaba28b`
- Product authority read first: `logmate/AGENTS.md`, `logmate/MASTER.md`
- Implementation evidence inspected: `lib/screens/home_screen.dart`, `lib/screens/add_flight_screen.dart`, `lib/screens/view_logbook_screen.dart`, `lib/theme/logmate_theme.dart`
- Design authority: `AGENTS.md`, `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md`, `case-studies/logmate/DESIGN_CORRIDOR_20260919.md`

This candidate does not modify LogMate and does not treat current Flutter implementation as product authority. It preserves confirmed product semantics and leaves MASTER OPEN decisions OPEN.

---

## 1. Product context and design problem

LogMate is a personal pilot logbook companion: manual-first, import-optional, local-first, paper-logbook-first, and targeted equally at native mobile and tablet/EFB PWA. The interface therefore has to serve two apparently conflicting modes:

1. **quiet orientation** - Home should expose what matters now without becoming a generic analytics dashboard;
2. **operational density** - Add Flight and View Logbook must tolerate compact aviation identifiers, time values, many optional fields, and paper-transcription workflows without losing semantic ownership.

The current implementation is useful evidence but still contains presentation shells and unresolved persistence/calculation/runtime contracts. Candidate 01 therefore designs a visual system around *record continuity*, not around current widget containers.

## 2. Design thesis

**The flight record is the visual atom.**

Instead of cards, tiles, cockpit metaphors, or ornamental aviation graphics, Flight Strip Atlas uses a repeating horizontal strip grammar inspired only by the *functional property* of operational strips: identity on the left, route/context through the middle, quantitative outcome at the right. It does **not** imitate physical flight-progress strips or ATC equipment.

The same grammar scales from one flight on Home, to one editable flight in Add Flight, to many flights in View Logbook. This creates product identity through repeated information behavior rather than decoration.

Three rules govern the concept:

- **Open field before container:** whitespace and alignment group content; surfaces appear only for active/edit/error/recovery ownership.
- **Datum before decoration:** operational identifiers and time values align to stable reading axes.
- **Continuity before sameness:** Home, form, and ledger may have different density, but the identity -> route -> time reading direction survives.

## 3. Visual language

### Signature device: the datum spine

A narrow vertical datum near the start edge anchors section labels, dates, and record starts. It is not a permanent decorative rail: it appears only where multiple records/sections need a shared reading origin. On narrow phone Home it is mostly implied by alignment. On tablet and ledger surfaces it can become a faint structural guide.

### Surfaces

- Base canvas: warm-neutral or neutral-light field; dark mode uses a low-chroma near-black rather than a tinted cockpit theme.
- No universal cards.
- Active form group, invalid field ownership, offline/recovery notice, and selected Customize item may gain bounded local surfaces.
- Ledger uses actual column rules because boundaries improve scan accuracy; ordinary Home/form content does not inherit the ledger grid.

### Shape

Controls use restrained, medium-soft geometry, but rows and records remain primarily rectilinear. Rounded containers are not the identity. Icon buttons retain large targets while visible marks remain visually quiet.

## 4. Typography strategy

**PROPOSAL:** use a mature proportional sans for product-authored labels/navigation and a mature production monospace only for confirmed operational-data roles.

Operational mono roles include compact Flight identity, airport codes, clock/duration values, registration where useful for scan stability, and dense ledger cells. Remark, Crew, imported arbitrary Unicode, instructions, state/recovery messages, and general UI remain fallback-safe proportional text.

Numerical summaries use tabular figures rather than forcing whole summary blocks into monospace. The design explicitly avoids blanket mono, fixed per-character cells, whole-string Flight centering, negative tracking, and any dependency on unfinished T021 custom metrics.

**OPEN validation:** exact production families, resolved fallback, TextScaler behavior, Unicode stress, platform rasterization, and the Type drawing -> spacing -> kerning research gate remain unresolved.

## 5. Color and semantic-state strategy

The palette is neutral-dominant. One restrained brand hue may identify LogMate and high-level interactive intent, but it cannot simultaneously mean focus, selection, success, and sync state.

State expression is redundant:

- focus = boundary/underline geometry + focus semantics;
- invalid = local mark/boundary + explicit text;
- pending = progress/status text, never success color;
- saved locally = explicit local authority wording;
- synced = only after authoritative sync evidence;
- offline/degraded = status + icon/text, not hue alone;
- failure/unknown outcome = distinct wording and recovery affordance.

**PROPOSAL:** accent appears sparingly on primary action labels, current navigation, and selected controls, while operational data remains predominantly neutral.

**OPEN validation:** exact palette, light/dark transformations, native high-contrast, Web forced-colors, physical-device glare/night conditions, observer variation, and human salience.

## 6. Layout and spatial system

### Phone

A single start-edge datum establishes the reading axis. Major sections are separated by vertical rhythm and headings, not cards. Key numbers align to an end datum. Recent flights use compact strips with stable Date / Flight / Route / Block zones.

### Tablet / EFB PWA

The system becomes a two-field composition rather than simply stretching phone cards. A primary work field occupies roughly two-thirds of available width; a contextual field can hold recent records, totals, or supporting controls. Semantic order remains linear for accessibility/reflow.

### Landscape ledger

View Logbook remains dense and start-anchored. Confirmed column semantics and shared horizontal offsets are preserved. The unused right side is intentional expansion capacity, not a reason to stretch columns.

### Adaptive rule

When fit pressure occurs: intrinsic room -> redistribution -> row growth/wrap -> recomposition/detail transfer. The concept does not rescue geometry by shrinking operational type or abbreviating semantic jobs.

## 7. Interaction and recovery approach

Flight Strip Atlas makes state ownership spatially local. The object being edited, reordered, retried, or corrected remains visually identifiable through the transition.

- Add Flight groups fields by task sequence, but Save authority is separate from visual completion.
- Customize keeps item identity, proposed position, committed order, persistence result, and recovery distinct.
- Search/retrieval must keep query, status, results, selected record, and restored context connected.
- Retry is shown only when current authority makes it safe; unknown mutation outcome must not be disguised as ordinary failure.
- Navigation restoration should return users to the prior record/scroll/query context where product behavior supports it.

These are design contracts, not claims that current runtime already passes them.

## 8. Representative screen composition - Home

**Concept composition / not a runtime screenshot**

```text
LOGMATE                                      Settings
Pilot logbook companion

+ ADD FLIGHT                       VIEW LOGBOOK ->
---------------------------------------------------
Search flights, crew, airport, route...

28 DAYS                                  42+15
Block time                              compact datum

RECENT
22 SEP   7C 1203   ICN -> CJU             1+08
21 SEP   7C 1101   GMP -> CJU             1+05
20 SEP   7C 1302   CJU -> GMP             1+11
                         View recent ->

ACTIVITY              7D   [28D]   90D   CUSTOM
Flights  18     Block 42+15     Night 6+20

TOTALS
Block  4,821+35       Night  612+20       Inst  188+45
```

The hierarchy is deliberately editorial rather than dashboard-like. `28 DAYS` and its primary number form one visual sentence. Recent flights demonstrate the signature strip grammar. Activity controls are compact, and Totals remain an aligned readout rather than three decorative cards.

**Product boundary:** exact Home metrics/content are governed by current LogMate authority; this composition is a proposal and must not close OPEN product decisions.

## 9. Representative screen composition - Add Flight

```text
< Back                    ADD FLIGHT
22 Sep 2026

IDENTITY
Flight       [ 7C 1203 ]
Aircraft     [ B738    ]   Registration [ HLxxxx ]

ROUTE
Departure    [ ICN ]  ----------------->  [ CJU ] Arrival

TIME
Ramp Out     [ 08:10 ]        Ramp In      [ 09:18 ]
Block        [ 1+08  ]
              Show operational times v

COUNTS
Takeoffs       -  1  +        Landings       -  1  +

CREW / REMARK
Crew         [ ... ]
Remark       [ ... arbitrary Unicode ... ]

                                            SAVE
```

The form is not a stack of cards. Identity, Route, Time, Counts, and Crew/Remark are task bands separated by spacing and local rules. Focus/validation surfaces appear only around the owning field or band. Compact/expanded Time remains compatible with the current product direction, while persistence semantics remain OPEN until the real ledger/repository exists.

## 10. Representative screen composition - View Logbook

```text
LOGMATE / VIEW LOGBOOK                         Customize
Date    Type   Reg     Flight   DEP ARR   Block Night Inst  Remark
------------------------------------------------------------------
22 SEP  B738   HLxxxx  7C1203   ICN CJU    1+08  0+00 0+00  ...
21 SEP  B738   HLxxxx  7C1101   GMP CJU    1+05  0+42 0+00  ...
20 SEP  B738   HLxxxx  7C1302   CJU GMP    1+11  0+00 0+00  ...
...
------------------------------------------------------------------
Page Total                                15+42  3+10 1+15
Previous Total                         4,805+53 609+10 187+30
New Total                              4,821+35 612+20 188+45
```

This surface intentionally becomes more ruled and dense than Home. Header/body/totals share column boundaries and horizontal offset. Weight and separators establish hierarchy; New Total does not receive a celebratory fill. The ledger remains start-anchored with expansion room to the right, consistent with the current LogMate contract.

## 11. Native + tablet/EFB PWA adaptive approach

The concept uses one semantic composition model with platform adapters, not pixel-identical screens.

- Native phone: portrait Home/Add Flight; View Logbook follows confirmed landscape behavior.
- Tablet/EFB PWA: persistent wider work field may expose context alongside primary content, but no desktop-only semantic dependency is introduced.
- Pointer/keyboard on PWA: visible focus and non-drag alternatives are first-class.
- Touch: interactive target may be larger than visible mark.
- Offline: core work remains visually available; cloud/sync status is secondary and explicit.
- Install/update/background behavior is not assumed from visual design and requires Web/PWA runtime evidence.

## 12. Accessibility and content semantics

Product-authored UI remains English-only. User/source text is not forced to English and arbitrary-script Remark/source values must survive rendering.

The content system follows object -> state -> action -> consequence -> recovery. Labels do not pretend that presentation-shell actions are persisted. Visible meaning and accessible name/role/state/action must remain aligned.

The design does not claim WCAG conformance, AT interoperability, pilot comprehension, or workload performance from static composition. Those require implementation and representative evidence.

## 13. Canonical research basis

High-value Design Studio routes used by this proposal:

- `research/STATIC_RESEARCH_SYNTHESIS_EXTERNAL_ADVISORY_20260921.md` - preserve product truth before appearance; evidence boundaries.
- `research/EXTERNAL_ADVISORY_CLAIM_LEDGER_20260921.md` - bounded Type/Color/Layout/Interaction/Web/Content/UX claims.
- `research/EXTERNAL_ADVISORY_PACKAGE_TRACEABILITY_AUDIT_20260921.md` - prevents static evidence from being promoted to runtime/device/AT/FIELD/human PASS.
- `case-studies/logmate/DESIGN_CORRIDOR_20260919.md` - exact/calm/professional/direct corridor; no card-everything, cockpit mimicry, blanket mono, or color-only state.
- `research/type/T084-logmate-home-static-to-runtime-type-transfer.md`
- `research/color/C115-logmate-home-static-to-runtime-salience-transfer.md`
- `research/interaction/I102-logmate-home-static-shell-runtime-authority-transfer.md`
- `research/layout/L106-logmate-home-white-canvas-reflow-transfer.md`
- `research/web/W115-logmate-home-first-production-transfer-plan.md`
- `research/content/CD121-logmate-home-canonical-string-runtime-transfer.md`

## 14. Difference from earlier Design Studio candidates

This candidate is **not** a Candidate 05/07 restyle and does not use Candidate 01 from the separate visual-candidate archive as a generation source. Its identity is the cross-surface **record-strip + datum** grammar: the same operational reading relationship appears as a calm summary on Home, a task sequence in Add Flight, and a calibrated row system in View Logbook.

It deliberately rejects a persistent premium rail, instrument-panel metaphor, universal card shell, and ornamental aviation symbolism. The concept is intended to remain recognizable even if the eventual production palette or font family changes.

## 15. Trade-offs and risks

1. **Risk - too austere:** low-chrome structure may feel unfinished if spacing/type execution is weak. Validation must test whether users perceive clear grouping without card containers.
2. **Risk - false operational association:** the term/grammar `strip` must not imply ATC flight-progress-strip semantics or official airline-system authority. Product copy should never use that metaphor unless independently justified.
3. **Risk - dense mono overuse:** operational roles can expand until arbitrary content is incorrectly forced into mono. Role ownership must remain explicit.
4. **Risk - tablet overcomposition:** a two-field EFB layout may tempt product teams to expose extra information merely because space exists. Semantic priority must control expansion.
5. **Risk - visual continuity mistaken for persistence:** repeated strip identity must never imply a save/sync state that the runtime has not established.

## 16. OPEN validation plan

### Runtime
- exact resolved proportional/mono families and fallback;
- TextScaler and long/Unicode strings in actual widgets;
- Home reflow at narrow/wide/SafeArea states;
- Add Flight focus, validation, keyboard and save-authority states;
- View Logbook shared offsets, sticky header, scrolling/snap, orientation restoration;
- route/history/focus restoration and recovery-state injection.

### Device / platform transfer
- iOS and Android native rendering;
- served PWA on target tablet/EFB class;
- independent browser engine where materially supported;
- physical touch/pointer/keyboard target behavior;
- light/dark and supported high-contrast/forced-color behavior.

### AT
- screen-reader order and accessible names/roles/states/actions;
- focus visibility/not-obscured;
- non-drag reorder path;
- status/recovery announcement behavior.

### FIELD performance
- no FIELD claim from static work or synthetic tooling; representative provenance-bearing RUM is required for FIELD LCP/INP/CLS claims.

### Human / professional workflow
- representative pilots: scan accuracy, Add Flight completion, paper-transcription support, error recovery, discoverability, trust, workload;
- compare low-chrome grouping against a bounded alternative rather than asking preference alone;
- no simulated human PASS.

## 17. Candidate verdict

**STATIC DESIGN CANDIDATE - READY FOR PORTFOLIO REVIEW, NOT PRODUCTION PASS.**

Flight Strip Atlas provides a materially distinct whole-product visual thesis compatible with current LogMate contracts and Design Studio evidence boundaries. Its strongest hypothesis is that identity can come from repeated operational alignment and record continuity rather than decorative aviation styling or card-based dashboards. The next evidence step is implementation-grade rendering and adaptive/state stress, followed by device/AT/human validation where claims require it.
