# //////////BUBBLE SORT///////// #
a=[16,15,6,8,5]

# /-----without optimaization --------/

def bubble_sort1(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print('bubble_sort_asc',bubble_sort1(a)) 

def bubble_sort1_des(a):
    n=len(a)
    for i in range(n-1):
        for j in range(n-1):
            if a[j] < a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

print('bubble_sort_des',bubble_sort1_des(a))

# /---------with optimiztion for j(comparison) --------/

def bubble_sort2(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print('bubble_sort2',bubble_sort2(a))

def bubble_sort2_des(a):
    n = len(a)
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] < a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
    return a

print('bubble_sort2_dex',bubble_sort2_des(a))
# ------ fully optimized code for bubble sort -------/

def bubble_sort3(a):
    n=len(a)
    for i in range(n-1):
        swap = 0
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1] = a[j+1],a[j]
                swap = 1
        if swap == 0:
            break
    return a

print(bubble_sort3(a))

# /////////Insertion Sort////////#

def insertion_sort_des(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        j = i -1
        while j >= 0 and a[j] < temp:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = temp
    return a

print(insertion_sort_des(a))

def insertion_sort_asc(a):
    n = len(a)
    for i in range(1,n):
        temp = a[i]
        j = i-1
        while j >= 0 and a[j] > temp:
            a[j+1]= a[j]
            j -=1
        a[j+1] = temp
    return a

print(insertion_sort_asc(a))

# -------Selection Sort ------#

def selection_sort(a):
    n=len(a)
    for i in range(n-1):
        min_=i
        for j in range(i+1,n):
            if a[j] > a[min_]:
                min_ = j
        if min_ != i:
            a[i],a[min_] = a[min_],a[i]
    return a

print('selection_sort',selection_sort(a)) 