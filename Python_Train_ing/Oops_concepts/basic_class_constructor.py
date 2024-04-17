class Parrot:

    # class attribute
    species = "bird"

    # constructor classinstance attribute
    def __init__(self, name, age, colour):
        self.name = name
        self.age = age
        self.colour= colour
    #if we declared function with in the Class we call as Methods   
    def f1(self,):
        print("calling function f1")

# instantiate the Parrot class

blu = Parrot("Blu", 10,"Green")
woo = Parrot("Woo", 15,"yellow")
b= Parrot("Yel",25,"Red")
print(Parrot.f1())

# access the class attributes
print("Blu is a {}".format(blu.__class__.species))
print("Woo is also a {}".format(woo.__class__.species))
print("b is also a {}".format(b.__class__.species))

# access the instance attributes
#print("{} is {} years old".format( blu.name, blu.age ,blu.colour))
#print("{} is {} years old".format( woo.name, woo.age , woo.colour))
#print("{} is {} years old".format( b.name, b.age , b.colour))

print("calling constructor arguments",b.name,b.age,b.colour)



