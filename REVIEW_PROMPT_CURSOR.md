# Review prompt for the Cursor agent (mevarc26)

Copy everything below the line into the Cursor agent working in this repository.

---

You are reviewing a finished Beamer deck for a 30-minute conference talk (talk plus questions) that will be given on Monday 5 October 2026 at 12:00: "Does conditioning leave a structural memory? Large-area evidence for the dislocation picture" (MeVArc 2026, Conditioning session). The author is a materials-physics professor speaking to specialist colleagues. Your job is to CHECK the presentation and its logic and to REPORT. You are in REVIEW-ONLY mode: do not edit `main.tex`, do not rebuild, do not commit, do not push, do not upload anywhere.

## Read first, in this order

1. `CHANGES_2-4_OCT.md` — what changed in the last two days and the binding wording rules (section 2) and numbers (section 5). Treat section 2 as decisions already taken: you may flag a conflict, you may not propose to reverse them.
2. `HANDOFF.md` §5 "Decisions already made — do not re-open" and the sections dated 2–4 Oct.
3. `main.tex` (source of truth; notes are `\note{…}` with `\qa{…}` asides), `main.pdf` (22 pages: 21 main + 1 backup), `speaker_text.pdf` (23 pages: summary + one page per frame).
4. `REVIEW_CONTEXT.md` §2 (page map) and `QUESTIONS.md`.
5. For claim checking only: the copper paper is arXiv:2606.19192 (v4); the RFX facts are as stated on frame 19 (treat them as given; the project record is outside this repo).

Render the PDF pages to images and look at them (e.g. `pdftoppm -r 110 -png main.pdf out/p`); do not review from extracted text alone. State what you inspected.

## What to check

A. **Argument and continuity.** Reconstruct the spine in one paragraph (question → model → local evidence → sub-yield load → bridge → experiment → result → sheath mechanism → limits and next → answer → what/where/what-next). For every frame: what step does it contribute, and does the transition sentence in the speaker text actually connect to the next frame? Flag missing links, repeated content, and any concept used before it is introduced (e.g. "frustrated crystal", "sheath", "ℓ_D", "LAM", "tiers").

B. **Claim fidelity.** For each main claim, classify: observation / derived quantity / model prediction / fit / interpretation / hypothesis. Flag any slide or spoken sentence that states an interpretation as a result, a fit as a prediction, consistency as confirmation, or a priority claim without "to our knowledge". Check the forbidden words list in `CHANGES_2-4_OCT.md` §2 across slides AND speaker text.

C. **Numbers and consistency.** Every number in §5 of `CHANGES_2-4_OCT.md` must agree between slides, speaker text and figure labels. Check units, significant figures, and that no number appears in one place with a different value elsewhere.

D. **Sources.** Keyed markers (superscript letters) only for published or arXiv sources; each marker must point to the line it supports; "Sources:" letters must match; no other speaker's talk may appear as a source; internal records are not sources. Report any orphan marker or unlettered source.

E. **Visual QA.** On every rendered page: overlaps, clipping, orphan words, markers colliding with punctuation, text below ~8 pt on main-path frames (accepted exceptions: small figure labels on frames 6, 8, 10, 15, 16), colour key consistency (copper/orange high field, purple periphery, teal reference), figure captions and scale bars present, QR present on page 21. Check `speaker_text.pdf` for legibility on a laptop screen (13 pt body) and that asides are visibly distinct.

F. **Timing.** Count the speaker-text words per frame (the summary page lists them) and estimate at 130 wpm; state which frames are long relative to their role and which could be compressed if the dry run overruns. Do not invent a rehearsal time.

G. **Q&A readiness.** List the five hardest questions a CERN/Uppsala/RFX colleague would ask after this deck, and check whether the speaker text's [if asked …] lines already answer them; flag gaps.

## How to work: parallel sub-agents

Use grok-4.7 sub-agents in parallel to save time and cost; you are the integrator. Suggested split (one sub-agent each, run concurrently):

1. Frames 1–7 (question, model, local evidence, sub-yield load, bridge): checks A, B, C, D, E for those pages.
2. Frames 8–15 (experiment and result): checks A–E; pay special attention to the numbers in §5.
3. Frames 16–22 (sheath, limits, next, steel, conclusions, backup): checks A–E; pay special attention to interpretation-vs-result wording and to the steel frame.
4. Speaker text only (`speaker_text.pdf` and the `\note{}` blocks): checks B, C, F, G across all frames, plus consistency of each note with its slide.
5. Sources and figures across the whole deck: check D plus figure provenance (every `\includegraphics` file exists; captions and credits; `figures/*.py` scripts present for generated figures).

Give each sub-agent the same reading list and the same forbidden-words and numbers lists; have each return a table with the schema below. Then merge, de-duplicate, and rank.

## What to return (one Markdown file: `REVIEW_CURSOR_<date>.md` in the repo root; do not modify anything else)

1. Argument summary (one paragraph) and the three messages a listener should retain.
2. Prioritized issue table: `ID | page/frame | severity (critical/major/minor) | observed problem | exact location (main.tex line or render) | proposed edit (concrete wording) | what must stay true | how to verify`. Critical = wrong or misleading science or an unreadable central result; major = missing logical link, inconsistency between slide and speaker text, number mismatch; minor = polish.
3. Claim record for the main claims (category, source, qualification needed).
4. Consistency checklist for §5 numbers (pass/fail per number with locations).
5. Timing table and compression candidates.
6. Q&A gaps.
7. What you inspected and what you could not (e.g. projector, rehearsal).

## Constraints

- Do not propose changes that reverse the decisions in `CHANGES_2-4_OCT.md` §2 or `HANDOFF.md` §5; if you believe one is wrong, say so in a separate "disagreements with prior decisions" list with the reason, and leave it to the author.
- Do not invent scientific details, replicate counts, error bars or references; distinguish "not reported" from "absent".
- Do not edit, build, commit, push, or upload. Preserve the native Beamer source.
- Keep the main report under ~3 pages; put long tables in an appendix section of the same file.
