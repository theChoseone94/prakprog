import numpy as np
from qr import *
import math
import sympy as sp


def newtonian(func, x_0,eps):
    steps = 0
    alph = 1e-2
    x = x_0.copy()

    while True:
        steps +=1
        (fx, H, dfdx) = func(x)
        (Q, R) = qr_gs_decomposition(H)
        Dx_sol = qr_gs_solve(Q, R, -dfdx)
        lambd = 2.0
    
        while True:
            a = Dx_sol*lambd
            y = x + a
            (fy, Hy, dfy) = func(y)
            if (fy < fx + alph*np.dot(a.T, dfdx) or lambd < 0.02):
                break
            lambd /= 2.00
    
        x = y.copy()
        dfdx = dfy.copy()
    
        if (np.linalg.norm(dfdx) < eps): # steps>stepsmax): #
            print('Finished after %i iterations.' % (steps))
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

def gradient(func,x,dx):
    m=len(x)
    dfdx=np.empty(m)
    fx=func(x)[0]
    
    for i in range(m):
        x[i] +=dx
        dfdx[i]=(func(x)[0]-fx)/dx
        x[i] -=dx
    return dfdx


def quasi_newtonian(func,x_0,dx,eps):
    steps=0
    x=x_0.copy()
    m=len(x)
    dfdx=gradient(func,x,dx)
    fx=func(x)[0]
    alpha = 1e-4 #Alpha from the Armijo condition
    A=np.eye(m) #diagonal matrix with ones in the diagonal and zero else where.
    
    while True:
        steps +=1
        Dx_solved=np.dot(A,-dfdx) 
        lambd=2.0
        while True:
            lambd /=2.0
            s = Dx_solved*lambd
            g = x + s
            fg=func(g)[0]
            if np.abs(fg) < np.abs(fx) + alpha*np.dot(s,dfdx):
                break
            if np.linalg.norm(s) < dx:
                A=np.eye(m)
                break
        dfdx_g=gradient(func,g,dx)
        y = dfdx_g - dfdx
        u = s - np.dot(A,y)
        
        #broydens update from the chapter
        if(np.abs(np.dot(y,s))> eps):
            gamma=np.dot(u,y)/(2*np.dot(s,y))
            a=(u-gamma*s)/(np.dot(s,y))
            A = A + np.outer(s,a) + np.outer(a,s)
        
        x=g
        fx=fg
        dfdx=dfdx_g
        
        if(np.linalg.norm(dfdx)<eps or np.linalg.norm(Dx_solved)<dx):
            print('Finished after %i iterations.' %(steps))
            break
        
    return x
        
        
                
    
    
    
    
    
    
    
    
    