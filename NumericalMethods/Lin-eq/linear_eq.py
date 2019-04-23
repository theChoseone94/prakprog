import matplotlib.pyplot as plt
import numpy as np
import array
import random

class matrix(object):
    def __init__ (self,n:int,m:int,t:type='d'):
                self.size1=n; "rows"
                self.size2=m; "columns" 
                self.data=array.array(t,[0.0]*(n*m))
        
    def set(self,i:int,j:int,x): 
            self.data[i+self.size1*j]=x
        
    def get(self,i:int,j:int)   : 
            return self.data[i+self.size1*j]
        
    def __getitem__ (self,ij)   : 
            i,j=ij; return self.get(i,j)
        
    def __setitem__ (self,ij,x) : 
            i,j=ij; self.set(i,j,x)
        
    def col(self,j): 
        return [self.data[i+self.size1*j] for i in range(self.size1)]
        
    def row(self,i):
        return [self.data[i+self.size1*j] for j in range(self.size2)]
        
    def view_matrix(self,K):
            for i in range(self.size1):
                for j in range(self.size2):
                    self.data[i+self.size1*j]=K[i][j]
        
    def show(self):
            mat=''
            for i in range(self.size1):
                for j in range(self.size2):
                    mat += '{:.3f}'.format(self.data[i+self.size1*j]) + '\t'
                mat += '\n'
            print(mat)
                
def multiply_matrix(A:matrix,B:matrix):
    C = matrix(A.size1,B.size2)
    for i in range(C.size1):
        for j in range(C.size2):
            C[i,j] = sum(A[i,k]*B[k,j] for k in range(A.size2))
    return C
                
def multiply_vector(A:matrix,v:list):
    b=[]
    for i in range(len(v)):
        b.append(sum(A[i,j]*v[j] for j in range(len(v))))
    return b
        
        
def transpose_matrix(A:matrix):
        B=matrix(A.size2,A.size1)
        for i in range(A.size1):
            for j in range(A.size2):
                B[j,i]= A[i,j]
        return B
        
def dot_multiply(A:list,B:list):
        C=0
        for i in range(len(A)):
            C += A[i]*B[i]
        return C
        
def copy_matrix(A:matrix):
        B=matrix(A.size1,A.size2)
        for i in range(A.size1):
            for j in range(A.size2):
                B[i,j]=A[i,j]
        return B
        
def qr_gs_decomposition(A:matrix):
    R=matrix(A.size2,A.size2)
    Q=matrix(A.size1,A.size2)
            
    A_copy=copy_matrix(A)
        
    for i in range(A.size2):
        R[i,i]=dot_multiply(A_copy.col(i),A_copy.col(i))**(1./2)
        for l in range(A.size1):
            Q[l,i]=A_copy[l,i]/R[i,i]
                
        for j in range(i+1,A.size2):
            R[i,j]=dot_multiply(Q.col(i),A_copy.col(j))
            for k in range(A.size1):
                A_copy[k,j]=A_copy[k,j]-Q[k,i]*R[i,j]
    return Q,R
        
def qr_gs_solve(Q:matrix,R:matrix,b:list):
        x=[0 for i in range(Q.size2)]
        for i in range(Q.size2):
            x[i]=dot_multiply(Q.col(i),b)
        for i in range(Q.size2-1,-1,-1):
            x[i]/=R[i,i]
            for j in range(i-1,-1,-1):
                x[j] -= x[i]*R[j,i]
                
        return x
            
            
        


    