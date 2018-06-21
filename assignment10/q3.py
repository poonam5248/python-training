#q3 Create a class Cop. Initialize its name, age , work experience and designation. Define methods to add, display and update the following details. Create another class Mission which extends the class Cop. Define method add_mission _details. Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.

class Cop:

	def __init__(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation
	
		
	def display(self):
		print("Details:")
		print(self.name)
		print(self.age)
		print(self.work_experience)
		print(self.designation)
		
	def update(self,name,age,work_experience,designation):
		self.name=name
		self.age=age
		self.work_experience=work_experience
		self.designation=designation

class Mission(Cop):
	fighter_planes=10
	tankers=3
	def add_mission_details(self):
		print("number of fighter planes:",self.fighter_planes)
		print("number of tankers:",self.tankers)
		
		
name=input("Name:")
age=int(input("Age:"))
work_experience=input("Work Experience:")
designation=input("Designation:")

a=Mission(name,age,work_experience,designation)
print("")
a.display()
print("")
a.add_mission_details()
print("")
a.update(input("Name:"),int(input("Age:")),input("Work Experience:"),input("Designation:"))
print("")
a.display()