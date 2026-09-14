"""Reproducible raster probe for Exercise 002.

This is a study utility, not a font build pipeline. It rasterizes the existing
SVG construction hypotheses through CairoSVG, crops the three uppercase H/O
panels, and downsamples them so the nominal cap-height is approximately
14/24/48 px. The goal is to expose small-size failures that are invisible in
large vector inspection.

Dependencies: cairosvg, pillow
Run from repository root:
    python type-design/tools/raster_probe_ex002.py
Output:
    type-design/evidence/ex002-raster-14-24-48.png
"""

from pathlib import Path
from io import BytesIO

import cairosvg
from PIL import Image, ImageDraw, ImageOps

ROOT = Path(__file__).resolve().parents[2]
SOURCE = ROOT / "type-design" / "exercises" / "002-construction-curve-optics.svg"
OUTPUT = ROOT / "type-design" / "evidence" / "ex002-raster-14-24-48.png"

# Coordinates refer to the current Exercise 002 canvas (1600 × 1180).
# They intentionally include H and O but exclude most annotations.
PANELS = {
    "A": (95, 155, 535, 455),
    "B": (610, 155, 1055, 455),
    "C": (1125, 155, 1580, 455),
}

# Exercise 002 nominal uppercase flat cap zone is 250 design px high.
NOMINAL_CAP = 250
TARGET_CAPS = (14, 24, 48)
SUPERSAMPLE = 4


def render_source() -> Image.Image:
    svg = SOURCE.read_bytes()
    png = cairosvg.svg2png(
        bytestring=svg,
        output_width=1600 * SUPERSAMPLE,
        output_height=1180 * SUPERSAMPLE,
    )
    return Image.open(BytesIO(png)).convert("L")


def crop_panel(image: Image.Image, box: tuple[int, int, int, int]) -> Image.Image:
    return image.crop(tuple(v * SUPERSAMPLE for v in box))


def target_resize(panel: Image.Image, target_cap: int) -> Image.Image:
    # Source cap-height is NOMINAL_CAP * SUPERSAMPLE after supersampling.
    scale = target_cap / (NOMINAL_CAP * SUPERSAMPLE)
    width = max(1, round(panel.width * scale))
    height = max(1, round(panel.height * scale))
    return panel.resize((width, height), Image.Resampling.LANCZOS)


def compose() -> Image.Image:
    source = render_source()
    crops = {name: crop_panel(source, box) for name, box in PANELS.items()}

    rows: list[Image.Image] = []
    for target in TARGET_CAPS:
        parts: list[tuple[str, Image.Image]] = []
        for name, panel in crops.items():
            raster = target_resize(panel, target)
            parts.append((name, ImageOps.expand(raster, border=8, fill=255)))

        row_h = max(img.height for _, img in parts) + 22
        row_w = sum(img.width for _, img in parts) + 20 * (len(parts) - 1)
        row = Image.new("L", (row_w, row_h), 245)
        draw = ImageDraw.Draw(row)
        x = 0
        for name, img in parts:
            draw.text((x + 2, 2), f"{name} {target}px", fill=0)
            row.paste(img, (x, 20))
            x += img.width + 20
        rows.append(row)

    canvas_w = max(row.width for row in rows)
    canvas_h = sum(row.height for row in rows) + 10 * (len(rows) - 1)
    canvas = Image.new("L", (canvas_w, canvas_h), 245)
    y = 0
    for row in rows:
        canvas.paste(row, (0, y))
        y += row.height + 10
    return canvas


def main() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    result = compose()
    result.save(OUTPUT)
    print(OUTPUT)


if __name__ == "__main__":
    main()
