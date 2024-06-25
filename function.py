def my_function():
    print("hello world")
my_function()


def my_name(fname):
    print("hello"+" "+fname)
my_name("nihadh")
my_name("nihal")


def my_names(fname,lname):
    print(fname+" "+lname)
my_names("nihadh","abdulla")


def my_argiritatry(*kid):
    print("the youngest one"+" "+kid[2])
my_argiritatry("nihad","nihal","abdulla")  



def my_keyword(child1,child2,child3):
    print("the youngest one"+" "+child2)
my_keyword(child1="nihadh",child2="subaida",child3="abdulla")



def my_argiritatrykeyword(**school):
    print("start name is"+" "+school["fname"]+school["lname"])
my_argiritatrykeyword(fname="futura",lname="labs")    


words=int(input("enter a number"))
print(words)
def oddeven(n):
    if(n%2==0):
        print("even number")
    else:
        print("odd number")    
oddeven(words)      


number=int(input("enter a number"))
print(number)
def prime_number(d):
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
prime_number(number)    
