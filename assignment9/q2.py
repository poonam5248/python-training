#q2 Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.

class Student:
	def __init__(self,name,roll):
		self.name=name
		self.roll=roll
	def info(self):
		print(self.name,self.roll)
name=input("enter your name")	
roll=int(input("enter the roll number"))
	
s1=Student(name,roll)
s1.info()