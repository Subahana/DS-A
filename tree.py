# #----General Tree ------

# class TreeNode:
#     def __init__(self,value):
#         self.value = value
#         self.children = []

#     def add_child(self,node):
#         self.children.append(node)
    
#     def __str__(self):
#         return str(self.value)
    
# def pre_order(node):
#     if node is None:
#         return 
#     print(node.value ,end=' ')
#     for child in node.children:
#         pre_order(child)

# def post_order(node):
#     if node is None:
#         return 
#     for child in node.children:
#         post_order(child)
#     print(node.value,end=' ')


# root = TreeNode(1)
# node2 = TreeNode(2)
# node3 = TreeNode(3)
# node4 = TreeNode(4)
# node5 = TreeNode(5)
# node6 = TreeNode(6)
# node7 = TreeNode(7)
# # Build tree structure
# root.add_child(node2)
# root.add_child(node3)
# root.add_child(node4)
# node3.add_child(node5)
# node3.add_child(node6)
# node2.add_child(node7)
# # Run traversals
# print("Pre-order Traversal:")
# pre_order(root)
# print("\n")

# print("Post-order Traversal:")
# post_order(root)


# #------Binary Tree -------

# class Node:
#     def __init__(self,value):
#         self.value = value
#         self.left = None
#         self.right = None

# class BinaryTree:
#     def __init__(self):
#         self.root = None

#     def insert(self,value):
#         if not self.root:
#             self.root = Node(value)
#         else:
#             self.insert_recursive(self.root,value)

#     def insert_recursive(self,node,value):
#         if not node.left:
#             node.left = Node(value)
#         elif not node.right:
#             node.right = Node(value)
#         else:
#             self.insert_recursive(node.left,value)

# binarytree=BinaryTree()
# binarytree.insert(10)
# binarytree.insert(5)
# binarytree.insert(11)


# class BinarySearchTree:
#     def __init__(self):
#         self.root=None

#     def insert(self,value):
#         if not self.root:
#             self.root = Node(value)
#         else:
#             self.insert_recursive(self.root,value)

#     def insert_recursive(self,node,value):
#         if value < node.value:
#             if node.left:
#                 self.insert_recursive(node.left,value)
#             else:
#                 node.left = Node(value)
#         else:
#             if node.right:
#                 self.insert_recursive(node.right,value)
#             else:
#                 node.right = Node(value)

# binarysearchtree=BinarySearchTree()
# binarysearchtree.insert(100)
# binarysearchtree.insert(10) 

from collections import deque

class Node :
    def __init__(self,value):
        self.value = value 
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root:
            self.root = Node(value)
        else:
            self.insert_recursion(self.root,value)

    def insert_recursion(self,node,value):
        if not node.left:
            node.left = Node(value)
        elif not node.right:
            node.right = Node(value)
        else:
            self.insert_recursion(node.left,value)

class binarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        if not self.root :
            self.root = Node(value)
        else:
            self.insert_recursion(self.root,value)

    def insert_recursion(self,node,value):
        if value < node.value:
            if node.left:
                self.insert_recursion(node.left,value)
            else:
                node.left = Node(value)
        else:
            if node.right:
                self.insert_recursion(node.right,value)
            else:
                node.right = Node(value)
    
    def inorder(self,node): # left -> root -> right
        if node:
            self.inorder(node.left)
            print(node.value,end = ' ')
            self.inorder(node.right)
    
    def preorder(self,node): # root -> left -> right
        if node:
            print(node.value,end =' ')
            self.preorder(node.left)
            self.preorder(node.right)
    
    def postorder(self,node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.value,end=' ')

    def level_order(self):
        if not self.root:
            return 
        queue = deque()
        queue.append(self.root)
        
        while queue:
            node=queue.popleft()
            print(node.value,end = ' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    
    def search(self,value):
        return self.search_recursive(self.root,value)
    
    def search_recursive(self,node,value):
        if not node:
            return False
        if node.value == value:
            return True 
        if value < node.value:
            return self.search_recursive(node.left,value)
        else:
            return self.search_recursive(node.right,value)
    
    def delete(self,value):
        return self.delete_recursion(self.root,value)

    def delete_recursion(self,node,value):
        if not node:
            return node
        elif value < node.value:
            node.left = self.delete_recursion(node.left,value)
        elif value > node.value:
            node.right = self.delete_recursion(node.right,value)
        else:
            if not node.left and not node.right:
                return None
            elif not node.left:
                return node.right 
            elif not node.right :
                return node.left
            temp = self.find_min(node.right)
            node.value = temp.value
            node.right = self.delete_recursion(node.right,temp.value)
        return node
    
    def find_min(self,node):
        current = node
        while current.left:
            current = current.left
        return current
    
    def duplicate_remove(self):
        seen = set()
        return self.duplicate_delete(self.root,seen)

    def duplicate_delete(self,node,seen):
        if not node:
            return node
        node.left = self.duplicate_delete(node.left,seen)
        if node.value in seen :
            return self.delete_recursion(node,node.value)
        else:
            seen.add(node.value)

        node.right = self.duplicate_delete(node.right,seen)
        return node
        
    def height(self,node):
        if not node:
            return -1
        node_left=self.height(node.left)
        node_right=self.height(node.right)
        return 1 + max(node_left,node_right)
    
    def lowest_common_ancestor(self,node,p,q):
        if not node:
            return node
        if p < node.value and q < node.value:
            return self.lowest_common_ancestor(node.left,p,q)
        elif p > node.value and q > node.value:
            return self.lowest_common_ancestor(node.right,p,q)
        return node
    
    def k_th_smallest(self,k):
        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return 
            inorder(node.left)
            self.count += 1
            if self.count == k:
                self.result = node.value
            inorder(node.right)
        inorder(self.root)
        return self.result
    


def is_balanced(root):
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        if left == -1:
            return -1
        right = height(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return 1 + max(left,right)
    return height(root) != -1
def height_check(root):
    if not root:
        return -1
    left = height_check(root.left)
    right = height_check(root.right)
    return 1 + max(left,right)
def print_tree(node, level=0, prefix="Root: "):
    if node is not None:
        print("   " * level + prefix + str(node.value))
        if node.left or node.right:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def diameter(root):
    diameter = [0]
    def height(node):
        if not node:
            return 0
        left = height(node.left)
        right = height(node.right)

        diameter[0] = max(diameter[0],left+right)

        return 1 + max(left,right)
    height(root)
    return diameter[0]

tree=binarySearchTree()
tree.insert(10)
tree.insert(5)
tree.insert(15)
tree.insert(3)
tree.insert(8)
tree.insert(11)
tree.inorder(tree.root)
print()
tree.preorder(tree.root)
print()
tree.postorder(tree.root)
print()
tree.level_order()
print()
a=[1,10,2]
for i in a:
    tree.insert(i)
tree.inorder(tree.root)
print()
print(tree.search(10))
tree.delete(11)
tree.inorder(tree.root)
tree.duplicate_remove()
print()
tree.inorder(tree.root)
print()
print(tree.height(tree.root))
tree.preorder(tree.root)
print(is_balanced(tree.root))
print(height_check(tree.root))
print_tree(tree.root)
print(diameter(tree.root))
lca=tree.lowest_common_ancestor(tree.root,8,5)
print(lca.value)
print(tree.k_th_smallest(5))