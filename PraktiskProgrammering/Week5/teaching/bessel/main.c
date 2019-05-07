#include<stdio.h>
#include<math.h>
double besseljn(int n, double x);

int main(){
	for(double x=0;x<20;x+=0.1){
		double y0=besseljn(0,x);
		double y1=besseljn(1,x);
		double y2=besseljn(2,x);
		double y3=besseljn(3,x);
		printf("%g %g %g %g %g %g %g \n",x,y0,y1,y2,y3,j0(x));
	}
	return 0;
}
