#include<stdio.h>
#include<stdlib.h>
#include<time.h>

struct harm {int a,b;double result;};

void* dart(void* param){
	struct harm* data = (struct harm*)param;
	int a=data->a;
	int b=data->b;
	int R=1;		
	double Inside=0;

	for(int i=a;i<b;i++){
		unsigned int k=time(NULL)*i;	//use time as a seed for the random number	
		double DART_X=(double)rand_r(&(k))/(double)RAND_MAX; //Create x-position
		double DART_Y=(double)rand_r(&(k))/(double)RAND_MAX; //Create y-position
	
		if(DART_X*DART_X+DART_Y*DART_Y<R*R) //Check if inside circle
			Inside++;
		else
 			continue;
		}	 
	data->result=Inside;	
return 0;
}



int main(int argc, char** argv){
	int n = argc>1 ? (int)atof(argv[1]):1e6; /*NUMBER OF DARTS! CHANGE HERE */
	int mid = n/2;
	
	struct harm part1,part2;

	part1.a=0;
	part1.b=mid;

	part2.a=mid;
	part2.b=n;



#pragma omp parallel sections
   {
   #pragma omp section  // first thread will run this block of code
      {  
	dart((void*)&part1);
      }  
   #pragma omp section  // second thread will run this block of code
      {  
	dart((void*)&part2);
      }  
   }

	double pi=4*((double)part1.result+(double)part2.result)/n;
	printf("Pi using OpenMD is approximately = %g \n",pi);

return 0;
}
