all: partA
.PHONEY:
	all
partA: newton.py qr.py functions.py main.py out_A.txt

out_A.txt:
	python3 main.py >$@


.PHONEY:
	clean


clean:
	rm *.txt
