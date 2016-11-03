import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as integrate

def F(y,x):
    theta = y[0]
    omega = y[1]
    return [
        omega,
        -np.sin(theta)]

X = np.linspace(0, 25, 2000)
Y = integrate.odeint(F, [0.4,0], X)
plt.plot(X,Y)
plt.grid()
plt.show()