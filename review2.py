def repeat(key):
    a={}
    for i in key:
        count = 1
        if i in a:
            count += 1
            a[i] = count 
            if count > 1:
                return i
        else:
            a[i] = 1


def non_repeat(s):
    a = {}
    for i in s:
        if i in a:
            a[i] += 1
        else:
            a[i] = 1

    for x,y in a.items():
        if y == 1:
            return x
    return 'No Repeating element'


class hashtable:
    def __init__(self,size):
        self.size = size
        self.table = [{}
         for _ in range(size)]

    def hash_fun(self,key):
        return hash(key) % self.size

    def insert(self,key,value):
        index = self.hash_fun(key)
        self.table[index][key] = value  # Proper dictionary storage
    
    def display(self):
        for x in self.table:
            print(x)
    
    def get(self,key):
        index = self.hash_fun(key)
        return self.table[index].get(key, None)  # Retrieve value safely
   
        

def repeat_hash(s):
    a = hashtable(len(s))
    for x in s:
        y = a.get(x)
        if y is not None:
            y += 1
            a.insert(x,y)
            if y > 1:
                return x
        else:
            y = 1
            a.insert(x,y)

s='subahh'
print(repeat(s))
print(non_repeat(s))
h=hashtable(5)
h.display()
print(repeat_hash(s))