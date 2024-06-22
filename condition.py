a=33
b=20
if a<b:
    print("hello")
else:
    print("hai")
c=int(input("enter a number"))        
if(c%2)==0:
    print("it is a even number")
else:
    print("it is a odd number")    
d=int(input("enter a number"))
if(d==1):
    print("not a prime")
elif(d<1):
    print("not a prime")        
else:
    for i in range(2,d):
        if(d%i)==0:
            print("not a prime")
            break
    else: print("prime number")


n1=[]
for i in range(1000,2000):
    if(i%7==0) and (i%5==0):
        n1.append(i)
print(n1)        

student=["nihadh","nihal","nihan"]
for i in student:
    if i not in student:
        print("absent")
    else:
        print("present")    
        


 

    