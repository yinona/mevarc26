RFX status refresh — compiled 2026-09-28 from ../rfx/STATUS.md (mtime shown by ls: Sep 15 10:44)

## 1. Sample status

| sample | EBSD acquisition | indexability / pattern quality | conditioning (field, bursts, BDs) | source |
|---|---|---|---|---|
| #2-25 | APEX done 18 Aug (del. 20 Aug), 3 maps; July-22 maps now oldSIDE; LAM 2 Sep | indexes; 2 wide / 1 narrow; Area2 MA 3.27° (widest in study) | never installed (reference) | STATUS.md:38,204 |
| #3-25 | 13 Jul first; 27 Jul APEX/SIDE; 2–4 Aug +apex; 10 Aug +side (del. 13 Aug); LAM 3 Sep; .ang 14 Sep | 99.5% indexed (CI 0.13, IQ 2780); later apex IQ 2800–2960 | 90 h 07 m DC; 7 bursts, all before switch-on; peak 61 MV/m at 58 kV; no full BDs | STATUS.md:39,89–97,192 |
| #4-25 | 13 Jul first; no later usable map; no-repolish 13 Aug | poor patterns (sample-specific) | 72 h 41 m DC; 4 bursts, all after switch-on (~70 s); peak 59 MV/m at 56 kV; no full BDs | STATUS.md:40,89–97,524–535 |
| #1-25 (other) | 13 Jul first; apex complete 5 Aug; SIDE LAM 2 Sep (n=1, narrow); .ang 14 Sep | 97.2% indexed (CI 0.18, IQ 2310) | never installed (reference) | STATUS.md:37,192,201 |

## 2. Dated entries after 13 July 2026

- 21 Jul — Conditioning report and E(θ) received; 304L confirmed (certificate unrecoverable); Inna first EBSD deck (#3-25 indexes well).
- 23–24 Jul — Numerical EBSD exports; EBSD ferrite fractions judged inside the pseudo-symmetry noise floor.
- 26–27 Jul — EDS confirms δ-ferrite; XRD two-pair split; APEX/SIDE EBSD session on #3-25.
- 28 Jul — Nicola production chain; first apex-vs-side result (later withdrawn); two-pairs note.
- 29 Jul — XRD scanned the stub back face; IR CCD geometry; deformation twins at the cut.
- 30 Jul — Inna: XRD face is electropolished; “two deliveries” misread corrected; δ-at-depth becomes the decisive in-house test.
- 4 Aug — Apex heterogeneity: 28 Jul field claim withdrawn; wide/narrow dichotomy also on never-exposed #1-25.
- 5 Aug — Ref1 apex completed (2 wide / 2 narrow); SIDE θ ≈ 35°; Rietveld cards; microscope reserved 10–11 Aug.
- 13 Aug — FE3 SIDE ensemble with positions (all five narrow); Yinon: no repolish of #4-25; Ref1 SIDE is the 2×2 discriminator.
- 20 Aug — First #2-25 APEX maps (acquired 18 Aug); Area2 MA 3.27°; wide patches on three apexes (7/12 vs side 0/5).
- 21 Aug — Cu vs 304L framed as FCC + SFE, not FCC vs BCC; HANDOFF freeze.
- 23 Aug — LAM spatial ACF on dilated maps: 1/e is dilation scale; no field claim.
- 2 Sep — Ref1 SIDE exists (narrow, n=1); July-22 maps named SIDE; undilated LAM drop.
- 3 Sep — FE3 undilated LAM; raw ACF closes 0.3 µm LAM as a conditioning probe; mechanical-back XRD still finds ferrite only in Ref1/Ref2.
- 10 Sep — Independent five-map pack; July apex-vs-side ratio reproduced on never-installed #2.
- 14 Sep — First per-pixel .ang (five narrow maps); no field claim; wide-class .ang still asked; draft to Inna unsent.
- 15 Sep — Inna has no .up2 files; FE3 grain interiors cleaner than Ref1 (speculation: thermal history, not field). Latest dated entry.

## 3. Speaker summary

Since 13 July we have the conditioning record (~90 h / ~73 h DC, no full breakdowns) and extensive EBSD on #2-25 and #3-25; #4-25 still will not index and will not be repolished.
We cannot claim a stainless-steel field effect: the July apex-versus-side contrast is forming geography, reproduced on never-installed #2, and later tests put the #3 apex inside the unexposed range.

## 4. Deck statements now out of date (main.tex)

- L507 “AISI 304 … ≥100 h” → AISI 304L; 90 h 07 m (#3-25) and 72 h 41 m (#4-25); continuous DC, no full BDs.
- L510 “First plan-view EBSD: #1-25 good; #4-25 poor” → incomplete: #3-25 indexes 99.5%; #2-25 APEX done 18 Aug; #4-25 still poor (no-repolish 13 Aug).
- L529 “RFX status through 13 Jul 2026” → STATUS.md current through 15 Sep 2026.
- L566 “#2-25/#3-25 follow-up pending” → both acquired (#3 extensive apex+side; #2 APEX 18 Aug + LAM 2 Sep).
- L583 “#2-25 … follow-up acquisition planned” → APEX EBSD acquired 18 Aug (3 maps); LAM 2 Sep.
- L584 “#3-25 … ≥100 h HV … EBSD follow-up” → 90 h 07 m, peak 61 MV/m; EBSD done (apex, side, LAM, five-map .ang).
- L585 “#4-25 … ≥100 h HV … poor initial EBSD” → 72 h 41 m, peak 59 MV/m; still poor; SEM/EDS-only unless re-attempt as-is.
- L590 “Outstanding: full conditioning report; numerical E(θ); alloy certificate; electropolishing protocol” → report and E(θ) arrived 21 Jul; 304L confirmed, certificate unrecoverable; EP partly known (40 °C, 4–8 min, Ricerca Chimica).
- L591 “Needed: quantitative EBSD quality metrics and raw patterns” → metrics exist; five-map .ang in (14 Sep); no .up2 (15 Sep); wide-class .ang still open.
- L572 “RFX status 13 Jul 2026” (backup SEM source line) → same refresh as L529.
