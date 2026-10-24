#!/usr/bin/env python3
"""Checks that the numbers on the page still match the programs (read from the repositories on GitHub).

Exit code 1 and a list of differences when something is stale; run by the Check workflow every week and on every push.
"""
import re
import sys
import urllib.request
from pathlib import Path

RAW = "https://raw.githubusercontent.com/michalsarna/"
build = (Path(__file__).parent / "build.py").read_text()


def fetch(path):
    with urllib.request.urlopen(RAW + path, timeout=30) as r:
        return r.read().decode()


problems = []


def expect(what, claimed, actual):
    if claimed != actual:
        problems.append(f"{what}: the page says {claimed}, the programs say {actual}")


# Languages: the length of Lang::ALL in baseCreator.
langs = int(re.search(r"const ALL: \[Lang; (\d+)\]", fetch("baseCreator/main/crates/base-ui/src/i18n.rs")).group(1))
for m in re.finditer(r'"(\d+) (?:languages|języków)"', build):
    expect("languages", int(m.group(1)), langs)

# Clipart: "N ready-made ... pictures in M categories" in FEATURES.md of LightCreator.
m = re.search(r"(\d+) ready-made single-colour pictures in (\d+) categories", fetch("LightCreator/main/FEATURES.md"))
pictures, categories = int(m.group(1)), int(m.group(2))
for m in re.finditer(r"(\d+) (?:pictures|obrazków) (?:in|w) (\d+) (?:categories|kategoriach)", build):
    expect("clipart pictures", int(m.group(1)), pictures)
    expect("clipart categories", int(m.group(2)), categories)

if problems:
    print("The page is out of date:")
    for p in problems:
        print(" -", p)
    sys.exit(1)
print(f"OK: {langs} languages, {pictures} pictures in {categories} categories")
