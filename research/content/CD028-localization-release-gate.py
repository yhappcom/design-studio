#!/usr/bin/env python3
import copy
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
MANIFEST = HERE / "CD028-localization-release-manifest.json"


def lint(manifest):
    errors = []
    policy = manifest["policy"]
    source_rev = manifest["source_semantic_revision"]

    for m in manifest["messages"]:
        mid = m["message_id"]
        tier = m["risk_tier"]

        if m["semantic_revision"] != source_rev:
            errors.append(("STALE_SEMANTIC_REVISION", mid, m["semantic_revision"], source_rev))

        if not m["locale_present"]:
            fallback = m.get("fallback")
            allowed = policy["approved_fallbacks"].get(f"tier_{tier}", [])
            if fallback not in allowed:
                errors.append(("CRITICAL_OR_UNAPPROVED_FALLBACK", mid, tier, fallback))

        if tier in policy["require_linguistic_review_for"] and m["linguistic_review"] != "passed":
            errors.append(("LINGUISTIC_REVIEW_INCOMPLETE", mid, tier))
        if tier in policy["require_structural_validation_for"] and m["structural_validation"] != "passed":
            errors.append(("STRUCTURAL_VALIDATION_INCOMPLETE", mid, tier))
        if tier in policy["require_render_qa_for"] and m["render_qa"] != "passed":
            errors.append(("RENDER_QA_INCOMPLETE", mid, tier))
        if tier in policy["require_functional_qa_for"] and m["functional_qa"] != "passed":
            errors.append(("FUNCTIONAL_QA_INCOMPLETE", mid, tier))

        plural = m.get("plural_select")
        if plural:
            missing = set(plural["required_categories"]) - set(plural["provided_categories"])
            if missing:
                errors.append(("PLURAL_SELECT_COVERAGE_INCOMPLETE", mid, tuple(sorted(missing))))

    rollback = manifest.get("rollback", {})
    required_rollback = ("content_revision", "semantic_revision", "resource_bundle", "owner")
    missing_rollback = [k for k in required_rollback if not rollback.get(k)]
    if missing_rollback:
        errors.append(("ROLLBACK_METADATA_INCOMPLETE", tuple(missing_rollback)))

    for owner in ("content", "localization", "qa", "release"):
        if manifest.get("approvals", {}).get(owner) != "approved":
            errors.append(("RELEASE_APPROVAL_INCOMPLETE", owner))

    return errors


def mutation_suite(base):
    cases = []

    x = copy.deepcopy(base)
    x["messages"][1]["semantic_revision"] = "2026.09.15.1"
    cases.append(("stale_semantic_revision", "STALE_SEMANTIC_REVISION", x))

    x = copy.deepcopy(base)
    x["messages"][1]["locale_present"] = False
    x["messages"][1]["fallback"] = "source_en"
    cases.append(("critical_unapproved_fallback", "CRITICAL_OR_UNAPPROVED_FALLBACK", x))

    x = copy.deepcopy(base)
    x["messages"][2]["plural_select"]["provided_categories"] = ["other"]
    cases.append(("plural_category_missing", "PLURAL_SELECT_COVERAGE_INCOMPLETE", x))

    x = copy.deepcopy(base)
    x["messages"][1]["render_qa"] = "pending"
    cases.append(("critical_render_qa_pending", "RENDER_QA_INCOMPLETE", x))

    x = copy.deepcopy(base)
    x["messages"][1]["functional_qa"] = "pending"
    cases.append(("critical_functional_qa_pending", "FUNCTIONAL_QA_INCOMPLETE", x))

    x = copy.deepcopy(base)
    x["messages"][0]["linguistic_review"] = "pending"
    cases.append(("linguistic_review_pending", "LINGUISTIC_REVIEW_INCOMPLETE", x))

    x = copy.deepcopy(base)
    x["rollback"]["semantic_revision"] = ""
    cases.append(("rollback_semantic_revision_missing", "ROLLBACK_METADATA_INCOMPLETE", x))

    x = copy.deepcopy(base)
    x["approvals"]["qa"] = "pending"
    cases.append(("qa_approval_missing", "RELEASE_APPROVAL_INCOMPLETE", x))

    return cases


def main():
    base = json.loads(MANIFEST.read_text(encoding="utf-8"))
    baseline = lint(base)
    print("baseline:", "PASS" if not baseline else "FAIL", baseline)
    failed = bool(baseline)

    for name, expected, mutant in mutation_suite(base):
        found = lint(mutant)
        codes = {e[0] for e in found}
        ok = expected in codes
        print(f"mutation {name}: {'PASS' if ok else 'FAIL'} expected={expected} found={found}")
        failed = failed or not ok

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
