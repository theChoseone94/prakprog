CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)
PARAMETERS =  -3 3 0.01

.PHONEY: all clean

default:main-out.txt plot

plot:plot.gpi
	gnuplot plot.gpi

main-out.txt: main
	./main $(PARAMETERS) > $@

main: main.c


clean:
	$(RM) main main-out.txt Error_plot.svg
