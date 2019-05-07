CFLAGS = -Wall -std=gnu1x $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

.PHONEY: all clean

all: hydrogen-out.txt plot

plot: plot.gpi hydrogen-out.txt
	gnuplot plot.gpi

hydrogen-out.txt: main 
	./main > $@

main: main.c Fe.c


clean:
	$(RM) main hydrogen-out.txt *.svg
