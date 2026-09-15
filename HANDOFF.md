# Handoff — MeVArc 2026 presentation (mevarc26)

Last updated: **2026-09-15**. Prepared for resuming work on 2026-09-16.
**The talk is at MeVArc 2026, 5–8 October, Montreux — about three weeks away.**

## Where things stand

The deck is at final-draft quality and compiles cleanly on this machine
(verified 2026-09-15): `main.pdf` and `main-notes.pdf`, 22 pages each.

- **Structure (22 frames):** 18 core + 4 backup. Part I (5): operational
  problem, MDDF model, 2025 Uppsala STEM, Maxwell/VHCF, last-year-recap bridge.
  Part II (7): geometry, EBSD method, how-to-read-LAM, FE-vs-REF visual,
  three-tier ~75% result, distribution tail, MDDF-confirmation payoff.
  Part III (6): established-vs-open + cooperation call, depth+material,
  stainless-steel test, optional RFX preliminary (15b, skippable), conclusion
  with 2025 bookend. Backups: RFX SEM survey, RFX status table, 2025 STEM pair,
  copper infographic.
- **All content decisions are applied:** `E_S` delayed to one line on the
  payoff slide + conclusion; MDDF and Uppsala STEM prior work strengthened;
  RFX limited to two main-path slides (+ optional 15b); 2025 figures reused;
  ~200 nm denuded-zone wording; AI-tell text pass done (2026-07-20).
- **Template:** redesigned 2026-07-20 evening (Yinon, other computer):
  trilingual HUJI logo + Nano on title, HUJI emblem on content slides, compact
  footer, RFX credited on the future-directions slide only.
- **Git:** everything through the template redesign is in commit `ea22740`
  (synced with GitHub `origin/main`). Work after it (knowledge refreshes,
  answered questions, abstract draft, mined figures, `sources/` papers, this
  handoff) was committed and pushed on 2026-09-15 as the resume baseline.

## Timeline check (done 2026-09-15)

- Deck edits: none since 2026-07-20 17:37 (commit `ea22740`).
- Post-July-20 additions found: `presentation_map.pdf` (Jul 21),
  `abstract_mevarc26.md` (Jul 29), file touches through Aug 6 (likely Drive
  sync). No content in the repo is dated after 2026-07-20.

## Priority list for tomorrow (2026-09-16)

1. **Refresh RFX status — most stale item.** Slides 15/15b and both RFX backup
   slides reflect the record of **13 July 2026** ("#2-25/#3-25 EBSD planned").
   Two months have passed: check Inna's emails / `../rfx/STATUS.md` for the
   14 Jul acquisitions and anything later; update or drop slide 15b
   accordingly. If field-exposed samples are still unindexable, that itself is
   worth one line on slide 15.
2. **Verify the manuscript citation.** Slides cite "submitted to PRAB;
   arXiv:2606.19192" (`\condref`, `main.tex` line 76). Confirm the arXiv ID is
   live and correct, and check for PRAB referee reports since 23 June — a
   verdict would change the source lines and possibly the novelty wording.
3. **Abstract:** `abstract_mevarc26.md` (drafted ~Jul 29). Confirm it was
   actually submitted to the conference; align its title with the deck title if
   either changed.
4. **Timing rehearsal.** 18 core slides in 30 min is tight. Removal order if
   long: 15b (RFX preliminary, marked skippable) → 5b (recap bridge) → merge
   slides 7+8 (EBSD method + LAM reading). The optional Sigma-3/grain-skeleton
   slide was left OUT; assets are ready (`figures/full_range_overlay.pdf`, IPF
   maps) if you decide to add it.
5. **Final polish:** check logo rendering on the title slide, footer venue
   text, and run one full read of speaker notes (they were deliberately left in
   spoken register).

## Build

```bash
cd ".../clic/mevarc26"
make            # or:
latexmk -pdf -interaction=nonstopmode main.tex
latexmk -pdf -jobname=main-notes -usepretex='\def\shownotes{}' -interaction=nonstopmode main.tex
```

## Key files

- `main.tex` — the deck (single file, self-contained preamble).
- `presentation_map.md` — approved plan (historical; deck has evolved past it).
- `knowledge/` — evidence base with source citations; `mevarc25_assets.md` and
  `mined_figures_2026-07-20.md` map reusable figures from the 2013/2024/2025
  decks; `status_refresh_2026-07-20.md` answers the July status questions.
- `abstract_mevarc26.md` — conference abstract draft (submission unverified).
- `QUESTIONS.md` — only the still-open decisions (trimmed 2026-09-15).
- `sources/` — cited papers and the 2013/2024/2025 MeVArc decks.

## Decisions already made — do not re-open

30 min excluding questions; review-weighted balance; `E_S` delayed; "candidate
structural basis for `E_S`" claim strength; ~200 nm denuded zone; two RFX
main-path slides; 2025 figure reuse; template branding per commit `ea22740`.
