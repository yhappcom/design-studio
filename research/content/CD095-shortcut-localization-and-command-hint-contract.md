# CD095 — Shortcut localization and command-hint contract

Date: 2026-09-19
Stage: 3 PRACTICE
Purpose: extend CD094 from IME ownership into truthful platform/layout shortcut communication.

## RELATED DOMAIN CHECK
I076 owns actual command identity/routing. L080 owns placement/reflow. C089 owns visual state separation. W089 owns browser/platform evidence. T058 owns later rendering transfer.

## CONTENT MODEL
Generate user-facing shortcut content only from: `semantic action`, `platform`, `supported activator`, `scope`, `eligibility`, `focused context`, `composition state`, and `result`. Keep action name and shortcut hint separate data fields so localization never changes command identity.

Protected invariants: `key glyph ≠ semantic action`; `physical key ≠ produced character`; `shortcut recognized ≠ action applied`; `text Undo ≠ configuration Undo ≠ browser Back`; `composing ≠ committed`; `available ≠ failed ≠ superseded`; `applied locally ≠ Saved/Synced`.

## PRACTICE / CRITIQUE
Stress EN/KO action labels with platform hints such as Ctrl/Cmd combinations, but do not freeze literal Korean copy before runtime and linguistic review. Prefer the semantic action as primary text; hint is supporting metadata. Reject copy that tells users a shortcut is available when I076 cannot prove the route, or that reports success from the chord rather than the resolved result.

## REPRODUCIBLE VALIDATION
For each runtime scenario record source payload, rendered visible string, accessibility payload, locale, platform and resulting action. Compare concise visible feedback with richer accessibility content at baseline/200%. Human comprehension and linguistic naturalness require human review and remain OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Layout receives worst-case strings/hints. Type receives mixed Korean/Latin/key-symbol corpus after T021. Color receives semantic eligibility, never prose-derived color meaning. Web must prove the activator and result before Content can claim availability.