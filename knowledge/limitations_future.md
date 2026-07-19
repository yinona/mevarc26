# Limitations, unresolved issues, and future directions

## Article-stated limitations

1. **Single conditioned cathode and single reference.** The approximately 75%
   difference describes this material state and conditioning history, not a
   universal conditioning effect. Source: `cond26/main.tex`, Discussion,
   lines 405–406.
2. **Field and breakdown density covary.** The design cannot separate field
   level from integrated breakdown exposure. Distance from craters excludes
   local damage but not distant-breakdown history. Source: lines 407–408.
3. **Relative, protocol-dependent EBSD values.** Absolute LAM depends on the
   3-micrometer step and indexing precision. Source: line 409.
4. **Spatial agreement with `E_S` is qualitative.** A quantitative radial
   comparison needs finer steps and more positions. Source: lines 414–427.
5. **Depth is unresolved.** The article reconciles TEM depletion and EBSD
   accumulation through an inferred depth/initial-state picture but does not
   measure the connecting profile. Source: Discussion lines 372–383; interim
   report lines 40–44.
6. **Skewness trend remains unexplained.** Reference distributions retain a
   heavier-than-gamma tail. Source: article line 425.

## Alternative interpretations to address explicitly

- **Pre-existing spatial heterogeneity:** reduced by within-cathode comparison,
  but not eliminated at every length scale. Grain-size hierarchy argues against
  a simple grain-size explanation. Source: lines 198–205 and 398–403.
- **Preparation/FIB artifact:** protocols were identical and removal was shallow,
  but subtle ion-induced orientation effects were not independently mapped.
  Source: lines 118–121 and 409. This is especially important when extrapolating
  to metastable stainless steel.
- **Breakdown exposure rather than field exposure:** not separable in this
  dataset. Pulse-count scaling in prior work favors field-driven evolution but
  does not prove causality here. Source: lines 405–409.
- **LAM as defect/noise rather than GND:** agreement among LAM, KAM, and LOS and
  the spatial hierarchy strengthen the plasticity interpretation, but no
  absolute GND inversion or same-site TEM confirmation is reported.
- **Residual periphery signal:** article interprets it as consistent with fringe
  field. It could also include cathode-scale baseline variation; present this as
  consistency, not proof. Source: lines 398–403.
- **Mid-angle population:** consistent with rotated subgrains, but `TODO.md`
  records a request to soften the current wording. Avoid using it as an
  independent proof of continued GND accumulation.

## Concrete future directions supported by project plans

1. **Pilot site-specific FIB lamellae** from one high-field ROI and one matched
   reference, both already mapped by EBSD. Source:
   `reports/2026_interim/workplan.tex`, lines 23–30.
2. **Artifact-controlled depth-resolved TEM/STEM** through the top approximately
   1 micrometer, using identical reference processing and low-energy final
   polishing. Source: work plan lines 31–40.
3. **Finer-step EBSD at additional radii** for quantitative comparison with
   predicted `E_S(r)`. Source: work plan lines 41–43 and article line 427.
4. **Replicate on additional cathodes** to separate universal response from
   sample/history specificity. Source: article limitation line 406 and interim
   report line 42.
5. **RFX AISI 304 comparison** with two field-exposed and two batch-matched
   references, sampling apex-to-periphery field variation. Source: work plan
   lines 46–59; `rfx/PLAN.md`.
6. **RFX phase mapping** for possible austenite-to-martensite transformation,
   with explicit ion-beam artifact controls. Source: `rfx/PLAN.md`; `rfx/STATUS.md`
   open question 7.
7. **Inclusion cross-sections and census** to distinguish ruptured native
   inclusions from arc damage or preparation pull-out. Source: `rfx/STATUS.md`,
   open question 5; `rfx/REVIEW_NOTES.md`.

## Speculative directions from the article

- **Pulse-spectrum/dislocation-resonance coupling.** Article conclusion lines
  440–443. This is explicitly speculative; it needs a dedicated hypothesis and
  experiment before receiving more than one sentence in the talk.
- **Other crystal structures, RF-conditioned structures, and cryogenic
  cathodes.** Article lines 441–443. This is a broad universality program, not a
  result.
- **Suggested interpretation:** A combined material-by-loading matrix—soft Cu
  pulsed DC, hard Cu pulsed DC, stainless steel continuous DC, RF copper, and
  cryogenic copper—could distinguish dislocation mobility, initial state,
  cyclic spectrum, and thermal loading. This synthesis is not stated as such in
  the article and requires approval before presentation.

## RFX-specific unresolved inputs

The RFX status is dated 2026-07-13 and may be stale.

- Exact alloy/sub-grade: drawing says AISI 304; 304 versus 304L remains
  unresolved without the certificate. Source: `rfx/STATUS.md`, lines 24–27 and
  123–125.
- Conditioning report and breakdown log were not received. Source: lines
  64–74 and 128–129.
- Numerical field-versus-angle vector remained outstanding. Source: lines
  130–131.
- Only the first EBSD acquisitions were summarized: reference #1-25 good,
  exposed #4-25 poor pattern quality; causal interpretation unresolved. Source:
  lines 76–98.
- Preparation-induced BCC transformation in metastable austenite is a critical
  artifact risk. Source: `STATUS.md`, open question 7; interim work plan lines
  56–59.

