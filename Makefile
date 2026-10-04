.PHONY: all slides notes speaker clean

all: slides notes speaker

slides:
	latexmk -pdf main.tex

notes:
	latexmk -pdf main-notes.tex

# Speaker text: extracted from the \note{...} of main.tex (no duplicated text).
speaker: speaker_text.pdf

speaker_text.pdf: main.tex tools/extract_notes.py
	python3 tools/extract_notes.py main.tex speaker_text.tex
	pdflatex -interaction=nonstopmode -halt-on-error speaker_text.tex > /dev/null
	pdflatex -interaction=nonstopmode -halt-on-error speaker_text.tex > /dev/null

clean:
	latexmk -C main.tex
	latexmk -C main-notes.tex
	rm -f speaker_text.tex speaker_text.aux speaker_text.log
