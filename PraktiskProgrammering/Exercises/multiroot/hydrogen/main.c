#include<stdio.h>
#include<math.h>
#include<gsl/gsl_multiroots.h>
#include<gsl/gsl_vector.h>

/*The function Fe from Fe.c which also contains the wavefunction */
double Fe(double e, double r);

/*The auxiliary function */
int auxi(const gsl_vector *x, void *params, gsl_vector *f){
	double e = gsl_vector_get(x,0);	
	double r_max=*(double*)params;
	double fval=Fe(e,r_max);
	gsl_vector_set(f,0,fval);

return GSL_SUCCESS;
}


int main(){
	double r_max = 8;

	/* setting the solver for the auxiliary function*/
	gsl_multiroot_fsolver * SOLVE = gsl_multiroot_fsolver_alloc(gsl_multiroot_fsolver_hybrid,1);

	gsl_multiroot_function Func;
	Func.f=auxi;
	Func.n=1;
	Func.params=&r_max;

	gsl_vector *initial=gsl_vector_alloc(1);
	gsl_vector_set(initial,0,-5);
	gsl_multiroot_fsolver_set(SOLVE,&Func,initial);

	int status;
	int iter=0;

	do{
		iter++;
		status=gsl_multiroot_fsolver_iterate(SOLVE);
		if(status){
			fprintf(stderr,"ERROR! BREAKING MULTIROOT");
			break;
		}
		fprintf(stderr,"Iteration: %i\n",iter);
		status = gsl_multiroot_test_residual(SOLVE->f,1e-3);
		if(status == GSL_SUCCESS)
			fprintf(stderr,"Converged!\n");
	}
	while(status==GSL_CONTINUE && iter<200);

	double e = gsl_vector_get(SOLVE->x,0);
	printf("%g %g \n \n \n",r_max,e);

	for(double r=0;r<=r_max;r+=r_max/64){
	printf("%lg %lg %lg\n",r,Fe(e,r),r*exp(-r));
	}


	gsl_multiroot_fsolver_free(SOLVE);
	gsl_vector_free(initial);


return 0;
}



