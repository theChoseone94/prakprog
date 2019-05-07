#include<stdio.h>
#include<math.h>
#include<stdlib.h>

int equal(double a, double b, double tau, double epsilon){
	if( fabs(a-b) < tau ) {return 1;}
	else if ( fabs(a-b)/(fabs(a)+fabs(b)) < epsilon/2 ) { return 1; }
	else return 0;
}


int main() {
	const double tau=1e-1;
	const double eps=1e-1;
	double x=1,y=1.01;
	int eq=equal(x,y,tau,eps);
	printf("eq=%i\n",eq);
	return 0;
}
