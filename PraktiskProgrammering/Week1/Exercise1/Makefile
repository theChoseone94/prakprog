default: math-out.txt 

math-out.txt: Makefile math
	./math > $@
	./math2 >> $@

math: math.o
	gcc math.o -o math

math.o: Exercise_math1.c
	gcc -c Exercise_math1.c -o math.o

math2: math2.o
	gcc math2.o -o math2

math2.o: Exercise_math2.c
	gcc -c Exercise_math2.c -o math1.o

clean:
	rm -f math-out.txt math.o math2.o


