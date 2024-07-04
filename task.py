s=str(input("enter a string"))
print(s)
def paliandrome(s):
    if s== s[::-1]:
     print("yes")
    else:
     print("no")
paliandrome(s)

j=(input("enter a string"))
vowels=["a","e","o","i","u","A","E","O","I","U"]
count=0
for i in j:
  if i in vowels:
   count=count+1
print("the number of vowels in given sentence is:",count)   
  
