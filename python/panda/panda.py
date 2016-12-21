# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 21:04:12 2016

@author: Ben


HAving fun with panda
"""
from __future__ import print_function
import pandas as pd
import sys  
import h5py
import numpy as np


 


store = pd.HDFStore('store2.h5')#read .h5 file
df1=store['df1'] 
df2=store['df2'] 


print("\n\nstrt: df1")
#print(df1)

print("\n\nstrt: df2")
#print(df2)

'''

print("Select column 'name' ")
print(df1['name']) # select column "name"
print(df1.name) # select column "name"

print("\nSelect row with id equals 9")
print(df1.loc[9]) #select row with id equals 9 

print("\nselect rows from 6th to 9th (first row is 0) ")
print(df1[5:10]) #select rows from 6th to 9th (first row is 0) 
print("\n#select outlinks of article with id=0")
print(df2.loc[0].out_links) #select outlinks of article with id=0 

print('\n#show all columns where column "name" equals "Germany"')
#show all columns where column "name" equals "Germany"
print(df2[df2.name=="Germany"])

print('\nshow column out_links for rows where name is from list ["Germany","Austria"]')
#show column out_links for rows where name is from list ["Germany","Austria"]
print(df2[df2.name.isin(["Germany","Austria"])].out_links )


print('\n#show all columns where column "text" contains word "good"')
#show all columns where column "text" contains word "good" 
print(df1[df1.text.str.contains("good")])



'''
#print('\n##add word "city" to the beginning of each text value (IT IS ONLY SHOWS RESULT OF OPERATION, see explanation below!)"')
#add word "city" to the beginning of each text value 
#(IT IS ONLY SHOWS RESULT OF OPERATION, see explanation below!)
#print(df1.text.apply(lambda x: "city "+x))


#print(df1.text)

#make all text lower case and split text by spaces

#df1[["text"]]=df1.text.str.lower().str.split()

def do_sth(x):
	#here is your function
	#
	#
	return x
  

#apply do_sth function to text column 
#Iit will not change column itself, it will only show the result of aplication
print('\napply do_sth function to text column Iit will not change column itself, it will only show the result of aplication')	
#print(df1.text.apply(do_sth()))

#you always have to assign result to , e.g., column, 
#in order it affects your data.
#Some functions indeed can change the DataFrame by 
#applying them with argument inplace=True
#df1[["text"]]=df1.text.apply(do_sth())  

#delete column "text"
df1.drop('text', axis=1, inplace=True)
