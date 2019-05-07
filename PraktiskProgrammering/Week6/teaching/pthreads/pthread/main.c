#include<stdio.h>
#include<stdlib.h>
#include<pthread.h>


struct harm {int a,b; double result;};

void* bar(void* param){
	struct harm* data = (struct harm*)param;
	int a = data->a;
	int b = data->b;
	double sum =0;
	for(int i=b-1;i>a;i--)sum+=1.0/i;
	data->result=sum;

}

int main(int argc, char** argv){
	int n = argc>1? (int)atof(argv[1]):1e6;
	int mid = n/2;
	struct harm data,data1,data2;
	data.a=1;
	data.b=n;
	
	data1.a=1;
	data1.b=mid;
	
	pthread_t traad;
	pthread_create(&traad,NULL,bar,(void*)&data1);
	
	data2.a=mid;
	data2.b=n;
	bar((void*)&data2);
	pthread_join(traad,NULL);
	printf("Sum from %i to %i = %g\n",1,n,data1.result+data2.result);

	bar((void*)&data);
	printf("Sum from %i to %i = %g \n",1,n,data.result);

	


	return EXIT_SUCCESS;

}
