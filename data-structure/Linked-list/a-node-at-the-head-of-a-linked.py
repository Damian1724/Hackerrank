/*
uthor: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists >a-node-at-the-head-of-a-linked
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-head-of-a-linked-list/problem
*/


"""
 Insert Node at the begining of a linked list
 head input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method. 
"""

def Insert(head, data):
    aux=Node(data)
    if head is not None:
        aux.next=head
    return aux
            
        
    
    
