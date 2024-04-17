class Employee:

    def __init__(self,name,age,designation):
        self.name= name
        self.age= age
        self.designation=designation

    #instance method

    def clerk(self,song):
        return "{} sings {}".format(self.name, song)
    

#instance methods
obj= Employee("ravi",25,"Fresher")
print(obj.name)

#print(obj.clerk("'some work'"))
        
# call our instance methods
#print(obj.clerk("'Happy'"))



"""

class Parent():
f1()#ican access p.f1 and p.f2
f2()

p=Parent()

class child (Parent):
f3():
f4():
c= child()
#i can access method f3,f4
"""
