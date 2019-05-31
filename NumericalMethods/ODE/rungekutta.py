import numpy as np

def rk_12(func,h,y):
    #from the chapter
    k0=func(y)
    k1=func(y+h*k0)
    k=(k0+k1)/2.0
    
    y_1=y+h*k
    Err_1=h*(k-k0)
    
    
    return y_1,Err_1
    
    
    
def rk_34(func,h,y):
    k0=func(y)
    k1=func(y+0.5*h*k0)
    k2=func(y+0.5*h*k1)
    k3=func(y+h*k2)
    kh=1/6*k0+1/3*k1+1/3*k2+1/6*k3
    
    k4=func(y+h*k0)
    kl=1/6*k0+4/6*k1+1/6*k4
    
    
    y_1=y+h*kh
    Err_1=h*(kh-kl)
    
    return y_1,Err_1
    
    
def rk_driver(b,h,func,t,y,stepper,acc=1e-3,eps=1e-3):
    #for saving the path
    steps=0  
    a=t[-1]
    
    
    while steps < 1000:
        y0=y[-1]
        t0=t[-1]

        if(t0 >= b):
            break
        
        if(t0+h > b):
            h=b-t0
            
        (Y,Err) = stepper(func,h,y0)
        Err=np.linalg.norm(Err)
        Tole=(acc + np.linalg.norm(Y)*eps)*np.sqrt(h/(b-a))
        if(Err < Tole):
            steps +=1
            t = np.append(t,(t0+h))
            y.append(Y)
        elif (Err==0):
            h *=2
        else:
            h *=0.95*(Tole/Err)**0.25
    return t,y
        
    



