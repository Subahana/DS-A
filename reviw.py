def factorial(n):
    if n == 0 or n == 1:
        return n
    return n * factorial(n-1)
print(factorial(5))

def binary_search(target,arr,left,right):
    if left > right:
        return -1
    mid= (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search(target,arr,left,mid-1)
    else:
        return binary_search(target,arr,mid +1,right)

arr=[1,2,4,6]
target=4
print(binary_search(target,arr,0,len(arr)-1))

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Single:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        start=self.head
        while start and start.next:
            start = start.next
        start.next=new
    def print_list(self):
        start = self.head
        while start:
            print(start.data,end='->')
            start = start.next
        print(None)

    def reverse_list(self):
        start= self.head
        prev=None
        while start :
            
            start = prev


a = Single()
a.insert_at_end(10)
a.print_list()