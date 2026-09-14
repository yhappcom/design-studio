from __future__ import annotations

import ctypes as C
import glob
import hashlib
import json
import os
import platform

import numpy as np
import PIL
from PIL import ImageCms

# C010 research harness. This is not production color-management code.
# It loads the same LittleCMS shared library bundled with Pillow so the
# measured CMM version is traceable and matches Pillow's runtime.
LCMS_PATH = glob.glob(
    os.path.join(os.path.dirname(PIL.__file__), "..", "pillow.libs", "liblcms2*.so*")
)[0]
LCMS_PATH = os.path.realpath(LCMS_PATH)
lib = C.CDLL(LCMS_PATH)


class cmsCIExyY(C.Structure):
    _fields_ = [("x", C.c_double), ("y", C.c_double), ("Y", C.c_double)]


class cmsCIExyYTRIPLE(C.Structure):
    _fields_ = [("Red", cmsCIExyY), ("Green", cmsCIExyY), ("Blue", cmsCIExyY)]


HPROFILE = C.c_void_p
HTRANSFORM = C.c_void_p

lib.cmsGetEncodedCMMversion.restype = C.c_uint32
lib.cmsCreate_sRGBProfile.restype = HPROFILE
lib.cmsOpenProfileFromFile.argtypes = [C.c_char_p, C.c_char_p]
lib.cmsOpenProfileFromFile.restype = HPROFILE
lib.cmsCreateRGBProfile.argtypes = [
    C.POINTER(cmsCIExyY),
    C.POINTER(cmsCIExyYTRIPLE),
    C.POINTER(HPROFILE),
]
lib.cmsCreateRGBProfile.restype = HPROFILE
lib.cmsReadTag.argtypes = [HPROFILE, C.c_uint32]
lib.cmsReadTag.restype = C.c_void_p
lib.cmsDupToneCurve.argtypes = [C.c_void_p]
lib.cmsDupToneCurve.restype = C.c_void_p
lib.cmsFreeToneCurve.argtypes = [C.c_void_p]
lib.cmsSetProfileVersion.argtypes = [HPROFILE, C.c_double]
lib.cmsCreateTransform.argtypes = [
    HPROFILE,
    C.c_uint32,
    HPROFILE,
    C.c_uint32,
    C.c_uint32,
    C.c_uint32,
]
lib.cmsCreateTransform.restype = HTRANSFORM
lib.cmsDoTransform.argtypes = [HTRANSFORM, C.c_void_p, C.c_void_p, C.c_uint32]
lib.cmsDeleteTransform.argtypes = [HTRANSFORM]
lib.cmsCloseProfile.argtypes = [HPROFILE]

# Formatter macros from lcms2.h 2.19.
FLOAT_SH = lambda a: a << 22
COLORSPACE_SH = lambda s: s << 16
CHANNELS_SH = lambda c: c << 3
BYTES_SH = lambda b: b
PT_RGB = 4
TYPE_RGB_8 = COLORSPACE_SH(PT_RGB) | CHANNELS_SH(3) | BYTES_SH(1)
TYPE_RGB_16 = COLORSPACE_SH(PT_RGB) | CHANNELS_SH(3) | BYTES_SH(2)
TYPE_RGB_DBL = (
    FLOAT_SH(1) | COLORSPACE_SH(PT_RGB) | CHANNELS_SH(3) | BYTES_SH(0)
)
INTENT_RELATIVE_COLORIMETRIC = 1
cmsFLAGS_NOOPTIMIZE = 0x0100
cmsFLAGS_NONEGATIVES = 0x8000

D65 = (0.3127, 0.3290)
SRGB_PRIMARIES = ((0.640, 0.330), (0.300, 0.600), (0.150, 0.060))
P3_PRIMARIES = ((0.680, 0.320), (0.265, 0.690), (0.150, 0.060))


def signature(s: str) -> int:
    return int.from_bytes(s.encode("ascii"), "big")


def rgb_matrix(primaries, white=D65):
    columns = []
    for x, y in primaries:
        columns.append([x / y, 1.0, (1.0 - x - y) / y])
    p = np.asarray(columns, dtype=float).T
    xw, yw = white
    w = np.asarray([xw / yw, 1.0, (1.0 - xw - yw) / yw])
    scale = np.linalg.solve(p, w)
    return p @ np.diag(scale)


def decode_srgb(c):
    c = np.asarray(c, dtype=float)
    a = np.abs(c)
    return np.where(
        a <= 0.04045,
        c / 12.92,
        np.sign(c) * ((a + 0.055) / 1.055) ** 2.4,
    )


def encode_srgb(c):
    c = np.asarray(c, dtype=float)
    a = np.abs(c)
    return np.where(
        a <= 0.0031308,
        12.92 * c,
        np.sign(c) * (1.055 * a ** (1 / 2.4) - 0.055),
    )


M_SRGB = rgb_matrix(SRGB_PRIMARIES)
M_P3 = rgb_matrix(P3_PRIMARIES)
M_P3_TO_SRGB = np.linalg.inv(M_SRGB) @ M_P3


def css_p3_to_srgb(p3):
    return encode_srgb(decode_srgb(p3) @ M_P3_TO_SRGB.T)


def transform(handle, array, dtype):
    source = np.ascontiguousarray(array, dtype=dtype)
    output = np.empty_like(source)
    lib.cmsDoTransform(
        handle,
        source.ctypes.data_as(C.c_void_p),
        output.ctypes.data_as(C.c_void_p),
        len(source),
    )
    return output


def profile_metadata(path):
    p = ImageCms.getOpenProfile(path)
    c = p.profile
    with open(path, "rb") as f:
        digest = hashlib.sha256(f.read()).hexdigest()
    return {
        "path": path,
        "sha256": digest,
        "description": ImageCms.getProfileDescription(p).strip(),
        "version": c.version,
        "device_class": c.device_class.strip(),
        "color_space": c.xcolor_space.strip(),
        "connection_space": c.connection_space.strip(),
        "media_white_xyz": list(c.media_white_point[0]),
    }


def main():
    srgb = lib.cmsCreate_sRGBProfile()

    # Controlled Display-P3-like matrix/shaper profile. Duplicate the exact sRGB
    # tone curves used by the same CMM so the experiment isolates primary/gamut
    # differences. Keep the duplicated curves alive until the profile/transforms
    # are closed; premature freeing invalidates this ctypes specimen.
    tone_curves = [
        lib.cmsDupToneCurve(lib.cmsReadTag(srgb, signature(t)))
        for t in ("rTRC", "gTRC", "bTRC")
    ]
    curves_array = (HPROFILE * 3)(*tone_curves)
    white = cmsCIExyY(D65[0], D65[1], 1.0)
    primaries = cmsCIExyYTRIPLE(
        cmsCIExyY(*P3_PRIMARIES[0], 1.0),
        cmsCIExyY(*P3_PRIMARIES[1], 1.0),
        cmsCIExyY(*P3_PRIMARIES[2], 1.0),
    )
    p3 = lib.cmsCreateRGBProfile(C.byref(white), C.byref(primaries), curves_array)
    lib.cmsSetProfileVersion(p3, 4.4)

    flags = cmsFLAGS_NOOPTIMIZE
    x_float = lib.cmsCreateTransform(
        p3,
        TYPE_RGB_DBL,
        srgb,
        TYPE_RGB_DBL,
        INTENT_RELATIVE_COLORIMETRIC,
        flags,
    )
    x_float_nonnegative = lib.cmsCreateTransform(
        p3,
        TYPE_RGB_DBL,
        srgb,
        TYPE_RGB_DBL,
        INTENT_RELATIVE_COLORIMETRIC,
        flags | cmsFLAGS_NONEGATIVES,
    )
    x_back_float = lib.cmsCreateTransform(
        srgb,
        TYPE_RGB_DBL,
        p3,
        TYPE_RGB_DBL,
        INTENT_RELATIVE_COLORIMETRIC,
        flags,
    )
    x_16 = lib.cmsCreateTransform(
        p3,
        TYPE_RGB_16,
        srgb,
        TYPE_RGB_16,
        INTENT_RELATIVE_COLORIMETRIC,
        flags,
    )
    x_8 = lib.cmsCreateTransform(
        p3,
        TYPE_RGB_8,
        srgb,
        TYPE_RGB_8,
        INTENT_RELATIVE_COLORIMETRIC,
        flags,
    )

    steps = np.linspace(0.0, 1.0, 33)
    grid = np.array(np.meshgrid(steps, steps, steps, indexing="ij")).reshape(3, -1).T
    direct = css_p3_to_srgb(grid)
    cmm_float = transform(x_float, grid, np.float64)
    cmm_nonnegative = transform(x_float_nonnegative, grid, np.float64)
    roundtrip = transform(x_back_float, cmm_float, np.float64)

    in_gamut = np.all((direct >= -1e-12) & (direct <= 1.0 + 1e-12), axis=1)
    out_gamut = ~in_gamut
    float_error = np.abs(cmm_float - direct)
    rt_error = np.abs(roundtrip - grid)

    q16 = np.round(grid * 65535.0).astype(np.uint16)
    out16 = transform(x_16, q16, np.uint16).astype(float) / 65535.0
    q16_float = q16.astype(float) / 65535.0
    float_at_q16 = transform(x_float, q16_float, np.float64)
    quant16_error = np.abs(out16 - np.clip(float_at_q16, 0.0, 1.0))

    q8 = np.round(grid * 255.0).astype(np.uint8)
    out8 = transform(x_8, q8, np.uint8).astype(float) / 255.0
    q8_float = q8.astype(float) / 255.0
    float_at_q8 = transform(x_float, q8_float, np.float64)
    quant8_error = np.abs(out8 - np.clip(float_at_q8, 0.0, 1.0))

    # Gradient precision probe kept inside the destination gamut.
    ramp_n = 4097
    t = np.linspace(0, 1, ramp_n)
    ramp = np.column_stack(
        [0.15 + 0.70 * t, 0.18 + 0.66 * t, 0.20 + 0.62 * t]
    )
    ramp_float = transform(x_float, ramp, np.float64)
    r16 = np.round(ramp * 65535).astype(np.uint16)
    r8 = np.round(ramp * 255).astype(np.uint8)
    ramp16 = transform(x_16, r16, np.uint16).astype(float) / 65535
    ramp8 = transform(x_8, r8, np.uint8).astype(float) / 255

    samples = np.asarray(
        [
            [0.0, 0.0, 0.0],
            [1.0, 1.0, 1.0],
            [0.5, 0.5, 0.5],
            [1.0, 0.0, 0.0],
            [0.0, 1.0, 0.0],
            [0.0, 0.0, 1.0],
            [0.0, 1.0, 0.5],
            [1.0, 0.2, 0.8],
            [0.168, 0.950, 0.920],
            [0.500, 0.700, 0.200],
        ],
        dtype=float,
    )
    s_direct = css_p3_to_srgb(samples)
    s_float = transform(x_float, samples, np.float64)
    s_nonnegative = transform(x_float_nonnegative, samples, np.float64)
    s_back = transform(x_back_float, s_float, np.float64)

    # Independently distributed real on-disk sRGB profile if present.
    artifex_path = "/usr/share/color/icc/ghostscript/srgb.icc"
    artifex_result = None
    if os.path.exists(artifex_path):
        art = lib.cmsOpenProfileFromFile(artifex_path.encode(), b"r")
        x_art = lib.cmsCreateTransform(
            p3,
            TYPE_RGB_DBL,
            art,
            TYPE_RGB_DBL,
            INTENT_RELATIVE_COLORIMETRIC,
            flags,
        )
        art_out = transform(x_art, grid, np.float64)
        d = np.abs(art_out[in_gamut] - cmm_float[in_gamut])
        artifex_result = {
            "profile": profile_metadata(artifex_path),
            "in_gamut_sample_count": int(in_gamut.sum()),
            "max_abs_output_difference_vs_lcms_builtin_srgb": float(d.max()),
            "mean_abs_output_difference_vs_lcms_builtin_srgb": float(d.mean()),
            "p95_abs_output_difference_vs_lcms_builtin_srgb": float(
                np.percentile(d, 95)
            ),
            "interpretation": (
                "Profile-to-profile implementation comparison only; not a physical "
                "display validation and not a cross-CMM comparison."
            ),
        }
        lib.cmsDeleteTransform(x_art)
        lib.cmsCloseProfile(art)

    encoded = int(lib.cmsGetEncodedCMMversion())
    result = {
        "study": "C010",
        "environment": {
            "python": platform.python_version(),
            "pillow": PIL.__version__,
            "littlecms_encoded": encoded,
            "littlecms_version": f"{encoded // 1000}.{(encoded % 1000) // 10}",
            "littlecms_library": LCMS_PATH,
        },
        "controlled_profiles": {
            "source": (
                "generated Display-P3-like ICC v4.4 matrix/shaper: D65, P3 "
                "primaries, duplicated lcms sRGB TRCs"
            ),
            "destination": "LittleCMS built-in sRGB profile",
            "intent": "relative colorimetric",
            "flags": ["cmsFLAGS_NOOPTIMIZE"],
        },
        "matrices": {
            "srgb_to_xyz_d65": M_SRGB.tolist(),
            "display_p3_to_xyz_d65": M_P3.tolist(),
            "linear_display_p3_to_linear_srgb": M_P3_TO_SRGB.tolist(),
        },
        "grid": {
            "steps_per_channel": 33,
            "sample_count": int(len(grid)),
            "in_css_srgb_gamut_count": int(in_gamut.sum()),
            "out_css_srgb_gamut_count": int(out_gamut.sum()),
            "out_css_srgb_gamut_fraction_of_uniform_encoded_grid": float(
                out_gamut.mean()
            ),
            "note": (
                "This fraction is for a uniform encoded RGB grid; it is not a "
                "perceptual gamut-volume estimate."
            ),
            "float_cmm_vs_css_direct_max_abs_in_gamut": float(
                float_error[in_gamut].max()
            ),
            "float_cmm_vs_css_direct_mean_abs_in_gamut": float(
                float_error[in_gamut].mean()
            ),
            "float_cmm_vs_css_direct_p95_abs_in_gamut": float(
                np.percentile(float_error[in_gamut], 95)
            ),
            "float_cmm_vs_css_direct_max_abs_all": float(float_error.max()),
            "float_cmm_vs_css_direct_mean_abs_all": float(float_error.mean()),
            "out_of_range_component_counts": {
                "below_zero": int(np.sum(cmm_float < 0)),
                "above_one": int(np.sum(cmm_float > 1)),
            },
            "nonegatives_changed_pixel_fraction": float(
                np.mean(np.any(np.abs(cmm_nonnegative - cmm_float) > 1e-12, axis=1))
            ),
            "float_unbounded_roundtrip_max_abs_all": float(rt_error.max()),
            "float_unbounded_roundtrip_mean_abs_all": float(rt_error.mean()),
            "float_unbounded_roundtrip_max_abs_out_gamut": float(
                rt_error[out_gamut].max()
            ),
            "uint16_vs_clipped_float_max_abs": float(quant16_error.max()),
            "uint16_vs_clipped_float_mean_abs": float(quant16_error.mean()),
            "uint8_vs_clipped_float_max_abs": float(quant8_error.max()),
            "uint8_vs_clipped_float_mean_abs": float(quant8_error.mean()),
        },
        "gradient_probe": {
            "samples": ramp_n,
            "float_all_in_0_1": bool(
                np.all((ramp_float >= 0) & (ramp_float <= 1))
            ),
            "unique_rgb_triplets_16bit": int(
                np.unique(np.round(ramp16 * 65535).astype(np.uint16), axis=0).shape[0]
            ),
            "unique_rgb_triplets_8bit": int(
                np.unique(np.round(ramp8 * 255).astype(np.uint8), axis=0).shape[0]
            ),
            "input_unique_triplets_16bit": int(np.unique(r16, axis=0).shape[0]),
            "input_unique_triplets_8bit": int(np.unique(r8, axis=0).shape[0]),
        },
        "representative_samples": [],
        "independent_profile_check": artifex_result,
        "interpretation_boundaries": [
            (
                "In-gamut agreement compares an ICC/CMM transform against an "
                "independent CSS-style matrix/transfer calculation."
            ),
            (
                "Out-of-gamut floating-point numeric triplets are representation-"
                "dependent: LittleCMS unbounded ICC curve extrapolation is not "
                "assumed to equal CSS extended-range transfer semantics."
            ),
            (
                "Floating-point unbounded round-trip precision does not mean an "
                "sRGB display can show out-of-gamut P3 colors; integer destination "
                "encodings clip/bound them."
            ),
            (
                "cmsFLAGS_NONEGATIVES suppresses negative outputs but does not by "
                "itself constitute perceptual gamut mapping or full [0,1] clipping."
            ),
            (
                "The generated P3 profile is a controlled matrix/shaper specimen, "
                "not a measured device profile."
            ),
            (
                "The Artifex profile check is cross-profile, not cross-CMM or "
                "physical-display evidence."
            ),
        ],
    }

    for i, p3v in enumerate(samples):
        result["representative_samples"].append(
            {
                "display_p3_encoded": p3v.tolist(),
                "css_direct_extended_srgb": s_direct[i].tolist(),
                "lcms_unbounded_srgb": s_float[i].tolist(),
                "lcms_nonegatives_srgb": s_nonnegative[i].tolist(),
                "unbounded_float_back_to_p3": s_back[i].tolist(),
                "css_srgb_in_gamut": bool(
                    np.all((s_direct[i] >= 0) & (s_direct[i] <= 1))
                ),
            }
        )

    print(json.dumps(result, indent=2))

    for h in (x_float, x_float_nonnegative, x_back_float, x_16, x_8):
        lib.cmsDeleteTransform(h)
    for t in tone_curves:
        lib.cmsFreeToneCurve(t)
    lib.cmsCloseProfile(p3)
    lib.cmsCloseProfile(srgb)


if __name__ == "__main__":
    main()
