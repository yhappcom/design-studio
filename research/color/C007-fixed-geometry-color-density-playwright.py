import json
import tempfile
from pathlib import Path

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent
HTML = ROOT / 'C007-fixed-geometry-color-density-specimen.html'
RESULTS = ROOT / 'C007-fixed-geometry-color-density-results.json'
VARIANTS = ['neutral', 'overloaded', 'high-contrast-mono', 'semantic-sparse']


def srgb_to_linear(x):
    x = np.asarray(x, dtype=np.float64)
    return np.where(x <= 0.04045, x / 12.92, ((x + 0.055) / 1.055) ** 2.4)


def rgb_to_oklab(rgb):
    lin = srgb_to_linear(rgb)
    r, g, b = lin[..., 0], lin[..., 1], lin[..., 2]
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l_, m_, s_ = np.cbrt(l), np.cbrt(m), np.cbrt(s)
    L = 0.2104542553 * l_ + 0.7936177850 * m_ - 0.0040720468 * s_
    a = 1.9779984951 * l_ - 2.4285922050 * m_ + 0.4505937099 * s_
    bb = 0.0259040371 * l_ + 0.7827717662 * m_ - 0.8086757660 * s_
    return np.stack([L, a, bb], axis=-1)


def image_metrics(path):
    im = Image.open(path).convert('RGB')
    w, h = im.size
    ds = im.resize((max(1, w // 4), max(1, h // 4)), Image.Resampling.BOX)
    arr = np.asarray(ds, dtype=np.float64) / 255.0
    lab = rgb_to_oklab(arr)
    L, a, b = lab[..., 0], lab[..., 1], lab[..., 2]
    C = np.sqrt(a * a + b * b)
    dL = np.concatenate([np.abs(np.diff(L, axis=0)).ravel(), np.abs(np.diff(L, axis=1)).ravel()])
    dC = np.concatenate([np.abs(np.diff(C, axis=0)).ravel(), np.abs(np.diff(C, axis=1)).ravel()])

    # Study-specific local variability proxy. This is deliberately NOT called
    # Rosenholtz Feature Congestion; it is only for within-specimen comparison.
    try:
        from scipy.ndimage import uniform_filter

        def local_std(x, size=5):
            mu = uniform_filter(x, size=size, mode='reflect')
            mu2 = uniform_filter(x * x, size=size, mode='reflect')
            return np.sqrt(np.maximum(mu2 - mu * mu, 0))

        sL, sa, sb = local_std(L), local_std(a), local_std(b)
        local_feature = np.sqrt(sL * sL + sa * sa + sb * sb)
        local_mean = float(local_feature.mean())
        local_p95 = float(np.percentile(local_feature, 95))
    except Exception:
        local_mean = local_p95 = None

    return {
        'mean_oklab_L': float(L.mean()),
        'std_oklab_L': float(L.std()),
        'mean_oklab_chroma': float(C.mean()),
        'std_oklab_chroma': float(C.std()),
        'p95_oklab_chroma': float(np.percentile(C, 95)),
        'high_chroma_pixel_share_C_gt_0_04': float((C > 0.04).mean()),
        'high_chroma_pixel_share_C_gt_0_08': float((C > 0.08).mean()),
        'adjacent_L_absdiff_mean': float(dL.mean()),
        'adjacent_L_absdiff_p95': float(np.percentile(dL, 95)),
        'adjacent_chroma_absdiff_mean': float(dC.mean()),
        'local_feature_variability_mean': local_mean,
        'local_feature_variability_p95': local_p95,
        'image_size': [w, h],
        'analysis_size': [ds.size[0], ds.size[1]],
    }


def rect_mean_oklab(path, rect, inset=4):
    im = np.asarray(Image.open(path).convert('RGB'), dtype=np.float64) / 255.0
    x, y, w, h = rect
    x0 = max(0, int(round(x + inset)))
    y0 = max(0, int(round(y + inset)))
    x1 = min(im.shape[1], int(round(x + w - inset)))
    y1 = min(im.shape[0], int(round(y + h - inset)))
    lab = rgb_to_oklab(im[y0:y1, x0:x1])
    return lab.reshape(-1, 3).mean(axis=0)


results = {}
browser_version = None
with tempfile.TemporaryDirectory(prefix='c007-') as td, sync_playwright() as p:
    td = Path(td)
    browser = p.chromium.launch(headless=True, executable_path='/usr/bin/chromium', args=['--no-sandbox'])
    browser_version = browser.version
    page = browser.new_page(viewport={'width': 1024, 'height': 900}, device_scale_factor=1)
    page.set_content(HTML.read_text(encoding='utf-8'), wait_until='load')
    base_geom = None

    for variant in VARIANTS:
        page.evaluate('(v) => window.setVariant(v)', variant)
        page.wait_for_timeout(60)
        geom = page.evaluate('() => window.geometry()')
        if base_geom is None:
            base_geom = geom
        same = geom == base_geom

        shot = td / f'{variant}.png'
        page.screenshot(path=str(shot), full_page=True)
        metrics = image_metrics(shot)

        normal_btn = rect_mean_oklab(shot, geom['buttons'][0], 4)
        primary_btn = rect_mean_oklab(shot, geom['buttons'][2], 4)
        metrics['primary_vs_normal_button_region_oklab_distance'] = float(
            np.linalg.norm(primary_btn - normal_btn)
        )

        # Selected data row index 5 is geometry row 6 because row 0 is the table header.
        sel = rect_mean_oklab(shot, geom['rows'][6], 10)
        prev = rect_mean_oklab(shot, geom['rows'][5], 10)
        nxt = rect_mean_oklab(shot, geom['rows'][7], 10)
        metrics['selected_vs_adjacent_row_region_oklab_distance'] = float(
            np.linalg.norm(sel - (prev + nxt) / 2)
        )

        # Cell rectangles are only needed for the geometry identity assertion, not persisted.
        geom.pop('cells', None)
        results[variant] = {
            'geometry_identical_to_neutral': same,
            'geometry': geom,
            'metrics': metrics,
        }

    browser.close()

payload = {
    'environment': {
        'chromium_executable': '/usr/bin/chromium',
        'chromium_version': browser_version,
        'playwright_python': True,
        'viewport': [1024, 900],
        'device_scale_factor': 1,
    },
    'method_notes': {
        'geometry': 'DOM rectangles must be identical across variants; only CSS color custom properties change.',
        'image_metrics': 'Screenshots are downsampled 4x. Oklab statistics and a study-specific local feature-variability proxy are computed. The proxy is not Rosenholtz Feature Congestion and is not a human-clutter score.',
    },
    'results': results,
}
RESULTS.write_text(json.dumps(payload, indent=2), encoding='utf-8')
print(json.dumps({v: {'geometry_identical': results[v]['geometry_identical_to_neutral'], **results[v]['metrics']} for v in VARIANTS}, indent=2))
