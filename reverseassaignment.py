s="hello welcome to home"
print(s)
#print(str.split(","))
#words=str[-1::-1]
#Print(words)
l=s.split()[::-1]
k=[]
for i in l:
    k.append(i)
print(" ".join(k))

