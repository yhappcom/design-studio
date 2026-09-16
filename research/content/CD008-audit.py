#!/usr/bin/env python3
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
CONTRACT = ROOT / "CD008-message-contract.json"

weights = {
    "semantic_fidelity": 5,
    "concept_consistency": 4,
    "action_consequence_clarity": 5,
    "minimum_sufficient_information": 4,
    "accessibility_input_neutrality": 4,
    "localization_readiness": 4,
    "expert_domain_precision": 3,
    "cross_domain_fit": 3,
}

candidate_scores = {
    "A_minimal_command": {
        "semantic_fidelity": 2,
        "concept_consistency": 2,
        "action_consequence_clarity": 1,
        "minimum_sufficient_information": 2,
        "accessibility_input_neutrality": 3,
        "localization_readiness": 1,
        "expert_domain_precision": 2,
        "cross_domain_fit": 3,
    },
    "B_explanation_heavy": {
        "semantic_fidelity": 5,
        "concept_consistency": 4,
        "action_consequence_clarity": 4,
        "minimum_sufficient_information": 2,
        "accessibility_input_neutrality": 4,
        "localization_readiness": 3,
        "expert_domain_precision": 4,
        "cross_domain_fit": 3,
    },
    "C_state_decision_architecture": {
        "semantic_fidelity": 5,
        "concept_consistency": 5,
        "action_consequence_clarity": 5,
        "minimum_sufficient_information": 5,
        "accessibility_input_neutrality": 5,
        "localization_readiness": 5,
        "expert_domain_precision": 4,
        "cross_domain_fit": 4,
    },
}

forbidden = {
    "PSEUDO_PLURAL": re.compile(r"\(s\)", re.I),
    "COLOR_LOCK": re.compile(r"\b(red|blue|green|yellow)\b", re.I),
    "POSITION_LOCK": re.compile(r"\b(left|right|above|below)\b", re.I),
    "INPUT_METHOD_LOCK": re.compile(r"\b(click|tap)\b", re.I),
}

def audit_entry(entry):
    findings = []
    required = [
        "id", "role", "concept", "state", "text", "scope",
        "consequence", "localizer_context", "variables"
    ]
    for field in required:
        if field not in entry:
            findings.append(f"MISSING_FIELD:{field}")

    text = entry.get("text", "")
    for label, pattern in forbidden.items():
        if pattern.search(text):
            findings.append(label)

    if entry.get("role") == "action":
        if entry.get("accessible_name") != text:
            findings.append("ACCESSIBLE_NAME_DRIFT")

    if entry.get("state") == "outcome_unknown":
        if re.search(r"\bretry\b|\btry again\b", text, re.I):
            findings.append("UNSAFE_RETRY_LANGUAGE")

    variables_in_text = set(re.findall(r"\{(\w+)\}", text))
    defined_variables = set(entry.get("variables", {}).keys())
    if variables_in_text != defined_variables:
        findings.append("VARIABLE_CONTEXT_MISMATCH")

    return findings

def weighted_total(scores):
    return sum(weights[key] * scores[key] for key in weights)

def main():
    data = json.loads(CONTRACT.read_text(encoding="utf-8"))
    findings = []
    seen = set()

    for entry in data["entries"]:
        if entry["id"] in seen:
            findings.append({"id": entry["id"], "finding": "DUPLICATE_ID"})
        seen.add(entry["id"])
        for finding in audit_entry(entry):
            findings.append({"id": entry.get("id", "<unknown>"), "finding": finding})

    totals = {name: weighted_total(scores) for name, scores in candidate_scores.items()}
    maximum = sum(weights.values()) * 5

    output = {
        "study": "CD008",
        "structural_findings": findings,
        "structural_finding_count": len(findings),
        "candidate_weighted_totals": totals,
        "maximum_weighted_total": maximum,
        "selected_by_structured_studio_criteria": max(totals, key=totals.get),
        "evidence_boundary": (
            "Deterministic structural lint and arithmetic consistency only. "
            "Does not measure comprehension, findability, trust, task time, error rate, "
            "screen-reader quality, localization quality, or user preference."
        ),
    }
    print(json.dumps(output, ensure_ascii=False, indent=2))
    if findings:
        raise SystemExit(1)

if __name__ == "__main__":
    main()
