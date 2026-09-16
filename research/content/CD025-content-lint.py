#!/usr/bin/env python3
import copy
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
INVENTORY = HERE / "CD025-bounded-content-inventory.json"


def lint(inv):
    errors = []
    regs = inv["registries"]
    seen = set()
    for m in inv["messages"]:
        mid = m["message_id"]
        if mid in seen:
            errors.append(("DUPLICATE_MESSAGE_ID", mid))
        seen.add(mid)
        if m["concept_id"] not in regs["concepts"]:
            errors.append(("UNKNOWN_CONCEPT", mid))
        if m["state_id"] not in regs["states"]:
            errors.append(("UNKNOWN_STATE", mid))
        if m["action_id"] is not None and m["action_id"] not in regs["actions"]:
            errors.append(("UNKNOWN_ACTION", mid))
        if m["state_id"] == "outcome_unknown" and m["action_id"] == "retry_save":
            errors.append(("UNSAFE_BLIND_RETRY", mid))

        for v in m["variables"]:
            if v["type"] == "operational_literal":
                if v["localize"]:
                    errors.append(("LITERAL_LOCALIZED", mid, v["name"]))
                if not v["bidi_isolate"]:
                    errors.append(("BIDI_ISOLATION_METADATA_MISSING", mid, v["name"]))

        for channel, cfg in m["channels"].items():
            if cfg.get("eligible") and channel in ("notification", "email") and m["action_id"]:
                if not (cfg.get("freshness") and cfg.get("revalidate")):
                    errors.append(("EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING", mid, channel))

        for locale, catalog in inv["fixtures"].items():
            text = catalog.get(m["locale_key"])
            if text is None:
                errors.append(("MISSING_LOCALE_KEY", mid, locale))
                continue
            for v in m["variables"]:
                placeholder = "{" + v["name"] + "}"
                if placeholder not in text:
                    errors.append(("MISSING_VARIABLE", mid, locale, v["name"]))
            if locale == "rtl":
                for v in m["variables"]:
                    if v["type"] == "operational_literal":
                        isolated = "\u2066{" + v["name"] + "}\u2069"
                        if isolated not in text:
                            errors.append(("RTL_LITERAL_NOT_ISOLATED", mid, v["name"]))
    return errors


def mutation_suite(base):
    cases = []

    x = copy.deepcopy(base)
    x["messages"][0]["state_id"] = "savingish"
    cases.append(("unknown_state", "UNKNOWN_STATE", x))

    x = copy.deepcopy(base)
    x["fixtures"]["en"]["record.save.confirmed"] = "Record saved."
    cases.append(("missing_variable", "MISSING_VARIABLE", x))

    x = copy.deepcopy(base)
    x["messages"][0]["variables"][0]["localize"] = True
    cases.append(("literal_localized", "LITERAL_LOCALIZED", x))

    x = copy.deepcopy(base)
    x["messages"][2]["action_id"] = "retry_save"
    cases.append(("unsafe_retry", "UNSAFE_BLIND_RETRY", x))

    x = copy.deepcopy(base)
    del x["messages"][2]["channels"]["notification"]["revalidate"]
    cases.append(("missing_revalidation", "EXTERNAL_ACTION_FRESHNESS_POLICY_MISSING", x))

    x = copy.deepcopy(base)
    x["fixtures"]["rtl"]["record.save.confirmed"] = "تم حفظ {flight_number}."
    cases.append(("rtl_unisolated", "RTL_LITERAL_NOT_ISOLATED", x))

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
