# Layout, Spatial & Interaction Specialist Status

Operating state: **ACTIVE — STAGE 1 PASSED / STAGE 2 ENTRY AUDIT NEXT**  
Governance sync: 2026-09-15  
Canonical paths: `research/layout/`, `research/interaction/`  
Next new-study IDs: Layout `L008`; Interaction `I007`

This file is maintained by the Layout, Spatial & Interaction Specialist. It does not update global `progress/STATUS.md` during ordinary research.

## Mission / current level

Research exists to improve real app, web and product decisions. Research volume is not the objective.

Stage 1 — Foundations: **PASS**  
Next curriculum step: **Stage 2 — Intermediate Professional Practice / entry audit pending**

This PASS is deliberately narrow. L007 re-read the actual `curriculum/MASTER_CURRICULUM.md` and separated Foundation requirements from later production, platform, human and research gates.

Human-observer/user-task validation remains **DEFERRED TO APP-DEVELOPMENT VALIDATION** exactly as instructed by the user. No human evidence is fabricated or implied.

Stage 1 PASS does **not** mean:
- production/browser/device/AT validation is complete;
- every individual module has no OPEN items;
- Stage 2+ is passed;
- the specialist curriculum is complete.

The coordinator-maintained `progress/STATUS.md` may remain stale until coordinator sync. This specialist does not edit it directly.

---

## Four-specialist sync

- **Type:** through T015 at latest synchronized checkpoint; cross-browser/native/production shaping remains Type-owned.
- **Color:** Stage 1 PASS after C014/C015 closure; no production/device/human Color completion is inferred.
- **Web:** W001 completed; W002 next. Web has a Stage 1 baseline, not production integration PASS.
- **Layout/Interaction:** Stage 1 PASS established by L007; Stage 2 entry audit next.

---

# Stage 1 closure authority — L007

Canonical:
- `research/layout/L007-stage1-foundation-closure-audit.md`

L007 maps every Master Stage 1 visual and interaction requirement to existing original evidence and corrects the earlier stage-boundary error in which Stage 3–5/platform/human gaps were treated as perpetual Foundation blockers.

## Visual Foundation verdict

**PASS under the current Master Curriculum Stage 1 gate.**

Evidence map:
- figure/ground + Gestalt → Study 014, L001, L006;
- visual mass / balance / tension → L001 + raster practice;
- proportion / scale → Study 006 + Exercises 003/007;
- rhythm / repetition → Study 006 + Exercise 003 + L002;
- contrast → Exercise 003 + L001 + L005;
- negative space → Study 014 + L002;
- edge relationships → L001/L006;
- grid systems / intentional grid breaking → Study 006 + Exercises 003/007 + responsive transfer;
- color perception / luminance / simultaneous contrast → canonical Color Stage 1 PASS reused, especially C015;
- typography as composition / IA → Type Study 009 + Exercise 006 reused, with L003/L004 browser transfer;
- design history / precedent literacy → Study 006 modernist grid precedent + reaction/critique;
- original exercises and peer-domain reuse → satisfied across L001–L006 and legacy exercises.

## Interaction Foundation verdict

**PASS under the current Master Curriculum Stage 1 gate.**

Evidence map:
- affordance / feedback / mapping / consistency → Study 007 + Exercise 004 + I002/L006;
- recognition vs recall → Study 007 + Exercise 004;
- task/object/action relationships → Studies 007/015;
- navigation models → I001 **14/14**;
- system status / error prevention → Study 007 + Exercise 004 + I002 **19/19**;
- reversibility / modes / recovery → Study 015 + I002/I004;
- accessibility as a design constraint → research/004 + Exercise 001 + I001/I003/L006;
- original exercises / peer reuse → satisfied across I001–I006 and cross-specialist transfers.

Important historical correction:
- Study 007/015 originally withheld PASS because interactive prototype, keyboard traversal and navigation/state evidence were missing;
- later I001/I002/I003/L006 directly supplied those gaps.

---

## Canonical evidence

### Layout / spatial
- `006-grid-composition-hierarchy.md`
- `014-perceptual-grouping-spatial-grammar.md`
- `L001-figure-ground-balance-optical-centering.md`
- `L001-optical-centering-raster-validation.md`
- `L001-border-ownership-cue-isolation-validation.md`
- `L002-whitespace-density-spatial-rhythm.md` + **216-condition** validation
- `L003-type-fallback-density-reflow-transfer.md`
- `L004-tabular-numerals-dense-comparison-transfer.md`
- `L005-color-driven-density-salience-transfer.md`
- `L006-layer-ownership-cross-contract.md` and four higher-fidelity extensions
- `L007-stage1-foundation-closure-audit.md`

### Interaction
- `007-interaction-agency-feedback-errors.md`
- `015-directness-state-modes-reversibility.md`
- `I001-navigation-history-focus-restoration-interruption.md` + **14** assertions
- `I002-latency-pending-optimistic-retry.md` + **19** assertions
- `I003-forced-colors-state-semantic-resilience.md` + **14** assertions
- I004 concurrency/offline family: **17 + 16 + 18 + 15 + 20 + 18** controlled assertions across state, HTTP, durable reconnect, ambiguous outcome, multi-operation queue, and authorization/finalization
- `I005-ambiguous-outcome-idempotency.md` + **18** assertions
- `I005-business-effect-dedupe-atomicity-transfer.md` + **26** assertions
- `I006-sequence-collaboration-ot-crdt-boundary.md` + **18** assertions

Shared accessibility baseline: `research/004-accessibility-reflow-targets-focus.md`.

---

# Current reusable evidence beyond Foundation

## L006 — layer ownership

Ownership vector:

`visual owner / pointer hit owner / active gesture-capture owner / keyboard-focus owner / semantic-AT owner / action-data owner / layer-stack position / restoration target`

Five controlled layers:
- custom ownership **15/15**;
- native popover/dialog **13/13**;
- pointer capture/dismissal/lost invoker **13/13**;
- forced-colors/touch implicit capture/Chromium AX **28/28**;
- custom `aria-modal=true` versus actual modality **14/14**.

Standing rules:
- screenshot appearance cannot prove operational ownership;
- `aria-modal=true` describes but does not implement modality;
- pointer capture can survive modal entry;
- forced-colors can remove authored elevation while behavior remains foreground-owned;
- AX-tree evidence is not screen-reader PASS.

## I004 — concurrency / offline / queue

Six evidence layers:
- conflict state machine **17/17**;
- real HTTP ETag/If-Match **16/16**;
- durable offline/restart/reconnect **18/18**;
- applied-but-response-lost operation identity **15/15**;
- ordering/compaction/dependencies/temp identity **20/20**;
- authorization/finalization/account switch **18/18**.

Standing rules:
- historical base, current authoritative state and local intent are separate;
- retry is not conflict resolution;
- queue is a dependency-aware preserved-intention structure, not just FIFO requests;
- compaction safety depends on operation algebra, not path equality;
- actor/account, authorization and workflow mutability are part of queued-operation validity.

## I005 — duplicate-sensitive intent / atomicity

Stable-intent HTTP replication/extension: **18/18**.

Atomicity extension: **26/26**.

Key finding:

> Idempotency protection is only as strong as the atomicity or reconciliation boundary connecting the protected business effect and the dedupe result.

Evidence distinguishes:
- same-DB split commit duplicate failure;
- same-DB effect+ledger transaction;
- external-provider/local-ledger dual-write failure;
- provider-owned stable operation identity;
- transactional outbox producer boundary;
- duplicate delivery and consumer inbox/dedupe boundary.

Do not claim generic `exactly once` without naming effect/store/consumer/failure boundary.

## I006 — sequence collaboration boundary

Controlled matrix: **18/18**.

Key finding:

> Convergence, intent preservation and domain-semantic correctness are different gates.

Whole-field LWW and raw index replay can be structurally inadequate for concurrently authored sequences. OT/CRDT/serialization/locking/domain-specific operations should be considered only when product requirements justify a sequence-aware model.

The I006 OT-like/CRDT-like controls are didactic boundary evidence, not production algorithm proofs.

---

# Individual module state after Stage 1 PASS

Stage 1 PASS does not erase later validation gaps.

| Area | Current evidence state | Later-stage/open work |
| --- | --- | --- |
| Figure-ground / grouping / balance / optical centering | PRACTICE / CRITIQUE beyond Foundation | app-stage human judgments; physical/platform transfer |
| Grid / whitespace / density / responsive | PRACTICE / CRITIQUE beyond Foundation | Stage 2 multi-solution/product systems; real zoom/cross-browser/device |
| Type-dependent spatial robustness | PRACTICE / CRITIQUE | exact production fonts/packages/shaping/platform transfer |
| Color-driven spatial salience | PRACTICE / CRITIQUE | physical environment/device/human transfer |
| Layer ownership | PRACTICE / CRITIQUE | real OS/AT, Firefox/Safari, physical mobile, production frameworks |
| Navigation/state | CRITIQUE beyond Foundation | complete product/router/multi-form-factor transfer |
| Async/retry/cancel | PRACTICE / CRITIQUE | production API/proxy/background-sync/AT |
| Concurrent/offline sync | PRACTICE / CRITIQUE | production DB/storage/multi-device/security/operations |
| Duplicate-sensitive intent | PRACTICE / CRITIQUE | production provider/gateway/distributed guarantees |
| Sequence collaboration | PRACTICE / CRITIQUE | production OT/CRDT/editor integration only when product requires it |

---

# Stage 2 entry policy

The Master Curriculum Stage 2 gate requires **multiple solutions to the same problem and a defended selected direction using explicit criteria, including correct adjacent-specialist evidence reuse**.

Stage 2 topics relevant to this specialist include:
- task analysis and primary-question framing;
- information hierarchy and IA;
- dense-data vs low-density composition;
- forms, tables, search, settings, empty/error/loading states;
- responsive/adaptive composition;
- iconography and non-text signals;
- component systems without component-driven sameness;
- interaction states, async behavior and recovery paths;
- comparative studies / hypothesis / experiment design / KEEP-REWORK-REJECT critique / dependency handoffs.

Existing L002–L006/I001–I006 provide substantial **early Stage 2 evidence**, but Stage 2 is not passed. The next step is an explicit entry audit rather than more unstructured expansion.

---

## Active next queue

1. **Stage 2 entry audit** against the exact Master Curriculum; map existing evidence and identify only genuine intermediate-practice gaps.
2. Use the audit to select the next project-useful exercise, likely one requiring multiple materially different complete solutions rather than another isolated mechanism proof.
3. Consume W001/W002+ and current Type/Color evidence where the Stage 2 task depends on them.
4. Production/platform studies remain active when the required environment becomes available, but are no longer mislabeled as Foundation blockers.
5. Open `L008` or `I007` according to the highest-value Stage 2 gap revealed by the audit.

## APP-DEVELOPMENT VALIDATION queue

Execute with live app/prototype and suitable participants:
- L001 border ownership and optical-centering judgments;
- L002/L005/C007 task performance/error vs preference/workload;
- L006 layer comprehension/dismissal expectations;
- I004/I005 sync/conflict/retry/authorization-recovery comprehension;
- I006 collaborative-editing comprehension if relevant to a live product;
- real accessibility-user validation.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type
- Layout Stage 1 typography-as-composition requirement is satisfied by correct reuse of Type Study 009/Exercise 006 plus Layout browser transfer; no Type production PASS is inferred.
- I006 operation identity must not be confused with Unicode/grapheme/shaping identity.

### Color
- Color C014 directly exposed the same stage-boundary problem and informed L007's audit method.
- L005/C007 and I003/C011 remain strong valid transfer examples.

### Web Design
- W001 is reused as independent support for relationship-preserving Web composition.
- Production Web integration remains later evidence, not a Foundation prerequisite.
- Highest-value future transfers remain L006 overlay ownership and I004/I005 sync/retry contracts; I006 only if a real collaborative editor exists.

---

## Latest checkpoint

- **Stage 1 — Foundations: PASS** by L007 audit under the current Master Curriculum.
- No human/production/platform PASS is implied.
- `L001`–`L006` and `I001`–`I006` retain their own higher-fidelity OPEN items.
- Next IDs: Layout `L008`; Interaction `I007`.
- Next action: **Stage 2 entry audit**.
