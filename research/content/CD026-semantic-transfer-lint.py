#!/usr/bin/env python3
import copy
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
INVENTORY = HERE / "CD026-versioned-semantic-transfer-inventory.json"

SEMANTIC_FIELDS = ("concept_id", "state_id", "action_id", "certainty")


def variable_signature(message):
    return {v["name"]: v["type"] for v in message["variables"]}


def lint(inv):
    errors = []
    regs = inv["registries"]

    for m in inv["messages"]:
        mid = m["message_id"]
        if m["concept_id"] not in regs["concepts"]:
            errors.append(("UNKNOWN_CONCEPT", mid))
        if m["state_id"] not in regs["states"]:
            errors.append(("UNKNOWN_STATE", mid))
        if m["action_id"] is not None and m["action_id"] not in regs["actions"]:
            errors.append(("UNKNOWN_ACTION", mid))
        if m["certainty"] not in regs["certainties"]:
            errors.append(("UNKNOWN_CERTAINTY", mid))

        for v in m["variables"]:
            if v["type"] not in regs["variable_types"]:
                errors.append(("UNKNOWN_VARIABLE_TYPE", mid, v["name"], v["type"]))
            if v["type"] == "operational_literal" and v["localize"]:
                errors.append(("LITERAL_LOCALIZED", mid, v["name"]))
            if v["type"] in ("count", "datetime", "duration") and not v["localize"]:
                errors.append(("LOCALIZABLE_TYPE_MARKED_LITERAL", mid, v["name"], v["type"]))

        previous = inv.get("previous_contracts", {}).get(mid)
        if previous:
            changed = [field for field in SEMANTIC_FIELDS if previous.get(field) != m.get(field)]
            if set(previous.get("required_semantics", [])) != set(m.get("required_semantics", [])):
                changed.append("required_semantics")
            if previous.get("variable_signature", {}) != variable_signature(m):
                changed.append("variable_signature")
            if changed:
                errors.append(("INCOMPATIBLE_MESSAGE_ID_REUSE", mid, tuple(changed)))

        for channel, cfg in m["channels"].items():
            if not cfg.get("eligible"):
                continue
            projected = cfg.get("certainty", m["certainty"])
            if projected != m["certainty"]:
                errors.append(("CHANNEL_CERTAINTY_MISMATCH", mid, channel, m["certainty"], projected))
            if channel in ("notification", "email") and m["action_id"]:
                if not (cfg.get("freshness") and cfg.get("revalidate")):
                    errors.append(("EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING", mid, channel))

        for locale_name, catalog in inv["fixtures"].items():
            fixture = catalog.get(m["locale_key"])
            if fixture is None:
                errors.append(("MISSING_LOCALE_KEY", mid, locale_name))
                continue
            missing_semantics = set(m["required_semantics"]) - set(fixture.get("semantics", []))
            if missing_semantics:
                errors.append(("FALLBACK_SEMANTIC_LOSS", mid, locale_name, tuple(sorted(missing_semantics))))
            text = fixture["text"]
            for v in m["variables"]:
                placeholder = "{" + v["name"] + "}"
                if placeholder not in text:
                    errors.append(("MISSING_VARIABLE", mid, locale_name, v["name"]))
    return errors


def mutation_suite(base):
    cases = []

    x = copy.deepcopy(base)
    x["messages"][0]["certainty"] = "unknown"
    cases.append(("incompatible_id_reuse", "INCOMPATIBLE_MESSAGE_ID_REUSE", x))

    x = copy.deepcopy(base)
    x["messages"][1]["channels"]["notification"]["certainty"] = "failed"
    cases.append(("channel_certainty_strengthened", "CHANNEL_CERTAINTY_MISMATCH", x))

    x = copy.deepcopy(base)
    x["fixtures"]["fallback"]["record.save.outcome_unknown"]["semantics"] = ["object"]
    cases.append(("fallback_semantic_loss", "FALLBACK_SEMANTIC_LOSS", x))

    x = copy.deepcopy(base)
    x["messages"][2]["variables"][0]["localize"] = False
    cases.append(("count_not_localized", "LOCALIZABLE_TYPE_MARKED_LITERAL", x))

    x = copy.deepcopy(base)
    x["messages"][2]["variables"][1]["type"] = "timestampish"
    cases.append(("unknown_typed_variable", "UNKNOWN_VARIABLE_TYPE", x))

    x = copy.deepcopy(base)
    x["fixtures"]["fallback"]["record.offline.summary"]["text"] = "Showing {record_count} saved records from {updated_at}. Current data isn’t available."
    cases.append(("duration_variable_dropped", "MISSING_VARIABLE", x))

    x = copy.deepcopy(base)
    del x["messages"][1]["channels"]["notification"]["revalidate"]
    cases.append(("external_revalidation_dropped", "EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING", x))

    return cases


def main():
    base = json.loads(INVENTORY.read_text(encoding="utf-8"))
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
