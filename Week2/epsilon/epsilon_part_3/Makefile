CFLAGS= -Wall -std=gnu99 -O
CC = gcc

part_3_out.txt: part_3
	./part_3 > $@

part_3: part_3.c
	$(CC) $(CFLAGS) part_3.c -o part_3

clean:
	$(RM) part_3 part_3_out.txt
