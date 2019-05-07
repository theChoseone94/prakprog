#include<stdio.h>

int main(void){
	float x = 0.1111111111111111111111111111;
	double y =0.1111111111111111111111111111;
	long double z =0.1111111111111111111111111111L;
	printf("Float:%.25g\n",x);
	printf("Double:%.25lg\n",y);
	printf("LongDouble:%.25Lg\n",z); 
}
