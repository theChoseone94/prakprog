#include<math.h>
#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_odeiv2.h>
#include<gsl/gsl_errno.h>

int diff_error(double x, const double y[],double yprime[], void * params)
	{
	yprime[0]=2.0/(sqrt(M_PI))*exp(-x*x);
	return GSL_SUCCESS;
	}
/* The error function */


double int_error(double x){
	/* setting up the system to solve the error function */
	gsl_odeiv2_system ERROR;
	ERROR.function =diff_error;
	ERROR.jacobian = NULL;
	ERROR.dimension = 1;
	ERROR.params = NULL;

	double start =copysign(0.01,x),epsabs=1e-6,epsrel=1e-6;

	gsl_odeiv2_driver *DRIVER = 
		gsl_odeiv2_driver_alloc_y_new(&ERROR,gsl_odeiv2_step_rkf45,start,epsabs,epsrel);
	
	/* initial conditions */
	double t=0.0;
	double y[]={0.0};	
	gsl_odeiv2_driver_apply(DRIVER,&t,x,y);

	gsl_odeiv2_driver_free(DRIVER);

return y[0];
}


int main(int argc, char const *argv[]){
	double a=atof(argv[1]); 
	double b=atof(argv[2]);
	double dx=atof(argv[3]);
 	/*take in a, b and dx and integrate from a to b in steps of dx */
	for(double x=a;x<b;x+=dx)
	{
	printf("%g %g\n",x,int_error(x));
	}

return 0;
}






