"""
    sequence data types includes string, tuple and list. 
    Their behave like a sequence -- an ordered collection of objects.

    operators and methods for sequence apply to string, tuple and list too.

"""

#-----------------  6 operators for sequence data types (apply to string, tuple and list) -----------------
"""
          x in s
          x not in s
          s1 + s2. join two sequences
          s*n, n*s. mutiply the content of a sequence
          s[i]. access index i element of s. index from 0 to length -1. index also can be -length to -1.
          s[i:j], s[i:j:k]. slice from i to j (not including j). k is the stride. 

"""
ls = ["python", '123', '.io']
print(ls[::-1])  # ['.io', '123', 'python']
print(ls)        # ['python', '123', '.io']

s = 'python123.io'   # not ['python123.io']
print(s[::-1])   # 'oi.321nohtyp'
print(s)   # 'python123.io'

s = 2*s
print(s)   # python123.iopython123.io



#----------------- 5 methods for sequence data types (apply to string, tuple and list) ---------------
"""
       len(s) ---- legth of the sequence
       min(s) ---- the min element in the sequence. 
       max(s) ----- the max element in the sequence.
                    (1) if it contains multi data types, raise error. 
                    (2) if elements are not comparable, raise error.
       
       s.index(x), s.index(x, i,j) --- return the first x's index. return the first x's index from i to j.
       s.count(x) --- number of x in s

"""

s = [1, 2, 0, 4, 5]
print(max(s))  # 5

""" raise error. not comparable
s = [{'name':'Jason'}, [1,2]]
print(max(s))
"""
s=     'hello, worldo'
#index  012345678910
print(s.index('o'))  # 4
print(s.index('o', 5, 20)) # 8   # if j is greater than the length of s, it does not raise error.

#=============================

#                tuple
"""
            ordered, unchangeable, allow duplicates
            It does not have any other methods than general methods for sequence.
"""
#=============================
# create an empty tuple 
t = ()
t = tuple()

# create a tuple
t = 1, 2   # when create a tuple, () is not mandated
print("t = ", t)  # (1,2)
# in a function, when return multiple values, it is a tuple
def func():
    return 1, 2, 3
t = func()
print('t = ', t) # (1,2,3)
t = (1,2)
print('t = ', t)  # (1,2)


creature = 'cat', 'dog', 'tiger', 'human'

print('creature[::-1] = ', creature[::-1]) # ('human', 'tiger', 'dog', 'cat'). create a new tuple, the original one is not changed.
print("creature = ", creature)  # ('cat', 'dog', 'tiger', 'human')

color = (1100, 'blue', creature)
print(color[-1][2])  # [-1] is creature, [2] is 'tiger'
print(color[-1][2][2]) # continue to character 'g'

for item in creature:
    print("item = ", item)

for i, item in enumerate(creature):
    print(f"i = {i}, item = {item}")
"""
i = 0, item = cat
i = 1, item = dog
i = 2, item = tiger
i = 3, item = human
"""

"""
#==============================

            list
            
            ordered, changeable, allow duplicates


----------- operators and methods for list ---------------
    ls[i] = x       ------ replace the ith elements by x.
    ls[i:j:k] = lt  ------ replace 
    del ls[i]       ------ delete the ith element
    del ls[i:j:k]   ------ delete elements from i to j, stride is k.
    ls += lt        ------ update ls, append lt to ls
    ls *=n          ------ update ls, duplicate ls n times.
    ls.insert(index, x) -- insert x at a certain position.
    ls.append(x)    ------ update ls, append x to ls. x as a whole add to ls.
    ls.extend(x)    ------ update ls, if x is a list, every element appends to ls.
    ls.index(x)     ------ index of x in ls.
    ls.clear()      ------ remove all elements in ls.
    ls.pop()        ------ using list as a stack. remove the last element of ls.
    ls.pop(0)       ------ using list as a queue. remove the first element of ls.
    ls.remove(x)    ------ delete the first appear x in ls.
    ls.reverse()    ------ reverse order of ls.
    ls.copy()       ------ create a new copy. 

#==============================
"""

# create an empty list
myList = []
myList = list()

myList = [1,2,3]
cp_myList = myList   # it does not copy. It just point to myList. If you change elements in cp_myList, the original list also change
cp_myList[0] = 'changed'
print("myList = ", myList)  #['changed', 2, 3]

ls = ['cat', 'dog', 'tiger', 1024]
ls[1:2] = [1, 2,3,4]  # insert 1,2,3,4 at ith position. the other elements move backward.
print(f"ls = {ls}")  # ['cat', 1, 2, 3, 4, 'tiger', 1024]
ls[1:5:2] = ['a', 'b']  # insert 'a' and 'b' from ith position and stride is 2.
print("ls = ", ls)  #  ['cat', 'a', 2, 'b', 4, 'tiger', 1024]



#  remove, del, pop, clear methods can reference the following webpage.
# https://note.nkmk.me/en/python-list-clear-pop-remove-del/
del ls[::3]
print("ls = ", ls)   # [1, 2, 4, 'tiger']









