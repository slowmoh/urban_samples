# -*- coding: utf-8 -*-
"""
Created on Fri Nov 18 18:57:00 2016

@author: Ben
"""

text = 'Sample Text to Save\nNew Line!'

saveFile = open('exampleFile.txt', 'w')
saveFile.write(text)
saveFile.close()