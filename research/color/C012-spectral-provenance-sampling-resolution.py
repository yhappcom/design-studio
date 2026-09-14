"""C012 reproducible spectral-provenance and sampling-resolution practice.

This harness intentionally does not redistribute CIE datasets. Download the current
CIE 1931 2° CSV from the authoritative CIE source, then pass its local path.
The raw byte MD5 is checked before any numerical result is produced.

Optional CIE 1964 and CIE 2006 LMS paths are checksum-audited only. They are not
used for observer/cone calculations unless their current identities are verified and
a later study explicitly adds that calculation.

The 5 nm exercise is a sampling-grid sensitivity diagnostic. It is not a model of
spectroradiometer optical bandwidth, stray light, wavelength accuracy, or noise.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
from pathlib import Path

import numpy as np

EXPECTED_1931_MD5 = "17cca777db64b17170f06f67ce9d3ab7"
EXPECTED_1964_MD5 = "cd6135a724480eb8c5e7668bae914445"
EXPECTED_2006_LMS_2DEG_MD5 = "27c74cc0f98edecadc02fc71f540b116"


def md5_bytes(data: bytes) -> str:
    return hashlib.md5(data).hexdigest()


def checksum_audit(path: Path | None, expected_md5: str) -> dict | None:
    if path is None:
        return None
    raw = path.read_bytes()
    observed = md5_bytes(raw)
    return {
        "path": str(path),
        "observed_md5": observed,
        "expected_md5": expected_md5,
        "match": observed == expected_md5,
        "size_bytes": len(raw),
    }


def load_cie1931(path: Path) -> tuple[np.ndarray, np.ndarray, dict]:
    raw = path.read_bytes()
    digest = md5_bytes(raw)
    if digest != EXPECTED_1931_MD5:
        raise RuntimeError(
            f"CIE 1931 checksum mismatch: expected {EXPECTED_1931_MD5}, got {digest}"
        )

    rows: list[list[float]] = []
    text = raw.decode("utf-8")
    for row in csv.reader(text.splitlines()):
        rows.append([float(v) for v in row])
    arr = np.asarray(rows, dtype=float)
    wl = arr[:, 0]
    cmf = arr[:, 1:4]

    expected_wl = np.arange(360.0, 831.0, 1.0)
    if len(wl) != 471 or not np.array_equal(wl, expected_wl):
        raise RuntimeError("Unexpected CIE 1931 wavelength grid; expected 360..830 nm / 1 nm")

    provenance = {
        "path": str(path),
        "md5": digest,
        "rows": int(len(wl)),
        "range_nm": [int(wl[0]), int(wl[-1])],
        "step_nm": 1,
    }
    return wl, cmf, provenance


def gaussian(wl: np.ndarray, mu: float, sigma: float) -> np.ndarray:
    return np.exp(-0.5 * ((wl - mu) / sigma) ** 2)


def integrate(
    spd: np.ndarray,
    cmf: np.ndarray,
    indices: np.ndarray | None = None,
    step_nm: float = 1.0,
) -> tuple[np.ndarray, np.ndarray]:
    if indices is None:
        xyz = np.sum(spd[:, None] * cmf, axis=0) * step_nm
    else:
        xyz = np.sum(spd[indices, None] * cmf[indices], axis=0) * step_nm
    xy = xyz[:2] / np.sum(xyz)
    return xyz, xy


def evaluate_spectrum(spd: np.ndarray, cmf: np.ndarray) -> dict:
    xyz_1, xy_1 = integrate(spd, cmf)
    offsets = []
    for offset in range(5):
        idx = np.arange(offset, len(spd), 5)
        xyz_5, xy_5 = integrate(spd, cmf, idx, 5.0)
        offsets.append(
            {
                "offset_nm": offset,
                "delta_xy": float(np.linalg.norm(xy_5 - xy_1)),
                "relative_Y_error": float((xyz_5[1] - xyz_1[1]) / xyz_1[1]),
            }
        )
    return {
        "xyz_1nm": xyz_1.tolist(),
        "xy_1nm": xy_1.tolist(),
        "max_delta_xy_across_5nm_phase_offsets": max(x["delta_xy"] for x in offsets),
        "max_abs_relative_Y_error_across_5nm_phase_offsets": max(
            abs(x["relative_Y_error"]) for x in offsets
        ),
        "offset_diagnostics": offsets,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("cie1931", type=Path, help="current CIE_xyz_1931_2deg.csv")
    parser.add_argument("--cie1964", type=Path, default=None, help="optional checksum audit")
    parser.add_argument("--cie2006-lms", type=Path, default=None, help="optional checksum audit")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    wl, cmf, provenance = load_cie1931(args.cie1931)

    spectra = {
        "broad_warm": gaussian(wl, 610.0, 45.0) + 0.25 * gaussian(wl, 470.0, 30.0),
        "broad_cool": gaussian(wl, 460.0, 28.0) + 0.55 * gaussian(wl, 540.0, 55.0),
        "narrow_display_like": (
            gaussian(wl, 452.3, 8.0)
            + 0.85 * gaussian(wl, 531.7, 10.0)
            + 0.75 * gaussian(wl, 608.4, 8.0)
        ),
        "ultra_narrow_laser_like": (
            gaussian(wl, 452.3, 2.5)
            + 0.85 * gaussian(wl, 531.7, 3.0)
            + 0.75 * gaussian(wl, 608.4, 2.5)
        ),
    }

    result = {
        "study": "C012",
        "cie_1931": {
            "doi": "10.25039/CIE.DS.xvudnb9b",
            "expected_md5": EXPECTED_1931_MD5,
            **provenance,
        },
        "optional_provenance_audits": {
            "cie_1964_10deg": checksum_audit(args.cie1964, EXPECTED_1964_MD5),
            "cie_2006_lms_2deg": checksum_audit(
                args.cie2006_lms, EXPECTED_2006_LMS_2DEG_MD5
            ),
        },
        "integration": {
            "observer": "CIE 1931 2 degree",
            "range_nm": [360, 830],
            "integration_step_nm": 1,
            "five_nm_test": (
                "subsample the same 1 nm SPD/CMF grid every 5 nm at phase offsets 0..4, "
                "multiply sum by 5; diagnostic only, not an instrument-bandwidth model"
            ),
            "spectra": {k: evaluate_spectrum(v, cmf) for k, v in spectra.items()},
        },
    }

    payload = json.dumps(result, indent=2)
    if args.out:
        args.out.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
