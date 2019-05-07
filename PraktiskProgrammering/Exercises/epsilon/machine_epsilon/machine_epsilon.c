#include<stdio.h>
#include<limits.h>
#include<float.h>

int main(){
	float x=1;
	while(1+x!=1){x/=2;} x*=2;
	printf("Using float,while: %f\n",x);

	float k;
        for(k=1; 1+k!=1; k/=2) {} k*=2;
        printf("Using float, for-loop: %f\n", k);

	float g=1;
	do {g/=2;} while(1+g!=1); g*=2;
	printf("Using float, do-while: %f\n",g);


	printf("Table value for float: %f\n",FLT_EPSILON);


	double y=1;
	while(1+y!=1){y/=2;} y*=2;
	printf("Using double,while:%lg\n",y);

	double h;
        for(h=1; 1+h!=1; h/=2) {} h*=2;
        printf("Using double, for-loop: %lg\n",h);

	double f=1;
	do{f/=2;} while(1+f!=1); h*=2;
	printf("Using double, do-while: %lg\n",f);

	printf("Table value for double: %lg\n",DBL_EPSILON);


	long double z=1L;
	while(1+z!=1){z/=2;} z*=2;
	printf("Using long double,while:%Lg\n",z);	


	long double j;
	for(j=1; 1+j!=1; j/=2) {} j*=2;
	printf("Using long double,for-loop: %Lg\n",j);

	long double s=1L;
	do{s/=2;} while(1+s!=1); s*=2;
	printf("Using long double, do-while: %Lg\n",s);

	
	printf("Table value for double: %Lg\n",LDBL_EPSILON);

return 0;

}


