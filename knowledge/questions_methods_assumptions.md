# Questions, methods, and assumptions

## Main scientific questions

1. **Article-supported:** Do high-field-conditioned regions contain a
   large-area dislocation-sensitive structural signature absent from
   unexposed regions? Source: abstract, lines 36–42; Introduction, lines 67–80.
2. **Article-supported:** Does that signature vary systematically with local
   field-exposure history on one cathode? Source: Methods, lines 97–111;
   Results, lines 330–342.
3. **Article-supported interpretation question:** Can the spatial signature be
   a microstructural correlate of the conditioning variable `E_S`? Source:
   Discussion, lines 411–427.
4. **Contextual future question:** Are the near-surface TEM depletion and the
   deeper EBSD accumulation parts of one depth-dependent redistribution
   profile? Source: `reports/2026_interim/workplan.tex`, lines 1–18.
5. **Contextual future question:** Does the mechanism generalize to AISI 304
   stainless steel under continuous-DC exposure? Source: work plan, lines
   46–59; `rfx/PLAN.md`, Objective.

## Experimental design

- **Article-supported:** OFE copper cathode from the CERN pulsed-DC Large
  Electrode System. Pulses were 1 microsecond at 1 kHz; peak field about
  80 MV/m. Source: Methods subsection “Sloped-anode geometry,” lines 97–105.
- **Article-supported:** The anode has a flat central radius `r_i = 6.5 mm`, a
  60 micrometer gap, and a sloped annulus to `r_o = 20 mm`, where the gap is
  70 micrometers. The field falls from about 80 MV/m in the center to about
  69 MV/m at the active edge. Source: Fig. 1 caption and text, lines 89–101;
  PDF p. 2.
- **Article-supported:** Radial breakdown densities were approximately
  24, 12, and 5 breakdowns per square centimeter in center, middle, and outer
  regions. Source: Methods, lines 103–106.
- **Article-supported:** Nine EBSD ROIs: two FE center, two FE edge, two FE
  periphery, one REF center, and two REF edge. Exact radii and field ranges are
  listed at lines 156–165.
- **Article-supported:** FE periphery at radii about 25–27 mm received about
  2.9% of central field, at most roughly 2.5 MV/m. It is an internal low-field
  control, not a strictly zero-field control. Source: lines 160–174; Fig. 3,
  PDF p. 4.
- **Article-supported:** Separate REF cathode underwent identical machining and
  heat treatment but no high-field exposure. Source: lines 108–111 and 150–165.

## Sample preparation and acquisition

- **Article-supported:** Diamond turning gave `R_a < 20 nm`; vacuum heat
  treatment peaked at 835 degrees C after a 795 degrees C hold. Source:
  Methods subsection “Samples and regions of interest,” lines 140–147.
- **Article-supported:** ROIs were chosen hundreds of micrometers from visible
  breakdown craters. Source: lines 113–116; Fig. 2, PDF p. 3.
- **Article-supported:** Ga FIB cleaning used 30 keV, 2.5 nA over
  550 x 300 micrometer regions. AFM measured removal no greater than 10 nm.
  Source: lines 118–121.
- **Article-supported:** EBSD: 15 kV, 3.2 nA, about 40 patterns/s, 97% indexing,
  500-micrometer-wide maps, 3-micrometer hexagonal step, and 23,000–25,000
  indexed points per ROI. Source: lines 177–184.
- **Article-supported:** Analysis used raw acquisitions without wild-spike or
  confidence-index filtering. Source: line 184.
- **Article-supported:** Six nearest neighbors in a 3-micrometer first-order
  shell; pairs above 5 degrees excluded to suppress grain boundaries. About
  50,000–60,000 nearest-neighbor pairs per ROI. Source: lines 186–189.

## Analysis methods

- **Article-supported:** LAM is primary; KAM and LOS test metric dependence.
  All three reproduce the field-exposure trend. Source: Results, lines 274–280.
- **Article-supported:** Low-angle histograms cover 0–5 degrees with 0.1-degree
  bins and interval-censored maximum-likelihood gamma fits. Source: Fig. 8
  caption, lines 289–298.
- **Article-supported:** Table I reports empirical mean and skewness, gamma
  shape `k`, scale `theta`, and `P(LAM > 2 degrees)` with 95% bootstrap
  intervals. Source: lines 300–314 and generated table rows.
- **Article-supported:** Distribution comparisons use KS, chi-squared, and
  Anderson–Darling tests. Mean-versus-radius errors use
  `sigma/sqrt(N_grains)`. Source: lines 316–340; Fig. 9 caption.
- **Article-supported:** Full-range 0–63-degree histograms compare a 20–50-degree
  Mackenzie region and the Sigma 3 twin peak near 60 degrees. Source: lines
  344–359; Fig. 10, PDF p. 7.

## Assumptions and inference boundaries

| Assumption or inference | Status and source |
|---|---|
| Low-angle orientation gradients proxy GND density/plastic activity. | Literature-supported proxy, not an absolute density measurement. Article lines 224–229 and 409. |
| Regions far from craters exclude local arc damage. | Strong design control for local craters; cannot exclude integrated exposure to distant breakdowns. Article lines 386 and 405–409. |
| FE periphery is an internal reference. | Useful but not zero-field: residual field up to about 2.5 MV/m. Article lines 398–403. |
| Grain-size differences do not explain LAM hierarchy. | Supported within FE cathode: mean grain size is nearly constant while LAM drops. Cross-cathode grain size differs modestly. Article lines 198–205. |
| FIB cleaning does not create measurable signal. | Based on shallow AFM-measured removal and identical protocol; robustness against subtle ion damage is not independently demonstrated. Article lines 118–121 and 409. |
| Maxwell stress is the cyclic mechanical load. | Supported for this pulsed-DC geometry because no RF magnetic field or pulsed Ohmic heating is present. Article lines 389–396. |
| Dislocation population is the physical carrier of `E_S`. | Suggested by spatial/statistical agreement; not directly established. Article lines 414–427. |
| Hard-Cu depletion and soft-Cu accumulation are one mechanism at different depths/initial states. | Article discussion/interpretation, lines 372–383; requires depth-resolved confirmation. |

