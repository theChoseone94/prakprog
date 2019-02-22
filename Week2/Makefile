CFLAGS = -Wall -std=gnu99 -O1 
LDLIBS = -lm  
CC = gcc

.PHONEY: test
test: 
	@echo 'CFLAGS=' $(CFLAGS)


.PHONEY: clean
clean: 
	$(RM) *.o out*
	find -type f -executable -delete

