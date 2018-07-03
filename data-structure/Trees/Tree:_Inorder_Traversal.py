/*
uthor: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree: Inorder Traversal
problem url: https://www.hackerrank.com/challenges/tree-inorder-traversal/problem
*/


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def inOrder(root):
    if root is not None:
        going_over_tree(root)
        
def going_over_tree(curr_node):
    if curr_node is not None:
        going_over_tree(curr_node.left)
        print(curr_node,end =" ")
        going_over_tree(curr_node.right)
