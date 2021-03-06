import numpy as np
import sys
sys.setrecursionlimit(10000) #makes sure it doesn't diverge
from Integrator import *


def sqrt(x):
    return np.sqrt(x)

def invsqrt(x):
    return 1/np.sqrt(x)

def ln(x):
    return np.log(x)/np.sqrt(x)

def pi_func(x):
    return 4*np.sqrt(1-(1-x)**2)

def gaussian_func(x):
    return np.exp(-x**2)


a=0
b=1.0
acc=1e-6
eps=1e-6
error=0.0

def ProblemA():
    print('The Sqrt(x)')
    results_sqrt,steps_sqrt=integrator(sqrt,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_sqrt)
    print('The number of iterations is',steps_sqrt)
    print('The exact value of the integral is:')
    print(2/3)
    print('The error between the results and exact value is', np.fabs(results_sqrt-(2/3)))

    print('\n')
    
    
    print('The inverse Sqrt(x)')
    results_invsqrt,steps_invsqrt=integrator(invsqrt,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_invsqrt)
    print('The number of iterations is',steps_invsqrt)
    print('The exact value of the integral is:')
    print(2)
    print('The error between the results and exact value is', np.fabs(results_invsqrt-2))

    print('\n')
    
    
    
    print('The ln(x)/sqrt(x)')
    results_ln,steps_ln=integrator(ln,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_ln)
    print('The number of iterations is',steps_ln)
    print('The exact value of the integral is:')
    print(-4)
    print('The error between the results and exact value is', np.fabs(results_ln-(-4)))
    print('\n')
    
    
    print('The function to calculate pi')
    results_pi,steps_pi=integrator(pi_func,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_pi)
    print('The number of iterations is',steps_pi)
    print('The exact valye of the integral is:')
    print(np.pi)
    print('The error between the results and exact value is', np.fabs(results_pi-np.pi))


def ProblemB():
    print('#########################################################################')
    print('The Clenshaw-Curtis transformation')
    print('\n')
    print('The Sqrt(x)')
    results_sqrt,steps_sqrt=C_C(sqrt,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_sqrt)
    print('The number of iterations is',steps_sqrt)
    print('The exact value of the integral is:')
    print(2/3)
    print('The error between the results and exact value is', np.fabs(results_sqrt-(2/3)))
    print('\n')
    
    
    print('The inverse Sqrt(x)')
    results_invsqrt,steps_invsqrt=C_C(invsqrt,a,b,acc,eps,error)
    print('The recursive integrator gives the result:')
    print(results_invsqrt)
    print('The number of iterations is',steps_invsqrt)
    print('The exact value of the integral is:')
    print(2)
    print('The error between the results and exact value is', np.fabs(results_invsqrt-2))

    print('\n')  
  
    print('As it can be seen, the Clenshaw-Curtis is quite faster, than the original method')
    print('and has smaller errors')
    
def ProblemC():
    print('#########################################################################')
    print('Testing the infinite integration on the gaussian integral')
    print('from 0 to inf')
    
    result_inf1,steps_inf1=infinite_integrator(gaussian_func,0,np.inf,acc,eps,error)
    
    print('The result from the integral from 0 to inf',result_inf1)
    print('The number of interations is',steps_inf1)
    print('The exact value of the integral is',np.sqrt(np.pi)/2.0)
    
    
    print('\n')
    print('Testing the infinite integration on the gaussian integral')
    print('from -inf to 0')
    
    result_inf2,steps_inf2=infinite_integrator(gaussian_func,-np.inf,0,acc,eps,error)
    
    print('The result from the integral from -inf to 0',result_inf2)
    print('The number of interations is',steps_inf2)
    print('The exact value of the integral is',np.sqrt(np.pi)/2.0)
    
    print('\n')
    print('Testing the infinite integration on the gaussian integral')
    print('from -inf to inf')
    
    result_inf3,steps_inf3=infinite_integrator(gaussian_func,-np.inf,np.inf,acc,eps,error)
    
    print('The result from the integral from -inf to inf',result_inf3)
    print('The number of interations is',steps_inf3)
    print('The exact value of the integral is',np.sqrt(np.pi))    
    
    
    