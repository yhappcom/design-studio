# W003 — Responsive / Adaptive Recomposition by Relationship Ownership

Status: **PRACTICE / CRITIQUE — Foundation work in progress; no cross-browser or human PASS claimed**

Canonical artifacts:

- `research/web/W003-responsive-adaptive-recomposition.md`
- `research/web/W003-responsive-recomposition-specimen.html`

## Research question

How should a Web designer decide **what recomposes, who owns the trigger, and what must remain invariant** when available space, content length, input mode, user preferences or embedding context changes?

The target is not a catalogue of media/container-query syntax. The target is a reusable design judgment for page-global versus component-local adaptation.

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md` through T016. Exact downloadable-font state can change wrapping and downstream geometry. W003 therefore treats a breakpoint as a response to relationship stress, not a guarantee that one font realization will always fit before it.

### Color

Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS. W003 preserves task priority and state distinctions structurally; hiding, stacking or moving content must not make color the sole remaining information channel.

### Layout / Interaction

Checked `progress/LAYOUT_STATUS.md`, now Stage 1 PASS. W003 reuses L002 responsive density/reflow, L003 Type-dependent transfer and L006 ownership/state distinctions. The Web-specific extension is to assign **adaptation ownership** to the page, component or intrinsic artifact and preserve source/focus meaning across those changes.

### Web

Checked W001 and W002. W001 established the Web as a flexible medium; W002 established relationship-first layout selection and measured a case where a table required local overflow before the surrounding comparison workspace needed to stack. W003 makes that observation explicit as an adaptation-ownership model.

### Why overlap is useful

This is **TRANSFER VALIDATION**. It turns peer responsive/layout evidence and W002's measured threshold divergence into a Web design contract for reusable components embedded in different page contexts.

---

## SOURCE

Authoritative W3C sources were rechecked on 2026-09-15.

### Media queries

W3C Media Queries Level 4 describes media queries as tests of user-agent or display-device values/features. They are therefore appropriate when the adaptation condition is genuinely viewport/device/user-environment scoped.

### Container queries

CSS Containment Level 3 introduced size-query containers so descendant presentation can respond to the size of an appropriate containing box. This supports a different ownership model from viewport media queries: a reusable component can adapt to the space actually allocated to it.

### Responsive navigation consistency

WAI menu guidance states that responsive menu structure should remain consistent across screen sizes; items may be collapsed/hidden into subnavigation, but items that remain shown should preserve order, wording and destination.

### Focus and meaningful order

WCAG/WAI guidance requires visible sequential focus and preserves meaningful sequence. Responsive visual rearrangement therefore cannot be judged from screenshots alone. Source order, focus order and visual/task order must be checked together when meaning depends on sequence.

### Evidence boundary

These sources establish platform/accessibility constraints. They do **not** prescribe one breakpoint, one navigation pattern, or universal preference for container queries.

---

## SYNTHESIS — adaptation ownership

A responsive decision has three independent questions:

1. **Trigger ownership** — what fact changed?
2. **Recomposition ownership** — which relationship is responsible for adapting?
3. **Invariant** — what task/meaning must survive the adaptation?

| Condition | Likely owner | Typical trigger | Invariant |
| --- | --- | --- | --- |
| page shell/navigation loses usable space | page/global | viewport/media feature | resource identity, primary navigation, current location |
| reusable KPI cluster embedded in narrow column | component | container inline size | KPI identity/value pairing and scan order |
| toolbar actions no longer fit | component or page section | local available width + content | primary action priority and reachable secondary actions |
| semantic data table is intrinsically 2-D | artifact | intrinsic minimum vs allocated width | row/column comparison semantics |
| long localized labels expand controls | component/content | intrinsic content pressure | label/action association; no clipping |
| text/font loading changes wrap | content/runtime | actual rendered geometry | reading/task hierarchy, not exact line count |
| pointer/hover capability changes | interaction layer | media feature such as hover/pointer, plus actual control semantics | all essential actions remain available without hover |

### Core rule

**Do not ask “what device breakpoint should this component use?” before asking whether the component owns that breakpoint at all.**

A viewport query is justified when the relationship is page/global. A container query is justified when the same component can receive materially different allocated widths independent of viewport. Intrinsic wrapping/flow is preferable when no discrete mode change is required.

---

## Failure taxonomy

### A. Device-folklore breakpoint

A component switches at a named phone/tablet width even though its actual failure threshold changes with parent allocation or content.

### B. Global-query leakage

A reusable component uses viewport width to infer its own available space. The same component then behaves incorrectly in a narrow sidebar on a wide viewport or a wide main region on a medium viewport.

### C. Breakpoint proliferation

Every minor wrap is converted into a discrete query. This replaces intrinsic layout with a brittle state machine.

### D. Priority inversion

Narrow layout preserves every low-value element while hiding, moving or visually weakening the primary task.

### E. Visual reorder / semantic-order split

CSS visual reordering creates a convincing screenshot but source/focus order tells a different task story.

### F. False simplification

An intrinsically two-dimensional artifact is stacked merely to avoid horizontal scrolling, destroying comparison meaning. W002 already established local overflow as a legitimate bounded alternative.

---

## Original practice — one dashboard, three owners

Scenario: a portfolio dashboard has a global shell, a reusable KPI cluster, an action toolbar, a chart summary and a transaction table.

### Direction A — viewport owns everything

All components change at 768px and 480px.

**KEEP only if:** components are never embedded independently and measured failures actually coincide.

**REJECT when:** the KPI cluster is placed in a 320px sidebar on a 1280px viewport but still renders its wide arrangement.

### Direction B — component-local ownership

Page shell uses viewport-level adaptation. KPI cluster and toolbar respond to their own allocated inline size. Table retains intrinsic 2-D semantics with local overflow.

**KEEP when:** components are reusable across main/aside/detail contexts and local allocation differs from viewport.

**REWORK when:** container-query modes multiply without a meaningful task change; replace those cases with intrinsic wrapping.

### Direction C — intrinsic-first with minimal discrete modes

Most clusters use Grid/Flex/normal flow with `minmax()`, wrapping and intrinsic sizing. Queries are reserved for actual relationship changes: navigation mode, KPI label/value arrangement, or toolbar disclosure.

**KEEP when:** continuous geometry can absorb content/space changes without changing task structure.

**REJECT when:** a required simultaneous comparison or action priority is lost before intrinsic layout naturally recovers.

### Studio judgment

Direction C is the default starting point; Direction B is added where a reusable component has a genuine local mode change. Direction A is reserved for truly page-global relationships.

This is a professional design judgment, not a human-performance result.

---

## Specimen contract

The companion specimen intentionally places the same KPI component in both a wide main region and a narrow aside **at the same viewport width**. It compares:

- a viewport-owned implementation that cannot distinguish the two allocations;
- a container-owned implementation that recomposes only the narrow instance;
- an intrinsic-first action group that wraps without a discrete breakpoint;
- a semantic table that preserves local 2-D overflow.

This isolates the W003 question from device folklore: identical viewport, different component allocation.

---

## Validation plan

Executable follow-up should measure at minimum:

1. same viewport + different component containers;
2. same container width + different viewport widths;
3. long Korean and English labels;
4. preferred-font loading/failure where executable;
5. source order and sequential focus order before/after recomposition;
6. no unintended document horizontal overflow;
7. table overflow remains local;
8. hover-independent access to essential actions;
9. actual browser zoom separately from viewport/text-size proxies;
10. Firefox/Safari/physical mobile when environments exist.

A later harness should include a deliberate failure→revision cycle rather than only asserting the authored success state.

---

## STUDIO JUDGMENT — project method

For every responsive component, record a compact contract:

`task → relationship → stress signal → owner → adaptation → invariant → validation`

Example:

`compare KPIs → label/value pairs + cross-card scan → card allocation < useful two-column measure → KPI component → stack label/value internally → identity/value pairing + source order preserved → same viewport/different container + long-label test`.

This is more durable than a handoff that says only “mobile breakpoint: 768px.”

---

## OPEN

- reproducible Chromium harness/results for the companion specimen;
- actual browser-UI zoom;
- exact downloadable-font lifecycle in the full responsive specimen;
- Firefox/Safari and physical iOS/Android;
- keyboard/focus and accessibility-tree transfer under navigation disclosure;
- mixed pointer/hover/touch behavior;
- real routed navigation/wayfinding, which remains a separate major Foundation gap;
- human comprehension/task evidence deferred to project-stage validation.

## HANDOFFS TO OTHER SPECIALISTS

### Type

W003 treats font realization as a stress input rather than a breakpoint authority. Type can provide exact delivered-font/fallback pairs for later component-threshold transfer.

### Color

Responsive mode changes must retain semantic distinctions without relying on hue. Later theme/forced-color Web transfer should test all responsive modes, not only the wide state.

### Layout / Interaction

W003 extends relationship-first layout into explicit adaptation ownership. The highest-value peer challenge is whether source/focus/task sequence remains coherent when page-global and component-local recomposition happen simultaneously.

---

## Evidence level

**PRACTICE + CRITIQUE / SOURCE-grounded synthesis + original three-direction exercise + companion specimen contract. No browser validation PASS yet.**
