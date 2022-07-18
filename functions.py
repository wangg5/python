def myFunc():
    print("function can take no args")

myFunc()
print()

def myFunc(a):
    print("take one arg = ", a)
myFunc(10)
print()

# pass args using position
def myFunc(a, b):
    print("first arg = ", a)
    print("second arg = ", b)
myFunc(b=10, a=5)
print()

# takes default args
def myFunc(a,b="hello"):
    print("take default args")
    print("a = ", a)
    print("default = ", b)
myFunc(10)
myFunc(10, "world")
print()
# take arbitrary args
def myFunc(a, *argv):
    print("take arbitray args")
    print("a = ", a)
    print("arbitray args. It is a tuple")
    for item in argv:
        print("item = ", item)

myFunc(10)
myFunc(10, 'a', 'b', 'c')
print()
# **kwargs
def myFunc(a, **kwargs):
    print("**kwargs")
    print("a= ", a)
    for key, value in kwargs.items():
        print("key = ", key)
        print("value = ", value)

myFunc(10)
myFunc(10, first="hello", second="world")
