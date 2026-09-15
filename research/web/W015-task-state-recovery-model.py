"""W015 deterministic task-state/recovery model.

This is a Web design contract oracle, not browser/network/AT proof.
It tests W006/I002 distinctions without fabricating runtime evidence.
"""
from dataclasses import dataclass
import json

@dataclass
class Surface:
    data: tuple = ("A", "B")
    query: str = ""
    result: tuple = ("A", "B")
    field: str = "10"
    validation: str = "valid"
    operation: str = "idle"
    message: str = ""
    retry_safe: bool = False
    freshness: str = "fresh"


def search(s, query):
    s.query = query
    s.result = tuple(x for x in s.data if query.lower() in x.lower())


def edit(s, value):
    s.field = value
    s.validation = "valid" if value.isdigit() and int(value) > 0 else "invalid"


def submit(s):
    if s.validation != "valid":
        s.message = "fix-validation"
        return
    s.operation = "pending"
    s.message = "saving"
    s.retry_safe = False


def resolve(s, outcome):
    if outcome == "confirmed":
        s.operation, s.message, s.retry_safe = "confirmed", "saved", False
    elif outcome == "known-fail":
        s.operation, s.message, s.retry_safe = "failed", "not-saved", True
    elif outcome == "unknown":
        s.operation, s.message, s.retry_safe = "outcome-unknown", "verify-before-retry", False
    else:
        raise ValueError(outcome)


def refresh(s, outcome):
    if outcome == "partial":
        s.freshness, s.message = "partial", "some-data-stale"
    elif outcome == "offline":
        s.freshness, s.message = "stale-offline", "offline-cached"
    else:
        raise ValueError(outcome)


def run():
    checks = []
    def check(name, condition): checks.append({"name": name, "pass": bool(condition)})

    s = Surface()
    check("initial data usable", s.result == ("A", "B"))
    search(s, "Z")
    check("filtered zero distinct", s.result == () and s.query == "Z")
    check("zero retains criteria", s.query == "Z")
    edit(s, "x"); submit(s)
    check("invalid blocks submit", s.operation == "idle" and s.message == "fix-validation")
    check("invalid preserves input", s.field == "x")
    edit(s, "12"); submit(s)
    check("valid enters pending", s.operation == "pending")
    check("pending no retry", not s.retry_safe)
    resolve(s, "confirmed")
    check("confirmed explicit", s.operation == "confirmed" and s.message == "saved")

    s = Surface(); edit(s, "12"); submit(s); resolve(s, "known-fail")
    check("known failure explicit", s.operation == "failed" and s.message == "not-saved")
    check("known failure retry safe", s.retry_safe)

    s = Surface(); edit(s, "12"); submit(s); resolve(s, "unknown")
    check("unknown not failed", s.operation == "outcome-unknown")
    check("unknown blocks blind retry", not s.retry_safe)
    check("unknown directs verify", s.message == "verify-before-retry")

    s = Surface(); before = s.data; refresh(s, "partial")
    check("partial preserves prior data", s.data == before)
    check("partial marks incompleteness", s.freshness == "partial")

    s = Surface(); before = s.data; refresh(s, "offline")
    check("offline preserves cached data", s.data == before)
    check("offline provenance visible", s.freshness == "stale-offline")

    return {"study":"W015", "evidence":"DETERMINISTIC MODEL VALIDATION", "browser_proof":False,
            "passed":sum(c["pass"] for c in checks), "total":len(checks), "checks":checks}

if __name__ == "__main__":
    print(json.dumps(run(), indent=2))
