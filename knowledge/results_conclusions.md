# Results and conclusions

## Directly supported results

### 1. Grain structure is not the spatial driver

- Both cathodes show recrystallized, broadly oriented, equiaxed grains.
- Mean grain diameters across nine ROIs are 26–30 micrometers.
- REF grains are modestly larger than FE grains, approximately 30 versus
  26 micrometers, interpreted as pre-existing cathode-to-cathode variation.
- Within the FE cathode, grain size is essentially constant from center to
  periphery while mean misorientation falls sharply.

Source: `cond26/main.tex`, Results subsection “Grain orientation maps,” lines
195–205; Fig. 4, submitted PDF p. 4.

### 2. Field-exposed regions show higher intragrain misorientation

- LAM maps show widespread low-angle intragrain misorientation in FE center
  and edge regions, lower values in FE periphery and external REF.
- KAM and LOS reproduce the LAM trend.

Source: Results, lines 221–280; Figs. 5–7, submitted PDF p. 5.

### 3. Mean LAM forms a three-tier hierarchy

- FE center and edge: approximately 1.18–1.24 degrees.
- FE periphery: approximately 0.78–0.79 degrees.
- external REF: approximately 0.65–0.71 degrees.
- High-field center/edge mean is about 75% above the external-reference mean
  of approximately 0.68 degrees.

Source: Results, lines 330–342; Fig. 9, PDF p. 6; exact values in
`ebsd2/results/low_angle_moments_rows.tex`, lines 1–9.

### 4. Field exposure mainly stretches the low-angle distribution

- Gamma shape is nearly constant: `k ≈ 2.6–2.9` across ROIs.
- Gamma scale nearly doubles: about 0.22–0.25 degrees for external references
  versus about 0.43–0.46 degrees for FE center/edge.
- Fraction with LAM above 2 degrees rises from approximately 0.013–0.019 in
  REF to approximately 0.133–0.150 in FE center/edge—roughly eightfold.
- Empirical skewness decreases with field exposure: about 2.0–2.3 in REF,
  1.7–1.8 in FE periphery, and 1.3 in FE center/edge. The reference's
  heavier-than-gamma upper tail remains unexplained.

Source: Results, lines 285–328; Fig. 8 and Table I, PDF p. 6; generated table.

### 5. Distribution separation is large and robust

- Every FE center/edge distribution differs from every unexposed distribution
  with `D_KS > 0.25`; against external REF, values exceed 0.31.
- FE periphery versus external REF is much closer, `D_KS ≈ 0.06–0.12`.
- Chi-squared and Anderson–Darling comparisons reach the same qualitative
  conclusion.
- Formal p-values are extreme because each ROI contributes about 50,000 pairs;
  the article therefore emphasizes effect sizes and grain-corrected errors.

Source: Results, lines 316–324; `pairwise_tests.tex`, especially lines 7–29.

### 6. High-angle grain skeleton is preserved

- In the 20–50-degree Mackenzie window, FE regions contain roughly 2–3 times
  more pixel pairs than unexposed regions.
- The Sigma 3 twin fraction near 60 degrees remains similar, approximately
  7–11%, in every sample.

Source: Results, lines 344–359; Fig. 10, PDF p. 7.

**Caution:** `TODO.md`, lines 15–19, records an unresolved proposal to soften
the wording that identifies the mid-angle population as rotated subgrains.
For a talk, say the mid-angle excess is **consistent with** continued
subgrain rotation, not that it proves it.

## Article conclusions

1. Field-exposed copper regions contain a reproducible, large-area,
   dislocation-sensitive structural difference from both internal low-field
   and external unexposed controls. Source: Conclusions, lines 430–435.
2. The spatial ordering follows decreasing field exposure and the predicted
   ordering of `E_S`. Source: lines 437–438.
3. The data support collective dislocation dynamics as part of conditioning
   and suggest that the evolving subsurface dislocation population may be the
   physical process tracked by `E_S`. This is a suggested mechanism, not a
   direct identification. Source: lines 437–443.
4. The authors claim this is the first large-area, spatially resolved
   observation of dislocation-related structural differences between
   conditioned and unconditioned high-field-electrode regions. Source:
   abstract, lines 39–42; Conclusions, lines 433–435.

## Suggested presentation interpretation

The strongest defensible conference message is:

> Conditioning leaves a measurable subsurface structural memory in copper.
> Its spatial and statistical organization is consistent with accumulated
> dislocation activity and makes the dislocation population a candidate—not
> yet a proven identity—for the phenomenological conditioning state `E_S`.

This wording preserves the novelty while separating observation from
mechanistic inference.

