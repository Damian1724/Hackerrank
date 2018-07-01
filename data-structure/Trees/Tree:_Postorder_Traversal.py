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
def visiting_tree(cur_root,lista):
    if cur_root is not None:
        lista.append(cur_root)
        visiting_tree(cur_root.left,lista)
        visiting_tree(cur_root.right,lista)
        print(cur_root, end=" ")
        
def postOrder(root):
    lista=[]
    if root is not None:
        visiting_tree(root,lista)
