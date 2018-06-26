#q3 # Program to depict Raising Exception
 
# try:
    # raise NameError("Hi there")  # Raise Error
# except NameError:
    # print "An exception"
    # raise  # To determine whether the exception was raised or not
	
	
#output
#1.no parenthesis after print....(error)
#2. raise in line 7 should raise NameError...


#solution

# Program to depict Raising Exception
 
try:
    raise NameError("Hi there")  # Raise Error
except NameError:
    print ("An exception")
    
	
#output= An exception