# Equations, figures, numerical results, and citations

## Important equations and relations

| Relation | Meaning | Source |
|---|---|---|
| `sigma_M = epsilon_0 E^2 / 2` | Tensile Maxwell stress at a metal surface. Gives about 0.028 MPa at 80 MV/m. | `cond26/main.tex`, Introduction line 69; Discussion lines 389–390. |
| `E(r) = V_applied / d(r)` | Local cathode field in the sloped-gap approximation. | Methods line 100. |
| `ell_D ~ 1/sqrt(rho)` | Debye-like screening length for a dislocation ensemble. | Discussion lines 372–376; Groma et al., PRL 2006. |
| Gamma mean `= k theta` | Parameterization of fitted LAM distributions. | Table I caption, lines 300–303. |
| Grain-corrected SEM `sigma/sqrt(N_grains)` | Error bars on mean-LAM radial plot. | Fig. 9 caption, lines 336–340. |

No numbered display equations appear in the current article; these relations
are embedded in prose and captions.

## Numerical evidence hierarchy

### Headline numbers

- Peak conditioning field: approximately 80 MV/m; edge about 69–77 MV/m.
  Source: Methods lines 97–105 and ROI definitions lines 156–165.
- Pulse protocol: 1 microsecond at 1 kHz, about `10^9` conditioning pulses.
  Source: Methods line 103; Introduction line 71.
- Maxwell stress at 80 MV/m: about 0.028 MPa. Source: lines 69 and 390.
- Nine ROIs; 23,000–25,000 indexed points and about 50,000–60,000 neighbor
  pairs per ROI. Source: Methods lines 180–189.
- Mean LAM: high field about 1.2 degrees; external REF about 0.68 degrees;
  approximately 75% difference. Source: Results lines 330–340 and Discussion
  line 370.
- LAM above 2 degrees: about 0.14 in FE center/edge versus about 0.016 in REF;
  approximately eightfold. Source: Results line 318 and Table I.

### Supporting numbers

- Field-exposed periphery field: about 2.9% of center, at most 2.5 MV/m.
  Source: Fig. 3 caption, lines 167–174.
- Breakdown density: about 24, 12, and 5 per square centimeter across radial
  zones. Source: Methods lines 103–106.
- Grain size: 26–30 micrometers across all ROIs. Source: Results lines 200–205.
- Common gamma shape: `k ≈ 2.6–2.9`; scale roughly 0.22 to 0.46 degrees.
  Source: Results lines 322–324 and Table I.
- KS effect sizes: greater than 0.25 for FE center/edge against all unexposed
  regions; greater than 0.31 against external REF. Source: line 319.
- Mackenzie-window population: 2–3 times higher in FE; Sigma 3 fraction
  approximately 7–11% across all samples. Source: lines 344–359.

## Recommended figure sequence for evidence

1. Fig. 1 — geometry creates the controlled spatial coordinate.
2. Fig. 2a — ROIs are far from craters.
3. Fig. 5 — teach wide-angle versus low-angle LAM.
4. Fig. 7 — direct field-exposed versus reference visual comparison.
5. Fig. 9 — headline three-tier quantitative result.
6. Fig. 8 — distribution broadening, eightfold tail, and common-shape fit.
7. Optional Fig. 10 — preserved twin skeleton and mid-angle excess.
8. Fig. 11 — synthesis/closing only.

## Load-bearing citations

| Citation key | Claim supported | Bibliographic source |
|---|---|---|
| `wuensch_fundamental_2026` | Conditioning mechanism remains open; dislocation evidence and material trends. | Wuensch et al., *Reviews of Modern Physics* 98, 025004 (2026), DOI 10.1103/h8wb-y278. |
| `bjelland_field_dependent_2026` | Sloped-electrode conditioning history, local-field model, `E_S` profile, breakdown positions. | Bjelland et al., arXiv:2606.21259 (2026), DOI 10.48550/arXiv.2606.21259. |
| `engelberg_stochastic_2018` / `engelberg_theory_2019` | MDDF breakdown model and collective dislocation instability. | PRL 120, 124801 (2018); PRAB 22, 083501 (2019). |
| `engelberg_dark_2020` | Dark-current spikes consistent with mobile-dislocation dynamics. | PRAB 23, 123501 (2020). |
| `jacewicz_surface_2025` | Local approximately 200-nm dislocation-denuded zone in conditioned hard copper. | *Journal of Applied Physics* 137, 193302 (2025). |
| `korsback_vacuum_2020` | Hard versus soft copper conditioning behavior. | PRAB 23, 033102 (2020). |
| `pantleon_resolving_2008` / `konijnenberg_3d_ebsd_gnd_2015` | EBSD orientation gradients as GND proxies. | *Scripta Materialia* 58, 994–997; *Acta Materialia* 99, 402–414. |
| `lehockey_mapping_2000` / `kamaya_smoothing_2010` | Misorientation mapping and kernel treatment. | EBSD book chapter; *Materials Transactions* 51, 1516–1520. |
| `mughrabi_cyclic_2009` / `stanzl-tschegg_vhcf_2007` | Cumulative sub-yield dislocation rearrangement in VHCF. | *MMTB* 40, 431–453; *IJF* 29, 2050–2059. |
| `hughes_scaling_1998` / `gurao_generalized_2014` | Fixed-shape scaling of deformation-induced misorientation distributions. | PRL 81, 4664–4667; *Scientific Reports* 4, 5641. |
| `ashkenazy_ebsd_data_2026` | Public nine-ROI dataset. | Zenodo DOI 10.5281/zenodo.20623348. |

## Page map for the archived submitted PDF

- p. 1: title, abstract, Introduction begins.
- p. 2: Introduction ends; Methods A; Fig. 1.
- p. 3: Fig. 2; Methods B.
- p. 4: Fig. 3; Methods C; Results begin; Fig. 4.
- p. 5: Figs. 5–7; LAM, KAM/LOS, histogram analysis begins.
- p. 6: Table I; Figs. 8–9; principal low-angle quantitative result.
- p. 7: Fig. 10; Discussion A begins.
- p. 8: Discussion A limitations; Discussion B (`E_S`) and future comparison.
- p. 9: Conclusions, data availability, acknowledgments, references begin.
- pp. 9–11: references; Appendix A begins on p. 11.
- p. 12: Fig. 11 graphical summary.

