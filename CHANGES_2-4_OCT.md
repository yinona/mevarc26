# Changes to the MeVArc 2026 deck, 2–4 October 2026

Scope: 106 commits from 2 Oct 12:00 to 4 Oct 23:58 (HEAD 51f1b85). Full per-commit detail with file:line sources is in `HANDOFF.md` (sections dated 2–4 Oct) and `git log`. This file is the summary for an independent reviewer. Numbering: 22 pages = 21 main-path frames + 1 backup (STEM 2025). Three deliverables are built by `make`: `main.pdf` (projected), `main-notes.pdf` (slide + note), `speaker_text.pdf` (speaker script only, from `tools/extract_notes.py`).

## 1. Structure

- Design pass (2 Oct): three frames added — 4 "What the model says the microscope should see" (model → implication → trace → test), 10 "What one EBSD pixel measures", 21 "Conclusions, and an invitation" (QR + arXiv link + invitation box). Deck-wide colour key: high-field tiers copper/orange, periphery purple, unexposed reference teal. Redrawn figures: geometry/E(r) tiers, SEM low-mag callouts, matched LAM pair, tiers plot, tail plot, result card.
- RFX (stainless steel) reduced to one credited main-path frame (19) and, on 4 Oct, all three RFX backups commented out (restorable); the manuscript infographic backup was dropped on 3 Oct. Backup 22 (field-exposed vs reference STEM, 2025) remains.
- Frame 18 rebuilt as a depth-by-material TikZ diagram (no photos); frame 7 left column filled with two MeVArc 2025 STEM images (HAADF lamella overview, cross-section detail; no sample ID or temperature).
- Frame 2 conditioning curve redrawn as a schematic (log pulse axis, saturating, breakdown dips, tagged "schematic"); it had no data source.
- Frame 16 rewritten twice: 3 Oct to three length scales; 4 Oct to the "sheath" picture with a plasma-at-an-absorbing-wall drawing replacing the dielectric one; then de-loaded to drawings, one line per box, one claim (details moved to the speaker text).
- Frame 21 rebalanced for question time (small tier chart, 2 cm QR, text dominant) and given a what / where / what-next list so it no longer repeats frame 20.

## 2. Scientific wording (binding; the reviewer must not undo these)

- Verbs: "supports", "consistent with", "shows", "our picture"; never "confirms", "establishes", "the only". Priority claims carry "to our knowledge".
- Frame 3: "Field holding rises FCC→BCC→HCP — matching the order of barriers"; "The same model, fitted to the ~E³⁰ rate and its temperature dependence, then reproduced the histogram of dark-current spikes" (fit vs prediction explicit; never "one model").
- Frame 5: title "Identified using STEM at specific locations"; "Direct imaging of an altered near-surface dislocation structure"; closing "Seen at specific locations. The large-area view was missing." (never "one spot", "a few").
- Frame 6: title "A sub-yield stress, repeated a billion times"; "Maxwell stress is the dominant cyclic load"; "MDDF needs only the stress that moves mobile dislocations in a frustrated crystal: far below yield" (never "threshold-free"); claim ends "Is it there?" (never "this year we looked" — the group has looked for a decade; the large area is what is new).
- Frame 8: reference labelled "reference: E = 0" (never "never installed" on slides).
- Frame 9 claim: "Target: the cumulative response to the field, measured far from craters."
- Frame 13 claim: "The ordering follows field history; grain size does not track it." (the bullet "Grain size does not follow this hierarchy" is an author decision of 1 Oct, not to be reopened).
- Frame 15: no E_S on any slide (Q&A only); bullet "The measured order follows the simulated local field: center ≈ edge > periphery > reference"; claim "Before, dislocations were plausible. / Now a dislocation-sensitive state tracks field exposure."
- Frame 16: title "Elastic screening: a sheath of dislocations at the surface"; boxes "≲ 0.1 nm field penetration (Thomas–Fermi)", "ℓ_D ~ 25 nm screening of weak internal fluctuations; only this layer talks to the surface", "~mm applied load, not screened (dislocation stress is self-equilibrated)"; claim "In this picture, weak screened internal stresses set the structure; the strong unscreened load drives the mobile dislocations through it." ℓ_D ∝ 1/√ρ is an order-of-magnitude estimate; Groma 2006 is a keyed reference only, never "Groma's screening".
- Frame 17: "Copper shows the effect, not universality" / "What is shown" / "Three metrics agree (LAM, KAM, LOS)".
- Frame 18: "Depth continues our STEM line; material tests the mechanism itself" (the STEM work is HUJI's, published with Uppsala); first bullet asks whether the EBSD layer (~40 nm) and the STEM denuded zone (~200 nm) belong to one depth profile and whether the denuded zone is the sheath (≈ 8 ℓ_D).
- Frame 19: "Steel: different material, different structural evolution"; no two-phase (γ→α′, δ-ferrite) story, no "pass-or-fail", no "Next campaign" line on the slide; bullets: SFE/planar slip; continuous DC ~16 kPa not ~10⁹ pulses; "Metastable austenite is a built-in strain gauge: ε and α′ martensite mark plastic strain above a few 0.1 %"; RFX facts (304L, HVPTF, 90 h and 73 h at 59–61 MV/m, zero breakdowns, stopped at emission switch-on; 26 EBSD maps; apex inside or below the unexposed range; references exist but no same-area before-and-after; 2–4 maps per group cannot yet resolve a field effect); credit Consorzio RFX — De Lorenzi, Pilan, Spada; hand-over "RFX HV program: N. Pilan, next talk (12:30)"; claim "Copper supports the memory; steel asks whether it is universal."
- Frame 21: items "supported on one cathode, not yet replicated" / "Our picture: it lives within a screening length of the surface — the layer EBSD sees, and the layer that sets emission" / "What would settle it: the same area mapped before and after; a depth profile; a second material (steel, with Consorzio RFX)"; invitation box "before-and-after" (no slashes anywhere in prose).
- Copper paper cited on slides as "Ashkenazy et al., arXiv:2606.19192 (2026)" only (no "PRAB, under revision").
- Title slide: author at the same size as coauthors; "I. Popov (HUJI) · W. L. Millar, V. M. Bjelland, W. Wuensch (CERN)"; "Montreux, Switzerland · Monday 5 October 2026".

## 3. Sources and markers

- Keyed source markers (\src{a}, \src{b}, …) tie each listed source to the line or number it supports; "Sources:" lines use the same letters. Rule (4 Oct): markers and Sources entries only for published papers or arXiv preprints; internal records (interim work plan, RFX project record, SEM report, EBSD pass, MeVArc 2025 talk) are not sources; image credits appear as captions ("STEM: HUJI, I. Popov").
- Other speakers' talks (Wuensch, Wang/Zadin, Bjelland, Coman) are never sources; they appear only as optional first-name asides in the speaker text (Walter, Victoria, Mircea at 11:30 just before us, Jianyu with Guodong Meng, Veronika, Nicola).

## 4. Speaker text (4 Oct night)

All notes rewritten as the sentences to be said: 21 frames, 2083 words, ≈ 16 min at 130 wpm, leaving time to narrate figures within the 30-min slot (talk + questions). Each note opens with the slide's point and closes with the transition; bracketed [optional …] / [if asked …] lines are asides (gray in `speaker_text.pdf`). Frame 16 carries the three scales, "a plasma of dipoles … it reduces, it does not nullify", the absorbing-wall sentence, the roles sentence, and the two-time-constants aside (mobile dislocations ↔ electrons, stored network ↔ ions; the 1 µs pulse is above the network's plasma frequency and passes; ~10⁹ repetitions act like a ponderomotive force; the Maxwell stress is the ponderomotive force of the field on the metal).

## 5. Numbers that must agree everywhere

LAM 1.21 / 1.19 / 0.79 / 0.68° (center, edge, periphery, reference), ~75 % higher, P(LAM > 2°) ~8× (0.016 → 0.14), gamma shape k ≈ 2.7 with scale 0.22–0.25 → 0.43–0.46°; σ_M = 0.028 MPa at 80 MV/m (~10³ below yield); ~10⁹ pulses, 1 µs at 1 kHz; EBSD information depth ~40 nm at 15 kV (CASINO/Drouin 2007; Chen 2011 measured 38–72 nm); 3 µm step; denuded zone ~200 nm (Jacewicz 2025, Fig. 10 scale bar); ℓ_D ≈ 1/(4.2√ρ) ≈ 25 nm at ρ ~ 10¹⁴ m⁻² (order of magnitude); breakdown density 24 / 12 / 5 cm⁻²; Thomas–Fermi ≲ 0.1 nm; steel 90 h and 73 h at 59–61 MV/m, 16 kPa at 60 MV/m, 26 maps, 2–4 maps per group (80 % power at 1 SD needs ≈ 17).

## 6. Verification state at 51f1b85

Fresh `make` reproduces the committed PDFs; main.pdf and main-notes.pdf 22 pages, speaker_text.pdf 23; worst overfull 1.61 pt; no undefined references; QR decodes to https://arxiv.org/pdf/2606.19192; all pages inspected at scale 2 by two independent review passes (3 Oct night, 4 Oct). Not checked: projector, timed rehearsal.
