#!/usr/bin/env python3
"""Builds the Creator Apps landing page: index.html (English) and pl/index.html (Polish).

Edit the texts in T below and run `python3 build.py`. The generated pages are committed,
so GitHub Pages serves the repository as it is.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
VERSIONS = json.loads((ROOT / "versions.json").read_text())  # from update_versions.py
BASE = "https://michalsarna.github.io/creatorapps/"
GH = "https://github.com/michalsarna/"
BMC = "https://buymeacoffee.com/michalsarna"
PLUGINS = "https://michalsarna.github.io/baseCreator-plugins/"

APPS = [
    # id, repo, icon, screenshots
    ("lc", "LightCreator", "lightcreator", ["lc-editor", "lc-preview"]),
    ("mc", "MillCreator", "millcreator", ["mc-3d", "mc-control"]),
    ("pc", "PenCreator", "pencreator", ["pc-plot", "pc-layers"]),
]

T = {
    "en": {
        "html_lang": "en",
        "path": "",
        "other": "pl",
        "other_label": "Polski",
        "skip": "Skip to content",
        "title": "Creator Apps · free software for lasers, CNC mills and pen plotters",
        "desc": "LightCreator, MillCreator and PenCreator: free, open-source design and G-code software for laser engravers, CNC mills and pen plotters. Windows, macOS and Linux, 30 languages.",
        "nav": ["Apps", "Together", "Plugins", "Download", "Support"],
        "hero_kicker": "Free · open source · Windows, macOS, Linux",
        "hero_title": "One family of programs for your <em>laser</em>, <em>CNC mill</em> and <em>pen plotter</em>",
        "hero_text": "Design or import a drawing, give every layer a job, look at the result in the preview and send G-code to the machine. The same window, the same tools and the same shortcuts in all three programs.",
        "cta_download": "Download",
        "cta_support": "Buy me a coffee",
        "apps_title": "Pick your machine",
        "apps": {
            "lc": {
                "tag": "Laser engravers and cutters",
                "text": "An open-source alternative to LightBurn. Cut layers, line, fill and image engraving with six dithering methods, a camera overlay, a toolpath preview with the time of the job and a G-code viewer.",
                "points": ["GRBL and Marlin over a serial port or the network", "Ruida / Trocen jobs as PLT / DXF", "Tested on a Sculpfun S9 diode laser"],
                "shots": ["The editor with the Properties tab", "The preview of a job"],
                "status": "Works on a real machine",
            },
            "mc": {
                "tag": "CNC milling machines",
                "text": "Layers with an operation (outside, inside, on the line, pocket, drill) and a bit from the library, a 3D preview of the material, picture engraving and 3D relief, streaming to GRBL with probing and macros.",
                "points": ["Bit library with seven kinds of bits", "3D view and an animated simulation", "Tested on a TwoTrees TTC450Pro"],
                "shots": ["The 3D preview of the cuts", "The Control tab: position, jogging, probing"],
                "status": "Works on a real machine",
            },
            "pc": {
                "tag": "Pen plotters",
                "text": "Pens as layers: colour, width, speed, outline and fill lines. A plot preview with the pen-up moves, the number of lifts and the time, stroke ordering to shorten the moves, and a pause to change the pen.",
                "points": ["Z axis or a servo pen lift", "Pen library with the mark each pen makes", "Pictures drawn with dots or hatching"],
                "shots": ["The plot preview", "Pens as layers"],
                "status": "Early: not yet tried on a real plotter",
            },
        },
        "btn_download": "Download",
        "btn_github": "Source on GitHub",
        "together_title": "Built together, on baseCreator",
        "together_text": "All three programs share one core, so a new tool or fix lands in every one of them.",
        "features": [
            ("30 languages", "Polish, English, German, Spanish, Chinese, Hindi, Greek and more. Switch in the start window."),
            ("Windows, macOS, Linux", "Installers for Windows, .dmg for Apple silicon and Intel, .deb and .tar.gz for x86_64 and ARM64."),
            ("Free and open", "MIT or Apache-2.0. No account, no subscription, no telemetry."),
            ("Imports what you have", "SVG, PDF and Illustrator files, bitmaps with tracing, LightBurn projects (.lbrn2) and UGS Designer designs."),
            ("A shared clipart gallery", "310 pictures in 9 categories, your own pictures and online search of open icon collections."),
            ("One project file", "A .cre project keeps one drawing with a section for every program, so you can laser a part and mill another."),
            ("A G-code viewer", "Open any G-code file from the start window, without a project: flat or in 3D, with travel moves, colour by height, size and time."),
            ("A navigation cube", "Click a face, an edge or a corner of the cube in a 3D view to look from there, the same as in FreeCAD."),
            ("Control the machine", "Jogging, probing, start from a line, macros, the firmware settings and calibration, over a serial port or the network."),
        ],
        "plugins_title": "Plugins",
        "plugins_text": "Install generators, importers and G-code postprocessors from the official list with one click: Settings → Plugins… → Official plugins. Each one runs in a sandbox and works in every program that can use it.",
        "plugins_list": ["Circuit boards from KiCad, Gerber, EAGLE and EasyEDA", "Boxes with finger joints for a laser", "Nets of boxes to cut out of card", "Fractals, gears, holes on a circle", "STL projection, x,y point files"],
        "plugins_btn": "See all plugins",
        "dl_title": "Download",
        "dl_text": "Every release has ready packages. Pick your program and your system; the link takes you to the newest version.",
        "dl_cols": ["Windows", "macOS", "Linux"],
        "dl_win": "Installer (.exe)",
        "dl_mac": "Apple silicon / Intel (.dmg)",
        "dl_linux": ".deb / .tar.gz",
        "dl_note": "macOS: the apps are not notarized yet, so open them the first time with right-click → Open. Check downloads with SHA256SUMS.txt. You can also build every program from source with Rust.",
        "dl_safety": "A laser and a milling machine are dangerous. Try every new job in the air first and never leave a running machine alone.",
        "support_title": "Support the project",
        "support_text": "The Creator apps are made after hours by one person and they are free for everyone. If they save you time or money, you can buy me a coffee. Thank you!",
        "support_other_title": "Other ways to help",
        "support_other": [
            ("Star the repositories", "it helps other makers find the programs"),
            ("Report bugs and ideas", "in the Issues tab of each repository"),
            ("Test on your machine", "and tell how it went, especially plotters and Marlin"),
            ("Improve a translation", "or add clipart and materials"),
        ],
        "footer": "Made by Michał Sarna · MIT or Apache-2.0",
    },
    "pl": {
        "html_lang": "pl",
        "path": "pl/",
        "other": "en",
        "other_label": "English",
        "skip": "Przejdź do treści",
        "title": "Creator Apps · darmowe programy do laserów, frezarek CNC i ploterów",
        "desc": "LightCreator, MillCreator i PenCreator: darmowe programy open source do projektowania i G-code dla grawerek laserowych, frezarek CNC i ploterów pisakowych. Windows, macOS i Linux, 30 języków.",
        "nav": ["Programy", "Wspólne", "Wtyczki", "Pobierz", "Wesprzyj"],
        "hero_kicker": "Za darmo · open source · Windows, macOS, Linux",
        "hero_title": "Jedna rodzina programów do <em>lasera</em>, <em>frezarki CNC</em> i <em>plotera</em>",
        "hero_text": "Narysuj lub zaimportuj projekt, przypisz każdej warstwie zadanie, obejrzyj wynik w podglądzie i wyślij G-code do maszyny. To samo okno, te same narzędzia i te same skróty we wszystkich trzech programach.",
        "cta_download": "Pobierz",
        "cta_support": "Postaw mi kawę",
        "apps_title": "Wybierz swoją maszynę",
        "apps": {
            "lc": {
                "tag": "Grawerki i wycinarki laserowe",
                "text": "Otwarta alternatywa dla LightBurna. Warstwy cięcia, grawerowanie liniami, wypełnieniem i obrazem z sześcioma metodami ditheringu, nakładka z kamery, podgląd ścieżek z czasem pracy i przeglądarka G-code.",
                "points": ["GRBL i Marlin przez port szeregowy lub sieć", "Zadania dla Ruida / Trocen jako PLT / DXF", "Przetestowany na laserze diodowym Sculpfun S9"],
                "shots": ["Edytor z zakładką Właściwości", "Podgląd zadania"],
                "status": "Działa na prawdziwej maszynie",
            },
            "mc": {
                "tag": "Frezarki CNC",
                "text": "Warstwy z operacją (na zewnątrz, wewnątrz, po linii, kieszeń, wiercenie) i frezem z biblioteki, podgląd materiału w 3D, grawerowanie obrazów i relief 3D, wysyłanie do GRBL z sondowaniem i makrami.",
                "points": ["Biblioteka frezów, siedem rodzajów", "Widok 3D i animowana symulacja", "Przetestowany na TwoTrees TTC450Pro"],
                "shots": ["Podgląd cięć w 3D", "Zakładka Sterowanie: pozycja, ruch, sondowanie"],
                "status": "Działa na prawdziwej maszynie",
            },
            "pc": {
                "tag": "Plotery pisakowe",
                "text": "Pisaki jako warstwy: kolor, grubość, prędkość, kontur i wypełnienie liniami. Podgląd rysowania z ruchami przy podniesionym pisaku, liczbą podniesień i czasem, porządkowanie kresek i pauza na zmianę pisaka.",
                "points": ["Podnoszenie pisaka osią Z lub serwem", "Biblioteka pisaków ze śladem każdego z nich", "Obrazy rysowane kropkami lub kreskowaniem"],
                "shots": ["Podgląd rysowania", "Pisaki jako warstwy"],
                "status": "Wczesna wersja: jeszcze nie sprawdzony na ploterze",
            },
        },
        "btn_download": "Pobierz",
        "btn_github": "Kod na GitHubie",
        "together_title": "Zbudowane razem, na baseCreator",
        "together_text": "Wszystkie trzy programy mają wspólny rdzeń, więc nowe narzędzie albo poprawka trafia do każdego z nich.",
        "features": [
            ("30 języków", "Polski, angielski, niemiecki, hiszpański, chiński, hindi, grecki i inne. Zmiana w oknie startowym."),
            ("Windows, macOS, Linux", "Instalator dla Windows, .dmg dla Apple silicon i Intela, .deb i .tar.gz dla x86_64 i ARM64."),
            ("Darmowe i otwarte", "Licencja MIT lub Apache-2.0. Bez konta, bez abonamentu, bez telemetrii."),
            ("Otwiera to, co masz", "Pliki SVG, PDF i Illustrator, bitmapy z wektoryzacją, projekty LightBurn (.lbrn2) i UGS Designer."),
            ("Wspólna galeria clipartów", "310 obrazków w 9 kategoriach, własne obrazki i wyszukiwanie w otwartych kolekcjach ikon."),
            ("Jeden plik projektu", "Projekt .cre trzyma jeden rysunek z sekcją dla każdego programu: jedną część wypalisz laserem, drugą wyfrezujesz."),
            ("Przeglądarka G-code", "Otwórz dowolny plik G-code z okna startowego, bez projektu: płasko lub w 3D, z ruchami jałowymi, kolorem wg wysokości, rozmiarem i czasem."),
            ("Kostka nawigacyjna", "Kliknij ścianę, krawędź lub narożnik kostki w widoku 3D, żeby spojrzeć stamtąd, tak jak we FreeCAD."),
            ("Sterowanie maszyną", "Ruch osiami, sondowanie, start od wybranej linii, makra, ustawienia firmware i kalibracja, przez port szeregowy lub sieć."),
        ],
        "plugins_title": "Wtyczki",
        "plugins_text": "Generatory, importery i postprocesory G-code instalujesz jednym kliknięciem z oficjalnej listy: Ustawienia → Wtyczki… → Oficjalne wtyczki. Każda działa w piaskownicy i we wszystkich programach, które mogą jej użyć.",
        "plugins_list": ["Płytki PCB z KiCad, Gerber, EAGLE i EasyEDA", "Pudełka na wczepy do lasera", "Siatki brył do wycięcia z kartonu", "Fraktale, koła zębate, otwory na okręgu", "Rzut STL, pliki punktów x,y"],
        "plugins_btn": "Zobacz wszystkie wtyczki",
        "dl_title": "Pobierz",
        "dl_text": "Każde wydanie ma gotowe paczki. Wybierz program i system; link prowadzi do najnowszej wersji.",
        "dl_cols": ["Windows", "macOS", "Linux"],
        "dl_win": "Instalator (.exe)",
        "dl_mac": "Apple silicon / Intel (.dmg)",
        "dl_linux": ".deb / .tar.gz",
        "dl_note": "macOS: programy nie są jeszcze notaryzowane, więc za pierwszym razem otwórz je przez prawy klik → Otwórz. Pobrane pliki sprawdzisz z SHA256SUMS.txt. Każdy program można też zbudować ze źródeł w Rust.",
        "dl_safety": "Laser i frezarka są niebezpieczne. Każde nowe zadanie najpierw sprawdź w powietrzu i nigdy nie zostawiaj pracującej maszyny bez nadzoru.",
        "support_title": "Wesprzyj projekt",
        "support_text": "Programy Creator powstają po godzinach, robi je jedna osoba i są darmowe dla wszystkich. Jeśli oszczędzają ci czas albo pieniądze, możesz postawić mi kawę. Dziękuję!",
        "support_other_title": "Inne sposoby pomocy",
        "support_other": [
            ("Daj gwiazdkę repozytoriom", "dzięki temu inni łatwiej znajdą programy"),
            ("Zgłaszaj błędy i pomysły", "w zakładce Issues każdego repozytorium"),
            ("Przetestuj na swojej maszynie", "i opisz wynik, zwłaszcza plotery i Marlin"),
            ("Popraw tłumaczenie", "albo dodaj cliparty i materiały"),
        ],
        "footer": "Autor: Michał Sarna · MIT lub Apache-2.0",
    },
}

CHECK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20 6 9 17l-5-5"/></svg>'
ICONS = {
    0: '<path d="m5 8 6 6"/><path d="m4 14 6-6 2-3"/><path d="M2 5h12"/><path d="M7 2h1"/><path d="m22 22-5-10-5 10"/><path d="M14 18h6"/>',
    1: '<rect x="2" y="3" width="20" height="14" rx="2"/><path d="M8 21h8"/><path d="M12 17v4"/>',
    2: '<path d="M12 2a10 10 0 1 0 0 20 10 10 0 0 0 0-20Z"/><path d="M9 12l2 2 4-4"/>',
    3: '<path d="M14.5 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V7.5Z"/><path d="M14 2v6h6"/><path d="M12 18v-6"/><path d="m9 15 3 3 3-3"/>',
    4: '<rect x="3" y="3" width="18" height="18" rx="2"/><circle cx="9" cy="9" r="2"/><path d="m21 15-3-3-9 9"/>',
    6: '<path d="M2 12s3.6-7 10-7 10 7 10 7-3.6 7-10 7S2 12 2 12Z"/><circle cx="12" cy="12" r="3"/>',
    7: '<path d="M21 8 12 3 3 8v8l9 5 9-5Z"/><path d="m3 8 9 5 9-5"/><path d="M12 13v8"/>',
    8: '<circle cx="12" cy="12" r="9"/><path d="m12 7 3 3h-2v4h2l-3 3-3-3h2v-4H9Z"/>',
    5: '<path d="M12 2 2 7l10 5 10-5-10-5Z"/><path d="m2 17 10 5 10-5"/><path d="m2 12 10 5 10-5"/>',
}


def json_ld(lang):
    """Structured data for search engines: the three programs as free software applications."""
    t = T[lang]
    apps = [
        {
            "@type": "SoftwareApplication",
            "name": repo,
            "description": t["apps"][aid]["text"],
            "applicationCategory": "DesignApplication",
            "operatingSystem": "Windows, macOS, Linux",
            "softwareVersion": VERSIONS[repo].lstrip("v"),
            "url": GH + repo,
            "downloadUrl": f"{GH}{repo}/releases/latest",
            "license": ["https://opensource.org/license/mit", "https://www.apache.org/licenses/LICENSE-2.0"],
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "EUR"},
            "author": {"@type": "Person", "name": "Michał Sarna"},
        }
        for aid, repo, _, _ in APPS
    ]
    return json.dumps({"@context": "https://schema.org", "@graph": apps}, ensure_ascii=False, indent=1).replace("</", "<\\/")


def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def page(lang):
    t = T[lang]
    up = "../" if t["path"] else ""
    other_href = (up + T[t["other"]]["path"]) or "./"
    nav_ids = ["apps", "together", "plugins", "download", "support"]
    nav = "".join(f'<a href="#{i}">{esc(n)}</a>' for i, n in zip(nav_ids, t["nav"]))

    cards = []
    for i, (aid, repo, icon, shots) in enumerate(APPS):
        a = t["apps"][aid]
        early = " early" if aid == "pc" else ""
        pts = "".join(f"<li>{CHECK}{esc(p)}</li>" for p in a["points"])
        figs = "".join(
            f'<figure><img src="{up}img/{s}.webp" alt="{esc(cap)}" width="1280" height="800" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>'
            for s, cap in zip(shots, a["shots"])
        )
        cards.append(f"""
      <article class="app app-{aid}" id="{repo.lower()}">
        <div class="app-text">
          <header>
            <img src="{up}img/{icon}.png" alt="" width="64" height="64">
            <div><h3>{repo}</h3><p class="tag">{esc(a["tag"])}</p></div>
          </header>
          <span class="status{early}">{esc(a["status"])}</span> <span class="ver">{VERSIONS[repo]}</span>
          <p>{esc(a["text"])}</p>
          <ul class="checks">{pts}</ul>
          <div class="actions">
            <a class="btn primary" href="{GH}{repo}/releases/latest">{esc(t["btn_download"])}</a>
            <a class="btn" href="{GH}{repo}">{esc(t["btn_github"])}</a>
          </div>
        </div>
        <div class="shots">{figs}</div>
      </article>""")

    feats = "".join(
        f'<div class="feat"><svg viewBox="0 0 24 24" aria-hidden="true">{ICONS[i]}</svg><h3>{esc(h)}</h3><p>{esc(p)}</p></div>'
        for i, (h, p) in enumerate(t["features"])
    )
    plist = "".join(f"<li>{CHECK}{esc(p)}</li>" for p in t["plugins_list"])
    rows = "".join(
        f"""<tr><th scope="row"><img src="{up}img/{icon}.png" alt="" width="28" height="28">{repo} <span class="ver">{VERSIONS[repo]}</span></th>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_win"])}</a></td>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_mac"])}</a></td>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_linux"])}</a></td></tr>"""
        for _, repo, icon, _ in APPS
    )
    th = "".join(f'<th scope="col">{c}</th>' for c in t["dl_cols"])
    other = "".join(f"<li><strong>{esc(h)}</strong> {esc(p)}</li>" for h, p in t["support_other"])
    url = BASE + t["path"]

    return f"""<!doctype html>
<html lang="{t["html_lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(t["title"])}</title>
<meta name="description" content="{esc(t["desc"])}">
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="en" href="{BASE}">
<link rel="alternate" hreflang="pl" href="{BASE}pl/">
<link rel="alternate" hreflang="x-default" href="{BASE}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(t["title"])}">
<meta property="og:description" content="{esc(t["desc"])}">
<meta property="og:image" content="{BASE}img/og.jpg">
<meta property="og:locale" content="{"pl_PL" if lang == "pl" else "en_US"}">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#1f2125">
<link rel="icon" href="{up}img/favicon.png">
<script type="application/ld+json">{json_ld(lang)}</script>
<link rel="stylesheet" href="{up}style.css">
<script>try{{localStorage.setItem("creatorapps-lang","{lang}")}}catch(e){{}}</script>
</head>
<body>
<a class="skip" href="#main">{esc(t["skip"])}</a>
<header class="top">
  <div class="wrap bar">
    <a class="brand" href="./"><img src="{up}img/basecreator.png" alt="" width="32" height="32">Creator Apps</a>
    <nav>{nav}</nav>
    <a class="lang" href="{other_href}" hreflang="{t["other"]}" lang="{t["other"]}">{t["other_label"]}</a>
  </div>
</header>

<main id="main">
  <section class="hero">
    <div class="wrap">
      <p class="kicker">{esc(t["hero_kicker"])}</p>
      <h1>{t["hero_title"]}</h1>
      <p class="lead">{esc(t["hero_text"])}</p>
      <div class="actions">
        <a class="btn primary big" href="#download">{esc(t["cta_download"])}</a>
        <a class="btn coffee big" href="{BMC}">☕ {esc(t["cta_support"])}</a>
      </div>
      <div class="trio">
        <a href="#lightcreator"><img src="{up}img/lightcreator.png" alt="" width="72" height="72"><span>LightCreator</span></a>
        <a href="#millcreator"><img src="{up}img/millcreator.png" alt="" width="72" height="72"><span>MillCreator</span></a>
        <a href="#pencreator"><img src="{up}img/pencreator.png" alt="" width="72" height="72"><span>PenCreator</span></a>
      </div>
    </div>
  </section>

  <section id="apps" class="wrap">
    <h2>{esc(t["apps_title"])}</h2>{"".join(cards)}
  </section>

  <section id="together" class="band">
    <div class="wrap">
      <h2>{esc(t["together_title"])}</h2>
      <p class="sub">{esc(t["together_text"])}</p>
      <div class="feats">{feats}</div>
    </div>
  </section>

  <section id="plugins" class="wrap split">
    <div>
      <h2>{esc(t["plugins_title"])}</h2>
      <p>{esc(t["plugins_text"])}</p>
      <a class="btn" href="{PLUGINS}">{esc(t["plugins_btn"])}</a>
    </div>
    <ul class="checks">{plist}</ul>
  </section>

  <section id="download" class="band">
    <div class="wrap">
      <h2>{esc(t["dl_title"])}</h2>
      <p class="sub">{esc(t["dl_text"])}</p>
      <div class="table"><table><thead><tr><td></td>{th}</tr></thead><tbody>{rows}</tbody></table></div>
      <p class="note">{esc(t["dl_note"])}</p>
      <p class="note warn">⚠️ {esc(t["dl_safety"])}</p>
    </div>
  </section>

  <section id="support" class="wrap split">
    <div class="coffee-box">
      <h2>{esc(t["support_title"])}</h2>
      <p>{esc(t["support_text"])}</p>
      <a class="btn coffee big" href="{BMC}">☕ buymeacoffee.com/michalsarna</a>
    </div>
    <div>
      <h3>{esc(t["support_other_title"])}</h3>
      <ul class="plain">{other}</ul>
    </div>
  </section>
</main>

<footer class="wrap foot">
  <span>{esc(t["footer"])}</span>
  <span><a href="{GH}LightCreator">LightCreator</a> · <a href="{GH}MillCreator">MillCreator</a> · <a href="{GH}PenCreator">PenCreator</a> · <a href="{GH}baseCreator">baseCreator</a> · <a href="{BMC}">Buy Me a Coffee</a></span>
</footer>
</body>
</html>
"""


if __name__ == "__main__":
    for lang in T:
        out = ROOT / T[lang]["path"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        html = page(lang)
        if lang == "en":
            # first visit from a Polish browser goes to the Polish page; a choice made later is kept
            html = html.replace(
                '<script>try{localStorage.setItem("creatorapps-lang","en")}catch(e){}</script>',
                '<script>try{var s=localStorage.getItem("creatorapps-lang");'
                'if(!s&&/^pl\\b/i.test(navigator.language||"")){location.replace("pl/")}'
                'else{localStorage.setItem("creatorapps-lang","en")}}catch(e){}</script>',
            )
        out.write_text(html, encoding="utf-8")
        print("wrote", out.relative_to(ROOT))

    # For search engines: both languages, each pointing at the other.
    urls = "".join(
        f"""  <url>
    <loc>{BASE}{T[lang]["path"]}</loc>
    <xhtml:link rel="alternate" hreflang="en" href="{BASE}"/>
    <xhtml:link rel="alternate" hreflang="pl" href="{BASE}pl/"/>
  </url>
"""
        for lang in T
    )
    (ROOT / "sitemap.xml").write_text(
        f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">
{urls}</urlset>
""",
        encoding="utf-8",
    )
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}sitemap.xml\n", encoding="utf-8")
    print("wrote sitemap.xml, robots.txt")
