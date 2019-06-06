import numpy as np
import matplotlib.pyplot as plt
from CubeSpline import *

#The data set of sin(x) with derivative cos(x) from 0 to 2 pi
x0=np.linspace(0,2*np.pi,20)#x_i in the assignment
y=np.sin(x0) #y_i in the assignment
dydx=np.cos(x0) # y'_i in the assignment 




S=CS_with_D(x0,y,dydx)




#Setting up the plot
plt.figure()
#plot the interpolated function



#plot sin(x) and cos(x)
plt.plot(x0,y,'ro',label='sin(x) from data')
plt.plot(x0,dydx,'ko',label='sin\'(x) = cos(x) from data')
plt.legend()