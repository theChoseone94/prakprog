Questions 4
1. How are arguments passed to functions in C: by-value or by-reference? And what does that mean? 

	It is passed by value. It means that if I made a function y = x^2 and I used y(x) in another file, it would get the value of y, i can't alter the original variables. 
	

2. If double x=1.23, what is *(&x)? What is NULL? Hint: null pointer. 

	I think it would give you the address of x, in the memory. 
	so &x would give the value, where *(&x) would then give the address.
	
3.What happens to variables declared inside a function when the function exits (returns)? 
	It gets deleted. 
	
4. What is a static variable?

	a variable that has been allocated on some memory. I would imagine that 
	if you use the global prefix, you would set it globally - meaning it is set. 

5. What will the following three programs print out and why? 
	
	1. i = 1, it prints the value of i, which is set by int i = 1.
	2. i = 0, it prins the value of i, which comes by the &i pointer to give 0.
	3. i = 1, does it have something to do with the NULL pointer, so it looks to int i = 1?
	
6. If you pass an array to a function with the signature void f(double a[]) – what is actually passed to the function: 

	It will pass the pointer of the first element. 
	
7. When the function with the signature void f(double a[]) gets the array as parameter – can it figure out the size of the array? 

	I think it can, but it is good practice to give it "int n" where n is the size of array. 

8. If you declare an array as int a[5]; and then try a[7]=1; what will happen? Hint: Segmentation fault / causes. 
	I think it would give segmentation error. So you are trying to access a part of the memory
	you think are in the array, but is not. So you are trying to get some wild pointer, which 
	leads to a segmentation error. 
	
9. If you declare an i) static, ii) variable-length, iii) dynamic array inside a function, can the function return it? 
	i) I think it can return it when it is static.
	ii) I think it won't because the length of the array is based on the program, so
		it will end/free the variable once the process ends. 
	iii) No I don't think it can return it. Arrays are apparently hard to return. 
	
10. What will the following C-program print? 

	It will print
	i = 0
	i = 1
	i = 2
	

	
	 
	
