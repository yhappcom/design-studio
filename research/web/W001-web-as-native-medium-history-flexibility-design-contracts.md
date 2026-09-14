# W001 — Web as a Native Medium: History, Flexibility, and Design Contracts

Status: **FOUNDATION / PRACTICE + CRITIQUE — first substantive Web baseline; not PASS**  
Owner: Web Design Specialist  
Date: 2026-09-15

## Question

What is the web as a design medium, why did its distinctive constraints and capabilities emerge, and which durable design principles follow from that history for real websites and web applications?

This study does **not** attempt to survey every web technology. It establishes the baseline mental model required before later Web studies on composition, responsive systems, navigation, components, forms, dashboards, accessibility, performance, and browser validation.

The core claim to test is:

> A web page is not primarily a fixed visual canvas delivered to a known device. It is an addressable structured document/application interpreted by user agents under variable content, viewport, input, preference, font, network, and capability conditions.

The professional consequence is that Web Design should control **relationships, priorities, constraints, and adaptation rules** more strongly than exact coordinates.

---

## RELATED DOMAIN CHECK

### Typography / Type

Evidence checked:
- `progress/TYPE_STATUS.md`
- `research/type/T001-web-typography-fallback-metrics-reflow-transfer.md`

Reusable findings:
- actual browser layout can change with loading fallback, failure fallback, script fallback, and user/browser substitution;
- text geometry and line wrapping are runtime inputs, not constants exported from a design tool;
- Type explicitly hands browser font loading, fallback, wrapping, zoom, and reflow validation to Web.

Web transfer decision:
- **REUSE + TRANSFER VALIDATION**. W001 treats changing text metrics as one proof that the web medium cannot be designed safely as a fixed bitmap/canvas.

### Color

Evidence checked:
- `progress/COLOR_STATUS.md`
- `research/color/C001-web-color-user-override-resilience.md`

Reusable findings:
- author values are not always final used/rendered colors;
- browser/user forced-color behavior can replace authored fills, borders, and other channels;
- color meaning must survive user-agent participation.

Web transfer decision:
- **REUSE + TRANSFER PRINCIPLE**. The browser/user is an active participant in presentation; Web Design cannot assume exclusive pixel ownership.

### Layout / Interaction

Evidence checked:
- `progress/LAYOUT_STATUS.md`
- `research/layout/L002-whitespace-density-spatial-rhythm.md`
- established L003/L006 and I001–I004 status summaries.

Reusable findings:
- responsive systems preserve semantic relationships rather than exact coordinates;
- density is task-dependent and cannot be reduced to element count or universal whitespace rules;
- visual ownership, pointer ownership, focus ownership, semantic exposure, data ownership, and restoration are different layers;
- screenshot QA cannot validate interaction ownership.

Web transfer decision:
- **REUSE + WEB-SPECIFIC INTEGRATION**. W001 turns those abstract spatial/interaction findings into a general web-medium model and a browser-rendered fixed-vs-fluid exercise.

### Web Design

Evidence checked:
- `progress/WEB_STATUS.md`
- `research/web/README.md`

State before W001:
- no substantive `W###` study existed;
- Foundation baseline was not established.

Overlap decision:
- **NEW FOUNDATION + PRACTICE**. W001 establishes the first Web-owned evidence and does not claim to replace deeper Type, Color, Layout, or Interaction ownership.

### Cross-cutting evidence

Checked:
- CERN history of the Web;
- W3C CSS1/CSS2 history and current CSS architecture;
- W3C DOM Level 1 history;
- WHATWG HTML Living Standard;
- W3C Device Independence Principles;
- W3C WCAG Reflow;
- John Allsopp, *A Dao of Web Design*;
- Ethan Marcotte, *Responsive Web Design*;
- current Flexbox, Grid, Sizing, Media Queries, and Container Queries specifications.

---

# 1. History begins with information sharing, not page composition

## SOURCE

CERN records that Tim Berners-Lee invented the World Wide Web in 1989 while working at CERN to meet the need for automated information-sharing between scientists. By the end of 1990 the first server and browser were running. The first website described the Web project itself and linked to technical information and other servers. CERN later released the Web software publicly and placed it in the public domain in 1993.

Primary sources:
- https://home.cern/science/computing/the-birth-of-the-web/
- https://home.cern/science/computing/the-birth-of-the-web/short-history-web/

## SYNTHESIS

The first-order abstraction was not a designed “screen.” It was a network of **identifiable resources connected by hypertext and interpreted by browsers**.

This history matters because several persistent web-design properties follow from it:

1. **addressability** — pages/resources have identities that can be linked, shared, bookmarked, indexed, and revisited;
2. **document continuity** — information should remain meaningful independently of one exact visual rendering;
3. **user-agent mediation** — the browser interprets and presents the resource;
4. **heterogeneity** — different systems can participate in the same web;
5. **navigation is architectural** — links and history are part of the medium, not decorations around the page.

## STUDIO JUDGMENT

A Web designer must ask more than “what does this screen look like?”

For every important surface, also ask:
- What is its stable URL/resource identity?
- Can a user arrive directly rather than through the homepage?
- Does the page explain its context after direct entry?
- What remains meaningful if author styling changes or fails?
- What should browser navigation/history do?
- Which information is document content versus temporary application state?

A visually strong composition that fails those questions may be a strong **image** but a weak **web surface**.

---

# 2. HTML established structure before rich presentation

## SOURCE

W3C describes HTML as the Web's core markup language and notes that it was originally designed to semantically describe scientific documents, then evolved to describe many other document and application types.

The current WHATWG HTML Living Standard defines documents, semantics, interaction, page loading, application APIs, syntax, and rendering expectations. Its rendering section explicitly distinguishes document meaning from default user-agent presentation.

Sources:
- https://www.w3.org/TR/html/all/
- https://html.spec.whatwg.org/
- https://html.spec.whatwg.org/multipage/rendering.html

## SYNTHESIS

HTML establishes a durable distinction between:

`meaning / structure` and `one particular visual presentation`.

A heading, navigation region, form control, article, list, link, or table is not merely a rectangle with typography. It participates in document structure, browser behavior, accessibility APIs, navigation, selection, copy/paste, search, and other platform conventions.

## STUDIO JUDGMENT

Web design should start from the **content/task model and semantic source order**, then add visual composition.

This does not mean “semantic HTML automatically creates good design.” It means visual design should not casually destroy the underlying document/action model merely to reproduce a static mockup.

A useful design chain is:

`user/task → content object → semantic structure/source order → default flow → visual hierarchy/layout → interaction enhancement → browser/device validation`.

---

# 3. CSS emerged because structure and presentation needed different control systems

## SOURCE

W3C's 1996 CSS1 announcement states that HTML intentionally favored document structure over presentation and that CSS provided authors a way to specify fonts, colors, margins, and other presentation while enabling one stylesheet to affect an entire site. W3C records that Håkon Wium Lie began work on CSS in 1994 and Bert Bos joined in 1995; CSS1 became a W3C Recommendation on 17 December 1996.

CSS2 became a W3C Recommendation in 1998 and expanded presentation with positioning, media-specific styles, downloadable fonts, table layout, and internationalization-related capabilities.

Sources:
- https://www.w3.org/press-releases/1996/css1-rec/
- https://www.w3.org/TR/REC-CSS1-961217
- https://www.w3.org/press-releases/1998/css2/
- https://www.w3.org/TR/1998/REC-CSS2-19980512/

## SYNTHESIS

The separation of structure and presentation was not an aesthetic purity rule. It solved practical system problems:
- maintainability across many pages;
- multiple media/presentation conditions;
- user and author participation in style;
- cleaner document structure;
- greater ability for presentation technology to evolve without rewriting content semantics.

The “cascade” also means author intent is not the only input. Web presentation is negotiated among platform defaults, user-agent behavior, user preferences, authored rules, inheritance, and conditional contexts.

## STUDIO JUDGMENT

Design tokens and design files are **inputs to a rendering negotiation**, not sovereign pixel specifications.

For production Web work, distinguish:
- semantic/content contract;
- author presentation contract;
- browser/platform defaults;
- user preference/override conditions;
- actual rendered result.

This directly aligns with Color C001 and Type T001: author color and type intentions can be altered by valid browser/user conditions.

---

# 4. DOM and scripting expanded the Web from documents toward applications without deleting the document model

## SOURCE

W3C's DOM Level 1 Recommendation (1998) established a platform- and language-neutral interface allowing programs and scripts to dynamically access and update document content, structure, and style. The accompanying W3C announcement emphasized interoperability across browser/vendor mechanisms.

ECMA records that work on ECMAScript standardization began in 1996 and the first edition of ECMA-262 was approved in 1997.

Sources:
- https://www.w3.org/TR/REC-DOM-Level-1/
- https://www.w3.org/press-releases/1998/dom/
- https://ecma-international.org/news/ecma-262-the-ecmascript-javascript-the-most-popular-web-scripting-standard-is-celebrating-its-20th-birthday/

## SYNTHESIS

Web applications added mutable state and richer behavior, but they still execute inside an environment with:
- documents and DOM trees;
- URLs and navigation/history;
- browser controls and defaults;
- loading/failure conditions;
- multiple input methods;
- user preferences;
- accessibility trees and platform APIs.

The false dichotomy “website = document, web app = software so document principles no longer matter” is rejected.

## STUDIO JUDGMENT

For application-like web products, the design model becomes:

`resource/document semantics + application state + browser state + network state + interaction state`.

A web app is not professionally designed if only the happy-state component screenshot is defined.

Later W studies must explicitly cover loading, pending, error, retry, offline, history, direct entry, focus restoration, interrupted tasks, and partial data.

---

# 5. Early attempts to imitate print exposed a medium mismatch

## SOURCE

Historical accessibility guidance from W3C explicitly addressed layout tables and advised authors to use style sheets for layout/positioning; when layout tables were used, content still needed to linearize meaningfully. Current WAI guidance continues to state that data tables are not intended as general layout mechanisms.

Sources:
- https://www.w3.org/TR/WCAG10-HTML-TECHS/#tables-layout
- https://www.w3.org/WAI/tutorials/tables/

John Allsopp's 2000 essay *A Dao of Web Design* argued that designers were treating the Web too much like a fixed printed page and that the medium's adaptability should be treated as a strength rather than a defect.

Source:
- https://alistapart.com/article/dao/

## SYNTHESIS

A recurring historical failure pattern is:

`new medium → import conventions of previous medium → force medium to imitate old constraints → discover incompatibility → develop native conventions`.

For Web Design, the imported assumption was often:

`designer controls exact page dimensions, typography, and placement`.

But users can change viewport size, text size, fonts, language, input, preferences, and browsing context. Content can change independently. Network and resources can fail. The document can be printed, read aloud, indexed, copied, or reached directly.

## STUDIO JUDGMENT

“Pixel precision” is useful locally but dangerous as the top-level definition of quality.

Web precision should mean:
- precise semantic hierarchy;
- precise relationships and constraints;
- precise component/state behavior;
- precise alignment where conditions support it;
- precise adaptation rules;
- precise failure/recovery behavior;
- known tolerance to content and environment variation.

It should **not** mean forcing every browser/context to reproduce one artboard at the expense of usability or meaning.

---

# 6. Responsive Web Design formalized adaptation, but the deeper principle predates breakpoints

## SOURCE

W3C's Device Independence Principles (2003) state an aim to minimize authoring that restricts web content to a narrow set of devices and focus on matching content to the needs, capabilities, and limitations of delivery environments.

Source:
- https://www.w3.org/TR/di-princ/

Ethan Marcotte's 2010 *Responsive Web Design* identified fluid grids, flexible images, and media queries as three technical ingredients, but also argued for a change in thinking away from separate device-specific experiences toward adaptation across a gradient of viewing contexts.

Source:
- https://alistapart.com/article/responsive-web-design/

Current Media Queries continue to let authors condition presentation on user-agent/display features. Container queries add a component-level adaptation model based on the actual containing element rather than only the global viewport.

Sources:
- https://www.w3.org/TR/mediaqueries/all/
- https://www.w3.org/TR/css-contain-3/#container-queries

## SYNTHESIS

Responsive design is not synonymous with:
- “desktop / tablet / mobile” artboards;
- three standard breakpoint numbers;
- shrinking desktop UI;
- hiding secondary content on small screens.

The durable principle is:

> Define how information and interaction relationships should transform when available space, content, user preferences, or capabilities change.

## STUDIO JUDGMENT

A breakpoint is justified by a **layout/content/task stress point**, not by device folklore.

Prefer:
1. normal flow and intrinsic sizing;
2. flexible constraints;
3. component-local adaptation where appropriate;
4. media queries for environment/viewport changes;
5. explicit alternate composition only when the existing relationship stops serving the task.

This aligns with Layout's finding that responsive systems should preserve semantic relationships rather than exact coordinates.

---

# 7. Modern CSS layout is a relationship engine, not a better artboard exporter

## SOURCE

CSS2 formalized normal flow, floats, and absolute positioning. Modern Flexbox is optimized for one-dimensional interface layout and distributes free space among children. Grid is a two-dimensional layout system allowing flexible/fixed tracks and alignment. CSS Sizing defines intrinsic `min-content`/`max-content` concepts. Container Queries condition descendant styling on containing-element properties.

Sources:
- https://www.w3.org/TR/1998/REC-CSS2-19980512/visuren.html
- https://www.w3.org/TR/css-flexbox-1/
- https://www.w3.org/TR/css-grid/
- https://www.w3.org/TR/css-sizing-3/
- https://www.w3.org/TR/css-contain-3/

W3C's CSS Snapshot explains that modern CSS is modular rather than one monolithic “CSS3” specification.

Source:
- https://www.w3.org/TR/css-2024/

## SYNTHESIS

Modern CSS gives designers much more control than early Web CSS, but much of that power is **constraint-based and relational**:
- distribute available space;
- size from content;
- align along axes/tracks;
- define minimum/maximum bounds;
- change composition when a containing context changes.

This is materially different from specifying absolute X/Y coordinates on a fixed page.

## STUDIO JUDGMENT

Use absolute positioning when the design problem is actually positional/layered. Do not use it to simulate ordinary document layout that should respond to content growth.

Use Grid/Flexbox because their layout model fits the relationship being designed—not because they are modern defaults.

W002 will deepen this distinction into composition, flow, grid, density, intrinsic sizing, and spatial hierarchy.

---

# 8. Accessibility makes Web flexibility an operational requirement, not only a philosophy

## SOURCE

WCAG 2.1 Reflow requires content, with defined exceptions, to remain available without loss of information/functionality and without two-dimensional scrolling at a width equivalent to 320 CSS pixels. W3C notes the equivalence to a 1280 CSS pixel viewport at 400% zoom for vertically scrolling content.

Source:
- https://www.w3.org/TR/WCAG21/#reflow

## SYNTHESIS

The web's flexibility is not merely a designer preference. User-controlled enlargement and narrow effective layout widths are real conditions that interfaces must survive.

## STUDIO JUDGMENT

For ordinary vertically scrolling page/application regions, 320 CSS px is a meaningful stress condition during design validation, but it is **not** a universal “mobile design width.” Data tables, maps, diagrams, and other intrinsically two-dimensional content require task-specific handling rather than forced one-dimensionalization.

Do not infer WCAG conformance from one viewport test. Reflow is only one criterion and actual browser zoom, text spacing, focus, semantics, and assistive technology remain separate gates.

---

# 9. W001 medium model

W001 establishes the following Web Design baseline:

`addressable resource`  
`→ semantic document / task structure`  
`→ source order + browser-native behavior`  
`→ normal flow / intrinsic content geometry`  
`→ authored hierarchy, layout, type, color, surfaces`  
`→ conditional adaptation (container / viewport / preference / capability)`  
`→ application state and enhancement`  
`→ browser/user override + runtime rendering`  
`→ validation under real content, input, device, failure, and accessibility conditions`

No one layer can substitute for the others.

### Consequences

- Semantic structure is not the visual design, but visual design must respect it.
- Normal flow is not a mandatory aesthetic, but it is the safest baseline geometry for variable content.
- CSS control is powerful, but user agents/users retain legitimate influence.
- Responsive design is about adaptation rules, not device categories.
- JavaScript can enrich behavior, but application state must coexist with browser/document state.
- Design-tool artboards are useful representations, not the product runtime.
- Browser validation is a design activity, not merely engineering QA.

---

# 10. PRACTICE — fixed-canvas transfer vs web-native revision

Artifacts:
- `research/web/W001-web-medium-resilience-specimen.html`
- `research/web/W001-web-medium-resilience-playwright.py`
- `research/web/W001-web-medium-resilience-results.json`

## Question

Can the same semantic content remain reachable across large and narrow viewports when one composition is designed as a fixed 960px canvas and another is designed with normal flow, flexible wrapping, intrinsic/grid sizing, and bounded fluid dimensions?

## Controlled setup

Both variants contain the same kind of page structure:
- product brand;
- navigation;
- hero heading/body;
- two primary links/actions;
- preview region;
- supporting facts;
- mixed English/Korean text.

### Fixed transfer

Deliberately uses:
- 960px fixed shell;
- fixed-height hero;
- fixed pixel grid columns;
- fixed-size preview;
- absolutely positioned action group;
- no narrow-width recomposition.

This is a bounded proxy for “canvas-in” thinking, not a claim that every fixed width is wrong.

### Web-native revision

Uses:
- bounded `inline-size: min(100%, …)`;
- normal-flow action group;
- wrapping navigation/actions;
- responsive Grid with `auto-fit` and `minmax()`;
- intrinsic/flexible widths;
- fluid padding;
- content wrapping;
- no device-named breakpoint for the principal composition.

## Runtime

- Engine: installed Chromium through Playwright;
- page loaded with `set_content` because this execution environment blocks browser navigation to local HTTP/file URLs;
- viewport widths: 1280, 768, 320 CSS px;
- bounded checks: shell overflow, document horizontal overflow, action reachability;
- additional unstyled check at 320 CSS px by removing author `<style>` rules.

## Results

### 1280 CSS px

Fixed:
- shell 960px;
- no viewport overflow;
- both actions within viewport.

Fluid:
- shell 1120px bounded by available width/max;
- no viewport overflow;
- both actions within viewport.

### 768 CSS px

Fixed:
- shell remains 960px;
- shell and document overflow horizontally.

Fluid:
- shell becomes 684px in the specimen's surrounding padding/border context;
- no horizontal overflow;
- actions remain within viewport.

### 320 CSS px

Fixed:
- shell remains 960px;
- horizontal overflow;
- not all actions are within viewport.

Fluid:
- shell becomes 268px inside the specimen's surrounding padding/border context;
- no horizontal overflow;
- both actions remain within viewport.

### Author-CSS removed at 320 CSS px

For the duplicated semantic specimen content:
- no document horizontal overflow;
- 10/10 links remained rendered;
- 4/4 headings remained rendered.

## Bounded assertions

All intended bounded assertions passed:
- fixed shell overflow reproduced at 768 and 320;
- fluid shell fit at 1280, 768, and 320;
- fluid actions remained reachable at 320;
- fixed actions were not all reachable at 320;
- unstyled semantic content linearized without horizontal overflow;
- all specimen links/headings remained rendered without author CSS.

## CRITIQUE

This exercise proves only a narrow implementation fact:

> A fixed-canvas transfer can create avoidable horizontal overflow and off-viewport actions, while a relationship-based composition can preserve the same bounded content across the tested widths.

It does **not** prove:
- that fluid design is always superior;
- that every component should fit 320px without local scrolling;
- actual WCAG conformance;
- real 400% browser zoom behavior;
- keyboard/focus quality;
- screen-reader behavior;
- real font-loading/fallback behavior;
- production localization quality;
- Firefox/Safari/mobile parity;
- visual preference or task-performance superiority.

The experiment is therefore **PRACTICE + CRITIQUE**, not PASS.

---

# 11. Failure taxonomy established by W001

## A. Canvas transplant failure

Symptom:
- fixed dimensions/absolute placement preserve one reference screenshot but fail under content or viewport change.

Diagnosis:
- the designer specified coordinates where the product needed relationships/constraints.

## B. Device-folklore responsiveness

Symptom:
- arbitrary “mobile/tablet/desktop” breakpoints exist without evidence of a layout/task stress point.

Diagnosis:
- adaptation is being organized around assumed devices instead of content and behavior.

## C. Visual-semantic inversion

Symptom:
- semantic order or native behavior is distorted solely to achieve a visual arrangement.

Diagnosis:
- presentation has become the source of truth instead of an interpretation of the content/task model.

## D. Author-control illusion

Symptom:
- design assumes exact fonts, colors, dimensions, pointer input, or uninterrupted resources.

Diagnosis:
- valid browser/user/runtime participation was omitted from the design model.

## E. App exceptionalism

Symptom:
- a web app treats URLs, history, document semantics, focus, and native controls as irrelevant because “it is an app.”

Diagnosis:
- software behavior was added without respecting the host medium.

## F. Screenshot-only QA

Symptom:
- pixel similarity passes while focus ownership, history behavior, DOM order, semantics, overflow, or loading failure is wrong.

Diagnosis:
- one evidence layer is being mistaken for complete product behavior.

---

# 12. Operational design method derived from W001

For future Web Design work, begin major surfaces with this sequence:

1. **Purpose and task** — what user problem does this resource/surface solve?
2. **Resource/context** — URL, direct entry, page/app identity, navigation relationship.
3. **Content model** — what information and actions must exist?
4. **Semantic/source order** — what sequence remains meaningful without the final composition?
5. **Native baseline** — which browser behaviors/controls should be retained?
6. **Relationship model** — groups, priorities, alignment, density, simultaneous comparison needs.
7. **Intrinsic geometry** — what widths/heights come from content rather than arbitrary artboards?
8. **Constraints** — min/max sizes, readable measures, target sizes, comparison requirements.
9. **Adaptation** — what changes when relationships fail under available space/content/preferences?
10. **Enhancement/state** — asynchronous behavior, application state, motion, disclosure, persistence.
11. **Stress** — long localized content, font fallback, zoom/reflow, forced colors, keyboard/touch/pointer, loading/error.
12. **Validate** — browser/device/rendered evidence and human testing where the claim requires it.

This is not a mandatory waterfall. It is a diagnostic checklist to prevent skipping the medium's foundational contracts.

---

# 13. Project-readiness implications

After W001, Web Design should be able to challenge the following weak briefs:

- “Make desktop first at 1440 and scale it down.”
- “Use these exact coordinates everywhere.”
- “Tablet breakpoint is 768 because that is standard.”
- “This is an app, so browser Back does not matter.”
- “The Figma screenshot passed, so the overlay is correct.”
- “The brand font/color must always render exactly as authored.”
- “Hide the difficult content on mobile.”
- “Use JavaScript to reproduce a control the browser already provides” without task-specific justification.

W001 does **not** imply the opposite absolutes either:
- fixed dimensions are not forbidden;
- absolute positioning is not forbidden;
- custom controls are not forbidden;
- separate mobile experiences are not forbidden;
- visual fidelity is not unimportant.

The criterion is whether the chosen control mechanism matches the actual task and survives the relevant Web conditions.

---

# 14. OPEN / next validation gaps

W001 leaves important work open:

- actual browser zoom and text enlargement, not only narrow viewport equivalence;
- Firefox and Safari transfer;
- physical iOS/Android browser transfer;
- exact font-loading/fallback and Korean/English reflow using Type artifacts;
- forced-colors/high-contrast transfer using Color evidence;
- focus/history/navigation behavior with real routed pages;
- performance consequences of design choices;
- native vs custom control decisions;
- human comprehension/task evidence;
- complete page composition theory and practice;
- container-query/component-local responsive validation;
- production web app states and asynchronous failure.

These belong to later W studies rather than being falsely closed here.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type

**TRANSFER SUPPORT.** W001 confirms the project-level need behind T001: a Web layout should not require exact font metrics to remain usable. Future Web studies should test exact shipped webfonts, fallback, Korean/English wrapping, zoom, and loading states.

### Color

**TRANSFER SUPPORT.** W001 incorporates C001's broader implication that the browser/user participates in final presentation. Future Web specimens should combine responsive geometry with forced-colors/system-color conditions rather than validating those in isolation.

### Layout / Interaction

**CONFIRMATION + WEB TRANSFER.** The bounded fixed-vs-fluid Chromium exercise supports Layout's relationship-over-coordinate direction. It does not duplicate L002/L003/L006 or I-series behavioral evidence. W002 should deepen actual page composition and intrinsic/responsive geometry; later Web work should transfer focus/history/layer/state contracts into complete page systems.

---

# 15. Evidence level and completion judgment

**Evidence level:**
- primary/history standards review;
- cross-specialist evidence integration;
- one bounded Chromium failure→revision practice;
- explicit failure taxonomy and project method.

**W001 judgment:** **PRACTICE + CRITIQUE / Foundation baseline established, NOT PASS.**

Why not PASS:
- no cross-browser/device matrix;
- no real zoom/font-loading/forced-color integration;
- no human evidence;
- no complete production page/app exercise;
- historical and architectural principles still need transfer into later concrete Web domains.

However, W001 closes the initial “Web Design has no substantive baseline” gap. The specialist can now proceed to page composition with a defined model of the medium rather than treating Web Design as static artboard styling or frontend implementation.

---

## Sources — retrieved/revalidated 2026-09-15

Primary / standards / institutional:
- CERN, *The birth of the Web*: https://home.cern/science/computing/the-birth-of-the-web/
- CERN, *A short history of the Web*: https://home.cern/science/computing/the-birth-of-the-web/short-history-web/
- W3C HTML overview: https://www.w3.org/TR/html/all/
- WHATWG HTML Living Standard: https://html.spec.whatwg.org/
- W3C CSS1 announcement: https://www.w3.org/press-releases/1996/css1-rec/
- W3C CSS1: https://www.w3.org/TR/REC-CSS1-961217
- W3C CSS2 announcement: https://www.w3.org/press-releases/1998/css2/
- W3C CSS2: https://www.w3.org/TR/1998/REC-CSS2-19980512/
- W3C DOM Level 1: https://www.w3.org/TR/REC-DOM-Level-1/
- W3C DOM announcement: https://www.w3.org/press-releases/1998/dom/
- ECMA ECMAScript 20-year history: https://ecma-international.org/news/ecma-262-the-ecmascript-javascript-the-most-popular-web-scripting-standard-is-celebrating-its-20th-birthday/
- W3C Device Independence Principles: https://www.w3.org/TR/di-princ/
- W3C Media Queries: https://www.w3.org/TR/mediaqueries/all/
- W3C CSS Flexbox: https://www.w3.org/TR/css-flexbox-1/
- W3C CSS Grid: https://www.w3.org/TR/css-grid/
- W3C CSS Sizing: https://www.w3.org/TR/css-sizing-3/
- W3C CSS Containment / Container Queries: https://www.w3.org/TR/css-contain-3/
- W3C CSS Snapshot 2024: https://www.w3.org/TR/css-2024/
- W3C WCAG Reflow: https://www.w3.org/TR/WCAG21/#reflow
- W3C WAI tables guidance: https://www.w3.org/WAI/tutorials/tables/

Historically influential design arguments used as secondary evidence:
- John Allsopp, *A Dao of Web Design* (2000): https://alistapart.com/article/dao/
- Ethan Marcotte, *Responsive Web Design* (2010): https://alistapart.com/article/responsive-web-design/
