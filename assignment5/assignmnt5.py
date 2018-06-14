#q1 to check leap year or not.

leapyear = int(input("enter any value"))
if leapyear%4==0 and leapyear%100!=0:
    print("its a leap year") 
elif leapyear%400==0:
    print("its a leap year")
else:
    print("its not a leap year")		
	
#q2 take dimensions length and breadth input from user and check whether they are of square or reactangle.

length= int(input("enter the length"))
breadth= int(input("enter the breadth"))

if length==breadth:
    print("its a square")
else:
    print("its a rectangle")
	
	
	
	
#q3 take the input age of 3 people and determine oldest and youngest from them.

age1 = int(input("kindly enter your age"))
age2 = int(input("kindly enter your age"))
age3 = int(input("kindly enter your age"))
t=(age1,age2,age3)
print("youngest:",min(t))
t=(age1,age2,age3)
print("oldest:",max(t))  
	
	
	
	
#q4 prize won or not.

x = int(input("enter your scores"))
if x<=1 and x<=50:
	print("sorry! no prize this time.")
elif x>=51 and x<=150:
	print("congratulations! you won a wooden dog!")
elif x>=151 and x<=180:
    print("congratulations! you won a book!")
elif x>=181 and x<=200:
    print("congratulations! you won chocolates!")
else:
    print("sorry! no prize this time.")
	
	
	
#q5 judge discount and total cost for user.

x = int(input("enter the number of units please ."))
y = x*100
print(y)
if y>1000:
    cost = y-(y*(10/100))
    print("total purchase:",cost)
else:
    cost = y 
    print("total purchase:",cost)

