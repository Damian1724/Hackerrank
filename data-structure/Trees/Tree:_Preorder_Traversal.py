/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree: Preorder Traversal
problem url: https://www.hackerrank.com/challenges/tree-preorder-traversal/problem
*/


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"FOR THESE PROBLEM THEY GAVE ME EVERYTHING I JUST HAD TO COMPLETE THE PREORDER METHOD AND I CREATE THE PRINT_TREE METHOD." 
"""
def preOrder(root):
    if root is not None:
        print_tree(root)
def print_tree(cur_node):
    if cur_node is not None:
        print(cur_node,end=" ")
        print_tree(cur_node.left)
        print_tree(cur_node.right)




        
