#q2 Retrieve all the words starting with ‘b’ or ‘B’ from the following text.


import re
# s = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
#
# p= re.compile(r"b[i]t")
# result=p.finditer(s)
# for r in result:
#     print(r)
# a=re.compile(r"b[a-z][a-z][a-z][a-z][a-z]")
# file=a.finditer(s)
# for r in file:
#     print(r)
# b=re.compile(r"B[a-z][a-z][a-z]y")
# arr=b.finditer(s)
# for r in arr:
#     print(r)
# p= re.compile(r"B[u]t")
# result=p.finditer(s)
# for r in result:
#     print(r)

# p=re.compile(r"(.*)(.*)a(.*)of(.*),(.*)the(.*)was so (.*),So she (.*)some(.*)(.*),To make the(.*)(.*)(.*)")
#
# result=p.match(s)
# print(result.group(1))
# print(result.group(2))
# print(result.group(3))
# print(result.group(4))
# print(result.group(5))
# print(result.group(6))
# print(result.group(7))
# print(result.group(8))
# print(result.group(9))
# print(result.group(10))
# print(result.group(11))
# print(result.group(12))
# print(result.group(13))


s = 'Bettey bought a bit of butter but the butter was bitter so she bought some more butter to make bitter butter better'

p = re.compile(r"\b[Bb]\w+")

result = p.findall(s)

for r in result:
    print(r)