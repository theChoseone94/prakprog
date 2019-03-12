#include<stdio.h>
#include<gsl/gsl_odeiv2.h>
#include<math.h>
#include<gsl/gsl_matrix.h>


/** so i will setup the function for ode to integrate, the orbit function from the assignment **/

int GR(double t, const double y[], double f[], void * params){
	double eps = *(double*)params;
	/* the functions */ 
	f[0]=y[1];
	f[1]=1-y[0]+eps*y[0]*y[0];

	return GSL_SUCCESS;
}


/* Now set the jacobian of the orbit/system */
int jacob(double t, const double y[], double *dfdy, double dfdt[], void * params){
	double eps = *(double*)params;

	/* setting up the jacobian matrix in size 2 x 2 */
	gsl_matrix_view dfdy_m = gsl_matrix_view_array(dfdy,2,2);
	
	gsl_matrix * m = &dfdy_m.matrix;
	
	/* setting up the 2 x 2 matrix with inputs. (0, 1      )
	 *					    (-1+2*y[0],0)	 */ 
	gsl_matrix_set(m,0,0,0.0);
	gsl_matrix_set(m,1,0,-1+2*y[0]);
	gsl_matrix_set(m,0,1,1);
	gsl_matrix_set(m,1,1,0);
 /*the time derivative of the function is set here */
	dfdt[0]=0.0;
	dfdt[1]=0.0;

return GSL_SUCCESS;
}





/*now for the main calculation and the three cases that are asked in the assignment */
int main() {
/* setting up the driver for the integration*/
	double eps, epsabs=1e-6,epsrel=1e-6;
	gsl_odeiv2_system sys = {GR,jacob,2,&eps};
	gsl_odeiv2_driver * drive = gsl_odeiv2_driver_alloc_y_new(&sys, gsl_odeiv2_step_rk8pd,epsabs,epsrel,0.0);
/* setting up the constants which go into the integration. epsi and y1 is for the 3 cases in the assignment */
	int i;
	int j;
	double t,t1=20*M_PI;
	double y[2],epsi[3]={0.0,0.0,0.01},y1[3]={0.0,-0.5,-0.5};
	
	for(j=1;j<=3;j++){
	t=0.0;
	y[0]=1.0;
	y[1]=y1[j-1];
	eps=epsi[j-1];
	
	for(i=1;i<=300.0;i++){
		double ti = i*t1/300.0;
		int status = gsl_odeiv2_driver_apply(drive,&t,ti,y);
		if(status != GSL_SUCCESS){
			printf("ERROR!! Return value is %d\n",status);
			break;
		}
		
		printf("%lg %lg %lg \n", t,y[0],y[1]);

	}
	printf("\n\n");
	}
	gsl_odeiv2_driver_free(drive);
return 0;
}






