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

#%%
#how to build your own functions 
#We create a new function using the def keyword followed by oprtional parameters in parantheses
#this defines te function, but does not execute the body of the function
#it remembers the code and we can later call and invoke the function 
#an argument is a value we pass into the function as its inout, when we call a function 
#we use arguments so we can direct the function to do different kinds of work when we call it at different times 
#we can put the arguments in parentheses adter the name of the function
#Paramters
#A parameter is a vairable which we use in the function defintion
#It is a handle that allows the code in the function to access the arguments for a partiular function invocation
def greet(lang):
    if lang == 'es':
        print ('Hola')
    elif lang == 'fr':
        print ('Bonjour')
    else:
        print ('Hello')
#lang is the first parameter - it is the "alias" 
#when we call "greet" later, it will invoke the "lang" parameter since that is what we defined it as 
greet ('en')
greet ('es')
greet ('fr')

#Return Values 
#Often a fucntion will take its arguments, do some computation, and return a value to be used as the vakye if the function call in the calling expression
#the return keyword is used for this 
#Return has two primary functions 1) stops the function and jumps to next line and 2) determines residual value 
def greet ():
    return "Hello"
print (greet(), "Glenn")
print (greet(), "Sally")
#a fruitful function is one that produces a result (i.e., returns a value)
#the return statement ends the function execution and sends back the result of the function 

def greet(lang):
    if lang == 'es':
        return ('Hola')
    elif lang == 'fr':
        return ('Bonjour')
    else:
        return ('Hello')
print (greet('en'), 'Clara')
print (greet('fr'), 'Clara')
print (greet('es'), 'Clara')

def addtwo(a, b):
    added = a + b 
    return a 

x = addtwo(2, 7)
print(x)

#%%
#Activity 4.6
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay should be the normal rate for hours up to 40 and time-and-a-half for the hourly rate for all hours worked above 40 hours. 
#Put the logic to do the computation of pay in a function called computepay() and use the function to do the computation. 
#The function should return a value. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number.
#Do not worry about error checking the user input unless you want to - you can assume the user types numbers properly. 
#Do not name your variable sum or use the sum() function.
def computepay(h, r):
    return 42.37

hrs = input("Enter Hours:")

p = computepay(10, 20)
print("Pay", p)

#Activity 3.1 
#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). 
#You should use input to read a string and float() to convert the string to a number. 
#Do not worry about error checking the user input - assume the user types numbers properly.
sh = input("Enter Hours:")
sr = input ("Enter Rate:")
fh = float(sh)
fr = float (sr)
if fh > 40: 
    reg = fr * fh 
    otp = (fh - 40.0) * (fr * 0.5)
    xp = reg + otp
else: 
    xp = fh * fr 
print("Pay:",xp)






