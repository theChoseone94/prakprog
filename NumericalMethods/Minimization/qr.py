import numpy as np
import math
import sympy as sy
from numpy import linalg


def qr_gs_decomposition(A):
    
    (n, m)=np.shape(A)
    R=np.zeros((n,m))
    Q=np.zeros((m,m))
        
    for j in range(m):
        v = A[:, j]
        for i in range(j):
            R[i, j] = np.dot(Q[:, i].T, A[:, j])
            v = v.squeeze() - (R[i, j]*Q[:, i])
        R[j, j] = np.linalg.norm(v)
        Q[:, j] = (v/R[j, j]).squeeze()
    return Q, R

def qr_gs_solve(Q, R, b):
    qb = np.dot(Q.T, b)
    n = len(qb)
    x = np.zeros(n)
    for i in reversed(range(n)):
        xi = qb[i]
        for j in range(i+1, n, 1):
            xi = xi - R[i, j]*x[j]
        x[i] = xi/R[i, i]
    return x

def qr_gs_inverse(A):
    (n, m) = np.shape(A)
    (Qq, Rr) = qr_gs_decomposition(A)
    B = np.eye(n)
    A_inv = np.zeros((n, n))
    i = 0
    for column in B:
        A_inv[:, i] = qr_gs_solve(Qq, Rr, column)
        i = i + 1
    return A_inv