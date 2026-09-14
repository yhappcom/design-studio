# L008 — Stage 2 Intermediate Professional Practice Entry Audit

Status: **ENTRY AUDIT / Stage 2 NOT PASSED — substantial early evidence exists; remaining work narrowed to integrated product-practice gaps rather than more isolated mechanism studies**

Owner: Layout, Spatial & Interaction Specialist

## Question

After Stage 1 Foundation PASS, which Stage 2 requirements are already supported by accumulated Layout/Interaction evidence, and which still require genuinely new intermediate-practice work?

The objective is to avoid two opposite errors:

1. repeating already-proven mechanisms simply to accumulate studies;
2. promoting Stage 2 because many advanced technical experiments exist while integrated product-design practice remains incomplete.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: Type Study 009/Exercise 006 plus current Type status through T015.
- Reusable finding: semantic text-role systems and dense numeric/table behavior already have strong peer evidence.
- Stage 2 consequence: Layout should reuse Type role architecture rather than create a duplicate typography system.

### Color
- Evidence checked: Color Stage 1 PASS and existing semantic-token/data-color evidence.
- Reusable finding: Color can encode hierarchy/state after Interaction semantics and Layout relationships are defined.
- Stage 2 consequence: future integrated surfaces should use Color evidence as a constraint, not use Color to repair weak IA/component structure.

### Layout / Interaction
- Evidence checked: L001–L007, I001–I006, Studies 006/007/014/015, Exercises 003/004/007.
- Reusable finding: responsive composition, density, async/recovery, navigation, conflict and layered ownership are already much stronger than a normal Stage 2 entry baseline.
- Main uncertainty: whether those mechanism-level findings have been integrated into complete product workflows with task analysis, forms/search/settings/empty states, component architecture and non-text signal systems.

### Web Design
- Evidence checked: W001 and current Web status.
- Reusable finding: complete Web surfaces should begin from purpose/task → content/source order → relationship model rather than screenshot coordinates.
- Stage 2 consequence: Web W002+ should become a transfer partner for complete page/product exercises, not a prerequisite for non-Web product practice.

### Master Curriculum
Stage 2 Information and Product Design requires:
- task analysis and primary-question framing;
- information hierarchy and IA;
- dense-data vs low-density composition;
- forms, tables, search, settings, empty/error/loading states;
- responsive/adaptive composition;
- typography systems across multiple roles;
- iconography and non-text signals;
- component systems without component-driven sameness;
- interaction states, async behavior and recovery paths.

Stage 2 Research/Critique requires:
- precedent analysis without imitation;
- comparative studies;
- hypothesis/experiment design;
- critique vocabulary;
- KEEP/REWORK/REJECT rationale;
- identifying genericness, novelty-for-novelty and implementation bias;
- dependency/handoff discipline.

Stage 2 gate:

> produce multiple solutions to the same problem and defend the selected direction using explicit criteria, including evidence borrowed correctly from adjacent specialties.

### Overlap decision
**ENTRY AUDIT + EVIDENCE MAPPING + CAPSTONE PLANNING**.

---

# Stage 2 requirement matrix

| Requirement | Existing evidence | Audit verdict |
| --- | --- | --- |
| Task analysis / primary-question framing | W001 method; many studies define research questions; interaction models define intent/object/action | **PARTIAL** — no canonical complete task-analysis exercise driving a full product workflow |
| Information hierarchy / IA | Study 006, Exercises 003/007, Type Study 009 reuse, I001 navigation state, W001 | **STRONG / SATISFIED FOR ENTRY** |
| Dense-data vs low-density composition | L002; Exercise 007 archive↔editorial transfer; L004 dense numeric table | **STRONG / SATISFIED FOR ENTRY** |
| Forms | Exercise 004 includes save/edit/error semantics but not a full form system | **PARTIAL** |
| Tables | Type Exercise 006 + L004 numeric geometry | **STRONG / SATISFIED FOR ENTRY** |
| Search | navigation/search discussed, but no complete search/filter result-state exercise | **OPEN** |
| Settings | no canonical settings IA/state/component exercise identified | **OPEN** |
| Empty state | no dedicated integrated product exercise identified | **OPEN** |
| Error/loading states | Study 007, Exercise 004, I002 | **STRONG / SATISFIED FOR ENTRY** |
| Responsive/adaptive composition | Exercise 007, L002, L003, W001 | **STRONG / SATISFIED FOR ENTRY** |
| Typography across multiple roles | Type Study 009/Exercise 006 reused; L003/L004 browser transfer | **SATISFIED BY PEER REUSE** |
| Iconography / non-text signals | L001 icon centering; I003 non-color state resilience; Exercise 004 icon/gesture critique | **PARTIAL** — geometry/state evidence exists, but no coherent meaning/discoverability/fallback system |
| Component systems without sameness | individual components/patterns exist, but no canonical component-architecture exercise balancing reuse vs page/task differentiation | **OPEN** |
| Interaction states / async / recovery | I001–I005, Study 015 | **STRONG / EXCEEDS ENTRY BASELINE** |
| Precedent analysis without imitation | Study 006 modernist grid + reaction; W001 Web history | **SATISFIED FOR ENTRY** |
| Comparative studies | Exercise 003, L002 policy comparison, L005/C007 independent validation | **STRONG** |
| Hypothesis / experiment design | L001–L006, I002–I006 controlled failure→revision studies | **STRONG** |
| Critique vocabulary / KEEP-REWORK-REJECT | Exercises 003/004/006/007 and study dispositions | **STRONG** |
| Genericness / novelty-for-novelty | Study 006 grid-break burden; Study 007 navigation novelty burden; component sameness still needs direct exercise | **PARTIAL** |
| Implementation bias | W001 canvas-transplant critique; I004/I005 implementation/semantic separation | **STRONG** |
| Cross-specialist dependencies / handoffs | RELATED DOMAIN CHECK + handoffs throughout L/I series | **STRONG** |
| Multiple solutions + defended direction | Exercise 003 three composition hypotheses; L002 naive/preserve/adaptive; explicit selection criteria | **SATISFIED AS METHOD EVIDENCE** |

---

# Audit conclusion

Stage 2 is **NOT PASSED**.

The missing work is not more latency thresholds, more ETag variants, or more isolated Chromium component mechanics.

The actual remaining Intermediate Professional Practice gaps are product-integration gaps:

1. **Task analysis → complete workflow**
   - identify users/tasks/objects/primary questions;
   - derive IA and interaction priorities from those tasks rather than from components.

2. **Integrated form/search/settings/empty-state practice**
   - build states as one coherent product system rather than isolated patterns;
   - include error/loading/partial/recovery already informed by I002/I004.

3. **Component architecture without component-driven sameness**
   - decide what deserves reuse;
   - allow page/task-specific composition where semantic structure differs;
   - reject “everything is the same card/list row” as a false design-system goal.

4. **Iconography / non-text semantic system**
   - distinguish decoration, status, action, destination and data mark;
   - define labels/accessible names/alternatives;
   - test recognition burden and color/shape redundancy without requiring human data at this stage.

5. **Integrated alternatives + selection at product scale**
   - existing multiple-solution method evidence is strong, but the next capstone should apply it to a complete workflow rather than an isolated composition.

---

# Recommended integrated capstone

Rather than creating four unrelated studies, use one product-workflow capstone with **three materially different architecture hypotheses**.

Required content/states:
- one primary user task and one secondary task;
- browse/list or dashboard surface;
- search/filter;
- add/edit form;
- settings or preference surface tied to the task;
- populated, empty, loading, partial, error and recovery states;
- one dense comparison region/table;
- responsive narrow recomposition;
- labeled/non-text signals;
- reusable components plus at least one justified page-specific composition;
- explicit navigation/state model;
- async save/retry/outcome policy;
- Type/Color peer evidence reused;
- three alternatives with explicit criteria and KEEP/REWORK/REJECT critique.

The capstone should not become a production app redesign. It is a controlled Intermediate Practice exercise that can later transfer into MintTap, LogMate or another live project.

---

# Suggested evaluation criteria

Score/critique each architecture against explicit criteria rather than taste:

- primary-task directness;
- information priority;
- comparison efficiency supported by structure;
- discoverability / recognition burden;
- state visibility;
- error/recovery preservation;
- responsive relationship survival;
- localization/text-growth resilience;
- component reuse where semantics actually repeat;
- avoidance of false component sameness;
- accessibility structure;
- implementation risk;
- peer-domain compatibility;
- cost of future change.

Do not convert this into one generic numeric UX score. Criteria can conflict and require reasoned trade-offs.

---

# What remains for later stages, not this capstone

- human task-performance statistics;
- real AT users;
- three-form-factor coherent identity system;
- production framework/browser/device matrices;
- production backend/provider architecture;
- full design-system governance;
- end-to-end production handoff.

These remain active but should not be smuggled into the Stage 2 gate.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Stage 2 capstone should reuse Type role systems and actual fallback/number-format risks rather than design new fonts.

### Color
- Capstone should reuse semantic Color roles but hold Interaction meaning independent of hue.

### Web Design
- W001/W002 can independently transfer-test the selected architecture in a real Web medium; Layout should not prescribe Web coordinates.

### Layout / Interaction
- Next research should prioritize **integrated workflow architecture and component-system judgment**, not another isolated mechanism proof unless a live-project risk justifies it.

---

# Entry verdict

**Stage 2 — Intermediate Professional Practice: NOT PASSED / READY FOR INTEGRATED CAPSTONE.**

Strong existing evidence reduces the missing work to a small number of product-integration questions. The next high-value study should be a complete multi-solution workflow capstone rather than another Foundation-style topic survey.
