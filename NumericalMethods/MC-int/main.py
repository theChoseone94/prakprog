from plainMC import *
import matplotlib.pyplot as plt

def sqrt(x):
    return np.sqrt(x)

def invsqrt(x):
    return 1/np.sqrt(x)

def singular(x):
    return 1/(1-np.cos(x[0])*np.cos(x[1])*np.cos(x[2]))*1/np.pi**3


def ProblemA():
    
    a=np.array([0])
    b=np.array([1])
    N=1e6
    print('Testing the MC integration on the integral sqrt(x) from 0 to 1')
    result_sqrt,Err_sqrt=plainMC(sqrt,a,b,N,1)
    print('The result from the MC integration is', result_sqrt)
    print('The exact value of the integral is', 2/3)
    print('The estimated error from the MC-integration is',Err_sqrt)
    print('The real error is',(result_sqrt-2/3))
    print('\n')
    print('Testing the MC integartion on the integral 1/sqrt(x) from 0 to 1')
    result_invsqrt,Err_invsqrt=plainMC(invsqrt,a,b,N,1)
    print('The result from the MC integration is', result_invsqrt)
    print('The exact value of the integral is',2.0)
    print('The estimated error from the MC-integration is',Err_invsqrt)
    print('The real error is',(result_invsqrt-2.0))
    print('\n')
    
    
    print('I will now test on the difficult singular integral given in the assignment')
    a_sing=np.array([0,0,0])
    b_sing=np.array([np.pi,np.pi,np.pi])
    N_sing=1e5
    
    result_sing,Err_sing=plainMC(singular,a_sing,b_sing,N_sing,3)
    print('The result from MC-integration is',result_sing)
    print('The exact value of the integral is',1.393203929685676)
    print('The estimated error from the MC-integral is',Err_sing)
    print('The real error is',np.fabs(result_sing-1.393203929685676))
    
    
def ProblemB():
    a_sing=np.array([0,0,0])
    b_sing=np.array([np.pi,np.pi,np.pi])
    x=np.linspace(1,10**6,5)
    print('The error of the MC-method can be seen in Error.pdf')
    
    
    results=[]
    errors=[]
    Ns=[]
    for i in range(1,6):
        ress,errs=plainMC(singular,a_sing,b_sing,10**i,3)
        results.append(ress)
        errors.append(errs)
        Ns.append(10**i)
    plt.figure
    plt.loglog(Ns,errors,'r-',label='MC-error')
    plt.loglog(Ns,1/np.sqrt(np.array(Ns)),'k--',label='1/ \sqrt(N)')
    plt.legend()
    plt.xlabel('N')
    plt.ylabel('Error(N)')
    
    plt.grid()
    plt.savefig('Error.pdf')
    
    
    