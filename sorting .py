# //////////BUBBLE SORT///////// #
a=[16,15,6,8,5,6]

# /-----without optimaization --------/

def bubble_sort(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print(bubble_sort(a))

# --------with optimistaion  --------#

def bubble_sort1(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print(bubble_sort1(a))

def bubble_sort2(a):
    n = len(a)
    for i in range(n-1):
        swap = 0
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap = 1
        if swap == 0:
            break
    return a

print(bubble_sort2(a))


# //////// Insertion Sort //////// #

def insertion_sort(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1] = a[j]
            j -=1
        a[j+1] = temp
    return a

print(insertion_sort(a))


# //////// Selection Sort /////// #

def select_sort(a):
    n = len(a)
    for i in range(n-1):
        min_indes = i
        for j in range (i+1,n):
            if a[j] < a[min_indes]:
                min_indes = j
        if min_indes != i :
            a[i],a[min_indes] = a[min_indes],a[i]      
    return a          

print(select_sort(a))

#  //////// Quick Sort /////// #

def quick_sort(a):
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left=[x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right=[x for x in a if x > pivot]
    return quick_sort(left) +mid + quick_sort(right)

print(quick_sort(a))


# ///////// Merge Sort ////////// #

def merge_sort(a):
    if len(a) > 1:
        mid = len(a) // 2
        left = a[:mid]
        right = a[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                a[k] = left[i]
                i += 1
                k += 1
            else:
                a[k] = right[j]
                j += 1
                k += 1
        while i < len(left):
            a[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            a[k] = right[j]
            j += 1
            k += 1
    return a
print(merge_sort(a))