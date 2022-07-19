#  set using {} which is same to dict.
"""   -----  properties of set: --------
     unordered
     unchangeable(immutable)
     duplicated not allowed
     using {} 
     using , sepearate elements

"""
# if we want to create an empty set. can not do this: s = {}. That is an empty dict.
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

# ---------------------- convert to set -------------------------------
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

"""   error, dict cannot co-exist with other datatypes
mySet = set([1,2,2, {"name":"Jason", "age":12}])
print("mySet = ", mySet)
"""
# discard key's value
# mySet = {"name", "age", "sisters"}
mySet = set({"name":"Jason", "age":12, "sisters":["Amber", "Jen", "Ruby","Jen"]})
print("mySet = ", mySet)

#---------------------- create a set directly -------------------------
mySet = {1,2,3,1}
print("mySet = ", mySet)  # {1,2,3}

""" error, list can not be in a set 
mySet = {1,2,[1,2]}
print("mySet = ", mySet)
"""
mySet = {1,3, (1,1,2)}
print("mySet = ", mySet)   # {1,3, (1,1,2)}

""" error, dict can not be in a set
mySet = {1,1,3, {"name":"Jason", "age":12}}
print("mySet = ", mySet)
"""

# -------------------------- methods for set ---------------------------
"""
    union (s1|s2), intersection (s1&s2), difference (s1-s2), symmetric difference (s1^s2)


"""
"""          opertators for sets
             key in s, key not in s, ==, <=, >=, !=, <, >

"""
"""          methods for sets
        s.add(x), 
        s.remove(x), s.discard(x). remove x from s. if x is not in s, s.remove(x), raise
                                   a key error. s.discard(x) does not. 

        s.clear(). remove all elements in s.
        s.pop(). randomly return an element in s. remove this element from s. 
                 if s is empty, raise a key error.
        s.copy(). a copy of s
        len(s), length of s
        x in s, x not in s
        set(x).  convert x to set type

"""






























