# I072 — Intervening Action, Undo Causality, and Focus Agency

Date: 2026-09-18
Stage: Stage 3 PRACTICE
Purpose: TRANSFER VALIDATION / CONTRADICTION REVIEW extending I071.

## RELATED DOMAIN CHECK
- Type T053: restoration/status strings are transfer corpus; Type may not solve behavioral ambiguity by compression.
- Color C084: restored, focused, selected and recovery-available are independent states.
- Layout L075: semantic focus owner is declared before geometry is judged.
- Web W084: runtime evidence must record restored object and current focus owner separately.
- Content CD090: configuration restoration is not focus return and Undo is not Saved/Synced.

## SOURCE
WCAG 2.2 remains the studio accessibility baseline. SC 2.4.3 requires sequential focus order to preserve meaning and operability. SC 4.1.3 requires qualifying status messages to be programmatically determinable without receiving focus. WAI-ARIA APG Button guidance states that when activation does not dismiss the current context, focus typically remains on the button; when workflow logically changes context, another destination can be appropriate. APG is pattern guidance, not product compatibility proof.

Sources:
- https://www.w3.org/TR/WCAG22/
- https://www.w3.org/WAI/ARIA/apg/patterns/button/
- https://www.w3.org/WAI/ARIA/apg/patterns/tabs/

## PROBLEM
I071 asks whether Undo restoration should also restore focus. A harder case occurs when the user performs another meaningful action between the destructive mutation and Undo. Automatic return to the originally restored object can then override newer user agency.

Example:
1. focus object O;
2. Hide O → focus fallback F;
3. user explicitly focuses/acts on G;
4. user invokes Undo for Hide O;
5. O is restored.

Configuration restoration is attributable to transaction T1. Current focus/agency may now be attributable to later action A2. T1's inverse must not silently erase A2's interaction locus merely because O exists again.

## PRACTICE — CAUSALITY LEDGER
Record for every mutation/recovery sequence:
- transaction_id and inverse_of;
- semantic object changed;
- focus owner before mutation;
- fallback owner and reason;
- intervening action ID, semantic owner, input path and timestamp/order;
- Undo invocation locus;
- restored object;
- focus owner after Undo;
- whether any scroll/reveal was author-triggered;
- status payload and recovery availability.

Test families, twice per executable input path:
A. Hide O → immediate Undo.
B. Hide O → focus G only → Undo.
C. Hide O → operate G → Undo.
D. Hide O → reorder G → Undo T1 if still eligible.
E. Hide O → Reset → attempt stale Undo.
F. Hide O → navigation away/back → Undo if contract permits.

## CRITIQUE
Three policies remain viable hypotheses, not conclusions:
1. **Invocation-locus preservation:** keep focus on the Undo control if it remains operable.
2. **Latest-agency preservation:** if the user deliberately moved/acted after T1, preserve the newer semantic locus.
3. **Explicit return:** return to restored O only where product workflow makes that destination clearly more logical and the reason is recorded.

Automatic restored-object focus is rejected as a default inference. It confuses state inversion with user-intent inversion. Conversely, never returning focus is also not universal: a workflow may have an explicit logical destination.

## REPRODUCIBLE ACCEPTANCE
PASS requires:
- Undo restores only the eligible transaction state;
- intervening semantic actions are not silently reversed;
- focus owner after Undo is explainable by a declared policy and current causal ledger, never by stale visual index;
- no root/body focus loss;
- no false status claiming focus return, save or sync;
- repeated execution yields the same semantic result for the same policy/input path.

FAIL if restored O steals focus solely because it reappears after a later deliberate action, if stale Undo reverses a superseding Reset, or if ordinal position rather than semantic identity determines focus.

## PRODUCT TRANSFER
LogMate Customize should not choose a final policy until hide/group-collapse/Reset/Undo runtime exists. Non-drag single-pointer reorder remains an upstream accessibility/product-transfer blocker for the broader I063–I072 chain.

## HUMAN EVIDENCE BOUNDARY
Discoverability, preference, workload, screen-reader comprehension and representative-pilot task performance remain OPEN. No simulation is a human PASS.

## HANDOFFS TO OTHER SPECIALISTS
- Layout: measure displacement only after I072 resolves semantic destination.
- Color: visually separate restored object, current focus owner and recovery control.
- Content: report restoration result without fabricating focus movement.
- Web: capture causal ledger in served runtime and independent engine.
- Type: stress resulting strings after drawing/spacing gates, not before.