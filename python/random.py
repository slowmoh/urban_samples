# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 18:52:11 2016

@author: Souzan
"""

import numpy
from matplotlib import pyplot

# Producing 10 random numbers between 0 to 90
n=numpy.random.randint(91, size=10)

print(n)
# Converting degree to radian and calculating sin and cos and storing the values in two different arrays named SIN & COS
sin=numpy.sin(n * numpy.pi / 180.)
cos=numpy.cos(n * numpy.pi / 180.)

print(sin)
print(cos)

# Create a figure of size 20*10 inches, 80 dots per inch
pyplot.figure(figsize=(20, 10), dpi=80)

# Create a new subplot from a grid of 1x1
pyplot.subplot(1, 1, 1)

# We want to draw sin and cos functions in the interval (-pi,pi)
X = numpy.linspace(-numpy.pi, numpy.pi, 256, endpoint=True)
C, S = numpy.cos(X), numpy.sin(X)

# Setting tick labels
pyplot.xticks([-numpy.pi, -numpy.pi/2, 0, numpy.pi/2, numpy.pi],
          [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

pyplot.yticks([-1, 0, +1],
          [r'$-1$', r'$0$', r'$+1$'])

# Moving spines to the middle
# gca stands for 'get current axis'
ax = pyplot.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data',0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data',0))

# Show result on screen
pyplot.plot(X, C, color="blue", linewidth=2.5, linestyle="-", label="cosine")
pyplot.plot(X, S, color="red",  linewidth=2.5, linestyle="-", label="sine")

pyplot.legend(loc='upper left')

# Annotating the 10 random numbers on the sin and cos functions
def fun(t):

    pyplot.plot([t, t], [0, numpy.cos(t)], color='blue', linewidth=2.5, linestyle="--")
    pyplot.scatter([t, ], [numpy.cos(t), ], 50, color='blue')

    pyplot.plot([t, t],[0, numpy.sin(t)], color='red', linewidth=2.5, linestyle="--")
    pyplot.scatter([t, ],[numpy.sin(t), ], 50, color='red')

for number in n:
    m=number * numpy.pi / 180.
    fun(m)

pyplot.show()