# W007 — Performance-Sensitive Design: Priority, Progressive Rendering & Interaction Readiness

Status: **PRACTICE / CRITIQUE**  
Evidence intent: **WEB-SPECIFIC FOUNDATION + TRANSFER VALIDATION**  
Date: 2026-09-15

## PURPOSE

Establish a design-led Web performance baseline. The question is not “how do we maximize a benchmark?” but:

> Which content, controls and relationships must become perceptible and usable first, what may arrive later, and which visual/interaction choices create runtime cost that undermines the intended hierarchy?

Performance is therefore treated as a design constraint on **priority, stability, continuity and readiness**, not as an engineering afterthought.

## RELATED DOMAIN CHECK

### Type

Checked `progress/TYPE_STATUS.md`, especially T016. T016 demonstrates a concrete Type→Web performance/layout contract: delayed preferred-font loading can change width, wrapping and downstream geometry, while failure can make fallback geometry persistent. W007 reuses this as **TRANSFER VALIDATION**: font loading strategy changes what the user sees first and whether later rendering destabilizes hierarchy.

### Color

Checked `progress/COLOR_STATUS.md`. Color Stage 1 is PASS, but browser/device/production Color remains later-stage work. W007 does not invent a performance threshold for color. It records that heavy visual effects, image-based color treatments or duplicated themed assets must justify their runtime cost; semantic color itself is not treated as a performance problem.

### Layout / Interaction

Checked `progress/LAYOUT_STATUS.md`. L002/L003/L006 and I001/I002 are directly reusable: reflow and font changes can alter geometry; loading/pending/status are interaction states; visual ownership and operational ownership are separate. W007 transfers those findings to page-load and interaction-readiness sequencing rather than redefining them.

### Web

Checked W001–W006 status. W001 established browser/runtime participation; W002 demonstrated failure→revision under layout stress; W003 owns adaptation; W004 owns resource/history/direct entry; W005 owns semantic components; W006 owns region-level loading/error/recovery. W007 adds the missing Foundation question: **what should load/paint/become interactive first, and why?**

### Why overlap is useful

This is **TRANSFER VALIDATION**, not duplicate performance engineering. Existing Type/Layout/Interaction findings are tested as inputs to Web priority and progressive-rendering decisions.

---

## SOURCE

### W3C Web Performance

The W3C Web Performance Working Group maintains specifications including Performance Timeline, Resource Timing, Navigation Timing, Paint Timing, Event Timing and Largest Contentful Paint. These APIs provide measurement primitives; they do not prescribe a universal visual design.

### HTML image loading and priority

The current HTML Standard defines:

- `loading` as a lazy-loading policy for images outside the viewport;
- `fetchpriority` as a fetch-priority hint;
- responsive image selection via `srcset` / `sizes` and preload equivalents;
- a recommendation to provide image dimensions/aspect-ratio information so late image loading does not shift layout.

These are browser primitives. They do not mean every visible image should be eagerly loaded or every hero image should receive high priority.

### Performance metrics as diagnostics, not design goals

Current Web performance tooling exposes paint, resource, navigation and event timing. W007 uses metrics to test whether a design decision preserves intended priority and readiness. It rejects optimizing a metric by hiding, deleting or delaying product-critical content without a task rationale.

---

## CORE MODEL

Performance-sensitive Web design is modeled as:

`user task`
`→ information/action priority`
`→ critical visible structure`
`→ resource dependency`
`→ fetch/decode/execute/render cost`
`→ first truthful presentation`
`→ interaction readiness`
`→ progressive enrichment`
`→ stable continuation`
`→ measurement`

A useful design contract records, for each major region:

1. **task value** — why the region matters;
2. **first truthful state** — what can be shown before all data/assets arrive;
3. **critical resources** — what is actually required for that state;
4. **deferrable enrichment** — what may arrive later without breaking meaning;
5. **geometry reservation** — how later content avoids destructive reflow;
6. **interaction readiness** — whether visible controls are operational, pending, unavailable or merely decorative;
7. **failure state** — what remains usable when a resource fails;
8. **measurement** — what browser evidence would confirm or falsify the decision.

---

## PERFORMANCE BUDGET IS NOT ONLY BYTES

A design can be expensive through several distinct channels:

- transfer bytes;
- request discovery/priority;
- image decode and raster cost;
- font loading and swap geometry;
- script parse/compile/execute work;
- style/layout/paint work;
- animation/compositing work;
- hydration or client startup before controls work;
- repeated work after interaction;
- instability caused by late geometry changes.

**STUDIO JUDGMENT:** A design review should ask “what work does this visual/interaction choice force the browser to perform before the user can perceive or act on the primary task?” rather than reducing performance to total page weight.

---

## PRIORITY CONTRACT

### Tier A — task-critical now

Examples:
- page identity and primary heading;
- primary task/navigation controls;
- above-fold content needed to decide the next action;
- dimensions/placeholders required to preserve stable geometry;
- semantic/status information needed to interpret the current state.

These should not depend unnecessarily on ornamental media or nonessential script.

### Tier B — context-critical soon

Examples:
- secondary summary regions;
- immediately adjacent comparison data;
- next-step content likely to be used after the first decision.

These may render progressively if the first state remains truthful.

### Tier C — enrich later

Examples:
- below-fold editorial imagery;
- optional visualization detail;
- nonessential motion;
- tertiary recommendation panels;
- decorative media.

Deferral is acceptable only if later insertion preserves hierarchy and does not steal focus or unexpectedly move the active task.

**STUDIO JUDGMENT:** DOM/source order, visual prominence and network priority need not be numerically identical, but contradictions must be intentional and justified.

---

## THREE DESIGN DIRECTIONS

### Direction A — Showcase-first

Large media, custom fonts, motion and rich visual treatment dominate initial presentation.

**KEEP when:** brand/visual inspection is itself the primary user task and the media is genuinely content-critical.

**REWORK when:** the same hierarchy can be preserved with responsive assets, reserved geometry, staged motion or fewer critical resources.

**REJECT when:** task controls or page identity wait behind ornamental resources, or the design looks complete before it is operable.

### Direction B — Task-first progressive shell

Semantic page identity, primary actions and stable structural geometry arrive first; secondary data/media enrich regions progressively.

**KEEP when:** the user arrives to inspect, compare, search, edit or continue work.

**REWORK when:** the shell becomes a skeleton-screen theatre that exposes no truthful content or creates excessive placeholder churn.

**REJECT when:** progressive loading fragments a task that must be understood atomically.

### Direction C — Snapshot-first resilient workspace

A recent valid snapshot/cached state is immediately usable and freshness/revalidation is explicit; network results update bounded regions.

**KEEP when:** product semantics permit stale-but-labeled data and continuity matters.

**REWORK when:** freshness affects only some fields; mark ownership at the smallest truthful region.

**REJECT when:** stale data is unsafe, misleading or invalid for the task.

### Foundation default

For ordinary task-oriented Web products, prefer **Direction B — task-first progressive shell** unless product semantics justify showcase-first or snapshot-first behavior.

This is not a universal rule for marketing/editorial experiences.

---

## FAILURE → REVISION EXERCISES

### Failure 1 — “Hero” priority based on visual size alone

A large decorative image receives eager/high-priority treatment while the actual task summary and controls depend on later script/data.

**Revision:** define priority from task value and dependency chain. A visually large asset is high priority only if it is critical to the first truthful task state.

### Failure 2 — lazy-loading everything

Above-fold/task-critical media is delayed because “lazy is faster.”

**Revision:** lazy loading is a resource policy, not a virtue. Defer resources that are genuinely outside the immediate task/viewport need; do not mechanically lazy-load critical content.

### Failure 3 — skeleton as fake readiness

A polished skeleton resembles the final interface, but controls are not operable and status is unclear.

**Revision:** visually distinguish unresolved/pending state and expose the earliest truthful, usable subset. Do not imply readiness that does not exist.

### Failure 4 — late content shifts the task

Images, fonts or asynchronous regions arrive without reserved geometry and move the control the user is reading or activating.

**Revision:** reserve truthful geometry where dimensions are known; design robust wrapping/recomposition where exact geometry is not known; treat font loading/failure as a real state per T016.

### Failure 5 — remove content to improve a metric

Product-critical context is hidden or deferred solely to improve a lab score.

**Revision:** use measurement to locate expensive dependencies, then reduce/replace/reorder cost while preserving task semantics. A faster incomplete task is not automatically a better design.

---

## RESOURCE-SPECIFIC DESIGN QUESTIONS

### Images

- Is this content, brand-critical context, or decoration?
- Is it in the first task viewport?
- Can responsive selection avoid downloading unnecessary resolution?
- Are intrinsic dimensions/aspect ratio known so space can be reserved?
- Would art direction change meaning at narrow widths?
- If it fails, is the text/task still intelligible?

### Fonts

- Is the custom face required to understand hierarchy, or primarily brand expression?
- What is visible during load and after failure?
- Does fallback change line breaks or action geometry?
- Is metric adjustment justified for the exact pair?
- Are unnecessary families/weights/styles being made critical?

### Script / interactive enhancement

- Does visible UI require script before it can perform its advertised action?
- Can navigation/form semantics work before enhancement?
- Which interactions genuinely require application code?
- Does deferred code preserve focus, status and current task context when it activates?

### Motion / visual effects

- Does motion explain state/causality or merely decorate?
- Does the effect require heavy raster/paint/compositing work?
- Can reduced-motion/user preferences preserve the information contract?
- Is visual sophistication worth delaying primary task readiness?

---

## MEASUREMENT PLAN

W007 does **not** claim measured browser PASS in this run.

A future executable specimen should compare the same task surface under at least three transfers:

1. **showcase-heavy failure** — critical hero/font/script competition, late geometry;
2. **task-first revision** — critical semantic content/actions first, reserved geometry, deferred enrichment;
3. **snapshot-first variant** — cached labeled state + bounded revalidation where semantically valid.

Measure:

- request start/order and transferred resource classes using Resource Timing;
- paint/LCP candidate timing where supported;
- layout instability attributable to late assets/fonts;
- time at which primary controls are both visible **and operable**;
- focus/active-element continuity during progressive insertion;
- content geometry before/after enrichment;
- behavior under failed image/font/data/script requests;
- narrow viewport and long Korean/English content.

A benchmark score alone is insufficient. The harness must assert product invariants such as “primary task remains available,” “late content does not displace active controls,” and “failure leaves a truthful recovery state.”

---

## PROJECT-READINESS TEST

### When to use

Use this model whenever a Web design includes custom fonts, substantial images/media, client-side application code, asynchronous data, progressive regions, motion, or performance-sensitive target devices/networks.

### When not to use as a blunt rule

Do not force every static/local/intranet page into elaborate progressive-loading architecture. Do not trade away correctness, accessibility, security, privacy or essential content to optimize a score.

### Inputs required

- primary user tasks and arrival routes;
- content/resource inventory;
- first-viewport composition by breakpoint/container;
- font/media strategy;
- data and interaction dependencies;
- target browser/device/network constraints;
- freshness/offline semantics;
- failure/recovery requirements.

### Concrete decisions changed

- whether an image is eager/lazy/high-priority/deferrable;
- which font resources are critical;
- whether a region can render from cached/partial data;
- whether a control should be visible before its behavior is ready;
- where geometry must be reserved;
- whether animation or rich effects justify their runtime cost;
- whether content is server/native-first or enhancement-dependent;
- which measurements are acceptance criteria.

---

## SYNTHESIS

1. **Performance is hierarchy over time.** Visual hierarchy at a finished screenshot is incomplete if the runtime presents a different priority sequence.
2. **First paint is not first usefulness.** A surface may look populated while primary controls are unavailable or meaning is unresolved.
3. **Progressive rendering requires semantic ownership.** W006 region ownership determines which parts may resolve independently.
4. **Stability is a design property.** Late media/font/data insertion must not casually destroy reading position, focus or target geometry.
5. **Resource hints are implementation tools, not design policy.** `loading`, `fetchpriority`, preload and responsive images should implement a task-priority decision, not substitute for one.
6. **Measurement must preserve product invariants.** Better timing numbers do not justify removing necessary context or creating misleading readiness.

---

## STUDIO JUDGMENT

For task-oriented Web products, the default review order is:

`primary task`
`→ first truthful state`
`→ visible/operable controls`
`→ stable geometry`
`→ essential context`
`→ progressive enrichment`
`→ optional visual sophistication`.

A finished visual comp should therefore include a **temporal composition specification**: what appears first, what can lag, what must reserve space, what may fail, and what remains usable.

---

## OPEN

- executable W007 browser specimen and measured request/paint/layout/readiness evidence;
- actual Core Web Vitals field evidence on a live project;
- W003–W006 integrated execution in the same complete task surface;
- exact production font/image/script stack;
- cache cold/warm, bfcache and navigation transfer;
- CPU/network throttling on representative physical devices;
- Firefox/Safari/mobile browser comparison;
- actual keyboard/AT behavior during progressive insertion;
- service worker/offline strategy where project semantics require it;
- human perceived-speed/task-completion evidence, deferred to project/app validation where required.

---

## HANDOFFS TO OTHER SPECIALISTS

### Type

W007 transfers T016 into a page-level priority/stability contract: font load/failure is part of temporal composition. Future Type work should expose exact fallback geometry and critical font-role assumptions for Web consumers.

### Color

Performance optimization must not silently remove state semantics or contrast. If visual effects/assets are reduced, semantic Color roles remain canonical; Color should review any production change that materially changes appearance or state differentiation.

### Layout / Interaction

W007 extends L003/I002 into temporal composition: layout and interaction readiness should be validated before and after enrichment. Progressive insertion must preserve focus/context and not imply an operable state before behavior exists.

---

## EVIDENCE LEVEL

**SOURCE + SYNTHESIS + PRACTICE / CRITIQUE + TRANSFER VALIDATION.**

No measured browser PASS is claimed. The next useful step is an executable task-surface specimen/harness, followed by a Web Foundation closure audit only after integrated project evidence exists.