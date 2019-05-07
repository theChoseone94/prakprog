#include<stdio.h>
#include<math.h>
#include<stdlib.h>
int main(int argc, char** argv){
	for(int i=1; i<argc;i++){ /*takes argument, like 5, and runs from 1 to 5 */
		double x=atof(argv[i]); /* atof convert string to double!   */
		printf("%lg \t %lg\n",x,sin(x)); /* prints the x and the sin(x) */
	}
	return 0;
}
