# PRIMER – alpaca-fair-framework.github.io

Arbeitsplan für die Landing Page des Alpaca FAIR Frameworks (`alpaca-fair-framework/alpaca-fair-framework.github.io`). Wird zu Beginn jedes Chats komplett hochgeladen und am Ende zurückgeschrieben. Teil A gilt immer, Teil B ist die Übersicht, Teil C sind die Schritte, Teil D sind offene Punkte.

---

## Teil A – Immer gültig

### A1 Ausgangslage

| Was | Wo | Rolle |
|---|---|---|
| Startseite | `index.html` | eine Seite, Englisch und Deutsch in einer Datei, Umschalter oben rechts |
| Gestaltung | `assets/site.css`, `assets/palette.css`, `assets/site.js` | Kopie aus `n4o-rse/amt-engine` (`docs/assets/`), siehe Befunde |
| Bilder | `assets/img/` | Alpaka, Pinguin (AMT), Alligator; Logos in `assets/img/logos/` |
| Schrift | `vendor/roboto/` | Roboto, lokal, SIL OFL 1.1; es wird nichts von einem Fontserver geladen |
| Prüfung | `main.py` | Schritt `check`: Links, Dateien, Sprachparität, nichts von fremden Servern |
| Schwesterseite | `https://n4o-rse.github.io/amt-engine/` | Vorbild für Layout und Abschnitt „Teil einer Familie“ |

**Befunde** (alle am 2026-10-29 geprüft):

- Das Repo war leer (`git clone` meldete „empty repository“). Der erste Patch ist deshalb der ganze Baum.
- Die AMT-Seite (`amt-engine`, Stand 0.5.0) besteht aus `docs/index.html` plus `assets/site.css`, `palette.css`, `site.js`. `palette.css` ist dort aus `design/palette.yaml` **erzeugt** („Do not edit“). Hier liegt eine unveränderte Kopie; die Farben ändern sich also nur, wenn man sie in `amt-engine` ändert und neu kopiert (siehe D2).
- `site.css` ist bis auf einen angehängten Block am Ende (verlinkte Familien-Figuren, Karten) unverändert. `site.js` unterscheidet sich nur in den beiden Speicherschlüsseln (`alpaca-theme`, `alpaca-lang`), damit Hell/Dunkel und Sprache nicht mit der AMT-Seite kollidieren.
- Der Abschnitt „Part of a family“ der AMT-Seite verlinkt weder Alpaka noch Alligator; der PRIMER von `amt-engine` (D10) hält fest, dass das bewusst so ist, weil beide in Überarbeitung sind. Für den Alligator gibt es deshalb noch keine URL.
- Die AMT-Seite nennt das Framework „Alpaka Research Framework“; das Repo heißt `alpaca-fair-framework`. Diese Seite nutzt „Alpaca FAIR Framework“ (A4).
- Die Maskottchen (Alpaka, Pinguin, Alligator) sind eigene Entwürfe des Autors, erstellt mit Google Gemini, und liegen als Pixelbilder vor.

### A2 Zielbild

```
amt-engine/docs/assets  ──(Kopie)──►  assets/  ─┐
                                                 ├─►  index.html  ──►  GitHub Pages
LEIZA / N4O-Logos, Roboto  ──(Kopie)──►  img/ ──┘      (main, Wurzel)
```

Eigenschaften der fertigen Seite, jede prüfbar:

1. Eine Seite, Kopf und Fuß wie die AMT-Seite; der Abschnitt „Part of a family“ ist der Kern.
2. Von der Seite führen Links zu **AMT.engine** (Website, Quellcode, DOI) und **AMT.runner** (Quellcode); der Alligator hat eine eigene Karte.
3. Englisch und Deutsch verlinken dieselben Ziele (`python main.py` prüft das).
4. Die Seite lädt nichts von einem fremden Server (Schrift, Skripte, Bilder liegen im Repo).
5. Zwei Läufe von `python main.py` hintereinander: gleiche Ausgabe, `git status` sauber (es wird nichts geschrieben).

### A3 Querschnittsregeln

- `PRIMER.md` ist Deutsch. Alles andere (Seite, README, CHANGELOG, Code, Kommentare) ist britisches Englisch; die Seite ist zweisprachig EN/DE.
- Windows ist die Referenzplattform. Befehle für `cmd`, je einer pro Zeile, ohne Fortsetzungszeichen.
- Kein `datetime.now()` in irgendeinem Skript; die Seite trägt ihre Version (`site 0.1.0`), kein Datum.
- Netzwerk braucht nur das Veröffentlichen. Die Prüfung läuft offline.
- Gestaltung wird kopiert, nicht verlinkt (keine Abhängigkeit zur Laufzeit von `amt-engine`).
- Ein Thema pro Chat, ein Repo pro Chat.
- Jede Änderung wird im `CHANGELOG.md` unter `[Unreleased]` vermerkt und beim Veröffentlichen mit Version und Datum versehen.

### A4 Beschlusslage

| Frage | Beschluss | seit |
|---|---|---|
| Aufbau der Seite | eine Seite, Kopf und Fuß wie AMT, Hauptteil „Part of a family“, dazu Karten für die Werkzeuge | 2026-10-29 |
| Eigener Abschnitt für die Mitglieder | ja: „Tools“ / „Werkzeuge“ mit Karten für AMT.engine, AMT.runner und Alligator; Links zu Engine und Runner auch in Kopfleiste und Familien-Figur | 2026-10-29 |
| Sprache | Englisch und Deutsch in einer Datei, Umschalter wie bei AMT | 2026-10-29 |
| Name auf der Seite | „Alpaca FAIR Framework“ (entspricht dem Repo-Namen) | Vorschlag |
| Fußzeile mit LEIZA, NFDI4Objects, NFDI, DFG und Förderhinweis | von AMT übernommen | Vorschlag |
| Beschreibungstexte (Tagline, Lead, „Where it comes from“) | Entwurf, kurz gehalten | Vorschlag |
| Alligator | Karte „in Vorbereitung“ ohne Link, bis es ein Ziel gibt | 2026-10-29 |
| Build-Werkzeug | keins; handgeschriebenes HTML, `main.py` nur mit dem Schritt `check` | 2026-10-29 |
| Lizenz | MIT, wie die Schwester-Repos | 2026-10-29 |

### A5 Was in welchem Chat hochgeladen wird

Das Repo ist klein; immer den ganzen Baum außer `.git` hochladen:

```cmd
powershell -NoProfile -Command "Get-ChildItem -Force | Where-Object Name -ne '.git' | Compress-Archive -DestinationPath ..\alpaca-site-bundle.zip -Force"
```

Zusätzlich `PRIMER.md` einzeln, damit klar ist, welche Fassung gilt.

---

## Teil B – Schrittübersicht

| ID | Schritt | Repo | hängt ab von | Status |
|---|---|---|---|---|
| S0 | Festlegungen (Aufbau, Name, Sprache) | alpaca-fair-framework.github.io | – | erledigt 2026-10-29 |
| S1 | Landing Page mit Skeleton, Familien-Abschnitt und Links zu AMT.engine/AMT.runner | alpaca-fair-framework.github.io | S0 | erledigt 2026-10-29 |
| S2 | GitHub Pages einschalten und die Live-Seite ansehen | alpaca-fair-framework.github.io | S1 | offen |
| S3 | Alligator verlinken | alpaca-fair-framework.github.io | Ziel für Alligator | offen |
| S4 | Wortlaut und Ausbau der Familie (Beschreibung, weitere Mitglieder) | alpaca-fair-framework.github.io | S1 | offen |

S3 und S4 sind voneinander unabhängig. S2 ist ein Klick im Repo, kein Code, und kann sofort nach dem Einspielen von S1 erfolgen.

---

## Teil C – Die Schritte

## S1 — Landing Page mit Skeleton

**Ziel:** Das leere Repo enthält eine einseitige, zweisprachige Seite im Design von `n4o-rse.github.io/amt-engine/`, die auf AMT.engine und AMT.runner verlinkt.

**Uploads:** keine (Repo war leer).

Umgesetzt: `index.html` (Kopf mit Alpaka, Navigation Home / AMT.engine / AMT.runner / GitHub, Hero, „Part of a family“, „Tools“, „Where it comes from“, Fuß mit Logos), `assets/`, `vendor/roboto/`, `main.py` (Schritt `check`), `README.md`, `LICENSE`, `CITATION.cff`, `CHANGELOG.md`, `.gitignore`, `.nojekyll`.

**Abnahme:** `python main.py` meldet `[check] ok`; ein zweiter Lauf meldet dasselbe, `git status` bleibt sauber; die Seite im Browser öffnen und prüfen: Familie sichtbar, Pinguin führt zur AMT-Website, die Karten führen zu Website, Quellcode und DOI von AMT.engine bzw. zum Quellcode von AMT.runner, der Alligator ist als „in Vorbereitung“ erkennbar, Sprachumschalter und Hell/Dunkel funktionieren.

### Erledigt 2026-10-29

Alles umgesetzt wie oben beschrieben. Anker wie `#tools` gibt es bewusst nicht: Englisch und Deutsch liegen als zwei Blöcke in einer Datei, von denen CSS einen ausblendet, und doppelte IDs wären ungültig und würden im ausgeblendeten Block nicht scrollen. Die Navigation verlinkt deshalb direkt auf die Ziele. Die Seite wurde in einem Headless-Chromium gerendert und angesehen (Englisch hell, Deutsch dunkel, schmal wie ein Telefon); Layout wie bei AMT. Die Klicks auf die externen Links wurden nicht ausgeführt, die Ziele nur gegen die Quell-Repos abgeglichen (S2 prüft sie live).

## S2 — GitHub Pages einschalten

**Ziel:** `https://alpaca-fair-framework.github.io/` liefert die Seite.

**Abnahme:** Im Repo unter Settings → Pages als Quelle „Deploy from a branch“, Branch `main`, Ordner `/ (root)`; nach dem Lauf des Pages-Workflows die Seite aufrufen und Schritt S1 (Abnahme) auf der Live-Seite wiederholen.

## S3 — Alligator verlinken

**Ziel:** Die Karte „Alligator“ und die Figur im Familien-Abschnitt führen zum Alligator.

**Abnahme:** `python main.py` meldet `[check] ok`, Karte und Figur tragen denselben Link in EN und DE; „in Vorbereitung“ ist aus Text und Karte entfernt; `CHANGELOG.md` hat den Eintrag.

## S4 — Wortlaut und Ausbau der Familie

**Ziel:** Die Entwurfstexte (Tagline, Lead, „Where it comes from“) haben den Wortlaut des Autors; weitere Mitglieder sind als Karten ergänzt.

**Abnahme:** Wortlaut in A4 als beschlossen eingetragen; `python main.py` meldet `[check] ok`.

---

## Teil D – Offene Punkte

- **D1** Wortlaut der Texte und der Name „Alpaca FAIR Framework“ gegenüber „Alpaka Research Framework“ auf der AMT-Seite: eine Schreibweise festlegen und in `amt-engine` nachziehen (kommt in S4 als Entscheidung).
- **D2** Gestaltung liegt jetzt zweimal (`amt-engine`, hier). Ändert sich `design/palette.yaml` in `amt-engine`, muss `assets/palette.css` neu kopiert werden. Falls weitere Seiten der Familie dazukommen, lohnt sich eine gemeinsame Quelle; ein Punkt für S4, nicht jetzt.
- **D3** Fußzeile: Passt der Förderhinweis (NFDI4Objects / DFG) für das Framework als Ganzes, oder nur für das, was in NFDI4Objects entsteht?
- **D4** Die Maskottchen sind Pixelbilder; vektorisierte Fassungen folgen vom Autor (wie bei `amt-engine`, D10).
