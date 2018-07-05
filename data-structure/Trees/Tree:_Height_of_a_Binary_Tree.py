/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures> Tree: Height of a Binary Tree
problem url: https://www.hackerrank.com/challenges/tree-height-of-a-binary-tree/problem
*/


# Enter your code here. Read input from STDIN. Print output to STDOUT
'''
class Node:
      def __init__(self,info): 
          self.info = info  
          self.left = None  
          self.right = None 
           

       // this is a node of the tree , which contains info as data, left , right
'''
def height(root):
    return height_rec(root) -1

def height_rec(root):
    if root is None:
        return 0
    return max(height_rec(root.left),height_rec(root.right))+1
