from collections import deque,defaultdict

class graph:
    def __init__(self,directed=False):
        self.graph = defaultdict(list)
        self.directed = directed

    def add_edge(self,u,v):
        self.graph[u].append(v)
        if not self.directed:
            self.graph[v].append(u)

    def bfs(self,start):
        visted = set()
        queue = deque([start])
        result = []
        while queue:
            node = queue.popleft()
            if node not in visted:
                visted.add(node)
                result.append(node)
                for neighbor in self.graph:
                    if neighbor not in visted:
                        queue.append(neighbor)
        return result
    
    def dfs(self,start):
        visted = set()
        result = []
        self.dfs_util(start,visted,result)
        return result
    
    def dfs_util(self,node,visted,result):   
        visted.add(node)
        result.append(node)
        for neighbor in self.graph:
            if neighbor not in visted:
                self.dfs_util(neighbor,visted,result)

    
    def display(self):
        for node in self.graph:
            print(f"graph {node} -> {self.graph[node]}")


g=graph(directed=False)
g.add_edge('a','b')
g.display()
print(g.bfs('a'))
print(g.dfs('b'))