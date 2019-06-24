import numpy as np
from Searching import *


def CS_with_D(x,y,dydx):
    n=np.size(dydx)
    h=np.zeros(np.size(dydx))
    p=np.zeros(np.size(dydx))
    for i in range(n-1):
        h[i] = x[i+1]-x[i] #step size between points
        p[i] = (y[i+1]-y[i])/h[i] #slope
    b=np.array([])
    c=np.zeros(np.size(dydx))
    d=np.zeros(np.size(dydx))
    

    b=np.append(b,p[0])
    b=np.append(b,(p[0]+p[1])/2.0)
    #weights from Akimo
    for i in range(2,n-2):
        w1=np.fabs(p[i+1]-p[i])
        w2=np.fabs(p[i-1]-p[i-2])
        if(w1+w2==0):
            b=np.append(b,(p[i-1]+p[i])/2.0)
        else:
            b=np.append(b,(w1*p[i-1]+w2*p[i])/(w1+w2))
    
    
    b=np.append(b,(p[n-2]+p[n-3])/2.0) #b[n-2]
    b=np.append(b,p[n-2]) #b[n-1]
    
    ###############################################################################################################################
    
#    for i in range(2,np.size(x)-1):
#        c[i] = (3*(p[i]) - 2*b[i] - b[i+1])/(h[i]) #I tried changing the b's in this to dydx, with no change to the end result.
#        d[i] = (-2*(p[i]) + b[i] + b[i+1])/(h[i])**2 #I tried change the b's into dydx, but again no change to the end spline result.
#        
    ###############################################################################################################################
    
    #If you want to try yourself, comment the for loop marked with #'s above and uncomment the for loop below
    
    #########################################################
    for i in range(2,np.size(x)-1):
        c[i] = (3*(p[i]) - 2*dydx[i] - dydx[i+1])/(h[i]) 
        d[i] = (-2*(p[i]) + dydx[i] + dydx[i+1])/(h[i])**2 
        b[i]=dydx[i] 
    ############################################################ 
    return b,c,d
    
 
def eval_CS(x,y,z,dydx):
    n = len(x)
    #taking the b,c,d values from before cubic spline
    b = CS_with_D(x, y, dydx)[0]
    c = CS_with_D(x, y, dydx)[1]
    d = CS_with_D(x, y, dydx)[2]
    
    m = BinarySearch(n,x,z) # Searching using the binary search from the Seaching.py used in the Interpolation assignment
    
    S=(y[m] + b[m]*(z-x[m]) + c[m]*(z-x[m])**2 + d[m]*(z-x[m])**3) #calculating S
    
    return S
