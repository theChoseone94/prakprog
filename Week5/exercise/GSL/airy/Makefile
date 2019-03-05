CFLAGS = -Wall -std=gnu99
LDLIBS = -L/usr/lib/x86_64-linux-gnu -lgsl -lgslcblas -lm


all: airy-out.txt airy_plot.svg

airy-out.txt:airy
	./airy > $@

airy: airy.c


airy_plot.svg: airy_plot.gpi
	gnuplot airy_plot.gpi


clean:
	find -type f -executable -delete
	$(RM) airy-out.txt airy_plot.svg
