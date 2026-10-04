#!/usr/bin/env python3
"""Build speaker_text.tex (beamer) from the \\note{...} of every active frame in main.tex.

The note text is not duplicated anywhere: main.tex stays the single source.
Usage: python3 tools/extract_notes.py [main.tex] [speaker_text.tex]

Layout (author spec, 5 Oct 2026): a presentation-like PDF for the presenter's
laptop while main.pdf is on the projector. One page per page of main.pdf, same
order (backup included), so both documents advance in step; a frame whose text
does not fit gets continuation pages "N / 21 (cont.)". Each page: muted bold
header "N / 21 · title"; the spoken sentences in bold, one paragraph each, at
\\Large, stepped down to \\large only if needed (never smaller); the transition
sentence (last spoken sentence) in copper; a thumbnail of main.pdf page N
(4.2 cm, thin gray frame) top right; bracketed asides at the bottom in \\small
gray under a thin rule (cut to the first two plus "... (more in notes)" when
space is short); footer with venue left and page words plus cumulative minute
mark (130 wpm) right. Word-count summary on the last page.

Fit is decided by measuring every candidate text block in a first pdflatex run
(speaker_measure.tex) with the same fonts and widths as the final document.
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
REGION = 6.78          # cm: body + asides region below the header line
ASIDE_GAP = 0.42       # cm: space taken by the rule and gaps above the asides
SIZES = ["Large", "large"]

PREAMBLE = r"""\documentclass[aspectratio=169,12pt]{beamer}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{amsmath}
\usepackage{graphicx}
\usepackage{tikz}
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
\newlength{\textcol}
\newcommand{\body}[1]{{\csname #1\endcsname\bfseries\linespread{1.15}\selectfont
  \setlength{\parskip}{0.32em}\raggedright #2}}
\newcommand{\asides}[1]{{\small\mdseries\color{muted}\linespread{1.0}\selectfont
  \setlength{\parskip}{0.15em}\raggedright #1}}
"""
PREAMBLE = PREAMBLE.replace(r"\newcommand{\body}[1]", r"\newcommand{\body}[2]")


def body_tex(sents, last_is_transition):
    out = []
    for k, t in enumerate(sents):
        if last_is_transition and k == len(sents) - 1:
            out.append(r"{\color{copper}%s}\par" % t)
        else:
            out.append(t + r"\par")
    return "\n".join(out)


CUTS = (0, 2, 1)       # keep all asides; else the first two; else the first one


def aside_tex(asides, cut):
    a = asides[:cut] if cut and len(asides) > cut else asides
    tex = "\n".join(x + r"\par" for x in a)
    if len(a) < len(asides):
        tex += r"\ldots (more in notes)\par"
    return tex


items = []
for idx, (title, note, backup) in enumerate(frames):
    parts = split_note(note)
    items.append(dict(
        page=idx + 1, title=title, backup=backup,
        say=[t for kind, t in parts if kind == "say"],
        asides=[t for kind, t in parts if kind == "aside"]))

# ---- measurement pass -------------------------------------------------------
meas = [PREAMBLE, r"\begin{document}\begin{frame}",
        r"\setlength{\textcol}{0.68\textwidth}",
        r"\typeout{MEAS textheight \the\textheight}"]
for it in items:
    n = len(it["say"])
    for size in SIZES:
        for i in range(n):
            for j in range(i + 1, n + 1):
                meas.append(r"\setbox0=\vbox{\hsize=\textcol\body{%s}{%s}}"
                            r"\typeout{MEAS %d %s %d %d \the\dimexpr\ht0+\dp0\relax}"
                            % (size, body_tex(it["say"][i:j], j == n), it["page"], size, i, j))
    for cut in CUTS:
        if it["asides"]:
            meas.append(r"\setbox0=\vbox{\hsize=\textwidth\asides{%s}}"
                        r"\typeout{MEAS %d aside %d 0 \the\dimexpr\ht0+\dp0\relax}"
                        % (aside_tex(it["asides"], cut), it["page"], cut))
HEAD = r"{\large\bfseries %s \textperiodcentered{} %s\par}"
meas.append(r"\setbox0=\vbox{\hsize=\textwidth%s}\typeout{MEAS 0 head 0 0 \the\dimexpr\ht0+\dp0\relax}"
            % (HEAD % ("1 / 21", "X")))
for it in items:   # first page and continuation label (a long title may wrap)
    for c, lab in ((0, "22 / 21"), (1, "22 / 21 (cont.)")):
        meas.append(r"\setbox0=\vbox{\hsize=\textwidth%s}\typeout{MEAS %d head %d 0 \the\dimexpr\ht0+\dp0\relax}"
                    % (HEAD % (lab, it["title"]), it["page"], c))
meas.append(r"\end{frame}\end{document}")
base = os.path.splitext(dst)[0] + "_measure"
open(base + ".tex", "w", encoding="utf-8").write("\n".join(meas))
subprocess.run(["pdflatex", "-interaction=batchmode", "-halt-on-error", base + ".tex"],
               check=True, stdout=subprocess.DEVNULL)
H = {}
log = open(base + ".log", encoding="latin-1").read().replace("\n", " ")
for m in re.finditer(r"MEAS (\d+) (\w+) (\d+) (\d+) ([\d.]+)pt", log):
    H[(int(m.group(1)), m.group(2), int(m.group(3)), int(m.group(4)))] = float(m.group(5))
PT = 72.27 / 2.54
region = REGION * PT
gap = ASIDE_GAP * PT
THUMB = 2.45 * PT      # the thumbnail column (4.2 cm wide, 16:9, framed) sets a floor


def h(page, size, i, j):
    return H[(page, size, i, j)]


# ---- layout decision --------------------------------------------------------
pages = []           # dicts: item, size, i, j, cont, aside_cut (None = no asides)
report = {}
for it in items:
    p, n, has_a = it["page"], len(it["say"]), bool(it["asides"])
    def reg_of(cont):  # body + asides height left under a (possibly wrapped) header
        return REGION * PT - max(0.0, h(p, "head", int(cont), 0) - h(0, "head", 0, 0))
    region = reg_of(False)
    acost = [(c, h(p, "aside", c, 0) + gap if has_a else 0.0) for c in CUTS]
    done = False
    for size in SIZES:
        for cut, a in acost:
            if max(h(p, size, 0, n), THUMB) <= region - a:
                pages.append(dict(it=it, size=size, i=0, j=n, cont=False,
                                  cut=(cut if has_a else None)))
                report[p] = size + (" (asides cut to %d)" % cut if has_a and cut else "")
                done = True
                break
        if done:
            break
    if done:
        continue
    # split at \large: fill pages greedily; the last page also carries the asides
    size, i, first = "large", 0, True
    while i < n:
        region = reg_of(not first)
        fin = None
        for cut, a in acost:
            if max(h(p, size, i, n), THUMB) <= region - a:
                fin = cut
                break
        if fin is not None:
            pages.append(dict(it=it, size=size, i=i, j=n, cont=not first,
                              cut=(fin if has_a else None)))
            break
        j = i + 1
        while j < n - 1 and h(p, size, i, j + 1) <= region:
            j += 1
        pages.append(dict(it=it, size=size, i=i, j=j, cont=not first, cut=None))
        i, first = j, False
    report[p] = "large, %d pages" % sum(1 for q in pages if q["it"] is it)

# ---- write the document -----------------------------------------------------
out = [PREAMBLE, r"\begin{document}", r"\setlength{\textcol}{0.68\textwidth}"]
cum = 0
rows = []
for q in pages:
    it = q["it"]
    sents = it["say"][q["i"]:q["j"]]
    words = sum(plain_words(t) for t in sents)
    if not it["backup"]:
        cum += words
    sec = int(round(cum / WPM * 60))
    if it["backup"]:
        label = "Backup"
    else:
        label = "%d / %d" % (it["page"], nmain)
    if q["cont"]:
        label += " (cont.)"
    else:
        rows.append((label, it["title"], sum(plain_words(t) for t in it["say"]), cum - words))
    last = q["j"] == len(it["say"])
    out.append(r"\renewcommand{\pagefoot}{%d words \textperiodcentered{} at %d:%02d}" % (words, sec // 60, sec % 60))
    out.append(r"\begin{frame}[t]")
    out.append(r"\vspace*{-0.2cm}{\large\bfseries\color{muted}%s \textperiodcentered{} %s\par}\vspace{0.12cm}" % (label, it["title"]))
    reg = r"\dimexpr%.3fcm-%.2fpt\relax" % (REGION, max(0.0, h(it["page"], "head", int(q["cont"]), 0) - h(0, "head", 0, 0)))
    body_h = reg if q["cut"] is None else r"\dimexpr%s-%.3fcm-%.2fpt\relax" % (reg, ASIDE_GAP, h(it["page"], "aside", q["cut"], 0))
    out.append(r"\begin{columns}[T,onlytextwidth]")
    out.append(r"\column{0.68\textwidth}")
    out.append(r"\begin{minipage}[t][%s][t]{\textcol}\vspace{0pt}" % body_h)
    out.append(r"\body{%s}{%s}" % (q["size"], body_tex(sents, last)))
    out.append(r"\end{minipage}")
    out.append(r"\column{0.30\textwidth}")
    out.append(r"\vspace{0pt}\hfill{\color{thumb}\setlength{\fboxsep}{0pt}\setlength{\fboxrule}{0.4pt}"
               r"\fbox{\includegraphics[page=%d,width=4.2cm]{main.pdf}}}" % it["page"])
    out.append(r"\end{columns}")
    if q["cut"] is not None:
        out.append(r"\par\vspace{0.12cm}{\color{thumb}\rule{\textwidth}{0.4pt}}\par\vspace{0.06cm}")
        out.append(r"\asides{%s}" % aside_tex(it["asides"], q["cut"]))
    out.append(r"\end{frame}")
# summary page (after the last frame, so the pages above stay in step with main.pdf)
total = cum
half = (len(rows) + 1) // 2
def tab(rs):
    return (r"\begin{tabular}{@{}l p{4.3cm} r r@{}}\textbf{Frame}&\textbf{Title}&\textbf{Words}&\textbf{Starts}\\" + "\n"
            + "\n".join(r"%s & %s & %d & %d:%02d\\" % (l, t, w, int(round(c / WPM * 60)) // 60,
                                                        int(round(c / WPM * 60)) % 60) for l, t, w, c in rs)
            + r"\end{tabular}")
out.append(r"\renewcommand{\pagefoot}{%d spoken words, %.1f min at %d wpm}" % (total, total / WPM, WPM))
out.append(r"\begin{frame}[t]\relax{\large\bfseries\color{muted}Word count \textperiodcentered{} %d spoken words over %d main frames, %.1f min read aloud at %d words per minute\par}\vspace{0.15cm}" % (total, nmain, total / WPM, WPM))
out.append(r"{\tiny\begin{columns}[T,onlytextwidth]\column{0.5\textwidth}%s\column{0.5\textwidth}%s\end{columns}}" % (tab(rows[:half]), tab(rows[half:])))
out.append(r"\end{frame}")
out.append(r"\end{document}")
open(dst, "w", encoding="utf-8").write("%% Generated by tools/extract_notes.py from %s; do not edit by hand.\n" % src + "\n".join(out))
print("%s: %d pages (%d frames, %d main, + summary), %d spoken words, %.1f min at %d wpm"
      % (dst, len(pages) + 1, len(frames), nmain, total, total / WPM, WPM))
for p in sorted(report):
    if report[p] != "Large":
        print("  page %d: %s" % (p, report[p]))
