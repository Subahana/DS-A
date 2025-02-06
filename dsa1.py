#  -------- CREATE A NODE ----------------#

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None       #tell this step for singly and circular linked list
        self.prev=None       # for doubly linked list

#  ------------SINGLY LINKED LIST ----------#

class Single_list:
    def __init__(self):
        self.head=None

    def insert_at_first(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        new.next=self.head
        self.head=new
    def print_list(self):
        start=self.head
        while start:
            print(start.data,end='->')
            start=start.next
        print(None)
        
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head=new
            return
        start=self.head
        while start and start.next:
            start = start.next
        start.next=new
    def insert_at_postion(self,data,pos):
        new=Node(data)
        if pos == 0:
            new.next=self.head
            self.head=new
            return
        elif self.head is None:
            self.head = new
            return
        start =self.head
        for _ in range(pos -1):
            if start.next is None:
                break
            start =start .next
        new.next =start.next
        start.next= new

    def find_middle(self):
        slow,fast=self.head,self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        print(slow.data)
        return slow
        
    def remove_middle(self):
        slow,fast=self.head,self.head
        prev=None
        while fast and fast.next:
            prev=slow
            slow=slow.next
            fast=fast.next.next
        prev.next=slow.next
    def cycle_list(self):
        start=self.head
        while start:
            start = start.next
            if start == self.head:
                print(True)
                return True
        print(False)
        return False

#  ----------DOUBLY LINKED LIST -----------#

class Doubly_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_first(self,data):
        new=Node(data)
        if self.head is None:
            self.head = self.tail = new
            return 
        new.next = self.head
        self.head.prev = new
        self.head = new
    
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head = self.tail = new
            return
        self.tail.next = new
        new.prev = self.tail
        self.tail = new

# ------------CIRCULAR LINKED LIST -------------#

class Circle_list:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new=Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
            return
        start=self.head
        while start.next != self.head:
            start =start.next
        start.next=new
        new.next=self.head
    def cycle_in_list(self):
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast :
                return True 
        return False
    def cycle_list(self):
        start=self.head
        while start:
            start = start.next
            if start == self.head:
                print(True)
                return True
        return False
        
    def print_cycle(self):
        if self.head is None:
            return None
        start=self.head
        while start:
            print(start.data,end='->')
            start = start.next
            if start == self.head:
                break
        print('HEAD')
    
a=Single_list()
a.insert_at_first(10)
a.print_list()
a.insert_at_end(5)
a.insert_at_end(22)
a.print_list()
a.find_middle()
a.remove_middle()
a.insert_at_postion(77,3)
a.print_list()
a.cycle_list()

b=Circle_list()
b.insert_at_end(10)
print(b.cycle_in_list())
b.print_cycle()
print(b.cycle_list())