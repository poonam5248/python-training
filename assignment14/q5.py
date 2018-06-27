#q5 Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
import random
f=open('num.txt','w')

for i in range(10):
    x=str(random.randint(1,50))
    f.write(x)
    f.write("\n")
    print(x)
f.close()

f=open('num.txt','r')

l=f.readlines()
print(l)
l.sort()
print(l)

with open('abc.txt','w')as f2:      #to write sorted list in another file
    for n in l:
        f2.write(n)
        f2.write("\n")


f.close()
f2.close()

