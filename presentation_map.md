# Proposed presentation map — review-weighted talk (for review before slide edits)

> **Status note.** A full 18-slide Beamer deck already exists in `main.tex`
> (with compiled `main.pdf` / `main-notes.pdf`), written before this map was
> approved. That deck is a **two-project status talk**: 2 background slides,
> 6 copper slides, 7 RFX slides. This map re-plans it as a **review talk** that
> develops background and past results, centers on the copper (cond26) result,
> and treats RFX as a hint at the future. **No edits to `main.tex` should be
> made until this map is approved.**

## Data-gathering status (2026-07-20) — complete

- **Figures:** all missing cond26 figures copied into `figures/` (see the
  figure section below). Slides 8 and 11 no longer need placeholders.
- **Sources:** 11 backing PDFs collected into `sources/` — the three Engelberg
  MDDF papers (PRL 2018, PRAB 2019, PRAB 2020), Jacewicz JAP 2025, the cond26
  manuscript PDF, the MeVArc 2025 deck, Wuensch RMP 2026, Nordlund–Djurabekova
  2012, Korsback 2020, and the group's MeVArc 2024 + 2013 decks. Full mapping
  in `knowledge/source_inventory.md` ("Collected source files" section).
  **Not found:** Degiovanni PRAB 2016, Mughrabi 2009, Stanzl-Tschegg 2007
  (cited from `../cond26/refs.bib` only).
- **Status refresh:** Q14–16 answered in
  `knowledge/status_refresh_2026-07-20.md` — no new copper data; RFX #2-25/
  #3-25 unconfirmed after 13 Jul; cond26 submitted to PRAB 2026-06-23.
- **Not done on purpose:** no edits to `main.tex` and no compile — awaiting
  the user's answers in `QUESTIONS.md`.

## Format decisions (confirmed 2026-07-19)

- **Length:** 30 minutes **excluding** questions → room for ~16–18 core slides.
- **Balance:** review-weighted — about **30% background / 45% copper / 15%
  limits+future**, versus the current deck's copper/RFX co-headline.
- **RFX on the main path:** **two slides** — one "future directions" slide and
  one stainless-steel preview. All RFX electrode/SEM/EBSD/artifact detail moves
  to backup.
- **Closing claim strength:** **candidate structural basis for `E_S`** — the
  article's careful wording, not "we measured `E_S`."
- **`E_S` is delayed, not a background pillar.** The narrative spine is the
  group's own program — the MDDF dislocation model, the local Uppsala TEM
  microscopy, then the large-area cond26 test. `E_S` appears only once, late,
  in the interpretation, as a secondary phenomenological correlate.
- **Two prior-work links are strengthened:** (1) the MDDF dislocation-dynamics
  model (Engelberg & Ashkenazy, PRL 2018 / PRAB 2019) whose central prediction
  cond26 tests; (2) the prior microscopy (Jacewicz et al., Uppsala/FREIA, JAP
  2025) whose local denuded-zone observation cond26 extends to large area.
- **This talk is the explicit sequel to MeVArc 2025.** The 2025 HUJI talk
  ("Observing plastic evolution related to high-field conditioning") presented
  the MDDF model and the local STEM/FIB microscopy, and closed by asking *"much
  more comparative forensics — other materials? more samples?"* cond26 is the
  large-area answer; RFX answers "other materials?". Use a "last year / this
  year" callback as the Part I → Part II bridge and as the closing bookend.

## Continuity with MeVArc 2025 (source: `mevarc25_huji_v2.pdf`)

The audience largely overlaps with last year's, so build on the 2025 narrative
rather than re-deriving it:

- **2025 spine:** MDDF critical-transition model → model-vs-observation (rate
  vs field at T = 100/400 K; dark-current hypoexponential spikes) → post-BD
  SEM/plasma deposition → sub-surface predictions → STEM/FIB microscopy →
  denuded zones in the top ~100 nm of conditioned Cu (300 K and 30 K) →
  field-exposed vs reference comparisons → "method and its limits established;
  what next? other materials? more samples?"
- **2025 assets worth reusing** (embedded in `.pptx`, extract if approved): the
  MDDF governing-equation/critical-transition schematic; the rate-vs-field fit
  curves; the dark-current spike distribution; representative cross-sectional
  STEM denuded-zone panels; the FIB "red herring" artifact examples.
- **2025 lesson to carry into RFX:** FIB sample production generates dislocation
  artifacts ("red herrings") that masquerade as structure; large-scale features
  survive but fine structure does not. This is first-hand justification for the
  RFX depth-artifact controls.
- **Number to reconcile:** the 2025 talk says the modification is limited to the
  **top ~100 nm**, while `cond26/main.tex` and Jacewicz JAP 2025 quote
  **~200 nm** (and Groma `ℓ_D ~ 100 nm`). Pick one consistent figure for 2026.

## Proposed communication job

By the end, a MeVArc audience should understand (1) that the group's MDDF model
predicts conditioning is collective mobile-dislocation evolution driven by the
Maxwell stress, (2) that prior microscopy (the Uppsala TEM study) saw the
predicted structural change but only locally, (3) that cond26 provides the
first large-area structural confirmation — a field-correlated subsurface
misorientation signature in copper — and (4) how a depth-resolved and
stainless-steel program tests whether the effect is universal.

## Central message

**Model (prior):** The mobile-dislocation-density fluctuation (MDDF) model of
Engelberg & Ashkenazy treats breakdown initiation and conditioning as collective
dislocation dynamics driven by the tensile Maxwell stress, and reproduces the
`E^30` breakdown-rate scaling and dark-current behaviour. Its central prediction
is that conditioning evolves the near-surface dislocation structure.

**Microscopy (prior, local):** Cross-sectional TEM of conditioned copper (the
Uppsala/FREIA study, Jacewicz et al., with Popov and Ashkenazy) found a local
~200-nm dislocation-denuded zone — direct but single-site structural evidence.

**New result (center):** Large-area EBSD shows high-field copper regions with
substantially higher intragrain misorientation than low-field and unexposed
controls, in a three-tier spatial hierarchy with a broadened distribution — the
missing large-area structural test.

**Interpretation (careful, `E_S` delayed):** The result is the first large-area
confirmation of the MDDF prediction and is consistent with accumulated,
field-driven dislocation activity; the spatial ordering also tracks the
phenomenological conditioning variable `E_S`, making the evolving subsurface
dislocation population a **candidate structural basis** for `E_S` — not a proven
identity.

**Boundary:** One conditioned cathode; causality, depth profile, and
universality are not yet established.

## Audience takeaway

The dislocation picture of conditioning now has direct large-area structural
support, not just a model and a single TEM cross-section. The next decisive
experiments connect lateral exposure to depth and test a material/loading
contrast.

## Recommended balance and arc

- Core talk: about 16–18 slides, ~28 minutes; questions after the slot.
- Arc: operational problem → MDDF model and its prediction → prior local
  microscopy and its limit → why a sub-yield Maxwell stress can matter →
  controlled copper experiment → visual observation → quantitative hierarchy →
  distribution stretch → confirmation of the model (+ delayed `E_S` note) →
  limits → depth and cross-material future.
- Reuse the existing deck's copper slides and visual conventions; the main work
  is **re-spining Part I around MDDF + microscopy** and **shrinking RFX to two
  slides**.

## Extended introduction for the expected audience

Assume familiarity with vacuum breakdown and conditioning; do not assume EBSD
or dislocation-screening background. This is a genuine review of the group's
program, so the introduction builds the model-then-microscopy case before the
new data. `E_S` is deliberately withheld until the interpretation.

1. Operational fact: conditioning sets the usable field; breakdown rate scales
   roughly as `E^30`; conditioning tracks high-field **pulse count** more than
   breakdown count, implying the field itself drives conditioning, not arc
   damage.
2. The model: FCC/BCC/HCP field-holding ordering ~ barriers to dislocation
   motion; the MDDF model treats breakdown/conditioning as collective
   mobile-dislocation dynamics under the Maxwell stress and reproduces the
   `E^30` and temperature trends and dark-current behaviour. **Its central
   prediction — conditioning evolves the near-surface dislocation structure —
   is the hypothesis this talk tests.**
3. The prior microscopy: the Uppsala TEM study found a local ~200-nm denuded
   zone in conditioned copper, plus the hard-vs-soft conditioning contrast —
   direct structural evidence, but local and hard to extrapolate.
4. Why a tiny Maxwell stress can matter: `σ_M = ε₀E²/2 ≈ 0.028 MPa`, ~10³ below
   yield, but VHCF shows sub-yield cycling over ~10⁹ pulses accumulates
   irreversible rearrangement, and the MDDF description is threshold-free.
5. Name the precise missing experiment: a **large-area** structural comparison
   across controlled exposure on one electrode — the gap the model and the
   local microscopy both leave open.
6. Teach only the EBSD concept needed: low-angle intragrain orientation
   gradients proxy GND/plastic activity; grain boundaries are excluded.

Suggested spoken transition into results (the 2025 → 2026 bridge):

> Last year I showed this model and our STEM cross-sections, and ended by asking
> for more comparative forensics — other materials, more samples. This year we
> answer part of that: a full-electrode map that should know where the field was
> high, even far from breakdown craters.

## Slide-by-slide narrative

### Part I — A model, local microscopy, and the missing large-area test (~4 slides)

#### 1. Title: "Does conditioning leave a structural memory?"

- Job: pose the scientific problem; signal a review that lands on a new result.
- Visual: restrained title; existing title frame is reusable.

#### 2. "Conditioning works — but the mechanism is unknown"

- Highlight: conditioning raises voltage holding; steep `E^30` breakdown-rate
  scaling; conditioning tracks high-field **pulse count**, not breakdown count →
  the field, not arc damage, drives conditioning.
- Evidence: Introduction lines 52–53, 66; Wuensch et al. RMP 2026; Degiovanni
  et al. PRAB 2016.
- **Do not introduce `E_S` here** (delayed to Slide 12).
- Reuse: current Slide 2 left column and the exposure/field-holding sketch;
  drop its `E_S` box.

#### 3. "Our model: conditioning as collective dislocation dynamics (MDDF)"

- **Strengthened prior-work link (model).** Field-holding order FCC→BCC→HCP
  tracks barriers to dislocation motion; the thermodynamic defect model
  (Nordlund–Djurabekova) couples field stress to near-surface loop formation.
- The **MDDF model** (Engelberg, Ashkenazy et al.): breakdown initiation as a
  critical transition in collective mobile-dislocation motion driven by the
  tensile Maxwell stress; reproduces the `E^30` scaling and temperature
  dependence; pre-breakdown dark-current spikes are consistent with it.
- **Central prediction to foreground:** conditioning evolves the near-surface
  dislocation structure — the hypothesis cond26 tests.
- Reusable 2025 figures (already copied to `figures/`, see
  `knowledge/mevarc25_assets.md`): `mddf_critical_transition.png` (the `dn/dt`
  vs `n` runaway schematic), `mddf_rate_vs_field.png` (the steep `~E^30`
  scaling), and `mddf_nucleation_rate.png` (rate vs `E − E_th`).
- Evidence: Introduction lines 56–61; `engelberg_stochastic_2018` (PRL 120,
  124801, 2018); `engelberg_theory_2019` (PRAB 22, 083501, 2019);
  `engelberg_dark_2020` (PRAB 23, 123501, 2020); `nordlund_defect_2012`;
  `serafim_effects_2025`.
- Replaces the current deck's `E_S` slide.

#### 4. "Prior microscopy saw the structure — but only locally (Uppsala TEM)"

- **Strengthened prior-work link (microscopy) — this is our own 2025 STEM
  work.** Cross-sectional STEM/TEM of conditioned copper (Jacewicz &
  Profatilova, Uppsala/FREIA; Popov, HUJI; with Ashkenazy) revealed a
  dislocation-denuded zone in the top ~100–200 nm of field-exposed regions
  (both 300 K and 30 K) — the first *direct* structural evidence of field-driven
  near-surface plasticity. Reusable figures already in `figures/`:
  `stem_denuded_zone.png` (denuded band, 100/200 nm scale bars) and the
  `stem_fe_300k.png` / `stem_ref_300k.png` field-exposed-vs-reference pair.
- Support: soft (heat-treated) copper conditions more slowly than hard
  (as-machined) copper, consistent with different initial dislocation
  populations.
- **Carry the 2025 "red herring" caution:** FIB preparation itself generates
  dislocation artifacts; only large-scale structure survives. This both scopes
  the microscopy claim and pre-motivates the RFX artifact controls.
- **Limit that motivates cond26:** STEM/TEM is highly local and hard to
  extrapolate to the full electrode → the large-area structural comparison was
  still missing; the 2025 talk closed on exactly this ("other materials? more
  samples?").
- Fold the Maxwell-stress/VHCF point (`σ_M ≈ 0.028 MPa`, ~10⁹ sub-yield cycles,
  threshold-free MDDF) into this slide or a compact half-slide, so Part I stays
  at ~4 slides.
- Evidence: Introduction lines 63–71, 113; `jacewicz_surface_2025` (JAP 137,
  193302, 2025); `korsback_vacuum_2020`; `mughrabi_cyclic_2009`;
  `stanzl-tschegg_vhcf_2007`; MeVArc 2025 deck.
- **New/strengthened slide** relative to the current deck.

### Part II — The copper result (center, ~7 slides)

#### 5. "One cathode turns field exposure into a controlled coordinate"

- Figure: Fig. 1 geometry (`electrode_geometry.png`); optionally Fig. 3 field
  profile (`efield_vs_radius.eps`, needs copying).
- Highlight: 80 MV/m center; ~69–77 MV/m edge; low-field periphery; one cathode
  plus a separate unexposed reference.
- Reuse: current Slide 4.

#### 6. "EBSD maps plastic activity far from breakdown craters"

- Figure: Fig. 2a (`sem_lowmag.png`).
- Highlight: ROIs hundreds of microns from craters; identical cleaning; LAM
  primary, KAM/LOS as cross-checks; misorientation as GND proxy; EBSD chosen
  precisely because TEM is only local.
- Evidence: Methods lines 113, 177–189.
- Reuse: current Slide 5.

#### 7. "How to read a LAM map: wide-angle vs low-angle"

- Figure: Fig. 5 pair — `lam_widescale.png` (0–50°) and `lam_lowscale.png`
  (0–5°, needs copying).
- Job: teach the metric before the comparison.
- **Relocated slide.** In the current deck `lam_widescale.png` is used on the
  distribution slide, which is a mismatch to fix.

#### 8. "High-field copper contains more intragrain curvature"

- Figure: `lam_fe_center.png` vs `lam_ref_edge.png`, same 0–5° scale.
- Highlight: qualitative spatial observation before statistics.
- Reuse: current Slide 6.

#### 9. "The signal separates into three exposure tiers"

- Figure: Fig. 9 (`mean_vs_radius.pdf`).
- Numbers: ~1.2° high field; ~0.79° periphery; ~0.68° external REF; ~75%
  difference; grain size does not follow the hierarchy.
- Primary result slide. Reuse: current Slide 7.

#### 10. "Field exposure populates a high-misorientation tail"

- Figure: Fig. 8 (`low_angle_overlay.pdf`, needs copying) — **replace** the
  current wide-scale LAM image here.
- Numbers: `P(LAM > 2°)` ~0.14 vs ~0.016 (~8×); common gamma `k ≈ 2.7`, scale
  roughly doubles; `D_KS > 0.25` against all unexposed distributions.
- Caveat: emphasize effect size and grain-corrected errors, not tiny
  correlated-pixel p-values. Reuse: current Slide 8 (swap figure).

#### 11. "The large-area test confirms the MDDF prediction"

- **Payoff slide — closes the loop to Part I.** Lead: cond26 is the first
  large-area confirmation that conditioning evolves the near-surface dislocation
  structure, the central MDDF prediction. Chain: field → Maxwell stress (~10⁹
  cycles) → dislocation rearrangement → measured LAM hierarchy.
- Connect to microscopy: EBSD **extends the local Uppsala TEM observation** to
  the full conditioned region; the surface denuded zone and the deeper
  accumulation are reconciled at different depths (Groma screening length
  `ℓ_D ~ 100 nm` matches the ~200-nm zone).
- **Delayed `E_S` note (secondary):** the three-tier spatial ordering also
  follows the phenomenological `E_S(r)` profile from the conditioning
  simulations, so the dislocation population is a **candidate structural basis**
  for `E_S`. Keep this to one line; do not say "we measured `E_S`."
- Evidence: Introduction lines 61, 80; Discussion lines 369–385, 411–427.
- Reuse: current Slide 9, re-led on MDDF rather than on `E_S`.

#### (Optional) "The annealed grain skeleton stays intact"

- Figure: Fig. 10 (`full_range_overlay.pdf`, needs copying) or Fig. 4 IPF pair.
- Content: Σ3 fraction unchanged; change is intragrain/subgrain. Say the
  mid-angle excess is **consistent with** continued subgrain rotation (per the
  `TODO.md` wording concern).
- **Removable** if the talk runs long (first to cut).

### Part III — Limits and hints at the future (~4 slides, two RFX)

#### 12. "Copper establishes the effect, not universality"

- Split: established (large-area difference; three metrics; internal + external
  controls; confirms the MDDF prediction; ordering consistent with `E_S`) vs
  open (depth profile; grain-orientation dependence; more cathodes;
  cross-material generality).
- Transition slide. Reuse: current Slide 10.

#### 13. "Two next coordinates: depth and a change of material"

- **RFX slide 1 of 2 (future directions).** Merge the depth program and the
  cross-material motivation.
- Concrete depth plan: matched high-field/reference pilot FIB lamellae;
  identical artifact controls (informed by the 2025 "red herring" experience);
  low-energy final polish; correlated TEM/STEM + EBSD through the top ~1 µm —
  does the ~100–200-nm surface depletion join the deeper accumulation into one
  redistribution profile? (Directly continues the 2025 Uppsala STEM line.)
- Cross-material motive: stainless steel changes stacking-fault energy,
  dislocation mobility, and loading mode.
- Condenses current Slides 11 and 16; artifact detail goes to backup.

#### 14. "Stainless steel: a deliberately difficult, falsifiable test"

- **RFX slide 2 of 2 (preview).** AISI 304, lower SFE, metastable austenite,
  continuous DC, two exposed + two matched references, apex-to-periphery
  gradient.
- Falsifiable outcomes: field-correlated SS response supports generality; a
  different response identifies material-specific carriers; no resolved response
  bounds depth/loading/sensitivity.
- Keep preliminary SEM/EBSD observations **in backup**, labeled and only if
  approved. Condenses current Slides 12–15, 17.

#### 15. "Conditioning appears to leave a subsurface memory"

- Recap along the program spine: MDDF predicted structural evolution; the 2025
  Uppsala STEM saw it locally; cond26 confirms it large-area (~75%); depth and
  stainless steel test whether the memory survives a change of length scale,
  alloy, and loading. One-line `E_S` candidate close.
- **Bookend the 2025 talk:** last year closed on "other materials? more
  samples?"; this year delivers the large-area copper answer and hands off to
  the stainless-steel/depth program — the next round of comparative forensics.
- Reuse: current Slide 18; `infographic.pdf` optional.

## Figures to copy from `cond26/figures/` into `mevarc26/figures/`

**DONE (2026-07-20).** All copied into `figures/`:

- `low_angle_overlay.pdf` (Fig. 8) — real distribution/tail plot for Slide 10.
- `lam_lowscale.png` (Fig. 5b) — pair with `lam_widescale.png` for Slide 7.
- `efield_vs_radius-eps-converted-to.pdf` (Fig. 3) — optional field profile
  for Slide 5 (already PDF; no eps conversion needed).
- `full_range_overlay.pdf` (Fig. 10) and IPF maps (`ipf_fe_center.png`,
  `ipf_ref_center_keyed.png`, `ipf_key.png`) — available if the optional
  grain-skeleton slide is kept.

## Results deserving the most emphasis

1. Confirmation of the MDDF prediction by a large-area structural measurement.
2. Fig. 9 three-tier hierarchy and ~75% effect.
3. Fig. 8 distribution stretch and ~8× tail.
4. Agreement of LAM, KAM, and LOS.
5. Internal-control logic: same cathode, low-field periphery, ROIs away from
   craters; continuity with the Uppsala TEM cross-sections.

## Limitations and alternative interpretations to keep visible

- One conditioned cathode and one external reference.
- Field level and breakdown density are not independently varied.
- Pixel-pair p-values overstate independent sample count; report effect sizes
  and grain-corrected errors.
- LAM is a relative GND proxy at fixed step size, not an absolute density.
- FIB/indexing artifacts controlled by identical protocol, not exhaustively
  eliminated.
- Depth reconciliation and `E_S` identity are hypotheses.
- Soften the mid-angle/subgrain statement pending confirmation.

## Concrete versus speculative future directions

### Concrete

- matched high-field/reference pilot lamellae; artifact floor and low-energy
  final polish; depth-resolved TEM/STEM through ~1 µm (continuing the Uppsala
  line); finer radial EBSD for quantitative `E_S(r)`; additional cathode
  replication; RFX field-gradient EBSD with phase mapping and matched
  references.

### Speculative (one sentence, close or backup)

- pulse-spectrum coupling to dislocation resonances; a cross-material/loading
  "phase diagram" of conditioning response; extension to RF, cryogenic, BCC,
  and HCP systems.

## Optional/removable slides if the talk runs long

1. Optional grain-skeleton / Σ3 slide (first to cut).
2. Merge Slides 6–7 (EBSD method + how-to-read-LAM) into one.
3. Fold Slide 12 caveats into Slides 9, 10, and 11.
4. Backup only: RFX status table, SEM survey, early EBSD pattern quality,
   depth-artifact controls, exact Table I values, pairwise-test matrix.

## Open scientific questions for review

1. Is the MDDF "central prediction" framing (Slide 3 → Slide 11) the spine you
   want, with `E_S` only as a one-line correlate at Slide 11/15?
2. **Denuded-zone depth:** resolved — `stem_denuded_zone.png` carries both
   100 nm and 200 nm scale bars (different magnifications of the same layer), so
   2026 can say "top ~100–200 nm." Confirm you are happy with that phrasing.
3. How explicit should the 2025 callback be — a light spoken "last year/this
   year" bridge, or a dedicated recap slide at the Part I → Part II boundary?
4. Figure reuse: six 2025 figures are already copied into `figures/` (see
   `knowledge/mevarc25_assets.md`). Confirm they may be used; say if you want
   the FIB "red herring" or post-BD SEM panels pulled in too.
5. Do you endorse the hard/soft copper depth-reconciliation model (Groma
   `ℓ_D`) for a main-path sentence on Slide 11, or keep it in backup?
6. Should the optional grain-skeleton slide stay in the 30-minute cut?
7. Has newer data changed the one-cathode limitation or RFX status?
   **Answered 2026-07-20** (`knowledge/status_refresh_2026-07-20.md`): no new
   copper data (one-cathode caveat stands); RFX last record 13 Jul — #1-25
   EBSD good, #4-25 poor, #2-25/#3-25 scheduled 14 Jul with no record since;
   cond26 submitted to PRAB 2026-06-23, no reviewer changes.
8. Is there a quantitative EBSD information-depth estimate to replace the
   qualitative "deeper than the TEM surface zone" language?

## Open presentation-design questions for review

1. Audience mix: breakdown specialists, materials scientists, or both?
2. Confirm `E_S` stays out of Part I entirely and appears only at Slide 11/15.
3. May approved preliminary RFX SEM/EBSD appear even in backup, or is RFX
   strictly a clean future-direction preview?
4. Confirm the author/affiliation block. From the 2025 title slide: Ashkenazy
   (HUJI/Racah); Profatilova, Jacewicz (Uppsala); Popov (HUJI); Bjelland,
   Wuensch, Millar, Calatroni (CERN). Add RFX collaborators for the SS section.
5. Style: keep the current `main.tex` palette/title, or align more closely with
   the recommendations in `knowledge/style_inventory.md`?

## Approval gate

Before editing `main.tex`, please approve or revise:

- the model→microscopy→large-area→future spine, with `E_S` delayed;
- the strengthened MDDF (Slide 3) and Uppsala-TEM (Slide 4) prior-work links;
- the ~16–18-slide Part I / Part II / Part III structure;
- the two-slide RFX treatment (rest to backup);
- whether the optional grain-skeleton slide stays;
- copying the four missing figures listed above.
