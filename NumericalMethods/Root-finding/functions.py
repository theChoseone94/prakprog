import sympy as sy
import numpy as np
import math



def system_eq(x):
    z=np.empty(len(x))
    A=10000
    eq1=A*x[0]*x[1]-1.0
    eq2=np.exp(-x[0])+np.exp(-x[1]) - 1.0 - 1.0/A 
    z[0]=eq1
    z[1]=eq2
    return z
    
def Rosenbrock(x):
    z=np.empty(len(x))
    rosen1= 2*(x[0] - 1) + 400*(x[0]*x[0] - x[1])*x[0] #x-gradient
    rosen2=200*(x[1]-x[0]*x[0]) #y gradient
    z[0]=rosen1
    z[1]=rosen2
    
    return z
    
def Himmelblau(x):
    z=np.empty(len(x))
    himmel1=4*(x[0]*x[0] + x[1] - 11)*x[0] + 2*(x[0] + x[1]*x[1] -7) #x-gradient
    himmel2=2*(x[0]*x[0] + x[1] - 11) + 4*(x[0] + x[1]*x[1] -7)*x[1] - 22 #y-gradient
    z[0]=himmel1
    z[1]=himmel2
    
    return z



def system_eq_Jacob(x,J):
    z_J=np.empty(len(x))
    A=10000
    eq1_J=A*x[0]*x[1]-1.0 #x-gradient
    eq2_J=np.exp(-x[0])+np.exp(-x[1])-1.0-1.0/A #y-gradient
    z_J[0]=eq1_J
    z_J[1]=eq2_J
    
    #gradients 
    J[0,0]=A*x[1]
    J[1,1]=-np.exp(-x[1])
    J[1,0]=-np.exp(-x[0])
    J[0,1]=A*x[0]
    return z_J
    
    
    
    
def Rosenbrock_Jacob(x,J):
    z_Rj=np.empty(len(x))
    rosen1_Rj= 2.0*(x[0] - 1.0) + 400.0*(x[0]*x[0] - x[1])*x[0] #x-gradient
    rosen2_Rj=200.0*(x[1]-x[0]*x[0]) #y gradient
    z_Rj[0]=rosen1_Rj
    z_Rj[1]=rosen2_Rj
    
    J[0,0]=2.0*(600.0*x[0]*x[0]-200.0*x[1]+1)
    J[1,1]=200.0
    J[0,1]=-400.0*x[0]
    J[1,0]=-400.0*x[0]
    return z_Rj
    
    
def Himmelblau_Jacob(x,J):
    z=np.empty(len(x))
    himmel1=4*(x[0]*x[0] + x[1] - 11)*x[0] + 2*(x[0] + x[1]*x[1] -7) #x-gradient
    himmel2=2*(x[0]*x[0] + x[1] - 11) + 4*(x[0] + x[1]*x[1] -7)*x[1] - 22 #y-gradient
    z[0]=himmel1
    z[1]=himmel2
    
    J[0,0]=12*x[0]*x[0]+4*x[1]-42
    J[1,1]=12*x[1]*x[1]+4*x[0]-26
    J[0,1]=4*x[0]+4*x[1]
    J[1,0]=4*x[0]+4*x[1]
    
    return z
    
    
    
    
    
    