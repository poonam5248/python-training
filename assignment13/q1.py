#q1 Name and handle the exception occured in the following program:

# a=3
 # if a<4:
    # a=a/(a-3)
     # print(a)
	 
	 
#answer= it will give "Division By Zero" Exception.

#solution:

try:                               #try block throughs exception
	a=3
	if a<4:
		a=a/(a-3)
		print(a)
except Exception as e:             #except block handles it
	print("exception handled !")
	print(e)