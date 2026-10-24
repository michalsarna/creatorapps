# Creator Apps

The landing page of [LightCreator](https://github.com/michalsarna/LightCreator),
[MillCreator](https://github.com/michalsarna/MillCreator) and [PenCreator](https://github.com/michalsarna/PenCreator),
published at **https://michalsarna.github.io/creatorapps/** (English) and **/pl/** (Polish).

The pages are generated: edit the texts in `build.py` and run `python3 build.py`, then commit `index.html`, `pl/index.html`, `sitemap.xml` and `robots.txt`
together with it. Pictures are in `img/` (screenshots from the apps' `docs/screenshots`, as WebP).

After a release of a program: `python3 update_versions.py` (the version numbers on the page), `python3 build.py`, and
`python3 update_images.py` when its screenshots changed (needs Pillow). The Check workflow runs every week and fails when
a number on the page (languages, clipart, versions) no longer matches the programs.

## Licence

All rights reserved, see [LICENSE](LICENSE). The programs themselves are MIT OR Apache-2.0 in their own repositories.
