#q4 Create a class Shape.Initialize it with length and breadth Create the method Area. Create class rectangle and square which inherits shape and access the method Area.

class Shape:
	def __init__(self,length,breadth):
		self.length=length
		self.breadth=breadth
		
		
	def area(self):
		self.result=self.length*self.breadth
		
		
class Rectangle(Shape):
	def arearect(self):
		print("area of rectangle:",self.result)
		
class Square(Shape):
	def areasq(self):
		print("area of square:",self.result)
		
		
length=int(input("enter the length:"))
breadth=int(input("enter the breadth:"))
c=Rectangle(length,breadth)
b=Square(length,breadth)
if length==breadth:
	b.area()
	b.areasq()
else:
	c.area()
	c.arearect()
	
			
		
