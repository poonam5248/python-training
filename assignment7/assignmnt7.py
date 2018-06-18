#q1 create a function to calculate area of circle by taking radius as input from user.

pi=3.14
r=int(input("enter the radius"))
def area():
	z=pi*(r**2)
	print("area of circle is:",z,"sq. units")
area()

#q2  Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(n):
	sum=0
	for i in range(1,n):
		if n%i==0:
			sum=sum+i
	if sum==n:
		print(n,"is a perfect number")
for x in range(1,1001):
	perfect(x)

	
#q3 print multiplication table of 12 using recursion.

def mult(n,x):
	print(n*x)
	x=x+1
	if x<=10:
		mult(n,x)
mult(12,1)

#q4 Write a function to calculate power of a number raised to other ( a^b ) using recursion.

def power(a,b):
	if b==1:
		return a
	if b!=1:
		return(a*power(a,b-1))
a=int(input("enter the first number"))
b=int(input("enter the second number"))
print("result:",power(a,b))


#q5Write a function to find factorial of a number but also store the factorials calculated in a dictionary


def rec(x):
	if (x==1 or x==0):
		return 1
	else:
		f= x* rec(x-1)
		return f

d={}
for x in range(5):
	keys=int(input("enter the number"))
	fact=rec(keys)
	d[keys]=fact
print(d)

		
	



	

	
