#include<stdio.h>
#include<stdlib.h>
void set2(double *x){
	(*x)=2;
}
int main(){
	int n=5;
	double x=1;
	set2(&x);
	printf("x=%g\n",x);

	/* array */ 
	double v[n];
	for( int i=0; i<n;i++)v[i];		
	for( int i=0; i<n;i++)printf("v[%i]= %g\n",i,*(v+i));
	
	const int nn=100000;
	double* ann=malloc(nn*sizeof(double));
	ann[400]=99;
	printf("ann[400] = %g\n",ann[400]);
	free(ann);	



	return 0;
}
