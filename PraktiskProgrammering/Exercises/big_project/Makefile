CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


default: myarctan-out.txt plot myarctan.pdf

myarctan.pdf:plot main.tex
	pdflatex main.tex
	pdflatex main.tex


myarctan-out.txt:main 
	./$< > $@

plot: plot.gpi
	gnuplot plot.gpi



clean:
	$(RM) main myarctan-out.txt Atan.pdf main.log main.aux main.pdf
