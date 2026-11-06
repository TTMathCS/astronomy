# Astronomy

Astronomy book by book: https://astronomy.akadian.ca/ (part of Mars – your new home, www.akadian.ca).
Built with MkDocs Material in the same look as math.akadian.ca and physics.akadian.ca; GitHub Pages publishes it
on every push to `main` (`.github/workflows/pages.yml`), so a push here is a publish.

## Layout

```
mkdocs.yml            the site and its menu (the Books part is written by tools/nav.py)
docs/index.md         the first page
docs/books/<book>/    one folder per book: index.md (contents) and chapters NN-Name.md
docs/javascripts/     the shared scripts (reader.js, play.js, ask.js ...) and levels.js, this site's level rules
docs/stylesheets/     mars.css (the akadian.ca look) and the shared reading styles
docs/images/          the banner and background pictures, sources in images/README.md
overrides/home.html   the banner on the first page
tools/nav.py          rewrites the Books menu from the folders
```

## The shelf

Planned, in this order on the menu: the night sky, light and telescopes, orbits, the solar system, Mars, the Sun,
stars, galaxies, cosmology, exoplanets and life, and the history of astronomy. The history book was started first
(Jim, 5 Nov 2026). Folder names are in `tools/nav.py`; a book joins the menu when its folder has an `index.md`.

## Writing a chapter

- Chapters follow the math books' format: `# N. Title`, an italic summary, the "In this chapter" box, numbered
  sections, Check yourself with folded answers, Summary, Next, Further reading.
- Every fact links its source. Each section ends with a closed `??? note "Sources"` box.
- History covers the whole world in each period. A disputed claim says it is disputed and gives both sides.
- Mars numbers sit beside Earth's in a two-column table.
- After adding a chapter: `python3 tools/nav.py`, then `mkdocs build --strict`.
