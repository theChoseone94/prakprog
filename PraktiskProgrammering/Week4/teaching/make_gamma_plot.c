#include<gsl/gsl_sf.h>
#include"make_gamma_plot.h"
#include<math.h>
void make_gamma_plot(void){
	for(double x = -2*M_PI; x<2*M_PI;x+=0.1){
		double g= gsl_sf_gamma(x);
		double t=tgamma(x);
		fprintf(stderr,"%g %g %g\n",x,g,t);
	}
}
