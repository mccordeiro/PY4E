# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
#PY4E Section 2 - Chapter 3 
#%% Activity 2.2 
#using the input function
name = input ("Enter your name")
print ("Hello", name)

#%% Activity 2.3
#input, float and print are all functions. 
#functions are a named section of code that perform specific functions 
#variable is named place in the memory where a programmer can store data and later retriee the data using variable "name"
#we assign a value to a variable using the assignment statement = 
#an assignment statement consists of an expression on the right-hand side and a variable to store the result
#there are three main types of data in Python: Integers, floating point numbers and strings 
#integers are whole numbers 
#floating point numbers have decimal points 
#We can ask Python what type something is by using the type() function
#When you put an integer and floating point in an expression, the integer is implicitly converted to a float
#You can control this with the built-in functions int() and float()
#You can also use int() and float() to convert between strings and integers
#You will get an error if the string does not contain numeric characters

#THE INPUT FUNCTION 
#We can instruct Python to pause and read data from the user using the input()  function
#The input()  function returns a string

#Write a program to prompt the user for hours and rate per hour using input to compute gross pay. 
#Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25). 
#You should use input to read a string and float() to convert the string to a number.
#input function will create a prompt to enter the hours and pay rate 
#the variable "hours" is relative to how many hours one works,, the vairable "rate" is relative to the hourly rate of pay
hours = input("Enter Hours: ")
rate = input("Enter Rate: ")

#THE FLOAT FUNCTION
#If we want to read a number from the user, we must convert it from a string to a number using a type conversion function
#the float() function transforms an integer or string into a floating point 
#the above code creates strings 
#the variable "pay" multiplies hours and rate, while the function float() trasnforms strings to flaoting values in one step 
pay = float(hours) * float(rate)
#the function print () will iterate whatever variable is specific within the parentheses 
#the f() function allows us to add the variable with desired text in one step 
#alternatively, the code print('Pay:', pay) would return the same value
print (f'Pay: {pay}')
