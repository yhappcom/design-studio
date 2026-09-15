# W005 — Component & Page Systems: Native Semantics, Variants and State Contracts

Status: **PRACTICE / CRITIQUE — Foundation baseline; browser matrix and complete task-surface transfer remain OPEN.**

Owner: Web Design Specialist  
Canonical path: `research/web/`

## Question

How should a Web Design system define reusable components and page patterns without turning the product into a visual component catalogue, flattening semantic differences, or losing browser-native interaction behavior?

W005 treats a component as a reusable **semantic + behavioral + visual contract**, not merely a styled rectangle.

Core model:

`user intent → semantic role → native/platform primitive candidate → state machine → content contract → geometry/adaptation → visual treatment → accessibility/input behavior → page-system placement → validation`

A component abstraction is justified only when the repeated contract is genuinely shared.

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md`, including T016. Type has shown that delivered font state can change geometry even when nominal typography tokens are unchanged. W005 therefore does not encode fixed-height component assumptions that depend on one preferred-font realization. Labels, helper/error text, values and bilingual content must be allowed to wrap or recompose where the task permits.

### Color

Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS, but Web/device production transfer remains separate. Component state cannot be represented by hue alone. Disabled, selected, current, invalid, pending and destructive meanings remain semantic states first; Color is one presentation channel.

### Layout / Interaction

Checked `progress/LAYOUT_STATUS.md` and incoming L006/I-series contracts. Visual ownership, pointer ownership, focus ownership, semantic/AT ownership and action/data ownership can diverge. W005 therefore treats state and interaction ownership as part of the component contract rather than assuming a screenshot proves behavior.

### Web

Checked W001–W004. W001 established browser participation; W002 composition; W003 adaptation ownership; W004 resource/navigation identity. The largest untouched Web Foundation gap after W004 is reusable component/page-system coherence and task-surface behavior.

### Overlap decision

**TRANSFER VALIDATION + WEB-SPECIFIC EXTENSION.** This study reuses Interaction state/ownership evidence but asks a Web-specific question: when should repeated visual patterns share an implementation/design abstraction, when should native HTML behavior remain primary, and which states must survive reuse across pages and responsive contexts?

---

## SOURCE

Rechecked 2026-09-15 against current WHATWG HTML and W3C WAI/APG material.

- HTML form controls carry native semantics and behavior. The `disabled` content attribute makes supported form controls non-interactive and excludes their values from submission behavior as defined by HTML; disabled controls are also removed from normal keyboard focus traversal by browsers.
- WAI APG's Button pattern distinguishes ordinary command buttons from toggle buttons and exposes toggle state through `aria-pressed`; activation and focus consequences depend on the action performed.
- APG keyboard guidance explicitly distinguishes native `disabled` from `aria-disabled`: the latter can preserve focusability where discoverability of an unavailable function is important, but authors then retain responsibility for suppressing the action and presenting the state consistently.
- APG Disclosure and Menu Button patterns require explicit expanded/collapsed state (`aria-expanded`) and defined keyboard behavior. A visual chevron alone is not the state contract.
- Composite widgets such as toolbars and radio groups have keyboard models that differ from a flat row of independently tabbable buttons.

These sources define platform/accessibility behavior. They do not require every product to use every APG pattern, nor do they prove that a custom component is preferable to a native element.

---

# 1. Component identity before styling

Before creating a reusable component, classify what is actually repeated:

1. **semantic role** — command, navigation link, disclosure, selection, text entry, status, message, container, data comparison;
2. **interaction contract** — activation keys/input, focus behavior, state transitions, cancellation/recovery;
3. **content contract** — required/optional label, value, description, icon, error/help text;
4. **layout contract** — intrinsic size, wrapping, local overflow, parent/container dependency;
5. **visual contract** — hierarchy, emphasis, surface/boundary treatment;
6. **data/action contract** — what operation or destination the component represents;
7. **accessibility contract** — name, role, value/state, focus/status communication.

Two elements that merely look alike do not necessarily belong to one component. Two elements that look different may share a semantic primitive with different presentation variants.

## Failure: visual-component ontology

`same rounded rectangle → same component`

This can collapse links, command buttons, toggles, disclosures and menu buttons into one generic clickable primitive even though their navigation, state, keyboard and accessibility contracts differ.

---

# 2. Native-first is a decision test, not a visual ideology

Use a native HTML primitive when its semantics and browser behavior already match the task and customization does not require replacing that contract.

Escalate toward custom behavior only when the product requires a materially different interaction model and the team can reproduce the missing semantics, keyboard/focus behavior, states and platform resilience.

Decision sequence:

`task role matches native primitive?`
`→ yes: start native`
`→ styling/layout sufficient? keep native contract`
`→ no: identify exact missing behavior`
`→ choose established composite/pattern if appropriate`
`→ custom only with explicit state + keyboard + focus + AT + failure validation`

**STUDIO JUDGMENT:** custom styling is not the same thing as a custom widget. Preserve native semantics even when visual treatment is heavily authored.

---

# 3. State matrix: do not reduce state to pseudo-classes

A reusable interactive component should distinguish at least these categories when relevant:

| State dimension | Example | Contract question |
| --- | --- | --- |
| availability | enabled / unavailable | Can it be activated? Must it remain discoverable? |
| focus | unfocused / focused | Where is keyboard focus and is it visibly perceivable? |
| pointer | hover / active | Supplemental pointer feedback; never the only essential state |
| selection | selected / unselected | Is this a persistent choice? |
| toggle | pressed / not pressed | Is the same control changing a binary state? |
| expansion | expanded / collapsed | Does it control visibility of another region? |
| validity | valid / invalid | What field/group failed and how is correction explained? |
| async | idle / pending / succeeded / failed / outcome unknown | Is repeat activation safe? What remains editable? |
| permission | allowed / denied | Is unavailability temporary, contextual or authorization-based? |
| destructive risk | ordinary / destructive | Is confirmation/recovery proportional to consequence? |

These dimensions can combine. A focused pending toggle or an invalid disabled field is not impossible merely because a design tool offers only one `state` property.

Component APIs should therefore avoid a single uncontrolled enum when independent dimensions genuinely coexist.

---

# 4. Disabled is not one universal design state

Distinguish at least:

### A. Native disabled

Use when a control is currently non-operable and removing it from ordinary focus traversal is acceptable. Native behavior should be preferred where it matches the task.

### B. Discoverable unavailable

Use only when users need to discover that an action exists and understand why it cannot currently run. `aria-disabled="true"` may be part of such a pattern, but it does not itself prevent activation; event/action suppression and explanation remain the author's responsibility.

### C. Hidden/not applicable

If an action is genuinely irrelevant in the current context, rendering a disabled control may add noise. Omission can be more truthful, provided users do not need the unavailable option for orientation or learning.

### D. Permission-denied

Do not automatically present authorization failure as generic disabled styling. The user may need an explanation, request-access path, or stable read-only representation.

**STUDIO JUDGMENT:** choosing disabled/hidden/read-only/explained-unavailable is a product-state decision, not a color-opacity choice.

---

# 5. Variants: constrain by meaning, not by every visual permutation

A useful variant changes a stable semantic or hierarchy contract, for example:

- primary vs secondary command emphasis;
- destructive command treatment;
- compact vs regular density when task/environment justifies both;
- icon + label vs label-only when both preserve accessible naming and task recognition;
- page-level vs inline message where scope changes.

Avoid encoding arbitrary combinations such as `blue-small-left-icon-rounded-2` as semantic variants.

A variant should answer:

`what product/design decision does this option represent?`

If the answer is only “this screenshot needed it,” prefer composition-level styling or a local exception rather than expanding the global component API.

---

# 6. Component boundary versus page-pattern boundary

Not every repeated arrangement belongs inside a component.

### Component

Owns a compact semantic/interaction contract that can survive multiple placements.

Examples: command button, disclosure trigger+region, field, status message, metric item.

### Composite component

Owns coordinated focus/selection/interaction among descendants.

Examples: radio group, tabs, toolbar, listbox. It must not be modeled as unrelated child buttons merely because the visuals are similar.

### Page pattern

Owns task sequence and relationships among multiple components/resources.

Examples: search + filters + results; settings section; list/detail workspace; dashboard summary + comparison table; edit form + save/recovery messaging.

### Page template

Owns durable page-level regions and hierarchy: page identity, navigation context, primary task area, supporting region, feedback/status region.

The system becomes brittle when page-specific task logic is buried inside a generic component, or when every small primitive is assembled ad hoc with no shared contract.

---

# 7. Page-system coherence test

For a reusable Web page system, inspect consistency across:

- page identity/title/heading;
- navigation/current-location cues from W004;
- primary action placement and hierarchy;
- form/search/filter scope;
- loading/empty/error/partial states;
- responsive ownership from W003;
- dense comparison/local overflow from W002;
- focus entry/restoration and status communication;
- long Korean/English content;
- exact delivered font/fallback states where geometry matters;
- Color state channels beyond hue.

A design system is not coherent merely because button radii and spacing tokens match.

---

# 8. Three materially different system strategies

## Direction A — Native-semantic thin layer

Use semantic HTML/native controls as the dominant primitive layer, with a small token/variant system and page patterns composed around them.

**KEEP when:** product interactions are mostly conventional forms/navigation/content; accessibility/platform resilience and low maintenance are high priorities.

**REWORK when:** visual branding is too weak or repeated higher-order task patterns remain inconsistent.

**REJECT when:** the product genuinely requires complex composites that native primitives cannot express without awkward task compromises.

## Direction B — Pattern-led product system

Native primitives remain underneath, but the canonical design units are task patterns: filter bar, result set, editable data row, portfolio summary, settings group, recovery banner.

**KEEP when:** the same workflows recur across many pages and consistency of task behavior matters more than atom count.

**REWORK when:** patterns overfit one page and cannot survive content/responsive variation.

**REJECT when:** pattern wrappers obscure native semantics or create duplicated state ownership.

## Direction C — Highly abstract component platform

A broad polymorphic component API attempts to cover many roles/visuals through props/configuration.

**KEEP only when:** product scale, implementation discipline and repeated cross-team needs justify the abstraction and semantic roles remain explicit.

**REWORK when:** prop combinations create invalid or untested states.

**REJECT when:** semantic differences are hidden behind one generic clickable/container primitive or the abstraction costs more reasoning than it saves.

Current Foundation judgment: prefer A or B as the default learning baseline; C requires stronger evidence and production-scale justification.

---

# 9. Failure taxonomy

### CP-1 Visual equivalence collapse
Different semantic controls share one generic clickable abstraction because they look similar.

### CP-2 Variant explosion
Every local visual exception becomes a global variant.

### CP-3 State flattening
Hover/focus/selected/pressed/expanded/disabled/pending/error are treated as interchangeable “states.”

### CP-4 Native contract replacement without repayment
Custom widget removes built-in keyboard/form/focus behavior without explicitly rebuilding and testing it.

### CP-5 Screenshot-complete component
Default visual state is polished while long labels, error text, pending state, keyboard focus and forced/user color conditions are absent.

### CP-6 Page logic inside atom
A low-level component owns routing, data fetching, authorization and task-specific recovery, making reuse deceptive.

### CP-7 Token consistency mistaken for product coherence
Pages share colors/spacing/radii but differ in navigation, task hierarchy, error/recovery and state behavior.

---

# 10. Foundation practice matrix

| Product need | Primitive/system choice | Why | Required stress |
| --- | --- | --- | --- |
| navigate to holding detail | `<a href>` styled as needed | resource navigation from W004 | direct entry, visited/current context, long label |
| save form | submit `<button>` | command + native form semantics | pending, validation failure, outcome unknown |
| show optional detail | disclosure button + region | explicit expanded state | keyboard, long content, responsive |
| choose one portfolio | native radios/select or justified composite | exclusive selection semantics | keyboard, selected state, long names |
| unavailable export | disabled vs discoverable unavailable chosen by context | availability is product state | explanation/discoverability |
| dense action group | ordinary buttons or toolbar only if composite keyboard model is justified | visual grouping does not imply toolbar semantics | focus sequence, disabled items, narrow width |
| filter/search/results | page pattern, not one giant component | owns task relationships across controls/results | loading/empty/error, URL state, narrow width |

---

# 11. Project-readiness questions

Before approving a component/system decision, answer:

1. What user intent and semantic role does it represent?
2. Is there a native primitive that already satisfies most of the contract?
3. Which state dimensions can coexist?
4. What does disabled/unavailable mean here?
5. What is component-owned versus page/task-owned?
6. Does the abstraction preserve links vs commands vs toggles vs disclosures vs selections?
7. How does it behave with long/localized content and fallback fonts?
8. What happens at narrow allocation and text enlargement?
9. What are the keyboard/focus and status consequences?
10. Which visual channels disappear under user/browser overrides?
11. What async/error/recovery states exist?
12. What evidence would falsify the chosen abstraction?

---

## OPEN / next validation

W005 does **not** claim browser, AT or production PASS.

Highest-value next evidence:

1. browser specimen comparing native button/link/disclosure/radio with visually similar but semantically collapsed custom controls;
2. measure Tab/Enter/Space behavior, focusability and disabled versus `aria-disabled` consequences;
3. long Korean/English labels + 200% text-size stress + narrow allocation;
4. forced-colors/browser-user-style transfer where executable;
5. form validation + pending/error/outcome-unknown page-pattern transfer using I002/I004 evidence;
6. component/page boundary exercise across at least two unrelated product contexts;
7. Firefox/Safari/physical mobile and AT remain later evidence gates;
8. human discoverability/comprehension remains deferred to app/project validation where required.

## HANDOFFS TO OTHER SPECIALISTS

### Type
Component APIs must not encode fixed geometry that only survives one preferred-font metric realization. W005 transfers T016's runtime-font lesson into reusable Web controls and page patterns.

### Color
Component state taxonomy provides concrete Web transfer targets: focus, selected, toggle, expansion, validity, async, permission and destructive meaning must remain distinguishable without hue-only encoding.

### Layout / Interaction
W005 confirms that visual similarity is insufficient to establish interaction equivalence. L006/I-series ownership/state contracts should be preserved when Web components are abstracted or reused.

### Web
W005 supplies the missing Foundation baseline for component/page systems. Next Web work should validate this contract in browser behavior and then move into complete task surfaces (forms/search/filter/table/settings/dashboard) rather than expanding an atom catalogue.

## Evidence boundary

Evidence level: **SOURCE + SYNTHESIS + PRACTICE / CRITIQUE / TRANSFER VALIDATION.**

No browser execution, assistive-technology, physical-device, production-design-system or human-task PASS is claimed in W005.