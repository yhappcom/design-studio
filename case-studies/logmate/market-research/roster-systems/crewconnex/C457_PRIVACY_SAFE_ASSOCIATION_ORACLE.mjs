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
console.log(JSON.stringify({
  status: "RESEARCH_ONLY", pinnedManifest: true, skiaPhysicalRows: rows.length,
  pdcNumericAggregate: 26, physicalGroups: [size(1), size(2), size(4)],
  syntheticPolicyCases: fixture.policyModel.scenarios.length,
  c459ObservedLayoutBases: [28, 29, 32], c459GeometryMutantsRejected: 12,
  c460AllFieldMcids: 1116, c460PriorGateBypassesNowRejected: 6,
  actualPdfDecode: false, uidOwnedDartSembast: false,
  productionReadiness: "OPEN"
}, null, 2));
