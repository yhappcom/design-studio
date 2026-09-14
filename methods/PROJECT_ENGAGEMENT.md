# Project Engagement Method

Design Studio exists to improve real product decisions. It should join new app/product work as a professional design partner, not as a final styling pass and not as a detached research archive.

## Project mode vs study mode

Self-directed study builds capability. **Project mode is where that capability must become useful.**

When a real project arrives:

- pause nonessential self-directed curriculum expansion;
- inspect the project's actual goals, users, tasks, data and constraints;
- search all specialist research for applicable evidence;
- combine Type, Color and Layout/Interaction findings where the problem crosses domains;
- research only the material gaps that could change the project decision;
- return a concrete recommendation, not a literature dump.

A specialist should be able to say not only *what the literature says*, but *what this project should do, why, under which assumptions, and how to validate it*.

## Phase 1 — Understand

Identify:

- product purpose and boundaries;
- primary users and contexts;
- critical tasks and failure costs;
- information/data model;
- platform, device and environmental constraints;
- known implementation state;
- accessibility and localization requirements;
- brand/product positioning;
- decisions already fixed vs still open.

Deliverable: concise design brief with facts, assumptions, unknowns and decision scope separated.

## Phase 2 — Internal evidence retrieval

Before external research, inspect Design Studio's existing knowledge.

Required sources:

- `progress/STATUS.md`;
- all current specialist status files;
- relevant Type studies;
- relevant Color studies;
- relevant Layout/Interaction studies;
- applicable cross-cutting research and prior case studies.

Ask:

- What has already been established?
- Which findings transfer directly?
- Which findings require contextual validation?
- Which known limitations matter here?
- Which specialist dependency must be resolved?

Deliverable: project evidence map with reusable findings and open gaps.

## Phase 3 — Targeted external research

Only after internal evidence retrieval, investigate material gaps through:

- primary standards and specifications;
- peer-reviewed research;
- platform guidance;
- direct competitors when useful;
- adjacent product categories;
- editorial/industrial/graphic precedents;
- domain-specific artifacts and workflows.

Do not research broadly for its own sake. Prioritize questions that could alter the design decision.

Deliverable: gap-focused evidence update.

## Phase 4 — Frame

For every core surface or flow define:

1. the question the user is trying to answer;
2. the primary object/value;
3. the primary action;
4. state and feedback requirements;
5. supporting information;
6. secondary navigation;
7. what can be removed or deferred;
8. where Type, Color and Layout/Interaction each materially affect the solution.

Deliverable: information and interaction hierarchy before styling.

## Phase 5 — Compose / model alternatives

Produce multiple materially different viable approaches when a meaningful choice exists. Do not vary only color, radius or decorative details.

For each option identify:

- Type strategy;
- Color strategy;
- Layout / spatial strategy;
- Interaction/state strategy;
- accessibility implications;
- localization/data stress behavior;
- implementation risk;
- assumptions and trade-offs.

Deliverable: alternatives with explicit rationale.

## Phase 6 — Recommend

Do not stop at presenting options when the available evidence supports a recommendation.

State:

- preferred direction;
- why it best fits this product/user/task context;
- which specialist findings support it;
- what is intentionally rejected;
- where uncertainty remains;
- what evidence would change the recommendation.

Deliverable: actionable project recommendation.

## Phase 7 — Critique

Evaluate:

- clarity;
- task fit;
- hierarchy;
- interaction legibility;
- visual authorship;
- genericness;
- information density;
- typography;
- color behavior;
- spatial coherence;
- accessibility path;
- cross-surface coherence;
- localization/data stress;
- implementation risk.

Label major decisions KEEP / REWORK / REJECT.

## Phase 8 — Validate

Test representative stress cases:

- narrow/large viewport;
- large text;
- long and multilingual labels;
- keyboard/focus states;
- touch/pointer differences where relevant;
- empty/error/loading/pending;
- async failure and recovery;
- real user data and numerical density;
- grayscale/color-vision-independent comprehension;
- low/high glare when relevant;
- reduced motion;
- target-device rendering;
- both physical orientation directions where relevant.

Deliverable: evidence-backed validation report, not a claim of quality from static mockups alone.

## Phase 9 — Reconcile with engineering

Only after the design proposition is coherent:

- identify required product-contract changes;
- classify implementation difficulty;
- distinguish essential design intent from negotiable technique;
- define fallbacks without pretending they are preferred designs;
- document compromises explicitly;
- identify which compromises require later design re-validation.

## Phase 10 — Production review

Compare implemented output with accepted design intent on real target devices. Treat discrepancies as design/implementation issues to resolve, not silent drift.

## Phase 11 — Preserve project knowledge correctly

Project-specific decisions stay in:

- `case-studies/<project>/`, or
- the project's own repository.

Do not promote a project choice to a universal Design Studio rule merely because it worked once.

After enough evidence exists, extract only genuinely transferable lessons into the appropriate specialist research/methods layer and link back to the case study.

## Expected specialist answer to a project request

A useful project answer should normally contain:

1. **Diagnosis** — what problem actually needs solving;
2. **Applicable evidence** — what existing research transfers;
3. **Options** — materially different viable paths if appropriate;
4. **Recommendation** — what this project should do;
5. **Rationale** — why;
6. **Cross-specialist implications** — Type / Color / Layout-Interaction interactions;
7. **Trade-offs and risks**;
8. **Validation criteria**;
9. **Unknowns** that could materially alter the answer.

The specialist should not respond with a generic lecture when the user needs a project decision.

## Anti-patterns

- research volume becomes the success metric;
- completing a curriculum stage matters more than answering a live project need;
- theory is recited without translating it into a project decision;
- the specialist proposes a design before understanding product/user/task context;
- one specialist ignores reusable findings from the others;
- engineering schema becomes the screen hierarchy by default;
- component library determines composition;
- design review begins with “what is easiest to implement?”;
- visual references are copied as motifs;
- accessibility is postponed until handoff;
- every project inherits the previous project's visual language;
- one successful project decision is promoted into a universal rule without transfer evidence.