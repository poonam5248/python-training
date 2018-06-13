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



