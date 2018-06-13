#q1wap to create tuple with different data types 1=find length of each tuple

t=(1,2,3)
t1=(2.3,4)
t2=('a','b','c','d')
print(len(t))
print(len(t1))
print(len(t2))

#q2 find largest and smallest elements of tuples

t=(1,2,45,43)
print(max(t))
print(min(t))

#q3 wap to find product of all elements of tuple
t=(2,4,6,7)
z= t[0]*t[1]*t[2]*t[3]
print(z)

#q4 create two sets using user defined values
#1 cal diff bw two sets
#2 compare two sets
#3 print the result of intersection of two sets

x=int(input("enter any value:"))
y=int(input("enter any value:"))
z=int(input("enter any value:"))
p=int(input("enter any value:"))
s1=set([x,y,z,p])
a=int(input("enter any value:"))
b=int(input("enter any value:"))
c=int(input("enter any value:"))
d=int(input("enter any value:"))
s2=set([a,b,c,d])
print (s1-s2)
print(s1&s2)





