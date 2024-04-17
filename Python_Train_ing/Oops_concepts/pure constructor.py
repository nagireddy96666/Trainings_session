class Parrot:
    
    # instance attributes
    #sample constructor forthe class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    # instance method
    def sing(self, song):
        return "{} sings {}".format(self.name, song)

    def dance(self,cultural):
        return "{} is now dancing {}".format(self.name, cultural)

# instantiate the object
blu = Parrot("Blu", 10)
pink = Parrot("Pink", 12)
red  = Parrot("Red",4)

# call our instance methods
print(blu.sing("'Happy'"))
print(blu.dance("'some song'"))

# call our instance methods
print(pink.sing("'Happy'"))
print(pink.dance("'some song'"))


# call our instance methods
print(red.sing("'Happy'"))
print(red.dance("'some song'"))


        


