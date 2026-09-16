# CD049 — Temporal Provenance, Timezone and Localization System

Status: **STAGE 3 PRACTICE / LOCALIZATION CONTRACT READY — TOOLCHAIN OPEN**

## RELATED DOMAIN CHECK
I030 defines which time is authoritative and how ordering works. L034 owns role/value locality and chronology layout. C043 reinforces but cannot create temporal meaning. W043 owns actual browser/export/recheck transfer. Type T021 must eventually prove dense timestamp strings after drawing repair.

Purpose: **TRANSFER VALIDATION** of CD046–CD048 into multi-clock, multi-locale audit language.

## Current-source check
Unicode CLDR defines locale-sensitive date/time patterns, including differing field order, 12/24-hour conventions, timezone forms and user preference considerations: https://cldr.unicode.org/translation/date-time/date-time-patterns

WHATWG HTML supports machine-readable date/time values independently of displayed text: https://html.spec.whatwg.org/multipage/text-level-semantics.html#the-time-element

These sources support formatting architecture. They do not determine which product timestamp means “current”.

## Semantic resource model
Do not expose one generic `timestamp` label. Maintain distinct semantic IDs such as:

- `eventOccurredAt`;
- `observedAt`;
- `authorityConfirmedAt`;
- `reconciledAt`;
- `snapshotGeneratedAt`;
- `liveRecheckedAt`;
- `timeSourceUnavailable`;
- `eventTimeUnknown`;
- `timezoneChangedPresentationOnly` when explanation is actually needed.

## Localization rules

1. Store/transport typed instants and semantic roles; locale text is a realization, not product logic.
2. Allow CLDR-driven field order and 12/24-hour conventions.
3. When professional/audit interpretation depends on zone, include a zone/offset representation sufficient for that context rather than assuming device-local time is obvious.
4. Relative time may supplement but not replace durable absolute/provenance time in audit/export/recheck surfaces.
5. Translation must not turn “observed at” into “occurred at”, “generated at” into “confirmed at”, or “unknown” into “failed”.
6. Snapshot and live recheck times remain separate even if they format to the same minute.

## Round-trip cases for production tooling

- en-US 12-hour and 24-hour preference;
- ko-KR;
- one locale with materially different date order/long month expansion;
- explicit UTC offset/zone;
- DST/offset change across snapshot and recheck;
- pseudo-expansion;
- missing resource/fallback;
- locale switch with identical underlying instant/revision;
- long object IDs beside timestamp roles.

Record resource revision, locale, timezone, raw instant, semantic ID, formatted result and fallback path.

## Content failures

- one “Updated” label reused for generated/confirmed/reconciled/rechecked times;
- ambiguous numeric date used where locale/zone ambiguity changes professional interpretation;
- translator forced to infer whether a time is event or observation time;
- relative-only wording in durable history/export;
- timezone text omitted solely to preserve preferred geometry;
- locale switch treated as evidence that data changed.

## Evidence boundary
No Flutter `gen-l10n`, TMS, ARB or equivalent production round trip has been executed for CD049. No linguistic-review or human-comprehension PASS is claimed.

## HANDOFFS TO OTHER SPECIALISTS
W043 binds resource revision/locale/zone to runtime evidence. L034 must permit expanded role labels and zones. C043 must preserve meaning without color. Type receives unchanged strings for post-repair stress. I030 remains authority for ordering/action truth.
