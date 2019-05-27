import math
from linear_eq import *

def ls_fit(functions:list,x:list,y:list,dy:list):
    A=matrix(len(x),len(functions))
    b_s=[y[i]/dy[i] for i in range(A.size1)]
    b=matrix(len(b_s),1);
    for i in range(A.size1):
        b[i,0]=b_s[i]
        for k in range(A.size2):
            A[i,k]=functions[k](x[i])/dy[i]
    
    
    
    Q,R=qr_gs_decomposition(A)
    R_inv=matrix(R.size1,R.size2)
    for i in range(R.size2-1,-1,-1):
        R_inv[i,i]=1/R[i,i]
        for h in range(i+1,R.size2):
            R_inv[i,h] /= R[i,i]
        for j in range(i-1,-1,-1):
            for l in range(i,R.size2):
                R_inv[j,i] -= R[j,i]*R_inv[i,l]
            
    
    C = multiply_matrix(multiply_matrix(R_inv,transpose_matrix(Q)),b)
    S = multiply_matrix(R_inv,transpose_matrix(R_inv))
    
    c = [C[i,0] for i in range(C.size1)]
    s = [S[i,i] for i in range(S.size1)]
    return c,s