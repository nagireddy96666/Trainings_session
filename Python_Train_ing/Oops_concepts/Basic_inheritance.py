# parent class
class Bird:
    
    def __init__(self):#name,age,parrot,10
        print("Bird is ready")

    def whoisThis(self):
        print("Bird")

    def swim(self):
        print("Swim faster")

# child class
class Penguin(Bird):

    def __init__(self):#name,age, crow,2o
        # call super() function
        super().__init__()
        print("Penguin is ready")

    def whoisThis(self):
        print("Penguin")

    def run(self):
        print("Run faster")

b=Bird()
b.whoisThis()


p = Penguin()
p.whoisThis()
#p.swim()
#p.run()

