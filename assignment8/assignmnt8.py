#q1 What is Time Tuple?

#method1
import time

print(time.gmtime(0))

#method2
import time

print(time.localtime(0))
 
#here the output is in the form of a struct_time which is equivalent to time tuple having 9 time attributes.


#q2  Write a program to get formatted time.

import time;

localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)

#the current local time is printed in a most readable format.


#q3 Extract month from the time.

from datetime import datetime

now=datetime.now()

print("month:",now.strftime("%B"))


#q4 Extract day from the time.


from datetime import datetime

now=datetime.now()

print("day:",now.strftime("%A"))



#q5 Extract date (ex : 11 in 11/01/2021) from the time.


import datetime

d= datetime.date.today()
print(d)
print(d.day)


#q6 Write a program to print time using localtime method.

import time

print(time.asctime(time.localtime()))


#q7 Find the factorial of a number input by user using math package functions.

import math

n=int(input("enter the number whose factorial you want to calculate:"))

print("answer is:",math.factorial(n))


#q8 Find the GCD of a number input by user using math package functions.

import math

n=int(input("enter the first number:"))
p=int(input("enter the second number:"))

print("result:",math.gcd(n,p))


#q9 Use OS package and do the following tasks: 
#1. Get current working directory.
#2. Get the user environment.

import os

print("current working directory:",os.getcwd())
print("environment variables are:",os.environ)


