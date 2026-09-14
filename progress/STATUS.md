# Design Studio Global Status

Governance model: **three current specialist roles + coordinator + future specialist onboarding**
Governance sync: 2026-09-14
Current operating state: **ACTIVE — ALL CURRENT SPECIALISTS MAY RESUME RESEARCH**

This is the coordinator-maintained studio summary. Specialists must not edit this file during ordinary research work.

Detailed specialist status lives in:

- Type: `progress/TYPE_STATUS.md`
- Color: `progress/COLOR_STATUS.md`
- Layout & Interaction: `progress/LAYOUT_STATUS.md`

## Status vocabulary

- `NOT STARTED` — not yet studied
- `IN STUDY` — source study underway
- `PRACTICE` — exercises underway
- `CRITIQUE` — work exists and is being evaluated
- `PASS` — evidence satisfies the gate
- `REVISIT` — later work exposed a foundational gap
- `ACTIVE` — research may proceed

The previous owner-imposed pause was temporary and has been lifted.

## Current specialist map

| Specialist | Canonical research | Specialist status | Current stage/state |
| --- | --- | --- | --- |
| Typography / Type Design | `research/type/` | `progress/TYPE_STATUS.md` | Stage 1; PRACTICE / CRITIQUE; ACTIVE |
| Color | `research/color/` | `progress/COLOR_STATUS.md` | Stage 1 with early intermediate bridge; CRITIQUE; ACTIVE |
| Layout, Spatial & Interaction | `research/layout/`, `research/interaction/` | `progress/LAYOUT_STATUS.md` | Stage 1; CRITIQUE in studied modules; ACTIVE |

These are primary/canonical ownership roles, not intellectual silos. A specialist may study adjacent domains when the overlap has a useful reason such as replication, independent validation, method comparison, contradiction review, transfer testing, prerequisite learning, or project-specific research.

Future specialists may be added through the onboarding and ownership-definition protocol in `AGENTS.md` and `coordination/ONBOARDING.md`.

## Cross-cutting evidence

Accessibility, Human Factors, research methodology, platform behavior and other shared concerns are not currently separate specialist roles. Existing evidence remains valid and may be used or independently investigated by all specialists when useful.

Examples:

- `research/004-accessibility-reflow-targets-focus.md`
- related `product-design/exercises/` evidence

Interaction is owned by the **Layout, Spatial & Interaction Specialist**, while its evidence remains separately indexed in `research/interaction/` to avoid mixing spatial and temporal/behavioral claims.

## Current Foundation picture

### Typography / Type Design

Established: type system/anatomy foundations, metrics/spacing, construction/Bezier/optics, numerals/punctuation study, typography as information architecture, original exercises and critique.

Main unresolved gates: real raster/source proof, native numeral/punctuation outlines, broader family/system proof, platform scaling/reflow, multilingual/fallback validation.

### Color

Established: luminance/contrast hierarchy, RGB→linear→XYZ foundations, LMS/observer foundations, chromatic adaptation, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, numerical exercises and critique.

Main unresolved gates: official spectral integration, observer comparison, browser/device gamut validation, ICC/CMM round trip, bounded CAT comparison, physical-display/environmental validation.

### Layout, Spatial & Interaction

Established spatial evidence: grid/composition hierarchy, responsive transfer, perceptual grouping/spatial grammar, plus L001 source-grounded study/practice/critique covering figure-ground/border ownership, visual mass/balance/tension, and optical-centering method.

Established interaction evidence: agency/feedback/errors, state/modes/directness/reversibility, state-matrix practice and critique.

L001 advances three former gaps to `PRACTICE / CRITIQUE`; it does **not** justify PASS because controlled human comparison, actual-size raster/device proof, exact balance datasets, multilingual/RTL transfer, and repeated failure→revision evidence remain open.

Main unresolved gates: stronger figure-ground/balance/optical validation, explicit whitespace/density/rhythm study, real-browser multilingual/enlarged-text transfer, running navigation/state prototype, keyboard/focus/status validation, and async failure/recovery proof.

## Mandatory mutual-awareness rule

Before any specialist begins a new substantial work block, it must:

1. read this global status;
2. read **all specialist status files**;
3. inspect related canonical research from the other specialists;
4. identify reusable, uncertain, disputed, or test-worthy peer evidence;
5. decide whether to reuse, independently verify, challenge, transfer-test, or extend that evidence;
6. record this in the new study under `RELATED DOMAIN CHECK`.

After a study finishes, identify `HANDOFFS TO OTHER SPECIALISTS` whenever its findings could help another domain.

The objective is **active shared learning**, not absolute non-duplication.

## Overlap rule

Duplicate or overlapping research is allowed when it has a stated purpose.

Valid reasons include:

- replication / calculation check;
- independent validation;
- adversarial review;
- contradiction investigation;
- method / standard / dataset comparison;
- cross-domain or project transfer validation;
- prerequisite learning needed to correctly apply peer work;
- second-specialist interpretation;
- project urgency or risk reduction.

Avoid only repetition that adds no new analytical value.

When overlap is deliberate, label its purpose and link to the peer canonical evidence.

## Concurrency rules

1. Each specialist ordinarily edits only its own canonical research paths and its own specialist status file.
2. Cross-domain verification may be stored in the investigating specialist's own writable area with explicit links and overlap rationale.
3. Specialists do not edit this global status, `AGENTS.md`, global indexes, curriculum, coordination documents, or another specialist's files unless explicitly authorized.
4. No specialist moves, renames, deletes or renumbers existing research during ordinary study work.
5. Existing studies `001`–`017` retain their identifiers.
6. New studies use collision-resistant prefixes:
   - Type `T###`
   - Color `C###`
   - Layout `L###`
   - Interaction `I###` under the Layout & Interaction specialist
   - future specialist prefix assigned by coordinator
   - coordinator/shared cross-cutting `X###` when needed
7. Conflicting conclusions are preserved and reviewed rather than silently overwritten.

## Future specialist entry

A new specialist chat first reads:

- `AGENTS.md`
- root `README.md`
- this global status
- every existing specialist status file
- `research/README.md`
- relevant specialist/domain README files
- `coordination/ONBOARDING.md`
- `coordination/COLLABORATION_PROTOCOL.md`

It then submits an onboarding report defining proposed primary ownership, overlap/collaboration opportunities, reusable or test-worthy existing evidence, unique contribution, canonical path and proposed prefix.

Approval is required before creating a new canonical specialist structure. It is not required merely to learn, critique, or reason about overlapping topics.

## Current next-work queues

Research may resume immediately. Specialists should use their own status files plus the following principles:

- live project need takes priority;
- close important evidence gaps when they materially improve reliability;
- answer dependencies that help peers;
- independently verify or challenge high-impact peer findings when useful;
- expand breadth where doing so increases professional capability;
- do not restrict learning merely to avoid overlap.

In broad terms:

- Type can continue raster/native-outline/scaling work and may also pursue useful cross-domain validation;
- Color can continue spectral/browser/ICC/device work and may also pursue useful cross-domain validation;
- Layout & Interaction should convert L001 into stronger observer/rendering evidence, explicitly study whitespace/density/rhythm, and advance the running interaction prototype while using or independently testing Type/Color evidence where necessary.

## Curriculum progression

The studio uses five stages:

1. Foundation
2. Intermediate professional practice
3. Advanced / systems practice
4. Production and authorship
5. Research and advisory

No stage or specialist is considered complete from reading alone.

## Completion rule

No global mastery announcement until required curriculum gates are `PASS` with linked evidence and the specialist can explain, critique, apply, defend, revise, independently assess peer evidence, identify uncertainty, collaborate across domains, and advise across realistic project constraints.

The final measure is project usefulness, not research volume.
