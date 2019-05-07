CFLAGS = -Wall -std=gnu99 -pthread -fopenmp -lgomp
LDLIBS = -lm -lpthread 


default:pthread-out.txt openmp-out.txt

openmp-out.txt: open Makefile
	./open > $@

open:open.c

pthread-out.txt: main Makefile
	./main > $@


main: main.c


clean:
	$(RM) open main main-out.txt openmp-out.txt
