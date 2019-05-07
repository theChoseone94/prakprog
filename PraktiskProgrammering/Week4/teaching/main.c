#include "make_gamma_plot.h"
#include <gsl/gsl_vector.h>
int main(){
	make_gamma_plot();
	const int n=7;
	gsl_vector* v = gsl_vector_alloc(n);
	for(int i=0;i<n;i++){
	double x=i;
	gsl_vector_set(v,i,x);
	}
	gsl_vector_fprintf(stdout,v,"%g");

	for(int i=0;i<n;i++){
	double x=gsl_vector_get(v,i);
	printf("v[%i]=%g ",i,x);
	}
	printf("\n");

	gsl_vector_free(v);
return 0;
}
