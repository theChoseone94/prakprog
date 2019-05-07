#include<stdio.h>
#include<math.h>
#include<gsl/gsl_integration.h>

double eq1 (double x, void * params){
	double f=log(x)/sqrt(x);
	return f;
}

double norm (double x, void * params){
	double alpha = *(double *)params;
	double norm=exp(-alpha * x * x);
	return norm;
}

double hamil(double x, void * params){
	double alpha = *(double *)params;
	double hamil = exp(-alpha * x * x)*(-alpha*alpha*x*x/2 + alpha/2 + x*x/2);
	return hamil;
}


int main(){
	double epsabs=1e-6,epsrel=1e-6;
	double E,alpha;


	/* Integration of part 1 */
	gsl_integration_workspace * Work = gsl_integration_workspace_alloc(100);
	double results,errors;
	gsl_function F;
	F.function=&eq1;
	F.params=0;

	gsl_integration_qags(&F,0,1,epsabs,epsrel,100,Work,&results,&errors);
	printf("The result of the integration is %lg \n",results);

	double limit=5000;

	/*integration of E = hamilton/norm */
	gsl_integration_workspace * W_N =gsl_integration_workspace_alloc(limit);
	gsl_integration_workspace * W_H =gsl_integration_workspace_alloc(limit);
	
	gsl_function Norm;
	gsl_function Hamil;

	Norm.function = &norm;
	Hamil.function = &hamil;

	Norm.params=&alpha;
	Hamil.params=&alpha;

	double result1,result2;
	double error1,error2;
	int i;
	for(i=1;i<=300;i++){
		alpha=i/100.0;
		gsl_integration_qagi(&Norm,epsabs,epsrel,limit,W_N,&result1,&error1);
		gsl_integration_qagi(&Hamil,epsabs,epsrel,limit,W_H,&result2,&error2);
		E=result2/result1;
	printf("%lg %lg \n", alpha, E);
	}
	gsl_integration_workspace_free(W_N);
	gsl_integration_workspace_free(W_H);

	return 0;

}




