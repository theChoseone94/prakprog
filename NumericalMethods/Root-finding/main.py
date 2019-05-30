import math
import numpy as np
from newton import *
from functions import system_eq, Rosenbrock, Himmelblau, system_eq_Jacob,Rosenbrock_Jacob,Himmelblau_Jacob
from qr import *


#################################################################################
print('Problem A: solve a system of eqs., the rosenbrock and the Himmelblau eq.')
print('using the newtonian method with analytic Jacobian')
dx=1e-5
eps=0.0001
print('\n')  
print('The system of equations')
x_sys=[-1.0,12.0]
x_sys_solved=newtonian(system_eq,x_sys,dx,eps)
print('x is', x_sys_solved)
print('f(x) is',system_eq(x_sys_solved))
print('\n')
    
#print('The Rosenbrock')
print('The Rosenbrock function')
x_ros=[-2.0,2.0]
x_ros_solved=newtonian(Rosenbrock,x_ros,dx,eps)  
print('x is',x_ros_solved)
print('f(x) is',Rosenbrock(x_ros_solved))
print('\n')
  
#print('The Himmelblau')
print('The Himmelblau function')
x_him=[-3.0,3.0]
x_him_solved=newtonian(Himmelblau,x_him,dx,eps)
print('x is',x_him_solved)
print('f(x) is',Himmelblau(x_him_solved))
print('\n')
##################################################################################
print('Problem B: solve a system of eqs., the rosenbrock and the Himmelblau eq.')
print('using the newtonian method with numerical Jacobian')
print('\n')

print('System of equations')
x_sys_J=[-1,12.0]
x_sys_J_solved=newtonian_With_jacobian(system_eq_Jacob,x_sys_J,eps)
print('x is',x_sys_J_solved)
print('f(x) is',system_eq(x_sys_J_solved))
print('\n')

print('The Rosenbrock function')
x_ros_J=[-2.0,2.0]
x_ros_J_solved=newtonian_With_jacobian(Rosenbrock_Jacob,x_ros_J,eps)
print('x is',x_ros_J_solved)
print('f(x) is', Rosenbrock(x_ros_J_solved))
print('\n')
print('The Himmelblau function')
x_him_J=[-3.0,3.0]
x_him_J_solved=newtonian_With_jacobian(Himmelblau_Jacob,x_him_J,eps)
print('x is',x_him_J_solved)
print('f(x) is',Himmelblau(x_him_J_solved))

print('\n')
print('It can be seen that the two ways are similar in # of iterations')
print('but the value of f(x) is in general smaller with the numerical Jacobian')
print('than with the analytical Jacobian')


