
#q1=
x=int(input("enter any value:"))
y=int(input("enter any value:"))
z=int(input("enter any value:"))
p=int(input("enter any value:"))
l=[x,y,z,p]
print(l)

#q2
l=[x,y,z,p]
g=["google","apple","facebook","microsoft","tesla"]
print(l.extend(g))
print(l)

#q3
l=[x,y,z,p]
print(l.count(4))

#q4
#method1
l=[x,y,z,p]
l.sort()
print(l)

#method2
l=[x,y,z,p]
print(l.sort())
print(l)


#q5
A=[1,6,3]
B=[2,4,1]
A.sort()
B.sort()
print(A)
print(B)
print(A.extend(B))
print(A)
A.sort()
print(A)
C=A
print(C)



#q6 stack queue

l=[1,2,3,4]
print(l)
print(l.pop())
print(l)
l.append(5)
print(l)
#it will delete last element 4 of list.. so last in first out principle of stck is used.

l1=[1,2,3,4]
print(l1)
l1.reverse()
print(l1)
print(l1.pop())

#it will delete 1 element of list..so first in first out principle of queue is used.











#q7 even odd


l=[1,2,3,44,75,98]
even_count=0
odd_count=0
for i in l:
  if i%2==0:
    even_count= even_count+1
  else:
    odd_count= odd_count+1
print("even numbers:" ,even_count)
print("odd numbers:",odd_count)