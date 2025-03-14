# size=10
# # # ------hash() in built method is used in case of any data type of key ----#
# def hash_function(key):
#     return hash(key) % size
# print(hash_function('subahan'))

# # # ------no need of in built hash method for integer
# def hashCode(key):
#     # Return a hash value based on the key    
#     return key % size
# print(hashCode(100))

# a=[1,2]
# a.append([1,2])
# print(a)

# #  --------hashtable using list ------#

# class HashTable:
#     def __init__(self,size):
#         self.size = size
#         self.table=[[] for x in range(size)]
#     def hash_code(self,key):
#         return hash(key) % self.size

#     def insert(self,key,value):
#         index=self.hash_code(key)
#         for x in self.table[index]:
#             if x[0] == key:
#                 x[1] = value
#                 return
#         self.table[index].append([key,value])
#     def get(self,key):
#         index=self.hash_code(key)
#         for x in self.table[index]:
#             if x[0] == key:
#                 return x[1]
#         return None
#     def remove_key(self, key):
#         index = self.hash_code(key)
#         for x in self.table[index]:
#             if x[0] == key:
#                 self.table[index].remove(x)
#                 return
#     def print_hash(self):
#         for y in (self.table):
#             print(y)


# # -------hashtable using linkedlist -------#

# class Node:
#     def __init__(self,key,value):
#         self.key = key
#         self.value = value
#         self.next = None
# class HashtableList:
#     def __init__(self,size):
#         self.size = size
#         self.table = [None] * size

#     def hash_code(self,key):
#         return hash(key) % self.size
    
#     def insert(self,key,value):
#         index= self.hash_code(key)
#         if self.table[index] is None :
#             self.table[index] = Node(key,value)
#             return
#         else:
#             start = self.table[index]
#             while start :
#                 if start.key == key :
#                     start.value = value
#                     return 
#                 elif start.next is None:
#                     break
#                 start = start.next
#             start.next = Node(key,value)
#     def display(self):
#         for i in range(self.size):
#             print(i,end =' ')
#             start = self.table[i]
#             while start:
#                 print(start.key,start.value,end = ' ')
#                 start = start.next
#             print(None)
    
#     def get(self,key):
#         index = self.hash_code(key)
#         if self.table[index] is None:
#             print(None)
#             return
#         else:
#             start = self.table[index]
#             while start :
#                 if start.key == key :
#                     print(f"value of {start.key} is {start.value}")
#                     return 
#                 elif start.next is None:
#                     break
#                 start = start.next
#             print(None)
    
#     def remove_key(self,key):
#         index = self.hash_code(key)
#         if self.table[index] is None:
#             return 
#         start = self.table[index]
#         prev = None
#         while start:
#             if start.key == key:
#                 if prev is None:
#                     self.table[index] = start.next
#                 else:
#                     prev.next = start.next
#                     return True 
#                 prev = start 
#                 start = start.next
#         return False

            
# ht = HashtableList(10)
# ht.insert("name", "Alice")
# ht.insert("age", 25)
# # print(ht.get("age"))  # Output: 25
# # ht.remove_key('name')
# # print(ht.get('name'))
# ht.insert("city", "New York")
# ht.insert("email", "alice@example.com")
# ht.get(25)
# ht.remove_key('city')
# ht.display()
# # # ht.print_hash()
# # a=[1,5,3,9]
# # for x,y in enumerate(a):
# #     print(x,y)
# print((ht))


class Node :
    def  __init__(self,index,key,value):
        self.index = index
        self.key = key 
        self.value = value
        self.next = None

class HashTable :
    def __init__(self,size):
        self.size = size
        self.table = [None] * size

    def hash_function(self,index):
        return hash(index) % self.size

    def insert(self,index,key,value):
        index = self.hash_function(index)
        new_node = Node(index,key,value)
        if self.table[index] is None:
            self.table[index] = new_node
        else:
            start = self.table[index]
            while start and start.next:
                if start.key == key:
                    start.value = value
                    return 
                start = start.next
            start.next = new_node

    def display(self):
        for i in range(self.size):
            start = self.table[i]
            while start :
                print(f"{start.key}:{start.value}",end = ' ,')
                start = start.next
            print(None)

h=HashTable(5)
h.insert(1,'a1','subu')
h.insert(1,'a2','12')
h.display()