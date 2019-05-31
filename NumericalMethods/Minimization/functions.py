import sympy as sy
import numpy as np
import math


    
        
def Rosenbrock_Jacob(x):
    z_Rj=(1.0-x[0])**2.0 + 100.0 * (x[1]-x[0]**2.0)**2.0
    
    #Jacobian
    J=np.empty((len(x),len(x)))
    J[0,0]=2.0*(600.0*x[0]*x[0]-200.0*x[1]+1.0)
    J[1,1]=200.0
    J[0,1]=-400.0*x[0]
    J[1,0]=-400.0*x[0]
    
    #derivatives (0: x, 1: y)
    dfdx=np.empty(len(x))
    dfdx[0]=2.0*x[0] - 2.0 + 400.0*x[0]**3.0 - 400.0*x[1]*x[0]
    dfdx[1]=200.0*x[1]-200.0*x[0]**2.0
    
    
    return z_Rj, J, dfdx
    

    

def Himmelblau_Jacob(x):
    z=np.empty(len(x))
    z=(x[0]**2+x[1]-11)**2 + (x[0]+x[1]**2-7)**2
    
    #Jacobian
    J=np.empty((len(x),len(x)))
    J[0,0]=12*x[0]*x[0]+4*x[1]-42
    J[1,1]=12*x[1]*x[1]+4*x[0]-26
    J[0,1]=4*x[0]+4*x[1]
    J[1,0]=4*x[0]+4*x[1]
    
    #derivatives (0:x, 1:y) + 
    dfdx=np.empty(len(x))
    dfdx[0]= 4*x[0]**3 + 4*x[0]*x[1] - 42*x[0] + 2*x[1]**2-14
    dfdx[1]= 2*x[0]**2+4*x[1]*x[0]+4*x[1]**3-26*x[1]-22
    

    return z, J, dfdx
    

def radioactive(x,t):
    return x[0]*np.exp(-t/x[1])+x[2]

def Master_Function(t,y,e,p):
    s = 0
    for i in range(len(t)):
        s += ((radioactive(p,t[i]) - y[i])**2 / (e[i]*e[i]))
    return np.array([s])
    
    
    
    