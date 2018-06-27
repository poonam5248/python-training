#q2 Write a Python program to count the frequency of words in a file.

# f=open('new.txt','r',encoding="utf8")
# w=input('enter the word you want to search')
# x=f.read()
# c=0
# for w in x:
#     if w==x:
#         c=c+1
#         print(c)

from collections import Counter
def word_count(fname,encoding="utf8"):
        with open(fname,encoding="utf8") as f:
                return Counter(f.read().split())

print("Frequency of words in the file :",word_count("new.txt",encoding="utf8"))

