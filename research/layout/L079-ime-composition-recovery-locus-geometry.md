# L079 — IME composition and recovery-locus geometry

## Purpose
Transfer I075 command ownership into spatial evidence. Geometry must preserve the active editor/composition locus while configuration recovery remains available without visually or spatially impersonating the active text-history owner.

## RELATED DOMAIN CHECK
Type T056/T021, Color C087, Interaction I074/I075, Web W087 and Content CD093 were checked. Reuse I075 for behavioral ownership; this note owns only spatial/reflow consequences.

## SOURCE / SYNTHESIS
IME composition is platform/editor state, and candidate/composition UI can add transient visual occupancy. WCAG 2.2 reflow/focus-obscuration criteria remain accessibility floors, but they do not define where a configuration Undo surface belongs. Studio judgment: spatial proximity may cue ownership but must never redefine the runtime scope.

## PRACTICE
Compare at baseline and 200%:
1. editor focused with active Korean composition + local configuration recovery visible;
2. same state with sticky/page-level recovery;
3. composition commit causing helper/status expansion;
4. focus transfer editor → recovery control → editor;
5. narrow viewport with keyboard/IME-induced viewport change where executable.

Capture `editor_rect, focus_rect, recovery_rect, status_rect, viewport, visual_viewport if exposed, scroll offsets, overlap/obscuration, line count, semantic owner IDs`.

## CRITIQUE
FAIL when recovery obscures the active editor/focus, when a transient status causes unexplained large displacement, when 200% wrapping detaches the recovery control from its qualified scope, or when geometry makes non-owning configuration recovery look like editor Undo. Candidate-window behavior that is OS-owned must be recorded as platform evidence rather than simulated.

## REPRODUCIBLE VALIDATION
Use the identical I075 scenario IDs. Measure before composition, during composition, after commit, and after recovery invocation. Repeat twice. Interaction first determines semantic owner; Layout then judges visibility, displacement, reflow and ownership cue quality.

## OPEN
Real mobile virtual-keyboard/IME visual viewport behavior, desktop candidate windows, independent engines, physical devices and human workload remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Web should capture actual viewport/runtime geometry; Color must keep composition/focus/recovery cues separable; Content should not shorten necessary scope wording solely to preserve this layout; Type should test resulting strings only after its drawing gate permits.