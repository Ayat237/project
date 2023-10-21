import math as m

#---------------------------------------------------------#
#class structure
class class_name:# stucture has some methods and arguments
    def __init__(self, arguments):#constructor of each class ,it the first thing will be excute outomatically 
        self.arguments=arguments
    def methodes(self, argument):
        pass
#--------------------------------------------------#
class Person :
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.salary=5000
        print(f"hello {self.name}, your age is {self.age}")
    def saying_hello(self):
        print(f"hello {self.name}")
        


p = Person("ayat",21)
print(p.name)
print(p.age)
print(p.salary)
p.salary=1000 #updated salary
print(p.salary)   
del p.salary # to delete salary 
#print(p.salary)   
p1=p.saying_hello()
print(p1)

#-----------------------------------------------#
class parallogram:
    def __init__(self,s1,s2,angle):
        self.side1=s1
        self.side2=s2
        self.angle=angle
    def area(self):
        return (self.side1 * self.side2 * m.sin(m.radians(self.angle)))
#if you print the object -->print(p)-->it will print the address of this object
# we can use __str__ finction to get information about object not adress of object
    def __str__(self) :#magic function , if you want to print all information you want
       return f"side1 = {self.side1}, side2 = {self.side2} , angle = {self.angle}"
    
s1=int(input("enter side1 : "))
s2=int(input("enter side2 : "))
a=int(input("enter angle : "))
p1=parallogram(s1,s2,a)
print(p1.area())
print(p1)

#-------------------------------------------#

   
