# MeVArc 2025 assets extracted for reuse

Source deck: `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/Clic_huji_microscopy/Presentations/mevarc25_huji_v2.pptx`
(rendered `mevarc25_huji_v2.pdf`, 31 slides). All figures below are the author's
own published/presented work (PRL 120, 124801 (2018); JAP 137, 193302 (2025)),
so reuse in the 2026 deck is legitimate. `slideN.xml` numbering matches the PDF
display order.

Copied into `mevarc26/figures/` with descriptive names:

| New filename | Source (pptx media / 2025 slide) | Content | Proposed 2026 use |
|---|---|---|---|
| `mddf_critical_transition.png` | image8 / slide 3 | MDDF schematic: `dn/dt` vs `n` with unstable `n*` and critical `n_c`, runaway arrows. | Slide 3 (MDDF model) — the core mechanism cartoon. |
| `mddf_rate_vs_field.png` | image10 / slide 4 | Breakdown-rate ratio vs field `E` (MV/m); model curves + data; the steep `~E^30` scaling. | Slide 3 (MDDF model) — "reproduces the field dependence." |
| `mddf_nucleation_rate.png` | image13 / slide 5 | Nucleation rate `λ0` (per slip plane) vs `E − E_th`; model curves + several datasets. | Slide 3 backup or dark-current/rate detail. |
| `stem_denuded_zone.png` | image45 / slide 21 | Two-panel cross-sectional STEM; near-surface dislocation-denuded band; scale bars 100 nm (left) and 200 nm (right). | Slide 4 (prior microscopy) — the key denuded-zone figure. |
| `stem_fe_300k.png` | image49 / slide 24 | Field-exposed Cu (007, 300 K): denuded band adjacent to the surface. | Slide 4 — field-exposed half of the FE-vs-REF pair. |
| `stem_ref_300k.png` | image50 / slide 24 | Reference Cu (007, 300 K): dislocation-rich right up to the surface, no denuded zone. | Slide 4 — reference half of the FE-vs-REF pair. |

## Notes

- **100 vs 200 nm depth question is resolved by `stem_denuded_zone.png`:** the
  two panels carry 100 nm and 200 nm scale bars at different magnifications, so
  both numbers describe the same modified surface layer. The 2026 talk can say
  "top ~100–200 nm" without contradiction, and reconcile with Groma
  `ℓ_D ~ 100 nm`.
- Other embedded assets not copied (available if needed): FIB "red herring"
  artifact panels (slides 10–19: image25.gif, image31–image43), post-BD SEM /
  plasma deposition (slides 6–8), and additional STEM comparisons (slides
  22–30). Many are `.tif`/`.wdp`; convert to PNG/PDF before use with pdfLaTeX.
- Extraction method: `unzip` the `.pptx`, read `ppt/slides/_rels/*.rels` for the
  slide→media map, convert TIFF via `sips -s format png`.
