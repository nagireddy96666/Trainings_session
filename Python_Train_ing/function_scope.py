x=10
def f():
    global x
    x=x+1
    print(x)
    #print(locals())
    #print(globals())
x=x+1
f()
print(x)
