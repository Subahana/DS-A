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
    def reverse_list(self):
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev
        return self.head
    def remove_duplicates(self):
        if self.head is None:
            return 
        start = self.head
        prev=None
        while start and start.next:
            if start.data == start.next.data:
                start.next=start.next.next
                prev=start.next
            else:
                start = start.next
                prev=start
    def remove_duplicates_unsorted(self):
        if self.head is None or self.head.next is None:
            return
        sigma=set()
        start=self.head
        prev=None
        while start:
            if start.data in sigma:
                prev.next= start.next
            else:
                sigma.add(start.data)
                prev=start
            start=start.next
    def delete_end_elemen(self):
        if self.head is None:
            return
        elif self.head.next is None:
            self.head = None
            return
        start= self.head
        while start and start.next:
            start = start.next
        start.next=None
    def delete_first_element(self):
        if self.head is None:
            return 
        self.head = self.head.next
    def delete_element_pos(self,pos):
        if self.head is None:
            return 
        if pos == 0:
            self.head = self.head.next
        start= self.head
        for _ in range(pos -1):
            start = start.next
        start.next=start.next.next   
def merge_list_at_end(list1,list2):
    if list1 is None or list2 is None:
        return list1 or list2
    start=list1.head
    while start and start.next:
        start = start.next
    start.next = list2.head
    return list1
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
a.print_list()
a.insert_at_postion(100,2)
a.print_list()
a.reverse_list()
a.print_list()
b=Single_list()
b.insert_at_end(55)
b.print_list()
m=merge_list_at_end(a,b)
m.print_list()
m.insert_at_end(55)
m.insert_at_end(77)
m.print_list()
m.remove_duplicates()
m.print_list()
m.remove_duplicates_unsorted()
m.print_list()
b=Circle_list()
b.insert_at_end(10)
print(b.cycle_in_list())
b.print_cycle()
print(b.cycle_list())
m.delete_element_pos(2)
m.print_list()

