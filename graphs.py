# from collections import deque,defaultdict

# class graph:
#     def __init__(self,directed=False):
#         self.graph = defaultdict(list)
#         self.directed = directed

#     def add_edge(self,u,v):
#         self.graph[u].append(v)
#         if not self.directed:
#             self.graph[v].append(u)

#     def bfs(self,start):
#         visted = set()
#         queue = deque([start])
#         result = []
#         while queue:
#             node = queue.popleft()
#             if node not in visted:
#                 visted.add(node)
#                 result.append(node)
#                 for neighbor in self.graph:
#                     if neighbor not in visted:
#                         queue.append(neighbor)
#         return result
    
#     def dfs(self,start):
#         visted = set()
#         result = []
#         self.dfs_util(start,visted,result)
#         return result
    
#     def dfs_util(self,node,visted,result):   
#         visted.add(node)
#         result.append(node)
#         for neighbor in self.graph:
#             if neighbor not in visted:
#                 self.dfs_util(neighbor,visted,result)

    
#     def display(self):
#         for node in self.graph:
#             print(f"graph {node} -> {self.graph[node]}")


# g=graph(directed=False)
# g.add_edge('a','b')
# g.display()
# print(g.bfs('a'))
# print(g.dfs('b'))


# class graph:
#     def __init__(self):
#         self.graph = {}

#     def add_nodes(self,node):
#         if node not in self.graph:
#             self.graph[node] = []

#     def add_edges_undirected(self,node1,node2):
#         self.add_nodes(node1)
#         self.add_nodes(node2)
#         self.graph[node1].append(node2)
#         self.graph[node2].append(node1)
    
#     def add_edges_directed(self,node1,node2):
#         self.add_nodes(node1)
#         self.add_nodes(node2)
#         self.graph[node1].append(node2)

#     def print_graph(self):
#         for node in self.graph:
#             print(f"{node} --> {','.join(self.graph[node])}")
        
#         for node,neighbor in self.graph.items():
#             print(f"{node} --> {','.join(neighbor) if neighbor else 'None'}")
        
#     def dfs(self,start,visited=None):
#         if visited is None:
#             visited = set()

#         print(start,end=' ')
#         visited.add(start)

#         for n in self.graph[start]:
#             if n not in visited :
#                 self.dfs(n,visited)
    
#     def bfs(self,start):
#         visited = set()
#         queue = [start]
#         while queue :
#             current = queue.pop(0)
#             if current not in visited :
#                 print(current,end=' ')
#                 visited.add(current)
#                 for n in self.graph[current]:
#                     if n not in visited:
#                         queue.append(n)

#     def has_edge(self,node1,node2):
#         return node2 in self.graph.get(node1,[])
    
#     def remove_edges(self,node1,node2):
#         if node1 in self.graph and node2 in self.graph[node1]:
#             self.graph[node1].remove(node2)
#         if node2 in self.graph and node1 in self.graph[node2]:
#             self.graph[node2].remove(node1)

#     def remove_edge_directed(self, node1, node2):
#         if node1 in self.graph and node2 in self.graph[node1]:
#             self.graph[node1].remove(node2)

#     def remove_node(self,node):
#         if node in self.graph:
#             for n in self.graph[node]:
#                 self.graph[n].remove(node)
#             del self.graph[node]

#         for n in self.graph:
#             if node in self.graph[n]:
#                 self.graph[n].remove(node)


# g=graph()
# g.add_edges_undirected('a','b')
# g.add_edges_directed('b','c')
# g.print_graph()
# g.dfs('a')
# g.dfs('b')
# print()
# g.bfs('a')
# # g.remove_edges('a','b')
# g.remove_node('a')
# g.print_graph()

class graph:
    def __init__(self):
        self.graph = {}

    def add_node(self,node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edges(self,node1,node2):
        self.add_node(node1)
        self.add_node(node2)
        self.graph[node1].append(node2)
        # self.graph[node2].append(node1)

    def print_graph(self):
        for node in self.graph:
            print(f"{node} --> {self.graph[node]}")

    def dfs(self,start,visited = None):
        if visited is None:
            visited = set()

        print(start,end = ' ')
        visited.add(start)

        for n in self.graph[start]:
            if n not in visited:
                self.dfs(n,visited)

    def bfs(self,start):
        visited = set()
        queue = [start]

        while queue:
            current = queue.pop(0)
            if current not in visited:
                print(current,end=',')
                visited.add(current)
                for n in self.graph[current]:
                    if n not in visited:
                        queue.append(n) 

    def has_path(self,start,end,visited=None):
        if visited is None:
            visited = set()
        if start == end:
            return True
        visited.add(start)
        for n in self.graph[start]:
            if n not in visited:
                if self.has_path(n,end,visited):
                    return True
        return False
    def shortest_path(self,start,end):
        from collections import deque
        queue = deque([(start,[start])])
        visited = set()
        while queue:
            current ,path = queue.popleft()
            if current == end:
                return path
            visited.add(current)
            for n in self.graph[current]:                                                      
                if n not in visited:
                    queue.append((n,path+[n]))
                    visited.add(n)
        return None
    def cyclic_undirected(self):
        visited = set()
        def dfs(node,parent):
            visited.add(node)
            for n in self.graph[node]:
                if n not in visited:
                    if dfs(n,node):
                        return True
                elif n != parent:
                    return True
            return False
        for node in self.graph:
            if node not in visited:
                if dfs(node,None):
                    return True
        return False
    
    def cyclic_directed(self):
        visited = set()
        stack = set()

        def dfs(node):
            visited.add(node)
            stack.add(node)
            for n in self.graph[node]:
                if n not in visited:
                    if dfs(n):
                        return True
                elif n in stack:
                    return True
            stack.remove(node)
            return False

        for node in self.graph:
            if node not in visited:
                if dfs(node):
                    return True
        return False


    
g = graph()
g.add_edges('a','b')
g.add_edges('a','c')
g.add_edges('b','d')
g.add_edges('c','d')
g.add_edges('b','e')
g.add_edges('d','e')


g.print_graph()

g.dfs('a')
g.bfs('a')
print(g.has_path('a','c'))
print(g.shortest_path('a','e'))
print(g.cyclic_undirected())
print(g.cyclic_directed())