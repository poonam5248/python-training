#q1 Write a Python program to read last n lines of a file.

f=open('new.txt','r',encoding="utf8")
content=f.readlines()
n=int(input("enter number of lines you want to read from last"))

while n>0:
    print(content[-n])
    n-=1

f.close()