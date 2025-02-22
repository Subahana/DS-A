def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1):
        for j in range(n-1-i):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

a=[1,7,3,5,9]
print(bubble_sort(a))

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] > arr[min_index]:  
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]  
    return arr

arr = [29, 10, 14, 37, 13]
print("Sorted array:", selection_sort(arr))

def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -=1
        arr[j+1] = key
    return arr
h= [10,55,1,44]
m=len(h) // 2
print(insertion_sort(h))

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return arr

s=[10,88,77,44,99]
print(merge_sort(s))

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    mid_element= arr[len(arr) // 2]
    left=[x for x in arr if x < mid_element]
    mid=[x for x in arr if x == mid_element]
    right=[x for x in arr if x > mid_element]
    
    return quick_sort(left) + mid + quick_sort(right)
q=[5,7,3,8]
print(quick_sort(q))