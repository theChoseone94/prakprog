#include<stdio.h>
#include<math.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>
int orbit_eq(double phi, const double y[], double yprime[], void * params){
	double epsilon = *(double*) params;
	yprime[0] = y[1]; /*set the initial condition */
	yprime[1]= 1 - y[0] + epsilon * y[0] * y[0]; /*rewrite the ODE */
return GSL_SUCCESS;
}



int main(int argc, char** argv){
	double epsilon = 0, uprime=0;


	gsl_odeiv2_system orbit;
	orbit.function = orbit_eq;
	orbit.jacobian = NULL;
	orbit.dimension = 2;
	orbit.params = (void *)&epsilon;

	double start = 1e-3, epsabs=1e-6, epsreal=1e-6;
	double phi_max =1.9* M_PI, delta_phi=0.05; /* phi_max determines how far around to integrate, delta_phi tells the step size */

	gsl_odeiv2_driver *driver =
	       	gsl_odeiv2_driver_alloc_y_new(&orbit,gsl_odeiv2_step_rk8pd,start,epsabs,epsreal);

	double t = 0, y[2] = {1,uprime};
	for(double phi = 0;phi<phi_max;phi += delta_phi) {
		int status=gsl_odeiv2_driver_apply(driver,&t,phi,y);
		printf("%g %g\n", phi,y[0]);
		if(status != GSL_SUCCESS) fprintf(stderr,"fun:status=%i",status);
		}

	gsl_odeiv2_driver_free(driver);
return EXIT_SUCCESS;

}

