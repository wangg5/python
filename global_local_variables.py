a = 10
def func():
    print("a = ", a)  # 10
    #global a   # error, I think the print function cause an error here.
    #a = 3
    return a + 2
print(func())   #  12

def func1():
    # print("a = ", a)
    a = 3   # this will raise an error. Python gets confused. If you want to print out a's value, after this line will be fine.
    print("a = ", )
    return a + 2
print(func1()) # 5
print("a = ", a)  #10



def myFunc():
    print("inside a function")
    #print("global a =", a)  # same to func1, cannot print out a here. After assign, you can call print function

    print("assign a= 2. Here a is a local variable")
    a = 2
    print("local a = ", a)
    def in_myFunc():
        #print("in a nested function, a = ", a)  # same to func1, cannot call print function yet.
        print("assign a = 1. In this nested function")
        a = 1
        print("local->nested a = ", a)
    in_myFunc()
    print("after a nested function a =", a)  # 2

print("before call myFunc a = ", a)
myFunc()
print("after call myFunc a = ",a)   # 10


print("\n\na global list")
mylist = [1,2,3]
def myListFunc():
    print("inside myListFunc function. mylist =", mylist)

    mylist[0] = "changed"
    print("inside a function, after change, mylist = ", mylist)  #['changed', 2,3]
print("before call myListFunc, mylist = ", mylist)
myListFunc()
print("after call myListFunc, mylist =", mylist)  #['changed', 2, 3]


print("\n\n class")
class myClass:
    def changeList(self):
        mylist[1] = "in a class"
mc = myClass()
mc.changeList()
print("a method of a class changed the second element of the list\n mylist = ", mylist)   #['changed', 'in a class', 3]



xx = 111
def ff():
    global xx
    xx = 3
ff()
print("xx is a global variable which is defined in a function. \n xx = ", xx)



def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) 



