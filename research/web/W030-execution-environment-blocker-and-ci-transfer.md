# W030 — Browser execution environment blocker and CI transfer

Date: 2026-09-16
Evidence class: **EXECUTION ATTEMPT / BLOCKER / TRANSFER PLAN**

## RELATED DOMAIN CHECK
Type T021 remains independent. C029 and L020 require executed browser geometry/visual-state evidence. I016/W028 already supply controlled backend truth. CD035 supplies certainty-bound wording. W029 is the browser runner.

## Execution attempt
The current execution environment attempted to obtain the canonical repository and run `research/web/W029-browser-capture-runner.py` locally. The repository transfer failed before runner launch because the container could not resolve `github.com` (`Could not resolve host: github.com`).

This is an environment/network blocker, not a W029 functional failure. No browser result JSON, PASS, cross-browser claim or visual evidence is created from this attempt.

## Why another protocol-only study is not enough
W029 already defines the executable browser matrix. Repeating static Chromium assumptions would add no evidence. The next valid transfer needs an environment that has both the repository contents and Playwright browser engines.

## CI/local execution contract
A suitable GitHub Actions or developer workstation run should:
1. checkout canonical `main`;
2. install Python Playwright and Chromium/Firefox/WebKit engines;
3. execute `python research/web/W029-browser-capture-runner.py`;
4. fail the job if zero browser runs execute;
5. preserve `W029-browser-capture-results.json` as an artifact;
6. review the result before committing it as canonical evidence;
7. run separate actual-200%-zoom and forced-colors captures rather than relabeling 320 CSS px as zoom.

CI availability itself does not constitute browser evidence. Only the produced result artifact and environment metadata do.

## Cross-domain evidence mapping after execution
- **I016/CD035:** `drop-before` and `drop-after` must initially remain outcome-unknown and reconcile differently.
- **L020:** consume viewport, scroll width and focus/sticky rectangles; add actual 200% zoom separately.
- **C029:** consume focus visibility/occlusion and add forced-colors/high-contrast separately.
- **Web:** record browser engine/version, route/history and network/recovery result.
- **UX integration:** verify end-to-end state/recovery coherence without claiming human comprehension or workload.

## Evidence boundary
No Web/Color/Layout browser PASS is claimed. No AT, physical-device, Safari, field LCP/INP/CLS or human evidence is implied.