# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 19:03:06 2016
Just print a sinus plot
@author: Ben
"""
import numpy as np
import matplotlib.pylab as plt

y = [1,2,3]
x = np.linspace(-np.pi, np.pi, 200)
plt.plot(x, np.sin(x))
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

