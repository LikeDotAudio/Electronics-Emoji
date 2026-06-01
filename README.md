# Electronics Emoji

A proposal for a set of electronics schematic symbol emoji, presented as an
interactive viewer. Each symbol is available as an SVG icon (loaded as an ES
module) and rendered to PNG at standard emoji sizes (18×18 and 72×72).

## Live deployment

**https://likedotaudio.github.io/Electronics-Emoji/**

The viewer is `index.html`, served statically via GitHub Pages.

## Running locally

The viewer loads icons as ES modules, which browsers block under the `file://`
scheme (CORS), so it must be served over HTTP:

```bash
python3 server.py
```

This serves the site at http://localhost:8080/index.html and opens it in your
browser automatically.

## Regenerating the PNGs

`renderPNG.py` rasterizes the SVG symbols into the `symbols/18X18/` and
`symbols/72X72/` folders. Output filenames are slugs derived from each symbol's
name and category (kept in sync with the `slug()` function in `index.html`).

```bash
pip install cairosvg
python3 renderPNG.py
```

## Files

| File             | Purpose                                        |
| ---------------- | ---------------------------------------------- |
| `index.html`     | Interactive symbol viewer (the deployed page)  |
| `server.py`      | Local HTTP server for development              |
| `renderPNG.py`   | Renders the SVG symbols to PNG                 |
| `gallery.htm`    | Symbol gallery                                 |
| `proof.htm`      | Proof / preview page                           |
| `symbols/`       | Rendered PNG symbols, by size                  |
