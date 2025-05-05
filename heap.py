import heapq

min_heap =[]
heapq.heappush(min_heap,1)
heapq.heappush(min_heap,10)
heapq.heappush(min_heap,5)
heapq.heappush(min_heap,12)
heapq.heappush(min_heap,8)

print(min_heap)
print(min_heap[0])
heapq.heappop(min_heap)
print(min_heap)
print(heapq.heappop(min_heap))

class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i):return (i-1) // 2
    def left(self,i):return 2*i + 1
    def right(self,i):return 2*i + 2

    def insert(self,key):
        self.heap.append(key) 
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        while index > 0 and self.heap[index] < self.heap[self.parent(index)]:
            self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]
            index = self.parent(index)

    def extract_min(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.helpify_down(0)
        return root
    
    def helpify_down(self,index):
        smallest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < len(self.heap) and self.heap(right) < self.heap(smallest):
            smallest = right
        if smallest != index:
            self.heap[index],self.heap[smallest] = self.heap[smallest],self.heap[index]
            self.helpify_down(smallest)
        
    def peek(self):
        return self.heap[0] if self.heap else None
    
    def display(self):
        print('heap:',self.heap)

minheap=MinHeap()
minheap.insert(10)
minheap.insert(1)
minheap.insert(5)
minheap.display()
print(minheap.peek())

class MaxHeap:
    def __init__(self):
        self.heap = []

    def parent(self,i) : return (i-1) //2
    def left(self,i):return 2*i + 1
    def right(self,i) :return 2*i + 2

    def insert(self,key):
        self.heap.append(key)
        self.heapify_up(len(self.heap) -1)

    def heapify_up(self,index):
        while index > 0 and self.heap[index] > self.heap[self.parent(index)]:
            self.heap[index] ,self.heap[self.parent(index)] = self.heap[self.parent(index)] ,self.heap[index]
            index = self.parent(index)

    def extract_max(self):
        if not self.heap:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return root
    
    def heapify_down(self,index):
        largest = index
        left = self.left(index)
        right = self.right(index)

        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left

        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != index:
            self.heap[index],self.heap[largest] = self.heap[largest],self.heap[index]
            self.heapify_down(largest)

    def peek(self):
        return self.heap[0] if self.heap else None
    
    def display(self):
        print('Maxhea:',self.heap)

maxheap=MaxHeap()
maxheap.insert(100)
maxheap.insert(10)
maxheap.insert(1)
maxheap.insert(1000)
maxheap.display()


def heapify(arr,n,i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i] , arr[largest] = arr[largest] , arr[i]
        heapify(arr,n,largest)

def heap_sort(arr):
    n = len(arr)

    for i in range(n//2 -1,-1,-1):
        heapify(arr,n,i)

    for j in range(n-1,0,-1):
        arr[j] , arr[0] = arr[0] , arr[j]
        heapify(arr,j,0)


a=[4,1,12,4,9]
print(a)
heap_sort(a)
print(a)
