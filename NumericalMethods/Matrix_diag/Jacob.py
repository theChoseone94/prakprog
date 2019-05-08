import numpy as np
from diagon import *
from math import *


def Jacobian(A:matrix,eps=1e-6):
    
    V=matrix(A.size1,A.size2) #matrix with the eigenvectors as columns
    J=matrix(A.size1,A.size2) #Jacobian matrix 
    
    for i in range(A.size1):
        J[i,i]=1
        V[i,i]=1
    while sum([sum([abs(A[i,j]) for j in range(i)]) for i in range(1,A.size1)])>eps:
        for q in range(1,A.size1):
            for p in range(q):
                phi=0.5* np.arctan2(2.*A[p,q],A[q,q]-A[p,p])
                J[p,p]=cos(phi)
                J[q,q]=cos(phi)
                J[p,q]=sin(phi)
                J[q,p]=-sin(phi)
                A=multiply_matrix(transpose_matrix(J),multiply_matrix(A,J))
                V=multiply_matrix(V,J)
                J[p,p]=1
                J[q,q]=1
                J[p,q]=0
                J[q,p]=0
    return A,V
        

def Jacobian_eigen(A:matrix,m:int=None,transpose=False,eps=1e-6):
    if not m:
        m=A.size1
    else:
        assert(m<=A.size1)
        m+=1
    
    V=matrix(A.size1,A.size2)
    V_diag=matrix(A.size1,A.size2)
    A_diag=copy_matrix(A)
    for i in range(A.size1):
        V[i,i]=1
        V_diag[i,i]=1
    
    for p in range(m-1):
        while sum([abs(A[p,j]) for j in range(p+1,A.size2)]) >eps:
            for q in range(p+1,A.size1):
                if not transpose:
                    phi=0.5*np.arctan2(2.0*A[p,q],A[q,q]-A[p,p])
                elif transpose:
                    phi=0.5*(np.pi+np.arctan2(2.0*A[p,q],A[q,q]-A[p,p]))
                
                for i in range(A.size1):
                    if not (i==q) or (i==p):
                        #These are the diagonisation of A from the pdf
                        A_diag[p,i]=np.cos(phi)*A[p,i]-np.sin(phi)*A[q,i]
                        A_diag[i,p]=np.cos(phi)*A[p,i]-np.sin(phi)*A[q,i]
                        
                        A_diag[q,i]=np.sin(phi)*A[p,i]+np.cos(phi)*A[q,i]
                        A_diag[i,q]=np.sin(phi)*A[p,i]+np.cos(phi)*A[q,i]
                        #These are the diagonisation of V from the pdf 
                        V_diag[i,p]=np.cos(phi)*V[i,p]-np.sin(phi)*V[i,q]
                        V_diag[i,q]=np.sin(phi)*V[i,p]+np.cos(phi)*V[i,q]
                        
                A_diag[p,p]=np.cos(phi)**2*A[p,p]-2*np.cos(phi)*np.sin(phi)*A[p,q]+np.sin(phi)**2*A[q,q]
                A_diag[q,q]=np.sin(phi)**2*A[p,p]+2*np.cos(phi)*np.sin(phi)*A[p,q]+np.cos(phi)**2*A[q,q]
                A_diag[p,q]=np.sin(phi)*np.cos(phi)*(A[p,p]-A[q,q])+(np.cos(phi)**2 - np.sin(phi)**2)*A[p,q]
                A_diag[q,p]=np.sin(phi)*np.cos(phi)*(A[p,p]-A[q,q])+(np.cos(phi)**2 - np.sin(phi)**2)*A[p,q]
                
                V=copy_matrix(V_diag)
                A=copy_matrix(A_diag)
                
    return A,V

                        