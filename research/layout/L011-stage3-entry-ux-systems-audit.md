# L011 — Stage 3 Entry + UX Systems Audit

Classification: **STAGE ENTRY AUDIT + CROSS-DOMAIN UX SYNTHESIS**

## RELATED DOMAIN CHECK
- Type: custom LogMate family remains drawing-invalid; layout must tolerate current proportional control and future metric change.
- Color: Stage 2 PASS; C019 opens semantic multi-surface token work without allowing color-only state meaning.
- Web: W018 proves selected responsive/readiness behaviors in Chromium; true route/network and broader platform transfer remain open.
- Content: Stage 2 PASS supplies complete state/recovery and long-string semantics.
- UX is cross-cutting under current governance, not a new canonical specialist. This file owns spatial/interaction implications only.

## Entry question
Can Stage 3 practice begin without pretending that the existing L009 architecture is already a three-form-factor system?

## Audit
Stage 2 already proves task framing, multiple complete architectures, responsive reasoning, state/recovery modeling and critique. Stage 3 adds requirements not yet closed: coherent phone/tablet/desktop-web identity; navigation/state continuity across form factors; failure/interruption/recovery across surfaces; motion/reduced-motion equivalence; complex tables/long data; mixed-script/fallback stress; semantic token integration; human-factors/accessibility system behavior.

## Verdict
**Stage 3 ENTRY: OPEN / PRACTICE MAY BEGIN. Stage 3 NOT PASSED.**

## First three-form-factor UX contract
Fixed substrate: professional record lookup → inspect → compare → correct → confirm/recover.

Invariant across phone, tablet/EFB and desktop/web:
- same record identity and terminology;
- same truth states: idle, edited, pending, confirmed, known failure, outcome-unknown, offline/stale;
- destructive/irreversible consequences remain explicit;
- retry is exposed only when interaction contract says it is safe;
- selection, navigation history and transient overlays remain distinct state classes;
- recovery returns to a meaningful task context rather than merely a screen.

Adaptive, not invariant:
- density and simultaneous columns;
- persistent vs transient navigation;
- detail adjacency;
- pointer/touch/keyboard affordance presentation;
- disclosure depth.

## UX risk model
A cross-surface design fails before human testing if static/behavioral analysis shows any of these:
1. same state receives different action consequences by form factor without domain reason;
2. responsive recomposition changes reading/task order;
3. hidden navigation destroys recoverable context;
4. pending/outcome-unknown collapses to failure/success;
5. touch target or keyboard path is sacrificed to density;
6. long/localized content forces semantic deletion;
7. focus can be obscured by author-created sticky/transient UI;
8. visual color is the only state carrier;
9. motion is required to understand state change with no reduced-motion equivalent.

WCAG 2.2 integration boundary: Target Size (Minimum) AA uses 24×24 CSS px or specified spacing/equivalence exceptions on web; Focus Not Obscured (Minimum) AA requires focused components not be entirely hidden by author-created content. These are conformance constraints, not complete UX quality measures.

## Stage 3 executable sequence
1. formalize one state/navigation model shared by all three surfaces;
2. produce three compositions from that model;
3. stress with Content long strings, Type metric/fallback changes, Color adverse states;
4. test keyboard/focus and responsive ordering in Web where executable;
5. add reduced-motion equivalence;
6. only then evaluate system coherence gate.

## KEEP / REWORK / REJECT
KEEP: L009 Record-Centric architecture as a fixed task substrate, not a universal product answer.
REWORK: convert architecture into a three-surface invariant/adaptive contract.
REJECT: treating responsive scaling or component reuse alone as multi-surface coherence.

## HANDOFFS TO OTHER SPECIALISTS
- Color: state/surface inventory for multi-surface token work.
- Web: transfer focus, navigation, responsive order and recovery invariants into browser tests.
- Content: keep state names/actions semantically invariant while allowing surface-appropriate phrasing.
- Type: provide metric-change stress; Layout will not freeze around failed custom glyph geometry.

## Evidence boundary
No human findability, workload, preference, error-rate or recognition claim. No physical-device, native-router, AT or production backend PASS.