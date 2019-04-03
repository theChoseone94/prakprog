CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


default: myarctan-out.txt plot

myarctan-out.txt: myarctan
	./$< > $@

plot: plot.gpi
	gnuplot plot.gpi



clean:
	$(RM) myarctan myarctan-out.txt Atan.pdf
