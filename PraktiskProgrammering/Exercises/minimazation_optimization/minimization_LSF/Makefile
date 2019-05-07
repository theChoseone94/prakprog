CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: LSF-out.txt plot
LSF-out.txt:main
	./main >$@

plot: plot.gpi Makefile
	gnuplot plot.gpi

main: main.c


clean:
	$(RM) main LSF-out.txt LSF-out.svg
