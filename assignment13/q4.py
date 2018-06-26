#q4 What will be the output of the following code:

 # Function which returns a/b
# def AbyB(a , b):
	# try:
		# c = ((a+b) / (a-b))
	# except ZeroDivisionError:
		# print "a/b result in 0"
	# else:
		# print c

# Driver program to test above function
# AbyB(2.0, 3.0)
# AbyB(3.0, 3.0)

#answer= error due to no parenthesis after print statements.

#correct code


 # Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print ("a/b result in 0")
	else:
		print (c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#output= -5.0
		  #a/b result in 0
