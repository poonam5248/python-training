#q3 Make a list that has 5 elements.Create a threading process that prints the 5 elements of the list with a delay of multiple of 2 sec between each display.
#Delay goes like 2sec-4sec-6sec-8sec-10sec


import threading
from threading import Thread
import time

l=[]
print("enter the numbers:")
for x in range(5):
	l.append(int(input()))
print(l)              #list of 5 elements is printed

def display():
	bt=time.time()     #beginning time is started
	time.sleep(2)       #for first element delay of 2 sec 
	i=2
	for x in l:
		print(x)
		et=time.time()    #ending time for each element
		print("time taken",et-bt)   #total time taken to display every element
		time.sleep(i)             #each time sleep value is incremented by 2
		i=i+2
				
t=Thread(target=display)      #thread is made
t.start()