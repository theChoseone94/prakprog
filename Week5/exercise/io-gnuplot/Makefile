CFLAGS = -Wall -std=gnu99
LDLIBS = -lm
CC = gcc

.PHONEY: all

default: out.io.txt out.cmd.txt stdio-out.txt  plot

out.io.txt: main-stdio input.data.txt
	cat input.data.txt | ./main-stdio > $@

out.cmd.txt: main-cmdline input.data.txt
	./main-cmdline `cat input.data.txt` > $@


stdio-out.txt: main-stdio Makefile
	./main-stdio > $@

plot: plot.gpi
	gnuplot plot.gpi

main-stdio: main-stdio.c
	$(CC) $(CFLAGS) main-stdio.c -o main-stdio $(LDLIBS)


cmdline-out.txt: main-cmdline Makefile
	./main-cmdline >$@


main-cmdline: main-cmdline.c
	$(CC) $(CFLAGS) main-cmdline.c -o main-cmdline $(LDLIBS)



clean:
	find -type f -executable -delete
	$(RM) *.o test.cmd.out.txt test.io.out.txt plot.svg out.cmd.txt out.io.txt
