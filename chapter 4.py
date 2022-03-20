#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 22:01:17 2022

@author: claracordeiro
"""
#chapter 4 
#store and reuse functions 
#DRY - don't repeat yourself 
#def = start the definition of a function, defines a function 
def thing ():
    print ('Hello')
    print ('Fun')
thing ()

print ('Zip')
thing()

#max function finds the largest item in a line 
#a chunk of code that reads the lines and returns something 
#min does the same thing for smallest items 
#when you put an integer and a floating point in an expression, the integer is implicity converted to a float 
#you can control this with teh built-in fucntions int() and float()

print float(99) / 100 
#this should be 0.99
i = 42 
type (i)
f = float (i)
print(f)
type(f)
print(1 + 2 * float(3) / 4 - 5)

#%%
#you can also use int() and float () to convert between strings and integers 
#you will get an error if the string does not contain numeric characters 

sval = '123'
type(sval)
print(sval + 1)
ival = int(sval)
type(ival)
print(ival + 1) 
nsv = 'hello bob'
niv = int(nsv)
#this will not work because its not the correct data type 