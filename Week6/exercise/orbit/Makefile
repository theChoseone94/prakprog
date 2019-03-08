CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


.PHONEY: all

all: out.data

out.dat:in.dat main
	./main < $< > $@

in.dat: Makefile
	seq 0 0.05 3	


clean: 
	$(RM) *.o
