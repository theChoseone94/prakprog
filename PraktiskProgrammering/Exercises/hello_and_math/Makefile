default: out-hello.txt out-echo.txt out-math.txt

out-hello.txt: hello
	./hello > out-hello.txt

out-echo.txt: Makefile
	echo 'hello' > $@ # this points to the target out-echo.txt

hello: hello.o
	gcc hello.o -o hello

hello.o:hello.c
	gcc -c hello.c -o hello.o

clean:
	rm -f out*.txt *.o hello

out-math.txt: math
	./math > $@
