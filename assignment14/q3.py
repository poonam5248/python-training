#q3 Write a Python program to copy the contents of a file to another file

with open('new.txt','r',encoding="utf8") as f1:
    with open('abc.txt','w',encoding="utf8")as f2:
        for line in f1:
            f2.write(line)