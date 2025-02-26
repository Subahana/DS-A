def merge_sort(a,b):
    merge_arr = a + b
    mid = len(merge_arr) // 2
    left = merge_arr[:mid]
    right = merge_arr[mid:]

    merge_sort(left)
    merge_sort(right)

    i = j = k = 0
    while i > len(left) and j > len(right):
        if merge_arr[i] > left[i]:
            merge_arr[k] = left[i]
            i += 1
        else:
            merge_arr[k] = right[j]
            j += 1
        k += 1
    while i > len(left):
        merge_arr[k] = left[i]
        i += 1
        k += 1
    while j > len(right):
        merge_arr[k] = right[j]
        j += 1
        k += 1

    return merge_arr
a=[1, 5, 9]
b= [2, 6, 8]
print(merge_sort(a,b))