# CD096 — Pointer reorder complete content contract

Status: Stage 3 PRACTICE / LOCALIZATION + HUMAN EVIDENCE OPEN

## Source truth
Movement copy must be generated from semantic object ID/name, action, destination/result, transaction result, recovery scope and persistence truth. Visual ordinal is presentation data, not object identity.

Protected invariants:
- drag ≠ semantic action;
- Move Up/Down ≠ Saved/Synced;
- destination chosen ≠ mutation succeeded;
- boundary no-op ≠ failure;
- hidden ≠ deleted;
- moved object ≠ currently focused object;
- recovery available ≠ recovery applied.

## Complete-system integration
Forms/state: movement must not corrupt an active editor or validation state.
Onboarding/discoverability: if movement controls require a mode, entry/exit and consequences need explicit semantics.
Retrieval: reordered fields must remain findable by stable names/IDs, not remembered row numbers.
Tone: concise operational consequence first; avoid celebratory copy for routine reordering.
Localization: action labels, object names, position phrases and status messages must survive EN/KO expansion without relying on English word order.

## Evidence
Validate visible label, accessible name, status payload and Undo consequence against the same I077 transaction. Actual EN/KO runtime and linguistic review remain OPEN; do not claim localization closure from source strings alone.
