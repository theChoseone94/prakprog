import numpy as np
from linear_eq import *
import random


def TASKA1():
        print('This is task #1')
        A=matrix(4,3)
        data=np.random.rand(4,3)*4
        A.view_matrix(data)
        print('Setting the matrix A')
        A.show()
        print("R is upper triangular?")
        Q,R=qr_gs_decomposition(A)
        R.show()
        print("Q times Q-transposed should be 1")
        multiply_matrix(transpose_matrix(Q),Q).show()
        print("Is QR = A?")
        print("QR is:")
        multiply_matrix(Q,R).show()
        print("A is:")
        A.show()
        
def TASKA2():
    print("This is task #2")
    A=matrix(3,3)
    data=np.random.rand(3,3)*4
    A.view_matrix(data)
    print("This is matrix A")
    A.show()
    b=np.random.rand(3,1)*3
    print("This is vector b:")
    for i in range(len(b)):
        print(float(b[i]))
    
    Q,R=qr_gs_decomposition(A)
    
    print("\n this is Q")
    Q.show()
    
    print("this is R")
    R.show()
    
    x=qr_gs_solve(Q,R,b)
    print("x is:")
    for i in range(len(x)):
        print(float(x[i]))
    print("\n Ax is:")
    b_solve=multiply_vector(A,x)
    for i in range(len(b_solve)):
        print(float(b_solve[i]))
    
    
    print("\n b is:")
    for i in range(len(b)):
        print(float(b[i]))
        
def TASKB1():
    print("This is part B")
    A=matrix(3,3)
    data=np.random.rand(3,3)*3
    A.view_matrix(data)
    
    print("A is")
    A.show()
    
    Q,R=qr_gs_decomposition(A)
    
    print("Q is")
    Q.show()
    
    print("R is")
    R.show()
    
    B=qr_gs_inverse(Q,R)
    print("This is A inverse (or B)")
    B.show()
    print("AB is equal to")
    I=multiply_matrix(A,B).show()
    
    
    
    
    
    
    
    
    
    