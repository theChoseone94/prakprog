CFLAGS: -Wall 

all: out.txt out.2.txt
	cat out.2.txt

out.2.txt:main
	./main > $@


out.txt: in.txt Makefile
	cpp  in.txt > out.txt
