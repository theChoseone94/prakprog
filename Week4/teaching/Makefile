CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = `gsl-config --libs`

all: gamma.svg out.txt
	cat out.txt

gamma.svg: gamma.gpi gamma.txt
	gnuplot $< > $@

out.txt gamma.txt:main
	./$< 1> out.txt 2> gamma.txt

main: main.o make_gamma_plot.o

main.o make_gamma_plot.o: make_gamma_plot.h

test:
	@echo $(CFLAGS)
	@echo $(LDLIBS)

.PHONEY:clean
clean:
	$(RM) *.o out* *.svg main	
