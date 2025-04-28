def merge_sort(s):
    if len(s) >1:
        mid = len(s) // 2
        left = s[:mid]
        right = s[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                s[k] = left[i]
                i += 1
            else:
                s[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            s[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            s[k] = right[j]
            j += 1
            k += 1

def string_sort(a):
    s=[]
    for i in a:
        s.append(int(i))
    merge_sort(s)
    return s

s='1423'
print(string_sort(s))

# def reverse_str(s):
#     stack = []
#     for i in s:
#         stack.append(i)
#     s = ''
#     for _ in len(stack):
#         s += stack.pop()

#     return s

# print(reverse_str(s))


class hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [[] for i in range(size)]

    def hash_fun(self,key):
        return hash(key) % self.size
    
    def insert(self,key,value):
        index = self.hash_fun(key)

        for i in self.table[index]:
            if i[0] == key:
                i[i] = value
        self.table[index].append([key,value])

    def display(self):
        for i in self.table:
            print(i)

h=hashtable(5)
h.insert('name','subu')
h.insert('mane','adhi')
h.display()
