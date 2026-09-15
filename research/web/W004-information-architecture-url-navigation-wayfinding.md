# W004 — Information Architecture, URL Resource Structure, Navigation & Wayfinding

Status: **PRACTICE / CRITIQUE — Foundation baseline; browser/history and project transfer remain OPEN.**

Owner: Web Design Specialist  
Canonical path: `research/web/`

## Question

How should a web product turn its information and task model into addressable destinations, navigation and orientation cues so that direct entry, traversal, Back/Forward, responsive navigation and current-location signals remain coherent?

W004 is not a menu-pattern catalogue. It treats information architecture as a contract between **user task, content/resource identity, URL/location, navigation choice, history, page hierarchy and orientation**.

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md` and `research/type/009-typography-as-information-architecture.md`.

Reusable finding: typography routes attention among semantic roles; page identity, section identity, action, metadata and state must remain distinguishable. Web transfer: route labels and headings must preserve role hierarchy under wrapping/localization rather than encoding architecture only through position.

### Color

Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS but production Web transfer is not. Current-location, focus and selected navigation semantics must not rely on hue alone.

### Layout / Interaction

Checked `progress/LAYOUT_STATUS.md` and `research/interaction/I001-navigation-history-focus-restoration-interruption.md`.

I001 already separates location, traversal history, hierarchy, focus, transient layers, task state and restoration. W004 is therefore **TRANSFER VALIDATION + WEB-SPECIFIC EXTENSION**, not independent invention. Web adds URL/resource identity, direct entry, browser history, landmarks, responsive navigation and page-system application.

### Web

Checked W001–W003. W001 established addressability/browser participation; W002 established relationship-driven page composition; W003 established adaptation ownership. None yet supplied a Web-specific IA/navigation baseline.

### Overlap decision

**TRANSFER VALIDATION + EXTENSION.** Reuse I001's semantic separation, then test what changes when destinations are addressable Web resources and browser traversal/direct entry are first-class product behavior.

---

## SOURCE

Rechecked 2026-09-15:

- WHATWG HTML defines navigation and distinguishes navigation, reload/traversal and same-document URL/history updates. Web design must therefore not treat every visible screen transition as the same history operation.
- W3C WAI menu guidance recommends semantic navigation structure, labels for multiple navigation regions, current-item indication, and consistency of visible menu item order/wording/destination across responsive states.
- WAI breadcrumb guidance defines breadcrumbs as hierarchical parent links that orient users; the breadcrumb navigation landmark should be labelled and the current page can use `aria-current="page"`.
- WAI guidance connects clear/consistent navigation with Multiple Ways and location/orientation cues. Search, site maps, breadcrumbs and headings are complementary finding/orientation mechanisms, not interchangeable decorations.
- HTML sectioning elements such as `nav` and `main` expose landmark semantics; repeated navigation regions need meaningful differentiation.

These sources establish platform/accessibility contracts. They do not prove which architecture best fits a particular product; that requires task/content analysis and project validation.

---

# 1. IA model: identity before menu placement

A destination should be modeled before choosing whether it appears in a top bar, side rail, breadcrumb, search result or contextual link.

For each candidate destination record:

`user task → resource/content identity → canonical location → parent/context → entry paths → exit/traversal expectations → persistent state → orientation cues`

A navigation control is then one **access path** to that destination, not the destination's definition.

### Failure: menu-first architecture

Starting from “we need five tabs” tends to collapse different questions:

- what exists;
- what deserves a stable URL;
- what is merely a view/filter/state of something else;
- what belongs in global navigation;
- what is contextual;
- what should create history;
- what must survive direct entry.

W004 rejects navigation chrome as the canonical information model.

---

# 2. Four structures must not be conflated

## A. Resource hierarchy

Conceptual containment/ownership: e.g. `Portfolio → Holding → Distribution`.

## B. Navigation hierarchy

Which destinations are exposed globally, locally or contextually. It may be shallower than resource hierarchy.

## C. URL structure

Addressable location and state representation. URL path depth is not automatically visual hierarchy depth.

## D. Traversal history

How the user actually arrived and what Back/Forward means. History is temporal, not hierarchical.

A breadcrumb answers hierarchical orientation; browser Back answers traversal. They can point to different destinations and should not be visually or behaviorally conflated.

---

# 3. Route/state classification practice

Controlled product model: a portfolio-tracking Web app.

| Candidate | Identity judgment | Addressability | History judgment | Primary finding/orientation |
| --- | --- | --- | --- | --- |
| `/portfolios` | stable collection | canonical route | push on navigation | global nav + page heading |
| `/portfolios/alpha` | stable portfolio | canonical route | push | contextual links + breadcrumb/current nav |
| `/portfolios/alpha/holdings/CONY` | stable holding within portfolio | canonical route | push | list/detail link + breadcrumb |
| `?period=1y` | view state with sharing value | URL query candidate | push or replace depends on user-visible navigation semantics | filter state + URL |
| `?sort=yield-desc` | view state | URL query candidate | often replace if rapid ephemeral adjustment; project decision | table control |
| open “edit holding” dialog | transient task layer | not automatically a route | normally no page-history entry unless product explicitly makes it navigable | dialog title + restoration target |
| onboarding step | task/process state | route/URL only if resume/direct-entry contract requires it | explicit step history policy | progress indicator + heading |

This table is a design exercise, not a universal routing prescription. The point is to force explicit identity/history decisions before implementation.

---

# 4. Direct-entry test

Every canonical route should be reviewed as if the user arrives with **no prior in-app traversal context**.

Ask:

1. Can the page identify itself without a previous screen?
2. Is required parent/account/portfolio context visible?
3. Are permissions/absence/error states intelligible?
4. Does the primary navigation expose current location?
5. If hierarchy matters, is there an appropriate parent path/breadcrumb?
6. Does the page avoid relying on a custom “Back” control whose destination exists only in assumed history?

A route that works only after following the designer's preferred funnel is not robustly addressable.

---

# 5. Navigation layers by scope

Use scope rather than visual style to decide navigation ownership.

- **Global navigation:** major durable product areas.
- **Section/local navigation:** sibling destinations within a durable area.
- **Contextual navigation:** links generated by the current content/task.
- **Hierarchical orientation:** breadcrumbs or equivalent parent context where hierarchy is useful.
- **Within-page navigation:** headings/anchors for one resource/document.
- **Search:** retrieval by query; complements, not automatically replaces, browse architecture.
- **History traversal:** browser Back/Forward; temporal traversal, not site hierarchy.

A top bar, sidebar or disclosure menu can host more than one scope visually, but scope must remain semantically legible.

---

# 6. Current location contract

A current-location system should answer at least:

- what page/resource is this? — document/page heading/title;
- which major area contains it? — global/section navigation current state;
- where is it in a meaningful hierarchy? — breadcrumb/parent context when applicable;
- what local state is active? — filter/tab/view state when semantically relevant.

Do not use one blue highlight to represent all four layers.

WAI's `aria-current="page"` is useful for the navigation item representing the current page. It does not replace visible page identity, heading hierarchy, URL correctness or focus.

---

# 7. Responsive navigation contract

Transfer from W003:

`navigation scope + item priority + available allocation → adaptation owner → preserved invariant`

Preserve across responsive states:

- destination identity;
- wording unless a deliberate content rule changes it;
- relative order of items that remain visible;
- current-location semantics;
- keyboard reachability/focus order;
- alternate access to collapsed descendants.

Changing a sidebar into a disclosure is a presentation/adaptation decision. It must not silently rewrite the information architecture.

---

# 8. Three materially different IA directions

For the same portfolio product:

### Direction A — portfolio-centric hierarchy

`Portfolios → Portfolio → Holdings / Distributions / ROC`

Best when users primarily reason from a selected portfolio context. Strong contextual hierarchy; risk is repeated deep nesting and difficult cross-portfolio comparison.

### Direction B — task-domain top level

`Overview / Holdings / Income / Tax / Settings`, with portfolio as persistent context/filter.

Best when users repeatedly perform the same task across portfolios. Risk: portfolio identity becomes ambient state and direct links must make that context explicit.

### Direction C — hybrid workspace

Stable global task domains plus addressable portfolio/holding resources and contextual cross-links.

Best when both object identity and cross-object workflows matter. Risk: duplicated routes/navigation labels and unclear current-location ownership unless canonical resource and task routes are carefully separated.

**Studio judgment:** do not select among A/B/C from aesthetics. Choose using dominant tasks, frequency of context switching, sharing/direct-entry requirements, scale of object hierarchy and recovery cost when context is lost.

---

# 9. Failure taxonomy

### IA-1 Menu-first ontology
Navigation slots define the data/content model.

### IA-2 URL as implementation residue
Routes expose component/file structure instead of durable user concepts.

### IA-3 History/hierarchy conflation
Custom Back is used as “parent,” or breadcrumb is treated as temporal Back.

### IA-4 Direct-entry dependency
A page needs invisible prior traversal state to make sense.

### IA-5 Responsive architecture mutation
Collapsed mobile navigation changes labels/order/destinations or makes formerly reachable content inaccessible without an explicit product reason.

### IA-6 Current-state ambiguity
Page, section, selected object and filter state are encoded by one undifferentiated visual highlight.

### IA-7 Over-landmarking / unlabeled duplicate nav
Multiple navigation regions exist but users cannot distinguish their scope.

---

# 10. Project decision checklist

Before approving a Web IA/navigation system, produce:

1. resource/content inventory;
2. canonical destination matrix;
3. route vs transient-state classification;
4. direct-entry requirements;
5. global/local/contextual navigation ownership;
6. hierarchy vs history distinction;
7. current-location contract;
8. responsive adaptation contract;
9. empty/error/permission/deleted-resource destination behavior;
10. validation matrix for URL, Back/Forward, reload/direct entry, keyboard/focus and localization.

---

## SYNTHESIS

Web information architecture is not a sitemap alone. It is a coordinated model of:

`user concept ↔ resource identity ↔ addressable location ↔ navigation access ↔ hierarchy ↔ traversal history ↔ page identity ↔ resumable state`.

The Web-specific design advantage is addressability and native traversal. Treating these as implementation details throws away part of the medium established in W001.

## STUDIO JUDGMENT

- Model durable user concepts before navigation chrome.
- Keep resource hierarchy, navigation hierarchy, URL shape and history conceptually separate.
- Design canonical routes for direct entry, not only funnel traversal.
- Use breadcrumbs for hierarchy/orientation, not as a replacement for browser Back.
- Make responsive navigation preserve architecture unless the product explicitly changes task priority.
- Decide URL-backed state by shareability, restoration and user-visible navigation semantics rather than “all state in URL” or “no state in URL” dogma.

## Evidence level

**PRACTICE + CRITIQUE / SOURCE-grounded / TRANSFER VALIDATION from I001 + Web-specific extension / route-classification and three-direction design practice. NOT PASS.**

## OPEN

- executable browser route/history/direct-entry specimen;
- Back/Forward and reload state measurements;
- focus/scroll restoration after route changes;
- deleted/unauthorized/deep-link failure routes;
- long Korean/English navigation labels;
- responsive disclosure with source/focus/current-state validation;
- search vs browse/findability practice on a larger corpus;
- complete real-project IA inventory and tree/graph critique;
- human findability/orientation evidence, deferred to project-stage validation.

## HANDOFFS TO OTHER SPECIALISTS

### Type

Route labels, breadcrumbs, headings and current-location text need exact delivered-font/localization stress; architecture must survive wrapping.

### Color

Current/focus/selected states are separate semantics. Color should reinforce but not collapse them into hue-only meaning.

### Layout / Interaction

W004 confirms I001's hierarchy/history separation in Web-specific addressable routes. Future browser validation should jointly test history, focus/restoration and responsive navigation ownership.
