#q5  Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error


#1.import error

try:
	from foodie import *
except Exception:
	print("Import Error")

#here import error for module foodie...as no module exist
 
 
#2. value error

try:
	int("Gayatri")
except Exception:
	print("value error")
	
	
#3. Index error

try:
	l=[1,2,3]
	print(l[5])
except Exception:
	print("Index Error")