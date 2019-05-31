all: partAB
.PHONEY:
	all
partAB: newton.py qr.py functions.py main.py out.txt

out.txt:
	python3 main.py >$@


.PHONEY:
	clean


clean:
	rm *.txt
