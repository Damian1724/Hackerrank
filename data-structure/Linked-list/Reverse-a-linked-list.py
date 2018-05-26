/*
Author: Damian Cruz
source: HackerRank(https://www.hackerrank.com)
problem name: Algorithms >Data Structures>Reverse a linked list
problem url: https://www.hackerrank.com/challenges/reverse-a-linked-list/problem
cost of the algorithm:N
*/


"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head == Node or head.next is None:return head
    output=Node(head.data)
    while head.next is not None:
        head=head.next
        aux=output
        add_node=Node(head.data)
        output=add_node
        output.next=aux
    head=output
    return add_node
    
