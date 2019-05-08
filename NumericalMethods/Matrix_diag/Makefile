all:A B

A: main.py out_A.txt diagon.py 

B: main.py diagon.py out_B.txt

out_A.txt:
	python3 -c 'from main import *; problemA()' >$@

out_B.txt:
	python3 -c 'from main import*;problemB()'>$@

clean: 
	rm *.txt
              
