# Roster Systems Research Log

## 2026-10-04 — baseline

- Opened the broader LogMate roster-system intelligence and parser-corpus research program.
- Reused the existing CrewConnex market baseline rather than duplicating it.
- Seeded system queue: CrewConnex, AIMS eCREW, NAVBLUE/RAIDO, NetLine, CAE Crew Access, FLICA, IBS iFlight, Jeppesen, Sabre, LEON and later systems.
- Seeded parser-corpus leads for NetLine PDF, AIMS CSV/HTM, NAVBLUE ICS/PDF and FLICA ICS.
- Next highest-value target: verify and acquire the public scrambled NetLine/Crewlink PDF sample, then extract its field structure.


## 2026-10-04 23:00 KST — NAVBLUE N-Ops & Crew / N-Crew Planning

- Official NAVBLUE documentation verifies two calendar delivery modes in N-OC: subscription link and direct download, with roster changes synchronized to the external calendar.
- Official N-Crew Planning documentation explicitly identifies Download Schedule output as ICS.
- Official N-OC My Roster documentation verifies Print generates a PDF activity report.
- Documented roster semantics include calendar-month activities, check-in time/station, first activity code/start time, check-in/out, flight or station information, optional crew-on-board and notes.
- Two focused searches found no lawful public raw NAVBLUE ICS/PDF artifact. P1 remains open; do not repeat the same raw-sample query next cycle.
- Parser impact: ICS and PDF are now independently P2-verified export paths; exact ICS properties/PDF text layer remain blocked on P1.
- Next target: FLICA public ICS sample or stronger official export evidence.


## 2026-10-05 00:00 KST — CAE FLICA

- Frontier and JetBlue setup documentation independently confirms the same FLICA user export path: Schedule -> Export -> V2 Calendar (.ics), saved locally and repeated for each published monthly schedule.
- Current Flight Crew View support confirms a user-controlled ICS workflow: authenticate to FLICA in the device browser, export the ICS, then import it into the app. This supports a file-import architecture without authenticated scraping.
- Flight Crew View schedule documentation states BLK is block time downloaded with the schedule; exact ICS property mapping remains unknown.
- Two focused searches found no lawful public raw FLICA V2 Calendar ICS artifact. P1 remains open; do not infer VEVENT properties.
- Parser impact: FLICA remains P3, but V2 Calendar ICS is corroborated across two airlines plus a current downstream importer.
- Next target: CAE Crew Access export formats/public samples.
