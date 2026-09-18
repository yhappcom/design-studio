# L069 — Recovery Surface, Interaction Locus & Reflow Architecture

Status: **STAGE 3 PRACTICE / OPEN RUNTIME**  
Purpose: **EXTENSION** of L067/L068 for reversible reorder without spatial instability.

## RELATED DOMAIN CHECK
Type T046 protects operational strings from geometry-driven compression. Color C077 protects focus/state orthogonality. I064 protects post-move semantic locus; I065 adds reversal. W077 supplies browser geometry evidence. CD083 supplies structured consequence truth.

## SOURCE / SYNTHESIS
WCAG 2.2 remains the accessibility baseline. Focus must remain visible/not obscured at the applicable conformance level, and 2.5.8 constrains pointer-target size. WCAG 4.1.3 allows status messages to be exposed without forcing focus onto them. WAI APG scrollable listbox guidance explicitly keeps the active option visible when programmatic focus representation changes.

## Spatial question
Where can recovery live after a reorder without covering the moved row, shifting the control target between repeated moves, or forcing 200% text into unstable geometry?

## Architectures to compare
1. **Inline row recovery** — strongest object proximity; highest row-height/wrap mutation risk.
2. **Sticky local recovery rail** — stable location; can obscure list content/focus if viewport is short.
3. **Non-modal bottom status/Undo surface** — preserves row geometry; may be distant from the manipulated object and can collide with safe-area/keyboard.
4. **Top-level persistent action area** — predictable but high travel distance and weaker local attribution.

## Measurement matrix
For each architecture record at baseline and 200% text:
- viewport and safe-area dimensions;
- moved-row and focused-target bounding boxes;
- recovery target bounding box and 24×24 CSS px minimum check where Web applies;
- scroll offset before move, after move, after Undo;
- overlap with sticky/app bars, keyboard and safe-area regions;
- row-height change and wrap count;
- whether repeated move controls remain in a stable reachable region;
- semantic neighbor before/after/undo.

## Acceptance
- Recovery does not obscure the moved/focused control.
- Adding/removing recovery UI does not create unintended large scroll jumps.
- At 200% text, semantic content and recovery action remain available without truncating necessary labels solely for fit.
- Undo returns the spatial/semantic list state coherently; exact pixel scroll restoration is not required if the same semantic locus remains visible and understandable.
- Reset remains a separate architecture/action.

## CRITIQUE
A transient snackbar can look spatially cheap while stealing usable viewport height or covering bottom rows. Inline Undo can maximize proximity while moving every following row. Therefore placement must be judged by mutation geometry, not by static screenshots.

## OPEN
No architecture PASS until the non-drag path and recovery semantics exist in product runtime. Human motor/cognitive workload remains deferred.

## HANDOFFS TO OTHER SPECIALISTS
Interaction receives spatial failure modes for I065. Web receives exact geometry fields. Color receives overlap/state-layer requirements. Content receives available string budget as evidence, not permission to delete semantics. Type receives only reproduced rendering failures.