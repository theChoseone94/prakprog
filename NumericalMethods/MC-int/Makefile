

all: main.py plainMC.py outA.txt outB.txt

outA.txt: main.py plainMC.py 
	python3 -c 'from main import *; ProblemA()' > $@

outB.txt:
	python3 -c 'from main import *; ProblemB()' > $@

clean:
	rm *.txt
