*/
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Tress>Binary Search Tree : Lowest Common Ancestor
problem url:https://www.hackerrank.com/challenges/binary-search-tree-lowest-common-ancestor/problem
/*


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''

def lca(root, v1, v2):
    if root.info > v1 and root.info > v2:
        lca(root.left,v1,v2)
    elif root.info < v1 and root.info < v2:
        lca(root.right,v1,v2)
    else:
        print(root.info)
