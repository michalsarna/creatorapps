#!/usr/bin/env python3
"""Refreshes the screenshots in img/ from the apps' docs/screenshots (needs Pillow: pip install pillow).

The repositories of the programs are expected next to this one (../LightCreator and so on). Run it after a release of
a program whose pictures changed, then `python3 build.py` is not needed (the page names stay the same), only commit img/.
"""
from pathlib import Path
from PIL import Image

ROOT = Path(__file__).parent
SOURCES = {
    "lc-editor": "LightCreator/docs/screenshots/02-editor-properties.png",
    "lc-preview": "LightCreator/docs/screenshots/12-preview.png",
    "mc-3d": "MillCreator/docs/screenshots/16-3d-view.png",
    "mc-control": "MillCreator/docs/screenshots/25-control-tab.png",
    "pc-plot": "PenCreator/docs/screenshots/09-plot.png",
    "pc-layers": "PenCreator/docs/screenshots/05-layers.png",
}

for name, src in SOURCES.items():
    im = Image.open(ROOT.parent / src).convert("RGB")
    out = ROOT / "img" / f"{name}.webp"
    im.save(out, "WEBP", quality=82, method=6)
    print(f"{name}: {im.size[0]}x{im.size[1]}, {out.stat().st_size // 1024} KB")
