# Design Studio Global Status

Governance model: **three current specialist roles + coordinator + future specialist onboarding**
Governance sync: 2026-09-14
Current operating state: **ALL CURRENT SPECIALISTS PAUSED BY OWNER**

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
- `PAUSED` — deliberately stopped; no new work begins until explicitly restarted

## Current specialist map

| Specialist | Canonical research | Specialist status | Current stage/state |
| --- | --- | --- | --- |
| Typography / Type Design | `research/type/` | `progress/TYPE_STATUS.md` | Stage 1; PRACTICE / CRITIQUE; PAUSED |
| Color | `research/color/` | `progress/COLOR_STATUS.md` | Stage 1 with early intermediate bridge; CRITIQUE; PAUSED |
| Layout, Spatial & Interaction | `research/layout/`, `research/interaction/` | `progress/LAYOUT_STATUS.md` | Stage 1; CRITIQUE in studied modules; PAUSED |

These are the current specialist roles, not a permanently closed list. Future specialists may be added only through the onboarding and ownership-definition protocol in `AGENTS.md` and `coordination/ONBOARDING.md`.

## Cross-cutting evidence

Accessibility, Human Factors, research methodology, platform behavior and other shared concerns are not currently separate specialist roles. Existing evidence remains valid and may be used by all specialists.

Examples:

- `research/004-accessibility-reflow-targets-focus.md`
- related `product-design/exercises/` evidence

Interaction is no longer a fourth independent specialist: it is owned by the **Layout, Spatial & Interaction Specialist**, while its evidence remains separately indexed in `research/interaction/` to avoid mixing spatial and temporal/behavioral claims.

## Current Foundation picture

### Typography / Type Design

Established: type system/anatomy foundations, metrics/spacing, construction/Bezier/optics, numerals/punctuation study, typography as information architecture, original exercises and critique.

Main unresolved gates: real raster/source proof, native numeral/punctuation outlines, broader family/system proof, platform scaling/reflow, multilingual/fallback validation.

### Color

Established: luminance/contrast hierarchy, RGB→linear→XYZ foundations, LMS/observer foundations, chromatic adaptation, perceptual spaces/difference, gamut mapping, perceptual ramp authoring, numerical exercises and critique.

Main unresolved gates: official spectral integration, observer comparison, browser/device gamut validation, ICC/CMM round trip, bounded CAT comparison, physical-display/environmental validation.

### Layout, Spatial & Interaction

Established spatial evidence: grid/composition hierarchy, responsive transfer, perceptual grouping/spatial grammar and critique of grouping conflicts.

Established interaction evidence: agency/feedback/errors, state/modes/directness/reversibility, state-matrix practice and critique.

Main unresolved gates: figure-ground/border ownership, visual mass/balance/tension, optical centering, explicit whitespace/density/rhythm study, real-browser multilingual/enlarged-text transfer, running navigation/state prototype, keyboard/focus/status validation, and async failure/recovery proof.

## Mandatory mutual-awareness rule

Before any specialist begins a new substantial work block, it must:

1. read this global status;
2. read **all specialist status files**;
3. inspect related canonical research from the other specialists;
4. identify reusable evidence before planning new work;
5. confirm the question is not already answered or actively being studied elsewhere;
6. record this in the new study under `RELATED DOMAIN CHECK`.

After a study finishes, it must identify `HANDOFFS TO OTHER SPECIALISTS` whenever its findings could help another domain.

The objective is not only non-duplication. The objective is active reuse of one another's research.

## Concurrency rules

1. Each specialist edits only its own canonical research paths and its own specialist status file.
2. Specialists do not edit this global status, `AGENTS.md`, global indexes, curriculum, coordination documents, or another specialist's files unless explicitly authorized.
3. No specialist moves, renames, deletes or renumbers existing research during ordinary study work.
4. Existing studies `001`–`017` retain their identifiers.
5. New studies use collision-resistant prefixes:
   - Type `T###`
   - Color `C###`
   - Layout `L###`
   - Interaction `I###` under the Layout & Interaction specialist
   - future specialist prefix assigned by coordinator
   - coordinator-owned cross-cutting `X###` when needed
6. Dependencies are recorded in the requesting specialist's own status instead of solved by duplicating another domain.
7. Conflicting conclusions are preserved and escalated to coordinator review rather than silently overwritten.

## Future specialist entry

A new specialist chat must not begin research immediately. It must first read:

- `AGENTS.md`
- root `README.md`
- this global status
- every existing specialist status file
- `research/README.md`
- relevant specialist/domain README files
- `coordination/ONBOARDING.md`
- `coordination/COLLABORATION_PROTOCOL.md`

It then submits an onboarding report defining its unique scope, overlap risks, reusable existing evidence, canonical path and proposed prefix. No research files are created until the user/coordinator approves the boundary.

## Current next-work queues

All queues are **paused** until explicitly restarted.

When restarted, specialists follow their own status files. In broad terms:

- Type closes raster/native-outline/scaling evidence gaps before expanding breadth.
- Color closes spectral/browser/ICC/device validation gaps before expanding breadth.
- Layout & Interaction deepens spatial foundations and builds running interaction validation before expanding breadth.

## Curriculum progression

The studio uses five stages:

1. Foundation
2. Intermediate professional practice
3. Advanced / systems practice
4. Production and authorship
5. Research and advisory

No stage or specialist is considered complete from reading alone.

## Completion rule

No global mastery announcement until all required curriculum gates are `PASS` with linked evidence and the specialist can explain, critique, apply, defend, revise, integrate peer-domain evidence, identify uncertainty, and advise across realistic constraints.