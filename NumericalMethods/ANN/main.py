import numpy as np
import ANN as ann
import matplotlib.pyplot as plt



def Gauss_wave(x):
    return x*np.exp(-x**2)

def wavelet(x):
    return np.cos(5*x)*np.exp(-x**2)

print('I will used the Gaussian wavelet given in the assignment and')
print('10 neurons.')
neurons=10
ann=ann.ANN(Gauss_wave,neurons)

x = np.linspace(-2,2,100)
wave = wavelet(x)

print('Interpolating function..')
ann.training(x,wave)
print('Feeding forward..')
y = ann.forward(x)
print('The fit to the function can be seen in ANN.pdf, while the results')
print('can be seen beneath.')

print('\n')
print('Results')

print('x \t y \t gaussian')
[print(f'{x[i]:.16}\t{y[i]:.16}\t{wave[i]:.16}') for i in range(len(x))]


plt.figure()
plt.plot(x,y,'r.',label='ANN fit')
plt.plot(x,wavelet(x),'k-',label='Gaussian function')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.title('Artificial neural Network on a gaussian function')
plt.savefig('ANN.pdf')