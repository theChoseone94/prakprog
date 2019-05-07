CFLAGS = -Wall -std=gnu1x $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all:out_GR_orbit.txt plot

out_GR_orbit.txt: main
	./main >$@

plot: plot.gpi Makefile
	gnuplot plot.gpi

clean:
	$(RM) out_GR_orbit.txt *.o main
