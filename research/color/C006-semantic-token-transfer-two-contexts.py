"""C006 reproducible contrast checks for two semantic-color transfer specimens.

This script validates only WCAG-style relative-luminance contrast for declared
foreground/background or essential-boundary pairs. It does not validate
perceptual hierarchy, CVD robustness, browser forced-colors, device rendering,
or product suitability.
"""

from __future__ import annotations

import json


def linearize(c: float) -> float:
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def relative_luminance(hex_color: str) -> float:
    h = hex_color.lstrip("#")
    r, g, b = [int(h[i : i + 2], 16) / 255 for i in (0, 2, 4)]
    rl, gl, bl = map(linearize, (r, g, b))
    return 0.2126 * rl + 0.7152 * gl + 0.0722 * bl


def contrast(a: str, b: str) -> float:
    la, lb = relative_luminance(a), relative_luminance(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


CONTEXTS = {
    "finance_light": {
        "colors": {
            "surface.canvas": "#F7F9FA",
            "surface.raised": "#FFFFFF",
            "content.primary": "#152028",
            "content.secondary": "#52616B",
            "brand.accent": "#7CDDD3",
            "surface.selected": "#E7F8F6",
            "action.primary.surface": "#155EEF",
            "action.primary.content": "#FFFFFF",
            "focus.indicator": "#1D4ED8",
            "boundary.strong": "#7D8C97",
            "status.success": "#167A4B",
            "status.caution": "#9A6700",
            "status.critical": "#B42318",
            "status.info": "#175CD3",
        },
        "contracts": [
            ("content.primary", "surface.canvas", 4.5, "text"),
            ("content.secondary", "surface.canvas", 4.5, "text"),
            ("action.primary.content", "action.primary.surface", 4.5, "text"),
            ("content.primary", "brand.accent", 4.5, "text-on-brand"),
            ("content.primary", "surface.selected", 4.5, "text-selected"),
            ("focus.indicator", "surface.raised", 3.0, "focus-boundary"),
            ("focus.indicator", "surface.canvas", 3.0, "focus-boundary"),
            ("boundary.strong", "surface.raised", 3.0, "essential-boundary"),
            ("boundary.strong", "surface.canvas", 3.0, "essential-boundary"),
            ("status.success", "surface.raised", 4.5, "status-text"),
            ("status.caution", "surface.raised", 4.5, "status-text"),
            ("status.critical", "surface.raised", 4.5, "status-text"),
            ("status.info", "surface.raised", 4.5, "status-text"),
        ],
    },
    "operational_dark": {
        "colors": {
            "surface.canvas": "#0D1317",
            "surface.raised": "#161D23",
            "content.primary": "#F2F4F5",
            "content.secondary": "#AAB4BC",
            "action.active": "#89B4C8",
            "action.onActive": "#0D1317",
            "focus.indicator": "#C4E6F0",
            "boundary.strong": "#5E6D78",
            "status.success": "#6FAF88",
            "status.caution": "#D7A44A",
            "status.critical": "#D9605D",
        },
        "contracts": [
            ("content.primary", "surface.canvas", 4.5, "text"),
            ("content.primary", "surface.raised", 4.5, "text"),
            ("content.secondary", "surface.canvas", 4.5, "text"),
            ("content.secondary", "surface.raised", 4.5, "text"),
            ("action.onActive", "action.active", 4.5, "text-on-action"),
            ("focus.indicator", "surface.canvas", 3.0, "focus-boundary"),
            ("focus.indicator", "surface.raised", 3.0, "focus-boundary"),
            ("boundary.strong", "surface.canvas", 3.0, "essential-boundary"),
            ("boundary.strong", "surface.raised", 3.0, "essential-boundary"),
            ("status.success", "surface.raised", 4.5, "status-text"),
            ("status.caution", "surface.raised", 4.5, "status-text"),
            ("status.critical", "surface.raised", 4.5, "status-text"),
        ],
    },
}


def run() -> dict:
    result = {}
    for context_name, spec in CONTEXTS.items():
        colors = spec["colors"]
        rows = []
        for fg_role, bg_role, threshold, purpose in spec["contracts"]:
            ratio = contrast(colors[fg_role], colors[bg_role])
            rows.append(
                {
                    "foreground_role": fg_role,
                    "background_role": bg_role,
                    "foreground": colors[fg_role],
                    "background": colors[bg_role],
                    "purpose": purpose,
                    "threshold": threshold,
                    "contrast_ratio": round(ratio, 4),
                    "passes_numeric_contract": ratio >= threshold,
                }
            )
        result[context_name] = rows
    return result


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, ensure_ascii=False))
