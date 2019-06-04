import numpy as np
import scipy.optimize as opt


class ANN:
    
    def __init__(self,function,neurons):
        self.f=function
        self.n=neurons
        self.params = np.random.rand(self.n,3)
        
    def forward(self,input):
        
        x=input
        output=0
        
        for i in range(self.n):
            a = self.params[i][0]
            b = self.params[i][1]
            w = self.params[i][2] #weights 
            output += self.f((x+a)/b)*w
        return output
    
    def training(self,input_val,goal_val):
        
        def Corr_learn(k):
            self.params = np.reshape(k,(self.n,3))
            f=goal_val
            y = self.forward(input_val)
            diff = np.sum(np.fabs(y-f)**2)
            return diff
        
        opt.minimize(Corr_learn,np.random.rand(3*self.n),method='BFGS',tol=1e-4)
        