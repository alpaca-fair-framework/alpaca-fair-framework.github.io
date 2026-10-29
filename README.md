# Alpaca FAIR Framework: website

Landing page of the Alpaca FAIR Framework, published with GitHub Pages at
<https://alpaca-fair-framework.github.io/>.

One page, in English and German, in the design of the
[AMT website](https://n4o-rse.github.io/amt-engine/). It introduces the family and
links to its members:

| Member | Links |
|---|---|
| AMT.engine, the Academic Meta Tool as a Python reasoner | [website](https://n4o-rse.github.io/amt-engine/), [source code](https://github.com/n4o-rse/amt-engine), [doi:10.5281/zenodo.23669466](https://doi.org/10.5281/zenodo.23669466) |
| AMT.runner, a wrapper that runs the AMT.engine pipeline on one Turtle file | [source code](https://github.com/n4o-rse/amt-runner) |
| Alligator | in preparation |

## Layout

```
docs/             the site, as GitHub Pages serves it (as in amt-engine)
  index.html        the page
  assets/           site.css, palette.css, site.js and the images
  vendor/roboto/    the typeface, served from here (SIL OFL 1.1)
  .nojekyll         tells GitHub Pages to serve the files as they are
main.py           the check (see below)
PRIMER.md         work plan, in German
CHANGELOG.md      what changed, per version
```

GitHub Pages is set to deploy the branch `main`, folder `/docs`. The page is plain
HTML and CSS; there is nothing to build. `docs/assets/palette.css`,
`docs/assets/site.css` and `docs/assets/site.js` are copies from
[amt-engine](https://github.com/n4o-rse/amt-engine) (`docs/assets/`).

## Check

```
python main.py
```

Checks that every local file the page uses exists, that `docs/.nojekyll` is there, that nothing is loaded from
another server, that the English and the German half link to the same places and
that the links to AMT.engine and AMT.runner are there. It needs only Python 3
(standard library) and no network, and it writes no file.

To look at the page, open `docs/index.html` in a browser.

## Licence

MIT, see [LICENSE](LICENSE). Roboto is licensed under the SIL Open Font
License 1.1 (`vendor/roboto/LICENSE`). The mascots and the logos of the
institutions are not covered by the MIT licence.
