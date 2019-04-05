#include<stdio.h>
#include<math.h>
#include<gsl/gsl_vector.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>

int arctan_eq(double x,const double y[],double yprime[],void * params){	
	yprime[0]=1/(x*x+1); /* set the diff eq here: atan=1/(x*x+1 )*/
return GSL_SUCCESS;
}



double myarctan(double x){

	
	gsl_odeiv2_system ARCTAN;
	
	ARCTAN.function=arctan_eq;
	ARCTAN.dimension=1;

	double hstart=1e-3,epsabs=1e-9,epsrel=1e-9;	

	gsl_odeiv2_driver * DRIVER=
		gsl_odeiv2_driver_alloc_y_new(&ARCTAN,gsl_odeiv2_step_rkf45,hstart,epsabs,epsrel);

	double t=0;
	double y[1]={0};
	t=0;
	y[0]=0;
	double status = gsl_odeiv2_driver_apply(DRIVER,&t,x,y);
	if(status != GSL_SUCCESS)
		fprintf(stderr,"function:status=%g",status);

	gsl_odeiv2_driver_free(DRIVER);
return y[0];
}


int main(){
	
	for(double x=0;x<3;x+=0.1)
		printf("%g %g %g\n",x,myarctan(x),atan(x));

return 0;
}
