#q2 Make a thread that prints numbers from 1-10, waits for 1 sec between.

import threading
from threading import Thread
import time

def show():
	for x in range(1,11):
		time.sleep(1)
		print(x)           #numbers from 1-10 are printed
		
t=Thread(target=show)
t.start()