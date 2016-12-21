# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 20:33:09 2016

@author: Ben

Just a simple attempt to get a progress bar
"""
import time
import sys

def progress(curr, end):
    sys.stdout.write("\rDoing thing " + str(curr) + " out of " + str(end))
    sys.stdout.flush()
    sys.stdout.write("\rDoing thing ")
    sys.stdout.flush()


def progressBar(value, endvalue, bar_length=50):
        percent = float(value) / endvalue
        arrow = '#' * int(round(percent * bar_length))
        spaces = ' ' * (bar_length - len(arrow))

        sys.stdout.write("\rItem " + str(value) + " out of " + str(endvalue) +"|| Progress: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
        sys.stdout.flush()


def testBar():        
    print("hello World")
    size = 500
    i = 1
    for i in range(size):
        progressBar(i, size-1)
        time.sleep(0.3)
 
# uncomment testBar() to run a function       
testBar()
    