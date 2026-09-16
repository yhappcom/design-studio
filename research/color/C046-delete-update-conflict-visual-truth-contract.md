# C046 — Delete/Update Conflict Visual Truth Contract

## PURPOSE
Stage-3 systems practice extending C045 partial-order merge into destructive concurrency: one branch deletes an object while another branch updates it. This is a `TRANSFER VALIDATION` of the merge model because deletion introduces absence/tombstone semantics that ordinary branch comparison does not cover.

## SYSTEM TRUTH
Color may encode but must never decide whether an object is live, deleted, pending deletion, restored, conflicted, or unavailable. The authority/comparison contract comes from Interaction. A later wall-clock update must not visually resurrect an authoritative deletion, and a visually dominant destructive color must not imply that deletion is already confirmed.

Required distinct states where the product exposes them: `live-confirmed`, `delete-pending`, `delete-outcome-unknown`, `delete-update-conflict`, `deleted-confirmed`, `restore-pending`, `restore-outcome-unknown`, `restored-confirmed`, `object-unavailable`.

## VISUAL PRECEDENCE
1. current authoritative existence/consequence;
2. action safety and unresolved conflict;
3. operation certainty;
4. destructive/restore affordance;
5. focus, selection and brand emphasis.

Historical success, red/destructive styling, row removal animation, selection or receive-time recency cannot outrank current authority.

## ADVERSARIAL MATRIX
Evaluate the shared W046 artifact under: hue removal, icon removal, grayscale, forced-colors, background suppression, selected-row emphasis, keyboard focus, print/export, 200% text/reflow, and stale optimistic deletion. PASS requires the non-color semantic path to preserve existence/conflict/certainty and the visual hierarchy not to fabricate resurrection or confirmed deletion.

## RELATED DOMAIN CHECK
- Type: T021 remains provisional; mature fallback is required for operational identifiers.
- Layout/Interaction: I033 owns delete/update/tombstone truth; L037 owns spatial continuity when an object disappears or reappears.
- Web: W046 must supply executed runtime/export evidence with shared object/branch/delete/restore IDs.
- Content: CD052 must distinguish deleted, deletion pending, outcome unknown, conflict and restored without color-dependent wording.
- UX: human noticeability/trust remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
Return any case where visual removal or destructive emphasis disagrees with I033 authority to Interaction/Web. Content must provide explicit non-color consequence language; Layout must preserve a discoverable path to history/recovery when the live row disappears.

## EVIDENCE BOUNDARY
Contract ready; no executed artifact, calibrated display, CVD/low-vision observer, physical print/device, or human PASS.