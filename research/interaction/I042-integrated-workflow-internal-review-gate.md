# I042 — Integrated Workflow Internal Review Gate

Status: **TRANSFER VALIDATION / PRODUCT WORKFLOW PRACTICE / HUMAN OWNER GATE DEFINED**  
Date: 2026-09-17

## Question

How should a specialist studio iterate on a real product without forcing the owner to review every micro-change, while preserving meaningful human judgment at the right point?

## SOURCE

The MintTap owner explicitly rejected a workflow where one screen or one small UI change is repeatedly sent for manual emulator review. The preferred operating model is:

`whole-app specialist audit → cross-discipline review → integrated implementation → internal deterministic validation → specialist re-critique → holistic owner review`.

MintTap workflows contain dependencies that cross individual screens:

- Demo/Auth/Onboarding intent can affect first-data behavior;
- transaction save changes Home/Detail/history interpretation;
- gross/net/currency context affects multiple analysis surfaces;
- ROC finality affects tax-adjustment eligibility and wording;
- ad placement can interrupt first-value or return-value flows.

## SYNTHESIS

### 1. Review cadence is an interaction-system decision

Too-frequent owner checkpoints create three problems:

1. local decisions are judged before their system context exists;
2. owner attention becomes the bottleneck for internal specialist work;
3. approval of fragments can accidentally freeze poor global structure.

The studio should therefore distinguish **internal iteration gates** from **human owner gates**.

### 2. Internal deterministic gate

Before owner review, specialists may iterate without owner interruption when the question can be answered through product contracts or reproducible artifacts.

Examples:

- action vs destination vs state-control role;
- required financial label presence;
- scenario coverage;
- loading/partial/unavailable state presence;
- protected first-value flow;
- responsive recomposition;
- source-level architecture boundaries;
- accessibility target/contrast checks where tools can measure them.

### 3. Owner review gate

Owner review is valuable for judgments such as:

- whole-product hierarchy feels correct for actual YieldMax use;
- professional information density is appropriate;
- important specialist information is not hidden or over-promoted;
- visual identity is acceptable;
- workflow changes align with product intent;
- trade-offs between compactness and explanation are acceptable.

Owner review should receive a coherent product candidate plus known trade-offs, not isolated widgets.

### 4. Owner evidence is real human evidence but not population evidence

The owner's emulator review is a genuine human observation and can close owner-intent/design-direction questions.

It does **not** establish:

- novice usability;
- representative YieldMax investor comprehension;
- accessibility-user performance;
- population preference;
- retention/activation uplift.

Those claims require appropriate participants/telemetry.

### 5. Workflow continuity must survive interruptions

The integrated candidate should explicitly preserve intent across transitions such as:

- Demo → sign in → setup → intended task;
- Add transaction → validation/save → portfolio result;
- Import review → save → personal first value;
- ROC final publication → tax adjustment entry → updated after-tax result;
- detail → Home return without losing relevant portfolio context.

A polished screen that loses task intent fails the product interaction gate.

## PRACTICE — MintTap Product Lab

The current isolated lab represents six major surfaces from one shared scenario model. It includes:

- activation/first-value path;
- portfolio summary;
- holding detail;
- transaction task;
- specialist insights/ROC/tax;
- settings/configuration;
- explicit protected ad boundaries;
- synthetic validation success and result handoff.

The lab journey switcher is an internal test instrument, not the proposed production navigation.

## CRITIQUE

The current Product Lab does not yet reproduce production persistence, auth, navigation history or actual async failures. Therefore it cannot prove:

- durable save semantics;
- cancellation/retry behavior;
- process death recovery;
- back-stack restoration;
- Demo intent continuation through real auth;
- import reconciliation;
- focus restoration;
- notification/permission interruptions.

These remain implementation/runtime dependencies.

## RELATED DOMAIN CHECK

### Type
T024 large-text pressure can force interaction controls to recompose. Target/action meaning must survive that transformation.

### Color
C055 state color is not a substitute for explicit interaction state/action availability.

### Layout
L046 defines whole-product grouping and recomposition. Interaction supplies continuity and consequence contracts.

### Web
W055 must bind route/history/focus/runtime evidence to the same workflow scenario identities.

### Content
CD061 owns consequence wording and state labels; Interaction owns the underlying truth and allowed recovery action.

## HANDOFFS TO OTHER SPECIALISTS

### Content
Do not write final-success copy until persistence/result contracts establish finality.

### Web
Capture route, focus, reload/deep-link and browser history when the Product Lab is executable on web.

### Layout
Owner-review packages should compare coherent workflow states, not isolated screenshots without preceding/following task context.

## Gate effect

I042 increases product-transfer maturity but Stage 3 remains PRACTICE / NOT PASSED. Real production transitions, platform execution and representative human evidence remain OPEN.
