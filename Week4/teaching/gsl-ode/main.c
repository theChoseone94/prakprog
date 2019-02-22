#include<gsl/gsl_matrix.h>
#include<gsl/gsl_vector.h>
#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<math.h>


int main(){
	int size1,size2;
	scanf("%i",&size1);
	scanf("%i",&size2);
	printf("Size1 is %i\n",size1);
	printf("Size2 is %i\n",size2);
	gsl_matrix* A=gsl_matrix_alloc(size1,size2);
	gsl_matrix* B=gsl_matrix_alloc(size1,size2);
	gsl_matrix_fscanf(stdin,A);
	gsl_matrix_fscanf(stdin,A);
	gsl_matrix_free(A);
	

	gsl_vector *b = gsl_vector_alloc (size2);
	gsl_vector_fscanf(stdin,b);
	
	gsl_vector *x = gsl_vector_alloc (size2);
	gsl_matrix_memcpy(B,A);
	gsl_linalg_HH_solve(A,b,x);


	gsl_vector_free(b);
	gsl_vector_free(x);


	gsl_blas_dgemv(CblasNoTrans,1,A,x,0,b);
	vector_print("Ax=b",b);

	for(double x=0;x<10;x+=0.2)
		fprintf
	
	return 0;
}


void vector_print(const char* s, gsl_vector* v){
	printf("%s",s);

	printf("%s\n",s);
	for( int i=0;i<A ->size1;i++){
		printf("%8.3g ",gsl_vector_get(v,i));
	}

}



void matrix_printf(const char* s, gsl_matrix* A){
	printf("%s\n",s);
	for( int i=0;i<A ->size1;i++){
		for(int j=0;j<A->size2;j++){
			printf("%8.3g ", gsl_matrix_get(A,i,j));
			printf("\n");
		}
	}


}
