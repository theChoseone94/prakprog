CFLAGS = $$(gsl-config --cflags) -std=gnu99 -Wall
LDLIBS = $$(gsl-config --libs)

rosen-out.txt: main
	./main > $@

main: main.c


clean:
	$(RM) main rosen-out.txt 
