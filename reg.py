import re
x="hi frends am nihadh"
y=re.search("^hi.*nihadh$",x)
if x:
    print("yes")
else:
    print("no")

z=re.findall("am",x)
print(z)       

a=re.split("\s",x)
print(a)

b=re.sub("\s","9",x)
print(b)

c=re.findall("\Ahi",x)
print(c)