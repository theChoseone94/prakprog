CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

all: out-integ.txt plot

out-integ.txt: main 
	./main > $@
main: main.c
	gcc main.c -o main $(LDLIBS)

plot: plot.gpi
	gnuplot plot.gpi

clean:
	$(RM) main out-integ.txt Energy_plot.svg
