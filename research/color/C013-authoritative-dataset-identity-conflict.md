# C013 — Authoritative Dataset Identity Conflict and Artifact-First Colorimetry

Status: **PRACTICE + CONTRADICTION REVIEW / authoritative-surface checksum conflict reproduced; artifact-first intake gate defined; exact raw CIE 1964/LMS bytes still unavailable in this execution environment**

## Why this study exists

C012 deliberately left two provenance gates open:

- the current CIE 1964 10° raw-file identity had not been independently hashed;
- the CIE 2006 2° LMS file available through public mirrors did not match the checksum shown on the CIE dataset page.

The initial assumption was that stronger access to the current CIE metadata would resolve those questions.

C013 found something more important: **the authoritative CIE HTML dataset page and its own linked CIE metadata JSON currently disagree for two relevant datasets.**

That changes the problem from “which mirror is current?” to:

> What should a professional Color workflow do when two first-party authority surfaces publish different identities for what is nominally the same data file?

C013 therefore studies dataset identity as a production/colorimetry contract rather than treating checksums as incidental file-download details.

Reproducibility artifacts:

- `C013-provenance-conflict-gate.py`
- `C013-provenance-conflict-results.json`

The study does **not** redistribute CIE data tables.

---

## RELATED DOMAIN CHECK

### Typography / Type
- Evidence checked: current Type status through T014, especially deterministic rebuild and package-provenance practice.
- Reusable finding: a nominally equivalent source/package name is not sufficient evidence that the same artifact was built or shipped; exact artifact identity and reproducibility matter before downstream visual conclusions.
- Replication / challenge / transfer opportunity: C013 independently transfers that provenance discipline to numerical Color datasets.
- Dependency or overlap: Type is not required for the colorimetric identity decision itself. The methodological overlap is deliberate and useful.

### Color
- Evidence checked: Studies 010/011, C004, C005, C010 and C012.
- Reusable finding: observer definition, dataset version, spectral grid, NaN/interpolation policy and transform path are part of the calculation contract.
- Replication / challenge / transfer opportunity: challenge C012's provisional framing of a single “current published checksum” where the first-party page and first-party metadata disagree.
- Dependency or overlap: direct contradiction review and extension of C012.

### Layout / Interaction
- Evidence checked: current Layout/Interaction status through L006/I004.
- Reusable finding: diagnose failures at the correct layer; a data-identity failure must not be hidden by a downstream visual or interaction workaround.
- Replication / challenge / transfer opportunity: not materially relevant to the checksum comparison itself.
- Dependency or overlap: none for the core source audit.

### Web Design
- Evidence checked: current Web status; no substantive W### evidence exists at this checkpoint.
- Reusable finding: browser/device validation can only be interpreted correctly when the Color input artifact is known.
- Implementation/application validation opportunity: future Web wide-gamut/device work should preserve the exact profile/dataset/token artifacts used behind a claimed result.
- Dependency or overlap: no Web PASS is inferred.

### Other / Cross-cutting / Future Specialist
- Evidence checked: current CIE dataset HTML pages, their linked CIE metadata JSON, CIE's general dataset guidance, pinned public mirrors, and an independent public checksum-failure report.
- Reusable finding: authority is not the same as internal consistency. A first-party source can expose multiple version surfaces that disagree.
- Dependency or overlap: raw-byte retrieval from the CIE file host remains the decisive missing evidence for the conflicted files.

### Overlap decision
- **CONTRADICTION REVIEW + REPLICATION + METHOD EXTENSION**.
- Why: C012 already treated checksums as provenance evidence. C013 tests the authority layer itself and finds a first-party inconsistency that materially changes the validation method.

---

# SOURCE — CIE's data-table guidance

CIE's dataset index states that its datasets are taken from the cited original publications. It also states that blanks in source tables may appear as `NaN` and can usually be set to zero for computational purposes, with the cited publication controlling in cases of doubt.

Source:

- `https://www.cie.co.at/data-tables`

### SYNTHESIS

Two different questions must therefore be separated:

1. **artifact identity** — are these the same exact bytes/version of the source dataset?
2. **computational interpretation** — after the source is identified, how should `NaN`, interpolation or extrapolation be handled for the intended calculation?

Replacing `NaN` with numeric zero can be a valid documented computational operation while still producing a different byte-level artifact.

A checksum answers the first question, not the second.

---

# SOURCE AUDIT A — CIE 1931 2° is the consistency control

Dataset page:

- `https://cie.co.at/datatable/cie-1931-colour-matching-functions-2-degree-observer`

Linked metadata:

- `https://files.cie.co.at/CIE_xyz_1931_2deg.csv_metadata.json`

Observed MD5 values:

| Authority surface | MD5 |
| --- | --- |
| CIE HTML dataset page | `17cca777db64b17170f06f67ce9d3ab7` |
| linked CIE metadata JSON | `17cca777db64b17170f06f67ce9d3ab7` |

These agree.

C012 separately reconstructed the same checksum from a pinned copy with the expected 360–830 nm / 1 nm grid and validation sums.

### RESULT

CIE 1931 is the positive control showing that the two first-party surfaces **can** agree and that C013 is not merely observing a universal HTML-vs-JSON formatting difference.

---

# SOURCE AUDIT B — CIE 1964 10° first-party checksum contradiction

Dataset page:

- `https://cie.co.at/datatable/cie-1964-colour-matching-functions-10-degree-observer`
- DOI `10.25039/CIE.DS.sqksu2n5`

The HTML page currently reports MD5:

`cd6135a724480eb8c5e7668bae914445`

The metadata JSON linked by that same page is:

- `https://files.cie.co.at/CIE_xyz_1964_10deg.csv_metadata.json`

and currently reports MD5:

`6140e032f9326d88c5a0959b29b4d8f3`

with SHA-256:

`1b27fd4e8ca1167b47c3a6aee3aafe56abc57eae51fa20032cb83704224a27dc`.

### CONTRADICTION

The page and the linked metadata identify the nominally same `CIE_xyz_1964_10deg.csv` with different MD5 values.

This is not merely a third-party mirror disagreement.

### Mirror triangulation

A pinned `wetadigital/physlight` copy carries metadata with the `6140e032...` lineage and sample values consistent with that older/linked metadata family.

A pinned `chran554/pathtracer` metadata copy reports the HTML-page checksum `cd6135...` and a different SHA-256, demonstrating that the alternate identity also propagated into public copies.

C013 does **not** promote either mirror to authority.

### Important boundary

The execution environment could not retrieve the CIE CSV as raw bytes because the CSV endpoint was not available through the current connector path. Therefore the decisive question — which checksum the currently served raw file actually matches — remains unresolved here.

---

# SOURCE AUDIT C — CIE 2006 2° LMS first-party checksum contradiction

Dataset page:

- `https://cie.co.at/datatable/cie-2006-lms-cone-fundamentals-2-field-size-terms-energy`
- DOI `10.25039/CIE.DS.tijidesg`

The HTML page currently reports MD5:

`27c74cc0f98edecadc02fc71f540b116`

The metadata JSON linked by that same page is:

- `https://files.cie.co.at/CIE_lms_cf_2deg.csv_metadata.json`

and currently reports MD5:

`dba2e9d1f5e6667575aa069832159510`

with SHA-256:

`f48160edf11c1a121aaaf41d4c3b7513385bfc9c60d726b88e735519f6d37b1f`.

The linked metadata describes:

- wavelength range `390–830 nm`;
- `5 nm` increment;
- `S` values through `615 nm`;
- `dataQuality: approximated`.

### CONTRADICTION

Again, the first-party HTML page and first-party linked metadata disagree about the identity of the nominally same CSV.

### Independent replication of the ambiguity

A separate public experiment (`SmartVoltISA/Omega-lab-.--.-`) recorded an attempted download where:

- expected from the CIE page: `27c74cc...`;
- downloaded file MD5: `dba2e9d1...`.

That independently reproduces the same two checksum families seen in the CIE first-party surfaces.

### REVISION OF C012 INTERPRETATION

C012 described the accessible `dba2...` file as conflicting with the “current CIE-published checksum” `27c74...`.

C013 refines that statement:

> CIE currently exposes **conflicting first-party checksum claims** for the LMS file. The accessible `dba2...` identity agrees with CIE's own linked metadata JSON, while the HTML dataset page reports `27c74...`.

The unresolved issue is therefore not simply “mirror versus authority.” It is **authority-surface version conflict**.

---

# SOURCE AUDIT D — cone-fundamental-based spectral tristimulus tables provide a cleaner future path

CIE also publishes the later cone-fundamental-based spectral tristimulus-value tables from CIE 170-2:2015.

## 2° field

Page:

- `https://www.cie.co.at/datatable/cie-cone-fundamental-based-spectral-tristimulus-values-2-degree-field-size`
- DOI `10.25039/CIE.DS.548rw69q`

Page MD5:

`472cc50b14a6cf41ba9f08f8935aedc8`

Linked metadata MD5:

`472cc50b14a6cf41ba9f08f8935aedc8`

Metadata describes a `390–830 nm`, `1 nm` table of `x̄_F`, `ȳ_F`, `z̄_F` spectral tristimulus values from CIE 170-2:2015 Table 10.7a.

## 10° field

Page:

- `https://www.cie.co.at/datatable/cie-cone-fundamental-based-spectral-tristimulus-values-10-field-size`
- DOI `10.25039/CIE.DS.dm6qiig7`

Page MD5:

`c8504e70d7f4760253a0a4d3a42b7d20`

Linked metadata MD5:

`c8504e70d7f4760253a0a4d3a42b7d20`

### SYNTHESIS

These are **not the same dataset as the CIE 2006 raw LMS cone fundamentals**. They are later cone-fundamental-based spectral tristimulus tables from CIE 170-2:2015.

They are, however, a stronger candidate for a future verified complete-spectrum observer comparison because:

- their HTML and linked metadata identities currently agree;
- they are 1 nm tables;
- they directly provide spectral tristimulus functions appropriate for comparison with other tristimulus-observer formulations.

### STUDIO JUDGMENT

Do not silently substitute the 2015 cone-fundamental-based tristimulus dataset for a study explicitly claiming to validate the 2006 raw LMS table.

Instead, name the model and dataset exactly and treat the two investigations as different questions.

---

# C013 ARTIFACT-FIRST PROVENANCE GATE

C013 defines five useful states for numerical Color intake.

## 1. `SURFACE_CONSISTENT_RAW_UNVERIFIED`

`HTML checksum == linked metadata checksum`, but raw file bytes have not yet been hashed in the working environment.

Use: source discovery and provisional planning.

Do not use: claim of exact raw-file verification.

## 2. `RAW_VERIFIED`

`HTML checksum == linked metadata checksum == locally computed raw-file checksum`.

Use: canonical numerical work, with dataset version/DOI/grid recorded.

## 3. `AUTHORITY_CONFLICT_RAW_UNAVAILABLE`

`HTML checksum != linked metadata checksum`, and raw bytes cannot be independently hashed.

Use: blocker/contradiction record.

Do not choose a winner by convenience.

## 4. `RAW_MATCHES_ONE_AUTHORITY_SURFACE`

Raw bytes match exactly one of the conflicting first-party identities.

Use: reproducible calculation on that exact artifact **if the artifact is named explicitly**.

Do not call it unqualified “the current official dataset” until the authority conflict is resolved.

## 5. `TRANSFORMED_DERIVATIVE`

Raw data have been modified by operations such as:

- `NaN → 0`;
- interpolation/resampling;
- unit conversion;
- precision rounding;
- column transformation;
- line-ending/serialization change.

Use: derived calculations when transformation is justified and recorded.

Do not reuse the source checksum as the derivative's identity.

---

# FAILURE → REVISION

## Failure 1 — “the official webpage wins”

**Failure:** choose the HTML checksum simply because it is easier to see.

**Revision:** HTML page, downloadable metadata and raw file are separate provenance surfaces. Hash the raw bytes before declaring file identity.

## Failure 2 — “the metadata file wins”

**Failure:** assume file-adjacent JSON is necessarily newer or more authoritative than the page.

**Revision:** preserve the contradiction. Metadata proximity is useful evidence, not proof of version precedence.

## Failure 3 — mirror majority vote

**Failure:** whichever checksum appears in more GitHub repositories is declared correct.

**Revision:** mirrors establish propagation/history, not authority.

## Failure 4 — numerical similarity erases identity

**Failure:** two tables are considered the same source because their numerical effect is tiny.

**Revision:** byte identity, numerical equivalence and perceptual consequence are three separate claims.

## Failure 5 — checksum worship

**Failure:** exact matching bytes are treated as proof that the governing dataset/model is appropriate for the project.

**Revision:** checksum validates artifact identity only. Observer choice, spectral resolution, measurement quality, gamut/device context and project relevance remain separate gates.

---

# PROJECT READINESS CONSEQUENCES

## When should this method be used?

Use C013 when a project depends on external numerical Color assets whose version can materially alter or invalidate a claim:

- CIE observer/spectral tables;
- measured SPDs or reflectance files;
- ICC/output profiles;
- vendor calibration matrices;
- instrument correction files;
- LUTs;
- research datasets used to justify a product threshold.

## When should it not become bureaucracy?

Do not build a checksum ceremony around ordinary hand-authored UI tokens when artifact-version ambiguity is not a meaningful risk.

The method is for provenance-sensitive evidence, not for making every design variable look scientific.

## Required evidence ledger

For provenance-sensitive Color calculations, record as relevant:

`dataset/model → governing publication/DOI → page checksum → metadata checksum → raw-file MD5/SHA-256 → retrieval URL/time → row/grid validation → NaN policy → interpolation/extrapolation → transformations → calculation code/version`.

## Concrete project decisions this changes

- whether a supplied numerical dataset can support a canonical claim;
- whether a calculation should proceed, proceed with an explicit artifact qualifier, or stop;
- whether a discrepancy is source-version, transformation, color-management or device-related;
- whether an external vendor must supply exact calibration/profile artifacts;
- whether a regenerated result is genuinely reproducible.

---

## PRACTICE RESULT — current CIE authority-surface matrix

| Dataset | HTML page MD5 | linked metadata MD5 | Surface state |
| --- | --- | --- | --- |
| CIE 1931 2° XYZ | `17cca777db64b17170f06f67ce9d3ab7` | `17cca777db64b17170f06f67ce9d3ab7` | consistent |
| CIE 1964 10° XYZ | `cd6135a724480eb8c5e7668bae914445` | `6140e032f9326d88c5a0959b29b4d8f3` | **CONFLICT** |
| CIE 2006 2° LMS | `27c74cc0f98edecadc02fc71f540b116` | `dba2e9d1f5e6667575aa069832159510` | **CONFLICT** |
| CIE 170-2:2015 CFB 2° STV | `472cc50b14a6cf41ba9f08f8935aedc8` | `472cc50b14a6cf41ba9f08f8935aedc8` | consistent |
| CIE 170-2:2015 CFB 10° STV | `c8504e70d7f4760253a0a4d3a42b7d20` | `c8504e70d7f4760253a0a4d3a42b7d20` | consistent |

The companion JSON records the same ledger and the decision state produced by the C013 gate.

---

## HANDOFFS TO OTHER SPECIALISTS

### Typography / Type
- Useful finding/context: first-party naming/metadata can still expose multiple artifact identities; exact artifact evidence should precede downstream rendering claims.
- Canonical section: `C013 ARTIFACT-FIRST PROVENANCE GATE`.
- Confirmation / contradiction / transfer note: independently transfers T014-style reproducibility discipline to numerical Color inputs.
- Scope limit: no font/package rule is changed by this study.

### Layout / Interaction
- Useful finding/context: when a visual result is based on a numerical Color dataset, source-version ambiguity should be resolved at the Color/data layer rather than compensated spatially or behaviorally.
- Canonical section: `FAILURE → REVISION`.
- Confirmation / contradiction / transfer note: confirms layer-specific diagnosis.
- Scope limit: no human task or interaction behavior tested.

### Web Design
- Useful finding/context: future wide-gamut/device/browser proofs should record the exact Color profiles/datasets and transformations behind the rendered result.
- Web application / validation consequence: screenshot/browser differences are not interpretable if the upstream Color artifact changed unnoticed.
- Confirmation / contradiction / transfer note: method handoff only; no W### evidence or browser PASS.
- Scope limit: browser/device color management remains a separate transfer-validation problem.

---

# OPEN

- obtain the current raw `CIE_xyz_1964_10deg.csv` bytes from the CIE file host and compute MD5/SHA-256 locally;
- obtain the current raw `CIE_lms_cf_2deg.csv` bytes from the CIE file host and compute MD5/SHA-256 locally;
- determine whether CIE documents a revision/corrigendum explaining the page-vs-metadata checksum divergences;
- independently hash the raw CFB 2°/10° spectral-tristimulus files before using them for canonical numerical comparison;
- after verification, compare the **same complete spectra** under CIE 1931, CIE 1964 and explicitly named cone-fundamental-based tristimulus models;
- retain the 2006 raw-LMS investigation separately rather than silently substituting the 2015 CFB tristimulus tables;
- apply the gate to real measured display/profile/calibration artifacts in a later production study.

## Status implication

C013 does **not** close the 1964 or LMS provenance gate. It makes the gate more accurate.

Newly established:

- CIE 1931 HTML↔metadata consistency control: **confirmed**;
- CIE 1964 HTML↔metadata checksum contradiction: **confirmed**;
- CIE 2006 2° LMS HTML↔metadata checksum contradiction: **confirmed**;
- CIE 170-2:2015 CFB 2°/10° HTML↔metadata consistency: **confirmed**;
- artifact-first provenance classification method: **defined and reproducible**;
- raw current CIE 1964/LMS byte identity: **still OPEN**;
- complete verified observer-model numerical comparison: **still OPEN**.

Color remains **CRITIQUE / Foundation NOT PASSED**. The main advance is methodological: the studio now knows not only how to check a dataset, but how to respond when the authority itself publishes conflicting file identities.