# sort algorithms  ---- quick sort, merge sort, ...

"""
insertion sort
push x[i] to its sorted position by repeatedly swaping with the elment to its left
O(N**2)
input is a list.
output is a sorted list in ascending order.
"""
def insertion_sort():
    i = 0
    while i < len(x):
        j = i
        while j > 0 and x[j] < x[j-1]:
            # swap
            x[j-1], x[j] = x[j], x[j-1]
            j -= 1
        i += 1

"""
selection sort
find min in x[i, len(x)-1]. swap it with x[i]

"""
def selection_sort():
    for i in range(len(x)):

        # find min
        min = x[i]
        min_index = i
        for j in range(i, len(x)):
            if x[j] < min:
                min = x[j]
                min_index = j
        # swap x[i] and x[min_index]
        x[i], x[min_index] = x[min_index], x[i]



"""
   merge sort
   time complexity is O(nlgn)
   space complexity is O(n). It uses O(nlgn) space for the whole process. But each time, it only needs O(n) space.
   ****
      input x is a global variable. We pass it to merge_sort() function.
      Inside merge_sort() function, we divide x to two list, L and R. 
      Then pass L or R to merge_sort() function for recursion, L or R will become gloable
      variable now. In merge, we need a parent recursion call 'x'. This x is not the origianl
      pass x when we do merge sort.
   ****
"""
def merge_sort(x):
    if len(x) > 1:
        mid = len(x)//2
        L = x[:mid]
        R = x[mid:]
        merge_sort(L)
        merge_sort(R)
        merge(x, L, R)
def merge(x, L, R):
    i, j, k = 0, 0, 0
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            x[k] = L[i]
            i += 1
        else:
            x[k] = R[j]
            j += 1
        k += 1
    while i < len(L):
        x[k] = L[i]
        i += 1
        k += 1
    while j < len(R):
        x[k] = R[j]
        j += 1
        k += 1

"""
quick sort

"""
#------ my version. The return list is the sorted list------------
def quick_sort(x):
    if len(x) <= 1:
        return x
    if len(x) > 1:
        mid = partition(x)
        return quick_sort(x[:mid]) + quick_sort(x[mid:])

# pivot is the first elment in the list
def partition(x):
    pivot = x[0]
    index = 0
    for i in range(1, len(x)):
        if x[i] <= pivot:
            p = x.pop(i)
            x.insert(index, p)
            index += 1
    return index if index !=0 else 1

#----- online version, I modified ------
"""
def partition(l, r):
    # Last element will be the pivot and the first element the pointer
    pivot, ptr = nums[r], l
    for i in range(l, r):
        if nums[i] <= pivot:
            # Swapping values smaller than the pivot to the front
            nums[i], nums[ptr] = nums[ptr], nums[i]
            ptr += 1
    # Finally swapping the last element with the pointer indexed number
    nums[ptr], nums[r] = nums[r], nums[ptr]
    return ptr


def quicksort(l, r):
    #if len(nums) == 1:  # Terminating Condition for recursion. VERY IMPORTANT!
    #    return nums
    if l < r:
        pi = partition(l, r)
        quicksort(l, pi-1)  # Recursively sorting the left values
        quicksort(pi+1, r)  # Recursively sorting the right values
#----------------------------------------------------------------------------
"""


#"""
#   Least significant digit radix sort (LSD Radix sort)

#"""

def LSD_Radix_sort_contain_negative(x):
    neg = []
    pos = []
    for i in range(len(x)):
        if x[i] < 0:
            neg.append(abs(x[i]))
        else:
            pos.append(x[i])
    if len(neg) > 0:
        neg = LSD_Radix_sort(neg)
        for i in range(len(neg)):
            neg[i] *= -1
    if len(pos) > 0:
        pos = LSD_Radix_sort(pos)
    
    x = neg[::-1] + pos
    return x


def LSD_Radix_sort(x):
    q = [[] for i in range(10)] # create 10 buckets

    # calculate max digits in the list
    max = x[0]
    for i in range(len(x)):
        if max < x[i]:
            max = x[i]
    nDigits = 0
    while max > 0:
        max //= 10
        nDigits += 1

    for j in range(nDigits):
        for i in range(len(x)):
            r = (x[i] % 10**(j+1))//10**j
            q[r].append(x[i])  # put into the buckets
        x.clear()
        for i in range(10):
            while len(q[i]) > 0:
                x.append(q[i].pop(0))
    return x
"""
   counting sort

"""

# cannot deal with negative numbers 
# counting sort
def counting_sort(x):
    # find the max in the list
    if len(x) <=1:
        return x

    max = x[0]
    for i in range(len(x)):
        if x[i] > max:
            max = x[i]
    # create a counting list
    c = [0 for i in range(max+1)]
    # count
    for i in range(len(x)):
        c[x[i]] += 1
    # accumulate counts
    for i in range(1, len(c)):
        c[i] += c[i-1]
    # using a temp list to store sorted list
    temp = [0 for i in range(len(x))]
    for i in range(len(x)-1, -1, -1):
        temp[c[x[i]] -1] = x[i]
        c[x[i]] -= 1
    return temp

def counting_sort_contain_negative(x):
    neg = []
    pos = []
    for i in range(len(x)):
        if x[i] < 0:
            neg.append(abs(x[i]))
        else:
            pos.append(x[i])
    neg = counting_sort(neg)
    pos = counting_sort(pos)
    if len(neg) > 0:
        for i in range(len(neg)):
            neg[i] *= -1

    return neg[::-1] + pos



x = [8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#x = [-1]
#x =[7, 19, 61, 11, 14, 54, 1, 8, -20, -4, -8, -6]
#insertion_sort()
#selection_sort()
#merge_sort(x)
#print(quick_sort(x))
#x = LSD_Radix_sort_contain_negative(x)
x = counting_sort_contain_negative(x)
print(x)
