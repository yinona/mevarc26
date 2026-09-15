# MeVArc 2026 — conditioning and subsurface structural memory

LaTeX Beamer source for a 30-minute talk connecting the completed copper
conditioning study (`cond26`) to the RFX stainless-steel project as a future
direction.

## Build

```bash
make
```

Outputs:

- `main.pdf` — audience-facing 16:9 slides
- `main-notes.pdf` — slides with speaker notes on the right

The talk is review-weighted (30 min excluding questions), the sequel to the
MeVArc 2025 HUJI talk. 22 frames total: 18 core (5 background: operational
problem, MDDF model, 2025 Uppsala STEM, Maxwell/VHCF, last-year recap; 7 copper
results; 6 limits/future, including two RFX slides and one optional RFX
preliminary) plus 4 backup slides. `E_S` is delayed to a single mention in the
interpretation. The template uses the trilingual HUJI logo and emblem branding
(redesigned 2026-07-20).

Scientific status statements are frozen at the project record of 13 July 2026.
Refresh the RFX slides (15, 15b, and the backup tables) when newer acquisition
or conditioning data arrive. See `HANDOFF.md` for the current state and next
steps, and `QUESTIONS.md` for open decisions.

## Source material

- `cond26/main.tex` and its figures — copper EBSD manuscript
- `reports/2026_interim/` — interim report and depth-resolved work plan
- `rfx/` — project status, SEM survey, electrode geometry, and artifact review

