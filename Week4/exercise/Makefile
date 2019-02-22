CFLAGS = -Wall -std=gnu99
LDLIBS = -lm
CC = gcc

all:nvector_out.txt
	cat nvector_out.txt
	
nvector_out.txt: main
	./main > nvector_out.txt

main: main.o nvector.o

main.o nvector.o: nvector.h

clean:
	$(RM) out.txt main.o nvector.o


