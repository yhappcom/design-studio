"""T021 R4B shared-family construction grammar invariant model.

This is a pre-drawing constraint harness. It does not claim optical quality.
Kerning is intentionally out of scope.
"""
import json

G = {
    "units_per_em": 1000,
    "cap_height": 700,
    "x_height": 500,
    "overshoot_cap": 12,
    "overshoot_lower": 10,
    "stem": 82,
    "oval_cap": {
        "advance": 560, "outer_left": 45, "outer_right": 515,
        "outer_top": 712, "outer_bottom": -12,
        "counter_left": 135, "counter_right": 425,
        "counter_top": 622, "counter_bottom": 78,
    },
    "oval_lower": {
        "advance": 500, "outer_left": 45, "outer_right": 455,
        "outer_top": 510, "outer_bottom": -10,
        "counter_left": 125, "counter_right": 375,
        "counter_top": 430, "counter_bottom": 70,
    },
    "bowl_policy": {
        "glyphs": ["D", "B", "P", "R", "8"],
        "join_inset": 18, "counter_min": 150, "waist_y": 350,
    },
    "aperture_terminal_policy": {
        "glyphs": ["C", "G", "S", "5"],
        "minimum_opening": 105, "terminal_cut_degrees": 8,
    },
    "shoulder_policy": {
        "glyphs": ["n"], "rise": 380, "peak": 510, "join_x": 180,
    },
    "figure_policy": {
        "glyphs": ["0", "1", "5", "8"], "advance": 560,
        "zero_slash": True, "one_base": True, "five_top_open": True,
        "eight_counter_ratio": 0.92,
    },
}

oc, ol = G["oval_cap"], G["oval_lower"]
checks = {
    "cap_overshoot_symmetric": (oc["outer_top"] - G["cap_height"]) == -oc["outer_bottom"] == G["overshoot_cap"],
    "lower_overshoot_symmetric": (ol["outer_top"] - G["x_height"]) == -ol["outer_bottom"] == G["overshoot_lower"],
    "cap_counter_side_symmetry": (oc["counter_left"] - oc["outer_left"]) == (oc["outer_right"] - oc["counter_right"]),
    "lower_counter_side_symmetry": (ol["counter_left"] - ol["outer_left"]) == (ol["outer_right"] - ol["counter_right"]),
    "cap_counter_vertical_balance": (oc["outer_top"] - oc["counter_top"]) == (oc["counter_bottom"] - oc["outer_bottom"]),
    "lower_counter_vertical_balance": (ol["outer_top"] - ol["counter_top"]) == (ol["counter_bottom"] - ol["outer_bottom"]),
    "bowl_group_shared_policy": G["bowl_policy"]["glyphs"] == ["D", "B", "P", "R", "8"],
    "aperture_group_shared_policy": G["aperture_terminal_policy"]["glyphs"] == ["C", "G", "S", "5"],
    "figures_coordinated_advance": G["figure_policy"]["advance"] == oc["advance"],
    "ambiguity_constraints_explicit": all([G["figure_policy"]["zero_slash"], G["figure_policy"]["one_base"], G["figure_policy"]["five_top_open"]]),
}
metrics = {
    "cap_outer_width_height_ratio": round((oc["outer_right"]-oc["outer_left"])/(oc["outer_top"]-oc["outer_bottom"]), 3),
    "lower_outer_width_height_ratio": round((ol["outer_right"]-ol["outer_left"])/(ol["outer_top"]-ol["outer_bottom"]), 3),
    "cap_counter_clearance": {"left": oc["counter_left"]-oc["outer_left"], "right": oc["outer_right"]-oc["counter_right"], "top": oc["outer_top"]-oc["counter_top"], "bottom": oc["counter_bottom"]-oc["outer_bottom"]},
    "lower_counter_clearance": {"left": ol["counter_left"]-ol["outer_left"], "right": ol["outer_right"]-ol["counter_right"], "top": ol["outer_top"]-ol["counter_top"], "bottom": ol["counter_bottom"]-ol["outer_bottom"]},
}
result = {"study":"T021 R4B pre-drawing grammar", "status":"CONSTRAINT MODEL ONLY", "kerning":"OFF / NOT MODELED", "grammar":G, "checks":checks, "metrics":metrics, "passed":sum(bool(v) for v in checks.values()), "total":len(checks)}
print(json.dumps(result, indent=2))
