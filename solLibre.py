
from matplotlib import pyplot as plt
from scipy.integrate import odeint
import numpy as np

def f(u,x):
    return (u[1],-2*u[1]-400*u[0])

x0 = [0.01,0]

xs = np.linspace(1,10,400)
us = odeint(f,x0,xs)
ys =us[:,0]




plt.plot(xs,ys,'-')
plt.plot(xs,ys,'r*')

plt.show()
