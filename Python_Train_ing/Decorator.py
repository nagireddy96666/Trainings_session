#decorator example
def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner
"""
@make_pretty
def ordinary():
    print("I am ordinary")
"""
def ordinary():
    print("I am ordinary")
ordinary = make_pretty(ordinary)

ordinary()

