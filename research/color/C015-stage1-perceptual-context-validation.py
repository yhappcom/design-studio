"""C015 Stage 1 perceptual-context capstone validation.

This script validates encoded color identity and bounded relative-luminance
calculations used by the capstone. It does not measure human perception,
physical glare, display luminance, or low-light comfort.
"""

from __future__ import annotations
import json
import argparse
from pathlib import Path


def rgb_tuple(h: str) -> tuple[int, int, int]:
    h = h.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def _lin(v: int) -> float:
    c = v / 255.0
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def rel_lum(h: str) -> float:
    r, g, b = rgb_tuple(h)
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def contrast(a: str, b: str) -> float:
    x, y = rel_lum(a), rel_lum(b)
    hi, lo = max(x, y), min(x, y)
    return (hi + 0.05) / (lo + 0.05)


def veiled_contrast(a: str, b: str, veil_fraction: float = 0.15) -> float:
    # Deliberately simple sensitivity diagnostic: blend relative luminance
    # toward white. This is not an optical glare or display model.
    x = (1 - veil_fraction) * rel_lum(a) + veil_fraction
    y = (1 - veil_fraction) * rel_lum(b) + veil_fraction
    hi, lo = max(x, y), min(x, y)
    return (hi + 0.05) / (lo + 0.05)


def build() -> dict:
    pastels = ["#A8F0E9", "#B8D8FF", "#FFD6A5", "#FFADAD"]
    result = {
        "study": "C015",
        "simultaneous_contrast": {
            "target_hex": "#808080",
            "target_left_rgb": rgb_tuple("#808080"),
            "target_right_rgb": rgb_tuple("#808080"),
            "identical_encoded_target": True,
            "target_relative_luminance": rel_lum("#808080"),
            "surrounds": ["#202020", "#E8E8E8"],
            "note": "Pixel identity proves stimulus identity; contextual appearance remains a perceptual/source claim until observed by people.",
        },
        "grayscale_first": {
            "pairs": {
                "primary_text_canvas": contrast("#1E1E1E", "#F5F5F3"),
                "secondary_text_canvas": contrast("#666666", "#F5F5F3"),
                "tertiary_text_canvas": contrast("#8A8A8A", "#F5F5F3"),
                "primary_action_white_text": contrast("#FFFFFF", "#2A2A2A"),
                "revised_blue_action_white_text": contrast("#FFFFFF", "#155EEF"),
                "brand_mint_dark_content": contrast("#152028", "#A8F0E9"),
            },
            "ordering_note": "Add chroma to action/selection only after grayscale hierarchy is established.",
        },
        "low_light_design_stress": {
            "pairs": {
                "primary_text_canvas": contrast("#E8EEF2", "#0D1317"),
                "secondary_text_canvas": contrast("#AAB6BE", "#0D1317"),
                "primary_text_surface": contrast("#E8EEF2", "#151C21"),
                "secondary_text_surface": contrast("#AAB6BE", "#151C21"),
                "dark_text_light_blue_action": contrast("#0D1317", "#5FB5FF"),
                "light_text_blue_action": contrast("#E8EEF2", "#2B6CB0"),
                "boundary_surface": contrast("#667680", "#151C21"),
            },
            "note": "Design-stress variant only; no physical low-light comfort claim.",
        },
        "high_glare_math_stress": {
            "veil_fraction": 0.15,
            "pairs": {
                "primary_text_canvas": {
                    "baseline": contrast("#1E1E1E", "#F5F5F3"),
                    "veiled": veiled_contrast("#1E1E1E", "#F5F5F3"),
                },
                "secondary_text_canvas": {
                    "baseline": contrast("#666666", "#F5F5F3"),
                    "veiled": veiled_contrast("#666666", "#F5F5F3"),
                },
                "boundary_white": {
                    "baseline": contrast("#B8B8B8", "#FFFFFF"),
                    "veiled": veiled_contrast("#B8B8B8", "#FFFFFF"),
                },
                "white_text_blue_action": {
                    "baseline": contrast("#FFFFFF", "#155EEF"),
                    "veiled": veiled_contrast("#FFFFFF", "#155EEF"),
                },
            },
            "note": "White-veiling sensitivity diagnostic only; not a physical glare model or WCAG re-test.",
        },
        "attractive_swatches_context_failure": {
            "swatches": pastels,
            "white_text_contrast": {c: contrast(c, "#FFFFFF") for c in pastels},
            "dark_text_contrast": {c: contrast(c, "#152028") for c in pastels},
            "note": "Attractive light swatches can fail when assigned to filled controls with white content.",
        },
    }
    return result


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--out", type=Path)
    args = p.parse_args()
    payload = json.dumps(build(), indent=2)
    if args.out:
        args.out.write_text(payload + "\n", encoding="utf-8")
    else:
        print(payload)


if __name__ == "__main__":
    main()
