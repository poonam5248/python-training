#q5  Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
 #Display expenditure and savings 
 #Calculate total salary
#Display salary


class Expenditure:
	def __init__(self,expenditure,savings):
		self.expenditure=expenditure
		self.savings=savings
	def display(self):
		print("expenditure:",self.expenditure)
		print("savings",self.savings)
	def totalsalary(self):
		salary=self.expenditure+self.savings
		print("total salary:",salary)

expenditure=int(input("enter your expenditure"))
savings=int(input("enter your savings"))
s1=Expenditure(expenditure,savings)
s1.display()
s1.totalsalary()