import numpy as np
import math
from qr import *
import sympy as sy


def newtonian(func, x_0, dx,eps):
    steps=0
    x=x_0.copy()
    m=len(x)
    J=np.empty((m,m))
    while True:
        fx = func(x)
        for j in range(m):
            x[j] = x[j]+dx
            df = func(x)-fx
            for i in range(m):
                J[i,j]=df[i]/dx
            x[j]=x[j]-dx
            
        (J1,R) = qr_gs_decomposition(J)
        Dx = ((qr_gs_solve(J1,R,-fx)))


        lambd=2
        while True:
            lambd=lambd/2.0
            y = x + Dx*lambd
            fy=func(y)
            if(np.linalg.norm(fy) < (1-lambd/2.0)*np.linalg.norm(fx) or lambd < 0.02):
                break
        x=y.copy()
        fx=fy.copy()
        steps +=1
        if(np.linalg.norm(Dx) < dx or np.linalg.norm(fx) < eps):
            print('Finished in %i iterations.' %(steps))
            break
    return x
            

def newtonian_With_jacobian(func,x_0,eps):
    steps=0
    x=x_0.copy()
    m=len(x)
    J=np.empty((m,m))
    
    while True:
        fx=func(x,J)
        (J1,R)=qr_gs_decomposition(J)
        Dx_solvd=qr_gs_solve(J1,R,-fx)
        
        lambd=2.0
        while True:
            lambd /=2.0
            y=x+Dx_solvd*lambd
            fy=func(y,J)
            if(np.linalg.norm(fy) < (1-lambd/2)*np.linalg.norm(fx) or lambd < 0.02):
                    break
        x=y
        fx=fy
        steps+=1
        if(np.linalg.norm(fx) < eps):
            print('Finished in %i iterations.' %(steps))
            break
    return x