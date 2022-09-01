# hash
# convert a thing to an array index
# input % 1024

#============================= hash set
# HashSet(duplicates not allowed), using a hash table. Hash functions, like the above one. 
# Hash function should be efficient. O(1)

#  Load Factor of hash table. How full is your table?

#  load factor lamber = # entries in table/(size of the array)
#               lamber is too small, memory is wasted
#                         too large, runtime is slow

#==============================   hash map <key, value>==================================
# using hash table
# hash the key to determine array index
# store (key, value) in array 
#
"""
  h(k) = k % A.length   # such as A.length = 10
  put(1, 'dog')
  put(11, 'auk')
  put(10, 'bear')
  put(14, 'cat')
  put(24, 'ape')

  0 ---> 10 bear
  1 ---> 1 dog ---> 11 auk
  2
  3
  4 ---> 14 cat ---> 24 ape
  5
  6
  7
  8
  9


"""
#------------------------------- rehashing. lamber is large or small-----------
#     put each element where in belongs in the new array.

# need a new hash function
"""
    h(k) = k % A.length  # such as A.length = 3
    
    0 ---> 24 ape
    1 ---> 1 dog ---> 10 bear
    2 ---> 11 auk ---> 14 cat

runtime of rehashing:  N is the array size, n is number of entries
    for each bucket b"
        for each element e in b:
            put e into the new array <----- n times
    
    N + n(runtime of put). the worst case of put is O(n)

    overall runtime is:
        worst case: O(N + n**2)
        average case: O(N + n)
    because it is rehashing, I do not need to search there are duplicates or not. So, put methods, just put the elements in that slot. 
    So, the worst case of put is O(1)

    So, overall runtime is:
        worst case: O(N + c)

"""
#---------------------------- hash something is not integer ----------
# hashing strings: interpret ASCII (or unicode) representation as an integer





#----------------------------- Collision Resolution ---------------
"""
   1  Chaining -- use a LinkedList to store multiple elements per bucket.
   2 Open Addressing - use empty buckets to store things that belong in other buckets.
   Need some scheme for deciding which buckets to look in.
   Such as, Linear Probing. If it's slot is full, check the next slot. If it is empty, put it there. Otherwise, check the next slot, until find empty slot. If not find empty slot until the end of the array, go to the start of the array and keep searching.

   Quadratic Probing: H, H+1, H+2**2, H+3**3,..... what the runtime of get?? when do you stop searching?



"""

# ===============  TreeMap,  AVL tree: store a key and a value in each node, BST property applies to keys only.
# Example: TreeMap<String, Integer> maps words to the number of times they have been seen.





