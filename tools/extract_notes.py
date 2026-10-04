#!/usr/bin/env python3
"""Build speaker_text.tex (beamer) from the \\note{...} of every active frame in main.tex.

The note text is not duplicated anywhere: main.tex stays the single source.
Usage: python3 tools/extract_notes.py [main.tex] [speaker_text.tex]

Layout (author spec, 5 Oct 2026, second version): a presentation-like PDF for
the presenter's laptop while main.pdf is on the projector, one page per page of
main.pdf in the same order (backup included). Header row: muted bold
"N / 21 · title" at left, a 3.4 cm thumbnail of main.pdf page N (thin gray
frame) at right. Below it the spoken sentences span the full text width, bold,
\\large (BODY_SIZE; 12 pt at the 11 pt base, \\Large would be 14.4 pt), line spacing 1.12, one paragraph per sentence, the transition
sentence (last spoken sentence) in copper. A continuation page "N / 21 (cont.)"
is used only when the spoken text alone does not fit. Bracketed asides go under
a thin rule at the bottom in \\small gray when they fit; otherwise all of them
go on one extra page "N / 21 · Q&A" right after the frame. Footer: venue left;
page words and cumulative minute mark (130 wpm) right. Word-count summary last.

Fit is decided by measuring every candidate text block in a first pdflatex run
(speaker_text_measure.tex) with the same fonts and widths as the final document.
Words inside bracketed asides are not counted as spoken.
"""
import os
import re
import subprocess
import sys

WPM = 130
src = sys.argv[1] if len(sys.argv) > 1 else "main.tex"
dst = sys.argv[2] if len(sys.argv) > 2 else "speaker_text.tex"


def strip_comments(text):
    """Remove LaTeX comments (unescaped % to end of line)."""
    return "\n".join(re.sub(r"(?<!\\)%.*$", "", line) for line in text.split("\n"))


def braced(text, i):
    """text[i] == '{'; return (content, index after the closing brace)."""
    assert text[i] == "{"
    depth, j = 0, i
    while j < len(text):
        c = text[j]
        if c == "\\":
            j += 2
            continue
        if c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return text[i + 1:j], j + 1
        j += 1
    raise ValueError("unbalanced braces at %d" % i)


def plain_words(latex):
    """Approximate spoken word count of a LaTeX fragment."""
    t = re.sub(r"\\[a-zA-Z]+\*?", " ", latex)
    t = re.sub(r"[{}$\\~]", " ", t)
    return len(re.findall(r"[A-Za-z0-9][\w'\-\.,]*", t))


# any bracketed block that starts with a lowercase word, e.g. [optional: ...],
# [if asked: ...], [two time constants: ...]
ASIDE = re.compile(r"\[[a-z][^\]]*\]")


def split_note(note):
    """Return list of (kind, latex): kind 'say' for spoken sentences, 'aside' for brackets."""
    # unwrap \qa{...} (main.tex macro that sets asides small and muted on the notes page)
    while "\\qa{" in note:
        k = note.index("\\qa{")
        inner, after = braced(note, k + 3)
        note = note[:k] + " " + inner + " " + note[after:]
    parts, last = [], 0
    for m in ASIDE.finditer(note):
        parts.append(("say", note[last:m.start()]))
        parts.append(("aside", m.group(0)))
        last = m.end()
    parts.append(("say", note[last:]))
    out = []
    for kind, txt in parts:
        txt = " ".join(txt.split())
        if not txt:
            continue
        if kind == "aside":
            out.append((kind, txt))
            continue
        # one paragraph per spoken sentence
        for s in re.split(r"(?<=[.?!])\s+(?=[A-Z0-9])", txt):
            if s.strip():
                out.append(("say", s.strip()))
    return out



text = strip_comments(open(src, encoding="utf-8").read())
title_m = re.search(r"\\title\{", text)
deck_title = braced(text, title_m.end() - 1)[0] if title_m else "Title"
appendix_at = text.find("\\appendix")

frames = []
for m in re.finditer(r"\\begin\{frame\}", text):
    i = m.end()
    if text.startswith("[", i):          # frame options, e.g. [t]
        i = text.index("]", i) + 1
    title = braced(text, i)[0] if text.startswith("{", i) else deck_title
    end = text.index("\\end{frame}", i)
    n = text.find("\\note{", i, end)
    note = braced(text, n + 5)[0] if n >= 0 else ""
    backup = appendix_at >= 0 and m.start() > appendix_at
    frames.append((title, note, backup))
nmain = sum(1 for f in frames if not f[2])

# ---- layout constants (beamer 16:9, 16 cm x 9 cm) --------------------------
REGION = 5.75          # cm: body + asides region below the header row
ASIDE_GAP = 0.42       # cm: rule and gaps above the asides
BODY_SIZE = "large"    # \\large = 12 pt at the 11 pt base (\\Large = 14.4 pt)
QA_SIZES = ["small", "normalsize", "footnotesize", "scriptsize"]  # [0]: under the rule
THUMB_W = 3.4          # cm: thumbnail width in the header row
PT = 72.27 / 2.54

PREAMBLE = r"""\documentclass[aspectratio=169,11pt]{beamer}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{graphicx}
\definecolor{ink}{HTML}{17243A}
\definecolor{copper}{HTML}{C7663A}
\definecolor{muted}{HTML}{5D6978}
\definecolor{thumb}{gray}{0.6}
\setbeamertemplate{navigation symbols}{}
\setbeamertemplate{background canvas}{}
\setbeamercolor{background canvas}{bg=white}
\setbeamercolor{normal text}{fg=ink}
\setbeamersize{text margin left=0.45cm,text margin right=0.45cm}
\newcommand{\pagefoot}{}
\setbeamertemplate{footline}{%
  \hbox to \paperwidth{\hskip0.45cm{\tiny\color{muted}MeVArc 2026 \textperiodcentered{} Mon 5 Oct 12:00}%
  \hfill{\tiny\color{muted}\pagefoot}\hskip0.45cm}\vskip0.22cm}
\newlength{\bodyw}
\newcommand{\BODYSIZE}{\%(bs)s}
\newcommand{\body}[1]{{\BODYSIZE\bfseries\linespread{1.12}\selectfont
  \setlength{\parskip}{0.30em}\raggedright #1}}
\newcommand{\asides}[2]{{\csname #1\endcsname\mdseries\color{muted}\linespread{1.0}\selectfont
  \setlength{\parskip}{0.18em}\raggedright #2}}
\newcommand{\headrow}[2]{%
  \vspace*{-0.25cm}%
  \begin{minipage}[t]{\dimexpr\textwidth-%(tw)scm-0.3cm\relax}\vspace{0pt}%
    {\large\bfseries\color{muted}\raggedright #1\par}\end{minipage}\hfill
  \begin{minipage}[t]{%(tw)scm}\vspace{0pt}%
    {\color{thumb}\setlength{\fboxsep}{0pt}\setlength{\fboxrule}{0.4pt}%
    \fbox{\includegraphics[page=#2,width=\dimexpr%(tw)scm-0.8pt\relax]{main.pdf}}}\end{minipage}\par
  \vspace{0.12cm}}
""".replace("%(tw)s", "%.2f" % THUMB_W).replace("%(bs)s", BODY_SIZE)


def body_tex(sents, last_is_transition):
    out = []
    for k, t in enumerate(sents):
        if last_is_transition and k == len(sents) - 1:
            out.append(r"{\color{copper}%s}\par" % t)
        else:
            out.append(t + r"\par")
    return "\n".join(out)


def aside_tex(asides):
    return "\n".join(x + r"\par" for x in asides)


items = []
for idx, (title, note, backup) in enumerate(frames):
    parts = split_note(note)
    items.append(dict(
        page=idx + 1, title=title, backup=backup,
        say=[t for kind, t in parts if kind == "say"],
        asides=[t for kind, t in parts if kind == "aside"]))

# ---- measurement pass -------------------------------------------------------
meas = [PREAMBLE, r"\begin{document}\begin{frame}",
        r"\setlength{\bodyw}{0.95\textwidth}",
        ]
for it in items:
    n = len(it["say"])
    for i in range(n):
        for j in range(i + 1, n + 1):
            meas.append(r"\setbox0=\vbox{\hsize=\bodyw\body{%s}}"
                        r"\typeout{MEAS %d body %d %d \the\dimexpr\ht0+\dp0\relax}"
                        % (body_tex(it["say"][i:j], j == n), it["page"], i, j))
    if it["asides"]:
        for c, size in enumerate(QA_SIZES):
            meas.append(r"\setbox0=\vbox{\hsize=\bodyw\asides{%s}{%s}}"
                        r"\typeout{MEAS %d aside %d 0 \the\dimexpr\ht0+\dp0\relax}"
                        % (size, aside_tex(it["asides"]), it["page"], c))
meas.append(r"\end{frame}\end{document}")
base = os.path.splitext(dst)[0] + "_measure"
open(base + ".tex", "w", encoding="utf-8").write("\n".join(meas))
subprocess.run(["pdflatex", "-interaction=batchmode", "-halt-on-error", base + ".tex"],
               check=True, stdout=subprocess.DEVNULL)
H = {}
log = open(base + ".log", encoding="latin-1").read().replace("\n", " ")
for m in re.finditer(r"MEAS (\d+) (\w+) (\d+) (\d+) ([\d.]+)pt", log):
    H[(int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4)))] = float(m.group(5))
region = REGION * PT
gap = ASIDE_GAP * PT


def h(page, kind, i, j):
    return H[(page, kind, i, j)]


# ---- layout decision --------------------------------------------------------
pages = []       # dicts: it, kind ('body' or 'qa'), i, j, cont, asides_here, qa_size
cont_frames, qa_frames = [], []
for it in items:
    p, n = it["page"], len(it["say"])
    spans = []
    i = 0
    while i < n:              # greedy fill; one page whenever the whole text fits
        j = i + 1
        while j < n and h(p, "body", i, j + 1) <= region:
            j += 1
        spans.append((i, j))
        i = j
    if len(spans) > 1:
        cont_frames.append(p)
    under = False
    if it["asides"]:
        li, lj = spans[-1]
        under = h(p, "body", li, lj) + gap + h(p, "aside", 0, 0) <= region
    for k, (i, j) in enumerate(spans):
        pages.append(dict(it=it, kind="body", i=i, j=j, cont=k > 0,
                          asides_here=under and k == len(spans) - 1))
    if it["asides"] and not under:
        qa_frames.append(p)
        fits = [c for c in (1, 0, 2, 3) if h(p, "aside", c, 0) <= region]
        size = QA_SIZES[fits[0] if fits else 3]
        pages.append(dict(it=it, kind="qa", qa_size=size, cont=False))

# ---- write the document -----------------------------------------------------
out = [PREAMBLE, r"\begin{document}", r"\setlength{\bodyw}{0.95\textwidth}"]
cum = 0
rows = []
for q in pages:
    it = q["it"]
    lab = "Backup" if it["backup"] else "%d / %d" % (it["page"], nmain)
    if q["kind"] == "qa":
        sec = int(round(cum / WPM * 60))
        out.append(r"\renewcommand{\pagefoot}{Q\&A, not spoken \textperiodcentered{} at %d:%02d}" % (sec // 60, sec % 60))
        out.append(r"\begin{frame}[t]")
        out.append(r"\headrow{%s \textperiodcentered{} Q\&A}{%d}" % (lab, it["page"]))
        out.append(r"\begin{minipage}[t][%.3fcm][t]{\bodyw}\vspace{0pt}\asides{%s}{%s}\end{minipage}"
                   % (REGION, q["qa_size"], aside_tex(it["asides"])))
        out.append(r"\end{frame}")
        continue
    sents = it["say"][q["i"]:q["j"]]
    words = sum(plain_words(t) for t in sents)
    if not it["backup"]:
        cum += words
    sec = int(round(cum / WPM * 60))
    if q["cont"]:
        lab += " (cont.)"
    else:
        rows.append((lab, it["title"], sum(plain_words(t) for t in it["say"]), cum - words))
    last = q["j"] == len(it["say"])
    out.append(r"\renewcommand{\pagefoot}{%d words \textperiodcentered{} at %d:%02d}" % (words, sec // 60, sec % 60))
    out.append(r"\begin{frame}[t]")
    out.append(r"\headrow{%s \textperiodcentered{} %s}{%d}" % (lab, it["title"], it["page"]))
    body_h = "%.3fcm" % REGION
    if q["asides_here"]:
        body_h = r"\dimexpr%.3fcm-%.3fcm-%.2fpt\relax" % (REGION, ASIDE_GAP, h(it["page"], "aside", 0, 0))
    out.append(r"\begin{minipage}[t][%s][t]{\bodyw}\vspace{0pt}" % body_h)
    out.append(r"\body{%s}" % body_tex(sents, last))
    out.append(r"\end{minipage}")
    if q["asides_here"]:
        out.append(r"\par\vspace{0.12cm}{\color{thumb}\rule{\bodyw}{0.4pt}}\par\vspace{0.06cm}")
        out.append(r"\begin{minipage}[t]{\bodyw}\asides{small}{%s}\end{minipage}" % aside_tex(it["asides"]))
    out.append(r"\end{frame}")

# summary page (after the last frame, so the pages above stay in step with main.pdf)
total = cum
half = (len(rows) + 1) // 2


def mmss(words):
    t = int(round(words / WPM * 60))
    return "%d:%02d" % (t // 60, t % 60)


def tab(rs):
    return (r"\begin{tabular}{@{}l p{4.3cm} r r@{}}\textbf{Frame}&\textbf{Title}&\textbf{Words}&\textbf{Starts}\\" + "\n"
            + "\n".join(r"%s & %s & %d & %s\\" % (l, t, w, mmss(c)) for l, t, w, c in rs)
            + r"\end{tabular}")


out.append(r"\renewcommand{\pagefoot}{%d spoken words, %.1f min at %d wpm}" % (total, total / WPM, WPM))
out.append(r"\begin{frame}[t]\relax{\large\bfseries\color{muted}Word count \textperiodcentered{} %d spoken words over %d main frames, %.1f min read aloud at %d words per minute\par}\vspace{0.15cm}" % (total, nmain, total / WPM, WPM))
out.append(r"{\tiny\begin{columns}[T,onlytextwidth]\column{0.5\textwidth}%s\column{0.5\textwidth}%s\end{columns}}" % (tab(rows[:half]), tab(rows[half:])))
out.append(r"\end{frame}")
out.append(r"\end{document}")
open(dst, "w", encoding="utf-8").write("%% Generated by tools/extract_notes.py from %s; do not edit by hand.\n" % src + "\n".join(out))
print("%s: %d pages (%d frames, %d main, + summary), %d spoken words, %.1f min at %d wpm; body font %s"
      % (dst, len(pages) + 1, len(frames), nmain, total, total / WPM, WPM, {"large": "12 pt (\\large)", "Large": "14.4 pt (\\Large)"}[BODY_SIZE]))
print("  continuation pages:", ", ".join(str(x) for x in cont_frames) or "none")
print("  Q&A pages:", ", ".join(str(x) for x in qa_frames) or "none")
