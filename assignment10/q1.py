#q1 Create a class Animal as a base class and define method animal_attribute. Create another class Tiger which is inheriting Animal and access the base class method.

class Animal:
	def __init__(self,species):
		self.species=species
		
	def animal_attribute(self):
		print("tiger is:",self.species)
class Tiger(Animal):
	def display(self):
		print("Tiger is our national animal.")
		
		
species=input("enter the species of tiger")

a=Tiger(species)
a.display()
a.animal_attribute()
