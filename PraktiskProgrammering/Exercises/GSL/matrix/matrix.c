#include<stdio.h>
#include<gsl/gsl_linalg.h>
#include<gsl/gsl_blas.h>




int main(void)
{

double A_data[]= {6.13, -2.90, 5.86, /* I have that A*x = b. I set the matrix A here. This syntax is very						 nice to represent a matrix */
		8.08,-6.31,-3.89,
		-4.36, 1.00, 0.19};

double b_data[]={6.23,5.37,2.29}; /*This is the vector b, the result of A*x */ 

gsl_matrix_view A = gsl_matrix_view_array(A_data,3,3); /* This set A as a 3 x 3 matrix with the data from A_data  */ 

gsl_vector_view b = gsl_vector_view_array(b_data,3); /* set the vector b as a 1 x 3 vector */

gsl_vector *x = gsl_vector_alloc(3); /* allocates a vector x of size 3*/

int g;

gsl_permutation * p = gsl_permutation_alloc(3); /* a vector for decomposition of the matrix of size 3 */

gsl_linalg_LU_decomp (&A.matrix, p,&g); /*decomposes the matrix before solving A*x=b */

gsl_linalg_LU_solve (&A.matrix,p,&b.vector,x); /*solves A * x = b*/

printf("x = \n");
gsl_vector_fprintf(stdout,x,"%g"); /*prints out x */

/* to check whether x is really a solution to A*x = b, I create a new vector, check, that is the answer 
 * to A*x. So is Check != b then everything is alright */


double A_test_data[] = {	6.13, -2.90, 5.86,
			8.08, -6.31,-3.89,
			-4.36,  1.00, 0.19};
gsl_matrix_view A_test = gsl_matrix_view_array(A_test_data, 3, 3);


double check[] = {0.00,0.00,0.00}; /** make a new vector, which is the result of A*x_found **/
gsl_vector_view C = gsl_vector_view_array(check,3);
gsl_blas_dgemv(CblasNoTrans,1.0,&A_test.matrix,x,0.0,&C.vector);
/** calculate A*x. CblasNoTrans uses the ordinary A and not transposed A in the calculation. 1.0 is alpha in alpha * A *x and 0.0 is the beta in: alpha * A + beta * y. 
**/ 
printf("A*x is = \n %lg \n %lg \n %lg \n",check[0],check[1],check[2]);
printf("b is = (6.23,5.37,2.29)\n");




gsl_permutation_free(p); /*free the two allocated vectors */
gsl_vector_free(x);
	 return 0;
}
