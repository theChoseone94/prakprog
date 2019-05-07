#include<stdio.h>
#include<stdlib.h>
int main(int argc, char** argv) {
	
	printf("hello åøæ\n");
	/*writing to stuff */
	fprintf(stderr,"this goes to stderr x=%g\n",x);
	fprintf(stdout,"this goes to stdout\n");
	FILE* mystream=fopen("out.mystream","w");
	fprintf(mystream,"this goes to mystream");
	fclose(mystream);

	/* reading stuff */
	scanf("%lg",&x); /*takes in user input from the keyboard */
	printf("x =%lg\n",x);	
	FILE* myinput=fopen("out.input","r");
	fscanf(myinput,"%lg\n",&x);
	printf("x from input = %g\n",x);
	fclose(myinput);
	double y = 2.2;
	if(argc>1){
		y=atof(argv[1]);
		printf("y from command line = %g\n",y);

	}


	return 0;
}
