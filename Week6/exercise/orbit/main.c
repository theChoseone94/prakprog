#include<stdio.h>
#include<math.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_odeiv2.h>

int orbit_eq(double phi, const double y[] double yprime, void * params){
	double epsilon = *(double*) params;
	yprime[0] = y[1]; /*set the initial condition */
	yprime[1]= 1- y[0} + epsilon * y[0] * y[0] /*rewrite the ODE */
return GSL_SUCCESS;
}



int main(){
	




return 0;

}

