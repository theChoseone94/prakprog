#include<gsl/gsl_odeiv2.h>
#include<math.h>
#include<stdio.h>
#include<gsl/gsl_errno.h>
#include<assert.h>



int wavefunction(double r,const double y[],double f[], void * params){
	double e = *(double *)params;
	f[0] = y[1];
	f[1] = -2*(e+1/r)*y[0]; /*(1/2)f'' -(1/r)f = εf --> f'' = -2*(e + 1/r)*f */
	return GSL_SUCCESS;
}



double Fe(double e, double r){
	assert(r>=0.0);
	double hstart = 1e-3;
	double epsabs=1e-6,epsrel=1e-6;

	const double r_min=1e-2;
	if(r<r_min) return r-r*r;
	
	gsl_odeiv2_system system;
	system.function = wavefunction;
	system.jacobian = NULL;
	system.dimension = 2;
	system.params = (void*)&e;

	gsl_odeiv2_driver * DRIVE =
	       	gsl_odeiv2_driver_alloc_y_new(&system,gsl_odeiv2_step_rkf45,hstart,epsabs,epsrel);

	double t=r_min;
	double y[]={t-t*t,1-2*t}; /*r-r^2 and the derivative 1-2*r */
	int status = gsl_odeiv2_driver_apply(DRIVE,&t,r,y);
		if(status!=GSL_SUCCESS) fprintf(stderr,"odeiv2 error for Fe is %i \n",status);

	gsl_odeiv2_driver_free(DRIVE);
	
	return y[0];

}
