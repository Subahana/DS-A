class Stack:
    def __init__(self):
        self.stack = []
    def push(self,data):
        self.stack.append(data)
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return f"stack is empty"
    
    def display(self):
        print('stack from top to bottom')
        for i in self.stack[::-1]:
            print(i)

a=Stack()
a.push(1)
a.push(2)
a.display()
a.pop()
a.display()


f= [1,2,5]
f.pop()
print(f)
f.pop(-1)
print(f)

# ---------Queue -----------#

from collections import deque
# ----using deque in collection ---
class Queue:
    def __init__(self):
        self.queue = deque()

    def enqueu(self,item):
        self.queue.append(item)
    def deque(self):
        if len(self.queue) > 0:
            return self.queue.popleft()
        return 'Queue is empty'
    def display(self):
        if len(self.queue) == 0:
            print('Queue is Empty')
        print('Queue',(self.queue))
    def is_empty(self):
        return len(self.queue) == 0
    def size(self):
        return len(self.queue)
    def peek(self):
        if self.is_empty():
            return 'Queue is Empty'
        return self.queue[0]
q=Queue()
print(q.is_empty())
q.enqueu(55)
print(q.size())
q.display()

# -------Queue using list ----#

class QueueList:
    def __init__(self):
        self.queue = []

    def enqueu(self,item):
        return self.queue.append(item)
    def deque(self):
        if len(self.queue) == 0:
            return 'Queue is Empty'
        return self.queue.pop(0)
    def is_empty(self):
        return len(self.queue) == 0
    def peek(self):
        if self.is_empty():
            return 'Queue is Empty'
        return self.queue[0]
    def display(self):
        if self.is_empty():
            return 'Queue is empty'
        else:
            print('Queue:',(self.queue))

m=QueueList()
m.enqueu(10)
m.display()

import heapq


class PriorityQueue:
    def __init__(self):
        self.queue = []

    def enqueu(self,item,priority):
        heapq.heappush(self.queue,(item,priority))

    def dequeue(self):
        if len(self.queue) == 0:
            return None
        iteem,priority=heapq.heappop(self.queue)
        return iteem

    def peek(self):
        if len(self.queue) == 0:
            return None
        return self.queue[0][1]

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        if self.is_empty():
            return None
        else:
            print('Priority Queue unsorted:',self.queue)
            print('Priority Queue sorted',sorted(self.queue))
    
# -----Queue using Stack -------#

class QueueUsingStack:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self,item):
        return self.stack1.append(item)
        
    def dequeue(self):
        if not self.stack1:
            if not self.stack2:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        remove_item=self.stack2.pop()
        return remove_item

    def is_empty(self):
        return  not (self.stack1 or self.stack2)

    def display(self):
        if self.is_empty():
            return None
        else:
            print('Queue using stack :',self.stack2[::-1] + self.stack1)

    def size(self):
        return len(self.stack1) + len(self.stack2)
    
    def peek(self):
        if not self.stack2:
            if not self.stack1:
                return None
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]

h = QueueUsingStack()
h.enqueue(99)
h.enqueue(999)
h.enqueue(9999)
h.enqueue(9)
h.display()
            

            # ----stack using Queue -----#

class StackUsingQueue:
    def __init__(self):
        self.queue1 = deque()
        self.queue2 = deque()
    
    def puch(self,item):
        self.queue2.append(item)
        while self.queue1:
            self.queue2.append(self.queue1.popleft())
        self.queue1,self.queue2 = self.queue2,self.queue1


# /////Stack using linkedlist ////#

class Node:
    def __init__(self,data):
        self.data = data
        self.next =None

class stackLinkedlist:
    def __init__(self):
        self.top = None

    def push(self,item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return 
        pop_item = self.top.data
        self.top = self.top.next
        return pop_item
    def peek(self):
        if self.top is None:
            return 
        return self.top.data

# ////// Stack Using Array ///////#

class StackArray:
    def __init__(self):
        self.stack = []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if len(self.stack) <= 0:
            return
        return self.stack.pop()
    def peek(self):
        if len(self.stack) <= 0:
            return 
        return self.stack[-1]
    
m=StackArray()
print(m.peek())