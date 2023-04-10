# -*- coding: utf-8 -*-
from math import*
import numpy as np
import matplotlib.pyplot as plt
x = [0.01]
v= [0]
t = [0]
h = 1e-3


for i in range(0,10000):
    x.append(x[i]+h*v[i])
    v.append((1-h)*v[i]-100*h*x[i-1]+h*cos(10*i*h))
    t.append(i*h)

a = np.array(x)
c = np.array(v)
temp = np.array(t)

energie_cinetique= np.array(t)
energie_potentielle= 10*9.81*a
energie_cinetique = 0.5*10*(c**2)
energie_totale = energie_cinetique + energie_potentielle
plt.plot(temp,energie_potentielle, color = 'pink' )
plt.plot(temp,energie_cinetique, color = 'red' )
plt.plot(temp, energie_totale, color = 'orange')
plt.show()
