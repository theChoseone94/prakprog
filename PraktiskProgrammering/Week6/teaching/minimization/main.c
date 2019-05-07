#include<stdio.h>
#include<stdlib.h>
#include<gsl/gsl_vector.h>
#include<math.h>
#include<gsl/gsl_multimin.h>
struct expdata {int n; double *energy, *signal, *error;};

double BW(double e, double e0, double G){
	return 1/((e-e0)*(e-e0)+G*G/4);
}
double master(const gsl_vector *x, void *params){
	double E = gsl_vector_get(x,0);
	double G = gsl_vector_get(x,1);
	double F = gsl_vector_get(x,2);
	struct expdata  data =* (struct expdata *)params;
	double chi2=0;
	for(int i=0;i<data.n;i++){
		double e=data.energy[i];
		double y=data.signal[i];
		double u=data.error[i];
		chi2+=pow(F*BW(e,E,G)-y,2)/u/u;
	}
	return chi2;
}


int main(int argc, char** argv){

	if(argc<2){
		fprintf(stderr,"usage: %s number_of_lines to read \n",argv[0]);
	}
	int n = atoi(argv[1]);
	double energy[n],signal[n],error[n];
	
	for(int i=0;i<n;i++) 
		scanf("%lg %lg %lg", energy+i,signal+i,error+i);
	for(int i=0;i<n;i++)
		printf("%g %g %g\n",*(energy+i),*(signal+i),*(error+i));

	int dim = 3;
	struct expdata data;
	data.n=n;
	data.energy=energy;
	data.signal=signal;
	data.error=error;
	gsl_multimin_function F;
	F.f=master;
	F.n=dim;
	F.params=(void*)&data;

	gsl_multimin_fminimizer *M;
	#define TYPE gsl_multimin_fminimizer_nmsimplex2
	gsl_multimin_fminimizer_alloc(TYPE,dim);
	gsl_vector* start = gsl_vector_alloc(dim);
	gsl_vector* step = gsl_vector_alloc(dim);
	
	gsl_vector_set(start,0,120);
	gsl_vector_set(start,1,2);
	gsl_vector_set(start,2,6);
	
	gsl_vector_set(step,0,1);
	gsl_vector_set(step,0,0.5);
	gsl_vector_set(step,0,0.1);



	gsl_multimin_fminimizer_set(M,&F,start,step);
	do{
      		iter++;
      		status = gsl_multimin_fminimizer_iterate(M);
		if (status) break;

      size = gsl_multimin_fminimizer_size (M);
      status = gsl_multimin_test_size (size, 1e-2);

      if (status == GSL_SUCCESS)
        {
          printf ("converged to minimum at\n");
        }

      printf ("iter =%5d, E=%g, G=%g F=%g master= %g size = %g \n",
              iter,
              gsl_vector_get (M->x, 0),
              gsl_vector_get (M->x, 1),
	      gsl_vector_get (M->x, 2);
              M->fval, size);
    }
  while (status == GSL_CONTINUE && iter < 100);


return 0;
}

