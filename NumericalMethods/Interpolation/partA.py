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
"Create list of points x,y and z, with z being inbetween minimum(x) and maximum(x)"
xlist=list(range(0,11))
ylist=[1,2,3,4,5,6,7,8,9,10,11 ]
zlist=[(min(xlist)+random.random()*max(xlist)-min(xlist)) for i in range(50)]
zlist.sort()
"New points from interpolation saved in yz and area from integral is saved in Area "
yz=[]
Area=[]
for i in range(len(zlist)):
    yl,_=linterp(xlist,ylist,zlist[i])
    yz +=[yl]
    Al=linterp_integ(xlist,ylist,zlist[i])
    Area +=[Al]

"Plot figures"
f = plt.figure(figsize=(10,4))

ax1=f.add_subplot(121)
plt.grid("true") 
plt.xlabel("x")
plt.ylabel("y")
ax1.plot(zlist,yz,'r.',xlist,ylist,'b*')
plt.xlim(-1,11)
    
ax2=f.add_subplot(122)
plt.xlabel("x") 
plt.ylabel("Area")
plt.grid("true")
ax2.plot(zlist,Area,'r.')
plt.savefig('LinearInterpolation.png')
