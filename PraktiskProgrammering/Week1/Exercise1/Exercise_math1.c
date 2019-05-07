#include<stdio.h>
#include<math.h>
#include<complex.h>
# define M_PI 3.1415926535897932384 /* pi */
int main(void){
	
	printf("Tgamma(5)=%f\n", tgamma(5)); // Gamma function of 5
	
	printf("Bessel(0.5)=%f\n",j1(0.5)); //Bessel functino of 0.5
	
	double complex z1 = csqrt(-2.0); // sets the complex number sqrt(-2) as z1
    	printf("Sqrt(-2) = %.1f%+.1fi\n", creal(z1), cimag(z1)); //prints the real and imaginary part
	
	double complex z2 = cpow(M_E,I);
	printf("e^I = %.1f%+.1fi\n",creal(z2),cimag(z2));
	
	double complex z3 = cpow(M_E,I*M_PI);
	printf("e^(i*pi) = %.1f%+.1fi\n",creal(z3),cimag(z3));
	
	double complex z4 = cpow(I,M_E);
	printf("i^e = %.1f%.1fi\n",creal(z4),cimag(z4));
}
