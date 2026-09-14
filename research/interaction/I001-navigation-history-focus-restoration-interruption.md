# I001 — Navigation as State: History, Focus, Restoration, and Interruption Recovery

Status: **FOUNDATION STUDY / PROJECT-DECISION FRAMEWORK — running multi-input prototype and observed resumption validation still required before PASS.**

Owner: Layout, Spatial & Interaction Specialist  
Canonical path: `research/interaction/`  
Primary purpose: make navigation decisions project-usable by separating location, traversal history, hierarchy, focus, transient layers, task state, and restoration.

## Question

How should a product model navigation so that users can answer **where am I, how did I get here, what happens if I go back, what closes versus navigates, where will focus return, and can I resume after interruption** without relying on platform folklore or visually similar controls that have different semantics?

This study extends:

- `research/interaction/007-interaction-agency-feedback-errors.md`
- `research/interaction/015-directness-state-modes-reversibility.md`
- `research/layout/006-grid-composition-hierarchy.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`

Study 007 established orientation, agency and predictable navigation as Foundation requirements. Study 015 established state, modes, reversibility, commitment and recovery. I001 treats navigation itself as a user-facing state system and adds history, hierarchy, deep-link entry, focus restoration and interruption recovery.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked:
  - `progress/TYPE_STATUS.md`
  - `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`
  - `research/type/009-typography-as-information-architecture.md`
- Reusable finding:
  - label width, fallback metrics, localization and text enlargement can change navigation geometry, wrapping, row height and control placement;
  - hierarchy must survive font substitution and reflow rather than depend on nominal strings.
- Replication / challenge / transfer opportunity:
  - test navigation titles, breadcrumbs, tab labels, Back/Close controls and restoration targets under preferred/fallback fonts, Korean/Latin labels and enlarged text.
- Dependency / overlap:
  - Type owns font metrics and typographic hierarchy; Interaction owns what a navigation control means and where the user should return.

### Color
- Evidence checked:
  - `progress/COLOR_STATUS.md`
  - `research/color/C001-web-color-user-override-resilience.md`
  - `research/color/008-color-luminance-contrast-hierarchy.md`
- Reusable finding:
  - forced-colors and user-agent palette substitution can remove or replace fill, shadow, authored border and other visual channels;
  - selected/current/focus states therefore cannot depend on hue or tint alone.
- Replication / challenge / transfer opportunity:
  - validate current-location, focus and selected-navigation cues after color replacement while preserving the same navigation semantics.
- Dependency / overlap:
  - Color owns visual color encoding; Interaction owns current-location, focus, selected, pending and navigation semantics.

### Layout / Interaction
- Evidence checked:
  - Studies `007`, `015`, Layout Studies `006`, `014`, `L001`, `L002`, and `progress/LAYOUT_STATUS.md`.
- Reusable finding:
  - actions, destinations and states should not be conflated;
  - responsive systems preserve semantic relationships, not coordinates;
  - progressive disclosure exchanges spatial density for navigation/interaction cost;
  - user-facing states require explicit transition and recovery models.
- Replication / challenge / transfer opportunity:
  - I001 extends state modeling from local controls to product-level navigation, restoration and interruption.
- Dependency / overlap:
  - spatial location cues such as sidebars, tabs and breadcrumbs need Layout validation, but the behavioral contract remains Interaction-owned.

### Web Design
- Evidence checked:
  - `progress/WEB_STATUS.md`
  - `research/web/README.md`
  - WHATWG HTML session-history/navigation APIs as a Web-platform source.
- Reusable finding:
  - Web Design owns complete web page-system application and actual browser validation.
- Implementation / application validation opportunity:
  - browser Back/Forward, `pushState`/`replaceState`, scroll restoration, focus after same-document navigation, deep-link entry, native history, keyboard traversal and SPA route changes.
- Dependency / overlap:
  - no substantive `W###` study was available at the start of I001; this study defines an Interaction→Web validation contract rather than claiming current browser implementation proof.

### Other / Cross-cutting / Future Specialist
- Evidence checked:
  - Apple Human Interface Guidelines for standard Back/Close behavior;
  - Android navigation principles/back-stack/state-restoration guidance;
  - WHATWG HTML Living Standard navigation/session history;
  - W3C WCAG 2.2 and WAI-ARIA APG focus/dialog guidance;
  - interruption/resumption literature from Human Factors and cognitive psychology.
- Reusable finding:
  - predictable traversal, visible focus, preserved orientation and resumable task context are human-factors and accessibility requirements, not decoration.
- Dependency / overlap:
  - empirical resumption claims require task testing; specification conformance alone does not prove cognitive recovery quality.

### Overlap decision
- Reuse / replication / extension / contradiction review / method comparison / transfer validation / project-specific study:
  - **EXTENSION + METHOD COMPARISON + TRANSFER VALIDATION PREPARATION**.
- Why:
  - existing Interaction research explicitly leaves navigation/history/restoration OPEN. Platform models differ in details, so the useful studio result is a cross-platform semantic model plus platform-specific validation obligations rather than one universal Back implementation.

---

# 1. SOURCE — navigation is state, not merely a visual transition

Android's current Navigation guidance models navigation state as a back stack of destinations. Forward navigation pushes a destination and Back pops the current destination to reveal the previous one. Its newer Navigation 3 guidance explicitly describes a back stack as state that can be saved so users can leave and later return to the content they were viewing.

Primary sources:

- https://developer.android.com/guide/navigation
- https://developer.android.com/guide/navigation/principles
- https://developer.android.com/guide/navigation/navigation-3/basics
- https://developer.android.com/guide/navigation/navigation-3/save-state

The WHATWG HTML Living Standard likewise defines session-history entries and traversal. `history.back()` traverses one step backward, `history.forward()` moves forward, and `pushState()` / `replaceState()` create or modify history entries. It separately exposes scroll-restoration behavior and newer Navigation API concepts such as push, replace, reload and traverse.

Primary source:

- https://html.spec.whatwg.org/multipage/nav-history-apis.html

### SYNTHESIS

Navigation has at least two observable dimensions:

1. **current location** — what destination/context is active now;
2. **traversal history** — what sequence can be reversed or revisited.

These are related but not identical to the product's information hierarchy.

### STUDIO JUDGMENT

Before drawing navigation chrome, model the state first.

For every destination ask:

- What uniquely identifies this location?
- What parent/hierarchy does it belong to?
- What history entry, if any, should this transition create?
- What state should survive leaving and returning?
- What should Back do from here?
- What should Close/Escape do if this is transient?
- What should happen when the user enters here from a deep link with no prior in-product trail?

A navigation animation is evidence of transition. It is not the navigation model itself.

---

# 2. SOURCE — Back, Up, and Close can have different semantics

Apple's Human Interface Guidelines distinguish standard Back and Close controls: Back retraces navigation through a hierarchy of information, while Close dismisses a modal view.

Primary source:

- https://developer.apple.com/design/human-interface-guidelines/toolbars

Android distinguishes traversal history and hierarchy more explicitly in deep-link cases. Within an app task, Up and Back can behave identically, but a deep-linked destination creates an important difference: Up proceeds through the app's hierarchy/simulated app task, while Back can return to the external app that launched the deep link.

Primary source:

- https://developer.android.com/guide/navigation/principles

The browser Back command is a history traversal operation, not a request to navigate to a product-defined parent page.

Primary source:

- https://html.spec.whatwg.org/multipage/nav-history-apis.html

### SYNTHESIS

Controls that visually point “left” can represent different transitions:

- **Back / history traversal** — reverse the user's traversal history;
- **Up / hierarchy traversal** — move to a structural parent;
- **Close / dismiss** — end a transient layer or modal task and reveal the underlying context;
- **top-level destination switch** — change application area, often preserving independent task state;
- **Home / start** — go to a designated root, not necessarily the previous destination.

### STUDIO JUDGMENT

Do not label all of these “back.”

A project specification should name the semantic operation first, then use the platform-appropriate presentation.

**Failure example:** a modal editor displays a Back chevron that actually discards the modal and returns to its invoker. The control visually suggests traversal history while behaving as dismissal.

---

# 3. SOURCE — deep links prove that history and hierarchy are different

Android's navigation principles explicitly discuss deep linking as a path that can enter a destination without the user's manual in-app traversal. The system can construct a simulated app back stack for hierarchical Up navigation while Back may return to the external app/task that originated the deep link.

Source:

- https://developer.android.com/guide/navigation/principles

On the web, a user may open a URL directly from an external source. The browser's previous session-history entry can belong to another site; product hierarchy is therefore not the same thing as browser history.

Source:

- https://html.spec.whatwg.org/multipage/nav-history-apis.html

### SYNTHESIS

A location can be valid even when no internal route preceded it.

### STUDIO JUDGMENT — deep-link readiness test

Every meaningful destination should be reviewed under two entry modes:

1. **in-context entry** — user arrived through the product's normal navigation;
2. **context-poor entry** — user arrived directly via deep link, notification, search result, bookmark, external app, shared URL, restored state or OS handoff.

Ask whether the direct entrant can still determine:

- what object/page/task they are viewing;
- which larger area it belongs to;
- what action is available;
- how to reach a meaningful parent/root;
- what Back will do on the current platform.

Do not fake traversal history merely to make a Back button appear predictable.

---

# 4. Navigation state has more layers than destination ID

A robust navigation design separates at least these user-facing layers.

## 4.1 Semantic location state

The current domain object and product area.

Examples:

- Portfolio → CONY → Distribution detail;
- Logbook → Flight record → Edit;
- Settings → Appearance.

## 4.2 Traversal-history state

The chronological/reversible path available through Back/Forward or equivalent history traversal.

## 4.3 Hierarchy state

The structural parent/child relationship independent of how the user arrived.

## 4.4 Task/work state

Incomplete work that may need to survive navigation or interruption:

- form draft;
- selection set;
- filter query;
- unsaved edit;
- pending upload;
- multi-step progress.

## 4.5 Presentation state

Context that may be cheap to lose technically but expensive to lose cognitively:

- scroll position;
- expanded/collapsed groups;
- sort order;
- filters;
- pagination position;
- table column configuration;
- zoom or pane selection where product-controlled.

## 4.6 Focus/selection state

Where keyboard/assistive-technology interaction resumes and which item remains selected.

## 4.7 Transient-layer state

Modal, popover, sheet, menu, disclosure, temporary mode or overlay.

## 4.8 Data/commitment state

Whether a change is preview, draft, locally persisted, queued, remotely confirmed, failed or externally committed, extending Study 015.

### STUDIO JUDGMENT

Do not write “preserve state” as a single requirement. State is plural.

A product may intentionally preserve filter + scroll + selected top-level destination while discarding a temporary tooltip and blocking restoration of an expired financial confirmation step.

---

# 5. SOURCE — focus is part of navigation continuity

WAI-ARIA Authoring Practices describes predictable keyboard focus as fundamental. It notes that when the focused element is removed or hidden, authors need to move focus logically; otherwise browser focus can effectively fall back to the document body and the user loses their place.

Primary guidance:

- https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/

For modal dialogs, APG states that focus moves inside the dialog when it opens. When the dialog closes, focus normally returns to the element that invoked it, unless that element no longer exists or the workflow makes another target more logical.

Primary guidance:

- https://www.w3.org/WAI/ARIA/apg/patterns/dialog-modal/

WCAG 2.2 also requires visible keyboard focus and, at AA, that author-created content not entirely obscure the focused component.

Primary sources:

- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/

### SYNTHESIS

For keyboard and assistive-technology users, a navigation transition is incomplete until the new focus context is sensible and perceivable.

### STUDIO JUDGMENT — focus restoration contract

For every transition that creates or removes interactive UI, define:

- initial focus target;
- visible focus treatment;
- whether focus remains inside a transient layer;
- dismissal focus target;
- fallback target if the invoker was deleted/hidden;
- scroll behavior required to expose the focused target;
- whether selection should persist separately from focus.

Do not move focus merely to announce every visual change. Status communication and focus movement have different interruption costs.

---

# 6. Focus, selection, current location and active state are not synonyms

WAI-ARIA guidance explicitly separates keyboard focus from selection. A selected tab, row or item can remain selected after focus moves elsewhere.

Source:

- https://www.w3.org/WAI/ARIA/apg/practices/keyboard-interface/

### STUDIO JUDGMENT

A navigation system can expose several simultaneous states:

- current destination;
- selected object;
- keyboard focus;
- active/pending action;
- hovered object;
- expanded branch.

These states should not all be encoded by the same tint or outline.

This directly consumes Color C001: forced-colors or user-agent substitution may remove authored fills/shadows, so the semantic distinction must survive through structure, text, roles, programmatic state and appropriate redundant cues.

---

# 7. SOURCE — multiple top-level areas may need independent navigation state

Android's Navigation component supports multiple back stacks for patterns such as bottom navigation or navigation drawers so users can switch between top-level flows without necessarily losing their place in each flow.

Primary source:

- https://developer.android.com/guide/navigation/backstack/multi-back-stacks

### SYNTHESIS

Switching top-level areas and going Back are different operations.

### STUDIO JUDGMENT

For products with persistent top-level navigation, decide explicitly whether each area preserves:

- its own navigation depth;
- scroll/list position;
- filter/search state;
- selected object;
- draft work;
- transient layers.

Do not automatically reset every top-level area to its root on each switch, and do not preserve every stale detail forever. The preservation policy should reflect task continuity, data freshness, privacy/security and memory cost.

---

# 8. SOURCE — interruptions create measurable resumption costs

Interruption research repeatedly identifies **resumption lag**: time needed to reorient and continue a primary task after interruption.

Representative sources:

- Altmann EM, Trafton JG. *Memory for goals: an activation-based model*. Cognitive Science. 2002;26(1):39–83. DOI: 10.1016/S0364-0213(01)00058-1.
- Foroughi CK et al. *Individual differences in working-memory capacity and task resumption following interruptions*. Journal of Experimental Psychology: Learning, Memory, and Cognition. 2016. PMID: 26882286.
- Ratwani RM et al. *An eye movement analysis of the effect of interruption modality on primary task resumption*. Human Factors. 2010. PMID: 21077561.
- Westbrook et al./related electronic prescribing interruption work, including task-complexity findings: PMID: 20819867.
- Grundgeiger T et al. *Interruption management in the intensive care unit*. Journal of Experimental Psychology: Applied. 2010. PMID: 21198250.
- Sasangohar F et al. *Effects of Nested Interruptions on Task Resumption*. Human Factors. 2017. PMID: 28128985.

Across these lines of work, longer or more complex interruptions can increase resumption cost, and environmental/interface cues can help users recover the suspended task goal. Nested interruptions can further degrade resumption.

### Scope limit

These studies do not prove a universal UI pattern or a universal number of seconds. Many tasks were laboratory or safety-critical workflows. The transferable finding is that **resumption is cognitively costly and cue/context preservation can matter**.

### STUDIO JUDGMENT — interruption-resumption support

When a task is costly to reconstruct, preserve or expose useful cues such as:

- the object being edited;
- the last completed step;
- unsaved/draft state;
- selection and filter context;
- current section/step label;
- pending operation status;
- the next valid action;
- a safe review opportunity before high-cost commitment.

Do not preserve sensitive or obsolete state merely for convenience.

For high-risk work, “resume immediately” is not always the goal. Research on speed–accuracy trade-offs after interruptions shows that slower, more reflective resumption can reduce errors in some procedural tasks.

Representative source:

- Brumby DP et al. *Recovering from an interruption: investigating speed-accuracy trade-offs in task resumption behavior*. Journal of Experimental Psychology: Applied. 2013. PMID: 23795978.

---

# 9. Navigation restoration is a policy, not a technical default

## Preserve aggressively when

- users repeatedly switch between top-level work areas;
- task reconstruction is costly;
- content/data remains valid;
- comparison depends on returning to the same location;
- user intent is obvious and privacy/security risk is low.

## Restore cautiously or reset when

- stale data could cause a wrong decision;
- the state represents a completed/expired transaction;
- authentication/security context changed;
- the originating object was deleted;
- the user's previous action had an unresolved failure;
- restoring a transient layer would surprise or trap the user.

### STUDIO JUDGMENT

Separate three questions:

1. **Can this state be technically restored?**
2. **Would restoration help task continuity?**
3. **Is restoration still valid and safe?**

A yes to the first does not imply yes to the other two.

---

# 10. Unsaved work and navigation require an explicit commitment model

Study 015 distinguishes preview, local persistence, queued synchronization, remote confirmation and irreversible commitment.

Navigation adds a new question:

> What happens if the user leaves before the current work reaches its intended commitment state?

Possible policies:

- auto-save draft, then navigate;
- preserve local draft and indicate it on return;
- block navigation until required validation completes;
- allow navigation while async work continues with persistent status;
- request confirmation only when leaving would cause meaningful irreversible loss;
- discard ephemeral edits on explicit Cancel/Close.

### STUDIO JUDGMENT

Do not use a generic “Are you sure you want to leave?” alert as a substitute for deciding what the data lifecycle actually is.

Back, Close, route change, browser refresh, deep link and app interruption may all need the same underlying unsaved-work policy even if the presentation differs.

---

# 11. Navigation-state contract

For each significant destination or transient layer, document:

| Field | Question |
| --- | --- |
| Location key | What uniquely identifies the destination/context? |
| Parent | What is its structural parent, if any? |
| Entry modes | Normal traversal, deep link, notification, restore, external handoff? |
| History effect | Push, replace, traverse, none, platform-native behavior? |
| Back behavior | What does historical reversal do here? |
| Up behavior | Is there a meaningful hierarchy parent distinct from Back? |
| Close/Escape | What transient context ends, and what remains beneath it? |
| Top-level switch | Does this area keep an independent stack/state? |
| Draft/data state | What is preserved, committed, pending, failed or discarded? |
| Presentation state | Scroll, filters, sort, expansion, pagination, pane? |
| Focus on entry | Where should keyboard/AT focus land? |
| Focus on exit | Where should it return? What if that target no longer exists? |
| Status announcement | What changes need non-focus status communication? |
| Restore after interruption | What task cues must survive? |
| Expiration/invalidation | When is old state no longer safe to restore? |
| Accessibility path | Can keyboard/AT users traverse, dismiss and resume equivalently? |

This contract is a design artifact before it is an implementation artifact.

---

# 12. Project decision framework

## Use a history-first pattern when

- the user's main expectation is retracing recently visited content;
- the product is document/detail oriented;
- the arrival sequence matters more than parent hierarchy.

Examples: browser-like document exploration, detail drill-down, search result → detail → related detail.

## Use explicit hierarchical navigation when

- users need stable orientation independent of arrival path;
- parent structure is meaningful;
- deep-link entry is common;
- users may jump among siblings or nested categories.

Examples: settings hierarchies, asset/category management, structured administration.

## Use dismissible transient layers when

- the task is subordinate to the current context;
- the underlying object/context should remain conceptually present;
- completing/canceling the subtask returns to that context.

Examples: confirmation, quick edit, picker, auxiliary detail.

Do not use a modal merely because the implementation is convenient. If the task needs its own deep link, long-lived history, independent navigation, or large multi-step workflow, a full destination may be more coherent.

## Use multiple persistent top-level stacks when

- users frequently switch among major work areas;
- losing depth/context would create repeated reconstruction;
- each area has meaningful internal navigation.

Avoid preserving deep stacks when stale context is more harmful than reconstruction.

---

# 13. Failure modes

1. **Back-as-parent confusion** — Back always goes to a structural parent even when users expect chronological history.
2. **Close-as-back confusion** — modal dismissal is presented as hierarchical Back.
3. **Deep-link trap** — direct entrants see a Back control whose destination is meaningless or fabricated.
4. **History pollution** — transient filter toggles or internal state changes create excessive Back steps without user value.
5. **History erasure** — meaningful navigation is implemented as replace/reset, so users cannot retrace work.
6. **Focus loss** — closing/removing UI sends focus to the document body or an unrelated control.
7. **Focus/selection conflation** — selected navigation state is mistaken for keyboard focus.
8. **Color-only current location** — current tab/section becomes ambiguous under forced-colors or grayscale.
9. **State amnesia** — returning to a list loses filter, scroll and selected object despite comparison being the task.
10. **State fossilization** — old filters, stale records or expired transaction state are restored after they are no longer valid.
11. **Responsive semantic drift** — desktop sidebar and mobile compact navigation represent different destination structures because the design was transformed by component shape instead of semantics.
12. **Text-metric drift** — localized/fallback labels wrap and move navigation controls in ways that change grouping or obscure current location.
13. **Interruption cliff** — returning from an interruption provides no clue what was pending or what next action is safe.
14. **Immediate-resume hazard** — high-risk tasks encourage instant continuation when a short review/reorientation step would reduce error.

---

# 14. Controlled practice / validation matrix

I001 does not claim PASS until a running prototype or equivalent implementation tests at least the following scenarios.

## Scenario A — list → detail → edit → modal

Required checks:

- Back from detail returns to list with meaningful list context preserved;
- edit navigation has explicit unsaved-work policy;
- modal Close/Escape returns focus logically;
- deleting the invoking row provides a new logical focus target;
- browser/system Back does not conflict with modal dismissal semantics.

## Scenario B — deep link to detail

Required checks:

- current object and parent area are understandable without prior context;
- Back and Up/parent behavior are deliberately defined for each platform;
- no fake internal history is created merely to support a Back icon;
- focus lands at a meaningful destination heading/control rather than arbitrary first focusable item.

## Scenario C — top-level area switch

Required checks:

- each area's restoration policy is defined;
- switching does not unexpectedly duplicate history entries;
- returning preserves task-critical depth/filter/scroll when justified;
- stale or security-sensitive state is invalidated correctly.

## Scenario D — interruption during pending async work

Required checks:

- pending/confirmed/failed state remains distinguishable on return;
- the resumed UI exposes enough cueing to reconstruct the task;
- user cannot unknowingly repeat a high-cost operation;
- recovery path exists after network failure.

## Scenario E — keyboard/assistive-technology traversal

Required checks:

- visible focus remains discernible;
- route/modal transitions set focus logically;
- dismissal restores focus logically;
- current location and selection remain programmatically/visually distinguishable from focus;
- hover-only paths have keyboard equivalents;
- focus is not obscured by sticky/overlay content.

### Measures

Where performance matters, record separately:

- successful return/navigation rate;
- wrong-destination/back errors;
- resumption lag after interruption;
- resumption accuracy;
- lost-work incidents;
- focus-loss events;
- repeated navigation steps;
- subjective orientation/confidence.

Do not collapse preference, speed and correctness into one “usability” score.

---

# 15. Project Readiness Test

## When should this knowledge be applied?

Any product with multiple destinations, details, modals, multi-step work, top-level navigation, deep links, notifications, async work, browser history, keyboard interaction or interruption-prone workflows.

## When should it not be over-applied?

Very small single-surface tools may not need elaborate stack modeling. Do not invent hierarchy, restoration layers or custom history when the product genuinely has one stable context.

## What project inputs are required?

- product information hierarchy;
- primary tasks and interruption costs;
- entry points and deep-link requirements;
- target platforms and browser/native conventions;
- top-level navigation model;
- whether users switch between parallel workstreams;
- draft/commit/synchronization lifecycle;
- accessibility/keyboard requirements;
- localization/text-growth conditions;
- state freshness/security constraints.

## What concrete decisions can this change?

- Back vs Up vs Close control;
- modal vs full destination;
- push vs replace vs no-history transitions;
- whether top-level destinations preserve independent stacks;
- scroll/filter/selection restoration policy;
- focus placement/restoration;
- unsaved-work behavior;
- deep-link orientation affordances;
- interruption recovery cues;
- whether a high-risk resume requires review rather than immediate action.

## What alternatives/trade-offs follow?

- stronger state preservation improves continuity but increases stale-state and complexity risk;
- more explicit hierarchy improves orientation but can add visual/navigation chrome;
- aggressive history entries improve retraceability but can create Back fatigue;
- modals preserve context but can constrain deep linking, focus and complex flows;
- automatic resume improves speed but may increase error after interruption in high-risk tasks.

## How should it be validated?

Use the controlled scenarios above on target platforms with realistic content, keyboard/pointer/touch paths, direct/deep-link entry, interruption and failure states. For web products, include native browser Back/Forward and history restoration rather than testing only in-app controls.

---

# 16. OPEN

- Build a running prototype covering deep link, modal dismissal, history traversal, independent top-level stacks, focus restoration and interrupted async work.
- Validate browser Back/Forward/scroll restoration and SPA route behavior in actual target browsers with the Web Design Specialist.
- Test Android predictive Back and platform-specific behavior rather than treating generic back-stack theory as implementation proof.
- Test iOS/iPadOS navigation/dismissal conventions in real target contexts.
- Measure interruption-resumption behavior on representative product tasks; do not generalize healthcare/lab timings directly to all apps.
- Study navigation information scent, search-versus-browse strategy and wayfinding as a separate future module.
- Study gesture discoverability and system gesture conflicts separately.
- Test multilingual/RTL navigation geometry using Type evidence.
- Test forced-colors/current-location/focus state resilience using Color evidence.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context:
  - navigation titles, tabs, breadcrumbs and route controls are semantic state cues whose geometry can fail under fallback/localization;
  - I001 requires deep-link, focus-restoration and multi-stack specimens to be stress-tested with T001 fallback states.
- Canonical section:
  - `Navigation-state contract`, `Failure modes`, `Controlled practice / validation matrix`.
- Confirmation / contradiction / transfer note:
  - confirms T001's claim that typography can cause navigation/reflow failures that are not purely Layout defects.
- Scope limit:
  - I001 does not decide font selection or metric normalization.

### Color
- Useful finding/context:
  - current location, selection, focus and transient-state meaning must remain distinct even when authored fill/shadow/hue is removed.
- Canonical section:
  - `Focus, selection, current location and active state are not synonyms`.
- Confirmation / contradiction / transfer note:
  - extends C001 from component state resilience into navigation-state resilience.
- Scope limit:
  - I001 does not define the color palette or contrast calculations.

### Layout / Interaction
- Useful finding/context:
  - I001 adds history/hierarchy/focus/restoration as explicit layers to the existing action-state coupling model from Study 015.
- Canonical section:
  - `Navigation state has more layers than destination ID` and `Navigation-state contract`.
- Confirmation / contradiction / transfer note:
  - extends prior Interaction research rather than replacing it.
- Scope limit:
  - running implementation and observed user resumption remain OPEN.

### Web Design
- Useful finding/context:
  - concrete transfer contract for browser history, deep links, route transitions, focus restoration, modals, top-level stacks, scroll/filter restoration and interrupted async flows.
- Web application / validation consequence:
  - future `W###` work should test I001 in a real page/router/browser context using native Back/Forward, actual focus, zoom/reflow, localized content and network failure.
- Confirmation / contradiction / transfer note:
  - WHATWG/WAI define platform behavior and accessibility constraints, but no cross-browser product validation is claimed here.
- Scope limit:
  - Web-specific router architecture, framework behavior and browser implementation evidence remain Web-owned.

## Status implication

I001 closes an important **source-study gap** in navigation/task-flow integration and establishes a project-facing decision model. It does **not** move navigation or Interaction Foundation to PASS. A running multi-input prototype, actual focus/history behavior, deep-link tests, async failure/recovery and observed interruption/resumption evidence remain required.