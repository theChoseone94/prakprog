all: AB

AB: newton.py qr.py functions.py main.py out.txt out_B1 out_B2

out.txt:
	python3 -c 'from main import*; ProblemA()' > $@
out_B1:
	python3 -c 'from main import*; ProblemB1()' >> out.txt
out_B2:
	python3 -c 'from main import*; ProblemB2()' >> out.txt


clean:
	rm *.txt *.pdf
