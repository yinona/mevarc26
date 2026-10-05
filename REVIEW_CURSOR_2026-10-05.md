# Review of the MeVArc 2026 deck — 5 Oct 2026, 00:30 (review only; nothing edited)

Deck at `51f1b85`/`ffdb64a`: `main.pdf` 22 pages (21 main + 1 backup), `speaker_text.pdf` 23 pages. Method: `REVIEW_PROMPT_CURSOR.md` as written. Five `grok-4.7-high-fast` reviewers ran in parallel on rendered pages (PyMuPDF, 110 dpi; poppler is absent) — frames 1–7, frames 8–15, frames 16–22, speaker text + timing + Q&A, sources + figures. I merged, de-duplicated, checked the two number disputes against `../cond26/main.tex`, and ranked. Binding wording (`CHANGES_2-4_OCT.md` §2) was respected; no proposal below reverses it.

Bottom line: **no wrong science.** Verbs, hedges, forbidden words, steel guards, references (16 of 16 match `refs.bib`), QR (decodes to the arXiv PDF, 2.0 cm) all pass. What remains is a morning's worth of small fixes: one mislabelled image, two figure labels that do not match the manuscript, four places where the spoken text says something the slide does not, and some source-marker housekeeping. Fifteen edits are listed in §2; the first eight take under an hour and need no figure regeneration except item 5.

---

## 1. Argument and the three messages

Spine as the deck now tells it: conditioning raises the holding field and follows pulse count (f2) → the MDDF model fits the ~E³⁰ rate and then reproduces the dark-current spike histogram, and predicts an evolving near-surface dislocation structure (f3) → what a microscope should see: an order set by local field, far from craters, with size, depth and sign left open (f4) → 2025 STEM saw an altered near-surface structure at specific locations (f5) → a 0.028 MPa load repeated 10⁹ times can move dislocations in a frustrated crystal (f6) → last year's request, this year's cathode (f7) → one cathode with a field gradient and an E = 0 reference (f8) → EBSD far from craters, ~40 nm deep, 3 µm step (f9–10) → LAM maps (f11–12) → three tiers, ~75 % (f13) → the tail stretches, k fixed, scale doubles (f14) → ordering follows field; dense populations deplete, sparse ones build (f15) → the sheath picture: field stops in 0.1 nm, weak internal stresses screened over ~25 nm, the applied load not screened (f16) → one cathode shows the effect, not universality (f17) → depth and material (f18) → steel at RFX, no field effect claimed (f19) → conclusion (f20) → what / where / what-next and invitation (f21).

The chain holds. Its weakest joins are spoken, not drawn: f5→f6 (the note ends on the missing large-area view, then the next slide is the stress argument), f17→f18 (the claim promises "material and loading history", the note and f18 deliver "depth and material"), and f19→f20 (the note hands the floor to Nicola Pilan before the conclusions).

Three messages a listener should keep:
1. On one conditioned copper cathode, a dislocation-sensitive EBSD signal is ~75 % higher where the field was high, intermediate at the periphery, lowest on the unexposed reference; three metrics agree.
2. The order follows the field history, not grain size or position; the distribution stretches rather than shifts.
3. Our picture: the memory lives within a screening length of the surface, the layer EBSD sees and the layer that sets emission. One cathode; replication, depth, and a second material (steel, with RFX) would settle it.

---

## 2. Prioritized issues

Severity: **C** critical (wrong or misleading content on the main path), **M** major (missing link, slide–note inconsistency, number or source mismatch), **m** minor. "Line" = `main.tex`. Ranked by severity, then by cost to fix (cheapest first).

| ID | Frame | Sev | Observed problem | Location | Proposed edit (respects §2) | Verify |
|---|---|---|---|---|---|---|
| 1 | 7 | C | Right panel captioned "Large-area EBSD across one cathode"; the file `sem_lowmag.png` is an SEM overview (ETD SE, 5 kV, 1 mm bar) with one small IPF inset. No SEM credit. | L439–440; note L443 | Caption: "SEM of the cathode; the rectangle is one of the nine EBSD maps. Round pits are craters." Note: "On the right is the cathode, with one EBSD map inset." Add credit "SEM: HUJI, I. Popov" if that is the origin (author to confirm). | p-07 render; data bar reads SE 5.00 kV |
| 2 | 17 | M | Spoken claim contradicts the slide: slide "changes both the material and the loading history"; note "the depth we probe and the material". f18 is depth + material; loading history arrives with steel (f19). | claim L819; note L821 | Claim: "A stronger test changes the depth, the material, and the loading history." Note close: "Depth and material are the next slide; the loading history comes with the steel." | claim, note, f18 title agree |
| 3 | 16 | M | Analogy spoken as result: "a sheath of one screening length sets what it sees, hence emission and breakdown" comes before "In our picture". Also "which EBSD samples" equates the 25 nm sheath with the 40 nm EBSD depth, a question f18 still asks. | note L784 | Start the absorbing-wall sentence with "In our picture,". Delete "which EBSD samples". Keep every §4-required sentence. | s-17: hedge precedes "hence emission" |
| 4 | 19 | M | Note lacks two guards the slide has: "stopped at emission switch-on" and "references exist, no same-area before-and-after"; note ends by handing to Nicola, with no bridge to f20. | slide L909, L911; note L921 | After "zero breakdowns" add "stopped at emission switch-on". After the apex sentence add "References exist, but there is no same-area before-and-after." Replace the close with "Nicola's RFX talk is at 12:30. Next here: what we conclude." | s-20 reaches f20 |
| 5 | 8, 13 | M | Edge field labelled "73–74 MV/m" on both figures and in the f8 note. Manuscript: edge ROIs (r = 9.21, 8.65 mm) "exposed to intermediate fields (~69–77 MV/m)" (cond26 L161, L339). 73–74 appears nowhere in the paper. | `make_design_figures.py` L71, L124, L161; note L467 | Label "edge\n~69–77 MV/m" (manuscript range) on both plots; note "about 69 to 77 at the edge regions". Regenerate `geometry_efield_tiers.pdf`, `tiers_plot.pdf`; `make`. | p-08, p-13 renders |
| 6 | 14 | M | Tail plot prints "0.24° → 0.46°" (the one plotted ROI pair). Manuscript and §5: θ ≈ 0.22–0.25° → 0.43–0.46° (cond26 L325 "0.22° … 0.46°"). | `make_design_figures.py` L153; p-14 | Annotation "scale θ: 0.22–0.25° → 0.43–0.46° (this pair 0.24° → 0.46°)". Bullet L644 "k ≈ 2.7 fixed" → "k ≈ 2.7 (2.6–2.9)" per cond26 L324. Regenerate `tail_plot.pdf`. | p-14 render |
| 7 | 15 | M | Title and bullet 1 ("ordered as MDDF predicts") read as prediction; note then says "Size, depth and sign were not predicted" — but cond26 L65 does predict the sign (dense depletes, sparse builds). | title L652; bullet L701; note L706 | Keep title and claim box (§2). End bullet 1 at "dislocation structure." Note: "The magnitude of the LAM change and the denuded-layer thickness were not predicted." | spoken line no longer denies cond26 L65 |
| 8 | 10 | M | "top ~40 nm" (bullet and summary) keyed only to Chen 2011; f9 correctly splits ~40 nm at 15 kV → Drouin/CASINO, 38–72 nm → Chen. Drouin absent on f10. | L513, L578–579 | `\src{b,c}` on the depth lines; Sources: b Drouin, Scanning 29, 92 (2007); c Chen. | letters on p-10 match line 487's split |
| 9 | 3, 4 | M | f3: fit clause and the central-prediction claim keyed only to d (Wuensch review); a,b (Engelberg) sit only on the model bullet. f4: unlettered "Wuensch et al., RMP…" entry with no marker on the slide. | L244, L253–254; L343 | f3: `\src{a}` on the fit clause, `\src{a,b}` on the claim, `\src{d}` stays on the FCC→BCC→HCP line. f4: delete the Wuensch entry. | every letter has a marker on the line it supports |
| 10 | 21 | M | Copper line "Ashkenazy et al., arXiv:2606.19192" lacks "(2026)", the only such instance; no "Sources:" label. Small-card labels render 7.2–7.7 pt (< 8 pt floor). | L974; `make_result_card_small.py` | "Sources: ᵃAshkenazy et al., \condref." Raise the small-card annotation font to ≥ 8 pt if time allows. | p-21 text dict |
| 11 | 18 | M | "~200 nm, STEM" keyed to Jacewicz 2025 with no figure; the paper states no thickness (REVIEW_CONTEXT §3.7b). f22's note says so; f18's note states 200 nm as the STEM result. | L839, L865, L872–873 | Source b: "Jacewicz et al., JAP 137, 193302 (2025), Fig. 10 scale bar". Note: "about 200 nanometers, read from the Fig. 10 scale bar; the paper states no thickness." | f18 note matches f22 note |
| 12 | 5 | M | Bullet distinguishes 300 K from 30 K, caption gives ~200 nm, but neither STEM panel is labelled with sample or temperature; arrows unexplained. Note says "nearly free of dislocation walls" — stronger than slide's "dislocation-poor" / "fewer walls". | L352–358; note L366 | Note: "the top 200 nanometers or so is dislocation-poor, with fewer walls." Panels: label temperature only if the author knows which lamella each is (CHANGES §1 says the f7 STEM images carry no sample ID or temperature; same for f5?). Add "Arrows mark the zone under the coating." | p-05 render |
| 13 | 22 | M | Note: "this pair is Figure 9" identifies our HUJI 300 K lamellae with the JAP figure; they are not reproductions. | L1076 | "In the paper, the 300 K comparison is Fig. 9; the denuded zone is clearest for the 30 K cathode, Fig. 10. These are our lamellae of the 300 K pair." | REVIEW_CONTEXT §3.7b |
| 14 | 4, 9 | M | Colour key breaches: f4 three tier bars (high / low / none) all teal; f9 crater circles and "breakdown craters" chip in reference teal. Key: copper high field, purple periphery, teal reference. | L316–318; `make_design_figures.py` L86–88 | f4: `\fill[tierhigh]`, `[tierlow]`, `[tierref]`. f9: craters in steel or ink; regenerate `sem_lowmag_callouts.png`. Add SEM credit under f9 figure. | p-04, p-09 renders |
| 15 | 3 | M | Rate figure: three series, no legend; field axis 180–300 MV/m while the talk's load is 80 MV/m; caption does not say these are published model curves. | L250–251; `mddf_rate_vs_field.png` | Caption: "Published MDDF rate curves (Engelberg 2019), not this cathode." Legend only if the source figure's series names are known; do not invent. | p-03 |
| 16 | 5→6, 6→7 | m | Transitions: f5 note ends on the missing large-area view, f6 is the stress argument; f6 "Is it there?" then f7 "Here it is" before any result. | L366, L398, L404 | f5 close: "Before that map: can a stress this small write the structure?" f6 close: "The next slide is the measurement we brought; the distributions come after the geometry." | read s-06..s-08 aloud |
| 17 | 4 | m | Bullet "must sit in stored dislocations" vs the brace on the same slide "inference from the model: no equation for conditioning yet"; note repeats "must". | L332–337; note L344 | "In the model, a ~10⁹-pulse memory sits in stored, EBSD-visible dislocations." Note: add "That step is an inference; there is no equation for conditioning yet." | brace and bullet agree |
| 18 | 2 | m | Hypothesis "Something in the metal stores the improvement" carries `\src{a}`, so it reads as a Wuensch result. | L232 | Remove `\src{a}` from the claim box. | — |
| 19 | 6 | m | Note adds, as fact, "weak internal stresses, not the applied one, decide where mobile segments move" — the f16 picture, spoken ten frames early. | L395 | End the sentence at "far below yield." | — |
| 20 | 16 | m | "self-equilibrated" unglossed; marker d sits on that parenthetical. Aside cites Groma without the formula. | L776; note L784 | Move `\src{d}` to "not screened". Note: "internal stresses sum to zero, so they cannot cancel a surface traction." Aside: "ℓ_D ≈ 1/(4.2√ρ) ≈ 25 nm at ρ ~ 10¹⁴ m⁻²." | — |
| 21 | 13 | m | Periphery 0.79° neither printed nor spoken (bullets give ~1.2° and 0.68°). | L618–619; note L626 | Note: "The periphery sits near 0.79 degrees." | — |
| 22 | 9 | m | ROI, KAM, LOS, GND appear as bare abbreviations at first use. | L481–483 | Expand once on f9. | — |
| 23 | 18 | m | "2025 red herrings" undefined on the slide. | L866; note L873 | "Artifact controls from the 2025 FIB checks." | — |
| 24 | 7 | m | Surface-detail crop has no scale bar; HAADF crop keeps a clipped instrument footer. | L420–430 | One line: "Instrument scale not usable on these crops." Do not draw a bar. | p-07 |
| 25 | 5 | m | Aside: hard Cu ~25 M pulses, soft ~600–900 M — not in §5; from Korsbäck 2020 per earlier notes, fine if the author is sure. | L366 | Keep only if confident; otherwise drop the numbers and keep "much slower". | Korsbäck PRAB 23, 033102 |
| 26 | 21 | m | Note omits "cross-facility comparisons", which is in the invitation box. | L965 vs L976 | Add the phrase. | — |
| 27 | 9 | m | Aside "oxide removal under 10 nm" vs prep record "≤ 10 nm by AFM". | L488 | "at most 10 nanometers by AFM". | QA_PREP Q13 |

Passed without issue: forbidden words (none on slides or in notes); "To our knowledge" present on f15; E_S only in the f15 aside; steel frame carries both guards and claims no field effect; H_saturated absent; no prose slashes; copper cited as `\condref` everywhere but f21; no other speaker's talk as a source; no internal record as a source; all 16 references match `cond26/refs.bib` (two not in the bib: the copper arXiv itself and Bayerlein 1989, both correctly cited); every `\includegraphics` file exists; QR decodes (cv2) to `https://arxiv.org/pdf/2606.19192` at 2.00 × 2.00 cm; frames 20 and 21 do not repeat each other; TikZ on f16 and f18 legible; colour key holds on f8, f12–15, f20–22.

---

## 3. Claim record (main claims)

| Frame | Claim | Category | Qualification |
|---|---|---|---|
| 2 | BD rate ~E³⁰; conditioning tracks pulses more than arcs | observation (literature) | none |
| 2 | Something in the metal stores the improvement | hypothesis | drop `\src{a}` (#18) |
| 3 | Fitted to ~E³⁰, then reproduced the spike histogram | fit, then prediction | split already explicit |
| 3 | Conditioning evolves the near-surface dislocation structure | model prediction | keyed to Wuensch; re-key to Engelberg (#9) |
| 4 | Order follows local field, far from craters | model prediction | size, depth, sign tagged open — fine |
| 5 | Altered near-surface structure seen at specific locations | observation | panels unlabelled (#12) |
| 5 | Fewer walls at 300 K and 30 K; clearest at 30 K | observation (JAP Sec. III E) | none |
| 6 | σ_M = 0.028 MPa, ~10³ below yield | derived | none |
| 6 | Maxwell stress is the dominant cyclic load | interpretation | justified on slide (pulsed DC) |
| 8 | Field gradient gives internal controls on one specimen | design | edge label (#5) |
| 10 | Each 3 µm point: one angle from the top ~40 nm | method | Drouin key (#8) |
| 13 | Ordering follows field history; grain size does not | observation | binding |
| 14 | Distribution stretches; a uniform offset cannot | interpretation of fit | k range (#6) |
| 15 | A dislocation-sensitive state tracks field exposure | interpretation | claim box fine; bullet 1 and note (#7) |
| 15 | Dense populations deplete, sparse ones build | manuscript interpretation (cond26 L65, L376–382) | labelled "our picture" |
| 16 | Field stops in ≲ 0.1 nm | textbook | none |
| 16 | ℓ_D ~ 25 nm screens weak internal fluctuations | order-of-magnitude estimate | formula in aside (#20) |
| 16 | Applied load not screened | manuscript statement (cond26 L374) | gloss "self-equilibrated" (#20) |
| 16 | Sheath sets what the surface sees, hence emission | interpretation | hedge must precede it in the note (#3) |
| 17 | Copper shows the effect, not universality | limitation | none |
| 18 | 40 nm and 200 nm one profile? Denuded zone = sheath? | hypotheses as questions | 200 nm provenance (#11) |
| 19 | Steel: different material, different structural evolution expected | hypothesis | no field effect claimed — correct |
| 19 | Apex inside or below unexposed range; 2–4 maps cannot resolve | observation + limitation | note must carry both guards (#4) |
| 20–21 | Conditioning leaves a structural memory, on one cathode | interpretation | binding wording |

---

## 4. §5 numbers — consistency

| Number | Result | Where |
|---|---|---|
| LAM 1.21 / 1.19 / 0.79 / 0.68° | pass | f20 card, f21 small card, f20 note. Slides 10, 13 use ~1.2° and 0.68° (manuscript rounding); 0.79° never spoken (#21) |
| ~75 % | pass | f13, f15, f20 |
| P(LAM>2°) 0.016 → 0.14, ~8× | pass | f14 box and figure; note "eightfold" |
| k ≈ 2.7 | pass as number; "fixed" too tight (#6) | f14 |
| θ 0.22–0.25° → 0.43–0.46° | **fail on figure** (prints 0.24 → 0.46) | f14 (#6) |
| σ_M 0.028 MPa at 80 MV/m, ~10³ below yield | pass | f6; f15 order-of-magnitude line |
| ~10⁹ pulses, 1 µs at 1 kHz | pass | f2, 4, 6, 8; "1 kHz" spoken only on f8 |
| ~40 nm at 15 kV (Drouin); Chen 38–72 nm | pass on f9; **attribution fail on f10** (#8) | f9, f10, f18 |
| 3 µm step | pass | f9, f10 |
| ~200 nm denuded (Fig. 10 scale bar) | pass as number; provenance missing on f18 (#11) | f5, f15, f18, f22 |
| ℓ_D ≈ 25 nm (order of magnitude) | pass; formula and ρ absent (#20) | f16, f18 |
| 24 / 12 / 5 cm⁻² | pass | f17 slide; f13 note |
| Thomas–Fermi ≲ 0.1 nm | pass | f16 |
| Steel 90 h, 73 h, 59–61 MV/m, 16 kPa, 26 maps, 2–4 per group, ~17 | pass (16 kPa = ε₀E²/2 at 60 MV/m = 15.9 kPa; "at 60 MV/m" not printed) | f19 |
| Edge field | **fail**: "73–74 MV/m" vs manuscript "~69–77" (#5) | f8, f13 |
| Reference "E = 0" | pass | f8 |

---

## 5. Timing

Script 2083 words over 21 frames; **16.0 min at 130 wpm**, asides excluded. Blocks: f1–7 656 words (5.0 min), f8–15 757 (5.8), f16–21 670 (5.2). `CHANGES` §4 targets 22–24 min of talk inside the 30-min slot, so the headroom is figure narration; do not lengthen the notes. Long for their role: f4–6 (111–119 words each, background), f8–10 (methods, 104–115), f16 (139), f19 (130). Short: f11–12 (64–65) — the payoff frames; do not cut them.

Compression candidates if the dry run overruns:
1. f6, L395: cut "a dense, pinned network in which weak internal stresses, not the applied one, decide where mobile segments move." (belongs to f16; also #19).
2. f16, L784: cut "in the plasma on the left, only a sheath one Debye length thick reaches the wall." (the drawing says it).
3. f19, L921: cut "Nicola will tell you about the RFX program next." (the slide already has the hand-over; see #4).
4. f4: compress the brace explanation to one sentence.

Not measured: rehearsal time, projector.

---

## 6. Q&A gaps

| Question a CERN / Uppsala / RFX colleague will ask | Covered? | If gap: answer from repo facts |
|---|---|---|
| Is 0.028 MPa really enough to do anything? | f6 note argues accumulation; no `[if asked]` press-back | "The argument is 10⁹ cycles, not one pulse; VHCF data stop near tens of MPa, so we extrapolate, and MDDF does not predict the size of the LAM change — it predicts the ordering." (L400; QA_PREP 28, 137) |
| FIB or Ga damage inside the 40 nm EBSD depth? | oxide clean ≤ 10 nm in f9 aside; Ga depth is a gap | "Same clean on all nine regions, at most 10 nm by AFM; a field-ordered three-tier pattern is hard to attribute to a step identical everywhere." (QA_PREP 68–70) |
| Are the 40 nm EBSD layer and the 200 nm STEM zone one profile? | f18 asks it aloud; no answer aside | "Different starting materials and geometries: heat-treated Cu in plan view vs hard Cu in cross-section. Not yet one profile; matched lamellae are the next step." (L865; QA_PREP 50) |
| Is the periphery a zero-field control? | yes, f13 note: ≤ 2.5 MV/m internal control; E = 0 is the external reference | — |
| Steel: a null, or no test yet? | slide yes; note missing the guards (#4) | "Runs stopped at emission switch-on with zero breakdowns, so not yet a conditioning test; 2–4 maps per group, 17 needed for 80 % power." (L909, L921) |
| Where does 200 nm come from if the paper gives no number? | f5 aside and f22 note | — (fix f18, #11) |
| Dielectric vs Debye: which analogy? | f16 aside | — |
| E_S? | f15 aside: candidate basis, not a measurement | — |
| Why is S. Calatroni not on the author line? | no aside | author's call; one sentence ready: "the author line follows the EBSD paper" |

---

## 7. Disagreements with prior decisions (for the author; not applied)

- `HANDOFF.md` §5 still says "30 min excluding questions" and "E_S on the payoff slide"; `CHANGES` §2 and §4 say talk plus questions in 30 min and no E_S on slides. The deck follows `CHANGES`. Reconcile the handoff text after the talk; no deck change.
- None of the five reviewers disputed a §2 wording decision.

## 8. What was inspected, and not

Inspected: all 22 rendered slide pages and all 23 speaker-text pages at 110 dpi; `main.tex` in full (commented RFX backups ignored); `CHANGES_2-4_OCT.md`, `HANDOFF.md` §5, `REVIEW_CONTEXT.md` §2–3, `QUESTIONS.md`, `QA_PREP.md`; `cond26/main.tex` L61–81, 94–116, 158–190, 287–342, 364–400; `cond26/refs.bib`; `figures/make_design_figures.py`, `make_result_card_small.py`, `tools/extract_notes.py`; every live figure file (size, caption, credit); QR decoded. Not inspected: projector output, timed rehearsal, the generating data behind `efield_r_En_digitized.csv` beyond interpolation, the identity of the lamellae in `stem_denuded_zone.png`.

Subagent calls: `grok-4.7-high-fast` × 5; integrator (this file) by the Cursor agent.
