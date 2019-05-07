CFLAGS= -Wall -std=gnu99 -O
CC = gcc


sum_out.txt: sum
	./sum > $@

sum: sum.c
	$(CC) $(CFLAGS) sum.c -o sum

clean:
	$(RM) sum sum_out.txt

