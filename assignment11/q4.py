#q4 Call factorial function using thread.

import threading
from threading import Thread
import time
import math

def func():
	n=int(input("enter the number:"))       #number is inputed
	a=math.factorial(n)        #factorial is calculated
	print("factorial is:",a)
	
	
t=Thread(target=func)
t.start()