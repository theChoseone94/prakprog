#include<math.h>
#include<gsl/gsl_vector.h>
#include<stdio.h>
#include<gsl/gsl_multimin.h>

struct experimental_data{int n; double *t,*y,*e;};


double MASTER(const gsl_vector *x,void * params){
	double A = gsl_vector_get(x,0);
	double T = gsl_vector_get(x,1);
	double B = gsl_vector_get(x,2);

	struct experimental_data * p =(struct experimental_data*) params;

	int n = p->n;
	double *t = p->t;
	double *y = p->y;
	double *e = p->e;

	double sum=0;
	#define f(t) A*exp(-(t)/T) + B
	for(int i=0;i<n;i++){
	sum+=pow((f(t[i]) - y[i])/e[i],2);
	}
	return sum;
}


int main(){

	double t[]= {0.47,1.41,2.36,3.30,4.24,5.18,6.13,7.07,8.01,8.95};
	double y[]= {5.49,4.08,3.54,2.61,2.09,1.91,1.55,1.47,1.45,1.25};
	double e[]= {0.26,0.12,0.27,0.10,0.15,0.11,0.13,0.07,0.15,0.09};
	int n = sizeof(t)/sizeof(t[0]);

	struct experimental_data p;
	p.n=n;
	p.t=t;
	p.y=y;
	p.e=e;


	const gsl_multimin_fminimizer_type * TYPE = gsl_multimin_fminimizer_nmsimplex2;
	gsl_multimin_fminimizer * SYSTEM = gsl_multimin_fminimizer_alloc(TYPE,3);

	gsl_multimin_function F;
	F.f=MASTER;
	F.n=3;
	F.params=(struct experimental_data*)&p;



	/*Initial guesses, all 1 since I have no idea */
	gsl_vector* INIT = gsl_vector_alloc(3);
	
	gsl_vector_set(INIT,0,1);
	gsl_vector_set(INIT,1,1);
	gsl_vector_set(INIT,2,1);

	/*set the step size */
	gsl_vector * STEP=gsl_vector_alloc(3);
	gsl_vector_set(STEP,0,0.1);
	gsl_vector_set(STEP,1,0.1);
	gsl_vector_set(STEP,2,0.1);

	int iter=0,status;

	gsl_multimin_fminimizer_set(SYSTEM,&F,INIT,STEP);

	do{
		iter++;
		status=gsl_multimin_fminimizer_iterate(SYSTEM);
		if(status){
			fprintf(stderr,"Iteration did not go well. Error in %i\n",status);
			break;
		}
		status = gsl_multimin_test_size(SYSTEM->size,1e-3);
		if(status==GSL_SUCCESS){
			fprintf(stderr,"Fitting completed\n");
		}
		}while(status==GSL_CONTINUE && iter<100);

	double A_fit=gsl_vector_get(SYSTEM->x,0);
	double T_fit=gsl_vector_get(SYSTEM->x,1);
	double B_fit=gsl_vector_get(SYSTEM->x,2);
	
	int j;
	for(j=0;j<n;j++){
		printf("%g %g %g\n",t[j],y[j],e[j]);
	}
	printf("\n\n");	
	#define f_fit(t) A_fit*exp(-(t)/T_fit) + B_fit
	double t_fit;
	int k;
	for(k=0;k<100;k++){
		t_fit=k/10.0;
		printf("%g %g\n",t_fit,f_fit(t_fit));
	}




	gsl_vector_free(INIT);
	gsl_vector_free(STEP);
	gsl_multimin_fminimizer_free(SYSTEM);

return 0;
}




