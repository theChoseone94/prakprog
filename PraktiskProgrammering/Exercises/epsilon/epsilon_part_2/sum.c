#include<stdio.h>
#include<limits.h>
#include<float.h>


int main(){
	int max= INT_MAX/2;
	float sum_up_float=1.0f;
	for(int i=2; i<=max;i++) {sum_up_float+=(1.0f/i);}
	printf("Sum_up is given as: %f\n",sum_up_float);
	/* this sums up 1/1 + 1/2 + 1/3 + .... + 1/max) */	
	
	float sum_down_float=1.0f/max;
	for( int j=1; j<max; j++) {sum_down_float+=(1.0f/(max-j));}
	printf("Sum_down is given as: %f\n",sum_down_float);
	/* this sums the other way: 1/max + 1/(max-1) + 1/(max-2) + .... + 1/1 */

	printf("The difference must be in the precision of the float data type.\n");
	printf("So it is not as precise as one might think\n");
	printf(" and the number of digits is not as high\n");

	printf("Does the sum converge as a function of max?\n");
	printf("I tried change max to INT_MAX/3 and INT_MAX/4 and nothing changed\n");

	double sum_up_double = 1.0;
	for(int x=2; x<=max; x++) {sum_up_double+=(1.0/x);}
	printf("Sum_up_double is given as: %lg\n",sum_up_double);
	/* please note that the double needs "1.0" and not just "1". It will give a wrong answer if 1 is used */

	double sum_down_double = 1.0/max;
	for (int r=1; r<max; r++) {sum_down_double+=(1.0/(max-r));}
	printf("Sum_down_double is given as: %lg\n",sum_down_double);	

	printf("They are now the same number, which they should be.\n");
	printf("So it must the number of decimal places/precision\n");


	return 0;



}
