import numpy as np
import math
import sys
sys.setrecursionlimit(10000) #make sure it doesn't diverge

def points(a,b):
    x=np.array([1.0/6, 2.0/6, 4.0/6, 5.0/6])
    return a+(b-a)*x


def integrator_recursive(func,a,b,acc,eps,f2,f3,error,steps):
    f1=func(points(a,b)[0])
    f4=func(points(a,b)[3])
    q=(2*(f1 + f4) + f2 + f3)*(b-a)/6.0
    Q=(f1 + f2 + f3 +f4)*(b-a)/4.0
    
    tol = acc+eps*math.fabs(Q)
    error_int=np.fabs(Q-q)
    if(error_int < tol):
        error=error_int
        return Q,steps
    
    else:
        error_1=0.0
        error_2=0.0
        
        Q_half1,steps1=integrator_recursive(func,a,(a+b)/2.0,acc/math.sqrt(2.0),eps,f1,f2,error_1,steps=steps+1)
        Q_half2,steps2=integrator_recursive(func,(a+b)/2.0,b,acc/math.sqrt(2.0),eps,f3,f4,error_2,steps=steps+1)
        Q=Q_half1+Q_half2
        steps=max(steps1,steps2)
    return Q,steps


def integrator(func,a,b,acc,eps,error):
    f2=func(points(a,b)[1])
    f3=func(points(a,b)[2])
    
    Q,steps=integrator_recursive(func,a,b,acc,eps,f2,f3,error,steps=0)
    return Q,steps


def C_C(f, a, b, acc, eps, error): 
    def F(t):
        return (f((a + b)/2.0 + (a - b)*np.cos(t)/2.0)*np.sin(t)*(b - a)/2.0) 
    return integrator(F, 0.0, np.pi, acc, eps, error)


def infinite_integrator(func,a,b,acc,eps,error):
    Low=np.isinf(a)
    Up=np.isinf(b)
    
    if (Low == False and Up == False):
        Q,steps = integrator(func,a,b,acc,eps,error)
        
    elif (Low == True and Up == False):
        def Low_inf(x):
            return (func(b-(1-x)/x)/x**2)
        Q,steps = integrator(Low_inf,0,1,acc,eps,error)
        
    elif (Low == False and Up == True):
        def Up_inf(x):
            return (func(a+(1-x)/x)/x**2)
        Q,steps = integrator(Up_inf,0,1,acc,eps,error)
        
    elif(Low == True and Up == True):
        def LowUp_inf(x):
            return (func(x/(1-x**2))*(1+x**2)/(1-x**2)**2)
        Q,steps = integrator(LowUp_inf, -1, 1, acc,  eps, error)
        
    else:
        print('Error has occured')
        Q = float('Inf')
        
    return Q,steps
        
    




