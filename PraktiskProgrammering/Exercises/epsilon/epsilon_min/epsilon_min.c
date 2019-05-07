#include<limits.h>
#include<float.h>
#include<stdio.h>

int main(){
	int z=1;
       	while(z-1<z){z--;}
	printf("My min. using while: %i\n",z);	

	int k;
	for ( k = 1; k-1 < k; k--);
	printf("My min. using for-loop: %i\n",k);

	int h;
	do h--; while(h-1 < h);
	printf("My min. using do-while: %i\n",h);
	
	
	return 0;
}
