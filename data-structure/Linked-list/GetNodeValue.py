/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >Get Node Value
problem url: https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail/problem
*/


#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

def GetNode(head, position):
    i=-1
    aux=head
    while aux.next is not None:
        i+=1
        aux=aux.next
    i+=1
    i=i-position
    j=-1
    while j < i:
        j+=1
        if j==i:return head.data
        head=head.next
        
        
    
