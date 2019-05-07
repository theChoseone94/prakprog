CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags) 
LDLIBS = $$(gsl-config --libs)
CC = gcc



matrix_solve_out.txt: matrix
	./matrix > $@

matrix: matrix.c
	$(CC) $(CFLAGS) matrix.c -o matrix $(LDLIBS)

clean: 
	$(RM) matrix matrix_solve_out.txt 
