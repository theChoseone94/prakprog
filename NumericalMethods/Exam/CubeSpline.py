import numpy as np


def CS_with_D(x,y,dydx):
    n=np.size(dydx)
    h=np.zeros(np.size(dydx))
    p=np.zeros(np.size(dydx))
    for i in range(n-1):
        h[i] = x[i+1]-x[i] #step size between points
        p[i] = (y[i+1]-y[i])/h[i]
        
    b=np.array([])
    c=np.zeros(np.size(dydx))
    d=np.zeros(np.size(dydx))
    

    b=np.append(b,p[0])
    b=np.append(b,(p[0]+p[1])/2.0)
    
    for i in range(2,n-2):
        w1=np.fabs(p[i+1]-p[i])
        w2=np.fabs(p[i-1]-p[i-2])
        if(w1+w2==0):
            b=np.append(b,(p[i-1]+p[i])/2.0)
        else:
            b=np.append(b,(w1*p[i-1]+w2*p[i])/(w1+w2))
    
    
    b=np.append(b,(p[n-2]+p[n-3])/2.0) #b[n-2]
    b=np.append(b,p[n-2]) #b[n-1]
    for i in range(2,np.size(x)-1):
        c[i] = (3*(p[i]) - 2*b[i] - b[i+1])/(h[i])
        d[i] = (-2*(p[i]) + b[i] + b[i+1])/(h[i])**2
    
    
 

    #calculating S
    x_p=np.linspace(0,2*np.pi+1,n)
    S=np.zeros(np.size(dydx))
    for i in range (np.size(x-1))   :
        S[i] = y[i] + b[i] * (x_p[i]-x[i]) + c[i]*(x_p[i]-x[i])**2 + d[i]*(x_p[i]-x[i])**3

    

    return S













    
#for i in range(n):
#    b[0]=p[0]
#    b[1]=(p[0]+p[1])/2
#    b[n-1]=p[n-2]
#    b[n-2]=(p[n-2]+p[n-3])/2
#    
#for i in range()
#    