CFLAGS = -Wall -std=gnu99 -O 
LDLIBS = -lm
CC = gcc

epsilon-min-out.txt: epsilon-min-out.txt
		cat epsilon-min-out.txt

epsilon-min-out.txt: epsilon_min
	./epsilon_min > $@

epsilon_min: epsilon_min.c
	$(CC) $(CFLAGS) epsilon_min.c -o epsilon_min
	



clean:
	$(RM) *.o epsilon-min-out.txt
	find -type f -executable -delete


