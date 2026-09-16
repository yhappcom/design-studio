# CD005 — Accessible, Input-Neutral Language and Non-Visual Reference

Status: **FOUNDATION — SOURCE STUDY + CROSS-DOMAIN TRANSFER + ORIGINAL PRACTICE / NOT A PASS CLAIM**  
Date: 2026-09-16

## Research question

How should Content Design write labels, instructions and status language so the interface does not assume one visual layout, one color perception, one pointing device or one access technology?

CD001 established semantic fidelity. CD002 established terminology stability. CD003 established command semantics. CD004 established minimum-sufficient information and information order. CD005 addresses another Foundation requirement: **language must survive alternate input and perception modes without pretending that wording alone makes a product accessible.**

The goal is not a list of “accessible words.” The goal is to separate:
- semantic wording responsibilities owned by Content;
- spatial/behavioral responsibilities owned by Layout/Interaction;
- color encoding owned by Color;
- programmatic/browser implementation owned by Web;
- human assistive-technology outcomes that remain unproven without appropriate user evidence.

---

## 1. SOURCE — WCAG 1.3.3: instructions must not rely only on sensory characteristics

W3C’s WCAG 2.2 guidance for Success Criterion 1.3.3 states that instructions for understanding or operating content must not rely solely on sensory characteristics such as shape, color, size, visual location, orientation or sound.

Source:
- W3C WAI — Understanding SC 1.3.3 Sensory Characteristics  
  https://www.w3.org/WAI/WCAG22/Understanding/sensory-characteristics.html

W3C explicitly notes that sensory cues may still be useful when combined with other identifying information. The problem is **exclusive dependence** on the cue.

### Content consequence

Avoid instructions whose only identifier is:
- `the red button`;
- `the control on the right`;
- `the round icon`;
- `the field above`;
- `the sound you hear`.

Prefer naming the control, state or action:
- `Select **Delete record**`;
- `Choose **Payment method**`;
- `Open **Import history**`.

Location/color may remain as supplemental orientation when useful:
- `Select **Next**, at the bottom of the form.`

### STUDIO JUDGMENT

The design target is **identity first, sensory cue second**.

A control’s stable semantic identity is more transferable across responsive layout, reflow, magnification, screen readers, voice control and alternate themes than its current pixel position or color.

---

## 2. SOURCE — Microsoft: procedures should use input-neutral verbs by default

Microsoft’s current Style Guide notes that people interact through keyboard, mouse, touch, voice and other methods and recommends generic verbs rather than input-specific verbs such as `click` or `swipe` in general instructions.

Sources:
- Microsoft Style Guide — Describing interactions with the UI  
  https://learn.microsoft.com/en-us/style-guide/procedures-instructions/describing-interactions-with-ui
- Microsoft Style Guide — Procedures and instructions  
  https://learn.microsoft.com/en-us/style-guide/procedures-instructions/

Microsoft separately documents touch-specific terms when the procedure is genuinely about touch/pen behavior.

Source:
- Microsoft Style Guide — Touch and pen interaction terms  
  https://learn.microsoft.com/en-us/style-guide/a-z-word-list-term-collections/term-collections/touch-pen-interaction-terms

### SYNTHESIS

Input-neutrality is not a ban on words like `tap`, `click`, `press` or `swipe`.

The correct question is:

> **Is the physical input method itself part of the task, or is it merely one way to activate the same semantic command?**

If activation method is incidental:
- prefer `select`, `open`, `choose`, `enter`, `go to` or the control’s name.

If the interaction being taught is specifically touch, keyboard or gesture behavior:
- name that input method explicitly because the modality is itself relevant.

### STUDIO JUDGMENT

The studio therefore rejects the rule “never say click.”

Current rule:

> **Use input-neutral language for input-independent tasks; use modality-specific language only when modality-specific behavior is actually being explained.**

---

## 3. SOURCE — WCAG 1.4.1: color must not be the only way meaning is conveyed

W3C’s Success Criterion 1.4.1 requires that color not be the only visual means of conveying information, indicating an action, prompting a response or distinguishing a visual element.

Source:
- W3C WAI — Understanding SC 1.4.1 Use of Color  
  https://www.w3.org/WAI/WCAG22/Understanding/use-of-color

Examples include failures such as identifying required fields or errors by color alone.

### Content consequence

Wording should name the semantic state:
- `Required` rather than “fields in red are required”;
- `Error: Date must be after 16 September` rather than “fix the red field”;
- `Selected` or an equivalent programmatic/visual state rather than “the blue item”.

### Cross-domain boundary

Content does **not** decide the complete non-color visual encoding. Color/Layout/Web may add icon, border, pattern, shape or programmatic state.

Content responsibility is narrower:
- do not write an instruction whose meaning disappears when color disappears;
- use state language that remains valid across themes and forced-colors.

---

## 4. SOURCE — WCAG 2.5.3: visible label and accessible name should preserve the same control identity

W3C’s Label in Name guidance requires the accessible name of a text-labeled control to contain the visible label. This supports speech-input operation and reduces mismatch for users who hear text-to-speech output while also seeing the screen.

Sources:
- W3C WAI — Understanding SC 2.5.3 Label in Name  
  https://www.w3.org/WAI/WCAG22/Understanding/label-in-name.html
- W3C WAI — G211 Matching the accessible name to the visible label  
  https://www.w3.org/WAI/WCAG22/Techniques/general/G211

### Content consequence

Do not design two competing semantic names for one control.

Problem:
- visible label: `Save`
- hidden accessible name: `Commit current transaction to persistent storage`

Even if the hidden name is more technically descriptive, it changes the control identity and can break predictable voice activation.

Better default:
- visible: `Save draft`
- accessible name: `Save draft`

If additional context is required, use an accessible description or equivalent implementation mechanism rather than silently replacing the visible identity.

### STUDIO JUDGMENT

CD003’s command identity and CD005’s accessibility identity are now joined:

> **One command should have one stable user-facing identity across visible label and programmatic name unless a documented accessibility need requires additional context without changing that identity.**

The exact implementation remains Web/platform ownership.

---

## 5. SOURCE — WCAG 3.3.2: inputs need labels or instructions when users must enter information

W3C’s Labels or Instructions criterion requires labels or instructions where content requires user input. Guidance notes that formatting rules may need explicit instructions when the expected format is not customary or when specific rules are required.

Source:
- W3C WAI — Understanding SC 3.3.2 Labels or Instructions  
  https://www.w3.org/WAI/WCAG21/Understanding/labels-or-instructions

### Content consequence

A field needs a stable semantic label. Placeholder text is not a robust substitute for a visible/programmatically associated label.

Content should distinguish:
- **label** — what information is requested;
- **instruction** — what rule/format/condition applies;
- **example** — optional illustration of valid input;
- **error/recovery text** — what is wrong and how to correct it.

These should not be collapsed into one ephemeral placeholder merely to reduce density.

### STUDIO JUDGMENT

CD004’s minimum-sufficient rule applies here:
- if a format rule is necessary before entry, expose it before or at the field;
- do not wait until error to reveal a rule the user could not reasonably know.

---

## 6. SOURCE — WCAG 4.1.3: status wording and status exposure are separate contracts

W3C’s Status Messages criterion addresses messages about action results, waiting, progress and errors that appear without taking focus. Such messages must be programmatically determinable so assistive technologies can present them.

Source:
- W3C WAI — Understanding SC 4.1.3 Status Messages  
  https://www.w3.org/WAI/WCAG22/Understanding/status-messages

Examples include messages such as result counts, saved status, progress and errors.

### SYNTHESIS

This creates a critical boundary:

1. **Content semantic contract** — what the status message says.
2. **Interaction contract** — when the state changes and whether focus changes.
3. **Web/platform accessibility contract** — how the status is programmatically exposed/announced.

A perfect sentence inside an unannounced status region is not an accessible implementation.

Conversely, a perfectly announced live region with misleading text is not good Content Design.

### STUDIO JUDGMENT

Content must provide a truthful, concise state message. Web/Interaction must ensure the correct delivery mechanism.

Content must not claim “screen-reader accessible” merely because the wording seems suitable for speech.

---

## 7. Icon-only controls — semantic name is mandatory, but visible text remains the stronger default for consequential actions

### PEER EVIDENCE — Web W017

`research/web/W017-icon-signal-chromium-transfer.md` executed a bounded Chromium transfer. It confirmed:
- native controls had non-empty names;
- decorative SVGs were removed from the naming path;
- an icon-only exception had an explicit accessible name;
- consequential warning meaning remained textual;
- visible labels remained present under 200% text enlargement in the specimen.

### SYNTHESIS

An icon has at least three separable layers:
- visual shape;
- semantic control identity;
- accessible/programmatic name.

Content owns the semantic naming; Web/Interaction own correct implementation and behavior.

### STUDIO JUDGMENT

For a consequential or unfamiliar action, visible text should remain the default unless strong product/platform evidence supports an icon-only solution.

If an icon-only control is justified:
- give it a stable semantic name;
- ensure the name matches the same command terminology used elsewhere;
- do not make icon geometry or tooltip hover the only way to discover meaning;
- do not infer human recognition from an accessible-name assertion.

---

## 8. Accessible language is not “screen-reader prose”

### Failure mode

A common mistake is to make hidden text much more verbose than visible content under the assumption that assistive-technology users need a full explanation everywhere.

This can create:
- label/name mismatch;
- duplicated announcements;
- hidden terminology drift;
- excessive interruption;
- two different semantic interfaces for the same action.

### STUDIO JUDGMENT

Design one semantic interface first.

Then decide whether additional **description**, **instruction**, **state announcement** or **structural markup** is required.

Do not make the accessible name carry all surrounding help text.

Content distinguishes:
- **name** — identity of the control/object;
- **description** — supplementary context;
- **instruction** — what to do/how to provide input;
- **status** — what changed;
- **error** — what is wrong and recovery path.

This separation aligns with W3C’s accessible-name/description model but remains a Content information-architecture distinction, not implementation code guidance.

---

## 9. Non-visual reference model

CD005 introduces a provisional rule for referencing interface elements.

### Preferred reference order

1. **semantic label/name** — `Select **Import history**`;
2. **role/object** if needed — `In the **Import history** list...`;
3. **state** if needed — `Choose the record marked **Needs review**`;
4. **sensory/location cue** only as supplemental orientation — `...in the sidebar`.

### Avoid as sole reference

- color;
- left/right/top/bottom;
- shape;
- size;
- icon appearance;
- audio cue;
- gesture/input device when the same task is input-independent.

### Why

Semantic identity is more stable across:
- responsive recomposition;
- text enlargement;
- RTL/localization;
- themes/forced colors;
- keyboard vs pointer vs touch;
- screen-reader/voice interaction.

This is a transferability argument, not proof of user performance.

---

## 10. RELATED DOMAIN CHECK

### Type

Evidence checked:
- current `progress/TYPE_STATUS.md`;
- prior operational-string/fallback evidence.

Reusable finding:
- exact user-facing labels and status strings must survive font/fallback/size changes.

Content consequence:
- do not remove visible labels merely because they wrap under enlargement;
- accessible names should use the same stable terminology as visible content.

Relationship: **REUSE + FUTURE RENDER TRANSFER**.

### Color

Evidence checked:
- current `progress/COLOR_STATUS.md`;
- established semantic-state and forced-colors resilience findings.

Reusable finding:
- authored color may change/disappear while state meaning must remain stable.

Content consequence:
- instructions/statuses must name state rather than color.

Relationship: **DIRECT REUSE**.

### Layout / Interaction

Evidence checked:
- current `progress/LAYOUT_STATUS.md`;
- interaction state/action/recovery evidence reused in CD001–CD003.

Reusable findings:
- action/state/recovery meaning belongs to Interaction;
- responsive/layout position is not a stable semantic identifier;
- focus and mode behavior are separate from wording.

Content consequence:
- avoid location-only instructions;
- do not promise a keyboard/touch/focus behavior through copy unless Interaction implements it.

Relationship: **DEPENDENCY**.

### Web Design

Evidence checked:
- current `progress/WEB_STATUS.md` through W017;
- `research/web/W017-icon-signal-chromium-transfer.md`.

Reusable findings:
- accessible naming, native control semantics, focus-visible behavior, forced-colors resilience and enlargement need actual runtime validation;
- W017 preserved consequential text and visible labels rather than icon/color-only communication.

Content consequence:
- CD005 supplies naming/instruction contracts for future browser transfer;
- Content will not claim AT/browser support from static wording alone.

Relationship: **DIRECT TRANSFER + HANDOFF RECEIVED**.

### Existing Content

- CD001: object/state/action/consequence truth;
- CD002: stable concept/designation;
- CD003: stable command identity;
- CD004: minimum sufficient information/order.

CD005 adds modality independence and name/description/status separation.

---

## 11. Original practice — modality-dependent instructions

This is a controlled semantic/accessibility critique. It does not simulate a screen-reader, voice-control or low-vision user.

### Case A — location and color only

Product facts:
- form contains a button visibly labeled `Review duplicates`;
- desktop layout places it on the right;
- narrow layout moves it below the record list;
- button uses an accent color that can change in forced-colors.

Candidate A:
> Click the blue button on the right.

Critique:
- pointer-specific (`click`);
- color-dependent;
- location-dependent;
- ignores the stable visible label;
- becomes wrong under responsive recomposition.

Verdict: **REJECT**.

Candidate B:
> Select **Review duplicates**.

Critique:
- input-neutral for the task;
- identifies the stable command;
- survives responsive position and color changes;
- does not explain touch/mouse/keyboard mechanics because the task does not require modality-specific teaching.

Verdict: **KEEP AS SEMANTIC CONTROL**.

### Case B — modality-specific behavior is actually the topic

Product facts:
- a drawing tool supports a two-finger touch gesture to rotate the canvas;
- keyboard users have a separate rotate command;
- the help article section is specifically titled `Touch gestures`.

Candidate A:
> Select the canvas to rotate it.

Critique:
- input-neutral wording hides the actual gesture being documented.

Verdict: **REJECT / INSUFFICIENT**.

Candidate B:
> Place two fingers on the canvas and rotate them.

Critique:
- modality-specific because the section is intentionally teaching touch behavior;
- should be paired elsewhere with keyboard/other supported alternatives where product requirements call for them.

Verdict: **KEEP FOR TOUCH-SPECIFIC INSTRUCTION**, not as the only product instruction.

### Case C — visible label / accessible-name drift

Product facts:
- visible button reads `Import 121 records`;
- internal code concept is `commitBatch`;
- designers propose hidden accessible name `Commit batch`.

Critique:
- hidden name exposes internal terminology;
- does not contain the visible command identity;
- risks speech-input mismatch and Content terminology drift.

Verdict: **REJECT**.

Semantic control:
- visible label: `Import 121 records`;
- accessible name: `Import 121 records`;
- any additional explanation belongs in surrounding/description content, not a competing command name.

---

## 12. Reproducible non-human audit — accessibility-language v0.1

For each instruction/control/status string, test known facts against these flags.

### Reference failures

- `SENSORY-ONLY REFERENCE` — control identified only by color/shape/size/location/sound.
- `LOCATION-LOCK` — wording becomes false after responsive/reflow layout changes.
- `COLOR-LOCK` — semantic identity depends on authored color.
- `ICON-ONLY SEMANTICS` — meaning exists only in icon appearance with no stable semantic name.

### Input failures

- `INPUT-METHOD LOCK` — `click/tap/swipe/press` used although the task is input-independent.
- `FALSE INPUT NEUTRALITY` — generic wording used even though the instruction is specifically about a modality/gesture.

### Naming failures

- `LABEL-NAME DRIFT` — visible label and accessible/programmatic name describe different commands.
- `INTERNAL NAME LEAK` — hidden name exposes implementation/organizational terminology.
- `NAME-DESCRIPTION COLLAPSE` — help/instruction/status text is packed into the control name rather than separated by role.

### Form/status failures

- `MISSING INPUT LABEL` — user cannot identify what the field requests.
- `LATE REQUIRED RULE` — required format/condition appears only after avoidable error.
- `STATUS DELIVERY DEPENDENCY` — wording exists, but programmatic announcement/delivery must be validated by Web/Interaction.
- `COLOR-ONLY ERROR` — wording tells user to fix the colored field rather than naming field/error.

### Validation flags

- `BROWSER TRANSFER NEEDED`;
- `AT USER EVIDENCE NEEDED`;
- `VOICE CONTROL TEST NEEDED`;
- `KEYBOARD/TOUCH BEHAVIOR DEPENDENCY`;
- `FORCED-COLORS TRANSFER NEEDED`;
- `ZOOM/REFLOW TRANSFER NEEDED`;
- `LOCALIZATION/RTL REVIEW NEEDED`.

### What this audit can establish

It can reject wording that is demonstrably tied to unstable sensory/input assumptions or conflicts with known labels/state contracts.

### What it cannot establish

It cannot prove:
- screen-reader announcement quality;
- speech-recognition success rate;
- keyboard/touch operability;
- low-vision findability;
- cognitive accessibility outcomes;
- assistive-technology preference;
- task performance by disabled users.

Those require implementation/runtime and/or human evidence.

---

## 13. Foundation principles after CD005

The Content Foundation now provisionally adopts these additional rules:

1. **Identify controls by semantic name before sensory appearance or location.**
2. **Use input-neutral verbs for input-independent tasks.**
3. **Use modality-specific language when modality-specific behavior is genuinely the subject.**
4. **Do not use color as the sole linguistic identifier of state/action.**
5. **Keep visible label and accessible name semantically aligned.**
6. **Separate control name, description, instruction, status and error roles.**
7. **Do not use hidden accessibility text to create a second vocabulary system.**
8. **Accessible wording is necessary but not sufficient; behavior and programmatic exposure require peer-domain/runtime validation.**
9. **Responsive reflow can invalidate location-based instructions even without any accessibility technology.**
10. **Human AT outcomes remain a distinct evidence gate.**

---

## 14. HANDOFFS TO OTHER SPECIALISTS

### Web Design

CD005 supplies a bounded set of language/runtime contracts for later browser validation:
- visible label contained in accessible name;
- semantic control names independent of SVG/icon title;
- status messages requiring programmatic delivery;
- input labels/instructions separated from placeholders;
- no color/location-only instruction dependencies.

W017 already confirms part of this contract in Chromium; CD005 does not upgrade that to AT user evidence.

### Layout / Interaction

Location-based wording should be treated as fragile under responsive recomposition. Interaction should expose actual input/state behavior; Content will choose input-neutral or modality-specific language based on that contract.

### Color

Content explicitly removes color from sole semantic ownership. Color may reinforce state, but status/error/required meaning needs a non-color semantic path.

### Type

Visible labels should survive enlargement rather than be silently replaced by icon-only controls. Exact wording from CD003–CD005 should be retained in later Type stress tests.

---

## 15. OPEN questions after CD005

1. How should Content specify accessible descriptions without creating verbose/duplicative AT output?
2. Which UI concepts are genuinely conventional enough to support icon-only presentation for expert users, and what evidence is needed?
3. How should Korean input-neutral verbs be standardized across mobile/web without awkward literal translation from English?
4. How should instructions adapt across RTL or spatially reorganized interfaces when location is still useful as a supplemental cue?
5. What is the appropriate human-validation protocol for speech input, screen readers, magnification and switch/keyboard use during real app development?
6. How should status-message urgency/tone coordinate with live-region delivery without making interfaces excessively interruptive?

These remain Foundation/Stage 2+ questions.

## Current conclusion

`SOURCE`: W3C requires that instructions not rely solely on sensory characteristics, color not carry the only meaning, visible control labels remain represented in accessible names, inputs receive labels/instructions, and applicable status messages be programmatically exposed. Microsoft provides a strong platform precedent for input-neutral procedural language.

`SYNTHESIS`: stable semantic identity is more transferable than color, screen position, icon geometry or pointing-device verbs.

`STUDIO JUDGMENT`: Content should design one semantic interface whose control identities, instructions and status terms survive alternate presentation/input modes; additional accessibility descriptions should supplement rather than silently replace that identity.

`OPEN`: actual AT behavior and disabled-user task outcomes remain unproven and will not be simulated.

Stage 1 remains **IN STUDY / PRACTICE — NOT PASSED**.