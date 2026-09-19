# LogMate Design Synthesis Gate

Status: **MANDATORY PRE-DESIGN GATE**  
Date: 2026-09-19  
Owner directive: do not create Design Corridor, Operational Geometry Contract, or Signature Code as independent outputs before the complete relevant Design Studio evidence is reconciled.

## 1. Why this gate exists

LogMate has accumulated substantial research across Type, Color, Layout, Interaction, Web, Content, accessibility, runtime transfer, and project-specific product contracts.

Many findings are individually valid but can conflict when applied simultaneously.

Examples:
- Type may protect semantic strings and prohibit squeezing/tracking compensation while Layout must fit a dense ledger.
- Content may require full semantic distinction while Layout must manage finite width.
- Color may recommend restrained salience while Interaction may require highly visible state change.
- Visual identity may seek distinctive codes while accessibility/runtime evidence limits reliance on one visual channel.
- A Home treatment may look coherent at low density but fail in View Logbook.
- A browser/static result may not transfer to Flutter/iOS/Android font metrics.

The goal is therefore not to maximize the number of rules. The goal is to derive one internally coherent system with explicit precedence and exceptions.

## 2. Scope of review

Before any visual-system rule is promoted, review must include:

### Product authority
- LogMate `MASTER.md`;
- relevant `docs/specs/`;
- frozen structural Home snapshot;
- confirmed owner decisions;
- OPEN decisions that must not be silently closed.

### Design Studio status
- global status;
- Type status;
- Color status;
- Layout/Interaction status;
- Web status;
- Content status.

### Foundational research
At minimum:
- typography as a system;
- metrics, spacing and optical rhythm;
- numeral/punctuation systems;
- grid/composition/hierarchy;
- perceptual grouping;
- color luminance/contrast/hierarchy;
- directness/state/modes/reversibility;
- accessibility/reflow/focus.

### LogMate-specific transfers
At minimum:
- dense ledger type transfer;
- customize density/projection transfer;
- state-visibility color transfer;
- semantic governance;
- browser/runtime transfer;
- owner-review/internal-iteration gate;
- any later LogMate-specific study that changes these conclusions.

### Brand/identity research
- current brand-philosophy reset study;
- additional digital/professional-tool research;
- no rejected visual concept may be used as evidence of correctness.

## 3. Evidence classification

Every relevant finding is classified as one of:

- **CANONICAL PRODUCT** — product semantic/behavior decision already confirmed;
- **NORMATIVE** — platform/accessibility/standard requirement;
- **SUPPORTED DESIGN PRINCIPLE** — transferable design evidence with no known contradiction;
- **PROJECT-SPECIFIC CANDIDATE** — plausible for LogMate but not yet validated;
- **IMPLEMENTATION EVIDENCE** — proves only a particular runtime/build/context;
- **HUMAN EVIDENCE** — owner or representative-user observation, with population scope recorded;
- **OPEN** — insufficient evidence;
- **SUPERSEDED** — explicitly replaced/rejected.

A lower-authority category cannot silently override a higher-authority one.

## 4. Contradiction matrix

For every proposed rule, compare it against:

1. **Type**
   - glyph metrics;
   - fallback;
   - numeric alignment;
   - identifier stability;
   - text scale;
   - semantic-string protection.

2. **Layout**
   - width budgets;
   - reflow;
   - grouping;
   - density;
   - semantic axes;
   - horizontal/vertical scrolling.

3. **Color**
   - luminance hierarchy;
   - state salience;
   - color independence;
   - light/dark/forced-colors.

4. **Interaction**
   - target clarity;
   - state ownership;
   - directness;
   - reversibility;
   - focus;
   - motion/feedback.

5. **Content**
   - exact professional semantics;
   - abbreviation rules;
   - label hierarchy;
   - localization;
   - action/state wording.

6. **Web / runtime**
   - responsive/browser transfer;
   - font loading/fallback;
   - zoom;
   - focus;
   - platform rendering;
   - implementation provenance.

7. **Brand / identity**
   - visual authorship;
   - durability;
   - recognizable code;
   - no ornamental shortcut;
   - no domain cosplay.

8. **Accessibility / human factors**
   - target sizes;
   - contrast;
   - reflow;
   - non-color cues;
   - reading/scanning pressure;
   - glare/device use where relevant.

A proposed rule does not pass because most domains agree. Any unresolved material contradiction blocks promotion.

## 5. Conflict classes

### Class A — hard contradiction
Two requirements cannot both be satisfied in the proposed form.

Action:
- do not choose one silently;
- restate the underlying goals;
- search for a third implementation that satisfies both;
- if no solution exists, escalate as explicit owner/product trade-off.

### Class B — scope contradiction
Rules appear incompatible but apply to different surfaces/states.

Action:
- narrow the scope;
- record exact surface/state boundary;
- prohibit accidental generalization.

### Class C — evidence-level contradiction
Static/browser evidence disagrees with native/runtime evidence, or research maturity differs.

Action:
- higher-fidelity evidence does not automatically erase lower-level findings;
- reproduce the discrepancy;
- identify whether the difference is Type, Layout, platform, fallback, or implementation.

### Class D — priority tension
Both principles are valid but pull in different directions, e.g. density vs whitespace.

Action:
- define an explicit priority order for the specific task/surface;
- stress-test the losing dimension to ensure it remains acceptable.

### Class E — unresolved unknown
No reliable evidence determines the choice.

Action:
- mark OPEN;
- do not convert preference into system policy.

## 6. Proposed precedence for synthesis

Unless a later owner decision changes it:

1. product semantic truth / safety / professional meaning;
2. normative accessibility/platform constraint;
3. interaction consequence and state truth;
4. data comparability and geometry stability;
5. content clarity and professional terminology;
6. responsive/layout coherence;
7. typography/color expression;
8. brand distinctiveness;
9. decorative preference.

This does **not** mean visual identity is unimportant. It means identity must be authored inside the constraints above rather than violating them.

## 7. Cross-surface requirement

No rule becomes a LogMate design code from Home alone.

Before promotion, test transfer conceptually or visually against at least:
- Home;
- View Logbook dense ledger;
- Activity Detail;
- Add Flight;
- configuration/Customize where relevant.

If a rule only works on one surface, classify it as a surface-specific composition rule, not a brand code.

## 8. Operational-data stability gate

Before whole-screen visual review:
- stress Date;
- carrier/flight number/suffix;
- DEP/ARR;
- registration;
- Block/Night/Inst;
- cumulative duration;
- compact headers.

Aesthetic review cannot rescue a candidate that fails stable comparison geometry.

## 9. Deliverable order

The next three artifacts are created only in this order:

### Phase 0 — Evidence Map
One table of all materially relevant conclusions, source, authority, maturity, scope, and known conflict.

### Phase 1 — Contradiction Register
Every cross-domain conflict or tension is recorded and resolved, scoped, or marked OPEN.

### Phase 2 — Integration Principles
Only rules that survive the contradiction register become synthesis principles.

### Phase 3 — Design Corridor
Allowed/prohibited visual behavior.

### Phase 4 — Operational Geometry Contract
Data axes, typography/layout responsibilities, stress requirements.

### Phase 5 — Signature Code Study
Candidate recognizable behaviors derived from the integrated principles.

The three requested outputs therefore share one evidence base and one contradiction register.

## 10. Promotion rule

A rule may be promoted only when:
- its evidence source is identified;
- scope is explicit;
- cross-domain checks are complete;
- no material contradiction remains hidden;
- OPEN items are declared;
- rejected alternatives and reason are recorded where useful;
- runtime/human validation boundaries are not overstated.

## 11. Stop condition

If the research review reveals that a foundational assumption is wrong, stop the visual-identity work and repair the foundation first.

Rework at this stage is cheaper than propagating a contradiction through Home, View Logbook, Activity, Add Flight and the implementation system.
