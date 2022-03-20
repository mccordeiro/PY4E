#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 13 12:08:26 2022

@author: claracordeiro
"""

#Conditional Execution
#conditional vs. sequential code: conditional requires multiple lines of text and decision making, while sequential is just one line 
#Requires python to make choices on the path which you create 
#if statement is a reserved word that tells python how to make decisions 
#depending on what's being asks, the question inside the indent will or will not execute 
#indents are important to indicate a conditionally executed block - will run sequentially 
#to end a block of code, you should de-indent 
#you can also have multiple indentations, blocks within blocks are nested blocks generally used for looped codes

x = 5 
if x < 10:
    print('smaller')
if x > 20: 
    print('bigger')
print('Finis')
#comparison operators look at variables but do not change the variables 
#they evaluate or return us a false 
#boolean expressions ask a question and produce a yes or no result which we use to control program flow 
#boolean expressions using comparison operators to evaluate to treu/false or yes/no 
x = 42
if x > 1: 
    print ('more than one')
    if x < 100:
        print('less than one')
print('all done')
#%%
#one-way vs. two-way decisions 
#two-way decision are like a fork in the road, we must choose one path or the other path but not both 
#sometimes we want to do one thing if a logical expression is true and something else if the expression is false 
#"if tests" 
x = 4 
if x > 2: 
    print('bigger')
else: 
    print('smaller')
print ('all done')
#%%
#conditional execution patterns 
#blocks should always have an entry and an exit point 
#multi-way statement uses the elif statement 
#as soon as one elif is "triggered" within a box, the statement will stop exection
x = 0 
if x < 2: 
    print('small')
elif x < 10: 
    print('medium')
else: 
    print ('large')
print('all done')

x = 5 
if x < 2: 
    print('small')
elif x < 10: 
    print('medium')
else: 
    print ('large')
print('all done')

x = 20
if x < 2: 
    print('small')
elif x < 10: 
    print('medium')
else: 
    print ('large')
print('all done')
#%%
#try and accept structure
#you hve a bit of code that you know might fail, this eliminates or catches a traceback 
#surround a dangerous section of code with try and except 
#if the code in the try works, the except is skipped
#if the code in the try fails, it jumps to the except section
#should use one line or minimal lines in order to isolate the error
#the code below assigns the variable istr to equal -1 
astr = 'Hello Bob'
istr = 0 
try: 
    istr = int(astr)
except: 
    istr = -1 
print(istr)
#%%
#this code does not execute from line 1 becuase invalid literal for int() with base 10: 'Hello Bob'
str = 'Hello Bob'
istr = int(astr)
print('First', istr)
astr = '123'
istr = int(astr) 
print('Second', istr)
#%% 
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
#%%
#3.3 Write a program to prompt for a score between 0.0 and 1.0. 
#If the score is out of range, print an error. 
#If the score is between 0.0 and 1.0, print a grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#If the user enters a value out of range, print a suitable error message and exit. 
#For the test, enter a score of 0.85.
try:
    score = input("Enter Score:")
    finalscore = float (score)
    if finalscore >= 0.9:
        print('A')
    elif finalscore >= .08:
        print('B')
    elif finalscore >= .07:
        print('C')
    elif finalscore >= .06: 
        print('D') 
    elif finalscore < .06:
        print('F')
except: 
    print ('enter a valid numeric value')