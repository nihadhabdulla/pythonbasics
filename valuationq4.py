a=int(input("enter a number"))
if(a==1):
    print("false")
elif(a<1):
    print("false")
else:
    for i in range(2,a):
      if(a%2)==0:
        print("false")
        break
    else:
       print("true")  
