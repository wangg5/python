#  set using {} which is same to dict.
"""   -----  properties of set: --------
     unordered
     unchangeable(immutable)
     duplicated not allowed
     using {} 
     using , sepearate elements

"""
# if we want to create an empty set.
s = set()
print("empty set s = ", s)  # empty set s = set()

# dict can not in a set. This is wrong:
#    s = {123, "python", (1, 2), {"name":"Jason"}}
# list also can not is a set. This is also wrong.
#    s = {123, "python", [1,3]}
# why list and dict cannot in a set??  Because they are mutable. Set is immutable.
s = {123, "python", (1,3)}
for item in s:
    print(item)


mySet = set([1,1,2,2,3])
print("mySet = ", mySet)

mySet = set((1,2,3,3,3))
print("mySet = ", mySet)

# error, cannot have dict
#mySet = set([1,1, 3,3, "helloo", (10, 10, 100), {"name":"Jason", "age":12}])

# discard values
# mySet = {"name", "age"}
mySet = set({"name":"Jason", "age":12})
print("mySet = ", mySet)

mySet = set([1,1,3,3, "helloo"])
print("mySet = ", mySet)

mySet = set([1,1,3,3,"helloo", (10, 10, 100)])
print("mySet = ", mySet)

"""   error
mySet = set([1,2,2, {"name":"Jason", "age":12}])
print("mySet = ", mySet)
"""
# discard "systers"'s value
# mySet = {"name", "age", "sisters"}
mySet = set({"name":"Jason", "age":12, "sisters":["Amber", "Jen", "Ruby","Jen"]})
print("mySet = ", mySet)



