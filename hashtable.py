size=10
# # ------hash() in built method is used in case of any data type of key ----#
def hash_function(key):
    return hash(key) % size
print(hash_function('subahan'))

# # ------no need of in built hash method for integer
def hashCode(key):
    # Return a hash value based on the key
    return key % size
print(hashCode(100))

a=[1,2]
a.append([1,2])
print(a)

class HashTable:
    def __init__(self,size):
        self.size = size
        self.table=[[] for x in range(size)]
    def hash_code(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index=self.hash_code(key)
        for x in self.table[index]:
            if x[0] == key:
                x[1] = value
                return
        self.table[index].append([key,value])
    def get(self,key):
        index=self.hash_code(key)
        for x in self.table[index]:
            if x[0] == key:
                return x[1]
        return None
    def remove_key(self, key):
        index = self.hash_code(key)
        for x in self.table[index]:
            if x[0] == key:
                self.table[index].remove(x)
                return
    def print_hash(self):
        for y in (self.table):
            print(y)

ht = HashTable(10)
ht.insert("name", "Alice")
ht.insert("age", 25)
print(ht.get("age"))  # Output: 25
ht.remove_key('name')
print(ht.get('name'))
ht.insert("name", "Alice")
ht.insert("age", 25)
ht.insert("city", "New York")
ht.insert("email", "alice@example.com")
ht.insert("age", 25)
ht.print_hash()
a=[1,5,3,9]
for x,y in enumerate(a):
    print(x,y)