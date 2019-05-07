#include"komplex.h"
#include"stdio.h"
#define TINY 1e-6

int main(){
	komplex a={1,2}, b = {3,4};

	printf("testing komplex_add ... \n");
	komplex r = komplex_add(a,b);
	komplex R = {4,6};
	komplex_print("a=",a);
	komplex_print("b=",b);
	komplex_print("a+b should = ", R);
	komplex_print("a+b actually = ", r);


	/*New test for komplex_new and komplex set*/
	
	double x = 1;
	double y = 2;

	komplex h = komplex_new(x,y);
	komplex_print("testing, h should be 1+2i",h);
	

	komplex_set(&h,x,y);
	komplex_print("h should be 1+2i, and it is:",h);

	


	/*new test for komplex_subtract*/

	komplex p = komplex_sub(b,a);
	komplex_print("p should be 2+2i, and is", p);
}
