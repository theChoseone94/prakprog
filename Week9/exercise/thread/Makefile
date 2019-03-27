CFLAGS = -Wall -std=gnu99 -pthread
LDLIBS = -lm -lpthread



main-out.txt: main Makefile
	./main > $@


main: main.c


clean:
	$(RM) main main-out.txt
