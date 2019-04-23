all:partA

partA:linear_eq.py main.py out_A.txt out_B.txt

out_A.txt:
	python3 -c 'from main import *; TASKA1()' >$@
	python3 -c 'from main import *; TASKA2()' >>$@


out_B.txt:
	python3 -c 'from main import *; TASKB1()' >$@


clean:
	rm *.txt
