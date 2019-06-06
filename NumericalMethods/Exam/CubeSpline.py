import numpy as np


def CS_with_D(x,y,dydx):
    b=np.zeros(np.size(dydx))
    c=np.zeros(np.size(dydx))
    d=np.zeros(np.size(dydx))
    
    
    for i in range(np.size(x)-1):
        b[i] = dydx[i]
        c[i] = 3*(y[i+1]-y[i]) - 2*dydx[i] - dydx[i+1]
        d[i] = 2*(y[i]-y[i+1]) + dydx[i] + dydx[i+1]
    
    
#calculating S

    S[i] = y[i] + b[i] * (x-x0[i]) + c[i]*(x-x0[i])**2 + d[i]*(x-x0[i])**3




    return S