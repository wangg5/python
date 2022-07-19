a = 10
def myFunc(a):
    print("inside a function")
    print("global a =", a)

    print("assign a= 2. Here a is a local variable")
    a = 2
    print("local a = ", a)
    def in_myFunc(a):
        print("in a nested function, a = ", a)
        print("assign a = 1. In this nested function")
        a = 1
        print("local->nested a = ", a)
    in_myFunc(a)
    print("after a nested function a =", a)

print("before call myFunc a = ", a)
myFunc(a)
print("after call myFunc a = ",a)


print("\n\na global list")
mylist = [1,2,3]
def myListFunc(mylist):
    print("mylist =", mylist)

    mylist[0] = "change first element inside a function"
    print("inside a function, after change, mylist = ", mylist)
print("before call myListFunc, mylist = ", mylist)
myListFunc(mylist)
print("after call myListFunc, mylist =", mylist)


print("\n\n class")
class myClass:
    def changeList(self, mylist):
        mylist[1] = "in a class"
mc = myClass()
mc.changeList(mylist)
print("a method of a class changed the second element of the list\n mylist = ", mylist)
