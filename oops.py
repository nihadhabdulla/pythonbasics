class my_class:
    x=5
p1=my_class()
print(p1.x)


class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
p2=person("nihadh",24)
print(p2.name)
print(p2.age) 

#inherittance
class parent:
    def __init__(self,firstname,lastname):
        self.firstname=firstname
        self.lastname=lastname
    def print_name(self):
        print(self.firstname)
        print(self.lastname)
p3=parent("abdulla","nihadh")
p3.print_name()

class child(parent):
    pass
p4=child("nihal","abdulla")
p4.print_name()
    