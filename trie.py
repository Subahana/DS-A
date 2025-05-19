class TrieNode:
    def __init__(self):
        self.children ={}
        self.is_end = False
        self.prefix_count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node =self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
            node.prefix_count += 1
        node.is_end = True

    def search(self,word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startswith(self,prefix):
        node = self.root
        for char in prefix:
            if char not in node.children :
                return False
            node = node.children[char]
        return True
    
    # def autocomplete(self,prefix):
    #     def dfs(node,path,result):
    #         if node.is_end:
    #             result.append(''.join(path))
    #         for char,next_node in node.children.items():
    #             dfs(next_node,path+[char],result)

    #     node = self.root
    #     for char in prefix:
    #         if char not in node.children:
    #             return []
    #         node = node.children[char]

    #     result = []
    #     dfs(node,list(prefix),result)
    #     return result
        
    def autocomplete(self,prefix):
        def dfs(node,path,result):
            if node.is_end:
                result.append(''.join(path))
            for char,next_node in node.children.items():
                dfs(next_node,path + [char],result)
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        result = []
        dfs(node,list(prefix),result)
        return result
    
    def count_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return 0  # No such prefix found
            node = node.children[char]
        return node.prefix_count

a= Trie()
a.insert('apple')
a.insert('a')
print(a.search('a'))
print(a.startswith('app'))
print(a.startswith('ba'))
words = ["apple", "app", "apply", "application", "apt", "banana"]
for word in words:
    a.insert(word)
print(a.autocomplete('a'))
print(a.autocomplete('ap'))
print(a.autocomplete('b'))
print(a.count_prefix('app'))

