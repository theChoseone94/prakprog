#define _ISOC99_SOURCE
#include<math.h>
#include<gsl/gsl_errno.h>
#include<gsl/gsl_integration.h>

struct nx {int n; double x;};

double integrand (double t, void * params) {
  	struct nx p = *(struct nx *) params;
	int n = p.n;
	double x = p.x;
  	double f = cos(n*t - x * sin(t));
  	return f;
}

double besseljn(int n, double x){

	int limit=100;
	gsl_integration_workspace * w;
	w  = gsl_integration_workspace_alloc (limit);
	
	struct nx params = {.n=n,.x=x};
	gsl_function F;
	F.function= integrand;
	F.params = (void*)&params;

	double result,error,acc=1e-8,eps=1e-8;
       	int flag = gsl_integration_qags (&F, 0, M_PI, acc, eps, limit,
                        w, &result, &error);		

	if(flag!=GSL_SUCCESS) return NAN;
	return result/M_PI;

	gsl_integration_workspace_free(w);
}



