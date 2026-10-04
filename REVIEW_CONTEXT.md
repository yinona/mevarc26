# Review context — MeVArc 2026 talk "Does conditioning leave a structural memory?"

Written 2026-09-30 for an external reviewing agent. Purpose: give the full
scientific and editorial context of the deck, every quantitative claim with its
derivation or source, and pointers to deeper material, so the reviewer can
check the slides and the reasoning without re-deriving the project history.

Conventions. `main.tex:L430` = line in the deck source. `cond26:L372` = line in
the manuscript source `../cond26/main.tex` (state of 2026-09-28). `K/` =
`knowledge/`. Paths starting with `../` are siblings of this repo on the same
drive (`.../clic/cond26`, `.../clic/rfx`, `.../clic/reports/2026_interim`).
Claim-strength labels: **Established** (in the manuscript, referee-reviewed),
**Interpretation** (manuscript discussion), **Analogy** (talk-only framing),
**Preliminary** (RFX, no claim allowed).

---

## 0. The talk in one paragraph

Conditioning (the slow rise of the field a vacuum gap holds under repeated
high-field pulses) is universal in high-gradient devices but its material
basis is unknown. Our MDDF model (mobile-dislocation density and flux,
2018–2020) predicts that conditioning evolves the near-surface dislocation
structure. 2025 cross-sectional STEM of a conditioned hard-copper cathode saw a
dislocation-denuded top ~200 nm, locally. The new result (manuscript under
revision at PRAB, arXiv:2606.19192) is a large-area EBSD comparison across one
CERN pulsed-DC cathode of heat-treated OFE copper: low-angle misorientation is
~75 % higher in the high-field centre and edge than in an unexposed reference,
the field-exposed periphery is intermediate, and the misorientation distribution
grows an eightfold tail. The ordering matches the simulated profile of the
conditioning-state variable E_S, so the dislocation population is a *candidate*
structural basis for it. The talk closes with two next steps: depth-resolved
microscopy and a stainless-steel test at RFX (ongoing, no result claimed).

Slot: Monday 5 Oct 2026, 12:00–12:30, Conditioning session (K/mevarc26_programme.md).

---

## 1. Files the reviewer should open

| Need | File | Notes |
|---|---|---|
| Slide text and speaker notes | `main.tex` (single file) | frames listed in §2; `\note{}` = spoken register |
| Rendered slides | `main.pdf` (23 pp, 16:9); `main-notes.pdf` | render PNGs with PyMuPDF, see HANDOFF §4 |
| Manuscript (authoritative source) | `../cond26/main.tex`, `../cond26/refs.bib` | anchors: abstract L35, intro L49, methods L84, results L194, discussion L364, conclusions L437 |
| July manuscript snapshot | `sources/main.pdf` | what the deck was first built from |
| July→Sep manuscript diff, per deck frame | `K/cond26_changes_2026-09.md` | 19-row table |
| Numbers, equations, figures index | `K/equations_figures_numbers_citations.md` | presentation-ready evidence index |
| Results and conclusions summary | `K/results_conclusions.md` | |
| Methods and assumptions | `K/questions_methods_assumptions.md` | |
| Limitations | `K/limitations_future.md` | |
| Background and motivation | `K/motivation_background.md` | |
| RFX status | `K/rfx_status_2026-09.md` (+28 Sep addendum); `../rfx/HANDOFF.md`, `STATUS.md`, `NEEDED.md` (rewritten 29 Sep) | see §6 |
| Cited PDFs | `sources/*.pdf` | list in `K/source_inventory.md` |
| Prior decks (lineage) | `sources/mevarc2013_*.pdf`, `mevarc24_*.pdf`, `mevarc25_*.pdf` | |
| Decisions, history, next steps | `HANDOFF.md`, `QUESTIONS.md` | decisions in HANDOFF §5 are frozen |
| Writing rules the deck follows | `.cursor/rules/*.mdc` | US spelling, no AI-tell words, sentence-case titles |

---

## 2. Slide-by-slide map with claims and sources

Frame numbers = PDF page numbers (25 pages = 21 core + 4 backup since 3 Oct 2026, when the infographic backup was dropped; 26 pages after the design pass of 2 Oct 2026; HANDOFF 'Design pass, 2 Oct' and 'Author decisions, 3 Oct 2026 (morning)'). Line = `main.tex` frame start; rows 1 and 18–25 updated 3 Oct, other line numbers are from 2 Oct and may be off by a few lines.

| # | L | Title | Claim(s) on the slide | Strength | Source pointers |
|---|---|---|---|---|---|
| 1 | 149 | Title | registered title/subtitle; authors Ashkenazy, Popov, Millar, Bjelland, Wuensch; muted line 'Montreux, Switzerland · Monday 5 October 2026' (3 Oct) | — | Indico contribution 56 (QUESTIONS 16); venue from the Indico event 1637675 export |
| 2 | 182 | Conditioning works. What does it change? | BD rate ∝ ~E^30; conditioning follows pulse count, not breakdown count; field drives it | Established (literature) | Wuensch et al. RMP 98, 025004 (2026); Degiovanni PRAB 2016; cond26:L60–67 |
| 3 | 207 | Our model: breakdown as collective dislocation dynamics | field holding FCC→BCC→HCP order; runaway of mobile-dislocation population nucleates BD; one model gives E^30, T-dependence, dark-current spikes; claim box unchanged (central prediction) | Established (our papers) | Engelberg PRL 120, 124801 (2018); PRAB 22, 083501 (2019); PRAB 23, 123501 (2020); §3.1. Title per design C2; icon captions B15 |
| 4 | 230 | What the model says the microscope should see (NEW, design C1) | four-box chain model → implication → trace → test; a ~10⁹-pulse memory must sit in stored, EBSD-visible dislocations; look far from craters, order follows local field; predicts where/order, not size/depth/sign; brace: no equation for conditioning yet | Inference from the model (stated as such) | proj26/talk_mevarc26/design/C_motivation/PROPOSALS.md (C1, traceability table); OWN-PRL18/PRAB19 cards; cond26:L66, L78, L383 |
| 5 | 317 | STEM already saw it | fewer dislocation walls at 300 K and 30 K, denuded top ~200 nm clearest in the 30 K cathode; soft Cu conditions slower than hard; FIB artefacts | Established | Jacewicz et al. JAP 137, 193302 (2025); Korsbäck PRAB 23, 033102 (2020); cond26:L64–65; §3.7b |
| 6 | 339 | A sub-yield stress, repeated a billion times | σ_M = ε0E²/2 = 0.028 MPa at 80 MV/m, ~10³ below yield; VHCF; pulsed DC → Maxwell stress only cyclic load; MDDF needs only the stress that moves mobile dislocations in a frustrated crystal, far below yield | Established + Interpretation | §3.2; Mughrabi MMTB 40, 431 (2009); Stanzl-Tschegg; cond26:L69–70, L396–400 |
| 7 | 373 | Last year we asked… | visual recap, no numbers | — | 2025 deck |
| 8 | 403 | One cathode… coordinate | one figure: cross-section + E(r) + tiers + ROI markers (figures/geometry_efield_tiers.pdf); heat-treated OFE Cu, 1 µs at 1 kHz, ~10⁹ pulses, ~80 MV/m peak, nine EBSD regions; tier colour key | Established | cond26 §Methods L84–191 (geometry L94–101); E(r) digitized from cond26/figures/efield_vs_radius.eps (figures/efield_r_En_digitized.csv); ROI radii results.json; §3.3; design A P3/B6, B1 |
| 9 | 424 | EBSD maps plastic activity far from craters | SEM callouts (ROI box 500 µm, craters, 0.47 mm gap, 1 mm bar); 500 µm maps, 3 µm step (lateral only), information depth ~40 nm, ~24 000 points/ROI; LAM = local average misorientation (KAM, LOS cross-checks); misorientation ∝ GND | Established | cond26:L179–193, L383–384; Drouin 2007; Chen 2011; SEM pixel calibration design B7 |
| 10 | 449 | What one EBSD pixel measures (NEW, design A P2) | 15 kV beam, top ~40 nm forms the pattern, 3 µm lateral step; Kikuchi pattern → one orientation per point, ~24 000 points, unfiltered; six-neighbour kernel, LAM = ⟨θᵢ⟩, pairs > 5° dropped; 0–5° scale with reference mean 0.68° and high-field mean ~1.2°; bent lattice needs GND, so LAM is a GND proxy | Established (methods) + textbook EBSD | cond26:L179–193, L277–281; results.json; §3.4, §3.8; no tilt angle, no ρ_GND formula (author decision) |
| 11 | 535 | How to read a LAM map | 0–50° vs 0–5° scale | — | cond26 fig LAM_boundary_vs_intragranular L235–243 |
| 12 | 552 | High-field Cu contains more intragrain curvature | pair cropped to the same 485 × 279 µm field at matched magnification, one labelled 0–5° colour bar (figures/lam_pair_matched.png) | Established | cond26 fig LAM_FE_ref_pair L265–273; design B4 (QUESTIONS 9 closed by the crop) |
| 13 | 562 | Three exposure tiers | redrawn plot (figures/tiers_plot.pdf): centre 1.19/1.24°, edge 1.21/1.18°, periphery 0.78/0.79°, reference 0.68/0.65/0.71°, ~75 % bracket, reference band ±1 s.e.; grain size does not follow | Established | results.json; cond26:L320, L333, Table I; §3.4; design B2 |
| 14 | 581 | High-misorientation tail | redrawn plot (figures/tail_plot.pdf): P(LAM>2°) ~0.14 vs ~0.016 (~8×); gamma k≈2.7 fixed, θ 0.24°→0.45°; shaded tail | Established | results.json (k 2.59–2.92, θ 0.22–0.46°); cond26:L284–330; §3.5; design B3 |
| 15 | 603 | Large-area test supports the prediction | 'one mechanism, two starting populations' cartoon labelled as the manuscript's interpretation; to our knowledge first large-area observation, ordered as MDDF predicts; E_S line (candidate) | Established + Interpretation | cond26:L376–389, L443–445; §3.6; design A P4, C4 |
| 16 | 701 | Elastic screening: a sheath of dislocations at the surface | dielectric analogy; ℓ_D ≈ 25 nm; 200 nm ≈ 8 ℓ_D; thickness not predicted | Analogy on top of Interpretation | cond26:L374–381; Groma 2006; Lemaître 2021; Livne 2023; §3.7 |
| 17 | 725 | Copper establishes the effect, not universality | one cathode/one experiment; open: depth, orientation, more cathodes, materials (cooperation call moved to slide 21) | Established (limitations) | K/limitations_future.md; cond26:L446–451 |
| 18 | 771 | Next: go deeper, and change the material | one TikZ diagram: probed depth (~40 nm EBSD, ~200 nm STEM, ~1 µm lamellae) against material (copper pulsed DC → AISI 304L continuous DC); this work, 2025 STEM, 'go deeper', 'change the material', 'first run 2026'; bullets: matched FIB lamellae, TEM, STEM and EBSD through ~1 µm, artifact controls, one depth profile, steel with Consorzio RFX | Plan | interim work plan (2026); main.tex L440 (EBSD depth), L322 (~200 nm) |
| 19 | 835 | Steel: different material, different structural evolution | what differs (lower SFE and planar slip, different mobility; steady ~16 kPa traction, not ~10⁹ pulses; metastable austenite as a built-in strain gauge, ε and α′ above a few 0.1 % plastic strain); first run with Consorzio RFX as facts (90 h and 73 h at 59–61 MV/m, zero breakdowns; 26 EBSD maps, exposed apex inside or below the unexposed range; nothing mapped before exposure, so no field effect can be established); next campaign before and after on one electrode with ε and α′ in the phase list; credit and hand-over to N. Pilan | Outlook — no field effect claimed | ../rfx/HANDOFF.md L20–23, L179, L291; FINDINGS L82–84; QA_PREP L92, L101, L112, L131, L141; Bayerlein et al. MSEA 114, L11 (1989) |
| 20 | 866 | Conditioning appears to leave a subsurface memory | recap; four-bar result card 1.21/1.19/0.79/0.68° with ~75 % bracket (figures/result_card.pdf) at its drawn size, 7.0 cm wide, labels ≥ 8 pt (3 Oct) | — | results.json; design B8 |
| 21 | 891 | Conclusions, and an invitation | three one-line conclusions (third ends '— a stainless-steel test with Consorzio RFX is under way'); invitation box ('same-area before-and-after mapping'); right column: small result chart (figures/result_card_small.pdf), 2 cm QR and arXiv link | — | arXiv:2606.19192; interim work plan (2026); RFX project record |
| 22–25 | 924– | Backup | RFX first look; RFX status table (29 Sep); RFX apex vs unexposed range (null at low power); 2025 STEM pair. The manuscript-infographic backup was dropped 3 Oct (commented out in main.tex, restorable) | Preliminary / Established | §6 |

---

## 3. Every number on the slides, with its derivation

Slide numbers in the §3 headings are the pre-design-pass numbers (23-page deck). After 2 Oct: 3→3, 4→5, 5→6, 7→8, 8→9, 11→13, 12→14, 13→15, 14→16, 17→19, 18→20, backup 22→25.

### 3.1 MDDF model (slide 3) — what "one model" means

Birth–death dynamics of the mobile-dislocation density n on an active slip
plane; breakdown nucleates when n runs away above a critical density. The
2020 PRAB form of the rates (Engelberg et al., PRAB 23, 123501, Eq. 1):

$$\lambda_n=\frac{25\,\kappa C_t c}{G^2 b\,\Delta\rho}\,\sigma^2\,
e^{-\frac{E_a-\Omega\sigma}{k_BT}},\qquad
\mu_n=\frac{50\,\xi C_t c}{G}\,\sigma n,$$

with σ = ε0(βE)²/2 + Z G b Δρ n the stress on the slip plane, β the local
field-enhancement factor, T temperature. The ~E^30 dependence of the breakdown
rate comes from the exponential in σ ∝ E² near the critical point; the
temperature dependence from k_BT; dark-current spikes from fluctuations of n
before runaway. Deeper: `sources/Engelberg_2020_PRAB_DarkCurrentSpikes.pdf`
(pp. 1–2), `sources/Field_Dependent_Conditioning_Correct_Publisher.pdf`
(the 2019 PRAB), `K/motivation_background.md`. The deck shows only two figures
from these papers (`figures/mddf_critical_transition.png`,
`figures/mddf_rate_vs_field.png`); no equation appears on the slide.

**What may be said:** the model *predicts* an evolving near-surface dislocation
structure (cond26:L61). **What may not:** that E_S has been measured or that
the model is confirmed in detail.

### 3.2 Maxwell stress and the cycle count (slide 5)

$$\sigma_M=\tfrac{1}{2}\varepsilon_0E^2
=\tfrac12\,(8.854\times10^{-12}\,\mathrm{F/m})\,(8\times10^{7}\,\mathrm{V/m})^2
=2.83\times10^{4}\,\mathrm{Pa}=0.028\,\mathrm{MPa}.$$

Yield of annealed Cu 30–70 MPa (cond26:L70) → ratio ~10⁻³. Cycle count: 1 µs
pulses at 1 kHz; "~10⁹ pulses" is the conditioning history of this cathode
(cond26 methods; 10⁹ pulses at 1 kHz ≈ 280 h of running). Fields on the
cathode: ~80 MV/m at the flat centre, 69–77 MV/m in the edge region, ≲2.5 MV/m
(fringe ~2.9 %) beyond the anode radius (cond26:L101–191, fig
`efield_on_cathode` L176). Breakdown densities 24 / 12 / 5 cm⁻² for
centre / edge / periphery (cond26 methods).

The "field screened, load not" statement (cond26:L374–375): the electric field
ends in the surface charge layer, but the Maxwell traction is a mechanical
boundary condition carried into the metal as elastic stress, quasi-statically on
the pulse timescale, so the electrostatic screening length says nothing about
the depth of the response.

### 3.3 Geometry and controls (slide 7)

Sloped anode: inner radius r_i = 6.5 mm, outer r_o = 20 mm, gap heights 60/70 µm
(cond26:L87–140). Nine ROIs: field-exposed centre (2), edge (2), periphery (2),
plus external reference cathode ROIs (identically prepared, never installed).
Grain size 26–30 µm in all regions (cond26 results) — grain size does *not*
follow the misorientation hierarchy (slide 11).

### 3.4 The ~75 % result (slide 11)

Mean low-angle LAM: centre and edge 1.18–1.24°; periphery 0.78–0.79°;
reference 0.65–0.71° (~0.68°) (cond26:L333, Table I L306).
Ratio 1.2 / 0.68 = 1.76 → "approximately 75 %" (cond26:L79, L333, L372).
Errors are grain-corrected standard errors of the mean (fig 9 caption,
cond26:L340). The periphery saw ≲2.5 MV/m: it is a *low-field* control, not a
zero-field one; its intermediate value is "consistent with" residual exposure
(note on slide 11). Manuscript figures label the periphery "~0 MV/m"
(QUESTIONS 9).

### 3.5 Distribution tail and shape (slide 12)

Fraction of LAM above 2°: ~0.016 (reference) → ~0.14 (field-exposed); ratio
8.75, quoted as "eightfold" in the manuscript (cond26:L320) and "~8×" on the
slide (QUESTIONS 12). Gamma fits: shape k ≈ 2.6–2.9 common to all ROIs; scale
θ ≈ 0.22° → 0.46° (cond26:L298, L321–328). Kolmogorov–Smirnov distance
D_KS > 0.25 for every centre/edge ROI vs unexposed (> 0.31 vs the external
reference); chi-squared and Anderson–Darling agree (deck note, slide 12).
Mid-angle (Mackenzie-normalised) excess 2–3×; Σ3 fraction 7–11 % (cond26:L349–350;
not on slides). Interpretation "fixed-shape stretch = progressive deformation"
is discussion-level (cond26 §Discussion L367+).

### 3.6 The payoff and the E_S connection (slide 13)

Established: the spatial ordering centre ≈ edge > periphery > reference.
Interpretation: this is the large-area signature the MDDF model predicted
(cond26:L61, L376–388). E_S: Monte-Carlo simulations of the conditioning-state
variable give a spatial profile in the same order (cond26:L443–445, citing the
CERN simulation work); the manuscript says the dislocation population "may be
the physical mechanism tracked by E_S" (L445) and, as an outlook, "a description
that would give E_S a microstructural definition" (L450). The deck uses
"candidate structural basis" once (slide 13) — a frozen decision (HANDOFF §5).

"One mechanism, two starting populations" (cond26:L376–382): in dense
as-machined Cu the cyclic stress lets near-surface dislocations escape to the
surface or annihilate (TEM depletion); in heat-treated Cu there is little to
deplete, so the same load generates and rearranges dislocations (EBSD
curvature). The phrase "two starting populations" is deck wording; the manuscript
argues the same point in prose (L376–382, L389). This is Interpretation, stated
as such on the slide.

### 3.7 Elastic screening (slide 14) — the one talk-only construction

Source facts (cond26:L377–381): Groma, Györgyi, Kocsis (PRL 96, 165503, 2006)
show that in a 2D single-slip dislocation ensemble the long-range internal
stress of a density perturbation is screened Debye-like with wavenumber
k_0 ≈ 4.2√ρ. Hence

$$\ell_D=\frac{1}{k_0}=\frac{1}{4.2\sqrt{\rho}}
=\frac{1}{4.2\times10^{7}\,\mathrm{m^{-1}}}\approx 24\ \mathrm{nm}\approx 25\ \mathrm{nm}
\quad(\rho\sim10^{14}\ \mathrm{m^{-2}},\ \text{as-machined Cu}),$$

so the ~200 nm denuded layer is ~8 ℓ_D. Lemaître et al. (PRE 104, 024904, 2021)
and Livne, Schiller, Moshe (PRE 107, 055004, 2023) give the general "geometric
theory of mechanical screening" in which dislocations are the screening charges
of the *dipole* regime — the formal basis of the dielectric analogy. Neither
theory treats a cyclically loaded crystal with a free surface, so **the 200 nm
thickness is observed, not predicted** (cond26:L380; stated on the slide).

The analogy as drawn: applied field E₀ ↔ Maxwell traction σ_M; bound charge
(polarisation) ↔ dislocation rearrangement (dipole regime); Debye length ↔ ℓ_D;
screened interior field ↔ screened internal stress of the depleted layer. The
claim box was deliberately limited on 28 Sep to "Dislocations screen the
*internal* stress of a depleted layer, over ~25 nm" — the applied traction is
*not* said to be screened (that would exceed Groma). The July deck had said
ℓ_D ~ 100 nm "matching" the layer; the September manuscript corrected this
(K/cond26_changes_2026-09.md row (b)). Points a reviewer may want to probe:
the mixing of a dielectric (uniform E₀/ε_r, no length scale) with a Debye
length (plasma/electrolyte picture) — the manuscript itself uses both words
("Debye-like", "dipole regime"); and whether "dislocations respond like bound
charge" is a fair one-line summary of the dipole regime of Livne et al.

### 3.7b STEM provenance (slides 4 and 22) — checked against the published paper, 2 Oct

The STEM images on both slides are HUJI lamellae (I. Popov) of cathode 007
conditioned at 300 K, shown at MeVArc 2025; they are not reproductions of the
JAP figures. What the published paper (`sources/Jacewicz_2025_JAP_137_193302.pdf`)
states, verbatim: Sec. III E, "Conditioning in both cases significantly reduces
the number of dislocation walls (Fig. 9). This effect is more pronounced in
the cold-conditioned sample Cu038@30K", and "a dislocation-denuded zone close
to the surface is clearly visible (Fig. 10)" — Fig. 10 is the 30 K cathode.
**The paper gives no thickness anywhere**; the only "100 nm" is etch removal
on the 300 K reference (Fig. 8 caption). "~200 nm" is read from the images and
is the number the manuscript uses (cond26 L64, citing Jacewicz and the RMP
review). Discussion: "This initial observation … needs to be repeated more
systematically." Not in the paper at all: the FIB-artefact lesson, "protective
coating" band, the 25 M vs 600 M pulse counts (those are Korsbäck 2020 and our
own 2025 talk). Deck wording was aligned on 2 Oct: slide 4 caption
"dislocation-poor zone in the top ~200 nm", bullet "fewer dislocation walls at
300 K and 30 K; denuded layer clearest at 30 K", backup 22 tags "fewer walls" /
"walls to surface" at 300 K; notes state the paper's conservative wording.

### 3.8 Information depth (slide 8)

Backscattered-electron pattern formation depth in Cu at 15 kV: a few tens of
nanometres (Chen, Kuo, Wu, Ultramicroscopy 111, 1488, 2011). The manuscript
says only "thin surface layer" (cond26:L383) and carries an open author query
to I. Popov on whether to quote a number (L384, commented out); the deck quotes
the number on the authority of Chen 2011 and Popov's 27 Sep confirmation
(`K/cond26_changes_2026-09.md`). A reviewer should treat "few tens of nm" as
literature-supported but not yet in the referee-reviewed text. The 3 µm step
and kernel set only the lateral resolution. Consequence: the EBSD signal comes from within the depth range
where the hard-Cu TEM saw depletion — the two experiments are on different
starting materials, not different depths (slide 13 note, slide 15 note).

---

## 4. Design decisions the reviewer should not re-open (HANDOFF §5)

30 min excluding questions; review-weighted balance (5 background frames);
E_S delayed to one line on slide 13 (plus the infographic on 18); "candidate
structural basis" wording; ~200 nm denuded zone; two RFX main-path slides,
RFX framed as ongoing with no field claim; reuse of 2025 figures; template
(trilingual HUJI logo, emblem, footer); slide 14 states the manuscript's
screening claim and does not name E_S; title/subtitle per Indico registration.

## 5. Open questions the reviewer *may* weigh in on (`QUESTIONS.md`)

7 claim verb ("confirms" on 13 vs "appears to" on 18); 8 E_S on the conclusion
slide; 9 manuscript-figure legends ("~0 MV/m" periphery; mismatched scale bars
on slide 10); 10 infographic legibility on 18; 11 Calatroni on the author line;
12 "~8×" vs 8.75; 13 "first" priority claims (manuscript says "to our
knowledge"); 15 rhetorical patterns ("X, not Y" > 10 times; last-year/this-year
callback 7 times). Timing fallback (cut order) in HANDOFF §3.

---

## 6. RFX stainless-steel programme — what may and may not be said

Facts as of the 15 Sep record (`K/rfx_status_2026-09.md`; `../rfx/STATUS.md`):
AISI 304L electrodes at RFX HVPTF (Padova; De Lorenzi, Pilan, Spada).
#3-25: 90 h 07 m continuous DC, peak 61 MV/m at 58 kV, 7 current bursts (all
before switch-on), no full breakdowns. #4-25: 72 h 41 m, peak 59 MV/m at 56 kV,
4 bursts, no full breakdowns. #1-25, #2-25: never installed (unexposed controls).
EBSD: #1-25 97 % indexed, #3-25 99.5 % (CI 0.13, IQ ~2800), #2-25 three apex
maps (18 Aug) + side; #4-25 poor patterns, not repolished (decision 13 Aug).
XRD: δ-ferrite 1.3/2.3 wt % in #1/#2 vs < 0.2 in #3/#4 (Δa = +0.004 Å),
replicated on interior cut faces → the control and exposed pairs are not
matched material; the clean comparison is apex vs side within one electrode.
The July apex-vs-side LAM contrast on #3-25 reproduced on never-installed
#2-25 (forming geography), and later tests put the #3 apex inside the
unexposed range. **Therefore: no stainless-steel field effect is claimed
anywhere in the deck.** The deck carries one status line on slide 17 and two
backup slides (19, 20).

New since 28 Sep (`../rfx/` rewritten 29 Sep; full digest in
`K/rfx_status_2026-09.md`, addendum 30 Sep). All 26 catalogue maps (36 OIM
scans) are in hand, including the seven wide apex maps. Two analyses
(`../rfx/analysis/ebsd_histogram_ensemble_2026-09-28/FINDINGS.md`,
`../rfx/analysis/ebsd_orientations_all_2026-09-29/FINDINGS.md`) put the #3-25
apex *inside* the same-class unexposed range on every quantity tested,
including at matched confidence index; where it differs it is cleaner, not
rougher. Wide-vs-narrow map class is grain size and indexing quality, present
on every apex including never-installed #2. The 29 Sep decision
(`../rfx/HANDOFF.md:23–33`, `STATUS.md:786–790`): "no indication of field
exposure is establishable from the data in hand" (dose ~10⁻⁴ of yield; emitter
sampling ~10⁻⁴ per map). Prominent *untested* hypothesis H_saturated
(`STATUS.md:547–559`): as-manufactured 304L is already at its conditioned
dislocation state and the runs, which stopped at emission switch-on with zero
breakdowns, never engaged conditioning. #4-25: two 8 Jul scans exist; Area 2
is an outlier on confidence index (88 % of points CI < 0.1), location on the
electrode unrecorded, cause open.

**Deck state (30 Sep, edits applied):** slide 17 status line reads "all 26
EBSD maps in hand; the exposed apex sits inside the unexposed range on every
quantity tested, so no field indication yet"; its note names the zero-breakdown
baseline and H_saturated as a hypothesis. Backups 19–20 reflect the 29 Sep
record; backup 21 (new) shows the apex-vs-unexposed board figure with the
power line (≈17 maps per group at 1 SD). What may be said: "no field indication from the EBSD in hand"; "the runs
stopped at switch-on with zero breakdowns, so this is not yet a conditioning
test". What may not: any field effect; that the null proves H_saturated; that
#4-25's poor patterns are a preparation problem; any #1/#2 vs #3/#4 contrast
as a field contrast.

Corridor asks recorded in `../rfx/NEEDED.md`: thermal history of #3/#4 (vacuum
firing above ~800 °C?); matrix Cr/Ni EDS on all four under identical
conditions; scan folders of the seven wide-grain apex maps; one more #1 side
map at h = 2–3 mm.

---

## 7. Checks the reviewer is invited to run

1. Arithmetic in §3.2, §3.4, §3.5, §3.7 (all reproduce to the quoted rounding).
2. Every slide number against `cond26` at the cited lines; flag any slide number
   that is not in the manuscript (there should be none except the RFX status).
3. Claim strength: any sentence on slides 13, 14, 17, 18 stronger than the
   manuscript's discussion (§3.6, §3.7) or than "Preliminary" for RFX.
4. Consistency of symbols and units across slides (siunitx; ℓ_D italic D per
   manuscript; LAM/KAM/LOS/GND defined on slide 8).
5. Whether the elastic-screening analogy (slide 14) would mislead a plasma or
   condensed-matter physicist, and if so which single word to change.
6. Timing: 18 core slides in 30 min; proposed cut order HANDOFF §3.

## 8. Build and render

`make` → `main.pdf`, `main-notes.pdf`. Poppler is not installed; PNGs via
PyMuPDF: `python3 -c "import fitz; d=fitz.open('main.pdf'); [p.get_pixmap(dpi=100).save(f'/tmp/s-{i+1:02d}.png') for i,p in enumerate(d)]"`.
