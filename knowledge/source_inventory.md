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

