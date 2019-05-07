CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

default: orbit_out.txt main plot
orbit_out.txt: main Makefile
	./main --epsilon 0.02 --uprime -0.8 > $@

plot: plot.gpi Makefile
	gnuplot plot.gpi

clean: 
	$(RM) orbit_out.txt *.o main orbit.svg
