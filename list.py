fruits=["mango","apple","orange"]
print(fruits)
print(type(fruits))
print(len(fruits))
print(fruits[2])
print(fruits[-1])
fruits[1]="cherry"
print(fruits)
fruits[1:3]=["kiwi","apple"]
print(fruits)
fruits.insert(2,"watermelon")
print(fruits)
fruits.append("cherry")   
print(fruits)
num=[1,2,3,4,5]
fruits.extend(num)
print(fruits)
fruits.remove("watermelon")
print(fruits)
fruits.pop(5)
print(fruits)
fruits.clear()
print(fruits)
#del fruits
#print(fruits)
num1=[8,3,6,10]
num1.sort()
print(num1)
num1.sort(reverse=True)
print(num1)
num2=num1.copy()
print(num2)
num3=[1,1,1,4,5,6,8,]
print(num3)
vegitables=["potato","tomato","cucumber"]
for i in vegitables:                 
    print(i)
for i in "banana":
    print(i)
for i in range(2,6):
    print(i)      
    