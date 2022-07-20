"""
    dict data type

    Ordered or Unordered?
                As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

    changeable
    duplicates not allowed

***** dict data type cannot do d1+d2 or d1*n******

"""
# --------------- create a dict  ----------------
#d = {}   
# or
d = dict()
print("length of d = ", len(d))



Dict = dict([(1, 'Geeks'), (2, 'For')])
# Dict = dict([1,2,3,4])  # error
print("\nDictionary with each item as a pair: ")
print(Dict)



thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

if "model" in thisdict:
    print("model in thisdict")

print("True") if "car" in thisdict else print("False")

if "car" not in thisdict:
    print("car not in thisdict")
#rel = thisdic["car"]
#print("rel = ", rel)  # error
rel = thisdict.get("car", "not exist")
print("rel = ", rel)
rel = thisdict.get("car")
print("rel = ", rel)   # None
for x in thisdict:
    print(x)

# ------------------------ add/change items --------------------------
#                          d[key] = value, d.update({key:value})
d = {"name":"Jason", "gender":"male", "age":12}
d["school"] = "MIT"
print("d = ", d)
d.update({"school":"Oxford"})  # replace "school":"MIT"
print("d = ", d)
# add new items
d.update({"hobby":"jogging"})
print("d = ", d)


# ------------------------ remove items  ----------------------------
#                         pop(key), popitem(), del d[key], clear()
#  The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead).
# d.pop()  # wrong, it takes 1 argument
d.pop("school")
print("d = ", d)
# d.popitem("name")  # wrong. it takes no argument.
d.popitem()
print("d = ", d)
#  del d["school"]   # error, key not exist
del d['age']
print("d = ", d)

#------------------------- access items  ---------------------------
#                          d[key], d.get(key,default), d.keys(), d.values(), d.items()
# 

#  ************ For d.keys(), d.values() and d.items() ***************
# The returned list is a view of the items of the dictionary, 
#  meaning that any changes done to the dictionary will be reflected in the items list.
#  
print("d['gender'] = ", d['gender'])
print("d.get('gender', 'exist') = ", d.get("gender", "exist"))
ls = d.keys()
print("ls = ", ls)
d["age"] = 12
print("ls = ", ls)

li = d.items()
print("li = ", li)
d["school"] = "Stanford"
print("li = ", li)

#------------------------- loop dictionaries  -----------------------------

# k is keys in d
for k in d:
    print("key = ", k)

for k in d.keys():
    print("key = ", k)

for v in d.values():
    print("values = ", v)

for k, v in d.items():
    print(f"key = {k}, value = {v}")



# ======================== methods for dictionaries ----------------------
"""
       1 len(d)
       2 in
       3 not in
       4 copy()
       5 get(key, default)
       6 update()
       7 del d[key]
       8 pop
       9 popitem()
       10 clear
       11 d.keys(),d.values(),d.items()
       12 dict([(tuple_item1, tuple_item2), (tuple_item1, tuple_item2), (..), ...])

"""

