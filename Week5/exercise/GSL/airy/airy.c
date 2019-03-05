#include<gsl/gsl_sf_airy.h>
#include<gsl/gsl_sf.h>
#include<stdio.h>

int main(){
	for(double x=-15;x<5;x+=0.05){
		gsl_mode_t accura = GSL_PREC_DOUBLE;
		double A = gsl_sf_airy_Ai(x,accura);
		double B = gsl_sf_airy_Bi(x,accura);
		printf("%lg \t %lg \t %lg \n",x,A,B);
	}


	return 0;
}
