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
    #weights
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
    
    return b,c,d
    

def half_int(n, x, z):
    #finds the point to interpolate over
    it = int(0); # iteration number
    L = int (0); 
    R = int(n-1)

    if (L > R):
        print("Error, list must be longer\n")
        return -1

    while (L <= R):
        # Search for the interval in which z belongs
        m = int((L+R)/2)

        if (x[m] <= z and x[m+1] > z):
            return m
        elif (x[m] < z):
            L = m + 1
        elif (x[m] > z):
            R = m - 1
        it = it + 1
        if (it > n):
            print("Search was not succesful.\n")
            return -1
            break
 
def eval_CS(x,y,z,dydx):
    n = len(x)
    #taking the b,c,d values from before cubic spline
    b = CS_with_D(x, y, dydx)[0]
    c = CS_with_D(x, y, dydx)[1]
    d = CS_with_D(x, y, dydx)[2]
    
    m = half_int(n, x, z) # Search
    
    S=(y[m] + b[m]*(z-x[m]) + c[m]*(z-x[m])**2 + d[m]*(z-x[m])**3) #calc
    
    return S













    
#for i in range(n):
#    b[0]=p[0]
#    b[1]=(p[0]+p[1])/2
#    b[n-1]=p[n-2]
#    b[n-2]=(p[n-2]+p[n-3])/2
#    
#for i in range()
#    