#include<stdio.h>
#include<math.h>
#include<gsl/gsl_vector.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>

int myarctan(double x,const double y[],double yprime[],void * params){	
	yprime[0]=1/(x*x+1); /* set the diff eq here: atan=1/(x*x+1 )*/
return GSL_SUCCESS;
}


int main(){
	
	gsl_odeiv2_system ARCTAN;
	
	ARCTAN.function=myarctan;
	ARCTAN.dimension=1;

	double hstart=1e-3,epsabs=1e-9,epsrel=1e-9;	

	gsl_odeiv2_driver * DRIVER=
		gsl_odeiv2_driver_alloc_y_new(&ARCTAN,gsl_odeiv2_step_rkf45,hstart,epsabs,epsrel);


	double delta_x=0.05,x_min=0,x_max=3;
	double t=0;
	double y[1]={0};
	for(double x=x_min;x<x_max;x+=delta_x){
		t=0;
		y[0]=0;
		int status = gsl_odeiv2_driver_apply(DRIVER,&t,x,y);
		printf("%g %g %g \n",x,y[0],atan(x));
		if(status != GSL_SUCCESS)
			fprintf(stderr,"function:status=%i",status);
	}



	gsl_odeiv2_driver_free(DRIVER);

return EXIT_SUCCESS;
}
