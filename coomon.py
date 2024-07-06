a=[1,2,3,6,8]
b=[8,2,10,4,90]
def common(a,b):
    for i in a:
        for j in b:
            if i==j:  
                result=True
                return result           
print(common(a,b))            
            
