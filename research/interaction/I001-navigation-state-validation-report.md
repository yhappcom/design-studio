# I001 Validation Report — Navigation/State Running Specimen

Status: **PRACTICE + CRITIQUE / FAILURE → REVISION → RE-PROOF COMPLETE FOR THE CONTROLLED SPECIMEN**  
Owner: Layout, Spatial & Interaction Specialist  
Canonical research being validated: `research/interaction/I001-navigation-history-focus-restoration-interruption.md` and `research/interaction/015-directness-state-modes-reversibility.md`

This report records an executable validation cycle. It does **not** promote Navigation / task-flow integration to PASS because assistive-technology testing, real product/browser routing, cross-browser/device evidence, localization/fallback stress, real network behavior, and human observation remain open.

## Objective

Convert the I001 navigation-state model from a source-grounded framework into a running specimen that can expose state-contract failures.

The controlled scenario covers:

- Records list → detail → edit;
- top-level Records / Reports switching;
- hierarchy `Up`;
- browser/session-history `Back` and `Forward`;
- direct/deep-link style detail entry;
- dirty edit state and interruption;
- modal discard confirmation and `Escape`;
- focus placement and restoration;
- asynchronous save: pending → failed → retry → saved;
- workspace resumption with object identity.

The goal is not to prove one universal navigation architecture. It is to test whether I001's distinctions are operational enough to catch defects before a real project ships.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md`;
  - `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`;
  - Type T003 checkpoint in `progress/TYPE_STATUS.md`.
- Reusable finding:
  - real renderer/metric behavior can change advance, wrapping, row height, and compact geometry even when source metrics appear stable;
  - fallback and text growth can therefore alter navigation controls and spatial orientation.
- Replication / challenge / transfer opportunity:
  - rerun the specimen with fallback fonts, Korean/Latin mixed labels, long titles, enlarged text, and narrow containers.
- Dependency / overlap:
  - this controlled specimen intentionally does not claim Type stability; Type remains the owner of font/fallback/rendering evidence.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md`;
  - `research/color/C001-web-color-user-override-resilience.md`;
  - C002 semantic role/token checkpoint in `progress/COLOR_STATUS.md`.
- Reusable finding:
  - state semantics must precede Color encoding;
  - authored fills, shadows, outlines, and colors can be replaced or removed in forced-color conditions;
  - semantic roles and literal colors are separate layers.
- Replication / challenge / transfer opportunity:
  - run current-location, focus, invalid/failed, pending, and selected states under forced colors, grayscale, light/dark, and semantic-token substitutions.
- Dependency / overlap:
  - this specimen uses structure/text/focus semantics first and does not claim forced-color PASS.

### Layout / Interaction
- Evidence checked:
  - `research/interaction/007-interaction-agency-feedback-errors.md`;
  - `research/interaction/015-directness-state-modes-reversibility.md`;
  - `research/interaction/I001-navigation-history-focus-restoration-interruption.md`;
  - `research/layout/L002-whitespace-density-spatial-rhythm.md`.
- Reusable finding:
  - action, destination, state, history, hierarchy, focus, commitment, and recovery must not be collapsed;
  - spatial simplification can create temporal/navigation cost.
- Replication / challenge / transfer opportunity:
  - this report directly stress-tests those distinctions in a running state model.
- Dependency / overlap:
  - primary ownership remains Interaction; the HTML is an evidence instrument, not a Web Design page-system conclusion.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`;
  - `research/web/README.md`.
- Reusable finding:
  - Web Design owns complete browser/page-system integration and real browser/device validation.
- Implementation / application validation opportunity:
  - transfer the same assertions into a real router, real URLs, native/custom controls, actual server/network conditions, browser Back/Forward, page refresh, zoom/reflow, and assistive technology.
- Dependency / overlap:
  - no substantive `W###` study was available at this checkpoint, so this is an Interaction-owned independent validation, not Web evidence.

### Other / cross-cutting / future specialist
- Evidence checked:
  - existing shared accessibility focus/reflow evidence referenced by I001/Study 015;
  - the controlled Chromium DOM/focus/history behavior recorded here.
- Reusable finding:
  - route focus, modal focus restoration, live status, and recovery actions require explicit semantic contracts.
- Dependency / overlap:
  - screen-reader announcement quality and human resumption performance remain untested.

### Overlap decision
- **INDEPENDENT VALIDATION + FAILURE ANALYSIS + TRANSFER PREPARATION**.
- Why:
  - I001 had a project-decision framework but lacked running proof. The purpose here is to find where the model or specimen breaks under actual state transitions before handing the same contract to Web Design or a project team.

---

## Evidence class and test environment

### Actual evidence produced

- self-contained HTML/JavaScript state specimen;
- real Chromium DOM and focus behavior;
- real session-history state traversal using `history.pushState`, `history.replaceState`, `Back`, and `Forward` within a same-document hash route;
- actual native `<dialog>` behavior and `Escape` handling;
- asynchronous pending/failure/retry/success transitions;
- programmatic assertions through Playwright;
- explicit failure → revision → re-proof cycle.

### Environment

- headless Chromium available in the Design Studio execution environment;
- Playwright Python automation;
- same-document `about:blank#...` hash routing because this environment blocks browser access to localhost/network origins.

### Scope limit

The environment restriction is **not** product evidence. Same-document history is useful for state-contract validation, but it does not prove behavior of:

- a production router;
- real network/document navigations;
- Safari, Firefox, Android WebView, iOS WebKit, or other engines;
- page reload/process restoration;
- assistive technology;
- framework-specific history abstractions.

---

# Cycle 1 — baseline execution and failures

The first executable version modeled Records/Reports, detail/edit, modal dismissal, async save, and session history.

## Failure F1 — route focus landed on `Up`, not on route context

Observed after list → detail and detail → edit:

- active element became the `Up` button;
- the newly entered route's heading was not the focus target.

### Why this matters

The user receives an actionable control before being given explicit programmatic route context. In a complex SPA, that can weaken orientation after navigation.

### Revision

Add an explicit route-focus policy: after route transition, programmatically focus the route heading (`tabindex=-1`).

---

## Failure F2 — browser Back from dirty edit had no explicit draft policy

Baseline behavior:

- Back moved edit → detail;
- the in-memory `dirty` flag remained, but the edited field value was not preserved in a restorable draft model;
- returning to edit could silently reconstruct the original value.

### Why this matters

“Dirty” is not a useful state unless the product defines what data survives navigation/interruption.

### Revision

For this specimen, choose one explicit policy:

> browser/history traversal may leave the edit route, but the local draft is preserved and restored until the user saves or explicitly discards it.

This is a **tested specimen policy, not a universal studio rule**. Other projects may choose blocking confirmation, autosave, transaction rollback, or irreversible-step prevention depending on consequence and data model.

---

## Failure F3 — save success status was erased by destination render

Baseline behavior:

- async save completed;
- route changed back to detail;
- route render cleared the live status node;
- `Saved.` disappeared before it could function as stable success feedback.

### Revision

Treat status communication as part of the transition contract. The destination render must not automatically erase a success message that is still semantically relevant.

---

## Failure F4 — top-level restoration stored only view name, not object identity

Baseline behavior:

1. Records → `Record A` detail;
2. switch to Reports;
3. return to Records;
4. detail route restored without `Record A` identity.

### Why this matters

A workspace is not identified by screen type alone. Restoration may require the semantic object, filters, selection, scroll, query, and other context.

### Revision

Store a top-level resumable location as at least:

`{ view, object identity }`

and expand it only when the project requires more context.

---

# Cycle 2 — second-order problems found after the first revision

The first correction fixed the obvious state losses but exposed two interaction/accessibility problems.

## Failure F5 — focusing the heading could skip a preceding `Up` control in forward Tab order

The DOM originally placed:

`Up button → heading → content`

but route transition programmatically focused the heading.

Result: pressing `Tab` from the heading moved forward into later content, leaving the preceding Up button behind unless the user used `Shift+Tab`.

### Revision

For the controlled specimen, align focus policy and DOM order:

`heading → Up button → route content`

The important transferable lesson is not that every real product must visually place Up below a heading. It is:

> programmatic route focus and sequential DOM/focus order must be designed together.

A production UI may use CSS/layout to present a different visual arrangement while preserving a coherent accessibility order.

---

## Failure F6 — recovery action was placed inside `role="status"`

The first async-failure implementation appended an interactive Retry button into the live status container.

### Why this matters

A status message and a recovery action are different semantic objects. Combining them can create confusing live-region behavior and makes the feedback architecture less explicit.

### Revision

Separate:

- non-interactive live status text;
- actionable recovery control.

After failure:

- status = `Save failed. Check connection and retry.`;
- adjacent action = `Retry`;
- focus is explicitly moved to Retry in this controlled flow.

---

## Failure F7 — workspace resume state could become stale after history traversal

The initial resume map updated on explicit pushes but not on every history/popstate render. Therefore the resumable route could disagree with the route currently shown after Back/Forward or deep-link-style entry.

### Revision

Update resumable top-level location from the actual rendered semantic route, not only from explicit navigation commands.

---

# Cycle 3 — final controlled assertions

After revision, the Playwright harness executed 14 explicit checks.

| # | Assertion | Result |
| --- | --- | --- |
| 1 | keyboard activation list → detail focuses route heading | PASS |
| 2 | `Up` is immediately reachable by forward Tab after focused detail heading | PASS |
| 3 | keyboard activation detail → edit focuses edit heading | PASS |
| 4 | edit `Up` is immediately reachable after heading | PASS |
| 5 | discard modal opens with focus inside modal | PASS |
| 6 | `Escape` closes modal and restores invoker focus | PASS |
| 7 | browser Back from dirty edit preserves draft and emits preservation status | PASS |
| 8 | top-level workspace switch/resume preserves exact `Record A` identity | PASS |
| 9 | returning to edit restores draft value | PASS |
| 10 | save failure separates live status from Retry action and focuses Retry | PASS |
| 11 | retry success retains `Saved.` status and focuses destination heading | PASS |
| 12 | deep-link-style detail entry establishes destination identity and heading focus | PASS |
| 13 | `Up` traverses product hierarchy detail → list | PASS |
| 14 | browser Back traverses session history list → prior deep-linked detail | PASS |

Controlled result: **14 / 14 assertions PASS after the failure/revision cycle.**

This is stronger evidence than the prior static/state-matrix work, but it is still **controlled prototype evidence**, not production or human-study evidence.

---

# What the experiment changed in the studio model

## 1. Restorable navigation state must include semantic identity

`detail` is not enough. The state must answer **detail of what?**

A project may additionally need:

- filter/query;
- scroll anchor;
- selected subtab;
- sort order;
- draft identity;
- cursor/selection;
- pagination;
- pending transaction identity.

Do not save all of these by default. Save the minimum state required for correct resumption.

## 2. Focus restoration is not a single rule

The controlled specimen now distinguishes:

- route-entry focus;
- modal-entry focus;
- modal-dismissal focus restoration;
- async-failure recovery focus;
- destination focus after successful commitment.

“Put focus somewhere sensible” is not a sufficient specification.

## 3. DOM order is part of route-focus design

A correct target can still create a poor keyboard path if surrounding controls appear before it in DOM order.

Therefore route-focus validation must inspect **the next and previous sequential focus targets**, not only the focused node itself.

## 4. History traversal and hierarchy traversal remain distinct in executable behavior

The deep-link scenario demonstrates the difference:

- `Up`: detail → product parent list;
- browser Back: list → prior session-history detail entry.

The two controls can point to different destinations without contradiction because they answer different questions.

## 5. Dirty-state navigation requires a data-lifecycle policy

The specimen's preserved local draft is one valid option. The appropriate project choice depends on:

- consequence of data loss;
- privacy/security;
- local persistence capacity;
- multi-device conflict;
- legal/financial commitment;
- whether an incomplete draft is safe to resume;
- expiry and invalidation rules.

## 6. Status and recovery action are separate channels

A passive message can announce state without taking focus. A recovery action can be separately focusable and operable.

This gives projects more control over interruption cost than putting every error into a modal or every action into a live region.

---

# Project Readiness Test

## When should this knowledge be applied?

Use it for products with any combination of:

- list/detail/edit flows;
- nested navigation;
- deep links;
- browser/app Back behavior;
- top-level workspaces/tabs;
- modals/sheets/popovers;
- unsaved work;
- async save/sync;
- interruption/resumption;
- keyboard/focus requirements.

## When should it not be over-applied?

A short one-screen utility with no nested state, no async mutation, and no resumable work does not need a complex restoration architecture.

Do not preserve state merely because it is technically possible. Stale, unsafe, private, or misleading state should be reset.

## Project information required

Before specifying navigation/restoration, collect:

- route hierarchy and top-level destinations;
- object identities and deep-link requirements;
- data commitment model;
- dirty-draft policy;
- session/history expectations;
- modal/transient layers;
- keyboard/focus requirements;
- interruption/background lifecycle;
- security/privacy expiry constraints;
- localization/text-growth constraints;
- target platforms and browser/router frameworks.

## Concrete decisions this can change

- whether a control is Back, Up, Close, or top-level switch;
- what state is saved/restored;
- whether dirty edits block departure, autosave, or preserve a draft;
- where focus goes after route/modal/async transitions;
- whether status steals focus;
- how deep-link orientation is reconstructed;
- whether top-level destinations maintain independent work context;
- what browser/device validation is required.

## Failure conditions

Reject or rework when:

- workspace restoration loses the semantic object;
- Back and Up are visually interchangeable but semantically different with no clear model;
- route focus skips important controls in normal keyboard order;
- modal dismissal loses the invoker without a valid replacement target;
- dirty work disappears on history traversal without an explicit policy;
- success/failure status vanishes during rerender;
- a live status container contains unrelated interactive content;
- deep-link entry depends on unavailable previous-screen context;
- restoration revives stale or unsafe task state;
- async failure leaves the user with no focused/visible recovery path.

## Validation plan for a real project

At minimum, rerun equivalent tests using:

1. the actual app/router;
2. real persistent object IDs;
3. real network latency/failure;
4. keyboard-only operation;
5. browser/app Back and Forward;
6. direct/deep-link entry;
7. actual modal/sheet implementation;
8. page refresh/process restart where relevant;
9. assistive technology;
10. localized/enlarged labels;
11. target browser/device matrix;
12. human interruption/resumption tasks when resumption cost is important.

---

## OPEN

1. Run the same contract with a real URL/router rather than same-document hash history.
2. Test screen-reader announcement behavior for route heading, status, modal, and retry action.
3. Test real network abort, timeout, duplicate submission, and conflict resolution.
4. Compare draft-preservation policy against confirmation-before-leave and autosave alternatives.
5. Validate top-level independent stacks with deeper stacks and multiple object identities.
6. Add scroll/filter/search/pagination restoration where task evidence justifies it.
7. Stress with T001/T003 Type conditions: fallback font, Korean/Latin mixed labels, enlarged text, compact density.
8. Stress with C001/C002 Color conditions: forced colors, theme substitution, semantic-role mapping, focus/error/status resilience.
9. Hand the assertion matrix to Web Design for real browser/page-system transfer once substantive `W###` work begins.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - route titles, Back/Up/Close labels, and top-level navigation are part of state orientation; wrapping/fallback can therefore become navigation failures, not merely visual differences.
- Canonical section:
  - `Cycle 3`, `Project Readiness Test`, and the Type section of `RELATED DOMAIN CHECK`.
- Confirmation / contradiction / transfer note:
  - confirms the need expressed by T001/T003 to test actual rendered metrics in navigation contexts.
- Scope limit:
  - this experiment did not vary fonts or text size.

### Color
- Useful finding/context:
  - state meaning is carried structurally before visual encoding; status and recovery action are separate semantic channels.
- Canonical section:
  - `Failure F6` and `What the experiment changed`.
- Confirmation / contradiction / transfer note:
  - supports C001/C002 separation of semantics from literal color roles.
- Scope limit:
  - forced colors, theme substitution and contrast were not tested.

### Layout / Interaction
- Useful finding/context:
  - I001's distinction among location/history/hierarchy/focus/work state produced concrete defects when omitted.
- Canonical section:
  - full failure→revision cycle.
- Confirmation / contradiction / transfer note:
  - confirms the usefulness of explicit navigation-state modeling while adding a new constraint: route focus and DOM order must be designed jointly.
- Scope limit:
  - no human performance study or cross-platform validation yet.

### Web Design
- Useful finding/context:
  - reusable 14-assertion matrix and reproducible specimen for Back/Up/deep link/focus/modal/draft/async/workspace restoration.
- Web application / validation consequence:
  - reproduce with a real router, URL history, page architecture, native/custom controls, browser/device matrix and assistive technology.
- Confirmation / contradiction / transfer note:
  - current evidence is Chromium controlled-prototype evidence, not Web canonical evidence.
- Scope limit:
  - no `W###` result was available at this checkpoint and no real network origin was used.

---

## Status implication

This validation materially strengthens the Interaction Foundation evidence:

- `State / modes / reversibility / directness`: running failure/recovery proof now exists for the controlled specimen;
- `Navigation / task-flow integration`: running Back/Up/deep-link/focus/workspace/draft behavior now exists and has undergone failure → revision → re-proof.

Recommended status for Navigation / task-flow integration: **CRITIQUE**, not PASS.

PASS remains blocked by real platform/browser routing, assistive technology, broader async/network cases, cross-device/input validation, and representative human resumption evidence.
