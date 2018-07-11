/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Is This a Binary Search Tree?
problem url: https://www.hackerrank.com/challenges/is-binary-search-tree/problem
*/


""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def check_binary_search_tree_(root):
    lista=[]
    lista=going_over_tree(root,lista)
    for i in range(len(lista)-1):
        if lista[i] >= lista[i+1]:
            return False
    return True
    
def going_over_tree(root,lista):
    if root is not None: 
        going_over_tree(root.left,lista)
        lista.append(root.data)
        going_over_tree(root.right,lista)
    return lista
        
    
