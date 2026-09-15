# Source inventory

## Primary article

| File | Role | Notes |
|---|---|---|
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/main.tex` | Primary scientific source | Current 472-line RevTeX manuscript. Contains abstract, introduction, methods, results, discussion, conclusions, data availability, and Appendix A graphical summary. Submitted to PRAB on 2026-06-23 according to `TODO.md`. |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/refs.bib` | Primary bibliography | 33 references plus the Zenodo dataset. The current entry for Bjelland et al. is arXiv:2606.21259. |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/reports/2026_interim/images/submitted_manuscript.pdf` | Archived rendered article | 12 pages. Useful for page-level references. Its bibliography predates the current `refs.bib`: Bjelland et al. is still printed as “in preparation.” |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/TODO.md` | Submission/version notes | Records PRAB submission, tag `prab_submitted_2026-06-23`, Zenodo DOI, robustness ideas, and one unresolved wording issue concerning the mid-angle/subgrain interpretation. |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/cover_letter_PRAB.md` | Authorial significance statement | Concise statement of novelty, audience relevance, headline result, and intended interpretation. Not independent evidence. |

## Supporting and supplementary analysis

No standalone supplementary-information manuscript was found. The following
files function as generated supporting material:

| File | Role | Notes |
|---|---|---|
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/ebsd2/results/low_angle_moments_rows.tex` | Table I data | Nine ROI rows: empirical mean, gamma shape `k`, gamma scale `theta`, skewness, and fraction above 2 degrees, each with 95% bootstrap confidence intervals. Included by `main.tex`, lines 300–314. |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/ebsd2/results/low_angle_moments_rows 2.tex` | Duplicate table export | Same line count and apparent purpose as the included table file. Confirm whether it is obsolete before any cleanup; do not cite it preferentially. |
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/clic/cond26/ebsd2/results/pairwise_tests.tex` | Pairwise distribution tests | Generated KS, chi-squared, and Anderson–Darling matrices. Not directly included in `main.tex`; supports the summary at article lines 316–324. |
| Zenodo DOI `10.5281/zenodo.20623348` | Open data | EBSD datasets for all nine ROIs; cited in article Data Availability, lines 445–447, and `refs.bib`, lines 43–50. The raw Zenodo files are not present in the inspected directories. |

## Article figures

Figure numbers refer to the 12-page submitted PDF; source labels refer to
`cond26/main.tex`.

| File | Article location | Short description | Presentation value |
|---|---|---|---|
| `cond26/figures/electrode_geometry.png` | Fig. 1, PDF p. 2; lines 89–95 | Sloped-anode geometry and radial exposure zones. | Essential experimental-design figure. |
| `cond26/figures/sem_lowmag.png` | Fig. 2a, PDF p. 3; lines 123–138 | Low-magnification ROI far from craters. | Essential control against local arc damage. |
| `cond26/figures/sem_electron.png` | Fig. 2b, PDF p. 3 | Electron-induced image after FIB cleaning. | Methods/detail; likely optional. |
| `cond26/figures/sem_ion.png` | Fig. 2c, PDF p. 3 | Ion-induced orientation contrast used as cleaning endpoint. | Methods/detail; likely backup. |
| `cond26/figures/efield_vs_radius.eps` | Fig. 3, PDF p. 4; lines 167–175 | Simulated normalized cathode field vs radius; periphery band. | Important if explaining internal reference and fringe field. |
| `cond26/figures/ipf_ref_center_keyed.png` | Fig. 4a, PDF p. 4; lines 208–219 | Reference IPF map with orientation key. | Shows recrystallized grain structure; not the headline result. |
| `cond26/figures/ipf_fe_center.png` | Fig. 4b, PDF p. 4 | Field-exposed center IPF map. | Pair with reference only if grain-size control needs emphasis. |
| `cond26/figures/ipf_key.png` | Component/key asset | IPF color key. | Reusable only with IPF maps. |
| `cond26/figures/ipf_ref_center.png` | Alternate IPF asset | Unkeyed reference map; not used in current article figure. | Avoid unless its provenance is confirmed. |
| `cond26/figures/lam_widescale.png` | Fig. 5a, PDF p. 5; lines 231–242 | LAM at 0–50 degrees; grain boundaries dominate. | Useful pedagogical comparison. |
| `cond26/figures/lam_lowscale.png` | Fig. 5b, PDF p. 5 | Same area at 0–5 degrees; intragrain variation appears. | Useful EBSD explainer. |
| `cond26/figures/lam_fe_center.png` | Fig. 6a, PDF p. 5; lines 246–257 | Field-exposed center LAM map. | Strong visual evidence. |
| `cond26/figures/lam_fe_edge.png` | Fig. 6b, PDF p. 5 | Field-exposed edge LAM map. | Secondary field-on example. |
| `cond26/figures/lam_fe_edge2.png` | Fig. 7a, PDF p. 5; lines 261–272 | Field-exposed edge ROI. | Best used against matched reference. |
| `cond26/figures/lam_ref_edge.png` | Fig. 7b, PDF p. 5 | Position-matched unexposed reference ROI. | Best direct visual comparison. |
| `cond26/figures/low_angle_overlay.pdf` | Fig. 8, PDF p. 6; lines 289–298 | Low-angle histograms and gamma fits. | Essential for distribution broadening and common-shape argument. |
| `cond26/figures/mean_vs_radius.pdf` | Fig. 9, PDF p. 6; lines 333–342 | Mean LAM versus radius with grain-corrected SEMs. | Headline quantitative result. |
| `cond26/figures/full_range_overlay.pdf` | Fig. 10, PDF p. 7; lines 351–359 | Full-range pair-misorientation histogram; Mackenzie window and Sigma 3 twin peak. | Scientifically rich but interpretively delicate; optional/backup. |
| `cond26/figures/infographic.pdf` | Fig. 11, PDF p. 12; Appendix A, lines 458–470 | Four-part graphical summary of geometry, hierarchy, distribution, and candidate mechanism. | Useful closing or abstract graphic; avoid using it as a substitute for the evidence sequence. |

## Contextual reports and future-direction sources

| File | Role | Evidence status |
|---|---|---|
| `reports/2026_interim/report.tex` | Contract-stage summary | Contextual synthesis. Lines 38–44 explicitly frame the depth question and MeVArc future direction. |
| `reports/2026_interim/workplan.tex` | Next-stage work plan | Contextual/proposed work. Lines 7–44 define depth questions and pilot-first TEM/STEM + finer-EBSD approach; lines 46–59 define the RFX stainless-steel track. |
| `rfx/STATUS.md` | RFX status through 2026-07-13 | Contextual/preliminary. Records sample inventory, missing conditioning data, SEM observations, and first EBSD acquisition quality. Must be refreshed before public use. |
| `rfx/PLAN.md` | RFX experimental plan | Contextual/proposed. Defines cross-section, SEM, FIB, EBSD, field-gradient, phase-mapping, and inclusion-analysis steps. |
| `rfx/NEEDED.md` | Missing-input list | Contextual. Useful for identifying what cannot yet be claimed. |
| `rfx/REVIEW_NOTES.md` | Adversarial review of inclusion/depth memos | Contextual quality-control source. Identifies corrected citations, numerical slips, and overstatements. |
| `rfx/INCLUSION_DEBRIS_EXPECTED.md` | Inclusion/debris interpretation memo | Suggested interpretation, not article evidence. Must be read together with `REVIEW_NOTES.md`. |
| `rfx/INCLUSION_DENSITY_DEPTH.md` | Stereological depth-estimation memo | Suggested/order-of-magnitude analysis, not article evidence. Review says it is subordinate to direct FIB depth measurement. |
| `rfx/data/sem/SEM_summary_as-received.pdf` | SEM report | Preliminary RFX observation source. Public presentation requires author confirmation and updated status. |
| `rfx/docs/drawings/Dis_107_rev0.pdf` | Electrode drawing | Primary geometry document for RFX sample; confirms AISI 304 in the title block according to `STATUS.md`. |
| `rfx/docs/Electric_field_distributions.pptx` and `rfx/data/field-simulation/*.txt` | RFX field material | Geometry/simulation source. Confirm which surface vector and normalization correspond to the tested cathodes before plotting. |

## Prior presentation (direct predecessor)

| File | Role | Evidence status |
|---|---|---|
| `/Users/yinona/Library/CloudStorage/GoogleDrive-Yinon.Ash@mail.huji.ac.il/My Drive/Clic_huji_microscopy/Presentations/mevarc25_huji_v2.pdf` | MeVArc 2025 HUJI talk, "Observing plastic evolution related to high-field conditioning" (31 slides). | Contextual/authorial. The direct prequel: presents the MDDF model (rate-vs-field, dark-current spikes) and the local STEM/FIB microscopy (denuded zones, top ~100 nm, 300 K and 30 K), and closes asking for "other materials? more samples?". Confirms affiliations: Profatilova, Jacewicz = Uppsala; Popov = HUJI; Bjelland, Wuensch, Millar, Calatroni = CERN. Note the ~100 nm (2025) vs ~200 nm (paper) depth discrepancy. |
| `.../Presentations/mevarc25_huji_v2.pptx` (and `_comp.pptx`, `v1.pptx`) | Editable 2025 source | Asset source. MDDF and STEM figures are embedded here; extract only with approval before reuse in the 2026 deck. |

## Collected source files (sources/) — 2026-07-20

Local copies in `mevarc26/sources/` (original filenames preserved).

| Copied file | Original path | Identification |
|---|---|---|
| `Engelberg_MDDF_FieldDependent.pdf` | `../sideprojects/plast/papers/Engelberg_MDDF_FieldDependent.pdf` | Engelberg et al., PRL 120, 124801 (2018) — MDDF field-dependent breakdown model. |
| `Field_Dependent_Conditioning_Correct_Publisher.pdf` | `../cond26/private/ref_pdfs/Field_Dependent_Conditioning_Correct_Publisher.pdf` | Engelberg et al., PRAB 22, 083501 (2019) — field-dependent conditioning. |
| `Engelberg_2020_PRAB_DarkCurrentSpikes.pdf` | `../sideprojects/plast/papers/Engelberg_2020_PRAB_DarkCurrentSpikes.pdf` | Engelberg et al., PRAB 23, 123501 (2020) — dark-current spikes / MDDF. |
| `Jacewicz_2024_Surface_Modifications_Cu.pdf` | `../sideprojects/plast/papers/Jacewicz_2024_Surface_Modifications_Cu.pdf` | Jacewicz et al., JAP 137, 193302 (2025) — Cu surface / denuded-zone STEM. |
| `main.pdf` | `../cond26/main.pdf` | cond26 PRAB manuscript (compiled PDF). LaTeX source: `../cond26/main.tex`; bibliography: `../cond26/refs.bib`. |
| `mevarc25_huji_v2.pdf` | `.../Clic_huji_microscopy/Presentations/mevarc25_huji_v2.pdf` | MeVArc 2025 HUJI deck (31 slides; MDDF + STEM microscopy). |
| `RMP_Review_Wuensch_2026.pdf` | `../sideprojects/plast/papers/RMP_Review_Wuensch_2026.pdf` | Wuensch et al., RMP 98, 025004 (2026) — conditioning review. |
| `Nordlund and Djurabekova - 2012 - Defect model for the dependence of breakdown rate .pdf` | `../people/collaborators/ilan/Nordlund and Djurabekova - 2012 - Defect model for the dependence of breakdown rate .pdf` | Nordlund & Djurabekova, PRSTAB 15, 071002 (2012) — defect breakdown model. |
| `Korsback_2020_arXiv_DC_Conditioning.pdf` | `../sideprojects/plast/papers/Korsback_2020_arXiv_DC_Conditioning.pdf` | Korsbäck et al. (2020) — dark-current conditioning simulation. |
| `mevarc24_ashkenazy_v3.pdf` | `../research/microscopy/microscopy_24/mevarc24_ashkenazy_v3.pdf` | MeVArc 2024 microscopy talk (16 MB; SEM/FIB/EBSD). |
| `mevarc2013_ashkenazy_v01.1.pdf` | `../meetings/mevarc/2013/mevarc2013_ashkenazy_v01.1.pdf` | MeVArc 2013 group talk (6.5 MB; early MDDF/conditioning). |
| `Degiovanni_2016_PRAB_Conditioning.pdf` | https://inspirehep.net/files/65b4ebd41c8d6eca5d34c0e15ea5ff1e | Degiovanni et al., PRAB 19, 032001 (2016) — conditioning vs. RF pulses. |
| `Mughrabi_2009_MMTB_CyclicSlip.pdf` | https://link.springer.com/content/pdf/10.1007/s11663-009-9240-4.pdf | Mughrabi, MMTB 40, 431 (2009) — cyclic slip irreversibilities / fatigue damage. |

### Added by user 2026-07-20 (afternoon)

| File | Identification |
|---|---|
| `StanzlTschegg_2010_Procedia_VHCF.pdf` (copy of `1-s2.0-S1877705810001682-main.pdf`) | Stanzl-Tschegg & Schönbauer, Procedia Eng. 2 (2010) — VHCF near-threshold fatigue. Resolves the "not found" item below. |
| `CERN_logo.png` | Official CERN logo → installed to `figures/logo_cern.png` (replaced placeholder wordmark). |
| `rfx_logo.jpg` | Official RFX logo → installed to `figures/logo_rfx.jpg` (title page now references the `.jpg`). |

**Still a placeholder:** `figures/logo_uppsala.png` — no official Uppsala
University logo supplied yet; swap when available.

### Not found (web search + download attempts, 2026-07-20)

| Sought reference | Notes |
|---|---|
| Stanzl-Tschegg et al., Int. J. Fatigue 29, 2050 (2007); DOI 10.1016/j.ijfatigue.2007.03.010 (manuscript citation) | Elsevier paywall; same Cloudflare block on direct PDF fetch. |

Alternate manuscript paths exist but were not copied (already represented above): `../manuscripts/prl_2017/editor/main.pdf` (PRL 2018), `../manuscripts/prstab_2019/main.pdf` (PRAB 2019), `../manuscripts/eli_2020/main.pdf` (PRAB 2020), `../reports/2026_interim/images/submitted_manuscript.pdf` (earlier cond26 render).

### Related presentations in `../presentations/` (listed only)

| Path | Notes |
|---|---|
| `../presentations/clic-intro.pdf` / `clic-intro.pptx` | General CLIC introduction. |
| `../presentations/clic_short_nor.pptx` | Short CLIC overview. |
| `../presentations/seminar_clic_rafael.pdf` / `seminar_clic_rafael.pptx` | CLIC seminar (Rafael). |
| `../presentations/CLIC_2007_07_05_fatigue.ppt` | CLIC fatigue (2007). |
| `../presentations/microscopy_pres/huji_clic_ilvisit_v1.pptx` | HUJI CLIC microscopy visit deck (v1, ~8 MB). |
| `../presentations/microscopy_pres/huji_clic_ilvisit_v2.pptx` | Same visit deck v2 (~76 MB; not copied). |

Additional group decks outside `../presentations/` (not copied unless noted above): `../meetings/mevarc/2025/mevarc25_huji_v2.pdf` (duplicate of 2025 deck), `../sources/breakdown_in_rf_ww.pptx`, `../sources/mevarc_wuensch_final.pptx`, `../sources/20120929MeVArc12_UppsalaSEM.pptx`.

