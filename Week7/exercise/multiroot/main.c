#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_vector.h>
#include<gsl/gsl_multiroots.h>



/* setting up a and b in f(x) = a*(1-x)^2 + b*(y-x^2)^2, where in our case, a = 1 and b = 100 */
struct rparams{
	double a;
	double b;
};


/* now for the rosenbrock function */

int rosenbrock_func(const gsl_vector * x, void * params, gsl_vector * f) {

	double a = ((struct rparams *)params)->a;
	double b = ((struct rparams *)params)->b;

	const double x0 = gsl_vector_get(x,0);
	const double x1 = gsl_vector_get(x,1);

	/*so the first part of the eq: a * (1-x0)^2 and the second part of the eq: b * (x1 - x0^2)^2.
	 * I find the gradient of this and plug it in */
	const double y0 = a*2*x0-2+b*(4*x0*x0*x0 - 4*x0*x1);
	const double y1 = b*(2*x1-2*x0*x0);
	
	gsl_vector_set(f,0,y0);
	gsl_vector_set(f,1,y1);

return GSL_SUCCESS;
}
/*print the state and iterations*/
int print_state(size_t iter, gsl_multiroot_fsolver *s){
	printf("iter = %3u x = % .3f % .3f "
			"f(x) = %.3f %.3e \n",
			iter,
			gsl_vector_get(s->x,0),
			gsl_vector_get(s->x,1),
			gsl_vector_get(s->f,0),
			gsl_vector_get(s->f,1));
}

int main(void){

	const gsl_multiroot_fsolver_type *T;
	gsl_multiroot_fsolver *s;

	int status;
	size_t i, iter=0;
	
	/*setting a and b */
	const size_t n= 2;
	struct rparams p = {1.0,100.0};
	gsl_multiroot_function f = {&rosenbrock_func,n,&p};
	
	/* setting up initial guess on the solution (1,1) */
	double x_init[2]= {0.5,0.5};
	gsl_vector *x = gsl_vector_alloc(n);

	gsl_vector_set(x,0,x_init[0]);
	gsl_vector_set(x,1,x_init[1]);

	T=gsl_multiroot_fsolver_hybrids;
	s=gsl_multiroot_fsolver_alloc(T,2);
	gsl_multiroot_fsolver_set(s,&f,x);

	print_state(iter,s);
	
	do {
		iter++;
		status = gsl_multiroot_fsolver_iterate(s);
		print_state(iter,s);

		if(status)
			break;

		status = gsl_multiroot_test_residual (s->f,1e-7);
	}
	while(status == GSL_CONTINUE && iter < 1000);
	printf("status = %s\n",gsl_strerror(status));

	gsl_multiroot_fsolver_free(s);
	gsl_vector_free(x);




return 0;
}
