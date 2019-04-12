import numpy as np
import matplotlib.pyplot as plt
from math import *
import random


def BinarySearch(x,z):
    first=0
    last = len(x)-1
    mid=floor((first+last)/2.)

    while(first<=last):
        if x[mid]==z:
            break
        elif x[mid]<z:
            first=mid+1
        elif x[mid]>z:
            last=mid-1
        mid=floor((first+last)/2.)
        print(mid)
    return mid


def linterp(x:list, y:list,z:float):
    mid=BinarySearch(x,z)
    "Linear interpolation from wikipedia says that the new y value for the linear interpolation is given as:"
    
    pol=y[mid+1]-y[mid]/(x[mid+1]-x[mid])
    return y[mid]+pol*(z-x[mid]),mid


def linterp_integ(x:list,y:list,z:float):
    "Make x and y"
    
    yz,mid=linterp(x,y,z)
    
    x=x[:mid+1]+[z]
    y=y[:mid+1]+[yz]
    
    "Integrating analytically with a for loop. a and b is given as a standard linear line. The integration is just the"
    "integration of a linear function: y = a*x+b"
    integ=0
    for i in range(len(x)-1):
        a=(y[i+1]-y[i])/(x[i+1]-x[i])
        b=y[i]-a*x[i]
        integ=1/2*a*(x[i+1]**2 - x[i]**2)+b*(x[i+1]**2-x[i]**2)
        return integ

xlist=list(range(1,11))
ylist=[1, 2,4,8,16,32,40,44,46,47 ]
zlist=[(min(xlist)+random.random()*max(xlist)-min(xlist)) for i in range(50)]
zlist.sort()
yz=[]
At=[]
for i in range(len(zlist)):
    yl,_=linterp(xlist,ylist,zlist[i])
    yz +=[yl]
    Al=linterp_integ(xlist,ylist,zlist[i])
    At +=[Al]

plt.figure
plt.plot(zlist,yz,'r.',xlist,ylist,'b*')
plt.show() 
    
    
