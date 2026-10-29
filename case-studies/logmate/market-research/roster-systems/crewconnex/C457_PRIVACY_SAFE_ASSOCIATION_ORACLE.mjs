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
  actualPdfDecode: false, uidOwnedDartSembast: false,
  productionReadiness: "OPEN"
}, null, 2));
