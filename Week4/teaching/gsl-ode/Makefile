CFLAGS = -Wall -std=gnu99 $$(gsl-config --cflags)
LDLIBS = $$(gsl-config --libs)

out:out.txt plot.svg
	cat $<

plot.svg:plot.data
	gnuplot -e "\
	set terminal svg background 'white';
	plot 'plot.data' using 1:2 with lines title 'myexp'\
	" >$@


out.txt: main input_matrix
	cat input_matrix | ./main 1> out.txt 2> plot.data


test:
	echo $(PATH)


clean: 
	$(RM) main out.txt
