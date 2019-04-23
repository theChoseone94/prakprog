all:partA

partA:linear_eq.py main.py out_A.txt

out_A.txt:
	python3 -c 'from main import *; TASK1()' >$@
	python3 -c 'from main import *; TASK2()' >>$@



clean:
	rm *.txt
