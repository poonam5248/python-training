#q3 Split the following irregular sentence into words
#sentence = "A, very very; irregular_sentence"
#desired_output = "A very very irregular sentence"
import re
sentence = "A, very very; irregular_sentence"

# p = re.compile(r"[^,;_]")
# result=p.finditer(sentence)
# for r in result:
#     print(r)

p=re.sub(",|;","","A, very very; irregular_sentence")
p=re.sub(r"_"," ",p)
print(p)