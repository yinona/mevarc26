# Handoff — MeVArc 2026 presentation (mevarc26)

Last updated: **2026-09-28**. **The talk is at MeVArc 2026, 5–8 October,
Montreux — one week away.**

## Where things stand

The deck compiles cleanly (`main.pdf` and `main-notes.pdf`, 22 pages each,
16:9) and has been aligned with the September manuscript and the September
RFX record. Remaining overfull boxes are all below 3 pt.

- **Structure (22 frames):** 18 core + 4 backup.
  Part I (5): operational problem, MDDF model, 2025 Uppsala STEM (now labelled
  hard, as-machined Cu), Maxwell/VHCF with a pulse-train sketch, recap bridge.
  Part II (8): geometry (heat-treated OFE Cu), EBSD method (information depth
  a few tens of nm), how-to-read-LAM, FE-vs-REF visual, three-tier ~75%
  result, distribution tail, MDDF-confirmation payoff, **new elastic-screening
  analogy slide (14)**.
  Part III (4): established-vs-open + cooperation call, depth+material (with
  thumbnails), stainless-steel test with a one-line Sep-2026 status,
  conclusion with 2025 bookend.
  Backups: RFX first look (the former optional 15b, refreshed), RFX status
  table (15 Sep 2026), 2025 STEM pair, copper infographic (new Sep-27 version).
- **cond26 manuscript alignment (2026-09-28):** headline numbers unchanged
  (~75%, ~1.2° vs ~0.68°, eightfold tail, ~200 nm TEM zone). Changed and now
  reflected in the deck: screening length is `ℓ_D ≈ 25 nm` (the 200 nm layer
  is ~8 ℓ_D; thickness not predicted), not ~100 nm; EBSD information depth is a
  few tens of nm (3 µm step is lateral only); the STEM depletion was in hard
  Cu, the EBSD build-up in heat-treated Cu ("one mechanism, two starting
  populations"); `infographic.pdf` replaced; three new manuscript references
  (Lemaître 2021, Livne 2023, Chen 2011). `\condref` now reads "PRAB, under
  revision; arXiv:2606.19192" — the arXiv ID was verified live on 2026-09-28
  (title and five authors match). Details: `knowledge/cond26_changes_2026-09.md`.
- **RFX status (record through 15 Sep 2026):** #3-25 ran 90 h and #4-25 73 h
  of continuous DC at 59–61 MV/m peak with no full breakdowns; #1-25, #2-25,
  #3-25 give indexable EBSD (97–99.5%), #4-25 still does not and will not be
  repolished; the July apex-vs-side contrast reproduced on the never-installed
  #2-25, so no stainless-steel field effect is claimed. Alloy confirmed 304L.
  Details: `knowledge/rfx_status_2026-09.md`.
- **Review pass (2026-09-28):** two independent style reviews merged;
  uncontroversial items applied (slashes, standalone "this", US spelling,
  siunitx units, "no full breakdowns", 59–61 MV/m, slide-14 claim strength
  corrected to "dislocations screen the *internal* stress of a depleted
  layer"). Judgement calls are in `QUESTIONS.md` items 7–15.
- **Git:** all work through the review pass is committed and pushed to
  GitHub `origin/main` in phase-sized commits (Phase 0 rules, cond26
  alignment, RFX refresh, new slide, visual pass, review fixes).
- **Toolchain note:** poppler (`pdfinfo`, `pdftoppm`) is not installed on
  this machine; PyMuPDF (`python3 -c "import fitz"`) was used for page counts
  and slide rendering.

## Priority list (2026-09-28 → talk week)

1. **Timing rehearsal.** 18 core slides in 30 min. Cut order if long (both
   reviewers agreed): drop 6 (recap bridge, ~60 s) → move 14 (elastic
   screening) to backup (~100 s) → merge 9 into 10 (LAM how-to, ~50 s) →
   merge 15 into 16 or fold the slide-12 tail box onto 11 (~50–60 s). Total
   ≈ 4.5 min, which is the 25-min fallback.
2. **Manuscript status before the talk.** PRAB minor revision (ZT10260) was
   implemented on 2026-09-27; the resubmission is Yinon's action. If a verdict
   lands before 5 Oct, change `\condref` (`main.tex` ~line 116) to "accepted"
   or "in press".
3. **Decide the QUESTIONS.md items 7–10** (claim verb "confirms" vs "appears
   to"; E_S on the conclusion slide; periphery "~0 MV/m" legend in the
   manuscript figures; infographic legibility on slide 18). Each is a
   five-minute edit once decided.
4. **Abstract:** confirm `abstract_mevarc26.md` was submitted and that its
   title matches the deck (QUESTIONS.md item 3).
5. **Final read of speaker notes** in `main-notes.pdf`; check the title-slide
   logos and the footer once on the conference laptop.

## Build

```bash
cd ".../clic/mevarc26"
make            # or:
latexmk -pdf -interaction=nonstopmode main.tex
latexmk -pdf -jobname=main-notes -usepretex='\def\shownotes{}' -interaction=nonstopmode main.tex
```

## Key files

- `main.tex` — the deck (single file, self-contained preamble).
- `knowledge/` — evidence base with source citations.
  `cond26_changes_2026-09.md` (manuscript July→September diff, per deck
  frame) and `rfx_status_2026-09.md` (RFX record after 13 July) are the
  September refreshes; `status_refresh_2026-07-20.md` is the July one.
- `.cursor/rules/` — `general-english-writing.mdc`,
  `physics-research-writing.mdc` (copied from aihome on 2026-09-28).
- `presentation_map.md` — approved plan (historical; deck has evolved past it).
- `abstract_mevarc26.md` — conference abstract draft (submission unverified).
- `QUESTIONS.md` — only the still-open decisions (trimmed 2026-09-28).
- `sources/` — cited papers and the 2013/2024/2025 MeVArc decks;
  `sources/main.pdf` is the July manuscript snapshot.

## Decisions already made — do not re-open

30 min excluding questions; review-weighted balance; `E_S` delayed; "candidate
structural basis for `E_S`" claim strength; ~200 nm denuded zone; two RFX
main-path slides (15b now in backup); 2025 figure reuse; template branding per
commit `ea22740`; elastic-screening slide states the manuscript's claim
strength (ℓ_D ≈ 25 nm, thickness not predicted) and does not name `E_S`.
