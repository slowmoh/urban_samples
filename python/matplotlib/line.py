# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 15:19:17 2016
Tutorial: https://www.youtube.com/watch?v=q7Bo_J8x_dw&index=1&list=PLQVvvaa0QuDfefDfXb9Yf0la1fPDKluPF
@author: Ben
"""
import matplotlib.pyplot as plt


"""plot([x1,x2,x3], [y1,y2,y3]) """
x = [1,2,3]
y = [5,7,4]
x2 = [1,2,3]
y2 = [10,14,12]
x3 = [2,2,2]
y3 = [0,1,2]

plt.plot(x,y, label='First line')
plt.plot(x2,y2, label='second line')
plt.plot(x3, y3)
""" Just labeling the axis """
plt.xlabel('Plot Number')
plt.ylabel('Important var')
plt.title('Interesting graph\nCheck it out')
plt.legend()
plt.show()
