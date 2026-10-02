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
   `sources/Jacewicz_2024_*.pdf` is the 2022 preprint and lacks the STEM
   section), "First direct" → "Direct"; slide 5 source credits J. Wang as the
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
