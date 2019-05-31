import numpy as np
import matplotlib.pyplot as plt
from rungekutta import *

def sin(y):
    return np.array([y[1],-y[0]])
a=0
b=3*np.pi #end-point
h=0.01 #step-size

x_0=np.array([a])
y=[]
y.append(np.array([0,1]))

x=np.linspace(0,3*np.pi,500)



#Even though i don't need to make two, I made such that you can change the rk_12 or rk_34
def ProblemA1():
    
    (X_12,Y_12)=rk_driver(b,h,sin,x_0,y,rk_12)
    

    plt.figure
    plt.plot(X_12,[Y_12[i][0] for i in range(len(Y_12))],'b*')
    plt.plot(X_12,[Y_12[i][1] for i in range(len(Y_12))],'k*')    
    plt.plot(x,np.sin(x),'r--')
    plt.plot(x,np.cos(x),'r--')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('rk_12 for sin(x) and cos(x)')
    plt.savefig("outA1.pdf") 

    print('Using rk_12 on sin(x) and cos(x) can be seen in outA1.pdf') 
    print('The value of x,f,df can be seen in out.txt. The first entries are for rk_12,')
    print('while a line break marks the change to rk_34.')
    print('\n')
    for i in range(len(Y_12)):
        print(X_12[i],Y_12[i][0],Y_12[i][1])
    
    print('\n')


def ProblemA2():
    (X_34,Y_34)=rk_driver(b,h,sin,x_0,y,rk_34)
    
    plt.figure
    plt.plot(X_34,[Y_34[i][0] for i in range(len(Y_34))],'b.')
    plt.plot(X_34,[Y_34[i][1] for i in range(len(Y_34))],'k.')
    plt.plot(x,np.sin(x),'r--')
    plt.plot(x,np.cos(x),'r--')
    print('Using rk_34 on sin(x) and cos(x) can be seen in outA2cat.pdf')  
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('rk_34 for sin(x) and cos(x)')

    plt.savefig("outA2.pdf")
    print('\n')

    for i in range(len(Y_34)):
        print(X_34[i],Y_34[i][0],Y_34[i][1])



    