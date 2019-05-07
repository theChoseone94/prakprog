

CFLAGS = -Wall -std=gnu99 -O1 
LDLIBS = -lm
CC = gcc

epsilon-out.txt: epsilon-out.txt
		cat epsilon-out.txt

epsilon-out.txt: epsilon
	./epsilon > $@

epsilon: epsilon.c
	$(CC) $(CFLAGS) epsilon.c -o epsilon
	



clean:
	$(RM) *.o epsilon-out.txt
	find -type f -executable -delete


