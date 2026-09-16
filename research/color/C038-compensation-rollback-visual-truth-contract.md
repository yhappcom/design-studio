# C038 — Compensation / rollback visual-truth contract

Date: 2026-09-16
Evidence purpose: **SYSTEMS PRACTICE / ADVERSARIAL VALIDATION**

## RELATED DOMAIN CHECK
Type T021 remains pre-product; I025 defines compensation truth; L029 owns spatial continuity; W038 owns runtime provenance; CD044 owns compensation language. This study only owns visual encoding and cue precedence.

## Problem
After a concurrent mutation appears successful, later authority may require rollback or compensating action. A visually persistent success treatment can contradict the authoritative state even when text is corrected.

## State sequence to test
`pending → presented-success → authority-conflict → rollback-required/compensation-pending → reconciled-restored OR reconciled-alternate`.

## Visual truth rules
- transient success styling is presentation evidence, not authority evidence;
- rollback/compensation must not inherit confirmed-success emphasis merely because the optimistic surface previously did;
- focus and selection remain interaction cues, never proof that the rollback target is authoritative;
- brand/primary emphasis cannot visually outrank blocked/unsafe action semantics;
- semantic meaning must survive removal of authored hue and forced-colors substitution;
- conflict/rollback distinction needs a non-color channel supplied with Content/Layout, not a second hue alone.

## Adversarial matrix
Test: success hue persists after conflict; focused rollback button looks like confirmed state; selected stale row looks current; forced colors collapse conflict/restored distinction; disabled unsafe action retains dominant primary styling; long localized rollback explanation changes cue association.

Each case records semantic ID, action verdict, authored/computed visual tokens, non-color cue, focus state, forced-colors result, and L029 geometry/association result under the same W038 run ID.

## Evidence boundary
Static token reasoning is PRACTICE, not browser transfer. C038 cannot PASS Stage 3 until executed browser captures prove computed state/focus/forced-colors behavior. Human salience/comprehension remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
I025 supplies authoritative compensation state; L029 supplies locality; CD044 supplies explicit language; W038 records computed styles and engine provenance; Type must preserve the unchanged strings after T021.