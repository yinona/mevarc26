# Status refresh — 2026-07-20

Answers to QUESTIONS.md items 14–16, gathered from sibling directories
(`../rfx`, `../cond26`, `../research`, `../reports`, `../meetings`). Text/markdown
sources only; no PDF/PPTX/image bytes read.

---

## Q14 — RFX experiment status after 2026-07-13

### What we found

**Last documented state (2026-07-13):** First plan-view EBSD acquisitions on
as-received electropolished surfaces were done 12–13 Jul 2026.

| Sample | Result (13 Jul) |
|--------|-----------------|
| **#1-25** (reference) | Good dataset — LAM, misorientation charts, grain sizes extracted; pipeline validated on AISI 304. |
| **#4-25** (field-exposed) | Poor diffraction-pattern quality under identical excitation; higher beam current / longer exposure did not recover it. |
| **#2-25** (reference) | SEM not yet done; **scheduled for EBSD 14 Jul 2026**. |
| **#3-25** (field-exposed) | SEM done (exploded inclusion sites 3–7 µm); **scheduled for EBSD 14 Jul 2026**. |

Inna's candidate causes for poor #4-25 patterns: (a) electropolish prep
variation, (b) conditioning-induced near-surface defects (signal depth 20–50 nm),
(c) contamination/oxide overlayer from ≥100 h HV exposure. Proposed discriminators:
repeat on #3-25/#2-25; pattern quality vs apex→periphery field gradient on one FE
sample; EDS carbon check.

**After 2026-07-13:** No text record found that #2-25 or #3-25 EBSD was completed,
failed, or reported. No new EBSD data files in `../rfx/data/` (only field-simulation
`.txt` files). Draft reply to Inna (`draft_reply_inna_2026-07-13.md`) was still
"not yet sent" at the 13 Jul session end. `STATUS.md` and `.agent/HANDOFF.md` were
file-modified 2026-07-19 but their content still stops at 13 Jul; next action listed
as "log Inna's 14 Jul results when they arrive."

**Other RFX context (unchanged since before 13 Jul):** Samples at HUJI since 27 Apr
2026; cutting done; as-received SEM survey complete (Inna, 20 May 2026); conditioning
report and field-vs-angle vector from RFX still not received; depth-profiling/FIB
artifact debate remains open if FE samples stay unindexable.

**Meetings / reports:** No RFX-specific updates in `../meetings/` (grep, Jul 2026).
`../reports/2026_interim/workplan.tex` (modified 2026-07-19) describes the RFX track
as exploratory — SEM survey complete, sectioning started, EBSD protocols not yet
validated on steel; no mention of 13 Jul EBSD results or #2-25/#3-25 outcomes.

### File evidence

| Path | Date (mtime / content) | Relevance |
|------|------------------------|-----------|
| `../rfx/STATUS.md` | Content **2026-07-13**; mtime 2026-07-19 | Authoritative status snapshot; §3 data inventory, §4 current state |
| `../rfx/correspondence/email_inna_ebsd_first_results_2026-07-13.md` | Content 2026-07-13; mtime 2026-07-19 | Inna's first-results email (#1-25 good, #4-25 poor; #3-25/#2-25 tomorrow) |
| `../rfx/correspondence/draft_reply_inna_2026-07-13.md` | Drafted 2026-07-13; mtime 2026-07-19 | Reply not sent; analysis of poor FE patterns |
| `../rfx/.agent/HANDOFF.md` | Content **2026-07-13**; mtime 2026-07-19 | Next action: log 14 Jul results |
| `../reports/2026_interim/workplan.tex` | mtime 2026-07-19 | RFX parallel track; no post-13-Jul EBSD detail |

### Gap

**No information found** on whether #2-25 / #3-25 EBSD was acquired on or after
14 Jul 2026, or on any updated EBSD quality metrics/maps beyond the #1-25 / #4-25
13 Jul report. Presentation should keep Slide 15 / backup table at "follow-up
acquisition planned" until Inna confirms.

---

## Q15 — One-cathode limitation / newer copper cathode data

### What we found

**No new copper cathode EBSD data** that would weaken or remove the single-specimen
caveat. All indexed text sources still describe **one conditioned cathode (FE) + one
external reference (REF)**, nine ROIs on the FE cathode, with the ~75% mean
misorientation headline tied to that pair.

The submitted manuscript explicitly limits scope:

> "All results come from a single conditioned cathode and a single reference, so the
> ~75% figure characterizes this material state and conditioning history rather than
> conditioning in general." — `../cond26/main.tex` (Discussion, limitation paragraph)

The 2026 interim report (modified 2026-07-19) repeats the same limitation and
frames **additional cathodes** as future work ("whether the E_S match survives on
additional cathodes"), not as completed data. Next-stage workplan points to depth
profiling (pilot FIB lamellae from already-characterized ROIs, finer-step EBSD) —
not a second cathode campaign.

**Data freshness:** No markdown/text/csv files in `../cond26/ebsd2/` or
`../research/` with modification dates after the 2026-06-23 PRAB submission.
Last grain-count / Fig. 9 update was 2026-06-18 (mean grain sizes 26–30 µm;
within-FE decoupling unchanged). `../research/microscopy/surface_ebsd/` contains
only a legacy `readme.txt` naming FE/REF ROIs — no new notes.

### File evidence

| Path | Date | Relevance |
|------|------|-----------|
| `../cond26/main.tex` | mtime 2026-06-23 | Single-cathode limitation (Discussion); novelty + ~75% headline |
| `../cond26/TODO.md` | mtime 2026-06-23 | Grain-size update 2026-06-18; Table I / headline unchanged |
| `../reports/2026_interim/report.tex` | mtime 2026-07-19 | "one conditioned cathode and one reference"; next stage = depth + more cathodes (future) |
| `../reports/2026_interim/workplan.tex` | mtime 2026-07-19 | Pilot FIB from existing ROIs; no second cathode dataset |

### Gap

**No information found** of a second conditioned cathode, replicated EBSD campaign, or
revised statistics that would change the talk's "single conditioned cathode" caveat.
Keep the limitation on the main path; interim report language is consistent.

---

## Q16 — cond26 manuscript / PRAB submission status

### What we found

**Submission:** Manuscript **submitted to PRAB on 2026-06-23**. Git tag
`prab_submitted_2026-06-23`. Final submission PDF:
`../cond26/archive/Ashkenazy_PRAB_submission.pdf`. Cover letter:
`../cond26/cover_letter_PRAB.md`.

**Post-submission journal correspondence:** **No information found.** No reviewer
reports, editor decision, revision requests, or response-to-referees files anywhere
under `../cond26/` (glob for `*response*` returned zero files). `../cond26/private/correspondence/`
last updated 2026-06-23; contains only pre-submission discussion summaries.

**arXiv:** `../cond26/TODO.md` lists arXiv upload of `archive/arxiv/cond26_arxiv.zip`
as **"Remaining"** (physics.acc-ph + cond-mat.mtrl-sci) — status unclear from repo
text alone; Bjelland companion already on arXiv:2606.21259 (cited in submitted version).

**Numbers (unchanged since submission):**
- Headline: mean intragrain misorientation ~**75%** higher in field-exposed vs unexposed regions (three metrics + KS tests).
- Grain sizes: mean **26–30 µm** (REF slightly > FE); cathode-to-cathode variation acknowledged; within-FE misorientation hierarchy unchanged (2026-06-18 update in TODO).
- Table I / low-angle moment table: no post-submission edits logged.

**Novelty claim (unchanged):** Abstract, Introduction, and Conclusions retain
"**To our knowledge, the first large-area observation** of dislocation-related
microstructural differences between conditioned and unconditioned regions of a
high-field electrode." No post-submission text edits to `main.tex` (last git commits
2026-06-23).

**Optional pre-submission item still open (not applied):** Expert review
(`../cond26/private/style_review/PRAB_EXPERT_REVIEW_2026-06-17.md`) recommended
softening mid-angle Mackenzie/subgrain wording ("captures/marks" → "consistent with").
`TODO.md` lines 15–19: awaiting Yinon; **no other prose changes recommended.**

**Git activity after submission:** `git log --since=2026-06-23` in `../cond26/` returns
empty — no commits after submission date.

### File evidence

| Path | Date | Relevance |
|------|------|-----------|
| `../cond26/TODO.md` | mtime 2026-06-23 | SUBMITTED 2026-06-23; arXiv remaining; optional mid-angle hedge |
| `../cond26/cover_letter_PRAB.md` | mtime 2026-06-23 | Submission cover letter; ~75% headline; suggested referees |
| `../cond26/private/handoffs/AGENT_HANDOFF_2026-06-23.md` | mtime 2026-06-23 | Session-close handoff; submit + arXiv checklist |
| `../cond26/private/style_review/PRAB_EXPERT_REVIEW_2026-06-17.md` | 2026-06-17 | Pre-submission expert review; single-specimen + mid-angle notes |
| `../reports/2026_interim/report.tex` | mtime 2026-07-19 | Cites manuscript as "submitted to PRAB (2026)" — no acceptance/review update |

### Gap

**No information found** on PRAB editorial decision, referee reports, or revision
round. Safe to cite submitted manuscript + Zenodo DOI 10.5281/zenodo.20623348; treat
review status as **pending / unknown** unless confirmed outside the repo.

---

## Presentation implications (brief)

| Question | Recommended deck treatment (2026-07-20) |
|----------|------------------------------------------|
| Q14 | RFX backup: report 13 Jul first EBSD (#1-25 good, #4-25 poor); #2-25/#3-25 still "planned" — confirm with Inna before promoting. |
| Q15 | Keep single-cathode caveat; no new data to cite. |
| Q16 | Cite PRAB submitted 2026-06-23; novelty + ~75% unchanged; no reviewer-driven edits to report. |
