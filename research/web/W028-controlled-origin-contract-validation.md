# W028 — Controlled-origin contract validation

Date: 2026-09-16
Evidence class: **TRANSFER VALIDATION / executable backend contract**

## RELATED DOMAIN CHECK
- **Type:** T021 remains independent and blocked on operational repertoire/drawing/general spacing; this runtime harness must use mature fonts and cannot advance Type gates.
- **Color:** C029 can consume the served surface for focus/state/forced-colors captures, but no browser visual evidence is claimed here.
- **Layout/Interaction:** I015 is the authority for recovery classification; L020 still requires browser geometry evidence. This study validates the backend distinction needed by I015.
- **Web:** extends W027 from a frontend-only Fetch specimen to a controlled same-origin backend contract.
- **Content:** CD034 recovery wording can now be bound to distinguish known failure from transport ambiguity and post-commit response loss.

## Executed contract check
A local copy of `W028-controlled-origin-backend.py` was syntax/execution checked with Python's standard-library HTTP client against `127.0.0.1:8028`. Four controlled POST modes were exercised and then reconciled by operation ID.

| mode | immediate transport/result | reconciliation | semantic classification |
| --- | --- | --- | --- |
| `confirm` | HTTP 200, confirmed | confirmed record | confirmed |
| `reject` | HTTP 422, known-failure | not-found | known failure / no commit in this fixture |
| `drop-before` | transport exception (`RemoteDisconnected`) | not-found | transport ambiguity resolved to no recorded commit |
| `drop-after` | transport exception (`RemoteDisconnected`) | confirmed record | transport ambiguity resolved to committed |

This validates the core I015 distinction: the same client-visible transport exception can correspond to materially different authoritative outcomes. A retry policy based only on the exception would therefore be unsafe for the `drop-after` case.

## W027 binding correction
W027 was updated to expose all four controlled modes, preserve the last operation ID, and reconcile `/w027/status?id=<operationId>`. HTTP non-success with a JSON body is rendered as **Known failure**; transport exceptions remain **Outcome unknown** until reconciliation.

## Evidence boundary
This is **not** browser execution evidence. No DOM/focus/zoom/forced-colors/history/cross-browser/AT/physical-device or human UX PASS is claimed. The environment available for this run could execute the backend contract but could not retrieve/launch the repository through an installed browser runtime. Therefore W026/C029/L020 browser capture evidence remains OPEN.

## HANDOFFS TO OTHER SPECIALISTS
- **Interaction:** use `drop-before` and `drop-after` as the minimum adversarial pair for I015; both initially look like transport failure but reconcile differently.
- **Content:** do not map a transport exception directly to “failed.” Keep outcome-unknown wording until reconciliation.
- **Color/Layout:** use the updated W027 controls to capture focus/overlay/reflow states once a browser runtime is executable.
- **Web:** next closure block should automate W027+W028 in Chromium first, then transfer the identical capture schema to Firefox/WebKit/Safari where executable.
