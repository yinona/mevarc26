# Handoff — MeVArc 2026 presentation (mevarc26)

Last updated: **2026-09-28, 02:00** (end of a long session; resume 2026-09-29).

**Talk slot (from Indico, verified 2026-09-28): Monday 5 October 2026, 12:00–12:30,
Conditioning session, Montreux.** Registered title: *Does conditioning leave a
structural memory? Large-area evidence for the dislocation picture.* 30 min
excluding questions. W. Wuensch (09:15) and V. Bjelland (10:00) speak before
us, N. Pilan (RFX) right after. Programme notes: `knowledge/mevarc26_programme.md`.

---

## 1. Where we come from

### The science arc this talk sits in

1. **2013 (MeVArc, Ashkenazy):** plasticity-based picture of breakdown
   nucleation; early-warning statistics. Deck in `sources/mevarc2013_ashkenazy_v01.1.pdf`.
2. **2018–2020, the MDDF model** (Engelberg et al., PRL 120, 124801; PRAB 22,
   083501; PRAB 23, 123501): breakdown nucleates when the mobile-dislocation
   population, driven by the Maxwell stress, runs away. Reproduces the ~E^30
   rate, its temperature dependence and dark-current spikes. Its central
   prediction, *conditioning evolves the near-surface dislocation structure*,
   is the sentence the whole talk tests.
3. **2024 (MeVArc microscopy talk):** SEM/FIB/EBSD forensics, FIB artefacts
   ("red herrings"), cryogenic cross-sections. `sources/mevarc24_ashkenazy_v3.pdf`.
4. **2025 (MeVArc, HUJI + Uppsala):** cross-sectional STEM of a conditioned
   *hard* (as-machined) Cu cathode shows a dislocation-denuded top ~200 nm
   (Jacewicz et al., J. Appl. Phys. 137, 193302 (2025)). Local evidence only;
   the talk closed by asking for "more comparative forensics: other materials,
   more samples". `sources/mevarc25_huji_v2.pdf`.
5. **2026, the copper result (`../cond26`):** large-area EBSD on one CERN
   pulsed-DC cathode (heat-treated OFE Cu, ~80 MV/m peak, 1 µs pulses at
   1 kHz, ~10^9 pulses). Low-angle misorientation is ~75 % higher in the
   high-field centre/edge (~1.2°) than in the external reference (~0.68°);
   the field-exposed periphery is intermediate; the LAM tail above 2°
   rises ~8×. Manuscript: Ashkenazy, Popov, Bjelland, Millar, Wuensch —
   submitted to PRAB 23 Jun 2026, arXiv:2606.19192 (verified live
   2026-09-28), **minor revision ZT10260 implemented 27 Sep; resubmission is
   Yinon's action.** Zenodo dataset 10.5281/zenodo.20623348.
6. **2026, the interim report (`../reports/2026_interim`, Jul):** depth-resolved
   work plan — matched FIB lamellae, correlated TEM/STEM + EBSD through the
   top ~1 µm.
7. **2026, RFX collaboration (`../rfx`):** AISI 304L electrodes conditioned at
   RFX HVPTF (Padova; De Lorenzi, Pilan, Spada). #3-25 and #4-25 ran 90 h and
   73 h continuous DC at 59–61 MV/m peak with no full breakdowns; #1-25 and
   #2-25 are unexposed controls. SEM survey (Inna Popov, May), EBSD Jul–Sep.
   **No stainless-steel field effect is claimed:** the July apex-vs-side
   contrast reproduced on the never-installed #2-25 (forming geography), and
   XRD shows the control and exposed pairs differ in δ-ferrite, so the clean
   comparison is apex vs side within one electrode. #4-25 still does not index
   and will not be repolished. This is *ongoing and future work*; the deck
   keeps it to one status line on slide 17 plus two backup slides.

### How this deck was built (repo history)

| Commit | Date | What |
|---|---|---|
| `c7cdb01` | Jul 2026 | Knowledge base (`knowledge/`) extracted from cond26, reports, rfx; `presentation_map.md` approved plan. |
| `ea22740` | 20 Jul | Deck written (22 frames), all July content decisions applied, template redesign (trilingual HUJI logo, emblem, compact footer). |
| `1e8f760` | 15 Sep | Baseline: first HANDOFF/QUESTIONS, abstract draft, mined figures, `sources/` papers. |
| `d29d74a` | 28 Sep | Phase 0: rebuilt a Drive-damaged `.git/index` (no content lost); `.cursor/rules/` style rules. |
| `6ef9729` | 28 Sep | Aligned with the September manuscript (see §2). |
| `505ebbd` | 28 Sep | RFX refreshed to the 15 Sep record; optional slide 15b demoted to backup. |
| `442f588` | 28 Sep | New slide 14: elastic-screening analogy (dielectric vs dislocation screening). |
| `20b45e7` | 28 Sep | Visual pass: overfull frames fixed, pulse-train sketch (slide 5), thumbnails (slide 16). |
| `e6e95ca` | 28 Sep | Two independent style reviews merged and applied; HANDOFF/QUESTIONS rewritten. |
| `7c1ee35` | 28 Sep | Cleanup of unused files; Indico programme cross-references; RFX wording corrected from `../rfx/HANDOFF.md`; handoff rewritten. |
| `0d391ec` | 30 Sep | `REVIEW_CONTEXT.md` for external review of slides and derivations. |
| `53d0f0b` | 30 Sep | 29 Sep RFX record digested (`knowledge/rfx_status_2026-09.md` addendum). |
| `91b0304` | 30 Sep | RFX edits applied: slide 17 status line and note, backups 19–20 updated to 29 Sep, new backup 21 (apex vs unexposed range, null at low power). |
| (this) | 1 Oct | Modifier brief (`MEVARC26_MAIN_PRESENTATION_MODIFIER_BRIEF.md`) audited; nine factual and claim-strength edits applied (see §3 item 7). Slide 17 stays in the main path; target stays 30 min. |

The agent workflow on 28 Sep used subagents (`grok-4.7-high-fast` for reading
and mechanical passes, `claude-opus-5-5-medium` once as second reviewer); the
requested `grok-4.7-medium/high` and `claude-opus-5-5-high` slugs were not
available. Poppler is not installed on this Mac; PyMuPDF (`import fitz`) does
page counts and renders.

---

## 2. Where things stand

### Deck (23 frames = 18 core + 5 backup; `main.pdf` and `main-notes.pdf` compile clean)

| # | Frame | Notes |
|---|---|---|
| 1 | Title | registered title/subtitle; authors incl. S. Calatroni (see Q11) |
| 2 | Conditioning works. What does it change? | cross-ref Wuensch 09:15 |
| 3 | Our model: collective dislocation dynamics (MDDF) | |
| 4 | STEM already saw it, at single spots | now says *hard (as-machined)* Cu |
| 5 | A tiny stress, repeated a billion times | pulse-train sketch; cross-ref Meng/Zadin |
| 6 | Last year we asked for more forensics | recap bridge; first to cut |
| 7 | One cathode turns field exposure into a coordinate | *heat-treated* OFE Cu; cross-ref Bjelland 10:00 |
| 8 | EBSD maps plastic activity far from craters | information depth a few tens of nm (Chen 2011) |
| 9 | How to read a LAM map | |
| 10 | High-field copper contains more intragrain curvature | |
| 11 | Three exposure tiers (~75 %) | |
| 12 | High-misorientation tail (~8×) | KS detail moved to notes |
| 13 | The large-area test supports the model's prediction | payoff; "to our knowledge, the first large-area observation"; the one E_S line; "one mechanism, two starting populations" |
| 14 | **Elastic screening: dislocations respond like bound charge** | new; ℓ_D ≈ 25 nm, 200 nm ≈ 8 ℓ_D, "not predicted"; no E_S |
| 15 | Copper establishes the effect, not universality | cooperation call; cross-ref Coman 11:30 |
| 16 | Next: go deeper, and change the material | thumbnails |
| 17 | Stainless steel: a test chosen to be hard on the model | status line as of 29 Sep: all 26 maps, apex inside unexposed range, "no field indication yet"; note names H_saturated as a hypothesis; cross-ref Pilan 12:30 |
| 18 | Conditioning appears to leave a subsurface memory | conclusion, 2025 bookend, new infographic |
| 19–23 | Backup | RFX first look (ex-15b); RFX status table (29 Sep); RFX apex vs unexposed range (board figure from `../rfx/analysis/ebsd_orientations_all_2026-09-29/`, power line); 2025 STEM pair; infographic full size |

### What changed in the manuscript since July and is now in the deck

Headline numbers unchanged. Changed: screening length ℓ_D = 1/(4.2√ρ) ≈ 25 nm
(so the 200 nm denuded layer is ~8 ℓ_D and its thickness is *not predicted*),
replacing the old "~100 nm matching the layer"; EBSD information depth a few
tens of nm, the 3 µm step being lateral only; depletion happened in hard Cu,
build-up in the heat-treated Cu measured here; the field is screened by surface
charge but the load enters as elastic stress; `infographic.pdf` replaced
(27 Sep); three new references (Lemaître 2021, Livne 2023, Chen 2011);
conclusions add "interacting, self-screening dislocation population".
`\condref` (main.tex line ~117) = "PRAB, under revision; arXiv:2606.19192".
Full diff per frame: `knowledge/cond26_changes_2026-09.md`.

### Style state

Two review passes applied: no slashes, no standalone "this" on slides, US
spelling throughout, siunitx units, "no full breakdowns", 59–61 MV/m, slide-14
claim strength corrected (dislocations screen the *internal* stress of a
depleted layer, not the applied traction). Remaining judgement calls are
`QUESTIONS.md` items 7–15.

### Repo hygiene (2026-09-28)

Removed: duplicate logos and papers in `sources/`, unused logos (Uppsala, long
HUJI) and unused report images in `figures/`, the 9.6 MB `figures/mined/`
renders (re-extractable; recipe in `knowledge/mined_figures_2026-07-20.md`),
generated `presentation_map.pdf`, and the retired July questionnaire
`knowledge/confirmation_needed.md`. Only figures the deck uses or that are
ready assets for the optional Sigma-3 slide remain.

---

## 3. Tomorrow (2026-09-29) and the week — priority list

1. **Dry run with the notes** (`main-notes.pdf`). Target 27–28 min spoken.
   Cut order if long (both reviewers agreed): drop 6 (~60 s) → move 14 to
   backup (~100 s) → merge 9 into 10 (~50 s) → merge 15 into 16 or fold the
   slide-12 box onto 11 (~50–60 s). That is the 25-min fallback.
2. **Resubmit to PRAB** (cond26 `TODO.md` item 5, authors.aps.org). If a
   verdict lands before 5 Oct, change `\condref` to "accepted"/"in press".
3. **Decide QUESTIONS 7–10** (claim verb, E_S on slide 18, periphery
   "~0 MV/m" legend in the manuscript figures, infographic legibility).
   Each is a five-minute edit.
4. **RFX corridor asks** for Pilan/De Lorenzi (from `../rfx/NEEDED.md`, items
   31–36 not yet asked): thermal history of #3/#4 (vacuum firing above
   ~800 °C?); matrix Cr/Ni EDS on all four under identical conditions; full RFX
   run log; a next campaign of annealed vs as-received 304L, each with a sham,
   driven into breakdowns (NEEDED 34). The seven wide apex maps arrived 28 Sep;
   nothing more to ask Inna for the talk. Do not ask for `.up2`.
5. **Final checks on the conference laptop:** title-slide logos, footer,
   fonts; bring `main.pdf` and `main-notes.pdf` (both ~20 MB).
6. **RFX edits of 30 Sep — applied** (source: `knowledge/rfx_status_2026-09.md`,
   addendum 30 Sep; `REVIEW_CONTEXT.md` §6). Slide 17 status line and note now
   state the 29 Sep null ("no field indication yet"), the zero-breakdown
   baseline, and H_saturated as a hypothesis; backups 19–20 carry the 29 Sep
   record; new backup 21 shows the apex-vs-unexposed board figure
   (`figures/rfx_board_apex_vs_unexposed.png`, copied from
   `../rfx/analysis/ebsd_orientations_all_2026-09-29/figures/`) with the power
   line. Known limit: the board figure's panel labels are small at conference
   distance; if the slide is ever shown, regenerate the figure in `../rfx/`
   with larger type. Slide 18 bullet 3 unchanged — the steel test is ahead,
   not failed.
7. **Modifier brief, 1 Oct — disposition.** Applied (factual or manuscript
   alignment): Wuensch → Rev. Mod. Phys. 98, 025004; information depth
   "~40 nm at 15 kV" with Chen 2011 + Drouin 2007 (manuscript L383);
   "confirms" → "supports" (slides 13, 15, 18, notes); "to our knowledge, the
   first large-area observation" (slide 13); slide 10 source notes the
   200/100 µm scale bars; slide 17 null tag "informative only with enough
   maps" (no "bounds"); "pre-conditioning baseline" dropped for the plain
   fact "stopped at emission switch-on, zero breakdowns"; Korsbäck pulse
   counts nuanced in the slide-4 note. Not applied: move slide 17 to backup
   and the 22–24 min target (Yinon 1 Oct: 30 min, keep the overload);
   "credit 16:00 to J. Wang" (wrong — 16:00 is G. Meng); deleting "not
   sample position", "independent" metrics, and softening "the field, not
   the arcs" (each would underclaim the manuscript, L405, L441, L66/L415).
   The brief file was deleted on 1 Oct after this disposition was recorded.
8. **`../proj26/talk_mevarc26/deck_minimal.diff` (another agent, 1 Oct
   21:29) — disposition 2 Oct.** Applied: footer "4--9 Oct" (Indico event
   dates); slide 4 bullets per the published JAP paper ("fewer dislocation
   walls at 300 K and 30 K; denuded layer clearest at 30 K", source
   `../proj26/own_work/papers/jacewicz2025.md` — the local
   `sources/Jacewicz_2024_*.pdf` was the 2022 preprint and lacked the STEM
   section; replaced 2 Oct by the publisher PDF
   `sources/Jacewicz_2025_JAP_137_193302.pdf`), "First direct" → "Direct"; slide 5 source credits J. Wang as the
   16:00 speaker (Indico speaker field; Meng is first author); slide 8
   itemsep; slide 13 "conditioned regions carry a different near-surface
   dislocation structure" (spatial comparison, not before/after); slide 17
   and backup 19 "zero breakdowns (stopped at emission switch-on)"; slide 17
   claim "Any outcome…"; backup 21 power bullet adds "the data exclude only a
   uniform apex shift ≳2.5 map-SD" (`../rfx/analysis/field_indication_review_2026-09-29/SYNTHESIS.md:20`),
   columns rebalanced instead of `shrink=10`. Rejected: slide 14 "bound
   charge" → "screening charges" and "(no electrostatic counterpart)" — the
   left panel is a dielectric and bound-charge polarization *is* the
   electrostatic counterpart of the dipole regime (Livne 2023); the Debye
   wording stays in the correspondence strip as in the manuscript. Pending
   Yinon: title-slide author line (drop S. Calatroni, "W. L. Millar", order
   Bjelland, Millar, Wuensch as in the manuscript) — QUESTIONS 11.
   Other files in that folder (`PROPOSED_EDITS.md`, `QA_PREP*.md`,
   `TIMING_PLAN.md`, `deck_proposed.diff`) were not reviewed here.
   **2 Oct 12:30, published PDF checked:** the paper gives no denuded-zone
   thickness and names the denuded zone only for the 30 K cathode (Fig. 10);
   at 300 K it says "significantly reduces the number of dislocation walls"
   (Fig. 9). Deck images are HUJI lamellae of the 300 K cathode. Slide 4
   caption now "dislocation-poor zone in the top ~200 nm" (200 nm read from
   images, used by cond26 L64); backup 22 tags "fewer walls" / "walls to
   surface" at 300 K; both notes state the paper's wording; source lines
   credit HUJI STEM shown at MeVArc 2025. See `REVIEW_CONTEXT.md` §3.7b.
   Full item-by-item disposition for the other agent:
   `HANDOFF_TO_TALK_AGENT_2026-10-02.md` (copy placed in
   `../proj26/talk_mevarc26/HANDOFF_FROM_DECK_AGENT_2026-10-02.md`).

---

## 4. Working in this repo

### Build

```bash
cd ".../clic/mevarc26"
make            # both PDFs; or:
latexmk -pdf -interaction=nonstopmode main.tex
latexmk -pdf -interaction=nonstopmode main-notes.tex   # wrapper that defines \shownotes
latexmk -c main.tex; latexmk -c main-notes.tex           # clear aux files, keep PDFs
```

Render slides for inspection without poppler:
`python3 -c "import fitz; d=fitz.open('main.pdf'); [p.get_pixmap(dpi=60).save(f'/tmp/s-{i+1:02d}.png') for i,p in enumerate(d)]"`.

### Files

- `main.tex` — the deck, single file, self-contained preamble. Helper macros:
  `\claim`, `\tagbox`, `\source`, `\figorbox`, `\condref`.
- `main-notes.tex` — one-line wrapper for the notes build.
- `figures/` — only used figures plus the Sigma-3 assets
  (`full_range_overlay.pdf`, `ipf_*.png`, `mddf_nucleation_rate.png`).
- `knowledge/` — evidence base (see `knowledge/README.md`). September files:
  `cond26_changes_2026-09.md`, `rfx_status_2026-09.md` (with 28 Sep addendum),
  `mevarc26_programme.md`.
- `sources/` — cited papers, the July manuscript snapshot (`main.pdf`), the
  2013/2024/2025 decks.
- `abstract_mevarc26.md` — abstract as drafted; the programme shows it was
  accepted under the registered title above.
- `presentation_map.md` — the July plan (historical).
- `.cursor/rules/` — `general-english-writing.mdc`, `physics-research-writing.mdc`.
- `QUESTIONS.md` — open decisions only.
- `REVIEW_CONTEXT.md` (30 Sep) — self-contained brief for an external
  reviewing agent: slide-by-slide claims with strength labels, every number
  with its derivation, manuscript line anchors, RFX claim limits, checks to run.

### Sibling directories (read-only from here)

- `../cond26/` — manuscript (`main.tex`, `refs.bib`, `figures/`, `TODO.md`,
  `Rev1/` referee response). Edited as recently as 28 Sep 00:21.
- `../rfx/` — `STATUS.md` (log), `HANDOFF.md`, `NEEDED.md` (all 15 Sep),
  `presentation/` (Sep summary deck and one-sliders reusable if RFX grows).
- `../reports/2026_interim/` — interim report and work plan (Jul).
- aihome style rules: `~/Library/CloudStorage/GoogleDrive-*/My Drive/aihome/style/rules/`
  (only "… 2.mdc" Drive duplicates exist there; copied under clean names).

### Git

`origin/main` on GitHub is the reference; this directory lives on Google Drive
and its `.git/index` was once emptied by sync (fixed with `git read-tree HEAD`,
no content lost). If `git status` ever shows every file as deleted-and-
untracked again, that is the same symptom: rebuild the index, do not reset.

---

## 5. Decisions already made — do not re-open

30 min excluding questions; review-weighted balance; `E_S` delayed to one line
on the payoff slide (and the infographic on the conclusion); "candidate
structural basis for `E_S`" claim strength; ~200 nm denuded zone; two RFX
main-path slides with RFX framed as ongoing work, no field claim; 2025 figure
reuse; template branding per `ea22740`; slide 14 states the manuscript's
screening claim (ℓ_D ≈ 25 nm, thickness not predicted) and does not name `E_S`;
title and subtitle follow the Indico registration.

## Final touches, 2 Oct 2026 (talk agent, afternoon)

Baseline `main.tex` sha1 156e93f31d (commit 0636a65). Changes:

| Commit | Change | Source |
|---|---|---|
| b0dbe09 | Slide 8 source line: ~40 nm at 15 kV attributed to CASINO Monte Carlo (Drouin 2007); measured 38–72 nm over 5–30 kV attributed to Chen 2011 | proj26/lit/cards/chen2011.md (Table 2, Fig. 12); cond26/main.tex L383 cites both |
| e542781 | Speaker notes of the 18 core frames tightened for a fast 30-min delivery: 1754 → 1392 words; every fact, number and citation kept; sentences that repeated the slide removed; slide-17 note now says zero breakdowns | proj26/talk_mevarc26/final_pass/NOTES_REVISED.md; rfx/HANDOFF.md L20–21 |

Re-base of `proj26/talk_mevarc26/deck_proposed.diff` (23 hunks, cut against sha1 5cb00188ff) onto 156e93f31d — disposition (`proj26/talk_mevarc26/final_pass/REBASE_AUDIT.md`):
- Applied: E13 (above). 
- Already covered by commits dee2429 / b58b25e / 0636a65: E03, E06, E07 (slide 4 priority bullet hedged, b58b25e hunk 3), E08, E09, E12, E14, E15, E19, E20, E22, E25, E29–E31, E33, E34, E36–E38, E40, E41, E44, footer dates.
- Dropped as wording preferences without a factual source, or contradicting binding decisions: E02, E04, E05, E10, E11, E16–E18, E21, E23, E24, E26, E27, E32, E35, E39, E42, E43 (slide 14 wording frozen), M01/M02 (frame moves), `shrink=` hunks.
- For Yinon: E01 author line (QUESTIONS 16); slide-14 regimes paragraph (QUESTIONS 17).

Slide walk against REVIEW_CONTEXT.md §2–§3 and cond26 (`final_pass/SLIDE_WALK.md`, cheap sub-agent, text-only): no number, citation or verb mismatch found; no "confirms"; priority claim hedged; sentence-case titles. Builds: `make` clean, worst overfull 2.3 pt (unchanged). Q&A: `proj26/talk_mevarc26/QA_PREP.md` has a dated update section (five corrected answers, three new questions).

## Design pass, 2 Oct 2026 (talk agent, evening)

Baseline commit 00689de (23 pages). Result: 26 pages = 21 core + 5 backup; `make` clean,
worst overfull 2.64 pt (frame 10, tikz picture width); `main-notes.pdf` 26 pages. Author-approved
design changes from `proj26/talk_mevarc26/design/{A_explainer,B_legibility,C_motivation}/PROPOSALS.md`.
Binding rules kept: claim verbs, "to our knowledge", ~200 nm, slide 14 (now 16) untouched, title/subtitle/
template unchanged, RFX ongoing with no field effect, no `\shrink`.

| Commit | Frame (new no.) | Design ID | Change | Source |
|---|---|---|---|---|
| b28896a | preamble | B1 | tier colours `tierhigh`=copper (center+edge), `tierlow`=purple (periphery), `tierref`=teal (reference); `\tierkey`; tikz libraries; `qrcode`; `\bignum` | B_legibility §2 B1 |
| b28896a | 3 | C2, B15 | title → "Our model: breakdown as collective dislocation dynamics"; scriptsize captions under the two MDDF plots; note ends "Next slide: what that sentence means for a measurement." | C_motivation C2; B15 |
| b28896a | 4 (NEW) | C1 | "What the model says the microscope should see": four-box chain, two bullets, predicts / does-not-predict tags, brace "no equation for conditioning yet"; note (84 words) | C_motivation C1, `code/frame_motivation.tex`; Engelberg 2018/2019/2020 |
| a02c410 | 8 | A P3 / B6 | one figure `figures/geometry_efield_tiers.pdf`: cross-section (r_i 6.5, r_o 20 mm, gaps 60/70 µm, ×100 exaggerated) over E(r) in MV/m with tier shading, ROI markers, reference note; `\tierkey` under the columns; source line shortened | cond26 L94–101; **E(r) digitized from `cond26/figures/efield_vs_radius.eps`** (the finite-element data file is not in the Drive; `figures/efield_r_En_digitized.csv`, matches `design/B_legibility/efield_r_En.npy`); ROI radii `results.json` |
| a02c410 | 9 | B7 | SEM callouts `figures/sem_lowmag_callouts.png` (ROI box "EBSD map 500 µm wide", three craters, 0.47 mm arrow, 1 mm bar); bullet "LAM = local average misorientation …"; source line now two rows, fits | B7 pixel calibration (HFW 2.76 mm / 1800 px) |
| a02c410 | 10 (NEW) | A P2 | "What one EBSD pixel measures": four TikZ panels at true size (no resizebox); panel 1 without the 70° tilt, panel 4 without the ρ_GND formula (wording per author); one-line bold take-home instead of a `\claim` box (height); note 71 words | A_explainer P2, `ebsd_explainer.tikz` (redrawn); results.json means 0.68 / ~1.2° |
| 95a8bad | 12 | B4 | LAM pair cropped to a matched 485 × 279 µm field, identical 100 µm bars, tier-coloured chips, one labelled 0–5° bar (`figures/lam_pair_matched.png`); source line updated (magnifications matched) | B4 (0.62 / 0.53 µm px from the OIM bars) |
| 95a8bad | 13 | B2 | `figures/tiers_plot.pdf` at final size: direct labels, tier shading, reference band ±1 s.e., 75 % bracket | results.json |
| 95a8bad | 14 | B3 | `figures/tail_plot.pdf`: tier colours, faded histograms, gamma fits, dotted 2° line, shaded tails; side-box numbers `\Large` | results.json (center ROI2, edge ROI2, periphery ROI2, REF center ROI1) |
| 97c75fc | 15 | A P4, C4 | flow diagram → "one mechanism, two starting populations" cartoon labelled "the manuscript's interpretation"; bullet 1 ends "ordered as MDDF predicts"; bullet 2 absorbed by the cartoon; E_S line and claim unchanged | cond26 L376–389; Jacewicz 2025 |
| ce00357 | 17 | — | "Call for cooperation" box removed (moved to 21) | — |
| ce00357 | 19 | B9 | status as four large numbers (90 h, 73 h / 59–61 / 0 / 26) with captions; former status sentence kept below; columns 0.42/0.56 | rfx/HANDOFF.md L20–21; REVIEW_CONTEXT §6 |
| ce00357, 48b8e21 | 20 | B8 | infographic → `figures/result_card.pdf` (1.21°, 1.19°, 0.79°, 0.68°, ~75 % bracket); footer "Full infographic in backup" (backup 26 unchanged) | results.json |
| ce00357 | 21 (NEW) | — | "Conclusions, and an invitation": three one-line conclusions; `\qrcode` + `\href` to https://arxiv.org/pdf/2606.19192 (`\Large`); invitation box (author text); M. Coman cross-reference kept in the source line; note 58 words | — |

Figure generator: `figures/make_design_figures.py <figures dir> <results.json> <efield csv>` (matplotlib, env with
pypdfium2/scipy/PIL); all six new figures are drawn at their on-slide size, fonts ≥ 7.5 pt.

Speaker notes revised in `main.tex` (every frame whose visible content changed): 3 (last sentence → pointer to
3b), 4 new, 8 (describes the combined figure, the tier colours and the markers), 9 (callouts: ROI box, craters,
half a millimetre; LAM spelled out), 10 new, 12 (same magnification, cropped field), 13 (tier colours, band),
14 (dotted 2° line, shaded tails), 15 (cartoon described; C4 sentence "Size, depth and sign were not predicted;
the sign is set by the starting population"), 17 (invitation deferred to the last slide), 19 (four numbers
spoken as a strip), 20 (four bars with their values; pointer to the link slide), 21 new. Every fact, number and
citation of the previous notes is kept.

Not done / for Yinon: C3 (slide 6 "threshold-free" wording) and C5 were not in the approved list and were not
applied; B5 (annotated STEM pair), B10–B14 (backup legibility) not applied. REVIEW_CONTEXT §3 headings still use
the old slide numbers (mapping line added at the top of §3). Frame 17 (old 15) now has free space at the bottom
where the cooperation box was.

### RFX exposure reduced (author instruction, 2 Oct evening; supersedes B9)

RFX is future work and the RFX group is not part of this presentation. Frame 19 (old 17): the four-number
status strip and the three outcome tags were removed; the slide now carries the two material boxes, two bullets
(the four knobs; "a first continuous-DC campaign with Consorzio RFX is under way (first run: 90 h and 73 h DC,
zero breakdowns); analysis ongoing, no field effect claimed"), the RFX logo and credit line (De Lorenzi, Pilan,
Spada) and the hand-over line "RFX HV program: N. Pilan, next talk (12:30)" (US spelling "program"). Frame 18
(old 16): material axis as one bullet, RFX thumbnails dropped, source "Interim work plan (2026)". Frame 21:
conclusion 3 ends "— a stainless-steel test with Consorzio RFX is under way"; invitation box unchanged. Notes of
18, 19, 21 rewritten (brief, forward-looking, credit RFX, point to Pilan). Backup frames 22–24 (RFX first look,
status table, apex-vs-unexposed board) unchanged and remain the only place with status/null/power detail.


## Final repeat pass, 2 Oct 2026 (evening)

Baseline 6cbdb4e (26 pages). Result: `main.pdf` and `main-notes.pdf` 26 pages each (21 core + 5 backup),
`make` clean, worst overfull 1.61 pt (frame 4 line 314; was 2.64 pt), no undefined references, no missing
figures; the only log warning is the pre-existing hyperref `\translate` token on `\appendix`.
Full report: `../proj26/talk_mevarc26/final_pass/FINAL_REPEAT_PASS.md`.

| Commit | Frame | Change | Source |
|---|---|---|---|
| e868c65 | 17 | empty lower half filled with a "Limits of this dataset" line (field and breakdown density covary, ~24/12/5 per cm² center outward; LAM relative, internal comparisons) + missing source line | cond26 L107, L413–416; the frame's own note |
| 1cee8b2 | 10 | panels 2/4 shifted 1 mm left; overfull 2.64 pt → 0 | tikz bbox 400.98 vs 398.34 pt |
| b2ef4dc | 22, 24 | backup legibility, one page each: 22 = two large SEM crops (#1-25, #3-25) + electrode photo; 24 = 2 of 4 board panels (wide class) redrawn at slide size by `figures/make_rfx_board_backup.py` (reads `../rfx/analysis/ebsd_orientations_all_2026-09-29/per_map_table.csv`; rfx untouched), tier colors; bullet "inside or below"; caption names the one point above range | VISUAL_QA.md; rfx FINDINGS.md L82–84 |
| d9729a7 | 14 | tail-plot annotation 0.45° → 0.46° (θ = 0.4577 for FE Center ROI2) | results.json; cond26 L325 |
| 20f1e8a | 8, 10, 14, 15, all | layout only: `\source` ends with `\par`; frames 8 and 14 figures no longer cover the title rule; frame 10 no hyphenation, lattice lines clear of the panel-4 title; frame 15 labels on fill, arrows off the ~200 nm label; frame 14 gamma line spacing | renders |
| 5660577 | 5, 7, 21, 23, 24 | "catalogue" → "catalog"; no line-initial dash in conclusion 3; caption line spacing; backup-24 note aligned with bullet | FINDINGS.md L82–84 |
| a503680 | — | rebuilt PDFs (17.8 MB each), this section; the unused crop `rfx_sem_cavity_fe4.png` was removed in d9729a7 | — |

Checks: QR decodes (zxing-cpp 3.1.1) to `https://arxiv.org/pdf/2606.19192` in both PDFs; both link annotations
carry the same URI; arXiv API returns v4 "Direct large-area observation of subsurface plastic activity in conditioned
copper electrodes". Notes present on all 21 core frames; 1688 note words = 13.0 min at 130 wpm. Colors follow the
tier key on every copper data slide; backup 26 (manuscript infographic) keeps the paper's palette and its
"0.24° → 0.45°" label. Not touched (binding): frame 16 (old 14) wording and layout; title/subtitle.
`figures/rfx_board_apex_vs_unexposed.png` and `sem_page-2/4.png` are no longer shown but kept (full-board and
crop sources). Open items for Yinon: report §"Questions for the author".

## Frames 18-19 restructure, 2 Oct 2026 (late)

Baseline 66843a8 (26 pages). Author instruction (2 Oct late evening): frame 18 thumbnails out of place, use a
different figure and rethink the structure; frame 19 without the two-phase story, without "pass-or-fail",
not apologetic; message = different material, different structural evolution, building toward the next
campaign. Later the same evening: other speakers' talks must not appear as `\source` entries.
Result: `main.pdf` and `main-notes.pdf` 26 pages each (21 core + 5 backup), `make` clean, worst overfull
1.61 pt (frame 4 L314, unchanged), no undefined references. The only vbox overfull (0.55 pt) is backup 22,
pre-existing. Grep of the main path (lines before `\appendix`) for
`metastable|ferrite|alpha|pass-or-fail|martensit|austenit|phase transf`: no hits; backup 23 keeps the XRD
δ-ferrite fact.

| Commit | Frame (main.tex lines) | Change | Source |
|---|---|---|---|
| b512f3c | 18 (L767-812) | Two thumbnails (STEM, LAM) replaced by one TikZ "two coordinates" diagram: logarithmic depth axis (~40 nm EBSD, ~200 nm STEM, ~1 µm lamellae), material axis (copper, pulsed DC → AISI 304L, continuous DC); this work = filled `tierhigh` point at (Cu, 40 nm), labelled heat-treated Cu; 2025 STEM muted at (Cu, 200 nm), labelled hard Cu; purple "go deeper" arrow to a dashed target "matched lamellae, high field and reference"; `steel` "change the material" arrow to an open marker "first run 2026". Four bullets keep the depth content (matched lamellae, TEM/STEM + EBSD through ~1 µm, 2025 artifact controls, one depth profile) plus the steel pointer. `\claim` unchanged; note rewritten (79 words). | EBSD depth L440 (CASINO, Drouin 2007); ~200 nm in hard Cu L322 and §5; hard vs heat-treated L758 (frame 17 note); interim work plan (2026) |
| 1a08502 | 19 (L823-854) | Title "Steel: different material, different structural evolution" (the full "Stainless steel: …" version is 416 pt, the title box holds ~398 pt and it wrapped). Left: "What differs from copper" (lower SFE and planar slip; dislocation mobility; continuous DC = steady ~16 kPa traction, not ~10⁹ pulses) and one sentence on the test (does any field-correlated change appear at all?). Right: "First run with Consorzio RFX" as facts (304L at HVPTF, 90 h and 73 h at 59-61 MV/m, zero breakdowns, stopped at emission switch-on; 26 EBSD maps, HUJI, I. Popov, exposed apex inside or below the unexposed range; nothing mapped before exposure, so this design cannot establish a field effect), RFX logo and credit. Below: "Next campaign: one electrode mapped before and after being driven into breakdowns", Pilan hand-over line, claim "Copper supports the memory; steel asks whether it is universal." Removed: metastable austenite, γ→α′, the four-knobs bullet, the pass-or-fail claim. No figure: `rfx_board_wide_2panel.png` would have ~6 pt labels at column width. Note rewritten (108 words; the commit message says 106). | QA_PREP.md L92 (SFE, planar slip), L101 and L141 (16 kPa = ε₀E²/2 at 60 MV/m), L112, L131; ../rfx/HANDOFF.md L20-23, L291; ../rfx/NEEDED.md L341; ../rfx/analysis/ebsd_orientations_all_2026-09-29/FINDINGS.md L82-84 |
| 694a44c | 2, 6, 8, 18, 21 | Talks removed from `\source` lines: frame 21 L897 (M. Coman; source now interim work plan + RFX project record), frame 2 L202 (W. Wuensch 09:15), frame 6 L368 (J. Wang, V. Zadin 16:00/16:30), frame 8 L419 (V. Bjelland 10:00; "geometry from Bjelland et al." kept). Each pointer moved into the frame's note as one "(Optional aside: …)". Coman is Monday 11:30, the talk before ours, not Thursday. Frame 18 STEM source reads "HUJI, I. Popov 2025". Pilan hand-over stays as a line on frame 19. | proj26/talk_mevarc26/PROGRAMME.md L12-22, L34-37, L99-109; MORNING_POINTS.md L52 |

Consistency read: frame 17 (claim "A stronger test changes both the material and the loading history"),
frame 20 (item 3 "Depth and stainless steel test whether the memory survives a change of scale, alloy, and
loading") and frame 21 (item 3 "a stainless-steel test with Consorzio RFX is under way") fit the new wording
unchanged. Backups 22-24 unchanged.

Residual questions for Yinon:
- Frame 19 says "inside or below the unexposed range" (FINDINGS L82-84, as backup 24), not "inside the range on
  every indicator": one map-level θ(L) slope sits above a two-map baseline (p = 0.2).
- Frame 19 says the design "cannot establish a field effect", not "cannot bound": backup 24 does give a bound
  (a uniform apex shift ≳ 2.5 map-SD is excluded).
- Forward line names a before-and-after electrode; backup 24 note names the annealed vs as-received design with
  sham electrodes. Both are in ../rfx/NEEDED.md L341; say both if asked.
- Title drops "Stainless" for length; alternative "Stainless steel: different material, different evolution"
  (348 pt) fits if "structural" can go.
- Frame 21 invitation box (author text) still has "before/after" (slash in prose); left as author text.
- Optional asides were added to the notes of frames 2, 6, 8 and 21; delete any you will not say.

Renders of the new pages 18 and 19 at scale 2: `renders_tmp/p18.png`, `renders_tmp/p19.png` (not committed).
