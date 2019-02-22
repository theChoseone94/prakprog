#include "nvector.h"
#include<stdio.h>
#include<stdlib.h>
#define RND (double)rand()/RAND_MAX

int main()
{
	int n = 5;
	/*allocate memory for vectors */

	nvector* a=nvector_alloc(n);
	nvector* b=nvector_alloc(n);


	/*generate random vectors */

	double x=RND;
	double y=RND;
	float sum=0;	
	for(int i=0;i<n;i++){
	nvector_set(a,i,x);
	nvector_set(b,i,y);
	sum+=x*y;
	}
	/*testing nvector dot product */
	double z = nvector_dot_product(a,b);
	printf("Z is:%f\n",z);
	printf("Z is supposed to be: %f\n",sum);



}
