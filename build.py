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
DRAWING_ROBOT = "https://www.printables.com/model/137296-drawing-robot-arduino-uno-cnc-shield-grbl"

APPS = [
    # id, repo, icon, screenshots
    ("lc", "LightCreator", "lightcreator", ["lc-editor", "lc-preview"]),
    ("mc", "MillCreator", "millcreator", ["mc-3d", "mc-control"]),
    ("pc", "PenCreator", "pencreator", ["pc-plot", "pc-layers"]),
    ("bc", "baseCreator", "basecreator", ["bc-editor", "bc-page"]),
]

# The name of a program, where it differs from the name of its repository.
NAMES = {"baseCreator": "BaseCreator"}


def name_of(repo):
    return NAMES.get(repo, repo)


T = {
    "en": {
        "html_lang": "en",
        "path": "",
        "other": "pl",
        "other_label": "Polski",
        "skip": "Skip to content",
        "title": "Creator Apps · free software for lasers, CNC mills and pen plotters",
        "desc": "LightCreator, MillCreator and PenCreator: free, open-source design and G-code software for laser engravers, CNC mills and pen plotters, and BaseCreator for drawing without a machine. Windows, macOS and Linux, 30 languages.",
        "nav": ["Apps", "Together", "Plugins", "Download", "Support"],
        "hero_kicker": "Free · open source · Windows, macOS, Linux",
        "hero_title": "One family of programs for your <em>laser</em>, <em>CNC mill</em> and <em>pen plotter</em>",
        "hero_text": "Design or import a drawing, give every layer a job, look at the result in the preview and send G-code to the machine. The same window, the same tools and the same shortcuts in all the programs. No machine? BaseCreator is the same editor for drawing alone.",
        "cta_download": "Download",
        "cta_support": "Buy me a coffee",
        "apps_title": "Pick your program",
        "apps": {
            "lc": {
                "tag": "Laser engravers and cutters",
                "text": "An open-source program for laser engravers and cutters. Cut layers, line, fill and image engraving with six dithering methods, a camera overlay, a toolpath preview with the time of the job and a G-code viewer.",
                "points": ["GRBL (0.7 to 1.1 and newer) and Marlin over a serial port or the network", "Ruida / Trocen jobs as PLT / DXF", "Tested on a Sculpfun S9 diode laser"],
                "shots": ["The editor with the Properties tab", "The preview of a job"],
            },
            "mc": {
                "tag": "CNC milling machines",
                "text": "Layers with an operation (outside, inside, on the line, pocket, drill) and a bit from the library, a 3D preview of the material, picture engraving and 3D relief, streaming to GRBL (0.7 to 1.1 and newer) with probing and macros.",
                "points": ["Bit library with seven kinds of bits", "3D view and an animated simulation", "Tested on a TwoTrees TTC450Pro"],
                "shots": ["The 3D preview of the cuts", "The Control tab: START / STOP, position, jogging"],
            },
            "pc": {
                "tag": "Pen plotters",
                "text": "Pens as layers: colour, width, speed, outline and fill lines. A plot preview with the pen-up moves, the number of lifts and the time, stroke ordering to shorten the moves, and a pause to change the pen.",
                "points": ["Z axis or a servo pen lift, GRBL 0.7 to 1.1 and newer, AxiDraw / EggBot and HPGL plotters", "Pen library with the mark each pen makes", "Pictures drawn with dots or hatching", ("Tested on a pen plotter built after the ", "Drawing Robot", DRAWING_ROBOT, " (Arduino UNO, CNC Shield, GRBL)")],
                "shots": ["The plot preview", "Pens as layers"],
            },
            "bc": {
                "tag": "Drawing, with no machine",
                "text": "The same editor without devices, G-code or a camera, with a page in place of a work area. It writes the same project files, so a drawing made here can be finished for a machine in the other programs.",
                "points": ["A page of your own: A5 to A1, Letter, Legal or any size", "The same import and export lists as the other programs", "Plugins that make shapes and read files work here too"],
                "shots": ["The editor with the Layers tab", "Page setup"],
                "status": "Drawing only",
            },
        },
        "btn_download": "Download",
        "btn_github": "Source on GitHub",
        "together_title": "Built together, on baseCreator",
        "together_text": "All four programs share one core, so a new tool or fix lands in every one of them.",
        "features": [
            ("30 languages", "Polish, English, German, Spanish, Chinese, Hindi, Greek and more. Switch in the start window."),
            ("Windows, macOS, Linux", "Installers for Windows, .dmg for Apple silicon and Intel, .deb and .tar.gz for x86_64 and ARM64."),
            ("Free and open", "MIT or Apache-2.0. No account, no subscription, no telemetry."),
            ("The same files everywhere", "Every program reads and writes the files of LightBurn and MillMage (.lbrn2, .lbrn, .mage), DXF (current and R12), Illustrator and SVG with pictures; it also imports PDF, bitmaps with tracing and UGS Designer designs, and exports PLT."),
            ("A shared clipart gallery", "310 pictures in 9 categories, your own pictures and online search of open icon collections."),
            ("One project file", "A .cre project keeps one drawing with a section for every program, so you can laser a part and mill another."),
            ("A G-code viewer", "Open any G-code file from the start window, without a project: flat or in 3D, with travel moves, colour by height, size and time."),
            ("A navigation cube", "Click a face, an edge or a corner of the cube in a 3D view to look from there, the same as in FreeCAD."),
            ("Control the machine", "Jogging, probing, start from a line, macros, the firmware settings and calibration, over a serial port or the network."),
            ("Tabs of drawings", "Open up to 10 drawings at once, each in its own tab. Ctrl+1…9 switches, Ctrl+W closes, and on exit every unsaved tab is asked about, each with its own recovery file."),
            ("The same Control tab", "Home, Unlock, Pause and Resume, START and STOP, jogging and speed look and work the same in the laser, the mill and the plotter."),
            ("Trace the work first", "Go round the job before you start it: the box in every program, and in LightCreator also the line that wraps all the shapes, like a rubber band."),
            ("One element at a time", "Burn, cut or draw each element completely, all its layers and passes, before the next one, or only what you have selected: two switches in the Control tab."),
            ("The camera beside your drawing", "The live camera view (also an RTSP stream) as a tab next to your drawings, fitted to the window, or in a window of its own, with photos, video and a time-lapse every N seconds or after each layer, into a folder you choose."),
            ("Pen change at a place of the machine", "PenCreator drives to the place where the pen is changed, runs the G-code of your mechanism and stops there."),
            ("The milled piece in 3D", "MillCreator shows the material as it will be milled, with the real shape of every bit (on a cylinder when a rotary attachment is chosen), and saves it as an STL model. Own G-code and a work coordinate system (G54 to G59) are in the device settings."),
            ("Preview as a tab", "Pin the preview next to your drawings, in every program, or let it float. Plugins with settings, like the G-code tools, get a tab of their own."),
            ("Levels for pictures", "A histogram with a black and a white point when you import or adjust a picture, and a trace dialog that zooms in on the outlines."),
            ("Print the drawing", "Print it on a paper printer, to scale or as large as the page allows, to check the placement or use it as a template. Or save it as a PDF."),
            ("A quick guide", "Help → Quick guide, or F1, explains the program step by step, in English and Polish."),
            ("A picture under the drawing", "Put a photo under the drawing and line it up with the material. LightCreator, MillCreator and PenCreator can also show the live picture of a camera. The project keeps the picture."),
            ("USB keyboards and pads", "Drive the machine with a pad or the keyboard: moves while you hold a key, Stop, Home, and the spindle, air, water, laser beam or pen, on the keys you choose. One device can serve many machines, and only the window in front listens."),
            ("The project on the material", "In MillCreator's 3D view the shapes of the drawing can lie on top of the material, in the colours of their layers, so you can compare them with what the bit will cut."),
            ("Superman, Batman and Joker", "Three new colour schemes for the window, with Joker in a dark and a light version, 18 in all."),
            ("AxiDraw, EggBot and HPGL plotters", "PenCreator also drives plotters that do not speak G-code: the AxiDraw and the EggBot (EiBotBoard) and HPGL plotters on a serial port."),
            ("Paste a picture", "Ctrl+V with a screenshot or a picture copied from a browser opens the import window, with its levels, zoom and size."),
            ("Keys for the nodes", "In node editing D deletes, I inserts, L and S make a line or a curve, C a corner, R rounds and B breaks; a node dropped onto another joins them."),
            ("Cut with a drag knife", "PenCreator and MillCreator cut vinyl, paper, card and rubber with a drag knife: the offset of the tip is made good at every corner, the holes are cut first and every closed outline closes."),
            ("A knife library", "Ready-made 30°, 45° and 60° blades and a drag knife in a holder of a CNC machine, and knives of your own with their offset, corners, overcut and notes, kept with your settings."),
            ("HPGL cutters their own way", "Every HPGL plotter or cutter gets its own commands, on a page of the device that only such devices have: the start and the end, knife down and up, the speed with a top limit and the force."),
            ("Style trace", "Draw a picture again as lines in one of 19 styles, to burn, mill or plot: squiggles, a spiral, waves, halftone circles, etching, line art, a sketch and more, with a live preview."),
            ("Stippling and one line", "Dots spread by the tone of the picture, or the same dots joined into one continuous line that never crosses itself, drawn without lifting the pen."),
            ("Flow lines and hatching", "Long lines that flow along the shapes of the picture, closer together in the shadows, or hatching in layers like an old engraving."),
            ("A panel for each camera", "The Recording tab has a panel for every camera of the machine, named after it: photo, video and time-lapse, each camera on its own with its own settings and folder."),
            ("Time-lapse with the head out of the way", "LightCreator, MillCreator and PenCreator move the head aside for every picture of a time-lapse, take it, come back and go on with the job. A mill waits for its next lift, and can take a picture at every lift."),
            ("Long lines in parts", "Long straight cuts can be sent as 2 to 256 shorter lines, so a job stops sooner for a photo or a pause and its progress moves evenly. The path stays the same."),
        ],
        "plugins_title": "Plugins",
        "plugins_text": "Install generators, importers and G-code postprocessors from the official list with one click: Settings → Plugins… → Official plugins. Each one runs in a sandbox and works in every program that can use it.",
        "plugins_list": ["Circuit boards from KiCad, Gerber, EAGLE and EasyEDA", "Boxes with finger joints for a laser", "Nets of boxes to cut out of card", "Fractals, gears, holes on a circle", "Barcodes, x,y point files", "Postprocessors: line numbers, Mach3 / Mach4 / UCCNC, LinuxCNC"],
        "plugins_btn": "See all plugins",
        "dl_pkg_title": "Or with a package manager",
        "dl_pkg_rows": [
            ("macOS · Homebrew", "brew install --cask michalsarna/tap/lightcreator"),
            ("Windows · Scoop", "scoop bucket add creator https://github.com/michalsarna/scoop-bucket"),
            ("Windows · Scoop", "scoop install lightcreator"),
        ],
        "dl_pkg_note": "Use millcreator, pencreator or basecreator in place of lightcreator for the other programs. The same commands update to every new release. winget (MichalSarna.LightCreator and the others) follows once Microsoft has accepted the packages.",
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
        "desc": "LightCreator, MillCreator i PenCreator: darmowe programy open source do projektowania i G-code dla grawerek laserowych, frezarek CNC i ploterów pisakowych, oraz BaseCreator do rysowania bez maszyny. Windows, macOS i Linux, 30 języków.",
        "nav": ["Programy", "Wspólne", "Wtyczki", "Pobierz", "Wesprzyj"],
        "hero_kicker": "Za darmo · open source · Windows, macOS, Linux",
        "hero_title": "Jedna rodzina programów do <em>lasera</em>, <em>frezarki CNC</em> i <em>plotera</em>",
        "hero_text": "Narysuj lub zaimportuj projekt, przypisz każdej warstwie zadanie, obejrzyj wynik w podglądzie i wyślij G-code do maszyny. To samo okno, te same narzędzia i te same skróty we wszystkich programach. Nie masz maszyny? BaseCreator to ten sam edytor do samego rysowania.",
        "cta_download": "Pobierz",
        "cta_support": "Postaw mi kawę",
        "apps_title": "Wybierz swój program",
        "apps": {
            "lc": {
                "tag": "Grawerki i wycinarki laserowe",
                "text": "Otwartoźródłowy program do grawerek i wycinarek laserowych. Warstwy cięcia, grawerowanie liniami, wypełnieniem i obrazem z sześcioma metodami ditheringu, nakładka z kamery, podgląd ścieżek z czasem pracy i przeglądarka G-code.",
                "points": ["GRBL (od 0.7 do 1.1 i nowszych) i Marlin przez port szeregowy lub sieć", "Zadania dla Ruida / Trocen jako PLT / DXF", "Przetestowany na laserze diodowym Sculpfun S9"],
                "shots": ["Edytor z zakładką Właściwości", "Podgląd zadania"],
            },
            "mc": {
                "tag": "Frezarki CNC",
                "text": "Warstwy z operacją (na zewnątrz, wewnątrz, po linii, kieszeń, wiercenie) i frezem z biblioteki, podgląd materiału w 3D, grawerowanie obrazów i relief 3D, wysyłanie do GRBL (od 0.7 do 1.1 i nowszych) z sondowaniem i makrami.",
                "points": ["Biblioteka frezów, siedem rodzajów", "Widok 3D i animowana symulacja", "Przetestowany na TwoTrees TTC450Pro"],
                "shots": ["Podgląd cięć w 3D", "Zakładka Sterowanie: START / STOP, pozycja, ruch"],
            },
            "pc": {
                "tag": "Plotery pisakowe",
                "text": "Pisaki jako warstwy: kolor, grubość, prędkość, kontur i wypełnienie liniami. Podgląd rysowania z ruchami przy podniesionym pisaku, liczbą podniesień i czasem, porządkowanie kresek i pauza na zmianę pisaka.",
                "points": ["Podnoszenie pisaka osią Z lub serwem, GRBL od 0.7 do 1.1 i nowszych, plotery AxiDraw / EggBot i HPGL", "Biblioteka pisaków ze śladem każdego z nich", "Obrazy rysowane kropkami lub kreskowaniem", ("Testowany na ploterze zbudowanym na wzór ", "Drawing Robot", DRAWING_ROBOT, " (Arduino UNO, CNC Shield, GRBL)")],
                "shots": ["Podgląd rysowania", "Pisaki jako warstwy"],
            },
            "bc": {
                "tag": "Rysowanie, bez maszyny",
                "text": "Ten sam edytor bez urządzeń, G-code i kamery, ze stroną zamiast pola roboczego. Zapisuje te same pliki projektu, więc rysunek zrobiony tutaj można przygotować dla maszyny w pozostałych programach.",
                "points": ["Własna strona: od A5 do A1, Letter, Legal lub dowolny rozmiar", "Te same listy importu i eksportu co w pozostałych programach", "Wtyczki tworzące kształty i czytające pliki działają także tutaj"],
                "shots": ["Edytor z kartą Warstwy", "Ustawienia strony"],
                "status": "Tylko rysowanie",
            },
        },
        "btn_download": "Pobierz",
        "btn_github": "Kod na GitHubie",
        "together_title": "Zbudowane razem, na baseCreator",
        "together_text": "Wszystkie cztery programy mają wspólny rdzeń, więc nowe narzędzie albo poprawka trafia do każdego z nich.",
        "features": [
            ("30 języków", "Polski, angielski, niemiecki, hiszpański, chiński, hindi, grecki i inne. Zmiana w oknie startowym."),
            ("Windows, macOS, Linux", "Instalator dla Windows, .dmg dla Apple silicon i Intela, .deb i .tar.gz dla x86_64 i ARM64."),
            ("Darmowe i otwarte", "Licencja MIT lub Apache-2.0. Bez konta, bez abonamentu, bez telemetrii."),
            ("Te same pliki wszędzie", "Każdy program czyta i zapisuje pliki LightBurna i MillMage'a (.lbrn2, .lbrn, .mage), DXF (obecny i R12), Illustratora oraz SVG z obrazami; importuje też PDF, bitmapy z wektoryzacją i projekty UGS Designer, a eksportuje PLT."),
            ("Wspólna galeria clipartów", "310 obrazków w 9 kategoriach, własne obrazki i wyszukiwanie w otwartych kolekcjach ikon."),
            ("Jeden plik projektu", "Projekt .cre trzyma jeden rysunek z sekcją dla każdego programu: jedną część wypalisz laserem, drugą wyfrezujesz."),
            ("Przeglądarka G-code", "Otwórz dowolny plik G-code z okna startowego, bez projektu: płasko lub w 3D, z ruchami jałowymi, kolorem wg wysokości, rozmiarem i czasem."),
            ("Kostka nawigacyjna", "Kliknij ścianę, krawędź lub narożnik kostki w widoku 3D, żeby spojrzeć stamtąd, tak jak we FreeCAD."),
            ("Sterowanie maszyną", "Ruch osiami, sondowanie, start od wybranej linii, makra, ustawienia firmware i kalibracja, przez port szeregowy lub sieć."),
            ("Zakładki rysunków", "Do 10 rysunków naraz, każdy w osobnej zakładce. Ctrl+1…9 przełącza, Ctrl+W zamyka, a przy wyjściu program pyta o każdą niezapisaną zakładkę i trzyma dla niej osobny plik odzyskiwania."),
            ("Ta sama zakładka Sterowanie", "Home, Unlock, Pause i Resume, START i STOP, ruch i prędkość wyglądają i działają tak samo w laserze, frezarce i ploterze."),
            ("Obrysuj pracę przed startem", "Obejdź zadanie, zanim je uruchomisz: prostokąt w każdym programie, a w LightCreatorze także linię otaczającą wszystkie kształty, jak gumka."),
            ("Element po elemencie", "Wypalaj, wycinaj lub rysuj każdy element w całości, ze wszystkimi warstwami i przejściami, zanim zacznie się następny, albo tylko to, co zaznaczysz: dwa przełączniki w zakładce Sterowanie."),
            ("Kamera obok rysunku", "Obraz z kamery na żywo (także strumień RTSP) jako karta obok rysunków, dopasowany do okna, albo w osobnym oknie, ze zdjęciami, wideo i poklatkowym co N sekund lub po każdej warstwie, do wybranego katalogu."),
            ("Zmiana pisaka w miejscu maszyny", "PenCreator jedzie w miejsce zmiany pisaka, wykonuje G-code Twojego mechanizmu i zatrzymuje się tam."),
            ("Sfrezowany element w 3D", "MillCreator pokazuje materiał tak, jak zostanie sfrezowany, z prawdziwym kształtem każdego freza (na walcu, gdy wybrana jest przystawka obrotowa), i zapisuje go jako model STL. Własny G-code i układ współrzędnych roboczych (G54 do G59) są w ustawieniach urządzenia."),
            ("Podgląd jako karta", "Przypnij podgląd obok rysunków, w każdym programie, albo zostaw go w oknie. Wtyczki z ustawieniami, jak G-code tools, mają własną kartę."),
            ("Poziomy dla obrazów", "Histogram z punktem czerni i bieli przy imporcie i korekcie obrazu oraz okno trace, które przybliża kontury."),
            ("Wydruk rysunku", "Wydrukuj go na zwykłej drukarce, w skali albo tak duży, jak pozwala strona, żeby sprawdzić położenie albo użyć go jako szablonu. Możesz też zapisać PDF."),
            ("Krótki przewodnik", "Pomoc → Krótki przewodnik albo F1 objaśnia program krok po kroku, po polsku i po angielsku."),
            ("Obraz pod rysunkiem", "Podłóż zdjęcie pod rysunek i dopasuj je do materiału. LightCreator, MillCreator i PenCreator mogą też pokazać obraz na żywo z kamery. Projekt zachowuje obraz."),
            ("Klawiatury i pady USB", "Steruj maszyną padem albo klawiaturą: ruch, dopóki trzymasz klawisz, Stop, bazowanie oraz wrzeciono, powietrze, woda, wiązka lasera albo pisak na wybranych klawiszach. Jedno urządzenie może obsługiwać wiele maszyn, a naciśnięcia odbiera tylko okno na wierzchu."),
            ("Projekt na materiale", "W widoku 3D MillCreatora kształty rysunku mogą leżeć na wierzchu materiału, w kolorach warstw, żeby porównać je z tym, co wytnie frez."),
            ("Superman, Batman i Joker", "Trzy nowe schematy kolorów okna, a Joker w wersji ciemnej i jasnej. Razem jest ich 18."),
            ("Plotery AxiDraw, EggBot i HPGL", "PenCreator steruje też ploterami, które nie mówią G-code: AxiDraw i EggBot (EiBotBoard) oraz plotery HPGL na porcie szeregowym."),
            ("Wklejanie obrazu", "Ctrl+V ze zrzutem ekranu albo obrazem skopiowanym z przeglądarki otwiera okno importu z poziomami, powiększeniem i rozmiarem."),
            ("Klawisze węzłów", "W edycji węzłów D usuwa, I wstawia, L i S robią linię albo krzywą, C narożnik, R zaokrągla, a B rozdziela; węzeł upuszczony na inny łączy się z nim."),
            ("Cięcie nożem wleczonym", "PenCreator i MillCreator tną folię, papier, karton i gumę nożem wleczonym: przesunięcie czubka jest korygowane na każdym narożu, otwory są cięte najpierw, a każdy zamknięty obrys się domyka."),
            ("Biblioteka noży", "Gotowe ostrza 30°, 45° i 60° oraz nóż wleczony w uchwycie maszyny CNC, a także własne noże z przesunięciem, narożami, docięciem i notatkami, zapisywane z ustawieniami."),
            ("Plotery tnące HPGL po swojemu", "Każdy ploter lub ploter tnący HPGL dostaje własne polecenia, na stronie urządzenia, którą mają tylko takie urządzenia: początek i koniec, opuszczenie i podniesienie noża, prędkość z górną granicą i nacisk."),
            ("Obrys w stylu", "Narysuj obraz na nowo liniami w jednym z 19 stylów, do wypalenia, frezowania lub rysowania: wężyki, spirala, fale, koła rastra, akwaforta, rysunek konturowy, szkic i inne, z podglądem na żywo."),
            ("Puentylizm i jedna linia", "Kropki rozłożone według tonu obrazu albo te same kropki połączone w jedną ciągłą linię, która się nie przecina, rysowaną bez podnoszenia pisaka."),
            ("Linie przepływu i kreskowanie", "Długie linie płynące wzdłuż kształtów obrazu, gęstsze w cieniach, albo kreskowanie warstwami jak w dawnej rycinie."),
            ("Panel dla każdej kamery", "Karta Nagrywanie ma panel dla każdej kamery maszyny, nazwany jak ona: zdjęcie, wideo i poklatkowe, każda kamera osobno, z własnymi ustawieniami i folderem."),
            ("Poklatkowe z głowicą z boku", "LightCreator, MillCreator i PenCreator odsuwają głowicę na bok do każdego zdjęcia poklatkowego, robią je, wracają i prowadzą pracę dalej. Frezarka czeka na najbliższe podniesienie i może robić zdjęcie przy każdym podniesieniu."),
            ("Długie linie w częściach", "Długie proste cięcia można wysyłać jako 2 do 256 krótszych linii, więc praca szybciej zatrzymuje się do zdjęcia lub na pauzę, a postęp rośnie równiej. Ścieżka zostaje ta sama."),
        ],
        "plugins_title": "Wtyczki",
        "plugins_text": "Generatory, importery i postprocesory G-code instalujesz jednym kliknięciem z oficjalnej listy: Ustawienia → Wtyczki… → Oficjalne wtyczki. Każda działa w piaskownicy i we wszystkich programach, które mogą jej użyć.",
        "plugins_list": ["Płytki PCB z KiCad, Gerber, EAGLE i EasyEDA", "Pudełka na wczepy do lasera", "Siatki brył do wycięcia z kartonu", "Fraktale, koła zębate, otwory na okręgu", "Kody kreskowe, pliki punktów x,y", "Postprocesory: numery linii, Mach3 / Mach4 / UCCNC, LinuxCNC"],
        "plugins_btn": "Zobacz wszystkie wtyczki",
        "dl_pkg_title": "Albo przez menedżer pakietów",
        "dl_pkg_rows": [
            ("macOS · Homebrew", "brew install --cask michalsarna/tap/lightcreator"),
            ("Windows · Scoop", "scoop bucket add creator https://github.com/michalsarna/scoop-bucket"),
            ("Windows · Scoop", "scoop install lightcreator"),
        ],
        "dl_pkg_note": "Dla pozostałych programów wpisz millcreator, pencreator lub basecreator zamiast lightcreator. Te same polecenia aktualizują do każdego nowego wydania. winget (MichalSarna.LightCreator i pozostałe) pojawi się, gdy Microsoft przyjmie pakiety.",
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
    9: '<path d="M3 7a2 2 0 0 1 2-2h4l2 2h8a2 2 0 0 1 2 2v8a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2Z"/><path d="M3 11h18"/>',
    10: '<rect x="3" y="3" width="18" height="18" rx="2"/><path d="M3 12h18"/><path d="M12 3v18"/>',
    11: '<path d="M3 3h18v18H3Z" stroke-dasharray="3 3"/><path d="m9 12 2 2 4-4"/>',
    12: '<rect x="3" y="3" width="7" height="7" rx="1"/><rect x="14" y="3" width="7" height="7" rx="1"/><rect x="3" y="14" width="7" height="7" rx="1"/><path d="m14 17 2 2 5-5"/>',
    13: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3Z"/><circle cx="12" cy="13" r="3"/>',
    14: '<path d="m12 19 7-7 3 3-7 7-3-3Z"/><path d="m18 13-1.5-7.5L2 2l3.5 14.5L13 18l5-5Z"/><path d="m2 2 7.6 7.6"/><circle cx="11" cy="11" r="2"/>',
    15: '<path d="M21 8 12 3 3 8v8l9 5 9-5Z"/><path d="M3 8l9 5 9-5"/><path d="M12 13v8"/><path d="M8 11l-2-1"/>',
    16: '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 9h18"/><path d="M8 4v5"/>',
    17: '<path d="M3 3v18h18"/><path d="M7 17v-4"/><path d="M11 17V8"/><path d="M15 17v-6"/><path d="M19 17V5"/>',
    18: '<path d="M6 9V2h12v7"/><path d="M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
    19: '<path d="M2 3h6a4 4 0 0 1 4 4v14a3 3 0 0 0-3-3H2Z"/><path d="M22 3h-6a4 4 0 0 0-4 4v14a3 3 0 0 1 3-3h7Z"/>',
    20: '<path d="M4 5h16v14H4Z" stroke-dasharray="3 3"/><path d="m8 15 3-4 2 2 2-3 3 5"/><circle cx="9" cy="9" r="1"/>',
    21: '<line x1="6" x2="10" y1="12" y2="12"/><line x1="8" x2="8" y1="10" y2="14"/><line x1="15" x2="15.01" y1="13" y2="13"/><line x1="18" x2="18.01" y1="11" y2="11"/><rect x="2" y="6" width="20" height="12" rx="2"/>',
    22: '<path d="m12 2 10 5-10 5L2 7l10-5Z"/><path d="m2 12 10 5 10-5"/><path d="m2 17 10 5 10-5"/>',
    23: '<circle cx="13.5" cy="6.5" r=".5"/><circle cx="17.5" cy="10.5" r=".5"/><circle cx="8.5" cy="7.5" r=".5"/><circle cx="6.5" cy="12.5" r=".5"/><path d="M12 2a10 10 0 0 0 0 20c1.7 0 3-1.3 3-3 0-.8-.3-1.5-.8-2-.5-.5-.8-1.2-.8-2 0-1.7 1.3-3 3-3h2.4c2.3 0 4.2-1.9 4.2-4.2C23 4.3 18 2 12 2Z"/>',
    24: '<path d="M15.707 21.293a1 1 0 0 1-1.414 0l-1.586-1.586a1 1 0 0 1 0-1.414l5.586-5.586a1 1 0 0 1 1.414 0l1.586 1.586a1 1 0 0 1 0 1.414z"/><path d="m18 13-1.375-6.874a1 1 0 0 0-.746-.776L3.235 2.028a1 1 0 0 0-1.207 1.207L5.35 15.879a1 1 0 0 0 .776.746L13 18"/><path d="m2.3 2.3 7.286 7.286"/><circle cx="11" cy="11" r="2"/>',
    25: '<path d="M11 14h10"/><path d="M16 4h2a2 2 0 0 1 2 2v1.344"/><path d="m17 18 4-4-4-4"/><path d="M8 4H6a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2h12a2 2 0 0 0 1.793-1.113"/><rect x="8" y="2" width="8" height="4" rx="1"/>',
    26: '<circle cx="19" cy="5" r="2"/><circle cx="5" cy="19" r="2"/><path d="M5 17A12 12 0 0 1 17 5"/>',
    27: '<circle cx="6" cy="6" r="3"/><path d="M8.12 8.12 12 12"/><path d="M20 4 8.12 15.88"/><circle cx="6" cy="18" r="3"/><path d="M14.8 14.8 20 20"/>',
    28: '<path d="M12 7v14"/><path d="M3 18a1 1 0 0 1-1-1V4a1 1 0 0 1 1-1h5a4 4 0 0 1 4 4 4 4 0 0 1 4-4h5a1 1 0 0 1 1 1v13a1 1 0 0 1-1 1h-6a3 3 0 0 0-3 3 3 3 0 0 0-3-3z"/>',
    29: '<path d="M21 4h-7"/><path d="M10 4H3"/><path d="M21 12h-9"/><path d="M8 12H3"/><path d="M21 20h-5"/><path d="M12 20H3"/><path d="M14 2v4"/><path d="M8 10v4"/><path d="M16 18v4"/>',
    30: '<path d="m14.622 17.897-10.68-2.913"/><path d="M18.376 2.622a1 1 0 1 1 3.002 3.002L17.36 9.643a.5.5 0 0 0 0 .707l.944.944a2.41 2.41 0 0 1 0 3.408l-.944.944a.5.5 0 0 1-.707 0L8.354 7.348a.5.5 0 0 1 0-.707l.944-.944a2.41 2.41 0 0 1 3.408 0l.944.944a.5.5 0 0 0 .707 0z"/><path d="M9 8c-1.804 2.71-3.97 3.46-6.583 3.948a.507.507 0 0 0-.302.819l7.32 8.883a1 1 0 0 0 1.185.204C12.735 20.405 16 16.792 16 15"/>',
    31: '<circle cx="6" cy="6" r="1"/><circle cx="12" cy="6" r="1"/><circle cx="18" cy="6" r="1"/><circle cx="9" cy="12" r="1"/><circle cx="15" cy="12" r="1"/><circle cx="6" cy="18" r="1"/><circle cx="12" cy="18" r="1"/><circle cx="18" cy="18" r="1"/>',
    32: '<path d="M2 6c.6.5 1.2 1 2.5 1C7 7 7 5 9.5 5c2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 12c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/><path d="M2 18c.6.5 1.2 1 2.5 1 2.5 0 2.5-2 5-2 2.6 0 2.4 2 5 2 2.5 0 2.5-2 5-2 1.3 0 1.9.5 2.5 1"/>',
    33: '<path d="M14.5 4h-5L7 7H4a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h16a2 2 0 0 0 2-2V9a2 2 0 0 0-2-2h-3l-2.5-3z"/><circle cx="12" cy="13" r="3"/>',
    34: '<circle cx="12" cy="13" r="8"/><path d="M12 9v4l2 2"/><path d="M5 3 2 6"/><path d="m22 6-3-3"/>',
    35: '<path d="M3 12h3"/><path d="M9 12h2"/><path d="M14 12h2"/><path d="M19 12h2"/><circle cx="3" cy="12" r="1"/><circle cx="21" cy="12" r="1"/>',
}


def json_ld(lang):
    """Structured data for search engines: the programs as free software applications."""
    t = T[lang]
    apps = [
        {
            "@type": "SoftwareApplication",
            "name": name_of(repo),
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


def point(p):
    """A line of a card: a text, or (before, link text, url, after)."""
    if isinstance(p, str):
        return esc(p)
    before, label, url, after = p
    return f'{esc(before)}<a href="{url}">{esc(label)}</a>{esc(after)}'


def page(lang):
    t = T[lang]
    up = "../" if t["path"] else ""
    other_href = (up + T[t["other"]]["path"]) or "./"
    nav_ids = ["apps", "together", "plugins", "download", "support"]
    nav = "".join(f'<a href="#{i}">{esc(n)}</a>' for i, n in zip(nav_ids, t["nav"]))

    cards = []
    for i, (aid, repo, icon, shots) in enumerate(APPS):
        a = t["apps"][aid]
        status = f'<span class="status">{esc(a["status"])}</span> ' if a.get("status") else ""
        pts = "".join(f"<li>{CHECK}{point(p)}</li>" for p in a["points"])
        figs = "".join(
            f'<figure><img src="{up}img/{s}.webp" alt="{esc(cap)}" width="1280" height="800" loading="lazy"><figcaption>{esc(cap)}</figcaption></figure>'
            for s, cap in zip(shots, a["shots"])
        )
        cards.append(f"""
      <article class="app app-{aid}" id="{repo.lower()}">
        <div class="app-text">
          <header>
            <img src="{up}img/{icon}.png" alt="" width="64" height="64">
            <div><h3>{name_of(repo)}</h3><p class="tag">{esc(a["tag"])}</p></div>
          </header>
          {status}<span class="ver">{VERSIONS[repo]}</span>
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
        f"""<tr><th scope="row"><img src="{up}img/{icon}.png" alt="" width="28" height="28">{name_of(repo)} <span class="ver">{VERSIONS[repo]}</span></th>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_win"])}</a></td>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_mac"])}</a></td>
          <td><a href="{GH}{repo}/releases/latest">{esc(t["dl_linux"])}</a></td></tr>"""
        for _, repo, icon, _ in APPS
    )
    th = "".join(f'<th scope="col">{c}</th>' for c in t["dl_cols"])
    pkg = "".join(f'<tr><th scope="row">{esc(system)}</th><td><code>{esc(cmd)}</code></td></tr>' for system, cmd in t["dl_pkg_rows"])
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
        <a href="#basecreator"><img src="{up}img/basecreator.png" alt="" width="72" height="72"><span>BaseCreator</span></a>
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
      <h3 class="pkg">{esc(t["dl_pkg_title"])}</h3>
      <div class="table"><table><tbody>{pkg}</tbody></table></div>
      <p class="note">{esc(t["dl_pkg_note"])}</p>
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
  <span><a href="{GH}LightCreator">LightCreator</a> · <a href="{GH}MillCreator">MillCreator</a> · <a href="{GH}PenCreator">PenCreator</a> · <a href="{GH}baseCreator">BaseCreator</a> · <a href="{BMC}">Buy Me a Coffee</a></span>
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
