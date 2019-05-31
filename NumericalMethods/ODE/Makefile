

all: main.py rungekutta.py out.txt outA2.txt

out.txt:
	python3 -c 'from main import *; ProblemA1()' > $@
outA2.txt:
	python3 -c 'from main import *; ProblemA2()' >> out.txt
clean:
	rm *.txt *.pdf
