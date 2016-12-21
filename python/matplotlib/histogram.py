# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:12:38 2016

@author: Ben
"""

import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt




def plotHistogram2(values, keys):
    # Counter data, counter is your counter object
    keys = counter.keys()
    y_pos = np.arange(len(keys))
    # get the counts for each key, assuming the values are numerical
    performance = [counter[k] for k in keys]
    # not sure if you want this :S
    error = np.random.rand(len(keys))
    
    plt.bar(y_pos, performance, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, keys)
    plt.xlabel('Counts per key')
    plt.title('How fast do you want to go today?')
    
    plt.show()