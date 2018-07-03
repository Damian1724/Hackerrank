/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Tree: Level Order Traversal
problem url: https://www.hackerrank.com/challenges/tree-level-order-traversal/problem
*/


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""
def levelOrder(root):
    lista=[]
    lista.append(root)
    while len(lista)>0:
        if lista[0].left is not None:
            lista.append(lista[0].left)
        if lista[0].right is not None:
            lista.append(lista[0].right)
        print(lista[0].info,end=" ")
        lista.pop(0)
