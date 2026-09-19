# Candidate 04 — Content Design Review R1

Status: CHANGES REQUIRED

Evidence: Candidate 04 Flutter implementation ca5f95ba32d499db4b41a8800400aaef20f5341f, 390x844 deterministic render, MASTER and ui-contract.

No prior candidate consulted.

Blockers:
1. Home Current Period values are confirmed Block Time, but the render shows only date + This month/This year values. The metric identity is not visible and the numbers are therefore ambiguous.
2. Canonical Home section/action literals in the current contract are Recent, Add flight and View logbook. The draft uses Recent Flights / Add Flight / View Logbook.

Required:
- expose Block Time in the Current Period band;
- use canonical current literals: Recent, Add flight, View logbook;
- retain numeric locale-aware month/year fixture.

No invented greeting/slogan/state claims are present.

Verdict: NOT OWNER-REVIEW ELIGIBLE YET.