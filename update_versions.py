#!/usr/bin/env python3
"""Writes versions.json with the newest release of each program (from GitHub), for build.py. Run it after a release,
then `python3 build.py` and commit."""
import json
import urllib.request
from pathlib import Path

APPS = ["LightCreator", "MillCreator", "PenCreator"]


def latest(repo):
    with urllib.request.urlopen(f"https://api.github.com/repos/michalsarna/{repo}/releases/latest", timeout=30) as r:
        return json.load(r)["tag_name"]


if __name__ == "__main__":
    versions = {a: latest(a) for a in APPS}
    Path(__file__).with_name("versions.json").write_text(json.dumps(versions, indent=2) + "\n")
    print(versions)
