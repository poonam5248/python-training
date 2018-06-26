#q6 Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18. The code must keep taking input till the user enters the appropriate age number(less than 18).

class AgeTooSmallError(Exception):
	pass
	
try:
	def ag():                                 #age func is defined
		num=int(input("enter your age"))      #age is input
		if num<18:
			print("you are too small")
			raise AgeTooSmallError("age too small exception")            #exception raised if age less than 18
			
		else:
			print("congo")
	ag()                               #func is called
except AgeTooSmallError as e:
	print(e)                          #depicts age too small error is occured
	ag()                               #if age less then 18 func called again after raising exception
else:
	print("no exception")              
	