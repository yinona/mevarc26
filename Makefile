.PHONY: all slides notes clean

all: slides notes

slides:
	latexmk -pdf main.tex

notes:
	latexmk -pdf main-notes.tex

clean:
	latexmk -C main.tex
	latexmk -C main-notes.tex

