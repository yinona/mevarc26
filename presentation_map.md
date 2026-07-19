# Proposed presentation map — for review before slide authoring

No Beamer slides should be written or modified until this map is approved.

## Proposed communication job

By the end, a MeVArc audience should understand that high-field conditioning
leaves a large-area, field-correlated subsurface structural signature in
heat-treated copper, and should see the depth-resolved/RFX program as a
discriminating test of whether evolving dislocation structure is the physical
state tracked by conditioning.

## Central message

**Observation:** High-field regions show substantially higher intragrain
misorientation than low-field and unexposed controls, with a three-tier spatial
hierarchy and a broadened distribution.

**Interpretation:** The result is consistent with accumulated, field-driven
dislocation activity and makes subsurface dislocation structure a candidate
microstructural correlate of `E_S`.

**Boundary:** The experiment does not yet establish causality, the depth
profile, or universality across samples/materials/loading modes.

## Audience takeaway

Conditioning is no longer only an operational history or fitted state
variable: it now has a directly observed large-area structural correlate. The
next decisive experiments must connect lateral exposure to depth and test a
material/loading contrast.

## Recommended balance and arc

- Nominal length: 30 minutes.
- Core talk: 15 slides, approximately 24–26 minutes.
- Questions/buffer: 4–6 minutes.
- Content balance: about 70% copper article, 30% limitations and future tests.
- Arc: operational puzzle -> evidence gap -> controlled experiment -> visual
  observation -> quantitative hierarchy -> interpretation -> limits ->
  discriminating next experiments.

## Extended introduction for the expected audience

The introduction should assume familiarity with vacuum breakdown and
conditioning, but not with EBSD analysis or dislocation screening.

1. Start from the operational fact: conditioning determines the usable field
   of high-gradient devices, but the metal variable being changed is unknown.
2. Introduce `E_S` as a phenomenological local history variable—not as an
   established material property.
3. Summarize why dislocations are plausible in three pieces only:
   material/crystal-structure trends, MDDF/dark-current evidence, and local TEM
   depletion.
4. State the precise missing experiment: a large-area structural comparison
   across controlled exposure on one electrode.
5. Explain why the sloped-anode cathode is unusually powerful: position is a
   controlled exposure coordinate, and periphery/reference regions provide
   internal and external controls.
6. Teach only the EBSD concept needed to read the data: low-angle intragrain
   orientation gradients proxy GND/plastic activity; grain boundaries are
   excluded.

Suggested spoken transition into results:

> If conditioning really leaves a material memory, the map should know where
> the field was high—even far from individual breakdown craters.

## Slide-by-slide narrative

### Section I — The missing material state

#### 1. Title: “What does conditioning change inside the electrode?”

- Job: pose the scientific problem, not summarize the answer.
- Visual: minimal title; one restrained cathode/EBSD texture or no figure.
- Transition: conditioning works operationally; the microscopic memory is
  unknown.

#### 2. “Conditioning requires a local memory, but `E_S` has no microscopic identity”

- Highlight: conditioning, pulse-count dependence, phenomenological `E_S`.
- Equation/figure: none required; a compact conceptual sequence is optional.
- Evidence: article Introduction lines 52–66.
- Transition: ask what material degree of freedom can retain that history.

#### 3. “Dislocation dynamics explain several clues—but the structural evidence was local”

- Highlight: MDDF, material ordering, dark-current spikes, 200-nm TEM denuded
  zone.
- Equation: Maxwell stress may appear here or on the next slide.
- Avoid: a literature laundry list.
- Transition: the missing scale is the full conditioned area.

### Section II — A spatially controlled experiment

#### 4. “A sloped anode turns radius into an exposure coordinate”

- Figure: Fig. 1 geometry, optionally paired with Fig. 3 field profile.
- Highlight: 80 MV/m center; 69–77 MV/m edge; low-field periphery; one cathode.
- Transition: this geometry supplies internal controls that ordinary before/after
  comparisons lack.

#### 5. “We map intrinsic structure, not the aftermath of a crater”

- Figure: Fig. 2a ROI far from craters.
- Highlight: nine ROIs; identical cleaning/acquisition; separate unexposed
  cathode.
- Mention: field and breakdown density still covary at the integrated-history
  level.
- Transition: explain what EBSD can read from each ROI.

#### 6. “Low-angle EBSD reveals intragrain lattice curvature”

- Figure: Fig. 5 wide-scale versus low-angle-scale pair.
- Highlight: LAM, corroborated by KAM and LOS; 3-micrometer kernel; GND proxy.
- Keep equations off this slide unless necessary.
- Transition: with the scale fixed, compare exposed and unexposed regions.

### Section III — The structural signature

#### 7. “High-field regions contain visibly more intragrain misorientation”

- Figure: Fig. 7 FE edge versus matched REF edge, same 0–5-degree scale.
- Highlight: qualitative spatial observation before statistics.
- Transition: quantify all nine ROIs.

#### 8. “Mean misorientation follows a three-tier exposure hierarchy”

- Figure: Fig. 9, large and legible.
- Numbers: about 1.2 degrees high field, 0.79 periphery, 0.68 external REF;
  approximately 75% high-field/reference difference.
- Highlight grain-corrected errors and within-FE grain-size independence.
- This is the primary result slide.
- Transition: the mean hides how the population changed.

#### 9. “Field exposure builds an eightfold high-misorientation tail”

- Figure: Fig. 8 low-angle distributions.
- Numbers: `P(LAM > 2 degrees)` approximately 0.14 versus 0.016.
- Gamma result: common `k ≈ 2.7`; scale approximately doubles.
- Statistical result: `D_KS > 0.25` against all unexposed distributions.
- Caveat: emphasize effect size, not tiny p-values from many correlated pairs.
- Transition: ask whether the grain skeleton itself changed.

#### 10. “The annealed grain skeleton remains intact”

- Figure: either Fig. 4 IPF/grain-size summary or Fig. 10 full-range histogram.
- Recommended main-path content: Sigma 3 fraction unchanged; field-dependent
  change is intragrain/subgrain, not wholesale grain-boundary reconstruction.
- Wording: mid-angle excess is **consistent with** continued subgrain rotation.
- Removable if time is tight.
- Transition: what physical process can create this selective change?

### Section IV — Interpretation with boundaries

#### 11. “A billion tiny Maxwell-stress cycles can accumulate a structural memory”

- Equation: `sigma_M = epsilon_0 E^2/2 ≈ 0.028 MPa` at 80 MV/m.
- Highlight: no RF pulsed heating or bulk-current electroplasticity; cumulative
  MDDF/VHCF analogy, not direct stress-amplitude equivalence.
- Suggested interpretation: field -> repeated Maxwell stress -> dislocation
  rearrangement -> observed orientation gradients.
- Transition: connect the measured hierarchy to conditioning phenomenology.

#### 12. “Misorientation is a candidate structural correlate of `E_S`”

- Evidence: three-tier ordering matches predicted `E_S` ordering; gamma shape
  approximately fixed while scale changes.
- State explicitly: qualitative match, not point-by-point calibration or causal
  identification.
- Avoid the phrase “we measured `E_S`.”
- Transition: the strongest claim depends on acknowledging what remains
  unresolved.

#### 13. “The experiment establishes an effect, not yet a universal mechanism”

- Limitations: one FE cathode/one REF; field and breakdown density covary;
  relative EBSD values; unresolved depth; periphery is low-field, not zero-field.
- Alternative interpretations: preparation heterogeneity, integrated distant
  breakdown exposure, fringe-field versus baseline variation.
- Transition: each limitation motivates a specific next experiment.

### Section V — Discriminating next experiments

#### 14. “The next coordinate is depth”

- Visual: conceptual depth axis or site-specific high-field/reference pair;
  do not imply measured profile.
- Concrete plan: pilot matched FIB lamellae; identical artifact controls;
  low-energy polish; correlated TEM/STEM and EBSD through the top approximately
  1 micrometer.
- Scientific question: do 200-nm depletion and deeper accumulation join into
  one redistribution profile?
- Transition: depth tests one material; a material/loading contrast tests
  generality.

#### 15. “Stainless steel tests whether the memory survives a change of material and loading”

- RFX framing: AISI 304, lower stacking-fault energy, metastable austenite,
  continuous DC, two exposed and two matched references, apex-to-periphery
  gradient.
- Keep preliminary SEM/EBSD observations off the main slide unless updated and
  approved.
- State the falsifiable outcomes:
  - field-correlated SS response supports generality;
  - different response identifies material-specific carriers;
  - no resolved response constrains depth/loading/sensitivity.
- Closing takeaway: structural memory is now observable; its identity is the
  next question.

## Results deserving the most emphasis

1. Fig. 9 three-tier hierarchy and approximately 75% effect.
2. Fig. 8 distribution stretch and approximately eightfold tail.
3. Agreement of LAM, KAM, and LOS.
4. Internal-control logic: same FE cathode, low-field periphery, ROIs away from
   craters.
5. Preserved grain/twin skeleton as a constraint on what changed.

## Limitations and alternative interpretations to keep visible

- One conditioned cathode and one external reference.
- Field level and breakdown density are not independently varied.
- Pixel-pair p-values overstate independent sample count; effect sizes and
  grain-corrected errors are more communicative.
- LAM is a relative GND proxy at a fixed step size, not an absolute density.
- FIB and indexing artifacts are controlled by identical protocol but not
  exhaustively eliminated.
- The depth reconciliation and `E_S` identity are hypotheses.
- The mid-angle/subgrain statement should be softened pending confirmation.

## Concrete versus speculative future directions

### Concrete

- matched high-field/reference pilot lamellae;
- artifact floor and low-energy final polishing;
- depth-resolved TEM/STEM through approximately 1 micrometer;
- finer radial EBSD for quantitative `E_S(r)` comparison;
- additional cathode replication;
- RFX field-gradient EBSD with phase mapping and matched references.

### Speculative

- pulse-spectrum coupling to dislocation resonances;
- cross-material/loading “phase diagram” of conditioning response;
- extension to RF, cryogenic, BCC, and HCP systems.

Speculative items should be labeled as hypotheses and kept to the close or
backup.

## Optional/removable slides if the talk runs long

1. Slide 10: full-range histogram / Sigma 3 preservation.
2. Detailed EBSD-method slide: compress slides 5–6 into one.
3. Separate limitations slide: integrate its caveats into slides 8, 9, and 12.
4. RFX preliminary-observation slide, if later approved; otherwise backup only.
5. Backup: exact Table I values and pairwise test matrix.
6. Backup: hard-versus-soft copper depth-screening derivation.
7. Backup: RFX FIB-induced martensite artifact protocol.

## Open scientific questions for review

1. Is `E_S` correlation the final destination of the talk, or should the talk
   end more conservatively on “large-area structural memory”?
2. Do you endorse the hard/soft copper depth-reconciliation model strongly
   enough for a main-path slide?
3. Should Fig. 10's mid-angle excess remain in the main talk after the wording
   concern in `TODO.md`?
4. Has newer data changed the one-cathode limitation or RFX status?
5. Can field and breakdown exposure be partially decorrelated using the
   Bjelland simulation/history data beyond the current three-tier comparison?
6. Is there a quantitative estimate of EBSD information depth for this copper
   acquisition that should replace qualitative “deeper than TEM surface zone”
   language?

## Open presentation-design questions for review

1. Is the audience primarily breakdown specialists, materials scientists, or a
   mixed MeVArc audience?
2. Does the 30-minute slot include questions?
3. Should the narrative use `E_S` early, or delay it until after the structural
   evidence to reduce model overhead?
4. Should RFX appear only as a clean future-direction experiment, or may
   approved preliminary SEM/EBSD observations be shown?
5. Preferred style: restrained HUJI/RFX palette, existing internal RFX style,
   or another reference deck?
6. Which collaborators and logos must appear on the title and acknowledgments?

## Approval gate

Before Beamer authoring, please approve or revise:

- the central message and claim strength;
- the 15-slide core narrative;
- the 70/30 copper-to-future balance;
- whether Slide 10 and preliminary RFX material remain in the main path;
- the proposed style direction in `knowledge/style_inventory.md`.

