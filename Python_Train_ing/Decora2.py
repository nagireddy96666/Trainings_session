
# example of decorator
def sampleDecorator(func):
    def addingFunction():
        # some new statments or flow control
        print("This is the added text to the actual function.")
        # calling the function
        func()

    return addingFunction


@sampleDecorator
def actualFunction():
    print("This is the actual function.")


actualFunction()
