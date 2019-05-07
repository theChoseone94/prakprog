#include<stdio.h>
#ifndef NDEBUG
#define TRACE(arg...) fprintf(stderr,arg) /*... means any number of arguments */
#else
#define TRACE(arg...)
#endif

/*instead of printf, you set in TRACE for the printf you use to debug. They can then be turned on or off so you don't need to delete them afterwards */

int main() {
	/* it would be good to printf something like" main started" at the start and "main ended" at the bottom. To DEBUG */
	const int n=5;
	double v[n];
	int i = 1000;
	printf("hello\n");
	double y=3;
	printf("good bye, y=%g\n",y);
	printf("v[%i]=%g\n",i,v[i]);
return 0;
}

