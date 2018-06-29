#q1 Extract the user id, domain name and suffix from the following email addresses.
#emails = "zuck26@facebook.com" "page33@google.com"
#"jeff42@amazon.com"
#desired_output = [('zuck26', 'facebook', 'com'), ('page33', 'google', 'com'), ('jeff42', 'amazon', 'com')]

import re

s= " zuck26@facebook.com page33@google.com jeff42@amazon.com"
p=re.compile(r"(.*)@(.*).(...) (.*)@(.*).(...) (.*)@(.*).(...)")

result=p.match(s)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))
# print(result.group(8))
# print(result.group(9))

a=tuple([result.group(1),result.group(2),result.group(3)])
b=tuple([result.group(4),result.group(5),result.group(6)])
c=tuple([result.group(7),result.group(8),result.group(9)])

l=[]
l.append(a)
l.append(b)
l.append(c)
print(l)

