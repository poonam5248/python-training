#q1  Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.
import math
class circle:
	
	
	def __init__(self,radius):
		self.radius=radius
	def getArea(self):
		area=math.pi*(self.radius**2)
		print(area)
		
	
	def getCircumference(self):
		crcm=2*(math.pi*self.radius)
		print(crcm)

c1= circle(7)
c1.getArea()


c2=circle(7)
c2.getCircumference()