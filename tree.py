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