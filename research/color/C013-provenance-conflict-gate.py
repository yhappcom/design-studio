"""C013 artifact-first provenance gate for Color datasets.

The gate separates:
- authority-surface consistency (HTML page vs linked metadata);
- raw artifact identity (locally computed hash, when available);
- transformed derivatives.

It does not decide which conflicting first-party checksum is 'correct'.
That requires the exact raw file bytes and, where needed, clarification from the
publishing authority.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any


def digest_file(path: Path) -> dict[str, str]:
    data = path.read_bytes()
    return {
        "md5": hashlib.md5(data).hexdigest(),
        "sha256": hashlib.sha256(data).hexdigest(),
    }


def classify(
    page_md5: str | None,
    metadata_md5: str | None,
    raw_md5: str | None = None,
    transformed: bool = False,
) -> str:
    if transformed:
        return "TRANSFORMED_DERIVATIVE"

    surfaces_known = page_md5 is not None and metadata_md5 is not None
    surfaces_equal = surfaces_known and page_md5 == metadata_md5

    if raw_md5 is None:
        if surfaces_equal:
            return "SURFACE_CONSISTENT_RAW_UNVERIFIED"
        if surfaces_known and not surfaces_equal:
            return "AUTHORITY_CONFLICT_RAW_UNAVAILABLE"
        return "INSUFFICIENT_PROVENANCE"

    page_match = page_md5 == raw_md5 if page_md5 is not None else False
    metadata_match = metadata_md5 == raw_md5 if metadata_md5 is not None else False

    if surfaces_equal and page_match and metadata_match:
        return "RAW_VERIFIED"

    if not surfaces_equal and (page_match ^ metadata_match):
        return "RAW_MATCHES_ONE_AUTHORITY_SURFACE"

    if page_match and metadata_match:
        # Defensive branch for incomplete surface inputs.
        return "RAW_VERIFIED"

    return "RAW_DIVERGENT"


def evaluate_dataset(entry: dict[str, Any], base_dir: Path) -> dict[str, Any]:
    raw_path = entry.get("raw_path")
    raw_hashes = None
    if raw_path:
        raw_hashes = digest_file((base_dir / raw_path).resolve())

    state = classify(
        entry.get("page_md5"),
        entry.get("metadata_md5"),
        raw_hashes["md5"] if raw_hashes else None,
        bool(entry.get("transformed", False)),
    )

    result = {
        "dataset": entry["dataset"],
        "doi": entry.get("doi"),
        "page_url": entry.get("page_url"),
        "metadata_url": entry.get("metadata_url"),
        "page_md5": entry.get("page_md5"),
        "metadata_md5": entry.get("metadata_md5"),
        "raw_hashes": raw_hashes,
        "transformed": bool(entry.get("transformed", False)),
        "state": state,
    }

    if state == "SURFACE_CONSISTENT_RAW_UNVERIFIED":
        result["interpretation"] = (
            "First-party checksum surfaces agree, but exact raw-file bytes were not "
            "independently hashed in this run."
        )
    elif state == "AUTHORITY_CONFLICT_RAW_UNAVAILABLE":
        result["interpretation"] = (
            "First-party checksum surfaces disagree and raw bytes are unavailable; "
            "do not choose a winner by convenience."
        )
    elif state == "RAW_VERIFIED":
        result["interpretation"] = (
            "Page, metadata and locally hashed raw artifact identify the same bytes."
        )
    elif state == "RAW_MATCHES_ONE_AUTHORITY_SURFACE":
        result["interpretation"] = (
            "The raw artifact is reproducible but matches only one conflicting authority "
            "surface; qualify the artifact explicitly until the source conflict is resolved."
        )
    elif state == "TRANSFORMED_DERIVATIVE":
        result["interpretation"] = (
            "The working data are a transformed derivative; preserve source and derivative "
            "identities separately."
        )
    else:
        result["interpretation"] = (
            "Raw artifact identity does not align with the available authority evidence."
        )

    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("ledger", type=Path, help="JSON evidence ledger")
    parser.add_argument("--out", type=Path, default=None)
    args = parser.parse_args()

    ledger = json.loads(args.ledger.read_text(encoding="utf-8"))
    base_dir = args.ledger.parent
    results = [evaluate_dataset(e, base_dir) for e in ledger["datasets"]]

    payload = {
        "study": "C013",
        "method": "artifact-first provenance gate",
        "results": results,
        "counts": {
            state: sum(1 for r in results if r["state"] == state)
            for state in sorted({r["state"] for r in results})
        },
        "boundary": (
            "Checksum agreement validates artifact identity only. It does not validate "
            "observer/model appropriateness, numerical interpretation, perceptual validity, "
            "instrument quality, device reproduction, or project relevance."
        ),
    }

    text = json.dumps(payload, indent=2)
    if args.out:
        args.out.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)


if __name__ == "__main__":
    main()
