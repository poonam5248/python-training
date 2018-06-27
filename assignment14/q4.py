#q4  Write a Python program to combine each line from first file with the corresponding line in second file.

with open('new.txt',encoding="utf8")as f1,open('abc.txt',encoding="utf8")as f2:
    for line1,line2 in zip(f1,f2):
        print(line1+line2)