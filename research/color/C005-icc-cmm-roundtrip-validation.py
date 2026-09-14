"""C005 reproducible ICC/CMM validation specimen.

Purpose:
- inspect a generated sRGB v4 profile through Pillow/ImageCms + LittleCMS;
- verify its D65→D50 chromatic-adaptation matrix against the stored D50 colorants;
- compare a CMM sRGB→Lab transform with an independent hand calculation;
- quantify the loss introduced by an 8-bit Lab intermediate on round-trip.

This is research tooling, not a production color-management implementation.
"""

from __future__ import annotations

import itertools
import json
import platform

import numpy as np
import PIL
from PIL import Image, ImageCms

# CSS Color 4 / standard sRGB D65 linear-RGB → XYZ matrix.
M_SRGB_D65_TO_XYZ = np.array(
    [
        [0.41239079926595934, 0.35758433938387796, 0.1804807884018343],
        [0.21263900587151027, 0.7151686787677559, 0.07219231536073371],
        [0.01933081871559182, 0.11919477979462598, 0.9505321522496607],
    ],
    dtype=float,
)

D50_XYZ = np.array([0.9642, 1.0, 0.8249], dtype=float)


def srgb_decode(rgb: tuple[int, int, int]) -> np.ndarray:
    c = np.asarray(rgb, dtype=float) / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def xyz_d50_to_lab(xyz: np.ndarray) -> np.ndarray:
    t = xyz / D50_XYZ
    delta = 6 / 29
    f = np.where(t > delta**3, np.cbrt(t), t / (3 * delta**2) + 4 / 29)
    fx, fy, fz = f
    return np.array([116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)])


def decode_pillow_lab(pixel: tuple[int, int, int]) -> np.ndarray:
    # Pillow's 8-bit LAB mode maps L* to 0..255 and offsets a*, b* by 128.
    return np.array([pixel[0] * 100 / 255, pixel[1] - 128, pixel[2] - 128], dtype=float)


def main() -> None:
    srgb_core = ImageCms.createProfile("sRGB")
    lab_core = ImageCms.createProfile("LAB", 5000)
    srgb = ImageCms.ImageCmsProfile(srgb_core)
    lab = ImageCms.ImageCmsProfile(lab_core)

    chad = np.asarray(srgb_core.chromatic_adaptation[0], dtype=float)
    profile_colorants = np.column_stack(
        [
            np.asarray(srgb_core.red_colorant[0], dtype=float),
            np.asarray(srgb_core.green_colorant[0], dtype=float),
            np.asarray(srgb_core.blue_colorant[0], dtype=float),
        ]
    )

    d65_white = M_SRGB_D65_TO_XYZ @ np.ones(3)
    reconstructed_colorants = chad @ M_SRGB_D65_TO_XYZ

    # 17 values/channel → 17^3 = 4913 RGB samples.
    steps = list(range(0, 256, 16)) + [255]
    colors = list(itertools.product(steps, repeat=3))

    source = Image.new("RGB", (len(colors), 1))
    source.putdata(colors)

    lab_image = ImageCms.profileToProfile(
        source,
        srgb,
        lab,
        outputMode="LAB",
        renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
    )
    cmm_lab = np.asarray(
        [decode_pillow_lab(pixel) for pixel in lab_image.get_flattened_data()], dtype=float
    )

    hand_lab = np.asarray(
        [
            xyz_d50_to_lab(chad @ (M_SRGB_D65_TO_XYZ @ srgb_decode(rgb)))
            for rgb in colors
        ],
        dtype=float,
    )
    lab_error = np.abs(hand_lab - cmm_lab)

    roundtrip = ImageCms.profileToProfile(
        lab_image,
        lab,
        srgb,
        outputMode="RGB",
        renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
    )
    original_rgb = np.asarray(colors, dtype=int)
    roundtrip_rgb = np.asarray(list(roundtrip.get_flattened_data()), dtype=int)
    rgb_error = np.abs(roundtrip_rgb - original_rgb)

    sample_rgbs = [
        (168, 240, 233),  # MintTap mint example
        (0, 95, 204),
        (255, 0, 0),
        (0, 255, 0),
        (0, 0, 255),
        (128, 128, 128),
    ]
    samples = []
    for rgb in sample_rgbs:
        one = Image.new("RGB", (1, 1), rgb)
        one_lab_image = ImageCms.profileToProfile(
            one,
            srgb,
            lab,
            outputMode="LAB",
            renderingIntent=ImageCms.Intent.RELATIVE_COLORIMETRIC,
        )
        cmm = decode_pillow_lab(next(iter(one_lab_image.get_flattened_data())))
        hand = xyz_d50_to_lab(chad @ (M_SRGB_D65_TO_XYZ @ srgb_decode(rgb)))
        samples.append(
            {
                "rgb": list(rgb),
                "hex": "#%02X%02X%02X" % rgb,
                "lab_hand": hand.tolist(),
                "lab_cmm_8bit": cmm.tolist(),
                "abs_diff": np.abs(hand - cmm).tolist(),
            }
        )

    result = {
        "environment": {
            "python": platform.python_version(),
            "pillow": PIL.__version__,
            "littlecms": ImageCms.core.littlecms_version,
        },
        "profiles": {
            "srgb": {
                "description": ImageCms.getProfileDescription(srgb).strip(),
                "version": srgb_core.version,
                "device_class": srgb_core.device_class.strip(),
                "connection_space": srgb_core.connection_space.strip(),
                "media_white_xyz": list(srgb_core.media_white_point[0]),
            },
            "lab": {
                "description": ImageCms.getProfileDescription(lab).strip(),
                "version": lab_core.version,
                "device_class": lab_core.device_class.strip(),
                "connection_space": lab_core.connection_space.strip(),
                "media_white_xyz": list(lab_core.media_white_point[0]),
            },
        },
        "srgb_d65_white_xyz": d65_white.tolist(),
        "srgb_profile_chad": chad.tolist(),
        "chad_applied_to_d65_white": (chad @ d65_white).tolist(),
        "profile_colorant_matrix_d50": profile_colorants.tolist(),
        "chad_times_srgb_d65_matrix": reconstructed_colorants.tolist(),
        "max_abs_profile_colorant_residual": float(
            np.max(np.abs(profile_colorants - reconstructed_colorants))
        ),
        "grid": {
            "steps": steps,
            "count": len(colors),
            "cmm_vs_hand_lab_abs_max": np.max(lab_error, axis=0).tolist(),
            "cmm_vs_hand_lab_abs_mean": np.mean(lab_error, axis=0).tolist(),
            "cmm_vs_hand_lab_abs_p95": np.percentile(lab_error, 95, axis=0).tolist(),
            "rgb_lab8_rgb_roundtrip_max_channel_error": int(np.max(rgb_error)),
            "rgb_lab8_rgb_roundtrip_mean_channel_error": float(np.mean(rgb_error)),
            "rgb_lab8_rgb_roundtrip_p95_channel_error": float(
                np.percentile(rgb_error, 95)
            ),
            "exact_pixel_fraction": float(np.mean(np.all(rgb_error == 0, axis=1))),
            "all_channels_le_1_fraction": float(
                np.mean(np.all(rgb_error <= 1, axis=1))
            ),
            "all_channels_le_2_fraction": float(
                np.mean(np.all(rgb_error <= 2, axis=1))
            ),
        },
        "samples": samples,
        "interpretation_boundary": [
            "CMM-to-hand Lab agreement is observed through an 8-bit Lab output buffer; half-step Lab quantization is expected.",
            "Large RGB round-trip errors do not prove CMM inaccuracy; the tested route contains an 8-bit Lab intermediate and gamma re-encoding.",
            "The generated sRGB profile is a controlled toolchain specimen, not a substitute for project-specific display/output profiles.",
        ],
    }

    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
