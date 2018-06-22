#q1 Create a threading process such that it sleeps for 5 seconds and then prints out a message.

import threading
from threading import Thread
import time

class MyThread(Thread):
	def run(self):
		print("child thread:",threading.current_thread().getName(),threading.current_thread().ident)
		bt=time.time()        #cal beginning time
		time.sleep(5)
		et=time.time()         #cal ending time
		print("execution is completed in:",et-bt)     #it shows i have taken sleep of 5 sec after executing my child thread
		
t=MyThread()      #t is object made of mythread class
t.start()          #t calls start() and start automatically calls run()
		