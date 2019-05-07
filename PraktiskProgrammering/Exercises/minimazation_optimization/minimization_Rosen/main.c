#include<stdio.h>
#include<gsl/gsl_multimin.h>
#include<gsl/gsl_vector.h>
#include<math.h>


double Rosen(const gsl_vector * v, void *params){
	double x = gsl_vector_get(v,0);
	double y = gsl_vector_get(v,1);

	return (1-x)*(1-x) + 100*(y-x*x)*(y-x*x);
}




int main(){

	const gsl_multimin_fminimizer_type * TYPE = gsl_multimin_fminimizer_nmsimplex2;
	gsl_multimin_fminimizer * SYSTEM = gsl_multimin_fminimizer_alloc(TYPE,2);

	gsl_multimin_function F;
	F.f=Rosen;
	F.n=2;
	/* initial guesses */
	gsl_vector* INIT = gsl_vector_alloc(2);
	gsl_vector_set(INIT,0,5);
	gsl_vector_set(INIT,1,5);

	gsl_vector * STEP = gsl_vector_alloc(2);
	gsl_vector_set(STEP,0,0.1);
	gsl_vector_set(STEP,1,0.1);

	gsl_multimin_fminimizer_set(SYSTEM,&F,INIT,STEP);
	

	int iter = 0, status;
	do{
		iter++;
		status = gsl_multimin_fminimizer_iterate(SYSTEM);
		if(status) 
			break;
		
		double x = gsl_vector_get(SYSTEM->x,0);
		double y = gsl_vector_get(SYSTEM->x,1);

		status = gsl_multimin_test_size(SYSTEM->size,1e-2);
		
		if(status== GSL_SUCCESS){
			printf("Converged!\n");
			break;
		}


	printf("Iteration = %i, x_min = %g, y_min = %g, f = %g \n",iter,x,y,SYSTEM->fval);
	}while(status == GSL_CONTINUE && iter < 100);

	
	double x = gsl_vector_get(SYSTEM->x,0);
	double y = gsl_vector_get(SYSTEM->x,1);

//	printf("Iteration = %i, x_min = %g, y_min = %g \n",iter,x,y);

	gsl_vector_free(INIT);
	gsl_vector_free(STEP);
	gsl_multimin_fminimizer_free(SYSTEM);



return 0;
}

