CFLAGS = -Wall -std=c11 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

blah:out.txt
	cat $<

out.txt:main;./$< > $@

main: main.o root.o

