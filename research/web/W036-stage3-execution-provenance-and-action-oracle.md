# W036 — Stage-3 execution provenance + action oracle

Date: 2026-09-16
Evidence: **TRANSFER VALIDATION PROTOCOL / EXECUTION OPEN**

## RELATED DOMAIN CHECK
I023 defines action/fact dependencies; L027 defines locality/reflow geometry; C036 defines visual composition degradation; CD041/CD042 owns semantic resources; Type candidate transfer remains provisional pending T021 drawing critique.

## Purpose
W035 records partial authority but still risks producing a browser artifact that says what the page rendered without proving whether each rendered action was justified. W036 adds the Interaction oracle to the same browser evidence record.

## Per-run record
For each engine/scenario/run ID preserve:
- repository commit SHA and fixture revision;
- engine/version/platform and headless/headed mode;
- route, navigation/lifecycle event and viewport/visual viewport;
- raw authority request/response/timeout/conflict trace;
- presented and authoritative revisions;
- known/unknown/expired/conflicting facts;
- `actionId`, required facts, dependency verdict, rendered enabled/disabled state and recovery action;
- semantic resource ID/revision/locale;
- focus and authored-overlay rectangles;
- forced-colors state and computed/rendered state evidence;
- overflow/reflow result.

A mismatch between dependency verdict and rendered action state is a Web/Interaction integration failure even when the page otherwise looks correct.

## Stage-3 closure relevance
This shared record lets one product-like execution support independent verdicts from Interaction, Layout, Color, Content and Web without collapsing them. Chromium-only success is not cross-browser evidence. WebKit is not Safari evidence. Actual 200% browser zoom is not replaced by a 320 CSS px viewport.

## Performance boundary
Functional request timings from this fixture are lab diagnostics. LCP/INP/CLS are field evidence only when sourced from an actual field/RUM population with documented context; no field claim is generated here.

## Current blocker
No browser-capable W036 run has been executed in this environment. The repository already demonstrates that GitHub Actions can produce reproducible Type artifacts, so CI is a credible execution venue, but this Web specialist does not modify coordinator/noncanonical workflow infrastructure in this study. A future authorized CI/local runner should execute W036 and preserve raw artifacts.

## Evidence boundary
No Web Stage-3 PASS, cross-browser, Safari, AT, physical-device, field Core Web Vitals or human UX PASS is claimed.
