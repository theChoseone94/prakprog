import numpy as np



def plainMC(func,a,b,N,dim):
    
    V=1.0
    for i in range(dim):
        V *= b[i] - a[i]
    
    sum1=0.0
    sum2=0.0
    
    for i in range(int(N)):
        fx=func(np.random.uniform(a,b,len(a)))
        sum1+=fx
        sum2+=fx*fx
    
    mean=sum1/N
    sigma=np.sqrt(sum2/N- mean*mean)
    Sigma = sigma/np.sqrt(N) 
    
    result=mean*V
    Err= Sigma*V
    
    return (result, Err)