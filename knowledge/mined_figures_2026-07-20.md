# Mined figures from prior MeVArc decks (2026-07-20)

Brief pass over `sources/mevarc24_ashkenazy_v3.pdf` (31 pp) and
`sources/mevarc2013_ashkenazy_v01.1.pdf` (23 pp). Thumbnails at 60 DPI;
selected pages rendered at 200 DPI into `figures/mined/`.

**2026-09-28:** the `figures/mined/*.png` renders (9.6 MB, never used in the
deck) were deleted. Re-render any page listed below from the source deck in
`sources/` with PyMuPDF: `python3 -c "import fitz; fitz.open('sources/X.pdf')[N-1].get_pixmap(dpi=200).save('figures/mined/X_pN.png')"`.

**Already in `figures/` (not re-mined):** MDDF critical-transition, rate-vs-field,
nucleation-rate plots; STEM denuded-zone / 300 K FE–REF panels; cond26 EBSD maps.

---

## MeVArc 2024 (`mevarc24_ashkenazy_v3.pdf`)

| File | Slide | Description | 2026 use |
|---|---|---|---|
| `figures/mined/mevarc24_p4.png` | 4 | SEM + EBSD overlay of post-breakdown craters; intrinsic vs extrinsic events on grain structure. | Post-BD forensics / motivation for large-area EBSD (Part I or copper intro). |
| `figures/mined/mevarc24_p8.png` | 8 | Schematic pipeline: high field → critical transition → nucleation → emission → Cu plasma → BD; slip-plane cartoon. | MDDF mechanism slide — complements `mddf_critical_transition.png` with full breakdown chain. |
| `figures/mined/mevarc24_p16.png` | 16 | Bright-field TEM pair (g₁₁₁ vs g₂₂₀): FIB-induced dislocation contrast vanishes under diffraction — classic “red herring.” | Methods / limits slide; justifies FIB caution before showing cond26 EBSD. |
| `figures/mined/mevarc24_p20.png` | 20 | Cross-sectional STEM: 5 kV-only vs +2 kV cleanup; bright FIB artifacts removed while large features persist. | FIB artifact backup; pairs with denuded-zone STEM. |
| `figures/mined/mevarc24_p24.png` | 24 | FIB cross-section at 30 K: top ~100 nm of conditioned region visibly modified (wide + detail panels). | Prior-microscopy sequel — 30 K complement to existing 300 K STEM assets. |

**Not extracted (overlap or not found in brief pass):**

- Slide 12 — dark-current spike PDF + λ₀ vs field: duplicates `mddf_rate_vs_field.png` / Engelberg PRAB 2020 figures already copied from 2025 deck.
- **Hard-vs-soft copper conditioning curves:** not present in sampled slides; likely absent from this deck (see Korsbäck 2020 paper in `sources/` instead).
- Experiment-setup schematics: electrode geometry already in `figures/electrode_geometry.png` (cond26).

---

## MeVArc 2013 (`mevarc2013_ashkenazy_v01.1.pdf`)

| File | Slide | Description | 2026 use |
|---|---|---|---|
| `figures/mined/mevarc2013_p19.png` | 19 | Early-warning signals: variance and skewness moments vs σ_E spike near critical stress (~0.64 GPa). | MDDF “signs of criticality” backup — statistical precursor to rate-vs-field / critical-transition plots. |

**Not extracted (overlap or not complementary):**

- Slides 11–17 — bifurcation diagrams, analytical PDFs, BDR exponent fits: theory already covered by `mddf_*` figures from 2025.
- Slide 21 — early DC autocorrelation attempt (“shows nothing”): negative result; low presentation value.
- **Dark-current spike distributions, FIB/SEM panels, conditioning curves, setup schematics:** not found in this deck (2013 talk is model-focused).

---

## Search summary

| Sought asset | MeVArc 2024 | MeVArc 2013 |
|---|---|---|
| Dark-current spike distribution | Present (slide 12) but redundant with existing MDDF figures | Not found |
| Hard-vs-soft conditioning curves | Not found | Not found |
| FIB “red herring” panels | **Found** (slides 16, 20) | Not found |
| Post-breakdown SEM / plasma | **Found** (slide 4; slide 8 schematic) | Not found |
| Experiment-setup schematics | Partial (slide 8 mechanism only) | Not found |
| Complementary MDDF statistics | — | **Found** (slide 19 early-warning moments) |
