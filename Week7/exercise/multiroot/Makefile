CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)


multiroot-out.txt:main
	./main > $@

main: main.c
	gcc main.c -o main $(LDLIBS)

clean:
	$(RM) main multiroot-out.txt
