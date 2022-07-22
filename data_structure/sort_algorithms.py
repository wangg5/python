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

x = [8, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
#x = []
#insertion_sort()
#selection_sort()
merge_sort(x)
print(x)
