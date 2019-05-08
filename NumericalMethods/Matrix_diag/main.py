from Jacob import *
import numpy as np
import random
from timeit import Timer

def test(n,problem='A1',l=None):
    A=matrix(n,n)
    for i in range(n):
        A[i,i]=random.uniform(-5,5)
        for j in range(i,n):
            k=random.uniform(-5,5)
            A[i,j]=k
            A[j,i]=k
    if problem =='A1':
        print('A is equal to:')
        A.show()
        D,V=Jacobian(A)
        print('V is equal to:')
        V.show()
        print('D is equal to:')
        D.show()
        print('V^T A V is equal to:')
        C=multiply_matrix(transpose_matrix(V),multiply_matrix(A,V))
        C.show()
        print('This should be equal to D \n')
    if problem =='A2':
        D,V=Jacobian(A)
    if problem=='B':
        D,V=Jacobian_eigen(A,m=l)
            
            
def problemA():
    print('This is problem A')
    test(4,problem='A1')
    time = []
    size = []
    for n in range(2,10):
        size.append(n)
        t = Timer(lambda: test(n,problem='A2'))
        time.append(t.timeit(number=3))
    print('Testing the order:')
    for i in range(len(time)):
        print('n={:2d},\ttime={}'.format(size[i],time[i]))
        
def problemB():
    print('This is problem B')
    pi_matrix=[[3,1,4,1],
              [5,9,2,6],
              [5,3,5,8],
              [9,7,9,2]]
    A=matrix(4,4)
    A.view_matrix(pi_matrix)
    print('A is equal to:')
    A.show()


    print('Lowest eigenvalue:')
    D1,V=Jacobian_eigen(A,transpose=False)
    D1.show()
    print('Highest eigenvalue:')
    D2,V=Jacobian_eigen(A,transpose=True)
    D2.show()
    print('Testing the time of the execution. \n n is the dimension of the matrix \n Time_1 is the time for cyclic diagnolization \n time_2 is the time for the single eigenvalue \n time_3 is the time for all eigenvalues')
    for n in range(2,10):
        time_1 = Timer(lambda: test(n,problem='A2'))
        time_2 = Timer(lambda: test(n,problem='B',l=1))
        time_3 = Timer(lambda: test(n,problem='B'))
        print('n={:2d}\t time_1={:.10f}\t time_2={:.10f}\t time_3={:.10f}'.format(n,
time_1.timeit(number=1),time_2.timeit(number=1),time_3.timeit(number=1)))
    
    
    
    
    
    