CFLAGS = -Wall -std=gnu11
LDLIBS = -lm
CC= gcc
.PHONEY: all

all:out.txt 
	cat $^

out.txt: passfio
	./$< > $@

out.junk out.log out.mystream: input_output
	

clean:
	$(RM) main *.o out*

