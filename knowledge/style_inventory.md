# Presentation style inventory

This inventory covers reusable presentation-style material in accessible
project directories. Scientific content from those projects should not be
copied merely because a style element is reusable.

## Strongest reusable source: RFX Beamer presentation

### Main style file

`/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/rfx/presentation/main.tex`

- Beamer 16:9, 11 pt, default theme: lines 4–7.
- Packages include `graphicx`, `booktabs`, `amsmath`, `tikz`, `siunitx`, and
  `appendixnumberbeamer`: lines 10–22.
- HUJI palette: lines 25–40.
  - purple `#75325B`
  - teal `#50A781`
  - gold `#D8AF5C`
  - dark slate `#44546A`
  - crimson `#83151E`
  - mauve `#873B70`
  - cyan `#2B819B`
- Beamer color assignments: lines 43–63.
- Bold frame-title and title fonts; default sans-serif body: lines 65–71.
- Purple title bar with teal accent and optional white HUJI mark: lines 73–91.
- Minimal footer with author/project and frame counter: lines 93–109.
- Custom title page with centered title/subtitle, two affiliation columns, logo
  row, and corner geometry: lines 127–179.
- Speaker notes are embedded with `\note{...}`: lines 181 onward.

**Recommendation:** Reuse the palette, logos, 16:9 setup, `siunitx`, figure
placement conventions, and notes workflow. Rebuild the frame-title rule to
avoid full-paper-width overflow and simplify the title page for a conference
talk. The RFX deck is an internal status presentation, so its dense notes and
collaboration-centered title layout should not be copied verbatim.

### Build files

- `rfx/presentation/latexmkrc` — straightforward PDFLaTeX build with synctex.
- `rfx/presentation/Makefile` — `latexmk` target plus a Ghostscript compressed
  PDF target.

**Recommendation:** Reuse the build pattern. Keep normal and compressed outputs
separate; do not make lossy compression the only deliverable.

### Logo assets

| Path | Likely use | Recommendation |
|---|---|---|
| `rfx/presentation/figures/huji_logo_long.png` | HUJI horizontal mark | Good title-page/footer asset; verify conference-use rules and contrast. |
| `rfx/presentation/figures/huji_logo_tri_right.pdf` | HUJI triangular corner mark | Suitable for restrained title-page decoration. |
| `rfx/presentation/figures/huji_logo_wide_right_white.pdf` | White HUJI header mark | Use only on a sufficiently dark title bar. |
| `rfx/presentation/figures/logo_nano.png` | HUJI Nanoscience logo | Include only if the unit should be represented institutionally. |
| `rfx/presentation/figures/logo_rfx.png` | Consorzio RFX logo | Use when RFX future work is visible and collaborator approval is confirmed. |

### Figure conventions in the RFX deck

- Photographs and field maps use short, source-like captions beneath images.
- Tables use `booktabs` rather than grid lines.
- Scientific units use `siunitx`.
- Notes contain caveats and citations rather than crowding the audience slide.

**Recommendation:** Preserve these conventions. Do not reuse RFX scientific
images until their inclusion in the narrative is approved.

## HUJI report styling

`/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/reports/2026_interim/header_rpt.tex`

- Defines a conservative HUJI blue `RGB(51,77,167)`: lines 1–4.
- Uses Times for a formal report, plus `fancyhdr`: lines 5–21.
- Defines HUJI institute/footer strings and project ID: lines 23–27.
- Uses `huji_letterhead.jpg` in the header and a thin footer rule: lines 29–37
  and 65–75.
- Hyperlink color and PDF metadata conventions: lines 39–50.

Asset:
`/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/reports/2026_interim/images/huji_letterhead.jpg`

**Recommendation:** The letterhead is useful for institutional metadata but is
too document-like for repeated slide headers. The formal blue could be used for
citations or secondary accents if it harmonizes with the HUJI/RFX palette.

## Article figure conventions worth preserving

These are scientific encoding conventions, not content to copy from another
project:

- Field hierarchy is consistently red/orange/green/blue across the graphical
  summary and quantitative plots.
- The same 0–5-degree low-angle scale is used across LAM maps.
- Center ROIs are solid and off-center ROIs dashed in distribution plots.
- Uncertainty and reference bands are stated explicitly in captions.
- Figures distinguish measured data, fitted curves, and simulated fields.

**Recommendation:** Preserve these encodings wherever the same variables are
shown. Avoid restyling plots in ways that break cross-slide color consistency.

## Files not found

- No standalone Beamer `.sty`, theme `.sty`, custom `.cls`, or shared macro
  package was found in the inspected `cond26`, `rfx`, or `2026_interim`
  directories.
- The RFX style is embedded directly in `presentation/main.tex`.
- No custom font files were found; the RFX deck uses Beamer's default
  sans-serif setup with T1 encoding.

## Recommended style direction for the future deck

1. Use 16:9 Beamer and the HUJI purple/teal/gold palette, but with a quieter
   white scientific canvas.
2. Reserve red/orange/green/blue for scientific field-exposure categories so
   institutional colors do not compete with data semantics.
3. Use one dominant figure per result slide and minimal audience-facing text.
4. Keep detailed caveats, citations, and timing in notes.
5. Use the HUJI and collaborator logos only on title/closing slides, not every
   frame.
6. Use the article's graphical summary only as synthesis; build the argument
   from the underlying figures first.

