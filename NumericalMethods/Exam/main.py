import numpy as np
import matplotlib.pyplot as plt
from CubeSpline import *

plt.close('all')

print('I have tested the cubic-sub spline with sin(x) from 0 to 2*pi.')
#The data set of sin(x) with derivative cos(x) from 0 to 2 pi
x0=np.linspace(0,2*np.pi,20)#x_i in the assignment
y=np.sin(x0) #y_i in the assignment
dydx=np.cos(x0)# y'_i in the assignment 

k=100 #number of points
z0=np.zeros(k) #storing z-values
S=np.zeros(k) #storing S values
for i in range(k):
    z=i*2*np.pi/k
    z0[i]=z
    S[i]=eval_CS(x0,y,z,dydx)

print('The interpolated values can be seen beneath:')
print(S)
print('\n')
print('The mean residual between the interpolated sin(x) and numpy\'s sin(x) is')
print(np.mean(S-np.sin(z0)))

#Setting up the plot
print('\n')
print('A figure with the spline interpolation can be seen in Exam.pdf')

#plot sin(x) and cos(x)
plt.figure()
plt.plot(x0,y,'ro',label='sin(x) from data')
plt.plot(x0,dydx,'ko',label='sin\'(x) = cos(x) from data')
#plot the interpolated function
plt.plot(z0,S,'g*',label='C-spline with derivative')
plt.legend()
plt.savefig('Exam.pdf')