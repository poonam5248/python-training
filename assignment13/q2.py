#q2 Name and handle the exception occurred in the following program:

 
# l=[1,2,3]
# print(l[3])

#answer="IndexError"   index value 3 is out of range of given list.


#solution:

try: 
	l=[1,2,3]
	print(l[3])
	
except Exception as e:
	print("exception handled !")
	print (e)