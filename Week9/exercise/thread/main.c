#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<pthread.h>

void* dart(int n){
	//int n=500000;  //number of darts thrown. tested that 500000 is max, core dumps for higher # of darts.
	int i;
	int R=1; 
	double DART_X[n]; //holder for x-positions for dart
	double DART_Y[n]; //holder for y-positions for dart
	for(i=0;i<n;i++){
		unsigned int k=time(NULL)*i;	//use time as a seed for the random number	
		DART_X[i]=(double)rand_r(&(k))/(double)RAND_MAX; //Create x-position
		DART_Y[i]=(double)rand_r(&(k))/(double)RAND_MAX; //Create y-position
	}		 
	double Inside=0;
	int k;
	for(k=0;k<n;k++){
	if(DART_X[k]*DART_X[k]+DART_Y[k]*DART_Y[k]<R*R) //Check if inside circle
		Inside++;
	else
		continue;
	}	
	
return &Inside;
}



int main(){
	int n=100;
	int m=100;
	pthread_t thread;
	int flag=pthread_create(
		&thread,NULL,
		dart,(void*)&n);
	dart((void*)&m);
	flag=pthread_join(thread,NULL);





	//printf("Number of points inside is: %f\n",Inside);
	//double Pi = 4*Inside/n; //Calculate pi
	//printf("Pi is approximately: %f\n",Pi);

	return 0;
}



