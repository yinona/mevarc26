.PHONY: all slides notes speaker clean

all: slides notes speaker

slides:
	latexmk -pdf main.tex

notes:
	latexmk -pdf main-notes.tex

# Speaker deck: extracted from the \note{...} of main.tex (no duplicated text);
# it shows thumbnails of main.pdf, so the slides are built first.
speaker: slides
	python3 tools/extract_notes.py main.tex speaker_text.tex
	pdflatex -interaction=nonstopmode -halt-on-error speaker_text.tex > /dev/null
	pdflatex -interaction=nonstopmode -halt-on-error speaker_text.tex > /dev/null

clean:
	latexmk -C main.tex
	latexmk -C main-notes.tex
	rm -f speaker_text.tex speaker_text.aux speaker_text.log speaker_text.nav speaker_text.out speaker_text.snm speaker_text.toc
	rm -f speaker_text_measure.*
