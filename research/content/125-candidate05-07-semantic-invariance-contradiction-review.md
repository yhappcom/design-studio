# CD125 — Candidate 05/07 Semantic-Invariance Contradiction Review

Date: 2026-09-20
State: **CONTRADICTION REVIEW / TRANSFER VALIDATION — STAGE 3 PRACTICE, NOT PASS**

## PURPOSE
Determine whether materially different Home concepts require different product vocabulary, or whether semantic/content invariants should remain stable while visual expression changes.

## RELATED DOMAIN CHECK
- **Type:** T088 rejects semantic shortening as a fit fix.
- **Color:** C119 allows palette diversity while preserving semantic-state meaning.
- **Layout/Interaction:** I106/L110 separate action/state truth and protected relationships from presentation.
- **Web:** W117/W118 require visible and accessibility payload from the same runtime build.
- **Content:** CD123/CD124 already keep canonical English labels immutable-first per candidate.

## CONTRADICTION REVIEW
Concept novelty is not a user need for vocabulary novelty. Candidate 05 and Candidate 07 can look materially different while the same object/action/destination continues to use the same stable product term.

Reusable invariants:
1. same destination/action/object keeps the same canonical term unless product semantics actually change;
2. visible label/icon meaning, accessible name/role/state and actual action/destination must agree;
3. wording does not claim Search, Saved, Synced, Offline, recovery or other state that Interaction has not established;
4. pending, failure, ambiguous outcome, local persistence and sync acknowledgement remain distinct when the product can distinguish them;
5. geometry stress is handed first to Type/Layout rather than silently solved by abbreviation;
6. product-authored LogMate UI remains English-only under current project direction; source/user Unicode and locale-sensitive date/numeric data remain stress inputs rather than a reason to invent localized product copy.

Concept variables may include non-semantic editorial framing or optional descriptive hierarchy only where it does not rename stable product concepts or imply unsupported behavior.

## PRACTICE / CRITIQUE
Reject renaming the same Home destination/action merely to make Candidate 07 feel more editorial or Candidate 05 more instrument-like. Reject the opposite error of forcing identical visual prominence for identical words; semantic consistency does not require identical typography or placement.

## REPRODUCIBLE VALIDATION
From exact Candidate 05 and 07 builds, extract visible strings plus accessibility names/roles/states and map each to actual Interaction authority. Repeat after max text scaling, fallback and adaptive reflow. Any wording change must be classified as semantic change, evidence-backed clarity repair or unjustified fit/style churn.

## RESULT
The comparison supports **semantic invariance with presentation diversity**. This is stronger than per-candidate copy review because it can expose style-driven terminology drift. No Content Stage 3 PASS.

## OPEN
Exact runtime/a11y extraction, Search/state/recovery implementation, linguistic review, AT comprehension and representative-pilot comprehension/task evidence.

## HANDOFFS TO OTHER SPECIALISTS
Interaction remains authority for action/state truth. Type/Layout should absorb legitimate string growth. Color must not require color-referential wording. Web should compare visible and accessibility payload from the same build across candidates.