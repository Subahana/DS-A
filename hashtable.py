size=10
# ------hash() in built method is used in case of any data type of key ----#
def hash_function(key):
    return hash(key) % size
print(hash_function('subahan'))

# ------no need of in built hash method for integer
def hashCode(key):
    # Return a hash value based on the key
    return key % size
print(hashCode(100))