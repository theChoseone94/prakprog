all: main.py Integrator.py out.txt

out.txt:
	python3 -c 'from main import *; ProblemA()' > $@
	python3 -c 'from main import *; ProblemB()' >>$@

clean:
	rm *.txt
