// C457 research-only oracle. Run: node case-studies/logmate/market-research/roster-systems/crewconnex/C457_PRIVACY_SAFE_ASSOCIATION_ORACLE.mjs
// Uses only public Design Studio nonidentifying metadata and synthetic policy scenarios.
// It does NOT parse private PDFs, test Dart/Sembast, approve W-016, or certify FlightRecord links.
import assert from "node:assert/strict";
import { readFileSync } from "node:fs";
import { createHash } from "node:crypto";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const base = dirname(fileURLToPath(import.meta.url));
const read = name => readFileSync(join(base, name));
const fixture = JSON.parse(read("C457_PRIVACY_SAFE_ASSOCIATION_ACCEPTANCE_FIXTURE.json").toString("utf8"));
const manifestBytes = read("C194_THREE_MONTH_FIELD_LOCATOR_MANIFEST.csv");
const pdcBytes = read("C282_INTEGRATED_DATE_PAIRING_SOURCE_FAMILY_GATE.json");
const gitBlob = bytes => createHash("sha1")
  .update(Buffer.from("blob " + bytes.length + "\0"))
  .update(bytes).digest("hex");

assert.equal(gitBlob(manifestBytes), fixture.sourcePins.manifestGitBlob, "pinned C194 blob");
assert.equal(gitBlob(pdcBytes), fixture.sourcePins.pdcAggregateGitBlob, "pinned C282 blob");
assert.equal(fixture.status, "RESEARCH_ONLY_NOT_PRODUCT_APPROVAL");

const [header, ...lines] = manifestBytes.toString("utf8").trim().split(/\r?\n/);
const keys = header.split(",");
const source = lines.map(line => {
  const cells = line.split(",");
  assert.equal(cells.length, keys.length, "manifest column count");
  return Object.fromEntries(keys.map((k, i) => [k, cells[i]]));
});
const project = x => ({
  month: x.month,
  page: Number(x.page_1based),
  tr: Number(x.primary_tr_1based_including_header),
  ownDate: x.date_cell_state,
  pairing: x.pairing_cell_state,
  crewShape: x.crew_leaf_shape,
  physicalAnchorTr: x.physical_multileaf_anchor_tr_1based
    ? Number(x.physical_multileaf_anchor_tr_1based) : null,
  previewSelected: Boolean(x.preview_sheet4_row_1based)
});
const rows = source.map(project);
assert.deepEqual(rows, fixture.realSourceDerived.rows, "all 62 pinned projections");
const count = fn => rows.filter(fn).length;
assert.equal(rows.length, 62);
assert.deepEqual(["06", "07", "08"].map(m => count(x => x.month === m)), [18, 22, 22]);
assert.equal(count(x => x.previewSelected), 43);
assert.equal(count(x => x.ownDate === "PRESENT"), 35);
assert.equal(count(x => x.pairing === "PRESENT"), 30);
assert.equal(count(x => x.ownDate === "PRESENT" && x.pairing === "ABSENT"), 5);
assert.equal(count(x => x.crewShape === "SINGLELEAF_1"), 26);
assert.equal(count(x => x.crewShape === "MULTILEAF_6"), 31);
assert.equal(count(x => x.crewShape === "MULTILEAF_7"), 5);
assert.equal(count(x => x.page === 2), 6);
assert.equal(new Set(rows.map(x => [x.month, x.page, x.tr].join("|"))).size, 62);
assert(rows.some(x => x.month === "08" && x.page === 1 && x.tr === 14 &&
  x.ownDate === "ABSENT" && x.crewShape === "MULTILEAF_6"));
const groups = new Map();
for (const x of rows) {
  const anchor = x.crewShape === "SINGLELEAF_1" ? x.physicalAnchorTr : x.tr;
  assert(anchor !== null, "pipe has anchor");
  const key = [x.month, x.page, anchor].join("|");
  groups.set(key, [...(groups.get(key) ?? []), x]);
}
const size = n => [...groups.values()].filter(v => v.length === n).length;
assert.deepEqual([size(1), size(2), size(4)], [14, 20, 2]);
assert.equal(groups.size, 36);
const pdc = JSON.parse(pdcBytes.toString("utf8"));
assert.deepEqual(pdc.pdc.numericDatePairTextPresence,
  fixture.realSourceDerived.pdc.numericDatePairPresence);
assert.equal(Object.values(pdc.pdc.numericDatePairTextPresence)
  .reduce((a, b) => a + b, 0), 26);
assert.equal(pdc.pdc.nonnumericWithFourClocks, 22);
assert.equal(pdc.pdc.auxiliaryActivityTextAbsentButOtherCellPresent, 1);
const allowed = ["crewShape", "month", "ownDate", "page", "pairing",
  "physicalAnchorTr", "previewSelected", "tr"].sort();
for (const row of rows) assert.deepEqual(Object.keys(row).sort(), allowed);


// C459: independent, privacy-safe three-month physical-table geometry admission.
// This is an OBSERVED layout discriminator, not a month-driven production detector.
// Future production must select a validated header/profile before applying offsets.
function geometryErrors(items) {
  const errors = [];
  const requireShape = (ok, reason) => { if (!ok) errors.push(reason); };
  const rowIndex = new Map(), sourceBases = new Map();
  const scopedMcids = new Set();
  const offsets = { activity: 6, from: 9, to: 13, blh: 19,
    acreg: 21, emp: 24, cc: 25, pos: 27 };
  for (const r of items) {
    const rowKey = [r.source_git_blob_sha1, r.page_1based,
      r.primary_tr_1based_including_header].join("/");
    requireShape(!rowIndex.has(rowKey), "duplicate physical row");
    rowIndex.set(rowKey, r);
    const d = r.date_cell_state === "PRESENT" ? 1 : 0;
    const p = r.pairing_cell_state === "PRESENT" ? 1 : 0;
    const shift = d + p;
    const base = Number(r.body_td_count) - shift;
    requireShape([28, 29, 32].includes(base), "unsupported body width");
    const prior = sourceBases.get(r.source_git_blob_sha1);
    requireShape(prior === undefined || prior === base,
      "inconsistent source-wide layout");
    sourceBases.set(r.source_git_blob_sha1, base);
    for (const [field, position] of Object.entries(offsets)) {
      requireShape(Number(r[field + "_td_1based"]) - shift === position,
        "column offset " + field);
      if (["activity", "from", "to", "blh", "acreg"].includes(field)) {
        const mcid = r[field + "_mcid_page_local"];
        requireShape(Boolean(mcid), "missing mandatory MCID");
        const loc = [r.source_git_blob_sha1, r.page_1based, mcid].join("/");
        requireShape(!scopedMcids.has(loc), "reused source-scoped MCID");
        scopedMcids.add(loc);
      }
    }
    const leafCount = r.crew_leaf_shape === "SINGLELEAF_1"
      ? 1 : Number(r.crew_leaf_shape.split("_")[1]);
    for (const field of ["emp", "cc", "pos"]) {
      requireShape(r[field + "_leaf_mcids_page_local"].split("|").length
        === leafCount, "crew triplet cardinality " + field);
    }
    if (r.crew_leaf_shape === "SINGLELEAF_1") {
      requireShape(d === 0 && p === 0, "pipe row own Date/Pairing");
      requireShape(Number(r.singleleaf_chain_depth) >= 1,
        "pipe depth");
    } else {
      requireShape(Number(r.singleleaf_chain_depth) === 0,
        "direct depth");
    }
  }
  for (const r of items) {
    if (r.crew_leaf_shape !== "SINGLELEAF_1") continue;
    const anchor = rowIndex.get([r.source_git_blob_sha1, r.page_1based,
      r.physical_multileaf_anchor_tr_1based].join("/"));
    requireShape(Boolean(anchor), "missing same-source/page anchor");
    if (!anchor) continue;
    requireShape(anchor.crew_leaf_shape.startsWith("MULTILEAF_"),
      "non-direct anchor");
    requireShape(r.physical_anchor_date_state === anchor.date_cell_state,
      "anchor Date state mismatch");
    requireShape(r.physical_anchor_pairing_state === anchor.pairing_cell_state,
      "anchor Pairing state mismatch");
    requireShape(Number(r.primary_tr_1based_including_header) -
      Number(r.physical_multileaf_anchor_tr_1based) ===
      Number(r.singleleaf_chain_depth), "noncontiguous physical depth");
    requireShape(Boolean(r.preview_sheet4_row_1based) ===
      Boolean(anchor.preview_sheet4_row_1based), "preview selection split");
  }
  return errors;
}
assert.deepEqual(geometryErrors(source), [], "C459 pinned geometry");
const mutateGeometry = (label, change) => {
  const copy = source.map(r => ({ ...r }));
  change(copy);
  assert(geometryErrors(copy).length > 0, "C459 mutation admitted: " + label);
};
const firstPipe = a => a.find(r => r.crew_leaf_shape === "SINGLELEAF_1");
mutateGeometry("body width", a => { a[0].body_td_count = "35"; });
mutateGeometry("missing Date with unchanged columns",
  a => { a[0].date_cell_state = "ABSENT"; });
mutateGeometry("missing Pairing with unchanged columns",
  a => { a[0].pairing_cell_state = "ABSENT"; });
mutateGeometry("From offset",
  a => { a[0].from_td_1based = "12"; });
mutateGeometry("Pos offset",
  a => { a[0].pos_td_1based = "30"; });
mutateGeometry("crew cardinality",
  a => { a[0].cc_leaf_mcids_page_local = "131|132"; });
mutateGeometry("MCID collision",
  a => { a[0].from_mcid_page_local = a[0].activity_mcid_page_local; });
mutateGeometry("source swap",
  a => { a[0].source_git_blob_sha1 = "f".repeat(40); });
mutateGeometry("cross-page continuation",
  a => { firstPipe(a).page_1based = "2"; });
mutateGeometry("chain depth",
  a => { firstPipe(a).singleleaf_chain_depth = "3"; });
mutateGeometry("missing anchor",
  a => { firstPipe(a).physical_multileaf_anchor_tr_1based = "999"; });
mutateGeometry("direct-to-pipe misclassification",
  a => { a[0].crew_leaf_shape = "SINGLELEAF_1"; });


// C460 pinned all-field MCID regression: source-derived integrity ONLY.
// These observed page-local patterns are NOT a production ParserProfile detector,
// PDF version signature, crew identity, flight date, or semantic field mapping.
const c460PinnedSourceIds = new Set(source.map(r => r.source_git_blob_sha1));
const c460PinnedBases = new Map(source.map(r => [
  r.source_git_blob_sha1,
  Number(r.body_td_count) -
    Number(r.date_cell_state === "PRESENT") -
    Number(r.pairing_cell_state === "PRESENT")
]));
function c460PinnedMcidErrors(items) {
  const errors = [];
  const seen = new Set();
  const pageRows = new Map();
  const mcidFields = [
    "date", "pairing", "activity", "from", "to", "blh", "acreg",
    "emp", "cc", "pos"
  ];
  for (const r of items) {
    if (!c460PinnedSourceIds.has(r.source_git_blob_sha1))
      errors.push("unrecognized pinned source");
    const shift = Number(r.date_cell_state === "PRESENT") +
      Number(r.pairing_cell_state === "PRESENT");
    if (Number(r.body_td_count) - shift !==
        c460PinnedBases.get(r.source_git_blob_sha1))
      errors.push("pinned source base mismatch");
    const mcids = mcidFields.flatMap(field =>
      (r[field + "_mcid_page_local"] ||
        r[field + "_leaf_mcids_page_local"] || "")
        .split("|").filter(Boolean).map(Number));
    if (!mcids.length) errors.push("missing MCIDs");
    for (const mcid of mcids) {
      if (!Number.isSafeInteger(mcid) || mcid < 0)
        errors.push("invalid MCID");
      const scoped = [r.source_git_blob_sha1, r.page_1based, mcid].join("/");
      if (seen.has(scoped)) errors.push("duplicate MCID including optional/crew");
      seen.add(scoped);
    }
    if (mcids.some((mcid, i) => i > 0 && mcid <= mcids[i - 1]))
      errors.push("MCIDs out of row order");
    const core = ["activity", "from", "to", "blh", "acreg"];
    const gaps = core.slice(1).map((field, i) =>
      Number(r[field + "_mcid_page_local"]) -
      Number(r[core[i] + "_mcid_page_local"]));
    if (gaps.join("/") !== "3/4/6/2")
      errors.push("C194-only core MCID gap drift");
    const pageKey = [r.source_git_blob_sha1, r.page_1based].join("/");
    if (!pageRows.has(pageKey)) pageRows.set(pageKey, []);
    pageRows.get(pageKey).push({
      tr: Number(r.primary_tr_1based_including_header),
      min: Math.min(...mcids),
      max: Math.max(...mcids)
    });
  }
  for (const rowsOnPage of pageRows.values()) {
    rowsOnPage.sort((a, b) => a.tr - b.tr);
    for (let i = 1; i < rowsOnPage.length; i++)
      if (rowsOnPage[i].min <= rowsOnPage[i - 1].max)
        errors.push("MCID page stream out of physical-row order");
  }
  return errors;
}
assert.deepEqual(c460PinnedMcidErrors(source), [], "C460 pinned MCID integrity");
const c460Bypasses = [
  ["crew MCID overlaps Emp", a => {
    const r = a[0];
    r.cc_leaf_mcids_page_local = r.cc_leaf_mcids_page_local.replace(
      /^\d+/, r.emp_leaf_mcids_page_local.split("|")[0]);
  }],
  ["Date MCID overlaps Activity", a => {
    a[0].date_leaf_mcids_page_local = a[0].activity_mcid_page_local;
  }],
  ["From MCID inversion", a => {
    a[0].from_mcid_page_local = "999999";
  }],
  ["From MCID gap drift", a => {
    a[0].from_mcid_page_local =
      String(Number(a[0].from_mcid_page_local) + 1);
  }],
  ["isolated row source retag", a => {
    const r = a.find(x => x.month === "06" &&
      x.primary_tr_1based_including_header === "9");
    assert(r, "pinned isolated row");
    r.source_git_blob_sha1 = "f".repeat(40);
  }],
  ["whole-source retag", a => {
    for (const r of a) if (r.month === "06")
      r.source_git_blob_sha1 = "f".repeat(40);
  }]
];
for (const [label, mutate] of c460Bypasses) {
  const copy = source.map(r => ({ ...r }));
  mutate(copy);
  assert.deepEqual(geometryErrors(copy), [],
    "C460 expected previous C459 gate blind spot: " + label);
  assert(c460PinnedMcidErrors(copy).length > 0,
    "C460 pinned gate admitted adversary: " + label);
}
// All 62 original-derived observations have 5 core, 3 crew fields and
// optional Date/Pairing MCIDs: 310 + 3*247 + 35 + 30 = 1116 unique.
const c460AllMcids = source.flatMap(r => [
  "date", "pairing", "activity", "from", "to", "blh", "acreg",
  "emp", "cc", "pos"
].flatMap(field => (r[field + "_mcid_page_local"] ||
  r[field + "_leaf_mcids_page_local"] || "").split("|").filter(Boolean)));
assert.equal(c460AllMcids.length, 1116, "C460 1116 source-derived MCIDs");

function classify(changes) {
  const x = { ...fixture.policyModel.defaults, ...changes };
  if (x.privacy !== "CLEAN") return "REJECT_PRIVACY";
  if (x.backupOwner !== "SAME") return "REJECT_FOREIGN_BACKUP";
  if (x.layout !== "SUPPORTED") return "REJECT_LAYOUT";
  if (!x.complete) return "REJECT_INCOMPLETE_EXPORT";
  if (x.activity === "NONFLIGHT") return "EXCLUDE_NONFLIGHT";
  if (x.activity !== "FLIGHT_CANDIDATE") return "HOLD_ACTIVITY";
  if (x.ownDate !== "PRESENT" || x.dateConflict) return "HOLD_DATE";
  // Pairing is deliberately NOT required when the row has its own Date.
  if (!x.year || !x.carrier || !x.subject || !x.publication)
    return "HOLD_SOURCE_AUTHORITY";
  if (x.uid !== "SAME") return "HOLD_UID";
  if (x.activeMatches !== 1) return "HOLD_MATCH_CARDINALITY";
  if (x.owner !== "APPROVED" || x.operation === "CANCEL") return "NO_COMMIT_USER";
  if (x.operation === "CRASH") return "NO_COMMIT_ROLLBACK_REQUIRED";
  if (x.recordRevision !== "CURRENT") return "NO_COMMIT_CONFLICT";
  if (x.sourceChange === "CREW_CHANGED_SAME_BLH") return "REVIEW_CREW_REVISION";
  if (x.sourceChange === "FINGERPRINT_ONLY") return "REVIEW_SOURCE_REVISION";
  if (x.sourceChange === "PARSER_REINTERPRET") return "REVIEW_REINTERPRETATION";
  if (x.sourceChange === "BLH_DISAGREES") return "REVIEW_DURATION_CONFLICT";
  if (x.sourceChange === "EXACT_REPLAY") return "HOLD_DEDUP_MECHANISM";
  if (x.crew === "NOT_PROVIDED" && x.priorCrew) return "PRESERVE_EXISTING_CREW";
  return "REVIEW_ELIGIBLE_NO_PERSISTENCE_APPROVAL";
}
for (const c of fixture.policyModel.scenarios) {
  assert.equal(c.kind, "SYNTHETIC_POLICY_ONLY");
  assert.equal(classify(c.changes), c.expected, "synthetic policy " + c.id);
}
assert.equal(new Set(fixture.policyModel.scenarios.map(c => c.id)).size,
  fixture.policyModel.scenarios.length);

// C461 pinned *candidate census* regression. This is NOT PDF completeness:
// C194 contains selected numeric rows only, not the full primary table,
// nonflight bands, Sum/footer, or all PDF page/section boundaries.
// The full C457 oracle already pins all 62 fixture rows; the purpose here is
// to show that the C460 *local MCID-integrity function by itself* can accept
// dropped rows/pages. Production must validate a fresh full-document census.
const c461ExpectedNumericPageCounts = new Map([
  ["06/1", 16], ["06/2", 2],
  ["07/1", 20], ["07/2", 2],
  ["08/1", 20], ["08/2", 2]
]);
function c461PinnedCensusErrors(items) {
  const errors = [];
  const counts = new Map();
  const physical = new Set();
  for (const r of items) {
    const page = r.month + "/" + r.page_1based;
    counts.set(page, (counts.get(page) ?? 0) + 1);
    if (!c461ExpectedNumericPageCounts.has(page))
      errors.push("unrecognized pinned numeric page");
    const locator = [r.source_git_blob_sha1, r.page_1based,
      r.primary_tr_1based_including_header].join("/");
    if (physical.has(locator)) errors.push("duplicate physical candidate");
    physical.add(locator);
  }
  for (const [page, expected] of c461ExpectedNumericPageCounts)
    if ((counts.get(page) ?? 0) !== expected)
      errors.push("missing or extra numeric candidate: " + page);
  return errors;
}
assert.deepEqual(c461PinnedCensusErrors(source), [], "C461 pinned numeric census");
const c461AugPage2 = source.find(r =>
  r.month === "08" && r.page_1based === "2" &&
  r.crew_leaf_shape !== "SINGLELEAF_1");
assert(c461AugPage2, "C461 pinned August page2 direct candidate");
const c461RemoveCases = [
  ["one August page2 direct candidate", a => a.filter(r => r !== c461AugPage2)],
  ["whole June page2", a => a.filter(r =>
    !(r.month === "06" && r.page_1based === "2"))],
  ["whole August page2", a => a.filter(r =>
    !(r.month === "08" && r.page_1based === "2"))]
];
for (const [label, remove] of c461RemoveCases) {
  const incomplete = remove(source);
  // Demonstrates insufficiency of the local integrity check, NOT a bypass
  // of the global fixture's 62-row deep-equality and source pin.
  assert.deepEqual(c460PinnedMcidErrors(incomplete), [],
    "C461 expected local MCID gate to miss omission: " + label);
  assert(c461PinnedCensusErrors(incomplete).length > 0,
    "C461 pinned numeric census missed omission: " + label);
}
const c461Duplicate = [...source, { ...source[0] }];
assert(c460PinnedMcidErrors(c461Duplicate).length > 0,
  "C461 duplicate must fail local MCID gate");
assert(c461PinnedCensusErrors(c461Duplicate).length > 0,
  "C461 duplicate must fail pinned census");


// C468 pinned source-binding gate: the C457 whole-file Git blob pin protects
// the fixture on disk, but standalone geometry/MCID/page-census validators
// did not bind each row's source_raw_sha256 to its Git blob and month.
// This is a RESEARCH-ONLY fixture-integrity check, not a PDF parser or
// authorization to persist private source identifiers in product data.
const c468SourceBindings = new Map();
for (const r of source) {
  const git = r.source_git_blob_sha1;
  const pair = { raw: r.source_raw_sha256, month: r.month };
  const prior = c468SourceBindings.get(git);
  if (prior) assert.deepEqual(prior, pair, "pinned source binding");
  else c468SourceBindings.set(git, pair);
}
assert.equal(c468SourceBindings.size, 3, "three distinct source bindings");
assert.equal(new Set([...c468SourceBindings.values()].map(x => x.raw)).size, 3,
  "no cross-source SHA256 alias");
function c468SourceBindingErrors(items) {
  const errors = [];
  for (const r of items) {
    const pin = c468SourceBindings.get(r.source_git_blob_sha1);
    if (!pin || pin.raw !== r.source_raw_sha256 || pin.month !== r.month)
      errors.push("source Git blob / raw SHA256 / month mismatch");
    if (!/^[a-f0-9]{40}$/.test(r.source_git_blob_sha1))
      errors.push("invalid source Git blob SHA1");
    if (!/^[a-f0-9]{64}$/.test(r.source_raw_sha256))
      errors.push("invalid source raw SHA256");
    if (![1, 2].includes(Number(r.page_1based)))
      errors.push("unrecognized pinned page");
    for (const field of ["date", "pairing"]) {
      const state = r[field + "_cell_state"];
      const leaves = r[field + "_leaf_mcids_page_local"];
      if (state === "PRESENT") {
        if (!/^\d+(?:\|\d+)*$/.test(leaves))
          errors.push("present optional cell missing MCID: " + field);
      } else if (state === "ABSENT") {
        if (leaves !== "")
          errors.push("absent optional cell has MCID: " + field);
      } else errors.push("unknown optional cell state: " + field);
    }
  }
  return errors;
}
assert.deepEqual(c468SourceBindingErrors(source), [],
  "C468 original-derived source bindings");
const c468SourceMutants = [
  ["one raw SHA256 retag", a => { a[0].source_raw_sha256 = "f".repeat(64); }],
  ["whole-month raw SHA256 retag", a => {
    for (const r of a) if (r.month === "06")
      r.source_raw_sha256 = "f".repeat(64);
  }],
  ["cross-source raw SHA256", a => {
    a[0].source_raw_sha256 = source.find(r => r.month === "07").source_raw_sha256;
  }],
  ["one row month retag", a => { a[0].month = "07"; }],
  ["unsupported page", a => { a[0].page_1based = "3"; }],
  ["present Date MCID erased", a => {
    a.find(r => r.date_cell_state === "PRESENT").date_leaf_mcids_page_local = "";
  }],
  ["absent Date stray MCID", a => {
    a.find(r => r.date_cell_state === "ABSENT").date_leaf_mcids_page_local = "999";
  }],
  ["present Pairing MCID erased", a => {
    a.find(r => r.pairing_cell_state === "PRESENT").pairing_leaf_mcids_page_local = "";
  }],
  ["absent Pairing stray MCID", a => {
    a.find(r => r.pairing_cell_state === "ABSENT").pairing_leaf_mcids_page_local = "999";
  }],
  ["invalid raw SHA256", a => { a[0].source_raw_sha256 = "invalid"; }],
  ["known but wrong Git source", a => {
    a[0].source_git_blob_sha1 = source.find(r => r.month === "07").source_git_blob_sha1;
  }]
];
for (const [label, mutate] of c468SourceMutants) {
  const copy = source.map(r => ({ ...r }));
  mutate(copy);
  assert(c468SourceBindingErrors(copy).length > 0,
    "C468 source-binding mutant admitted: " + label);
}

// C468 PDC 14-column *observed* clock lexical grammar. Original private
// August PDC 49-band census was independently inspected in transient memory:
// 26 numeric Activity bands, 23 others, 26/26 base elapsed=printed Blk Hrs,
// and 4 numeric bands with bare +1 marker (not parenthesized).
// This code uses SYNTHETIC strings only. Nonflight clock-bearing bands must
// never be admitted by a clock grammar match. No timezone or duty inference.
function c468PdcRawClock(raw) {
  const m = /^(\d{2})(\d{2})([+-]\d+)?$/.exec(raw);
  if (!m || Number(m[1]) > 23 || Number(m[2]) > 59) return null;
  // Restricted observed family only: +1 on numeric; -1/+3 also observed
  // on nonnumeric bands. A new marker is an unsupported-layout HOLD.
  if (m[3] && !["+1", "-1", "+3"].includes(m[3])) return null;
  return { minute: Number(m[1]) * 60 + Number(m[2]),
    rawDayMarker: m[3] ?? null };
}
const c468ClockCases = [
  ["2350+1", true], ["0010", true], ["2350(+1)", false],
  ["2400", false], ["1260", false], ["0100-1", true],
  ["0010+3", true], ["0100+7", false], ["0100+0", false],
  ["0100+2", false], ["0100+1", true]
];
for (const [raw, expected] of c468ClockCases)
  assert.equal(c468PdcRawClock(raw) !== null, expected,
    "C468 synthetic raw-clock lexical " + raw);
const c468SyntheticStart = c468PdcRawClock("2350");
const c468SyntheticEnd = c468PdcRawClock("0100+1");
assert.equal(c468SyntheticEnd.minute + 1440 -
  c468SyntheticStart.minute, 70, "C468 synthetic day-marker arithmetic");
assert.equal(c468PdcRawClock("0100(+1)"), null,
  "C468 no silent parenthesized-marker repair");


// C468 company/PDC minute-normalized duration comparison (SYNTHETIC).
// In two conditionally matched ORIGINAL PDC↔2026-company observations,
// raw H:MM text was unequal 0/2 while parsed integer minutes agreed 2/2.
// This is formatting equivalence only, not source/UID or Block authority.
function c468ParsePrintedDuration(raw) {
  const m = /^(\d+):([0-5]\d)$/.exec(raw);
  return m ? Number(m[1]) * 60 + Number(m[2]) : null;
}
const c468DurationCases = [
  ["01:25", 85], ["1:25", 85], ["00:00", 0],
  ["1:60", null], ["1:5", null], ["-1:25", null],
  ["1:25x", null], ["1.25", null]
];
for (const [raw, expected] of c468DurationCases)
  assert.equal(c468ParsePrintedDuration(raw), expected,
    "C468 synthetic printed-duration " + raw);
assert.notEqual("01:25", "1:25", "C468 raw text preserved");
assert.equal(c468ParsePrintedDuration("01:25"),
  c468ParsePrintedDuration("1:25"), "C468 normalized minute equality");


// C471: source-derived PHYSICAL crew-pipe ancestry gate, pinned to the C194
// privacy-safe three-month locator manifest. NOT participant identity, duty
// continuation, operational Date inheritance, or production PDF admission.
// The same-source/same-page anchor and ordinal are physical provenance only.
function c471PipeAncestryErrors(items) {
  const errors = [], index = new Map(), groups = new Map();
  for (const r of items) {
    const key = [r.source_git_blob_sha1, r.page_1based,
      r.primary_tr_1based_including_header].join("/");
    if (index.has(key)) errors.push("duplicate source-scoped TR");
    index.set(key, r);
  }
  for (const r of items) {
    if (r.crew_leaf_shape !== "SINGLELEAF_1") continue;
    const anchorKey = [r.source_git_blob_sha1, r.page_1based,
      r.physical_multileaf_anchor_tr_1based].join("/");
    const anchor = index.get(anchorKey);
    if (!anchor || !["MULTILEAF_6", "MULTILEAF_7"].includes(anchor.crew_leaf_shape))
      errors.push("missing same-source/page multileaf anchor");
    else if (anchor.date_cell_state !== "PRESENT")
      errors.push("physical anchor Date absent: HOLD, no inheritance");
    if (r.date_cell_state !== "ABSENT" ||
        r.pairing_cell_state !== "ABSENT")
      errors.push("unexpected own Date/Pairing on pipe");
    const depth = Number(r.singleleaf_chain_depth);
    if (!Number.isSafeInteger(depth) || depth < 1 || depth > 3)
      errors.push("unsupported observed pipe depth");
    groups.set(anchorKey, [...(groups.get(anchorKey) ?? []), depth]);
  }
  for (const [key, depths] of groups) {
    const ordered = [...depths].sort((a,b) => a-b);
    if (ordered.some((depth,i) => depth !== i+1))
      errors.push("noncontiguous/duplicate pipe ordinal: " + key);
  }
  return { errors, groups };
}
const c471Baseline = c471PipeAncestryErrors(source);
if (c471Baseline.errors.length) throw Error("C471 pinned baseline rejected");
const c471GroupSizes = [...c471Baseline.groups.values()]
  .reduce((out, a) => (out[a.length] = (out[a.length] ?? 0) + 1, out), {});
if (source.filter(r => r.crew_leaf_shape === "SINGLELEAF_1").length !== 26 ||
    c471Baseline.groups.size !== 22 ||
    c471GroupSizes[1] !== 20 || c471GroupSizes[3] !== 2 ||
    Object.keys(c471GroupSizes).length !== 2)
  throw Error("C471 pinned chain-group census drift");
const c471Anchors = [...c471Baseline.groups.keys()].map(key =>
  source.find(r => [r.source_git_blob_sha1,r.page_1based,
    r.primary_tr_1based_including_header].join("/") === key));
if (c471Anchors.some(r => !r || r.date_cell_state !== "PRESENT") ||
    c471Anchors.filter(r => r.pairing_cell_state === "ABSENT").length !== 2)
  throw Error("C471 pinned anchor ownership drift");
const c471DirectUndated = source.filter(r =>
  r.crew_leaf_shape !== "SINGLELEAF_1" && r.date_cell_state === "ABSENT");
if (c471DirectUndated.length !== 1 ||
    c471DirectUndated[0].month !== "08")
  throw Error("C471 direct-undated detached observation drift");
const c471Pipe = source.findIndex(r => r.crew_leaf_shape === "SINGLELEAF_1");
const c471Triple = [...c471Baseline.groups].find(([,depths]) =>
  depths.length === 3)[0];
const c471TripleRows = source.map((r,i) =>
  ({r,i})).filter(({r}) => r.crew_leaf_shape === "SINGLELEAF_1" &&
    [r.source_git_blob_sha1,r.page_1based,
     r.physical_multileaf_anchor_tr_1based].join("/") === c471Triple);
const c471Mutants = [
  ["orphan anchor", a => { a[c471Pipe].physical_multileaf_anchor_tr_1based = "999"; }],
  ["self-as-anchor", a => { a[c471Pipe].physical_multileaf_anchor_tr_1based =
    a[c471Pipe].primary_tr_1based_including_header; }],
  ["cross-page pipe", a => { a[c471Pipe].page_1based = "3"; }],
  ["cross-source pipe", a => { a[c471Pipe].source_git_blob_sha1 = "f".repeat(40); }],
  ["own Date on pipe", a => { a[c471Pipe].date_cell_state = "PRESENT"; }],
  ["own Pairing on pipe", a => { a[c471Pipe].pairing_cell_state = "PRESENT"; }],
  ["depth zero", a => { a[c471Pipe].singleleaf_chain_depth = "0"; }],
  ["depth four", a => { a[c471Pipe].singleleaf_chain_depth = "4"; }],
  ["duplicate triple depth", a => {
    a[c471TripleRows[1].i].singleleaf_chain_depth =
      a[c471TripleRows[0].i].singleleaf_chain_depth;
  }],
  ["triple depth gap", a => { a[c471TripleRows[2].i].singleleaf_chain_depth = "5"; }],
  ["anchor Date removed", a => {
    const k = c471Triple;
    const i = a.findIndex(r => [r.source_git_blob_sha1,r.page_1based,
      r.primary_tr_1based_including_header].join("/") === k);
    a[i].date_cell_state = "ABSENT";
  }],
  ["anchor no longer multileaf", a => {
    const k = c471Triple;
    const i = a.findIndex(r => [r.source_git_blob_sha1,r.page_1based,
      r.primary_tr_1based_including_header].join("/") === k);
    a[i].crew_leaf_shape = "UNKNOWN";
  }]
];
for (const [label, mutate] of c471Mutants) {
  const copy = source.map(r => ({...r}));
  mutate(copy);
  if (!c471PipeAncestryErrors(copy).errors.length)
    throw Error("C471 ancestry mutant admitted: " + label);
}
// A dated physical anchor is NOT an operational-date or crew authority.
// Do not forward-fill Date, Pairing, crew identity, role, or BLH on this basis.

console.log(JSON.stringify({
  status: "RESEARCH_ONLY", pinnedManifest: true, skiaPhysicalRows: rows.length,
  pdcNumericAggregate: 26, physicalGroups: [size(1), size(2), size(4)],
  syntheticPolicyCases: fixture.policyModel.scenarios.length,
  c459ObservedLayoutBases: [28, 29, 32], c459GeometryMutantsRejected: 12,
  c460AllFieldMcids: 1116, c460PriorGateBypassesNowRejected: 6,
  c461PinnedPageNumericCounts: [16, 2, 20, 2, 20, 2],
  c461OmissionAdversaries: 3, c461DuplicateAdversaries: 1,
  c468SourceBindings: 3, c468SourceMutantsRejected: 11,
  c468SyntheticClockCases: 11, c468SyntheticDurationCases: 8, c468RealPdcRecheck: "49 bands / 26 numeric / 4 bare +1 numeric / 26 base arithmetic matches (separate original inspection)",
  actualPdfDecode: false, uidOwnedDartSembast: false,
  productionReadiness: "OPEN"
}, null, 2));
// C478 pinned Skia three-month whole-document structural census and Sum/auxiliary
// gate. PRIOR-ORIGINAL-DERIVED METADATA + SYNTHETIC MUTATIONS ONLY.
// Not new raw-PDF lexical validation, production parser, or UID matching.
function c478SkiaWholeDocumentGate(items, parentTree, pdcSummary, pinnedRows) {
 const errors=[],push=(ok,reason)=>{if(!ok)errors.push(reason)};
 const expected={"06":[40,18,22,0,8,257],"07":[44,22,22,7,30,241],"08":[42,22,20,5,28,311]};
 const key=r=>[r.month,r.source_raw_sha256,r.page_1based,r.primary_tr_1based_including_header].join("/");
 const pins=new Map(pinnedRows.map(r=>[key(r),r]));
 const seen=new Set(),sources=new Set();let pageTwoCount=0,leafChecks=0;
 push(parentTree.id==="C295","WRONG_PARENTTREE_PROFILE");
 push(pdcSummary.pdc?.nonnumericWithFourClocks===22&&pdcSummary.pdc?.auxiliaryActivityTextAbsentButOtherCellPresent===1,"CROSS_FAMILY_PDC_BASELINE_CHANGED");
 push(items.length===62,"CANDIDATE_COUNT_CHANGED");
 push(parentTree.sourceDerived?.length===3,"MONTH_SOURCE_COUNT");
 for(const month of ["06","07","08"]){
  const subset=items.filter(r=>r.month===month),t=parentTree.sourceDerived?.find(x=>x.month===month),e=expected[month];
  push(!!t,"MISSING_MONTH_PARENTTREE_"+month);if(!t)continue;
  push(t.primaryRowsIncludingHeader-1===e[0],"PRIMARY_BODY_CENSUS_"+month);
  push(subset.length===e[1],"SELECTED_CANDIDATE_CENSUS_"+month);
  push(t.primaryRowsIncludingHeader-1-subset.length===e[2],"RESIDUAL_NONSELECTED_CENSUS_"+month);
  push(t.postSumAuxiliaryTableRows===e[3]&&t.postSumNonTableMCIDs===e[4],"POST_SUM_CENSUS_"+month);
  push(t.sumMCID===e[5]&&t.primaryLeafRange[1]+1===t.sumMCID,"SUM_PARENTTREE_BARRIER_"+month);
  push(t.primaryLeafRange[0]===2,"PRIMARY_LEAF_START_"+month);
  const ar=t.postSumAuxiliaryLeafRange;
  push(e[3]===0?ar===null:(Array.isArray(ar)&&ar[0]>t.sumMCID&&ar[1]-ar[0]+1===2*e[3]),"AUXILIARY_AFTER_SUM_"+month);
  const src=new Set(subset.map(r=>r.source_raw_sha256+"|"+r.source_git_blob_sha1));
  push(src.size===1,"SOURCE_FINGERPRINT_SPLIT_"+month);
  if(src.size===1)sources.add([...src][0]);
  for(const r of subset){
   const id=key(r);push(!seen.has(id),"DUPLICATE_SOURCE_PAGE_TR");seen.add(id);
   const pin=pins.get(id);
   push(!!pin,"UNPINNED_NUMERIC_ROW");
   if(pin)push(r.activity_mcid_page_local===pin.activity_mcid_page_local&&r.blh_mcid_page_local===pin.blh_mcid_page_local&&r.date_cell_state===pin.date_cell_state&&r.crew_leaf_shape===pin.crew_leaf_shape,"ROW_FIELD_OWNERSHIP_DRIFT");
   const pg=+r.page_1based,tr=+r.primary_tr_1based_including_header;
   push((pg===1||pg===2)&&tr>=2&&tr<=t.primaryRowsIncludingHeader,"INVALID_PAGE_TR");
   push(/^[a-f0-9]{64}$/.test(r.source_raw_sha256||"")&&/^[a-f0-9]{40}$/.test(r.source_git_blob_sha1||""),"INVALID_SOURCE_DIGEST");
   push(["PRESENT","ABSENT"].includes(r.date_cell_state)&&["PRESENT","ABSENT"].includes(r.pairing_cell_state),"INVALID_PRESENCE_STATE");
   if(pg===2){
    pageTwoCount++;
    const mcids=Object.entries(r).filter(([k])=>k.endsWith("mcid_page_local")||k.endsWith("mcids_page_local")).flatMap(([,v])=>String(v).split("|").filter(Boolean).map(Number));
    leafChecks+=mcids.length;
    push(mcids.length>0&&mcids.every(n=>Number.isInteger(n)&&n>0&&n<t.sumMCID),"PAGE2_LEAF_AT_OR_AFTER_SUM");
   }
  }
 }
 push(sources.size===3,"CROSS_MONTH_SOURCE_ALIAS");
 push(pageTwoCount===6,"PAGE2_CANDIDATE_CENSUS");
 push(leafChecks===135,"PAGE2_SELECTED_LEAF_CENSUS");
 push(pins.size===62&&seen.size===62,"PINNED_NUMERIC_SET_INCOMPLETE");
 return {errors,summary:{primaryBody:126,numeric:items.length,nonselectedPrimary:126-items.length,auxiliaryRows:12,sumBarriers:3,pageTwoCandidates:pageTwoCount,pageTwoSelectedLeaves:leafChecks,pdcNumeric:Object.values(pdcSummary.pdc.numericDatePairTextPresence).reduce((a,b)=>a+b,0),verifiedNonflightLexical:false,production:false}};
}
const c478Parent=JSON.parse(read("C295_SKIA_PARENTTREE_SUM_AND_AUXILIARY_TABLE_GATE.json").toString("utf8"));
const c478Pdc=JSON.parse(pdcBytes.toString("utf8"));
const c478Baseline=c478SkiaWholeDocumentGate(source,c478Parent,c478Pdc,source);
assert.deepEqual(c478Baseline.errors,[]);
assert.deepEqual(c478Baseline.summary,{primaryBody:126,numeric:62,nonselectedPrimary:64,auxiliaryRows:12,sumBarriers:3,pageTwoCandidates:6,pageTwoSelectedLeaves:135,pdcNumeric:26,verifiedNonflightLexical:false,production:false});
const c478Clone=()=>source.map(r=>({...r}));
const c478Tree=()=>JSON.parse(JSON.stringify(c478Parent));
const c478PdcClone=()=>JSON.parse(JSON.stringify(c478Pdc));
const c478Mutants=[
 ["drop candidate",()=>{let a=c478Clone();a.pop();return[a,c478Tree(),c478PdcClone()]}],
 ["duplicate candidate",()=>{let a=c478Clone();a[1]={...a[0]};return[a,c478Tree(),c478PdcClone()]}],
 ["balanced noncandidate promotion",()=>{let a=c478Clone();a[0].primary_tr_1based_including_header="3";return[a,c478Tree(),c478PdcClone()]}],
 ["source fingerprint split",()=>{let a=c478Clone();a[0].source_raw_sha256="a".repeat(64);return[a,c478Tree(),c478PdcClone()]}],
 ["page three",()=>{let a=c478Clone();a[0].page_1based="3";return[a,c478Tree(),c478PdcClone()]}],
 ["header-as-row",()=>{let a=c478Clone();a[0].primary_tr_1based_including_header="1";return[a,c478Tree(),c478PdcClone()]}],
 ["row beyond primary",()=>{let a=c478Clone();a[0].primary_tr_1based_including_header="99";return[a,c478Tree(),c478PdcClone()]}],
 ["missing Date ownership",()=>{let a=c478Clone();a[0].date_cell_state="ABSENT";return[a,c478Tree(),c478PdcClone()]}],
 ["wrong Activity MCID",()=>{let a=c478Clone();a[0].activity_mcid_page_local="999";return[a,c478Tree(),c478PdcClone()]}],
 ["sum reparent to primary",()=>{let t=c478Tree();t.sourceDerived[0].sumMCID=256;return[c478Clone(),t,c478PdcClone()]}],
 ["aux before sum",()=>{let t=c478Tree();t.sourceDerived[1].postSumAuxiliaryLeafRange=[240,253];return[c478Clone(),t,c478PdcClone()]}],
 ["aux count drift",()=>{let t=c478Tree();t.sourceDerived[2].postSumAuxiliaryTableRows=4;return[c478Clone(),t,c478PdcClone()]}],
 ["primary body count drift",()=>{let t=c478Tree();t.sourceDerived[0].primaryRowsIncludingHeader=42;return[c478Clone(),t,c478PdcClone()]}],
 ["page2 leaf crosses Sum",()=>{let a=c478Clone();a.find(r=>r.page_1based==="2"&&r.month==="06").blh_mcid_page_local="257";return[a,c478Tree(),c478PdcClone()]}],
 ["page2 leaf missing",()=>{let a=c478Clone();a.find(r=>r.page_1based==="2"&&r.month==="06").blh_mcid_page_local="";return[a,c478Tree(),c478PdcClone()]}],
 ["PDC family baseline drift",()=>{let q=c478PdcClone();q.pdc.nonnumericWithFourClocks=21;return[c478Clone(),c478Tree(),q]}],
 ["source month alias",()=>{let a=c478Clone();for(const r of a.filter(x=>x.month==="07")){r.source_raw_sha256=a[0].source_raw_sha256;r.source_git_blob_sha1=a[0].source_git_blob_sha1}return[a,c478Tree(),c478PdcClone()]}]
];
for(const [label,make] of c478Mutants){const [a,t,q]=make();assert(c478SkiaWholeDocumentGate(a,t,q,source).errors.length>0,"C478 mutant admitted: "+label);}
console.log(JSON.stringify({c478:"RESEARCH_ONLY",priorOriginalDerived:true,newPrivatePdfDecode:false,skia:c478Baseline.summary,syntheticMutantsRejected:c478Mutants.length,production:"OPEN"}));
