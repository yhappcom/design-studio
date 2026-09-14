# I006 — Collaborative Sequence Semantics: When Record/Field Merge Stops Being Enough

Status: **PRACTICE + CRITIQUE / BOUNDARY STUDY + CONTROLLED SEQUENCE FAILURE→REVISION — whole-field loss, positional divergence, transform/stable-anchor convergence controls, tombstone policy, and semantic-conflict limit established; production OT/CRDT/library/network/app validation remains OPEN**

Owner: Layout, Spatial & Interaction Specialist — Interaction stream

Reproducible artifacts:
- `research/interaction/I006-sequence-collaboration-boundary-validation.py`
- `research/interaction/I006-sequence-collaboration-boundary-results.json`

## Question

I004's conflict model works well when a product can reason about records, fields, patches, dependencies, and explicit semantic conflicts.

But some user-authored data is inherently **sequential**:
- collaborative text;
- ordered lists;
- rich-text ranges;
- timelines;
- structured documents;
- sequence operations whose meaning depends on neighboring elements.

This study asks:

> At what point does `base record + changed fields + conditional save + manual merge` become structurally too coarse, and when does the product need a sequence-aware concurrency model such as Operational Transformation (OT), a CRDT, locking/serialization, or another domain-specific operation model?

The objective is **decision boundary literacy**, not implementing a production CRDT for research volume.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Latest Type status checked through **T015**.
- Reusable finding: Unicode representation, shaping and rendered text are separate layers.
- I006 operates on logical sequence operations, not glyph layout. A production text-collaboration system must decide whether positions/ranges are defined over code units, code points, grapheme clusters, document nodes or another semantic unit before connecting this work to Type/rendering.
- No Type shaping policy is claimed here.

### Color
- Color Stage 1 PASS acknowledged; production/device/human Color remains separate.
- Collaborative states such as local insertion, remote insertion, unresolved semantic conflict and deleted content are Interaction semantics first.
- No Color conclusion is claimed.

### Layout / Interaction
- I004 established `base/current/local`, semantically safe field merge, durable outboxes and operation dependencies.
- I004 also warned that text/list/order CRDT/OT behavior remained OPEN.
- I006 directly investigates that boundary.

### Web Design
- W001 is complete; next W002.
- Future Web transfer should test selection/caret/focus, composition/IME, browser editing events, network partition, offline persistence and production collaboration libraries.
- Current Python sequence controls are not browser/editor PASS.

### Other / foundational sources
Academic sources:
- C. A. Ellis and S. J. Gibbs, *Concurrency Control in Groupware Systems*, SIGMOD 1989, DOI: https://doi.org/10.1145/67544.66963
- Marc Shapiro et al., *Conflict-Free Replicated Data Types*, SSS 2011: https://pages.lip6.fr/Marc.Shapiro/papers/CRDTs_SSS-2011.pdf
- Martin Kleppmann and Alastair R. Beresford, *A Conflict-Free Replicated JSON Datatype*, IEEE TPDS 2017: https://doi.org/10.1109/TPDS.2017.2697382

Current implementation example:
- Automerge text/document documentation: https://automerge.org/docs/reference/documents/text/

Relevant source boundaries:
- Ellis/Gibbs describes concurrency control for fine-grained groupware and an operation-transformation approach whose algorithm depends on operation semantics.
- CRDT literature formalizes replicated datatypes designed so replicas can accept concurrent updates and converge when they have received the same updates.
- Kleppmann/Beresford shows that general JSON/list/map concurrent modification requires explicit merge semantics; it is not solved by ordinary sequential JSON mutation semantics alone.
- Automerge is an implementation example, not a universal design mandate.

### Overlap decision
**NEW INTERACTION BOUNDARY STUDY + FAILURE REPRODUCTION + METHOD COMPARISON**.

Why a new `I006`: the question is not another HTTP retry or record conflict. It asks when the **unit of interaction/concurrency itself must change from whole field/record state to sequence-aware operations**.

---

# Evidence boundary

The harness contains intentionally minimal **OT-like** and **CRDT-like stable-anchor** controls.

They are didactic models, **not production implementations** and not proofs of the full OT/CRDT algorithms in the cited literature.

Their purpose is to isolate the failure classes:
- lost concurrent intent;
- non-convergent positional replay;
- need for transformed/stable operation references;
- difference between technical convergence and semantic correctness.

Final bounded matrix: **18 / 18 assertions PASS**.

---

# 1. Whole-field last-write resolution loses fine-grained concurrent intent

Base text:

`AB`

Replica A inserts `X` between A/B:

`AXB`

Replica B concurrently inserts `Y` at the same logical position:

`AYB`

A deterministic whole-field last-writer policy chooses B's final string:

`AYB`

Observed:
- B's edit remains;
- A's `X` disappears.

## Finding

Whole-field LWW may converge, but convergence was achieved by **discarding one valid concurrent text intention**.

This can be an acceptable product policy for some scalar metadata. It is usually too coarse for collaborative text where preserving independent edits is a requirement.

---

# 2. Replaying raw positional operations can preserve both edits and still fail convergence

Both clients create the same kind of operation against base `AB`:

- A: insert `X` at index 1;
- B: insert `Y` at index 1.

Naive merge rule:

> Apply the remote operation using its original base index to the already locally edited string.

Replica A:

`AXB` + remote Y@1 → **`AYXB`**

Replica B:

`AYB` + remote X@1 → **`AXYB`**

Both replicas contain both `X` and `Y`, yet they disagree.

## Finding

**Preserving all payloads is not enough. Replicas also need a shared concurrency/order semantics.**

An integer position such as `index=1` is contextual to the sequence version from which it was created.

---

# 3. Minimal transform-aware control demonstrates why operation context matters

The lab's deliberately small OT-like control transforms a remote insert against a concurrent local insert.

For equal original indices, a deterministic actor ordering is used only as the bounded tie rule.

Observed:
- A transforms B's insert from index `1 → 2`;
- B keeps A's insert at index `1`;
- both replicas produce **`AXYB`**;
- both concurrent inserts remain present.

## Scope limit

This is not a production OT algorithm. Real text editors require much richer transform definitions across insert/delete/range/format operations and may use different correctness criteria.

## Synthesis

The useful lesson is not the toy tie-breaker. It is:

> When operations are position-relative, concurrent operations may need to be transformed relative to one another rather than replayed as if the base never changed.

---

# 4. Stable-anchor / operation-identity control demonstrates a CRDT-style design direction

The second didactic control does not address an insertion only by transient integer index.

Concurrent operations instead say conceptually:

- insert `X` after stable element `A`, op id `A:1`;
- insert `Y` after stable element `A`, op id `B:1`.

When both operations are known, deterministic ordering of concurrent children produces the same result regardless of delivery order:

`AXYB`

Observed:
- delivery `[X,Y]` → `AXYB`;
- delivery `[Y,X]` → `AXYB`;
- both changes survive.

## Scope limit

This is only a CRDT-like anchor/identity demonstration. It is not a full list/text CRDT and does not establish metadata, garbage collection, move, undo, rich-text or performance behavior.

## Synthesis

A sequence concurrency model may need **stable element/operation identity** so changes refer to logical structure rather than ephemeral array/string positions.

---

# 5. Delete + concurrent insert exposes the need for deletion/anchor policy

Base:

`ABC`

Concurrent operations:
- A deletes `B`;
- B inserts `X` after `B`.

If deletion physically destroys all knowledge of B immediately, B's insertion anchor becomes undefined.

The bounded control retains deleted B as a non-visible **tombstone anchor**.

Both delivery orders then render:

`AXC`

## Finding

Sequence systems need explicit semantics for references to concurrently deleted/moved elements.

A tombstone is one possible technique, not a universal product requirement. Production algorithms make different trade-offs around stable references, tombstone cleanup, move semantics and metadata growth.

---

# 6. Convergence is not the same as resolving the user's semantic conflict

Base ordered list:

`[A, B, C]`

Concurrent intentions:
- A moves `B` after `C` → `[A,C,B]`;
- B moves `B` before `A` → `[B,A,C]`.

A deterministic winner rule can make all replicas converge to one of these states.

The bounded control converges to:

`[B,A,C]`

But A's move intent is discarded.

## Finding

**CRDT/OT-style convergence cannot by itself decide every domain-semantic conflict.**

A product can have:
- technically convergent state;
- no lost bytes;
- and still violate one participant's meaningful intention or a business invariant.

Automatic conflict-free replication is therefore not equivalent to “the product always knows the right merged meaning.”

---

# 7. Whole-field conflict detection can also be too conservative

Base text:

`hello world`

Concurrent edits:
- A adds prefix `Hi, `;
- B adds suffix `!`.

A whole-field version model sees:
- local text changed;
- remote text changed;
- same field ⇒ conflict.

Yet a sequence-aware model can preserve both independent changes:

`Hi, hello world!`

## Finding

Coarse field conflict detection has two opposite failure modes:
- **under-protect:** LWW silently loses valid concurrent text edits;
- **over-escalate:** any same-field text modification becomes a manual conflict even when edits are independent.

---

# Decision boundary — when I004 field/record merge is enough

Field/record merge remains a good fit when most of the following hold:

- meaningful state consists largely of scalar/map values;
- concurrent edits to one field are rare or can legitimately choose one value;
- operations on different fields are semantically independent and can be proven so;
- manual resolution of the uncommon same-field conflict is acceptable;
- offline edits do not need fine-grained simultaneous coauthoring;
- order is not itself the main user-authored artifact.

Examples can include many settings, metadata records, forms and structured business objects.

---

# Decision boundary — when operation/sequence-aware collaboration deserves consideration

Investigate OT, CRDT or another sequence-aware model when requirements include several of:

- multiple replicas/users edit the **same text/list/document concurrently**;
- editing must remain responsive while offline/disconnected;
- independent concurrent changes should normally survive automatically;
- replicas must converge despite different message arrival order;
- positions/ranges shift under concurrent edits;
- ordered structure is itself meaningful user data;
- same-field conflicts would otherwise be frequent and burdensome;
- peer-to-peer or multi-master operation is important.

This still does not mean “use a CRDT automatically.” Alternatives can include:
- single-writer/lease/lock;
- server-serialized operations;
- explicit checkout;
- OT;
- CRDT;
- append-only domain operations;
- domain-specific merge;
- manual conflict resolution.

Choose according to latency, offline, topology, invariants, undo/history, storage, complexity and product consequences.

---

# Product inputs required before choosing OT/CRDT

1. What is the real collaborative datatype: scalar, set, counter, sequence, tree, rich text, graph?
2. What is the semantic editing unit: bytes, Unicode scalar values, grapheme clusters, words, document nodes, list items?
3. How many concurrent writers/replicas are expected?
4. Must edits work offline?
5. Is central serialization acceptable?
6. Which edits commute?
7. Which invariants must never be violated?
8. Is deterministic winner selection acceptable for concurrent assignments/moves?
9. Must all intentions remain inspectable even when one value wins?
10. What undo/history semantics are required?
11. How are identity, authorization and deletion represented?
12. What metadata/storage/performance cost is acceptable?
13. What happens when old/offline replicas reconnect after long periods?
14. Can schema/document semantics evolve while operations remain queued?

---

# Failure modes rejected

- using whole-field LWW for collaborative text merely because it converges;
- replaying index-based concurrent operations without transform/reference semantics;
- calling “both edits are present” sufficient when replicas disagree on order;
- assuming every CRDT automatically preserves every semantic intent;
- assuming technical convergence guarantees domain invariants;
- adopting CRDT/OT where ordinary versioned records/manual conflict are simpler and sufficient;
- implementing a collaboration algorithm without defining its text/list identity unit;
- tying cursor/range identity directly to unstable integer positions without a concurrency model;
- treating algorithm choice as purely backend engineering when it changes user-visible conflict, undo, offline and recovery behavior.

---

# Evidence limits / OPEN

This study does not establish:
- production OT correctness;
- production CRDT correctness;
- Automerge/Yjs/ProseMirror/Google Docs implementation equivalence;
- rich-text mark/annotation merge behavior;
- move-capable CRDT algorithms;
- Unicode grapheme/IME/editor event integration;
- cursor/selection awareness;
- collaborative undo/redo;
- schema evolution;
- metadata/tombstone garbage collection;
- network protocol/performance;
- malicious/untrusted replicas;
- authorization of individual operations;
- large-document scalability;
- production Flutter/Web/native integration;
- human collaboration quality.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- A production collaborative text model must define its logical text units before mapping operations to shaped/rasterized output.
- Unicode normalization, grapheme clusters, fallback and shaping should not be conflated with CRDT/OT operation identity.

### Color
- Local/remote/concurrent/unresolved states are semantic Interaction states. Color can support awareness but cannot establish merge correctness.

### Layout / Interaction
- I004 field merge is not a universal concurrency model.
- For sequence-authoring tasks, integer positions are version-relative and can become invalid under concurrency.
- **Convergence, intent preservation, and domain-semantic correctness are three different gates.**

### Web Design
- Real collaborative editor transfer must test browser `beforeinput`/IME/composition, selection/caret restoration, keyboard/focus, offline persistence, reconnect and the chosen production collaboration library.
- W001's relationship/state model applies: editing relationships and operation identity matter more than preserving static coordinates.

---

# Evidence level

**PRACTICE + CRITIQUE / sequence concurrency boundary study + deliberately minimal OT-like and stable-anchor CRDT-like controls.**

**18 / 18 bounded assertions PASS.**

I006 is **not PASS**. It establishes when the studio should ask for a stronger concurrency model, not a production collaborative editor implementation.
