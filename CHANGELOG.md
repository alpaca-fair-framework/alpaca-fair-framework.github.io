# Changelog

All notable changes to the Alpaca FAIR Framework website are documented in this file.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/)
and the project uses [Semantic Versioning](https://semver.org/). The version
is the one shown in the footer of the page (`site 0.1.0`).

## [Unreleased]

### Changed

- The site moves into `docs/` (`index.html`, `assets/`, `vendor/`, `.nojekyll`), as in
  `amt-engine`. GitHub Pages deploys the branch `main`, folder `/docs`. `main.py`, the
  README and the PRIMER follow.

### Fixed

- The first Pages run failed because the folder `docs/` that Pages builds from did not
  exist: the 0.1.0 commit had the site in the repository root.

### Added

- `main.py check` also fails when `docs/.nojekyll` is missing, since without it GitHub
  Pages runs Jekyll on the folder.

## [0.1.0] - 2026-10-29

First version of the site: a single, bilingual (English and German) landing page
in the design of the AMT website (<https://n4o-rse.github.io/amt-engine/>), with
the "Part of a family" section as its core.

### Added

- `index.html`: header with the alpaca and the navigation (Home, AMT.engine,
  AMT.runner, GitHub), hero with the mascot, the section "Part of a family"
  (Alpaca, AMT, Alligator), the section "Tools" with one card each for
  AMT.engine (website, source code, DOI), AMT.runner (source code) and
  Alligator (marked "in preparation", no link yet), a short "Where it comes
  from" and the footer with the LEIZA, NFDI4Objects, NFDI and DFG logos and
  the funding note.
- English and German in one file with a language switch, and a light and dark
  mode that follows the system until the visitor chooses (`assets/site.js`).
- `assets/site.css`, `assets/palette.css`, `assets/site.js`: copied from
  `amt-engine` 0.5.0 (`docs/assets/`). `site.css` has one block appended for the
  linked family figures and the tool cards; `site.js` stores its settings under
  `alpaca-theme` and `alpaca-lang` so that they do not clash with the AMT site.
- `assets/img/`: the alpaca, the AMT penguin and the alligator, a small alpaca
  for the header and the favicon, and the logos of the footer.
- `vendor/roboto/`: Roboto (SIL OFL 1.1), served from this repository so that
  the page loads nothing from another server.
- `main.py` with the step `check`: every local file the page points to exists,
  no element loads anything from another server, the English and the German
  half link to the same places, and the links to AMT.engine and AMT.runner are
  present.
- `PRIMER.md` (work plan), `README.md`, `LICENSE` (MIT), `CITATION.cff`,
  `.gitignore` and `.nojekyll`.
