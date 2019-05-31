import numpy as np
from functions import *
from newton import *
from qr import *
import matplotlib.pyplot as plt



def ProblemA():
    print('Minimization with Newton\'s method')
    print('\n')
    
    x=[10.0,12.0]
    eps = 1e-7
    dx = 1e-9
    print('The Rosenbrock')
    min_Ros = newtonian(Rosenbrock_Jacob,x,eps)
    print('The minimum of the Rosenbrock function is',(min_Ros))
    print('\n')
    print('The Himmelblau')
    min_him = newtonian(Himmelblau_Jacob,x,eps)
    print('The minimum of the Himmelblau function is',(min_him))

def ProblemB1():
    x=[10.0,12.0]
    eps = 1e-7
    dx = 1e-9
    print('\n')
    print('Minimization with the QuasiNewton method')
    min_RosQ=quasi_newtonian(Rosenbrock_Jacob,x,dx,eps)
    print('The minimum of the Rosenbrock function is',min_RosQ)
    print('\n')
    min_himQ=quasi_newtonian(Himmelblau_Jacob,x,dx,eps)
    print('The minimum of the Himmelblau function is', min_himQ)
    print('\n')
    
    print('When comparing the # of iterations, it is clear that the')
    print('that the Quasi-Newton method is much faster.')
    print('For the Rosenbrock is 609 vs. 52 iterations')
    print('and for the Himmelblau it is 9 vs 12.')
    print('It should be noted that the Himmelblau finds another minimum.')
    print('\n')

    
def ProblemB2():
    print('Decay function')
    x=[10.0,12.0]
    eps = 1e-7
    dx = 1e-9
    t=[0.23,1.29,2.35,3.41,4.47,5.53,6.59,7.65,8.71,9.77]
    y=[4.64,3.38,3.01,2.55,2.29,1.67,1.59,1.69,1.38,1.46]
    e=[0.42,0.37,0.34,0.31,0.29,0.27,0.26,0.25,0.24,0.24]
    
    fit = lambda p: Master_Function(t,y,e,p)
    x_guess = [2.0, 2.0, 2.0]
    
    Fitting = quasi_newtonian(fit,x_guess,dx,eps)
    print('The fit from the decay can be seen in decay.pdf')
    
    t_plot=np.linspace(0,10,1000)
    figure,ax=plt.subplots(1,1)
    ax.plot(t_plot,radioactive(Fitting,t_plot),'-b',label='Fit')
    ax.errorbar(t,y,yerr=e,fmt='r.',label='Data')
    plt.legend()
    plt.savefig('decay.pdf')
   
