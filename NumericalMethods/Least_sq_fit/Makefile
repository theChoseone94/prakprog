all: partA partB

partA: linear_eq.py main.py out_A.txt 
partB: linear_eq.py main.py out_B.txt

out_A.txt:
	python3 -c 'from main import *; ProblemA()' >$@

out_B.txt:
	python3 -c 'from main import *; ProblemB()' >$@

clean:
	rm *.txt *.pdf
