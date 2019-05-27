import math
import numpy as np
import matplotlib as plt
from lsqfit import *

def one(x):
    return 1

def const(x)    :
    return x

def square(x):
    return x*x


def ProblemA():
    print('Problem A: Ordinary least-squares fit by QR-decomposition \n')
    x = [0.1,1.33,2.55,3.78,5,6.22,7.45,8.68,9.9]
    y = [-15.3,0.32,2.45,2.75,2.27,1.35,0.157,-1.23,-2.75]
    dy = [1.04,0.594,0.983,0.998,1.11,0.398,0.535,0.968,0.478]
    print('The functions are: log(x), 1 and 1/x \n')
    func=[math.log,one,const]
    results,uncern=ls_fit(func,x,y,dy)
    print('The fitted parameters are:\n')
    print(results)
    print('\nThe uncertainties are:\n')
    print(uncern)
    

def ProblemB():
    print('Problem B: Uncertainties of the fitting coefficients \n')
    x_b=[-4.2,-3.1,-1.9,-1,0,1.2,2.1,3,4.1]
    y_b=[30, 9, 0, -15, -16.3, -11, 0.3, 18, 48]
    dy_b=[2,4,1,3,2,0.5,1,3,2]
    print('The functions are: x^2, x and 1 \n')
    func_b=[square,const,one]
    results_b,uncern_b=ls_fit(func_b,x_b,y_b,dy_b)
    print('The fitted parameters are: \n')
    print(results_b)
    print('The uncerntainties are: \n')
    print(uncern_b)
    print('The fit can be seen in plot_B.pdf')
    
    x_fit=np.linspace(-4,4,100)
    y_fit=results_b[0]*square(x_fit)+results_b[1]*const(x_fit)+results_b[2]*one(x_fit)
    y_low=(results_b[0]-uncern_b[0])*square(x_fit)+(results_b[1]-uncern_b[1])*const(x_fit)+(results_b[2]-uncern_b[2])*one(x_fit)
    y_up=(results_b[0]+uncern_b[0])*square(x_fit)+(results_b[1]+uncern_b[1])*const(x_fit)+(results_b[2]+uncern_b[2])*one(x_fit)
    
    
    plt.figure()
    plt.errorbar(x_b,y_b,yerr=dy_b,label='Data')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.plot(x_fit,y_fit,'r-',label='Fit')
    plt.plot(x_fit,y_low,'k--',label='Fit +- $\delta$c')
    plt.plot(x_fit,y_up,'k--')   
    plt.grid()
    plt.legend()
    plt.title('Problem B')
    plt.savefig('plot_B.pdf')
    