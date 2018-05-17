/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>linked lists > Insert a Node at the tail of a linked list.
problem url: https://www.hackerrank.com/challenges/insert-a-node-at-the-tail-of-a-linked-list/problem
*/


"""
 Insert Node at the end of a linked list 
 head pointer input could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node
 
 return back the head of the linked list in the below method
"""

def Insert(head, data):
    aux=head
    a=Node(data)
    if head==None:return a
    else:
        while head.next is not None:
            head=head.next
        head.next=a
        return aux
        
        
        
        
