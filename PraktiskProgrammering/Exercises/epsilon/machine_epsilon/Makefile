CFLAGS= -Wall -std=gnu99 -O
LDLIBS = -lm
CC = gcc
machine-epsilon-out.txt: machine-epsilon
	./machine-epsilon.o > $@

machine-epsilon: machine_epsilon.c
	$(CC) $(CFLAGS) machine_epsilon.c -o machine-epsilon.o

clean:
	$(RM) *.o machine-epsilon-out.txt
	find -type f -executable -delete


