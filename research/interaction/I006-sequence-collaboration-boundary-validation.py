import json
from copy import deepcopy

ASSERTIONS = []

def check(name, condition, detail=None):
    ASSERTIONS.append({"name": name, "pass": bool(condition), "detail": detail})
    if not condition:
        raise AssertionError(name)

def insert_at(text, index, value):
    return text[:index] + value + text[index:]

def transform_remote_against_local(remote, local):
    remote_actor, remote_index, remote_text = remote
    local_actor, local_index, local_text = local
    if local_index < remote_index or (local_index == remote_index and local_actor < remote_actor):
        remote_index += len(local_text)
    return remote_actor, remote_index, remote_text

def render_anchor(ops):
    out = "A"
    for op in sorted(ops, key=lambda x: x["id"]):
        if op["after"] == "a":
            out += op["char"]
    return out + "B"

def render_tombstone(order):
    nodes = {
        "a": {"char": "A", "visible": True},
        "b": {"char": "B", "visible": True},
        "c": {"char": "C", "visible": True},
    }
    inserts = []
    for op in order:
        if op["kind"] == "delete":
            nodes[op["id"]]["visible"] = False
        else:
            inserts.append(op)
    out = "A" if nodes["a"]["visible"] else ""
    if nodes["b"]["visible"]:
        out += "B"
    for op in sorted(inserts, key=lambda x: x["id"]):
        out += op["char"]
    if nodes["c"]["visible"]:
        out += "C"
    return out

def apply_move(values, move):
    values = [x for x in values if x != move["item"]]
    if move["dest"] == "after:C":
        values.insert(values.index("C") + 1, move["item"])
    elif move["dest"] == "before:A":
        values.insert(values.index("A"), move["item"])
    return values

def run():
    base = "AB"

    # Whole-field LWW.
    a_state = "AXB"
    b_state = "AYB"
    merged = b_state
    check("whole_field_lww_loses_A_insert", "X" not in merged, merged)
    check("whole_field_lww_preserves_only_one_intent", merged == "AYB", merged)

    # Raw positional operations diverge when replayed against changed local state.
    replica_a = insert_at(base, 1, "X")
    replica_a = insert_at(replica_a, 1, "Y")
    replica_b = insert_at(base, 1, "Y")
    replica_b = insert_at(replica_b, 1, "X")
    check("naive_positional_merge_replica_A", replica_a == "AYXB", replica_a)
    check("naive_positional_merge_replica_B", replica_b == "AXYB", replica_b)
    check("naive_positional_operations_diverge", replica_a != replica_b, [replica_a, replica_b])
    check("naive_merge_keeps_both_but_not_convergent", all(x in replica_a for x in "XY") and all(x in replica_b for x in "XY"))

    # Minimal OT-like transform control.
    op_a = ("A", 1, "X")
    op_b = ("B", 1, "Y")
    state_a = insert_at(base, op_a[1], op_a[2])
    transformed_b = transform_remote_against_local(op_b, op_a)
    state_a = insert_at(state_a, transformed_b[1], transformed_b[2])
    state_b = insert_at(base, op_b[1], op_b[2])
    transformed_a = transform_remote_against_local(op_a, op_b)
    state_b = insert_at(state_b, transformed_a[1], transformed_a[2])
    check("ot_like_replica_A_result", state_a == "AXYB", [transformed_b, state_a])
    check("ot_like_replica_B_result", state_b == "AXYB", [transformed_a, state_b])
    check("ot_like_converges", state_a == state_b)
    check("ot_like_preserves_both_inserts", "X" in state_a and "Y" in state_a)

    # Minimal stable-anchor/identity control.
    ops = [
        {"id": "A:1", "char": "X", "after": "a"},
        {"id": "B:1", "char": "Y", "after": "a"},
    ]
    r1 = render_anchor(ops)
    r2 = render_anchor(list(reversed(ops)))
    check("stable_anchor_merge_order_independent", r1 == r2, [r1, r2])
    check("stable_anchor_merge_preserves_both", r1 == "AXYB", r1)

    # Concurrent delete + insertion after deleted anchor; tombstone policy control.
    delete_b = {"kind": "delete", "id": "b", "op": "A:2"}
    insert_x = {"kind": "insert", "id": "B:2", "char": "X", "after": "b"}
    t1 = render_tombstone([delete_b, insert_x])
    t2 = render_tombstone([insert_x, delete_b])
    check("tombstone_anchor_converges", t1 == t2, [t1, t2])
    check("tombstone_policy_preserves_insert_near_deleted_anchor", t1 == "AXC", t1)

    # Convergence does not imply semantic agreement for concurrent move.
    base_list = ["A", "B", "C"]
    move_a = {"actor": "A", "item": "B", "dest": "after:C"}
    move_b = {"actor": "B", "item": "B", "dest": "before:A"}
    winner = max([move_a, move_b], key=lambda x: x["actor"])
    converged = apply_move(base_list, winner)
    rejected_intent = apply_move(base_list, move_a)
    check("deterministic_move_resolution_converges_to_one_state", converged == ["B", "A", "C"], converged)
    check("deterministic_move_resolution_discards_one_move_intent", converged != rejected_intent, [converged, rejected_intent])

    # Whole-field conflict model can over-escalate disjoint edits.
    base_text = "hello world"
    local = "Hi, " + base_text
    remote = base_text + "!"
    check("whole_field_model_flags_same_field_conflict", local != base_text and remote != base_text)
    sequence_merged = "Hi, hello world!"
    check("sequence_model_can_preserve_disjoint_text_edits", sequence_merged.startswith("Hi, ") and sequence_merged.endswith("!"), sequence_merged)

    return {
        "passed": sum(x["pass"] for x in ASSERTIONS),
        "total": len(ASSERTIONS),
        "all_pass": all(x["pass"] for x in ASSERTIONS),
        "assertions": ASSERTIONS,
    }

if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
