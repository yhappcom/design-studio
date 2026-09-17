# W061 — GitHub Actions Flutter Runtime Execution Bridge

Evidence purpose: **TRANSFER VALIDATION / EXECUTION ENABLEMENT**

## Question
W059/W060 have enough acceptance theory. The dominant blocker is execution. Can the existing GitHub environment be converted from a documentation-only boundary into a reproducible Flutter runtime evidence path without pretending that CI equals human or physical-device evidence?

## RELATED DOMAIN CHECK
- **Type:** T029 requires exact runtime identity and a compact-iOS clamp versus unclamped diagnostic comparison while T021 drawing remains open; mature fallback must be used.
- **Color:** C060 requires locale-dependent polarity, contradiction states and rendered contrast/redundancy evidence.
- **Layout/Interaction:** L051/I047 require whole-workflow reflow, focus, target and recovery evidence rather than isolated screenshots.
- **Content:** CD066 requires MintTap's actual Dart localization pipeline, not an assumed ARB-only architecture.
- **Web:** W059/W060 already define artifact identity and explicitly prohibit further adjacent micro-theory while execution is blocked.

## Repository inspection
`yhappcom/design-studio` already has GitHub Actions proof workflows for Type. Therefore GitHub-hosted execution is an established studio mechanism rather than a new governance structure. The MintTap `design-lab/minttap-1.0.29` branch is Flutter 1.0.29+29 with Dart constraint `^3.10.7`, and the branch currently has no `.github` workflow directory. The design-lab branch head inspected for this study is `006d71ec525597aae6b0cbda32cfdaa85c83be0c`.

## Decision
The next executable Web block should be a **CI execution bridge**, not W062 theory.

A repository-local workflow in the MintTap design-lab branch is the preferred first implementation because it can check out the exact product commit without cross-repository credential assumptions. Design Studio remains the canonical owner of the acceptance contract; MintTap owns the executable product harness.

Minimum CI phases:
1. pin Flutter/Dart-compatible toolchain and exact product commit;
2. `flutter pub get`, `flutter analyze`, relevant deterministic tests;
3. build/run the isolated `lib/main_design_lab.dart` / whole-app lab on Flutter Web;
4. serve the built app locally;
5. exercise deterministic scenarios with a browser automation harness;
6. capture viewport, locale/currency, text-scaling diagnostic mode, screenshot, browser console/logs and accessibility/semantics evidence available to the chosen harness;
7. upload a manifest and raw artifacts with commit/build/scenario/browser identity;
8. only after the isolated lab is stable, add production smoke paths.

## Required scenario matrix
At minimum preserve the W059/W060 acceptance vectors:
- phone narrow + tablet/wide;
- baseline text and enlarged-text diagnostic;
- current compact-iOS cap behavior recorded separately from an **unclamped diagnostic** path; the diagnostic must not silently change production policy;
- ko/ja and a non-ko/ja locale;
- KRW and USD;
- positive/negative/zero;
- high distribution + negative total performance;
- estimated/final ROC;
- partial/unavailable/zero;
- pending/failure/ambiguous recovery;
- long portfolio/label content.

## Evidence classification
CI can provide reproducible **LAB / TRANSFER VALIDATION** evidence for build, browser rendering, deterministic focus/task paths and static/runtime accessibility checks. It does **not** establish:
- representative-human usability;
- TalkBack/VoiceOver comprehension;
- physical iOS/Android rendering;
- calibrated-display/observer evidence;
- Safari/WebKit breadth unless that engine is actually executed;
- field LCP/INP/CLS. Lighthouse or trace data remains LAB; only provenance-bearing RUM/CrUX/equivalent is field evidence.

## Failure policy
A CI failure is classified and routed, not cosmetically repaired:
- glyph/raster/metric issue → Type;
- color axis/contrast/redundancy issue → Color;
- clipping/reflow/adjacency/target issue → Layout;
- focus/state/retry/recovery issue → Interaction;
- semantic/localization drift → Content;
- browser/runtime/route/network/artifact-identity issue → Web.

No domain may shorten truth-bearing content, misuse color, or introduce kerning to conceal another domain's failure.

## Blocker change
The previous statement “Flutter/browser execution is unavailable” is now too broad. **Direct execution in the current chat runtime remains unavailable, but GitHub Actions is an available execution substrate already used by Design Studio.** What remains missing is the MintTap-specific CI workflow/harness and its first successful artifact-bearing run.

## Next executable block
Implement the MintTap design-lab CI workflow/harness, run it, inspect artifacts, then perform one cross-domain critique on the same manifest identity. Do not add another Web acceptance-theory study before that run unless execution reveals a genuinely new unknown.

## HANDOFFS TO OTHER SPECIALISTS
Type/Color/Layout/Interaction/Content should bind their next runtime claims to the first W061 CI manifest rather than creating separate scenario identities. Human and physical-device evidence remain OPEN.