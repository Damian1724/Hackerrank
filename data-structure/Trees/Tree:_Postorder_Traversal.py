/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree: Postorder Traversal
problem url: https://www.hackerrank.com/challenges/tree-postorder-traversal/problem
*/


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def visiting_tree(cur_root):
    if cur_root is not None:
        visiting_tree(cur_root.left)
        visiting_tree(cur_root.right)
        print(cur_root, end=" ")
        
def postOrder(root):
    if root is not None:
        visiting_tree(root)
