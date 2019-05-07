#include<limits.h>
#include<float.h>
#include<stdio.h>

int main(){
	int i=1; while(i+1>i){i++;}
	printf("my max int using while: %i\n",i);

	int x; 
	for ( x = 1; x< x+1; x++);
	printf("max int using for loop: %i\n",x);

	int y;
	do y++; while(y<y+1);
	printf("Max in using do-while: %i\n",y);
return 0;
}
