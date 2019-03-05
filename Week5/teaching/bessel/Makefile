CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

plot.svg: data Makefile
	gnuplot -e "\
	set terminal svg background 'white';\
	plot \
	 '$<' using 1:2 with lines title 'J_0'\
	 ,'$<' using 1:3 with lines title 'J_1'\
	 ,'$<' using 1:4 with lines title 'J_2'\
	 ,'$<' using 1:5 with lines title 'J_3'\
	" > $@

data:main
	./$< > $@

main: main.o bessel.o


